from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class snL4VirtualServer(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4VirtualServer'
    
    snL4VirtualServerName = None
    snL4VirtualServerVirtualIP = None
    snL4VirtualServerSDAType = None

    _properties = (
    {'id': 'snL4VirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerVirtualIP', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerSDAType', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4VirtualServers')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class snL4VirtualServer(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4VirtualServer'
    
    snL4VirtualServerName = None
    snL4VirtualServerVirtualIP = None
    snL4VirtualServerSDAType = None

    _properties = (
    {'id': 'snL4VirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerVirtualIP', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerSDAType', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4VirtualServers')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class snL4VirtualServer(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4VirtualServer'
    
    snL4VirtualServerName = None
    snL4VirtualServerVirtualIP = None
    snL4VirtualServerSDAType = None

    _properties = (
    {'id': 'snL4VirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerVirtualIP', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerSDAType', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4VirtualServers')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class snL4VirtualServer(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4VirtualServer'
    
    snL4VirtualServerName = None
    snL4VirtualServerVirtualIP = None
    snL4VirtualServerSDAType = None

    _properties = (
    {'id': 'snL4VirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerVirtualIP', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerSDAType', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4VirtualServers')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class snL4VirtualServer(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4VirtualServer'
    
    snL4VirtualServerName = None
    snL4VirtualServerVirtualIP = None
    snL4VirtualServerSDAType = None

    _properties = (
    {'id': 'snL4VirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerVirtualIP', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerSDAType', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4VirtualServers')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class snL4VirtualServer(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4VirtualServer'
    
    snL4VirtualServerName = None
    snL4VirtualServerVirtualIP = None
    snL4VirtualServerSDAType = None

    _properties = (
    {'id': 'snL4VirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerVirtualIP', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4VirtualServerSDAType', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4VirtualServers')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


