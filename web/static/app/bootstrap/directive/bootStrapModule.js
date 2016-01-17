/**
 * Created by Administrator on 2016/1/11.
 */
var bootStrapModuleStarter = angular.module("bootStrapModule", ["bootstrap"]);
bootStrapModuleStarter.service("Util", function ($http) {
    return {
        eval: function (str) {
            return eval("(" + str + ")")
        },
        toArray: function (from, to) {
            var temp = [];
            for (var a = from; a <= to; a++) {
                temp.push(a)
            }
            return temp
        },
        get: function (url, success, error) {
            $http.get(url).success(success).error(error)
        },
        create: function (url, data, success, error) {
            $http.post(url, data).success(success).error(error)
        },
        update: function (url, data, success, error) {
            $http.put(url, data).success(success).error(error)
        },
        delete: function (url, success, error) {
            $http.delete(url).success(success).error(error)
        },
        getSerialize: function (mudelName) {
            var searchUrl = "";
            for (name in mudelName) {
                if (mudelName[name] && mudelName[name] != "") {
                    searchUrl += name + "=" + mudelName[name] + "&"
                }
            }
            return "?" + searchUrl
        },
        topTip: function (msg) {
            layer.msg(msg, {
                offset: 0,
                shift: 6
            });
        },
        scope: function (ele) {
            return angular.element(ele).scope();
        },
        showDialog: function (id) {
            if (!id)
                $('#myModal').modal('show')
            else
                $('#' + id).modal('show')
        },
        hiddenDialog: function (id) {
            if (!id)
                $('#myModal').modal('hide')
            else
                $('#' + id).modal('hide')
        }
    }
})

bootStrapModuleStarter.directive("needUpdate", function () {
    return {
        restrict: 'A',
        link: function ($scope, $element, $attrs) {
            $scope.needUpdate = true;
        }
    }
})
bootStrapModuleStarter.directive("needDelete", function () {
    return {
        restrict: 'A',
        link: function ($scope, $element, $attrs) {
            $scope.needDelete = true;
        }
    }
})
bootStrapModuleStarter.directive("needPagination", function () {
    return {
        restrict: 'A',
        link: function ($scope, $element, $attrs) {
            $scope.needPagination = true;
        }
    }
})
bootStrapModuleStarter.directive("needSearchForm", function () {
    return {
        restrict: 'A',
        link: function ($scope, $element, $attrs) {
            $scope.needSearhForm = true;
        }
    }
})
bootStrapModuleStarter.directive("needTableTool", function () {
    return {
        restrict: 'A',
        link: function ($scope, $element, $attrs) {
            $scope.needTableTool = true;
        }
    }
})

