/**
 * Created by Administrator on 2016/1/10.
 */
var BootStrapStarter = angular.module("bootstrap", []);

BootStrapStarter.directive("row", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/layer/row.html"
    }
})
BootStrapStarter.directive("col1", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/layer/col1.html"
    }
})


BootStrapStarter.directive("col2", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/layer/col2.html"
    }
})

BootStrapStarter.directive("col3", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/layer/col3.html"
    }
})

BootStrapStarter.directive("col4", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/layer/col4.html"
    }
})

BootStrapStarter.directive("col6", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/layer/col6.html"
    }
})
BootStrapStarter.directive("col12", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/layer/col12.html"
    }
})

/**
 *文字颜色标签
 */
BootStrapStarter.directive("colorSuccess", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("success")
        }
    }
})
BootStrapStarter.directive("colorInfo", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("info")
        }
    }
})
BootStrapStarter.directive("colorWarning", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("warning")
        }
    }
})
BootStrapStarter.directive("colorDanger", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("danger")
        }
    }
})
/**
 * 可用状态标签
 */
BootStrapStarter.directive("disabled", function () {
    return {
        restrict: 'A',
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("disabled")
        }
    }
})
/***
 * 背景颜色标签
 */
BootStrapStarter.directive("bgPrimary", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("bg-primary")
        }
    }
})
BootStrapStarter.directive("bgSuccess", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("bg-success")
        }
    }
})
BootStrapStarter.directive("bgDanger", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("bg-danger")
        }
    }
})
BootStrapStarter.directive("bgInfo", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("bg-info")
        }
    }
})


BootStrapStarter.directive("inline", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {//加载数据
            $element.css("display", "inline-block")
        }
    }
})


BootStrapStarter.directive("tableComponent", function () {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/app/bootstrap/template/tab/tab.html",
    }
})

/**
 * 排在一行
 */
BootStrapStarter.directive("formInlineHorizontal", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/form/formInlineHorizontal.html"
    }
})


/**
 * 上传控件
 */
BootStrapStarter.directive("myUpload", function () {
        return {
            restrict: 'E',
            replace: true,
            templateUrl: "/static/app/bootstrap/template/form/upload.html",
            link: function ($scope, $element, $attrs) {

                var id = $attrs.inputid
                var lab = $attrs.lab
                var name = $attrs.name
                var uploadPath = $attrs.uploadpath

                //上传element
                var label = $element.find("label")
                var input = $element.find("input")

                //设置上传配置
                function setUploadConfig(uploadPath, success, error) {
                    $.fn.upload.defaults = {
                        // 留空表示提交到当前页面
                        action: uploadPath,
                        // 头信息
                        headers: {},
                        // 传递额外数据（键值对字符串）
                        data: null,
                        // 留空表示默认读取表单文件的name值
                        name: "",
                        // 完成回调，无论成功还是失败
                        oncomplete: $.noop,
                        // 成功回调
                        onsuccess: function () {
                            $scope.$apply(function () {
                                success()
                            })
                        },
                        // 失败回调
                        onerror: function () {
                            $scope.$apply(function () {
                                error()
                            })
                        },
                        // 进度回调
                        onprogress: $.noop
                    };
                }

                //确信上传回调ok, 如果没有回调也要写个空的
                function enSureUploadCallBack() {
                    if (!$scope.uploadSuccess && !$scope.uploadError) {
                        alert("$scope.uploadSuccess && $scope.uploadError function must be defined!")
                    }
                }

                function init() {
                    enSureUploadCallBack()
                    label.attr("for", id)
                    label.text(lab)
                    input.attr("id", id)
                    input.attr("name", name)
                }
                init()
                //上传点击按钮
                $scope.auto_upload = function () {
                    setUploadConfig(uploadPath, $scope.uploadSuccess, $scope.uploadError)
                    $('#uploadProject').upload()
                }

            }
        }
    }
)


/**
 * input控件
 */
BootStrapStarter.directive("myInput", function () {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/app/bootstrap/template/form/input.html",
        link: function ($scope, $element, $attrs) {
            var id = $attrs.id
            var lab = $attrs.lab
            var type = $attrs.type
            var placeholder = $attrs.placeholder
            var name = $attrs.name

            function sureFoemData() {
                if (!$scope.formData) {
                    $scope.formData = {}
                }
            }

            function init() {
                sureFoemData()
                var label = $element.find("label")
                label.attr("for", id)
                label.text(lab)
                var input = $element.find("input")
                input.attr("id", id)
                input.attr("type", type)
                input.attr("placeholder", placeholder)
                input.attr("name", name)
                $element.find("input").on('blur keyup change', function () {
                    var element = this
                    $scope.$apply(function () {
                        var sf = $scope.formData;
                        sf[name] = $(element).val()
                    })
                });
            }

            //初始化input组件
            init()
        }
    }
})

