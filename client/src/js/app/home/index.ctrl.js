(function(){
'use strict';

angular.module('demoApp.home')
    .controller('indexController', ['$mdSidenav', 'Geotag', 'alertServices', '$timeout', '$http', indexController]);

    function indexController ($mdSidenav, Geotag, alertServices, $timeout, $http) {
        var vm = this;

        vm.showSpinner = false;

        vm.initialize = initialize;
        vm.openCamera = openCamera;
        vm.closeSideNav = closeSideNav;

        vm.lastSideNavOpenId = '';

        vm.initialize();

        function initialize() {
            document.getElementById('camera-input').addEventListener('change', photoChanged);
        }

        function openCamera() {
            console.log('open camera');
            $('#camera-input').trigger('click');
        }

        function photoChanged (e) {
            var fileInput = e.target.files;
            //console.log('photoChanged: ', fileInput);

            if (!fileInput.length) return;

            vm.showSpinner = true;

            Geotag.uploadItem(fileInput[0], vm.caption)
                .then(function(response){
                    console.log('response: ',response);
                    if (response.data.status == 'OK') {
                        vm.caption = '';
                        //window.location = response.data['geotag_url];
                        alertServices.showTopRightToast('Photo successfully uploaded.');
                    } else {
                        $http({
                            method: 'POST',
                            url: 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBU2IhITO_ygNUan5ortuYxJc6idxrsFlE',
                            data: {'considerIp': 'true'}
                        }).then(function(response){
                            console.log('geolocation result: ',response);

                            if (response.status != 200) return;

                            Geotag.uploadItem(fileInput[0], vm.caption, {lat: response.data.location.lat, lng: response.data.location.lng})
                                .then(function (resp) {
                                    if (resp.data.status == 'OK') {
                                        vm.caption = '';
                                        alertServices.showTopRightToast('Photo successfully uploaded.');
                                    }
                                });
                        });
                    }
                }, function (error) {
                    console.log('error: ',error);
                }).finally(function(){
                    $timeout(function(){
                        vm.showSpinner = false;
                    }, 500);
                });
        }

        function closeSideNav(navID) {
            $mdSidenav(navID).close();
        }
    }
}());
