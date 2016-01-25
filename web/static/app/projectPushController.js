myAppModule.controller('projectPushController', ["$scope", "$http","Util", function ($scope, $http,Util) {

    $scope.formData={}

    $scope.uploadSuccess=function(){
        console.log(arguments)
        alert(this)
    }

    $scope.uploadError=function(){
        console.log(arguments)
        alert(this)
    }


    $scope.push=function(){
        host=$scope.formData.pushserver.join(",")
        $http.get("/projectPush?host="+host+"&path="+$scope.formData.pushpath).success(function(data){
            console.log(data)
        }).error(function(data){
            console.log(data)
        })
    }

    $scope.pushAfter=function(){
        host=$scope.formData.pushserver.join(",")
        $http.get("/cmd?host="+host+"&cmd="+$scope.formData.execCmd).success(function(data){
            console.log(data)
        }).error(function(data){
            console.log(data)
        })
    }


}]);

