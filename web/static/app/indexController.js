myAppModule.controller('indexController', ["$scope", function ($scope) {
    $scope.formData={}

    $scope.show = function () {
        console.log($scope)
    }
    $scope.say = function () {
        console.log("xxxx")
    }

}]);