/**
 * input控件
 */
BootStrapStarter.directive("myCheckbox", function () {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/app/bootstrap/template/form/checkBox.html",
        link: function ($scope, $element, $attrs, autoForm) {
            var id = $attrs.id
            var value = $attrs.value
            var lab = $attrs.lab
            var name = $attrs.name

            function sureFoemData() {
                //确认父容器的值容器
                if (!$scope.formData) {
                    $scope.formData = {}
                }
                //对选的容器
                if (!$scope.formData[name]) {
                    $scope.formData[name] = []
                }
            }

            function init() {
                sureFoemData()
                var label = $element.find("label")
                label.attr("for", id)
                label.text(lab)
                var input = $element.find("input")
                input.attr("id", id)
                input.attr("name", name)
                input.val(value)
                $element.find("input").on('click', function () {
                    var element = this
                    $scope.$apply(function () {
                        var sf = $scope.formData;
                        var needAdd = true
                        if (element.checked) {
                            for (var data in sf[name]) {
                                if (data == $(element).val()) {
                                    needAdd = false
                                }
                            }
                            if (needAdd)
                                sf[name].push($(element).val())
                        } else {
                            $($scope.formData[name]).each(function (index) {
                                if (this == $(element).val()) {
                                    //如果这个值存在于值域中则删除
                                    sf[name].splice(index, 1)
                                }
                            })
                        }
                    })
                });
            }

            init()
        }
    }
})


/**
 * input控件
 */
BootStrapStarter.directive("myRadio", function () {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/app/bootstrap/template/form/radio.html",
        link: function ($scope, $element, $attrs, autoForm) {
            var id = $attrs.id
            var value = $attrs.value
            var lab = $attrs.lab
            var name = $attrs.name

            function sureFoemData() {
                //确认父容器的值容器
                if (!$scope.formData) {
                    $scope.formData = {}
                }
            }

            function init() {
                sureFoemData()
                var label = $element.find("label")
                label.attr("for", id)
                label.text(lab)
                var input = $element.find("input")
                input.attr("id", id)
                input.attr("name", name)
                input.val(value)
                $element.find("input").on('click', function () {
                    var element = this
                    $scope.$apply(function () {
                        if (element.checked) {
                            var sf = $scope.formData
                            sf[name] = $(element).val()
                        }
                    })
                });
            }

            init()
        }
    }
})


/**
 * select控件
 */
BootStrapStarter.directive("mySelect", function () {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/app/bootstrap/template/form/select.html",
        link: function ($scope, $element, $attrs, autoForm) {
            var id = $attrs.id
            var lab = $attrs.lab
            var name = $attrs.name
            var option = eval("(" + $attrs.options + ")")//下拉列表项
            var multiple = $attrs.multiple//多选

            function sureFoemData() {
                //确认父容器的值容器
                if (!$scope.formData) {
                    $scope.formData = {}
                }
                if (multiple) {
                    if (!$scope.formData[name]) {
                        $scope.formData[name] = []
                    }
                }
            }

            function init() {
                sureFoemData()
                var label = $element.find("label")
                label.attr("for", id)
                label.text(lab)
                var select = $element.find("select")
                if (multiple) {
                    select.attr("multiple", true)
                }
                select.attr("id", id)
                select.attr("name", name)
                $(option).each(function () {
                    //创建option
                    select.append(
                        $("<option/>").attr("value", this.value).text(this.text).on('blur keyup change click', function () {
                            var selectOptions = select.find("option:selected")
                            $scope.$apply(function () {
                                var sf = $scope.formData;
                                var data = []
                                $(selectOptions).each(function () {
                                    data.push($(this).val())
                                })
                                sf[name] = data;
                            })
                        })
                    )
                })
            }

            init()
        }
    }
})


BootStrapStarter.directive("formHorizontal", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/form/formHorizontal.html"
    }
})


BootStrapStarter.directive("inputContainer", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/form/inputContainer.html"
    }
})

BootStrapStarter.directive("inputLab", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {"lab": "@", "id": "@"},
        templateUrl: "/static/app/bootstrap/template/form/inputLab.html"
    }
})

BootStrapStarter.directive("inputClass", function () {
    return {
        restrict: 'A',
        link: function ($scope, $element, $attrs) {//加载数据
            $element.addClass("form-control")
        }
    }
})

BootStrapStarter.directive("staticInput", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            id: "@",
            lab: "@"
        },
        templateUrl: "/static/app/bootstrap/template/form/inputStatic.html",
    }
})

BootStrapStarter.directive("btn", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/form/button.html",
    }
})


