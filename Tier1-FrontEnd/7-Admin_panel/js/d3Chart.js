function draw (data) {
   var margin = 30,
      width = $(".UserChartPanel").width() - margin,
      height = $(".UserChartPanel").height() - margin;
   var mainLine = d3.select(".UserChartPanel")
               .append("svg")
               .attr("class","mainLine")
               .attr("height", height)
               .attr("width", width)
               .style("font-size", "0.5em")



   var time_extent = d3.extent(data, row => {
      return row['date'];
   });
   var value_extent = d3.extent(data, row => {
      return row['value'];
   });

   var time_scale = d3.time.scale()
                     .range([margin, width])
                     .domain(time_extent)
   var value_scale = d3.scale.linear()
                     .range([height, margin])
                     .domain(value_extent)

   var time_axis = d3.svg.axis()
                     .scale(time_scale)
                     .ticks(d3.time.month,Math.floor(40*(data.length/width)));
   //This seems to be a good formula for spacing the ticks. Mostly by trial and
   //Error though.

   var value_axis = d3.svg.axis()
                     .scale(value_scale)
                     .orient("left");
   var area = d3.svg.area()
            .x(function(d) { return time_scale(d["date"]); })
            .y0(height)
            .y1(function(d) { return value_scale(d["value"]); });
   var line = d3.svg.line()
            .x(function(d) { return time_scale(d["date"]); })
            .y(function(d) { return value_scale(d["value"]); });

   var mainGradient = mainLine.append('linearGradient')
       .attr('id', 'mainGradient')
       .attr('gradientTransform', "rotate(90)");

   // Create the stops of the main gradient. Each stop will be assigned
   // a class to style the stop using CSS.
   mainGradient.append('stop')
       .attr('class', 'stop-left')
       .attr('offset', '0');

   mainGradient.append('stop')
       .attr('class', 'stop-right')
       .attr('offset', '1');

   d3.select(".mainLine")
      .append('g')
      .attr('class', 'x axis')
      .attr('transform', "translate(0,"+(height)+")")
      .call(time_axis);
   d3.select(".mainLine")
      .append('g')
      .attr('class', 'y axis')
      .attr('transform', "translate("+margin+", 0)")
      .call(value_axis);
   d3.select(".mainLine")
      .append("path")
      .datum(data)
      .attr("class", "line")
      .attr("fill", "none")
      .attr("stroke", "url(#mainGradient)")
      .attr("stroke-width", 1.5)
      .attr("d", line);
   d3.select(".mainLine")
      .append("path")
      .datum(data)
      .attr("class", "area")
      .attr("d", area);
}

format = d3.time.format("%Y-%m-%d");
userByTime.forEach(row => {
   row['date'] = format.parse(row['date']);
   row['value'] = +row["value"];
});

draw(userByTime);
window.addEventListener("resize", draw);
