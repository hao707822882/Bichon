myAppModule.controller('serviceController', ["$scope", "$http","Util", function ($scope, $http,Util) {
    $scope.formData={}

    function  getProcessDAta(){
        $http.get("/service/statue?serverId="+$scope.host.id,{timeout:5000}).success(function (data) {
            $scope.data = data.data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }
    getProcessDAta()


    setInterval(function(){
        if($scope.flag=="service"){
            getProcessDAta()
        }

    },10000)

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

