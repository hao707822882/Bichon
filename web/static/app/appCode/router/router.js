/**
 * Created by Administrator on 2015/10/16.
 */
myAppModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.
        when('/disk', {
            templateUrl: '/static/app/template/monitor/disk.html',
            controller: 'diskController'
        }).when('/welcom', {
            templateUrl: '/static/app/template/monitor/welcom.html',
            controller: 'welcomeController'
        }).when('/mem', {
            templateUrl: '/static/app/template/monitor/mem.html',
            controller: 'memController'
        }).when('/cpu', {
            templateUrl: '/static/app/template/monitor/cpu.html',
            controller: 'cpuController'
        }).when('/net', {
            templateUrl: '/static/app/template/monitor/net.html',
            controller: 'indexViewController'
        }).when('/service', {
            templateUrl: '/static/app/template/monitor/service.html',
            controller: 'serviceController'
        }).when('/projectPush', {
            templateUrl: '/static/app/template/projectPush/projectPush.html',
            controller: 'indexViewController'
        }).when('/install', {
            templateUrl: '/static/app/template/monitor/install.html',
            controller: 'indexViewController'
        }).when('/security', {
            templateUrl: '/static/app/template/monitor/security.html',
            controller: 'indexViewController'
        }).when('/command', {
            templateUrl: '/static/app/template/monitor/command.html',
            controller: 'indexViewController'
        }).when('/server', {
            templateUrl: '/static/app/template/server/server.html',
            controller: 'indexViewController'
        }).when('/config', {
            templateUrl: '/static/app/template/config/config.html',
            controller: 'indexViewController'
        }).
        otherwise({
            redirectTo: '/disk'
        });
}])

