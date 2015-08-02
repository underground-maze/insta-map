$(document).ready(function () {

    function init_map() {
        // Create the map.
        var mapOptions = {
            zoom: 10,
            center: new google.maps.LatLng(43.296944, 34.029444),
            mapTypeId: google.maps.MapTypeId.SATELLITE,

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

    function init_mini_map(lat, lon, zoom) {
        // Create the map.
        var position = new google.maps.LatLng(lat, lon);
        var mini_map_options = {
            zoom: zoom,
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
            label = messages.site_name + ' {coord}';

        $modal.find('iframe#youtube_video').attr('src', card.video);
        $modal.find('div[name="description"]').text(card.description);
        $modal.find('#card-info-label').text(label.replace('{coord}', card.latitude + ', ' + card.longitude));
        // change url
        window.history.pushState(messages.site_name, label, messages.card_url.replace('{id}', card_id));
        // open modal
        $('#card-info').modal('show');
        $('#share-vk').attr('href', 'https://vk.com/share.php?url=' + encodeURIComponent(location.href) + '&image=' + encodeURIComponent(card.thumb));
        $('#share-twitter').attr('href', 'https://twitter.com/intent/tweet?url='
            + encodeURIComponent(location.href) + '&text=' + (messages.site_name + card.description).slice(0, 100) + '...');
        $('#share-facebook').attr('href', 'https://www.facebook.com/dialog/feed?app_id=834251373317741&link='
            + encodeURIComponent(location.href) + '&picture=' + encodeURIComponent(card.thumb) + '&redirect_uri=' + encodeURIComponent(location.href));

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

    function get_position(position){
        init_mini_map(position.coords.latitude, position.coords.longitude, 13);
        var coords = '(' + position.coords.latitude + ', ' + position.coords.longitude + ')';
        $('#add-card').find('input[name="position"]').val(coords)
    }

    function no_position(error){
        init_mini_map(43.296944, 34.029444, 3);
    }

    $('#add-card').on('shown.bs.modal', function(){
        $.geolocation.get({win: get_position, fail: no_position});
    });

    $('#card-info').on('hidden.bs.modal', function(){
        $('.modal#card-info').find('iframe#youtube_video').attr('src', 'https://www.youtube.com/embed/');
    });

    init_map();
});
