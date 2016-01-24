myAppModule.controller('projectPushController', ["$scope", "$http","Util", function ($scope, $http,Util) {

    $scope.uploadSuccess=function(){
        alert("success")
    }

    $scope.uploadError=function(){
        alert("fail")
    }


}]);

