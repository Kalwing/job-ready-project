//MAP HANDLING
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
moveISS(mymap, iss);

//PEOPLE HANDLING
$.getJSON('http://api.open-notify.org/astros.json?callback=?', data => {
   //Get all the cosmonauts names
    data['people'].forEach(d => {
      var newPerson = {name: d['name']}

      //Url asking the pageImage info of the cosmonaut
      var urlImg = "https://en.wikipedia.org/w/api.php"
               + "?callback=?"
               + "&action=query"
               + "&format=json"
               + "&prop=pageimages"
               + "&titles="
               + encodeURIComponent(d['name'].replace(" ","_"))
               + "&pithumbsize=250";

      $.getJSON(urlImg, pic => {
         for (var key in pic.query.pages){
            if (pic.query.pages[key].thumbnail != undefined) {
               newPerson.img = pic.query.pages[key].thumbnail.source;
            } else {
               newPerson.img = undefined;
            }
            //Add the person to the page
            addPerson(newPerson);
         }
      });

   });
});


/* Position the ISS on the map
 * Preconditions :
 *    Take a leaflet map, and a leaflet marker
 */
function moveISS(map, marker) {
    $.getJSON('http://api.open-notify.org/iss-now.json?callback=?', function(data) {
        var lat = data['iss_position']['latitude'];
        var lon = data['iss_position']['longitude'];

        marker.setLatLng([lat, lon]);
        map.panTo([lat, lon], animate=true);
    });
    setTimeout( () => { moveISS(map, marker); }, 10000);
}

/* Add this person to the page.
 * Preconditions :
 *    Take an object person such that person.name contain his name,
 *    and person.img an url pointing to his picture.
 */
function addPerson(person) {
   var html = ""
   if (person.name != undefined) {
      html += "<div class='item'><span>" + person.name
                        + "</span><div class='portrait'";
      if (person.img != undefined) {
         html += "style='background-image:url("
                           + person.img
                           + ");";
      }
      html += "'><div></div>";
      $('#names').append(html);
   }
}
