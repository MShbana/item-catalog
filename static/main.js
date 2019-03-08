
$(document).ready(function() {

    var $wrapper = $("#wrapper")
    var $genresToggler = $("#genres-toggler")

    $genresToggler.click(function(e) {
        e.preventDefault();
        $(this).blur();

        $wrapper.toggleClass("toggled");

        if (!$wrapper.hasClass("toggled")) {
            displayHideSidebarButton($(this));
        } else {
            displayShowSidebarButton($(this));
        }
    });

    var $cachedWindowWidth = $(window).width();
    $(window).resize(function() {
        // Check if window width has actually changed
        // and that it's not just androic/ios broswer
        // triggering a resize event on scroll.
        if ($(window).width() != $cachedWindowWidth) {
            var $newwindowWidth = $(window).width();

            if ($newwindowWidth <= 992) {
                $wrapper.addClass("toggled");
                displayShowSidebarButton($genresToggler);
            } else {
                $wrapper.removeClass("toggled");
                displayHideSidebarButton($genresToggler);
            }
        }
    });


    function displayHideSidebarButton(genresToggle) {
        $(genresToggle).html("&laquo;");
        $(genresToggle).attr("title", "Hide Movie Genres bar");
    };

    function displayShowSidebarButton(genresToggle) {
        $(genresToggle).html("Genres &raquo;");
        $(genresToggle).attr("title", "Show all Movie Genres");
    };
});
