window.onload = function() {
	var canvas = document.getElementById("canvas"),
		context = canvas.getContext("2d"),
		width = canvas.width = window.innerWidth,
        height = canvas.height = window.innerHeight;
    var centerY = .5*height,
        centerX = .5*width,
        axisY = .4*height,
        axisX = .4*height,
        speedY = .05,
        speedX = .065,
        angleX = 0,
        angleY = 0;

    render();
    
    function render() {
        var y = centerY + Math.sin(angleY) * axisY,
            x = centerX + Math.cos(angleX) * axisX;
        
        // context.clearRect(0, 0, width, height);
        context.beginPath();
        context.arc(x, y, 10, 0, Math.PI*1.75, false);
        context.fill();
        
        angleY += speedY;
        angleX += speedX;
        requestAnimationFrame(render);
    }
};