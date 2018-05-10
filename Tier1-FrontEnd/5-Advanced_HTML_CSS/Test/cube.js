$("body").keydown( e => {
   console.log(e.which);
   if (e.which == 80) {//p
      console.log("p");
      if ($("#controllable").css("animation-play-state") == "running") {
         $("#controllable").css("animation-play-state", "paused");
      }
      else {
         $("#controllable").css("animation-play-state", "running");
      }
   }

});
