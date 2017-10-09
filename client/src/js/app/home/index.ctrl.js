(function(){
'use strict';

angular.module('demoApp.home')
    .controller('indexController', ['$mdSidenav', 'Geotag', 'alertServices', '$timeout', indexController]);

    function indexController ($mdSidenav, Geotag, alertServices, $timeout) {
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
                    //window.location = response.data;
                    vm.caption = '';
                    alertServices.showTopRightToast('Photo successfully uploaded.');
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
