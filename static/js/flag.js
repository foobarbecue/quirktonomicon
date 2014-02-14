//TODO generalize success handler (prototype?), use deferred object
$(function(){
$('.funny').click(
    function(){
        $.ajax({
            type: 'POST',
            url: '/flag',
            dataType: 'json',
            data: {kind:'funny',idea_id:$($(this).parent()).parent()[0].id},
            context: this,
            success: function(data){
                $(this).text('funny (' + data.funny + ')')
            }
        });
    }
);
$('.junk').click(
    function(){
        $.ajax({
            type: 'POST',
            url: '/flag',
            dataType: 'json',
            data: {kind:'junk',idea_id:$($(this).parent()).parent()[0].id},
            context: this,
            success: function(data){
                $(this).text('junk (' + data.junk + ')')
            }
        });
    }
);
});