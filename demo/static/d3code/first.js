d3.selectAll('li').style('color', 'blue'); //All
d3.select("body").style("background-color", "#7EC0EE");
d3.select('li').style('color', 'red');  // Only first
d3.select('li:nth-child(3n)').style('color', 'green');  // 3rd one
d3.select('li:nth-child(odd)').style('color', 'white');  // first odd one
d3.selectAll('li:nth-child(even)').style('color', 'white')
.html("<p> EVEN</p>");  // even ones

var numArray = [12, 54, 45, 43, 78, 47, 43, 75, 56, 53, 24, 51, 33, 46, 53, 43, 41, 43]

d3.selectAll('li')
.data(numArray)
.enter().append("li").text(function(d){"This is extra data and has value " + d})
.text(function(d){
    return "This has value " +  d;
})
.style('font-size', function(d){return d + 'px'});