from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FoundryLB.Definition import *

class snL4RealServerMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(snL4RealServerDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpTableName = 'snL4RealServerEntry'
    snmpTableOID = '.1.3.6.1.4.1.1991.1.1.4.3.1.1'
    snmpIndexName = 'snL4RealServerIndex'
    snmpTitleName = 'snL4RealServerName'
    snmpMonitorName = 'snL4RealServerAdminStatus'
    snmpMonitorFlagExists = True
    
    snmpGetTableMaps = (
        GetTableMap(snmpTableName, snmpTableOID, {
            '.1': snmpIndexName,
            '.2': snmpTitleName,
            '.3': 'snL4RealServerIP',
            '.4': snmpMonitorName,
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
            om.setRealdevice = om.snL4RealServerIP
            if self.snmpMonitorFlagExists == True:
                if getattr(om, self.snmpMonitorName) == 0:
                    om.monitor = False
            rm.append(om)
        maps.append(rm)
        return maps

