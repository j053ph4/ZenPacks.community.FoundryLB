from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FoundryLB.Definition import *

SERVERSTATEMAP = {'serverdisabled': 0,
                  #'serverenabled': 1,
                  'serverfailed': 2,
                  'servertesting': 3,
                  'serversuspect': 4,
                  'servershutdown': 5,
                  #'serveractive': 6,
                  }

PORTSTATEMAP = {'disabled': 0,
                #'enabled' : 1,
                'failed': 2,
                #'testing': 3,
                #'suspect': 4,
                'shutdown': 5,
                #'active': 6,
                'unbound': 7,
                'awaitUnbind': 8,
                'awaitDelete': 9,
                }

class snL4BindMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(snL4BindDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpTableName = 'snL4BindEntry'
    snmpTableOID = '.1.3.6.1.4.1.1991.1.1.4.6.1.1'
    snmpIndexName = 'snL4BindIndex'
    snmpTitleName = 'snL4BindIndex'
    snmpMonitorName = ''
    snmpMonitorFlagExists = False
    
    snmpGetTableMaps = (
        # map of binds
        GetTableMap('snL4BindEntry', '.1.3.6.1.4.1.1991.1.1.4.6.1.1', {
            '.1': 'snL4BindIndex',
            '.2': 'snL4BindVirtualServerName',
            '.3': 'snL4BindVirtualPortNumber',
            '.4': 'snL4BindRealServerName',
            '.5': 'snL4BindRealPortNumber',
            '.6': 'snL4BindRowStatus',
            }),
        # map of real servers:
        GetTableMap('snL4RealServerEntry', '.1.3.6.1.4.1.1991.1.1.4.3.1.1', {
            '.1': 'snL4RealServerIndex',
            '.2': 'snL4RealServerName',
            '.3': 'snL4RealServerIP',
            '.4': 'snL4RealServerAdminStatus',
            }),
        # map of real server  status:
        GetTableMap('snL4RealServerStatusEntry', '.1.3.6.1.4.1.1991.1.1.4.8.1.1', {
            '.1': 'snL4RealServerStatusIndex',
            '.2': 'snL4RealServerStatusName',
            '.3': 'snL4RealServerStatusRealIP',
            '.9': 'snL4RealServerStatusState',
            }),  
        # map of virtual servers:
        GetTableMap('snL4VirtualServerTable', '.1.3.6.1.4.1.1991.1.1.4.2.1.1', {
            '.1': 'snL4VirtualServerIndex',
            '.2': 'snL4VirtualServerName',
            '.3': 'snL4VirtualServerVirtualIP',
            '.4': 'snL4VirtualServerAdminStatus',
            '.5': 'snL4VirtualServerSDAType',
            '.6': 'snL4VirtualServerRowStatus',
            }),
        # map of real server ports:
        GetTableMap('snL4RealServerPortEntry', '.1.3.6.1.4.1.1991.1.1.4.5.1.1', {
            '.1': 'snL4RealServerPortIndex',
            '.2': 'snL4RealServerPortServerName',
            '.3': 'snL4RealServerPortPort',
            '.4': 'snL4RealServerPortAdminStatus',
            }),
        # map of real server port status:
        GetTableMap('snL4RealServerPortStatusEntry', '.1.3.6.1.4.1.1991.1.1.4.10.1.1', {
            '.1': 'snL4RealServerPortStatusIndex',
            '.2': 'snL4RealServerPortStatusPort',
            '.3': 'snL4RealServerPortStatusServerName',
            '.5': 'snL4RealServerPortStatusState',
            }),        
        # map of virtual server ports:
        GetTableMap('snL4VirtualServerPortEntry', '.1.3.6.1.4.1.1991.1.1.4.4.1.1', {
            '.1': 'snL4VirtualServerPortIndex',
            '.2': 'snL4VirtualServerPortServerName',
            '.3': 'snL4VirtualServerPortPort',
            '.4': 'snL4VirtualServerPortAdminStatus',
            '.5': 'snL4VirtualServerPortSticky',
            }),
        )
    
    def mergeResults(self,data):
        master = {}
        bindtable = data.get('snL4BindEntry')
        realtable = data.get('snL4RealServerEntry')
        virtualtable = data.get('snL4VirtualServerTable')
        realporttable = data.get('snL4RealServerPortEntry')
        virtualporttable = data.get('snL4VirtualServerPortEntry')
        realstatustable = data.get('snL4RealServerStatusEntry')
        realportstatustable = data.get('snL4RealServerPortStatusEntry')
        master = bindtable.copy()
        for i in master.keys():
            realserver = master[i]['snL4BindRealServerName']
            realport = master[i]['snL4BindRealPortNumber']
            virtualserver = master[i]['snL4BindVirtualServerName']
            virtualport = master[i]['snL4BindVirtualPortNumber']
            for v in realtable.values():
                if realserver == v['snL4RealServerName']:
                    master[i].update(v)
            for v in virtualtable.values():
                if virtualserver == v['snL4VirtualServerName']:
                    master[i].update(v)
            for v in realporttable.values():
                if realserver == v['snL4RealServerPortServerName']:
                    if realport == v['snL4RealServerPortPort']:
                        master[i].update(v)
            for v in virtualporttable.values():
                if virtualserver == v['snL4VirtualServerPortServerName']:
                    if virtualport == v['snL4VirtualServerPortPort']:
                        master[i].update(v)
            for v in realstatustable.values():
                if realserver == v['snL4RealServerStatusName']:
                    master[i].update(v)
            for v in realportstatustable.values():
                if realserver == v['snL4RealServerPortStatusServerName']:
                    if realport == v['snL4RealServerPortStatusPort']:
                        master[i].update(v)
        return master
    
    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        master = self.mergeResults(tabledata)
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get(self.snmpTableName)
        for trunk in trunktable.values():
            om = self.objectMap(trunk)
            name = "%s_%s_%s_%s" % (om.snL4BindVirtualServerName, om.snL4BindVirtualPortNumber, 
                                    om.snL4BindRealServerName, om.snL4BindRealPortNumber)
            #name = "%s" % str(getattr(om, 'snL4BindIndex'))
            name = self.prepId(name)
            om.id = name
            om.title = name
            om.snmpindex = getattr(om, 'snL4BindIndex')
            om.setRealserver = om.snL4BindRealServerName
            om.setVirtualserver = om.snL4BindVirtualServerName
            om.setIpservice = om.snL4BindRealPortNumber
            statuses = ['snL4RealServerAdminStatus', 'snL4VirtualServerAdminStatus',
                        'snL4RealServerPortAdminStatus', 'snL4VirtualServerPortAdminStatus']
            for s in statuses:
                if getattr(om, s) == 0: om.monitor = False
            if getattr(om,'snL4RealServerStatusState') in SERVERSTATEMAP.values():  om.monitor = False
            if getattr(om,'snL4RealServerPortStatusState') in PORTSTATEMAP.values():  om.monitor = False
            rm.append(om)
        maps.append(rm)
        return maps
