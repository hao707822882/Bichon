myAppModule.controller('configController', ["$scope", "$http","Util", function ($scope, $http,Util) {
    $scope.formData={}

    var transform = function(data){
        return $.param(data);
    }


    $scope.getConfig=function (){
        $http.get("/getConfig?host="+$scope.formData.server[0]+"&path="+$scope.formData.configPath,{timeout:5000}).success(function (data) {
            $scope.data = data.data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }

    $scope.update=function(){
        textdata=$("#text").val()
        $http.post("/updateConfig",{host:$scope.formData.server[0],data:textdata,path:$scope.formData.configPath},{
            headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            transformRequest: transform
        }).success(function (data) {
            $scope.data = data.data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }

    $scope.execCmd=function(){
        host=$scope.formData.server[0]
        $http.get("/cmd?host="+host+"&cmd="+$scope.formData.execCmd).success(function(data){
            console.log(data)
        }).error(function(data){
            console.log(data)
        })
    }

}]);

