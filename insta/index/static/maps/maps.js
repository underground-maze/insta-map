$(document).ready(function () {

    function init_map() {
        // Create the map.
        var mapOptions = {
            zoom: 10,
            center: new google.maps.LatLng(44.654675, 33.771838),

            mapTypeControl: true,
            mapTypeControlOptions: {
                style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
                position: google.maps.ControlPosition.LEFT_CENTER
            },

            zoomControl: true,
            zoomControlOptions: {
                style: google.maps.ZoomControlStyle.DEFAULT,
                position: google.maps.ControlPosition.LEFT_CENTER
            },

            panControl: true,
            panControlOptions: {
                position: google.maps.ControlPosition.LEFT_CENTER
            },

            scaleControl: true,
            streetViewControl: false,
        };

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
                    open_modal(marker.card_id);
                });
            }
        );

        var cluster = new MarkerClusterer(map, markers);

        // after map initialize try open modal
        modal_from_get(map);
    };

    function open_modal(card_id){
        var card = cards[card_id];

        var $modal = $('.modal#card-info'),
            label = 'Я первооткрыватель {coord}';
        $modal.find('iframe').attr('src', card.video);
        $modal.find('div[name="description"]').text(card.description);
        $modal.find('#card-info-label').text(label.replace('{coord}', card.latitude + ', ' + card.longitude));
        $('#open-modal').click();

        return [card.latitude, card.longitude];
    };

    function get(name){
        if (name = (new RegExp('[?&]' + encodeURIComponent(name) + '=([^&]*)')).exec(location.search))
            return decodeURIComponent(name[1]);
    }

    function modal_from_get(map){
        // if url has get parametr `?card=<id>` open modal
        var card = get('card');
        if (card && cards[card]) {
            var position = open_modal(card);
            map.setZoom(17);
            map.setCenter(new google.maps.LatLng(position[0], position[1]));
        }
    }

    init_map();
});