bootStrapModuleStarter.directive("tableModule", function ($http, Util) {
        return {
            restrict: 'E',
            replace: true,
            scope: true,
            templateUrl: "/static/app/bootstrap/module/table/tableModule.html",
            controller: function ($scope, $element, $attrs) {
                function paginations(now, total) {
                    if (total > 10) {
                        if (now == 1) {
                            return Util.toArray(1, 10)
                        } else if (now == total) {
                            return Util.toArray(total - 10, total)
                        } else {
                            if (now - 5 > 0 && now + 5 <= total) {
                                return Util.toArray(now - 4, now + 5)
                            } else if (now - 5 < 0) {
                                return Util.toArray(1, 10)
                            } else if (now - 5 == 0) {
                                return Util.toArray(1, now + 5)
                            } else if (now + 5 > total) {
                                return Util.toArray(total - 10, total)
                            }
                        }
                    }
                    else {
                        return Util.toArray(1, total)
                    }
                }

                //初始化th数据
                $scope.ths = Util.eval($attrs.ths)

                //判断来源
                $scope.url = $attrs.url
                //数据更新url
                $scope.updateUrl = $attrs.update
                //数据删除url
                $scope.deleteUrl = $attrs.delete
                //数据查询URL
                $scope.searchUrl = $attrs.search
                //初始化now
                $scope.now = 1
                //初始化检索字段属性
                $scope.searchs = Util.eval($attrs.searchs);
                //检索ng-model绑定字段
                $scope.searchData = {}
                //更新数据
                $scope.updateData = {}

                $scope.targetTrItem

                $scope.showPaginations = function (show) {
                    $scope.needPagination = show
                }
                $scope.showSearhForm = function (show) {
                    $scope.needSearhForm = show
                }
                $scope.showTableTool = function (show) {
                    $scope.needTableTool = show
                }
                $scope.showUpdate = function (show) {
                    $scope.needUpdate = show
                }
                $scope.showDelete = function (show) {
                    $scope.needDelete = show
                }


                //初始化数据
                $scope.initData = function () {
                    Util.get($scope.url, function (data) {
                        $scope.paginations = paginations(1, data.pages)
                        $scope.trs = data.data
                    }, function () {
                        Util.topTip("数据获取失败！")
                    })
                }

                /**
                 * 数据重置
                 */
                $scope.tableToolRest = function () {
                    $scope.showPaginations(true)
                    $scope.initData();
                }

                //分页获取
                $scope.paginationAction = function (index, nowpage) {
                    $scope.now = nowpage
                    url = $scope.url + "?pager=" + nowpage
                    Util.get(url, function (data) {
                        $scope.paginations = paginations(nowpage, data.pages)
                        $scope.trs = data.data
                    }, function () {
                        Util.topTip("数据获取失败！")
                    })
                }
                //更新
                $scope.update = function (data, ele) {
                    $scope.targetTrItem = ele
                    $scope.updateData = angular.copy(data);
                    Util.showDialog()
                }
                //删除
                $scope.delete = function (data, btn) {
                    if (!window.confirm("！确认删除该数据"))
                        return;
                    var deleteUrl = $scope.deleteUrl + "/" + data.id;
                    Util.delete(deleteUrl, function (data) {
                        $(btn).parents("tr").remove();
                        Util.topTip("删除成功")
                    }, function () {
                        Util.topTip("删除失败")
                    })
                }

                /**
                 * 对话框取消按钮
                 */
                $scope.dialogCancel = function () {
                    Util.hiddenDialog()
                }

                /**
                 * 对话框成功按钮
                 */
                $scope.dialogOk = function () {
                    var url = $scope.updateUrl;
                    Util.update(url, $scope.updateData, function (data) {
                        Util.topTip("更新成功！")
                    }, function () {
                        Util.topTip("更新失败！")
                    })
                    var targetScope = angular.element($scope.targetTrItem).scope();
                    targetScope.tr = $scope.updateData
                    Util.hiddenDialog()
                }

                //检索方法
                $scope.search = function (element) {
                    console.log($scope.searchData)
                    url = $scope.searchUrl + Util.getSerialize($scope.searchData)
                    Util.get(url, function () {
                        $scope.trs = data.data
                        $scope.showPaginations(false)
                    }, function () {
                        Util.topTip("检索数据失败")
                    })
                }

                $scope.initData()

            }
        }
    }
)


bootStrapModuleStarter.directive("headerMenu", function ($http) {
    return {
        restrict: 'E',
        replace: true,
        scope: {
            "logo": "@"
        },
        templateUrl: "/static/app/bootstrap/module/header/headerMenuModule.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            remoteUrl = $attrs.remote
            $scope.indexUrl = $attrs.index
            var menu;
            if (remoteUrl) {
                $http.get(initDataPath).success(function () {

                }).error(function () {
                    layer.topTip("初始化诗句获取失败")
                })
            } else {
                menu = eval("(" + $attrs.menu + ")");
            }

            var ms = []
            var msSub = []
            $(menu).each(function (index, data) {
                ms.push(data.name)
                msSub.push(data.child)
            })
            $scope.menus = ms//主菜单
            $scope.menuSub = msSub[0]//默认为第一个的子菜单

            $scope.menuClick = function (index) {//更换当前的子菜单
                $scope.menuSub = msSub[index]
                $scope.menuSub[0].url
                window.location.href = "/static/index.html#/" + $scope.menuSub[0].url
            }

            $scope.hosts = ["127.0.0.1", "127.0.0.12", "127.0.0.13", "127.0.0.14"]

            $scope.host=$scope.hosts[0]

            $scope.changHost = function (host) {
                $scope.host = host

            }

            $scope.$evalAsync(function () {
                window.location.href = "/static/index.html#/" + $scope.menuSub[0].url
            })


        }
    }
})
