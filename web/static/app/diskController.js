myAppModule.controller('diskController', ["$scope", "$http", function ($scope, $http) {
    console.log($scope.host)
    $http.get("/fileSystem/partitonInfo?host=127.0.0.1").success(function (data) {
        $scope.data = data
    }).error(function () {
        layer.msg("初始化诗句获取失败")
    })
}]);

