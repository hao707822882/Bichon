myAppModule.controller('installController', ["$scope", "$http","Util", function ($scope, $http,Util) {
    $scope.formData={}

    function  getInstallStatue(){
        $http.get("/install/check?host="+$scope.host.host,{timeout:5000}).success(function (data) {
            $scope.installs = data.data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }
    getInstallStatue()




    $scope.addServiceCheck=function(){
        $scope.formData["serverId"]=$scope.host.id
        var url=Util.getSerialize($scope.formData)
        $http.get("/service/add"+url).success(function (data) {
            $scope.data = data.data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }
}]);

