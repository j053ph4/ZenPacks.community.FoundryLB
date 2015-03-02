from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *
from Products.ZenModel.IpInterface import *
from Products.ZenModel.IpAddress import *

ROOT = "ZenPacks.community"
BASE = "FoundryLB"
VERSION = Version(1, 5, 0)

RDATA = getBasicDefinitionData(VERSION, ROOT, BASE, 'snL4RealServer', 'L4 Real Server', 'L4 Real Servers')
RDATA['componentData']['displayed'] = 'snL4RealServerName'
RDATA['componentData']['primaryKey'] = 'snL4RealServerName'
RDATA['componentData']['properties']['snL4RealServerName'] = addProperty('snL4RealServerName')
RDATA['componentData']['properties']['snL4RealServerIP'] = addProperty('snL4RealServerIP')

snL4RealServerDefinition = type('snL4RealServerDefinition', (BasicDefinition,), RDATA)

addDefinitionDeviceRelation(snL4RealServerDefinition,
                          'realserver', ToMany, 'ZenPacks.community.FoundryLB.snL4RealServer','snL4RealServerIP',
                          'realdevice',  ToOne, 'Products.ZenModel.Device', 'manageIp',
                          "Zenoss Device")

def unsetBinds(ob):
    ob.binds._remoteRemove()
    ob.binds._remove()

def removeCustomRelations(ob):  ob.unsetBinds()

def updateCustomRelations(ob):  ob.unsetBinds()

def getVirtualIpLink(ob): return ob.getIpLink(ob.snL4VirtualServerVirtualIP)

def setCustomProp(ob, id, value):
    """
    Override from PerpertyManager to handle checks and ip creation
    """
    if id == 'ips':
        ob.setIpAddresses(value)
    if id == 'macaddress':
        ob.index_object()

def __init__(ob, id, title=None):
    IpInterface.__init__(ob, id, title)
    super(CustomComponent, ob).__init__(id, title)

snL4VirtualServerDefinition = type('snL4VirtualServerDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'snL4VirtualServer',
        'componentData' : {
                          'singular': 'L4 Virtual Server',
                          'plural': 'L4 VirtualServers',
                          'displayed': 'snL4VirtualServerName', # component field in Event Console
                          'primaryKey': 'snL4VirtualServerName',
                          'properties': {
                                        'snL4VirtualServerName' : addProperty('snL4VirtualServerName','Basic'),
                                        'snL4VirtualServerVirtualIP' : addProperty('snL4VirtualServerVirtualIP','Basic'),
                                        'snL4VirtualServerSDAType' : addProperty('snL4VirtualServerSDAType','Basic'),
                                        'getVirtualIpLink' : getReferredMethod('Virtual IP', 'getVirtualIpLink'),
                                        },
                          },
        'parentClasses' : [IpInterface],
        'componentMethods' : [__init__, getVirtualIpLink, unsetBinds, setCustomProp, removeCustomRelations, updateCustomRelations],
        })


snL4BindDefinition = type('snL4BindDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'snL4Bind',
        'componentData' : {
                          'singular': 'L4 Bind',
                          'plural': 'L4 Binds',
                          'properties': {
                                        'snL4BindRealServerName' : addProperty('snL4BindRealServerName','Basic'),
                                        'snL4BindVirtualServerName' : addProperty('snL4BindVirtualServerName','Basic'), 
                                        'snL4BindRealPortNumber' : addProperty('Real Port','Basic', optional=False, order=4),
                                        'snL4BindVirtualPortNumber' : addProperty('Virtual Port','Basic', optional=False, order=7),
                                        'snL4RealServerIP' : addProperty('snL4RealServerIP','Basic'),
                                        'snL4VirtualServerVirtualIP' : addProperty('snL4VirtualServerVirtualIP','Basic'),
                                       },
                          },
        'componentMethods' : [],
       })

addDefinitionSelfComponentRelation(snL4BindDefinition,
                          'binds', ToMany, 'ZenPacks.community.FoundryLB.snL4Bind','snL4BindRealServerName',
                          'realserver',  ToOne, 'ZenPacks.community.FoundryLB.snL4RealServer', 'snL4RealServerName',
                          "Real Server")

addDefinitionSelfComponentRelation(snL4BindDefinition,
                          'binds', ToMany, 'ZenPacks.community.FoundryLB.snL4Bind','snL4BindVirtualServerName',
                          'virtualserver',  ToOne, 'ZenPacks.community.FoundryLB.snL4VirtualServer', 'snL4VirtualServerName',
                          "Virtual Server")

addDefinitionDeviceComponentRelation(snL4BindDefinition,'manageIp', 'snL4RealServerIP',
                          'bind', ToOne, 'ZenPacks.community.FoundryLB.snL4Bind','snL4BindRealPortNumber',
                          'ipservice',  ToOne, 'Products.ZenModel.IpService', 'port',
                          'IP Service', 'snL4BindRealPortNumber')
