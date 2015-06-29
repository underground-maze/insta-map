$(document).ready(function () {

    function init_map() {
        // Create the map.
        var mapOptions = {zoom: 10, center: new google.maps.LatLng(44.654675, 33.771838)};

        var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

        var fog_of_war = {
            strokeColor: '#AAAAAA', strokeOpacity: 0.3, strokeWeight: 15,
            fillColor: '#EEEEEE', fillOpacity: 0.9,
            map: map,
            paths: polygons
        };
        cityCircle = new google.maps.Polygon(fog_of_war);

        // add markers events
        markers.forEach(
            function(marker){
                google.maps.event.addListener(marker, 'click', function() {
                    open_modal(marker);
                });
            }
        );

        var cluster = new MarkerClusterer(map, markers);
    };

    function open_modal(marker){
        var $modal = $('.modal#card-info'),
            label = 'Я первооткрыватель {coord}';
        // insert values
        $modal.find('iframe').attr('src', marker.video);
        $modal.find('div[name="description"]').text(marker.description);
        $modal.find('#card-info-label').text(label.replace('{coord}', marker.position));
        // open modal
        $('#open-modal').click();
    };

    init_map();
});
