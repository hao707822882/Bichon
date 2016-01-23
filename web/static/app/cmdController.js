myAppModule.controller('commandController', ["$scope", "$http","$sce","Util", function ($scope, $http,$sce,Util) {

    $scope.formData={}

    $scope.actionCmd=function(){
        $http.get("/cmd?host="+$scope.host.host+"&cmd="+$scope.formData.cmd,{timeout:5000}).success(function (data) {
            $scope.data = data.data
            $scope.data.msg=$scope.data.msg.replace(/\n/g,"<br/>")
            $scope.data.msg=$sce.trustAsHtml($scope.data.msg);
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }

}]);

