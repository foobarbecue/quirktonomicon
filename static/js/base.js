var votes_plot;
var votes_ajax_req;

function vote_on_quirky(idea_id){
    $.post(
        "http://www.quirky.com/api/v2/ideations/" + idea_id + "/votes",
        {"value":1}
    )
}

function update_idea_details(data) {
    data = data[0]['fields']
    for (var key in data){
        $('#idea_details #' + key).html(data[key]);
    }
    $('#idea_details').fadeIn();
}

function update_votes_plot(data) {
    if (votes_plot){
        votes_plot.destroy();
    }
    $('.loading').hide();
    $.jqplot.config.enablePlugins=true;
    votes_plot = $.jqplot('votes_plot',  [data],
    {
        axes: {
            xaxis:{renderer:$.jqplot.DateAxisRenderer} },
        grid: {background: 'transparent', gridLineColor: '#222', borderColor: '#222'},
        seriesColors:['#A7B67F'],
        cursor:{zoom:true},
        seriesDefaults:{showLine:false,
            markerOptions:{size:2}
        },
        legend: {show:true, location:'nw'},
        series:[
            {label:'votes on Quirky'},
            {label:'# times flagged as junk'},
            {label:'# times flagged as funny'}
        ]
        
    }
    );
  }
      

$(function(){
    $.jqplot.config.enablePlugins = true;
    votes_ajax_req = false;
    details_ajax_req = false;
    $('.loading').hide()
    $('#idea_details, #search_text').hide()
    
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
    $('#page_selector').change(
        function(evt){
            window.location = window.location + "&page=" + $(this).val()
        }
                        )
    $('#idea_list_table tr').hover(
        function(evt){
            $( this ).addClass('highlighted');
            $( this ).siblings().removeClass('highlighted');
            $('#missing_features').hide();
            $('.loading').fadeIn();
            
            // Stop all pending ajax requests before making new ones to avoid queue
            if (votes_ajax_req){
                votes_ajax_req.abort();
            }
            if (details_ajax_req){
                votes_ajax_req.abort();
            }            
            if (votes_plot){
                votes_plot.destroy();
            }
            
            details_ajax_req=$.get(
                '/ideas_json/'+this.id,
                null,
                update_idea_details
                
            );
            votes_ajax_req=$.get(
                '/votes_plot_json/'+this.id,
                null,
                update_votes_plot
            );
            //$('#quirky_frame').attr('src', 'http://www.quirky.com/invent/' + this.id);
            
        },
        function(evt){
//             $( this ).removeClass('highlighted');
//             $('.loading').hide();
//             $('#idea_details').hide();
//             $('#votes_plot').hide();
//             $('#missing_features').show();
        })
})


