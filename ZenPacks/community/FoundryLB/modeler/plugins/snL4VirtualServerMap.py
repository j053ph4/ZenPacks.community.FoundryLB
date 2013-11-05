from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FoundryLB.Definition import *

class snL4VirtualServerMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(snL4VirtualServerDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpTableName = 'snL4VirtualServerTable'
    snmpTableOID = '.1.3.6.1.4.1.1991.1.1.4.2.1.1'
    snmpIndexName = 'snL4VirtualServerIndex'
    snmpTitleName = 'snL4VirtualServerName'
    snmpMonitorName = 'snL4VirtualServerAdminStatus'
    snmpMonitorFlagExists = True
    
    snmpGetTableMaps = (
        GetTableMap(snmpTableName, snmpTableOID, {
            '.1': snmpIndexName,
            '.2': snmpTitleName,
            '.3': 'snL4VirtualServerVirtualIP',
            '.4': snmpMonitorName,
            '.5': 'snL4VirtualServerSDAType',
            '.6': 'snL4VirtualServerRowStatus',
            }),
        )

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get(self.snmpTableName)
        snmpindex = 1
        for trunk in trunktable.values():
            om = self.objectMap(trunk)
            name = "%s" % getattr(om, self.snmpTitleName)
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = getattr(om, self.snmpIndexName)
            om.ifindex = om.snmpindex
            om.setIpAddresses = [ getattr(om, 'snL4VirtualServerVirtualIP') ] 
            if self.snmpMonitorFlagExists == True:
                if getattr(om, self.snmpMonitorName) == 0:
                    om.monitor = False
            rm.append(om)
        maps.append(rm)
        return maps
