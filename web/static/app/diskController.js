myAppModule.controller('diskController', ["$scope", "$http", function ($scope, $http) {
    console.log($scope.host)
    $http.get("/fileSystem/partitonInfo?host="+$scope.host.host,{timeout:5000}).success(function (data) {
        $scope.data = data
    }).error(function () {
        layer.msg("初始化诗句获取失败")
    })
}]);

