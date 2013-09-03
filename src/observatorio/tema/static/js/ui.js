(function($) {    
    "use strict";
    $(document).ready(function() {

        // BARRA BRASIL
        $("#barra-brasil").prependTo(".fixed.contain-to-grid");

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

        // OBSERVATORIO E VOCE
        $("#observatorio-e-voce select").change(function() {
            var links = $("option:selected", this).data("links");
            var links = JSON.stringify(eval('('+links+')'));
            // var links = JSON.parse(links);
            $("#observatorio-e-voce .bullet-item a").fadeOut().each(function(i) {
                var parent = $(this).parent();
                var url = links[i].url;
                var title = links[i].title;
                var html = $("<li><a href='" + url + "' title='" + title + "'>" + title + "</a></li>");
                // debugger;
                parent.remove();
                parent.html(html);
            }).fadeIn();            
        });

        // XXX: Verificar se eh possivel remover
        //   $(window).load(function() {
        //   $('#destaques').orbit({ fluid: '2x1' });
        // });
        
        // TODO: Fallback para animacao da caixa de busca
        // if(!Modernizr.csstransitions) {
        //   console.log("no css transitions!");
        //   $("#search-box").focus(function() {
        //     $(this).stop().animate({width: "9em"});
        //   }).blur(function() {
        //     $(this).stop().animate({width: "3.5em"});
        //   });
        // }

        // TODO: Slider para areas tematicas
        // $(document).on({
        //   mouseenter: function() { $(".panel", this).slideDown(100); },
        //   mouseleave: function() { $(".panel", this).slideUp(100); }
        // }, "#temas li");

        // PARTICIPE (Enquete/Boletim/Contato)
        // XXX: Verificar se eh possivel remover
        $("[data-match-height]").each(function() {
            var parentRow = $(this),
                childrenCols = $(this).find("[data-height-watch]"),
                childHeights = childrenCols.map(function(){ return $(this).outerHeight(); }).get(),
                tallestChild = Math.max.apply(Math, childHeights);
            childrenCols.css("min-height", tallestChild);
            // XXX: Remove me
            // console.log(childHeights, tallestChild);
        });

        $(document).foundation().foundation("joyride", "start");

    });

})(jQuery);
