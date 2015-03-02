
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
    }
    
    ZC.snL4BindPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'snL4Bind',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "getIpserviceLink"
                    }, 
                    {
                        "name": "getRealserverLink"
                    }, 
                    {
                        "name": "getVirtualserverLink"
                    }, 
                    {
                        "name": "snL4BindRealPortNumber"
                    }, 
                    {
                        "name": "snL4BindVirtualPortNumber"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "IP Service", 
                        "renderer": "pass_link", 
                        "id": "getIpserviceLink", 
                        "dataIndex": "getIpserviceLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Real Server", 
                        "renderer": "pass_link", 
                        "id": "getRealserverLink", 
                        "dataIndex": "getRealserverLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Virtual Server", 
                        "renderer": "pass_link", 
                        "id": "getVirtualserverLink", 
                        "dataIndex": "getVirtualserverLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Real Port", 
                        "renderer": "pass_link", 
                        "id": "snL4BindRealPortNumber", 
                        "dataIndex": "snL4BindRealPortNumber"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Virtual Port", 
                        "renderer": "pass_link", 
                        "id": "snL4BindVirtualPortNumber", 
                        "dataIndex": "snL4BindVirtualPortNumber"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.snL4BindPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('snL4BindPanel', ZC.snL4BindPanel);
    ZC.registerName('snL4Bind', _t('L4 Bind'), _t('L4 Binds'));
    
    })();

