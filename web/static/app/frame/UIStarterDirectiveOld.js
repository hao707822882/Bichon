/**
 * Created by Administrator on 2015/10/21.
 */
UIStarter.directive("tab", function ($http, $window, layer, serialize) {
    var baseUrl = "";
    return {
        restrict: 'E',
        replace: true,
        scope: {},
        templateUrl: "app/directive/table/table.html",
        controller: function ($scope, $element, $attrs) {
            baseUrl = $attrs.url;
            $scope.querys = eval("(" + $attrs.querys + ")");
            $scope.ths = eval("(" + $attrs.ths + ")");
            $scope.labs = eval("(" + $attrs.labs + ")");
            $scope.search = {};
            $scope.update = $attrs.update && $scope.ths.push({'lab': '更新'});
            $scope.delete = $attrs.delete && $scope.ths.push({'lab': '删除'});
            $scope.Fsearch = function () {
                $http.get(baseUrl + serialize.getSerialize($scope.search)).success(function () {
                    $scope.data = arguments[0]
                }).error(function () {
                    layer.topTip("查询数据失败")
                })
            }
            $scope.Fdelete = function (date) {
                if (!$window.confirm("！确认删除该数据"))
                    return;
                $http.delete(baseUrl + "/" + date.id).success(function () {
                    $scope.data = arguments[0];
                    layer.topTip("删除成功")
                }).error(function () {
                    layer.topTip("删除失败")
                })
            }
            $scope.Fupdate = function (date) {
                $scope.updateDate = angular.copy(date);
                $('#myModal').modal('show')
            }

            function update() {
                $http.post($attrs.url + "/" + $scope.updateDate.id, $scope.updateDate, {"headers": "Content-Type"}).success(function () {
                    layer.topTip("更新数据成功！")
                    $scope.data = arguments[0]
                    $('#myModal').modal("hide")
                }).error(function () {
                    layer.topTip("更新数据失败")
                })
            }

            $scope.DoFupdate = function () {
                update();
            }
        },
        link: function ($scope, $element, $attrs) {//加载数据
            $http.get($attrs.url).success(function () {
                $scope.data = arguments[0];
            }).error(function () {
                layer.topTip("加载数据失败")
            })
        }
    }
})


UIStarter.directive("autoForm", function ($http, $window, layer, serialize) {
    var baseUrl = "";
    return {
        restrict: 'E',
        replace: true,
        scope: {},
        templateUrl: "app/directive/form/autoForm.html",
        controller: function ($scope, $element, $attrs) {
            baseUrl = $attrs.url;
            $scope.inputs = eval("(" + $attrs.inputs + ")");
            $scope.data = {};
            $scope.fSave = function () {
                console.log($scope.data)
                $http.put($attrs.url, $scope.data).success(function () {
                    layer.topTip("更新保存成功！")
                    $scope.data = arguments[0]
                }).error(function () {
                    layer.topTip("更新保存失败")
                })
            }
        }
    }
})
/**
 *参数：
 *  remote=null（本地）/url
 *  menu=[{name:"",child=[{name:"",url:""}]}]
 *  scope参数：menuSub是当前子菜单的数据
 *
 */
UIStarter.directive("headerMenu", function ($http, layer) {
    return {
        restrict: 'E',
        replace: true,
        scope: {},
        templateUrl: "app/directive/header/headerMenu.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            remoteUrl = $attrs.remote

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
            }

            $scope.$evalAsync(function () {
                window.location.href = "/index.html#/save"
            })

        }
    }
})

/***
 * 点击交换状态
 */
UIStarter.directive("swap", function ($http, layer) {
    return {
        restrict: 'A',
        replace: true,
        scope: {},
        link: function ($scope, $element, $attrs) {//点击改变状态
            $element.click(function () {
                $(this).siblings().removeClass("active");
                $(this).addClass("active")
            })
        }
    }
})


