  
    <script src="js/js/modernizr-latest.js"></script> 
    <script type='text/javascript' src='js/js/jquery.min.js'></script>
    <script type='text/javascript' src='js/js/fancybox/jquery.fancybox.pack.js'></script>
    
    <script type='text/javascript' src='js/js/jquery.mobile.customized.min.js'></script>
    <script type='text/javascript' src='js/js/jquery.easing.1.3.js'></script> 
    <script type='text/javascript' src='js/js/camera.min.js'></script> 
     
    
    
    <script>
        jQuery(function(){
            
            jQuery('#camera_wrap_4').camera({
                height: '600',
                loader: 'bar',
                pagination: false,
                thumbnails: false,
                hover: false,
                opacityOnGrid: false,
                imagePath: 'img/'
            });

        });
    </script>