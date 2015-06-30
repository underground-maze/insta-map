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

        var bounds = new google.maps.LatLngBounds();
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
                bounds.extend(marker.position);
                google.maps.event.addListener(marker, 'click', function() {
                    open_modal(marker.card_id);
                });
            }
        );

        var cluster = new MarkerClusterer(map, markers);
        map.fitBounds(bounds);

        // after map initialize try open modal
        modal_from_get(map);
    };

    function init_mini_map() {
        // Create the map.
        var position = new google.maps.LatLng(0, 0);
        var mini_map_options = {
            zoom: 3,
            center: position,
            mapTypeControl: true,
            zoomControl: true,
            panControl: true,
            scaleControl: true,
            streetViewControl: false,
        };
        var marker = new google.maps.Marker({
            position: position,
            draggable: true,
        });


        var mini_map = new google.maps.Map(document.getElementById('mini-map-canvas'), mini_map_options);

        marker.setMap(mini_map);

        google.maps.event.addListener(marker, 'dragend', function() {
            $('#add-card').find('input[name="position"]').val(marker.position)
        });

        var circle = new google.maps.Circle({
            center: position,
            map: mini_map,
            radius: 5000,
            strokeColor: "#AAAAAA", strokeOpacity: 0.8, strokeWeight: 2,
            fillColor: '#EEEEEE', fillOpacity: 0.3,
        });
        circle.bindTo('center', marker, 'position');

    };

    function open_modal(card_id){
        var card = cards[card_id];

        var $modal = $('.modal#card-info'),
            label = 'Я первооткрыватель {coord}';
        $modal.find('iframe').attr('src', card.video);
        $modal.find('div[name="description"]').text(card.description);
        $modal.find('#card-info-label').text(label.replace('{coord}', card.latitude + ', ' + card.longitude));
        // change url
        window.history.pushState('Я первооткрыватель', label, '?card={id}'.replace('{id}', card_id));
        // open modal
        $('#card-info').modal('show');

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
            // cet map center to point
            var bounds = new google.maps.LatLngBounds();
            bounds.extend(new google.maps.LatLng(position[0], position[1]));
            map.fitBounds(bounds);
        }
    }

    $('#add-card-link').click(function(){
        $('#add-card').modal('show');
    });

    $('#add-card').on('shown.bs.modal', function(){
        init_mini_map();
    });

    init_map();
});
