myAppModule.controller('cpuController', ["$scope", "$http", "$timeout",function ($scope, $http,$timeout) {
    $http.get("/cpu/Info?host="+$scope.host.host,{timeout:5000}).success(function (data) {
        $scope.data = eval("("+data.data+")")
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
        if($scope.flag=="cpu"){
            getProcessDAta()
        }
    },10000)

}]);

