
$(function() {

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

    $(window).resize(function() {
        windowWidth = $(this).width();
        
        if (windowWidth <= 992) {
            $wrapper.addClass("toggled");
            displayShowSidebarButton($genresToggler);
        } else {
            $wrapper.removeClass("toggled");
            displayHideSidebarButton($genresToggler);
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
