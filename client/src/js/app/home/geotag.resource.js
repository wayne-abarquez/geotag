(function(){
'use strict';

angular.module('demoApp.home')
    .factory('Geotag', ['Restangular', 'Upload', Geotag]);
    
    function Geotag (Restangular, Upload) {
        var myModel = Restangular.all('geotags');

        var resource = {
            uploadItem: function (_file, _caption) {
                var uploadUrl = myModel.getRestangularUrl() + '/upload',
                    caption = _caption || '';

                return Upload.upload({
                    url: uploadUrl,
                    method: 'POST',
                    data: {file: _file, caption: caption}
                });
            }
        };

        angular.merge(myModel, resource);

        return myModel;
    }
}());