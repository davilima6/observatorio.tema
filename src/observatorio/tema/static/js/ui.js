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
            var desc = $("img", slide).attr("alt");
            fade.html("<span>" + title + "</span>" + desc);
            fade.fadeTo(300, 1);

            var table = $(".download a.tabela");
            var slide = $(event.target).children().eq(orbit.slide_number);
            var href = slide.attr('href');
            var url = href + '/download.table';
            table.attr('href', url);
            table.fadeTo(300,1);

            var table = $(".download a.csv");
            var slide = $(event.target).children().eq(orbit.slide_number);
            var href = slide.attr('href');
            var url = href + '/download.csv';
            table.attr('href', url);
            table.fadeTo(300,1);

            var table = $(".download a.json");
            var slide = $(event.target).children().eq(orbit.slide_number);
            var href = slide.attr('href');
            var url = href + '/download.json';
            table.attr('href', url);
            table.fadeTo(300,1);

            var table = $(".download a.xml-only");
            var slide = $(event.target).children().eq(orbit.slide_number);
            var href = slide.attr('href');
            var url = href + '/download.xml';
            table.attr('href', url);
            table.fadeTo(300,1);

            var table = $(".download a.xml-schema");
            var slide = $(event.target).children().eq(orbit.slide_number);
            var href = slide.attr('href');
            var url = href + '/download.schema.xml';
            table.attr('href', url);
            table.fadeTo(300,1);

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
            var list = []
            var areas = $("#area-filtro").val();
            alert(areas);
            if (areas !== '') {
                list.push(areas)
            }
            var filtro = $("#area-filtro");
            var el = $(this);
            if (el.is(filtros[0])) {
                filtros.removeClass();
            }
            else {
                $(filtros[0]).removeClass();
            }
            el.toggleClass("active");
            list.push(el.text());
            filtro.val(list);
            alert(list);
            if (!filtros.hasClass("active")) {
                $(filtros[0]).addClass("active");
            }
            return false;
        });

        $(document).foundation().foundation("joyride", "start");
        // $(window).load(function() {
        //   $('#destaques').orbit({ fluid: '2x1' });
        // });

    });

})(jQuery);
