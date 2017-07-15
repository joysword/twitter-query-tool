/**
 * Created by joysword on 6/18/17.
 */

$(window).resize(function () {
    var h = $(window).height(),
      offsetTop = 150; // Calculate the top offset

    $('#map').css('height', (h - offsetTop));
}).resize();

var map = L.map('map', {center: [41.8910,-87.8839], zoom: 9});

L.tileLayer('https://api.tiles.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoiam95c3dvcmQiLCJhIjoiSmJYSVNnUSJ9.is_i8oSQtofgH31ZkIMBgA')
    .addTo(map);

var circleMarkerOptions = {
    radius: 5,
    stroke: false,
    fill: true,
    fillColor: 'red',
    fillOpacity: 0.1
};

var place_layer = L.featureGroup;
var tweet_layer = L.featureGroup;

// place_id = '1d9a5370a355ab0c'; // Chicago
// place_id = '8b351eeb91372dc7';  // Evaston

function update_layer(data) {
    var layer = L.geoJSON(data);
    map.addLayer(layer);

    // resize map if the checkbox is checked

    if ($('#input-resize-map')[0].checked) {
        // console.log('here');
        map.fitBounds(layer.getBounds());
    }

    return layer;
}

function update_info(data) {
    var table = $('#table-result');
    table.empty();
    for (var key in data) {
        console.log(key);
        table.append('<tr><td>'+key+'</td><td>'+data[key]+'</td></tr>');
    }
}


// place id
$('#button-place-id').click(function(e) {
    e.preventDefault();
    // console.log('here');
    // if (map.hasLayer(place_layer)) {
    map.removeLayer(place_layer);
    console.log('removed place');
    //}

    var place_id = $('#input-place-id').val();

    $.getJSON('get/place', { "id": place_id }, function (data) {
        place_layer = update_layer(data);
        update_info(data.properties);
    });
});


// tweet id
$('#button-tweet-id').click(function(e) {
    e.preventDefault();

    if (map.hasLayer(tweet_layer)) {
        map.removeLayer(tweet_layer);
        console.log('removed tweet');
    }
    var tweet_id = $('#input-tweet-id').val();

    $.getJSON('get/tweet', { "id": tweet_id }, function (data) {
        tweet_layer = update_layer(data);
        update_info(data.properties);
    });
})

// an interface with a map and a canvas for returned textual values and a control panel

// control panel includes (for now):
// pick a user id to retrieve its information
// pick a user id to retrieve its recent tweets and show locations on map (when applicable)
// pick a place id to retrieve its information and show bounding box on map
// pick a hashtag to retrieve all recent tweets