BootStrapStarter.directive("img", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            src: "@",
            alt: "@"
        },
        templateUrl: "/static/app/bootstrap/template/other/img.html              "
    }
})


BootStrapStarter.directive("dropdown", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            id: "@",
        },
        templateUrl: "/static/app/bootstrap/template/compent/dropdown/dropDown.html"
    }
})
BootStrapStarter.directive("dropDownItem", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/compent/dropdown/dropDownItem.html"
    }
})


BootStrapStarter.directive("dropDownSeparator", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/compent/dropdown/dropDownSeparator.html"
    }
})


BootStrapStarter.directive("buttonGroupHorizontal", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/compent/buttongroup/buttonGroup.html"
    }
})
BootStrapStarter.directive("buttonGroupVertical", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/compent/buttongroup/buttonGroupVertical.html"
    }
})

BootStrapStarter.directive("inputGroup", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            inputGroupAction: "&"
        },
        templateUrl: "/static/app/bootstrap/template/compent/inputgroup/inputGroup.html"
    }
})


/***
 * 导航栏
 */
BootStrapStarter.directive("navBootStrap", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/compent/nav/nav.html"
    }
})
BootStrapStarter.directive("navHeader", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            "lab": "@",
            "href": "@"
        },
        templateUrl: "/static/app/bootstrap/template/compent/nav/navHeader.html"
    }
})
BootStrapStarter.directive("navGeneralItemContainer", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/compent/nav/navGeneralItemContainer.html"
    }
})
BootStrapStarter.directive("navGeneralItem", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            "lab": "@",
            "navGeneralItemAction": "&"
        },
        templateUrl: "/static/app/bootstrap/template/compent/nav/navGeneralItem.html"
    }
})

BootStrapStarter.directive("navForm", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            "navFormInput": "=",
            "navFormAction": "&",
            "lab": "@"
        },
        templateUrl: "/static/app/bootstrap/template/compent/nav/navForm.html"
    }
})


BootStrapStarter.directive("navListDown", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            "lab": "@"
        },
        templateUrl: "/static/app/bootstrap/template/compent/nav/navListDown.html"
    }
})

BootStrapStarter.directive("navLeft", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {
            $element.addClass("navbar-left")
        }
    }
})
BootStrapStarter.directive("navRight", function () {
    return {
        restrict: 'A',
        replace: true,
        link: function ($scope, $element, $attrs) {
            $element.addClass("navbar-right")
        }
    }
})


BootStrapStarter.directive("pagination", function () {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/app/bootstrap/template/compent/pagination/pagination.html",
        link: function ($scope, $element, $attrs) {
            //初始化数据
            $scope.previousOk = false;
            $scope.nextOk = true
        }
    }
})

BootStrapStarter.directive("emblem", function () {
    return {
        restrict: 'E',
        replace: true,
        scope: {
            "num": "&",
        },
        templateUrl: "/static/app/bootstrap/template/emblem/emblem.html",
    }
})

BootStrapStarter.directive("progressBootStrap", function () {
    return {
        restrict: 'E',
        replace: true,
        scope: {
            "width": "@",
            "data": "@",
        },
        templateUrl: "/static/app/bootstrap/template/progress/progress.html",
    }
})

BootStrapStarter.directive("panel", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {
            "head": "@",
        },
        templateUrl: "/static/app/bootstrap/template/panel/panel.html",
    }
})

BootStrapStarter.directive("panelTable", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/panel/panelTable.html",
    }
})

BootStrapStarter.directive("panelListGroup", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/panel/panelListGroup.html",
    }
})

BootStrapStarter.directive("panelListGroupItem", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/panel/panelListGroupItem.html",

    }
})

/**
 * 对话框
 */
BootStrapStarter.directive("bootStrapDialog", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        scope: {dialogId: "@"},
        templateUrl: "/static/app/bootstrap/template/compent/dialog/dialog.html",
    }
})

BootStrapStarter.directive("dialogbody", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/compent/dialog/body.html"
    }
})
BootStrapStarter.directive("dialogfooter", function () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: "/static/app/bootstrap/template/compent/dialog/footer.html"
    }
})

/**
 * 点击交换状态
 */
BootStrapStarter.directive("swap", function ($http) {
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


/*BootStrapStarter.directive("tab", function () {
 return {
 restrict: 'E',
 replace: true,
 scope: {},
 templateUrl: "app/bootstrap/template/compent/table/table.html",
 link: function ($scope, $element, $attrs) {

 },
 controller: function ($scope, $element, $attrs) {
 $scope.paginations = ["1", "2", "3", "4", "5", "6"]
 $scope.click = function () {
 alert("controller")
 }
 }
 }
 })*/


