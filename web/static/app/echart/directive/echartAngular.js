/**
 * Created by Administrator on 2016/1/12.
 */
BootStrapStarter.directive("echartLine", function ($http) {
    return {
        restrict: 'EA',
        replace: true,
        scope: { "echartid": "@"},
        templateUrl: "app/echart/template/echart.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            alert($element.attr("id"))
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
                layer.msg("初始化诗句获取失败")
            })
        }
    }
})

BootStrapStarter.directive("echartPie", function ($http) {
    return {
        restrict: 'EA',
        replace: true,
        scope: {
            "echartid": "@"
        },
        templateUrl: "app/echart/template/echart.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            alert($element.attr("id"))
            var initDataPath = $attrs.initdatapath
            $scope.width = Number($attrs.width)
            $scope.heigth = Number($attrs.heigth)
            var pieItems = []
            var pieName = $attrs.piename
            var initDate = [];

            $http.get(initDataPath).success(function () {
                initDate = arguments[0].result
                $(initDate).each(function (index, data) {
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
                layer.msg("初始数据句获取失败")
            })
        }
    }
})


BootStrapStarter.directive("echartGraph", function ($http) {
    return {
        restrict: 'EA',
        replace: true,
        scope: {"echartid": "@"},
        templateUrl: "app/echart/template/echart.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            alert($element.attr("id"))
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
                layer.msg("初始数据句获取失败")
            })
        }
    }
})




