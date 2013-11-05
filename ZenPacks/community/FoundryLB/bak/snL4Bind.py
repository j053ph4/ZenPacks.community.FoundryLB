from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class snL4Bind(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4Bind'
    
    snL4BindVirtualPortNumber = None
    snL4BindRealServerName = None
    snL4BindVirtualServerName = None
    snL4BindRealPortNumber = None

    _properties = (
    {'id': 'snL4BindVirtualPortNumber', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindVirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealPortNumber', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4Binds')),
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

class snL4Bind(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4Bind'
    
    snL4BindVirtualPortNumber = None
    snL4BindRealServerName = None
    snL4BindVirtualServerName = None
    snL4BindRealPortNumber = None

    _properties = (
    {'id': 'snL4BindVirtualPortNumber', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindVirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealPortNumber', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4Binds')),
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

class snL4Bind(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4Bind'
    
    snL4BindVirtualPortNumber = None
    snL4BindRealServerName = None
    snL4BindVirtualServerName = None
    snL4BindRealPortNumber = None

    _properties = (
    {'id': 'snL4BindVirtualPortNumber', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindVirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealPortNumber', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4Binds')),
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

class snL4Bind(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4Bind'
    
    snL4BindVirtualPortNumber = None
    snL4BindRealServerName = None
    snL4BindVirtualServerName = None
    snL4BindRealPortNumber = None

    _properties = (
    {'id': 'snL4BindVirtualPortNumber', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindVirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealPortNumber', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4Binds')),
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

class snL4Bind(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'snL4Bind'
    
    snL4BindVirtualPortNumber = None
    snL4BindRealServerName = None
    snL4BindVirtualServerName = None
    snL4BindRealPortNumber = None

    _properties = (
    {'id': 'snL4BindVirtualPortNumber', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindVirtualServerName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'snL4BindRealPortNumber', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'snL4Binds')),
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

