myAppModule.controller('configController', ["$scope", "$http","Util", function ($scope, $http,Util) {
    $scope.formData={}

    function  getConfig(){
        $http.get("/getConfig?host="+$scope.host.host+"&path=/1.TXT",{timeout:5000}).success(function (data) {
            $scope.data = data.data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }
    getConfig()

}]);

