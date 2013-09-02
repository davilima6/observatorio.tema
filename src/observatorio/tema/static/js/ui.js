(function($) {
    "use strict";
    $(document).ready(function() {
        $("#barra-brasil").prependTo(".fixed.contain-to-grid");

        // if(!Modernizr.csstransitions) {
        //   console.log("no css transitions!");
        //   $("#search-box").focus(function() {
        //     $(this).stop().animate({width: "9em"});
        //   }).blur(function() {
        //     $(this).stop().animate({width: "3.5em"});
        //   });
        // }

        // Slider para areas tematicas
        // $(document).on({
        //   mouseenter: function() { $(".panel", this).slideDown(100); },
        //   mouseleave: function() { $(".panel", this).slideUp(100); }
        // }, "#temas li");

        $("#daviz").on("orbit:before-slide-change", function() {
            $("#visualizacoes h5.subheader").fadeTo(300, 0.01);
        });

        $("#daviz").on("orbit:after-slide-change", function(event, orbit) {
            var fade = $("#visualizacoes h5.subheader");
            var slide = $(event.target).children().eq(orbit.slide_number);
            var title = slide.attr("title");
            var href = slide.attr('href');
            var desc = $("img", slide).attr("alt");
            fade.html("<span>" + title + "</span>" + desc);
            fade.fadeTo(300, 1);
            $(".download a.tabela").attr('href', href + '/download.table');
            $(".download a.csv").attr('href', href + '/download.csv');
            $(".download a.json").attr('href', href + '/download.json');
            $(".download a.xml-only").attr('href', href + '/download.xml');
            $(".download a.xml-schema").attr('href', href + '/download.schema.xml');
        });

        $("[data-match-height]").each(function() {
            var parentRow = $(this),
                childrenCols = $(this).find("[data-height-watch]"),
                childHeights = childrenCols.map(function(){ return $(this).outerHeight(); }).get(),
                tallestChild = Math.max.apply(Math, childHeights);
            childrenCols.css("min-height", tallestChild);
            // XXX: Remove me
            // console.log(childHeights, tallestChild);
        });

        var filtros = $("#biblioteca dd");
        filtros.click(function () {
            var el = $(this);
            if (el.is(filtros[0])) {
                filtros.removeClass();
            }
            else {
                $(filtros[0]).removeClass();
            }
            el.toggleClass("active");
            if (!filtros.hasClass("active")) {
                $(filtros[0]).addClass("active");
            }
            return false;
        });

        $(document).foundation().foundation("joyride", "start");
        // $(window).load(function() {
        //   $('#destaques').orbit({ fluid: '2x1' });
        // });
        
        $("#observatorio-e-voce select").change(function() {
            var links = $("option:selected", this).data("links");
            $("#observatorio-e-voce .bullet-item a").fadeOut().each(function(i) {
                $(this).attr("href", links[i].url).text(links[i].title);
            }).fadeIn();
            
        });

    });

})(jQuery);
