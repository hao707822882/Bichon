myAppModule.controller('securityController', ["$scope", "$http","Util", function ($scope, $http,Util) {
    $scope.formData={}

    function  getIptableStatue(){
        $http.get("/iptable/statue?host="+$scope.host.host,{timeout:5000}).success(function (data) {
            $scope.security = data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }
    getIptableStatue()


    function getIptableList(){
        $http.get("/iptable/list?host="+$scope.host.host,{timeout:5000}).success(function (data) {
            $scope.iptables = data.data
        }).error(function () {
            layer.msg("初始化诗句获取失败")
        })
    }

    getIptableList()

    $scope.close=function(){
        ipOrPort=$scope.formData.ipport
        if(ipOrPort.length>6){
            $http.get("/iptable/add?host="+$scope.host.host+"&type=ip&data="+ipOrPort,{timeout:5000}).success(function (data) {
                if(data.error){
                    layer.msg("fail")
                }else{
                    layer.msg("success")
                }
            }).error(function () {
                layer.msg("初始化诗句获取失败")
            })
        }else {
            $http.get("/iptable/add?host="+$scope.host.host+"&type=port&data="+ipOrPort,{timeout:5000}).success(function (data) {
                if(data.error){
                    layer.msg("fail")
                }else{
                    layer.msg("success")
                }
            }).error(function () {
                layer.msg("初始化诗句获取失败")
            })
        }
    }

    $scope.antivirus=function(){
        console.log($scope.formData)
    }

    $scope.delete=function(chain,index){
       if(confirm("delete ok?")){
           $http.get("/iptable/delete?host="+$scope.host.host+"&chain="+chain+"&index="+index,{timeout:5000}).success(function (data) {
               if(data.data){
               layer.msg("success")}
               else{
                   layer.msg("fail")
               }
           }).error(function () {
               layer.msg("初始化诗句获取失败")
           })
       }
    }

}]);

