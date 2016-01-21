myAppModule.controller('serviceController', ["$scope", "$http", function ($scope, $http) {
    $http.get("/service/statue").success(function (data) {
        $scope.data = data.data
    }).error(function () {
        layer.msg("初始化诗句获取失败")
    })
}]);

