myAppModule.controller('memController', ["$scope", "$http", function ($scope, $http) {
    $http.get("/mem/memInfo?host=127.0.0.1").success(function (data) {
        d = data.data
        $scope.memPrecent = d[2]
    }).error(function () {
        layer.msg("初始化诗句获取失败")
    })
}]);

