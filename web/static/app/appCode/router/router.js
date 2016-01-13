/**
 * Created by Administrator on 2015/10/16.
 */
myAppModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.
        when('/disk', {
            templateUrl: '/static/app/template/monitor/disk.html',
            controller: 'indexViewController'
        }).when('/mem', {
            templateUrl: '/static/app/template/',
            controller: 'indexViewController'
        }).when('/cpu', {
            templateUrl: '/static/app/template/',
            controller: 'indexViewController'
        }).when('/net', {
            templateUrl: '/static/app/template/',
            controller: 'indexViewController'
        }).
        otherwise({
            redirectTo: '/index'
        });
}])

