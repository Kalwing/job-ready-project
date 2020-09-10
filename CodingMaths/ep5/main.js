window.onload = function() {
	var canvas = document.getElementById("canvas"),
		context = canvas.getContext("2d"),
		width = canvas.width = window.innerWidth,
        height = canvas.height = window.innerHeight;
    var centerX = width / 2,
        centerY = height / 2,
        dx, dy,
        angle = 0;
    var offsetY = 40,
        offsetX = 60;
        
    render();
    
    function render() {
        context.clearRect(0, 0, width, height);
        
        drawEye(centerX - 250, centerY);
        drawEye(centerX + 250, centerY);
        requestAnimationFrame(render)
    }
    
    function drawEye(centerX, centerY) {
        context.beginPath();
        context.arc(
            centerX, 
            centerY - 70,
            150, Math.PI*.15, Math.PI*.85, false
        );
        context.arc(
            centerX, 
            centerY + 20,
            150, Math.PI*1.2, Math.PI*2, false
        );
        context.stroke();
        
        context.beginPath();
        context.arc(
            centerX + Math.cos(angle)*offsetX, 
            centerY + Math.sin(angle)*offsetY + 10,
            20, 0, Math.PI*2, false);
        context.fill();
     
    }
    
    document.body.addEventListener("mousemove", function(event) {
       dx = event.clientX - centerX;
       dy = event.clientY - centerY;
       angle = Math.atan2(dy, dx);
        
    });
  
};