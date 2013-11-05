
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
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
                        "header": "IP Service", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getIpserviceLink", 
                        "dataIndex": "getIpserviceLink"
                    }, 
                    {
                        "header": "Real Server", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getRealserverLink", 
                        "dataIndex": "getRealserverLink"
                    }, 
                    {
                        "header": "Virtual Server", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getVirtualserverLink", 
                        "dataIndex": "getVirtualserverLink"
                    }, 
                    {
                        "header": "Real Port", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "snL4BindRealPortNumber", 
                        "dataIndex": "snL4BindRealPortNumber"
                    }, 
                    {
                        "header": "Virtual Port", 
                        "width": 120, 
                        "sortable": "true", 
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
    ZC.registerName('snL4Bind', _t('snL4 Bind'), _t('snL4 Binds'));
    
    })();

