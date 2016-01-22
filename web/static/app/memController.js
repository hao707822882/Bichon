myAppModule.controller('memController', ["$scope", "$http","$timeout", function ($scope, $http,$timeout) {

    $scope.order=

    $http.get("/mem/memInfo?host="+$scope.host.host).success(function (data) {
        d = data.data
        $scope.memPrecent = d[2]
    }).error(function () {
        layer.msg("初始化诗句获取失败")
    })


    function getProcessDAta(){
        $http.get("/allProcesses/detail?host="+$scope.host.host,{timeout:5000}).success(function (data) {
            $scope.processes = data.data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }
    getProcessDAta()
    setInterval(function(){
        if($scope.flag=="mem"){
            getProcessDAta()
        }

    },10000)


}]);

