(function(){
'use strict';

angular.module('demoApp.home')
    .controller('indexController', ['$mdSidenav', 'Geotag', indexController]);

    function indexController ($mdSidenav, Geotag) {
        var vm = this;

        vm.initialize = initialize;
        vm.openCamera = openCamera;
        vm.closeSideNav = closeSideNav;

        vm.lastSideNavOpenId = '';

        vm.initialize();

        function initialize() {
            console.log('initialize called');
            document.getElementById('camera-input').addEventListener('change', photoChanged);
        }

        function openCamera() {
            console.log('open camera');
            $('#camera-input').trigger('click');
        }

        function photoChanged (e) {
            var fileInput = e.target.files;

            console.log('photoChanged: ', fileInput);

            if (!fileInput.length) return;

            Geotag.uploadItem(fileInput[0], vm.caption)
                .then(function(response){
                    console.log('response: ',response);
                    alert('Photo successfully uploaded.');
                    //var blob = new Blob([response.data]);
                    //var link = document.createElement('a');
                    //link.href = window.URL.createObjectURL(blob);
                    //link.download = '12311.kmz';
                    //link.click();
                    //window.location = response.data;
                }, function (error) {

                });
        }

        function closeSideNav(navID) {
            $mdSidenav(navID).close();
        }
    }
}());
