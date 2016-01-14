/**
 * Created by Administrator on 2016/1/12.
 */
BootStrapStarter.directive("echartLine", function ($http) {
    return {
        restrict: 'EA',
        replace: true,
        scope: {"echartid": "@"},
        templateUrl: "/static/app/echart/template/echart.html",
        controller: function ($scope, $element, $attrs) {
            return true
        },
        link: function ($scope, $element, $attrs) {//加载数据
            //（1）是不是动态数据
            //（1-1）生成x轴，获取初始数据
            //生成X轴坐标
            function generate(length) {
                var now = new Date();
                var res = [];
                while (length--) {
                    res.unshift(now.toLocaleTimeString().replace(/^\D*/, ''));
                    now = new Date(now - 2000);
                }
                return res;
            }

            function getOption(lineLab, xLine, initDate) {
                return {
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
                    series: [initDate]
                }
            }


            var lineLab = eval("(" + $attrs.linetype + ")");


            var timeX = $attrs.timex;
            var timeXLength
            if (timeX) {//处理动态数据
                timeXLength = $attrs.timexlength;
                if (!timeXLength)
                    timeXLength = 30
                xLine = generate(timeXLength)
                initDate = (function (timeXLength) {
                    var res = [];
                    while (timeXLength--) {
                        res.push(0)
                    }
                    var temp = {}
                    temp.name = lineLab[0]
                    temp.type = "line"
                    temp.data = res
                    return temp;
                })(timeXLength)

                var chart = echarts.init($element[0]);
                chart.setOption(getOption(lineLab, xLine, initDate))
                setInterval(function () {
                    var axisData = (new Date()).toLocaleTimeString().replace(/^\D*/, '');
                    chart.addData([
                        [
                            0,        // 系列索引
                            Math.round(Math.random() * 1000), // 新增数据
                            false,     // 新增数据是否从队列头部插入
                            false,     // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
                            axisData
                        ]
                    ]);
                }, 1000);

            } else {//静态数据
                var initDate = []
                var initDataPath = $attrs.initdatapath
                var xLine = eval("(" + $attrs.xline + ")");//x坐标轴
                $http.get(initDataPath).success(function () {
                    $(arguments[0]).each(function (index) {
                        var temp = {}
                        temp.name = lineLab[index]
                        temp.type = "line"
                        temp.data = this
                        initDate.push(temp)
                    })
                    var chart = echarts.init($element[0]);
                    chart.setOption(getOption(lineLab, xLine, initDate))
                }).error(function () {
                    layer.msg("初始化诗句获取失败")
                })
            }


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
        templateUrl: "/static/app/echart/template/echart.html",
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
        templateUrl: "/static/app/echart/template/echart.html",
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




