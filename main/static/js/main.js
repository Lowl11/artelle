function videoError() {
    $('#promo').addClass('backup-bg');
    $('#soff-video').hide();
    $('#pause-video').hide();
}

$(document).ready(function() {

    /****************************** MAIN ******************************/

    $('#soff-video').click(function() {
        window.Utils.soundOnOrOffVideo();
    })

    $('#pause-video').click(function() {
        window.Utils.playOrPauseVideo();
    })

    $('#start-page .classic-btn').click(function() {
        setTimeout(function() {
            $('.modal-backdrop.fade.show').remove();
        }, 300)
    })

    $('.rps p.text').click(function() {
        var id = $(this).data('id');

        $('#carousel' + id + ' .carousel-indicators li').removeClass('active');
        $('#carousel' + id + ' .carousel-item').removeClass('active');

        $('#carousel' + id + ' .carousel-indicators li').each(function(index) {
            if(index == 0) {
                $(this).addClass('active');
                return;
            }
        });
        $('#carousel' + id + ' .carousel-item').each(function(index) {
            if(index == 0) {
                $(this).addClass('active');
                return;
            }
        });

        var name = $('#rp-name' + id).text();
        var description = '<h4>' + name + '</h4>';
        description += $('#rp-description' + id).html();
        $('#carousel-description' + id).html(description);

        var descHeight = $('#rp-description' + id).height() + 80;
        $('.carousel-indicators').css({'bottom': descHeight + 'px'});

        $('.carousel').hide();
        $('#carousel' + id).show();
        $('#slider-modal').modal('show');
    })

    /****************************** /MAIN ******************************/

})