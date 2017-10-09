(function () {
    'use strict';

    angular
        .module('demoApp', [
            'ngMaterial',
            'ngAnimate',
            'restangular',
            'oitozero.ngSweetAlert',
            'ngFileUpload',
            'demoApp.home'
        ])

        .constant('APP_NAME', 'Demo App')
        .constant('BASE_URL', window.location.origin)

        .config(['RestangularProvider', function (RestangularProvider) {
            //set the base url for api calls on our RESTful services
            RestangularProvider.setBaseUrl(window.location.origin + '/api');
        }])

        .config(function ($mdThemingProvider) {
            $mdThemingProvider.theme('default')
                .primaryPalette('red')
                .accentPalette('pink');
        });

}());

