myAppModule.controller('serverController', ["$scope", "$http","Util", function ($scope, $http,Util) {
    $scope.formData={}

    var transform = function(data){
        return $.param(data);
    }

    $scope.addServer=function(){
        $http.post("/server/add",{host:$scope.formData.host,lab:$scope.formData.lab},{
            headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            transformRequest: transform
        }).success(function (data) {
            if(!data.error){
                layer.msg("success")}
            else{
                layer.msg("fail")
            }
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }


}]);

