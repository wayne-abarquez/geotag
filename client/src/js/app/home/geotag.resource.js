(function(){
'use strict';

angular.module('demoApp.home')
    .factory('Geotag', ['Restangular', 'Upload', Geotag]);
    
    function Geotag (Restangular, Upload) {
        var myModel = Restangular.all('geotags');

        var resource = {
            uploadItem: function (_file, _caption, latlng) {
                var uploadUrl = myModel.getRestangularUrl() + '/upload',
                    caption = _caption || '';

                var params = {file: _file, caption: caption};

                if (latlng) {
                    params['lat'] = latlng['lat']
                    params['lng'] = latlng['lng']
                }

                return Upload.upload({
                    url: uploadUrl,
                    method: 'POST',
                    data: params
                });
            }
        };

        angular.merge(myModel, resource);

        return myModel;
    }
}());