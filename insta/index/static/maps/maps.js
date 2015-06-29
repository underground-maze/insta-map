function initialize() {
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
                var marker_info =
                    'position: ' + marker.position + '\n' +
                    'description: ' + marker.description + '\n' +
                    'video: ' + marker.video;
                alert(marker_info);
            });
        }
    );

    var cluster = new MarkerClusterer(map, markers);

}

google.maps.event.addDomListener(window, 'load', initialize);
