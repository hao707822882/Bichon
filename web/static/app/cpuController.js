myAppModule.controller('cpuController', ["$scope", "$http", function ($scope, $http) {
    $http.get("/cpu/Info?host=127.0.0.1").success(function (data) {
        $scope.data = eval("("+data.data+")")
    }).error(function () {
        layer.msg("初始化诗句获取失败")
    })
}]);

