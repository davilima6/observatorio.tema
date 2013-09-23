-- PASS THROUGH --
(function($) {
    "use strict";
    $(document).ready(function() {

//        // Carrega RespondJS para navegadores que nÃ£o suportam CSS3 media queries (ie: IE8)
//        if (Modernizr) {
//            Modernizr.load({
//                test: Modernizr.mq('only all'),
//                nope: 'js/respond.min.js'
//            });
//        }
//        else {
//            console.log("no modernizr!");
//        }

        // TODO: Slider para areas tematicas
        // $(document).on({
        //   mouseenter: function() { $(".panel", this).slideDown(100); },
        //   mouseleave: function() { $(".panel", this).slideUp(100); }
        // }, "#temas li");

        // VISUALIZACOES DE DADOS
        $("#daviz").on("orbit:before-slide-change", function() {
            $("#visualizacoes h5.subheader").fadeTo(300, 0.01);
        }).on("orbit:after-slide-change", function(event, orbit) {
            var fade = $("#visualizacoes h5.subheader");
            var slide = $(event.target).children().eq(orbit.slide_number);
            var title = slide.attr("title");
            var href = slide.attr('href');
            var desc = $("img", slide).attr("alt");
            fade.html("<span>" + title + "</span>" + desc);
            fade.fadeTo(300, 1);
            $(".download a.table").attr('href', href + '/download.table').prepOverlay({subtype: 'ajax'});
            $(".download a.csv").attr('href', href + '/download.csv');
            $(".download a.json").attr('href', href + '/download.json');
            $(".download a.xml-only").attr('href', href + '/download.xml');
            $(".download a.xml-schema").attr('href', href + '/download.schema.xml');
        });

        // BIBLIOTECA
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
        $("#biblioteca form").submit(function(e) {
            $("input[type=hidden]", this).remove();
            var paths;
            if ($("#biblioteca dd.active a[data-path=all]").length !== 0) {
                paths = $("#biblioteca dd:not(.active) a");
            } else {
                paths = $("#biblioteca dd.active a");
            }
            for (var i = 0; i < paths.length; i++) {
                var p = $(paths[i]).data("path");
                $(this).append($("<input type='hidden' name='c4' value='/observatorio/biblioteca/" + p + "' />"));
            }
            window.location = $(this).attr("action") + "#" + $(this).serialize();
            e.preventDefault();
        });

        // OBSERVATORIO E VOCE
        $("#observatorio-e-voce select").change(function() {
            var data_links = $("option:selected", this).data("links");
            var holder = $("<div />");
            for (var i = 0; i < data_links.length; i++) {
                var url = data_links[i].url;
                var title = data_links[i].title;
                holder.append($("<li class='bullet-item'><a href='" + url + "' title='" + title + "'>" + title + "</a></li>"));
            }
            var ul = $("#observatorio-e-voce ul");
            $(".bullet-item", ul).fadeOut(200, function() {
                $(this).remove();
                holder.children().hide().css("display", "inline-block").appendTo(ul).show(100);
            });
        });

        // FALLBACK para animacao CSS3 da caixa de busca
//        if(!Modernizr.csstransitions) {
//          $("#search-box").focus(function() {
//            $(this).stop().animate({width: "9em"});
//          }).blur(function() {
//            $(this).stop().animate({width: "5.5em"});
//          });
//        }

        // PARTICIPE (Enquete/Boletim/Contato)
        $("[data-match-height]").each(function() {
            var parentRow = $(this),
                childrenCols = $(this).find("[data-height-watch]"),
                childHeights = childrenCols.map(function(){ return $(this).outerHeight(); }).get(),
                tallestChild = Math.max.apply(Math, childHeights);
            childrenCols.css("min-height", tallestChild);
        });

        // Inicializa Foundation
        $(document).foundation();

    });

})(jQuery);
