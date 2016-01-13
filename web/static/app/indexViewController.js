/**
 * Created by Administrator on 2015/10/16.
 */
myAppModule.controller('indexViewController', ["$scope", "Util", function ($scope, Util) {
    $scope.saveData = {}
    $scope.upload = function () {
        $('#file').upload();
    }

    $scope.submitBGM = function () {
        Util.create("/admin/addBGM", $scope.saveData, function () {
            Util.topTip("新增成功！")
        }, function () {
            Util.topTip("新增成功！")
        })
    }

}]);