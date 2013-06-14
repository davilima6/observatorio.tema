(function($) {
    "use strict";
    $(document).ready(function() {

        $("#barra-brasil").prependTo(".fixed.contain-to-grid");

        // Slider para areas tematicas
        $(document).on({
            mouseenter: function() {
                // detalha informações
                $(".panel", this).slideDown(100);
            },
            mouseleave: function() {
                // esconde informações
                $(".panel", this).slideUp(100);
            }
        }, "#temas li");

        $("#daviz").on("orbit:before-slide-change", function() {
            $("#visualizacoes h5.subheader").fadeTo(300, 0.01);
        });

        $("#daviz").on("orbit:after-slide-change", function(event, orbit) {
            var fade = $("#visualizacoes h5.subheader");
            var slide = $(event.target).children().eq(orbit.slide_number);
            var title = slide.attr("title");
            var desc = $("img", slide).attr("alt");
            fade.html("<span>" + title + "</span>" + desc);
            fade.fadeTo(300, 1);
        });

        $("[data-match-height]").each(function() {
            var parentRow = $(this),
                childrenCols = $(this).find("[data-height-watch]"),
                childHeights = childrenCols.map(function(){ return $(this).outerHeight(); }).get(),
                tallestChild = Math.max.apply(Math, childHeights);
            childrenCols.css("min-height", tallestChild);
            console.log(childHeights, tallestChild);
        });

        $(document).foundation().foundation("joyride", "start");
    });

})(jQuery);