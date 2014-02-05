var votes_plot;
var votes_ajax_req;

function vote_on_quirky(idea_id){
    $.post(
        "http://www.quirky.com/api/v2/ideations/" + idea_id + "/votes",
        {"value":1}
    )
}

function update_idea(data) {
         $.jqplot.config.enablePlugins = true;
         if (votes_plot){
             votes_plot.destroy();
         }
         $('.loading').hide();
         votes_plot = $.jqplot('votes_plot',  [data],
            {axes:{xaxis:{renderer:$.jqplot.DateAxisRenderer} } }
         );
  }

$(function(){
    $('.loading').hide()
    $('#search_text').hide()
    text_bool = $('#text_bool')
    text_bool.change(function(){
        if (text_bool.val()){
            $('#search_text').fadeIn();
        }
        else {
            $('#search_text').fadeOut();
        }
    }
    )
    $('#idea_list_table tr').hover(
        function(evt){
            $( this ).addClass('highlighted');
            $('.loading').fadeIn();
            votes_ajax_req=$.get(
                '/idea_json/'+this.id,
                null,
                update_idea
            );
            //$('#quirky_frame').attr('src', 'http://www.quirky.com/invent/' + this.id);
            
        },
        function(evt){
            $( this ).removeClass('highlighted');
            if (votes_ajax_req){
                votes_ajax_req.abort();
            }
            votes_plot.destroy();
            $('.loading').hide();
        })
})


