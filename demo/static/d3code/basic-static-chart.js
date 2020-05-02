var dataArray = [
{
	'background': '#FF9933',
	'color': 'white',
	'width': 95
},
{
	'background': 'yellow',
	'color': 'black',
	'width': 90
},
{
	'background': 'black',
	'color': 'pink',
	'width': 80
},
{
	'background': 'cyan',
	'color': 'black',
	'width': 70
},
{
	'background': 'green',
	'color': 'white',
	'width': 55
},
{
	'background': 'grey',
	'color': 'white',
	'width': 41
},
{
	'background': 'brown',
	'color': 'white',
	'width': 32
},
{
	'background': 'black',
	'color': 'pink',
	'width': 46
},
{
	'background': 'blue',
	'color': 'white',
	'width': 49
},
{
	'background': 'magenta',
	'color': 'white',
	'width': 82
}
]

d3.selectAll('li')
.data(dataArray)
.style('font-size', '18px')
.style('padding', '6px')
.style('margin', '4px')
.style('list-style', 'none')
.style('background', function(obj){
	return obj.background;
})
.style('color', function(obj){
	return obj.color;
})
.style('width', function(obj){
	return obj.width + '%';
});