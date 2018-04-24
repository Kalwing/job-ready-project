function moveISS () {
    $.getJSON('http://api.open-notify.org/iss-now.json?callback=?', function(data) {
        var lat = data['iss_position']['latitude'];
        var lon = data['iss_position']['longitude'];

        iss.setLatLng([lat, lon]);
        mymap.panTo([lat, lon], animate=true);
    });
    setTimeout(moveISS, 10000);
}


var mymap = L.map('mapid').setView([0, 0], 2);
L.tileLayer('https://map1.vis.earthdata.nasa.gov/wmts-webmerc/VIIRS_CityLights_2012/default/{time}/{tilematrixset}{maxZoom}/{z}/{y}/{x}.{format}', {
	attribution: 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
	bounds: [[-85.0511287776, -179.999999975], [85.0511287776, 179.999999975]],
	minZoom: 1,
	maxZoom: 8,
	format: 'jpg',
	time: '',
	tilematrixset: 'GoogleMapsCompatible_Level'
}).addTo(mymap);

var iss = L.marker([0, 0]).addTo(mymap);
moveISS();

$.getJSON('http://api.open-notify.org/astros.json?callback=?', data => {
    data['people'].forEach(function (d) {

         var str = "https://en.wikipedia.org/w/api.php"
                  + "?callback=?"
                  + "&action=query"
                  + "&format=json"
                  + "&prop=pageimages"
                  + "&titles="
                  + encodeURIComponent(d['name'].trim())
                  + "&pithumbsize=250";
         $.getJSON(str, pic => {
            for (var key in pic.query.pages){
               var img = pic.query.pages[key].thumbnail;
               console.log(pic);
               if (img == undefined) {
                  $('#names').append("<div class='item'><span>" + d['name']
                                    +"</span><div class='portrait'></div></div>");
               }
               else {
                  $('#names').append("<div class='item'><span>" + d['name']
                                    + "</span><div class='portrait'"
                                    + "style='background-image:url("
                                    + img.source
                                    + ");'><div></div>");
               }
            }
         });
    });
});
