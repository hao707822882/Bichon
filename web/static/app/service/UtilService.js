/**
 * Created by Administrator on 2016/1/11.
 */
bootStrapModuleStarter.service("Util", function ($http) {
    return {
        eval: function (str) {
            return eval("(" + str + ")")
        },
        toArray: function (from, to) {
            var temp = [];
            for (var a = from; a <= to; a++) {
                temp.push(a)
                a++
            }
            return temp
        },
        get: function (url, success, error) {
            $http.get(url).success(success).error(error)
        }
    }
})