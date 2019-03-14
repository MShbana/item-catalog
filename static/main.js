
$(document).ready(function() {

    var $wrapper = $("#wrapper");
    var $genresToggler = $("#sidebar-toggler");
    var $navbarCollapse = $(".navbar-collapse");


    $genresToggler.on("click", function(e) {
        e.preventDefault();
        $(this).blur();

        // Collapse or display sidebar when genre toggler is clicked.
        $wrapper.toggleClass("toggled");

        // Collapse top navbar when sidebar toggler is clicked.
        $navbarCollapse.collapse("hide");

        // Change text in genre toggler depending on the state of the sidebar.
        if (!$wrapper.hasClass("toggled")) {
            displayHideSidebarButton($(this));
        } else {
            displayShowSidebarButton($(this));
        }
    });


    var $cachedWindowWidth = $(window).width();
    $(window).on("resize", function() {
        // Check if window width has actually changed
        // and that it's not just androic/ios broswer
        // triggering a resize event on scroll.
        if ($(window).width() != $cachedWindowWidth) {
            var $newwindowWidth = $(window).width();

            // Collapse the sidebar when resizing at small width,
            // and display it when resizing at wider screens.
            if ($newwindowWidth <= 992) {
                $wrapper.addClass("toggled");
                displayShowSidebarButton($genresToggler);
            } else {
                $wrapper.removeClass("toggled");
                displayHideSidebarButton($genresToggler);
            }
        }
    });


    function displayHideSidebarButton(genresToggler) {
        $(genresToggler).html("&laquo;");
        $(genresToggler).attr("title", "Hide Movie Genres bar");
    };

    function displayShowSidebarButton(genresToggler) {
        $(genresToggler).html("Genres &raquo;");
        $(genresToggler).attr("title", "Show all Movie Genres");
    };


    // Make top navbar collapse when nav-link is clicked.
    var $navLink = $(".navbar-nav > li > a")
    $navLink.on("click", function(e) {
        $navbarCollapse.collapse("hide");
    });


    // Make sidebar collapse when a specific genre is clicked in smaller screens.
    var $genreLink = $("#sidebar-wrapper > ul > li > a");
    $genreLink.on("click", function() {
        $wrapper.addClass("toggled");
        displayShowSidebarButton($genresToggler);
    });


    // Make sidebar collapse when top navbar toggler clicked.
    var $navbarToggler = $(".navbar-toggler-icon");
    $navbarToggler.on("click", function() {
        $wrapper.addClass("toggled");
        displayShowSidebarButton($genresToggler);
    });


    // Get the years from 1877 until now to
    // pass it to the movie release-year datalist
    // in the create/edit movie form.
    var start = 1877;
    var end = new Date().getFullYear();
    // Default empty value to make sure user chooses one.
    var options = "<option value=''>Select Release Year</option>";
    for(var year = start; year <= end; year++){
        // Concatenate all the years inside the option tags.
        options += "<option>" + year + "</option>"
    }
    // Pass the resulting tags to the years datalist.
    document.getElementById("release-year").innerHTML = options;
});
