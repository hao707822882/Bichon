/**
 * Created by Administrator on 2015/10/21.
 */
UIStarter.service("import", function ($window) {//自动导入服务
    return {
        autoImport: function (mudelName) {
            if (!mudelName || mudelName == "")
                return;
            if (!$window[mudelName]) {

            }
        }
    }
})

UIStarter.service("serialize", function () {//自动导入服务
    return {
        getSerialize: function (mudelName) {
            var searchUrl = "";
            for (name in mudelName) {
                if (mudelName[name] && mudelName[name] != "") {
                    searchUrl += name + "=" + mudelName[name] + "&"
                }
            }
            return "?" + searchUrl
        }
    }
})

UIStarter.service("layer", function () {
    return {
        topTip: function (msg) {
            layer.msg(msg, {
                offset: 0,
                shift: 6
            });
        }
    }
})