UIStarter.directive("echartLine", function ($http, layer) {
    return {
        restrict: 'EA',
        replace: true,
        scope: {},
        templateUrl: "app/directive/chart/echart.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            var initDataPath = $attrs.initdatapath
            $scope.width = Number($attrs.width)
            $scope.heigth = Number($attrs.heigth)
            var xLine = eval("(" + $attrs.xline + ")");
            var lineLab = eval("(" + $attrs.linetype + ")");
            var initDate = [];

            $http.get(initDataPath).success(function () {
                $(arguments[0]).each(function (index) {
                    var temp = {}
                    temp.name = lineLab[index]
                    temp.type = "bar"
                    temp.data = this
                    initDate.push(temp)
                })
                option1 = {
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        data: lineLab
                    },
                    calculable: true,
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: true,
                            data: xLine
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            splitArea: {show: true}
                        }
                    ],
                    series: initDate
                }
                var chart = echarts.init($element[0]);
                chart.setOption(option1)
            }).error(function () {
                layer.topTip("初始化诗句获取失败")
            })
        }
    }
})

UIStarter.directive("echartPie", function ($http, layer) {
    return {
        restrict: 'EA',
        replace: true,
        scope: {},
        templateUrl: "app/directive/chart/echart.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            var initDataPath = $attrs.initdatapath
            $scope.width = Number($attrs.width)
            $scope.heigth = Number($attrs.heigth)
            var pieItems = []
            var pieName = $attrs.piename
            var initDate = [];

            $http.get(initDataPath).success(function () {
                initDate = arguments[0]
                $(arguments[0]).each(function (index, data) {
                    pieItems.push(data.name)
                })
                option = {
                    tooltip: {
                        trigger: 'item',
                        formatter: "{a} <br/>{b} : {c} ({d}%)"
                    },
                    legend: {
                        orient: 'vertical',
                        x: 'left',
                        data: pieItems
                    },
                    calculable: true,
                    series: [
                        {
                            name: pieName,
                            type: 'pie',
                            radius: ['50%', '70%'],
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: false
                                    },
                                    labelLine: {
                                        show: false
                                    }
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        position: 'center',
                                        textStyle: {
                                            fontSize: '30',
                                            fontWeight: 'bold'
                                        }
                                    }
                                }
                            },
                            data: initDate
                        }
                    ]
                };

                var chart = echarts.init($element[0]);
                chart.setOption(option)
            }).error(function () {
                layer.topTip("初始数据句获取失败")
            })
        }
    }
})


UIStarter.directive("echartGraph", function ($http, layer) {
    return {
        restrict: 'EA',
        replace: true,
        scope: {},
        templateUrl: "app/directive/chart/echart.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            var initDataPath = $attrs.initdatapath
            $scope.width = Number($attrs.width)
            $scope.heigth = Number($attrs.heigth)
            var graphname = $attrs.name//图名字
            var initDate = [];//关系数据
            var node = []//节点

            $http.get(initDataPath).success(function () {
                initDate = arguments[0] //关系数据
                $(initDate).each(function (index, data) {
                    var item1 = {}
                    var item2 = {}
                    item1.name = data.source
                    item1.value = 5
                    item2.name = data.target
                    item2.value = 5
                    node.push(item1)
                    node.push(item2)
                })
                option = {
                    title: {
                        text: graphname,
                        x: 'right',
                        y: 'bottom'
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a} : {b}'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            restore: {show: true},
                            magicType: {show: true, type: ['force', 'chord']},
                            saveAsImage: {show: true}
                        }
                    },

                    series: [
                        {
                            type: 'force',
                            name: graphname,
                            ribbonType: false,
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        textStyle: {
                                            color: '#333'
                                        }
                                    },
                                    nodeStyle: {
                                        brushType: 'both',
                                        borderColor: 'rgba(255,215,0,0.4)',
                                        borderWidth: 1
                                    },
                                    linkStyle: {
                                        type: 'curve'
                                    }
                                },
                                emphasis: {
                                    label: {
                                        show: false
                                        // textStyle: null      // 默认使用全局文本样式，详见TEXTSTYLE
                                    },
                                    nodeStyle: {
                                        //r: 30
                                    },
                                    linkStyle: {}
                                }
                            },
                            useWorker: false,
                            minRadius: 15,
                            maxRadius: 25,
                            gravity: 1.1,
                            scaling: 1.1,
                            roam: 'move',
                            nodes: node,
                            links: initDate
                        }
                    ]
                };

                var chart = echarts.init($element[0]);
                chart.setOption(option)
            }).error(function () {
                layer.topTip("初始数据句获取失败")
            })
        }
    }
})



