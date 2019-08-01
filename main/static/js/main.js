function videoError() {
    $('#promo').addClass('backup-bg')
    $('#soff-video').hide()
    $('#pause-video').hide()
}

$(document).ready(function() {

    /****************************** MAIN ******************************/

    $('#soff-video').click(function() {
        var status = parseInt($(this).data('status'))
        if(status == 1) {
            $('#promo').prop('muted', true)
            $(this).prop('src', '/static/img/sound_off.png')
            $(this).data('status', '0')
        }
        else {
            $('#promo').prop('muted', false)
            $(this).prop('src', '/static/img/sound_on.png')
            $(this).data('status', '1')
        }
    })

    $('#pause-video').click(function() {
        var status = parseInt($(this).data('status'))
        if(status == 1) {
            $('#promo').get(0).pause()
            $(this).prop('src', '/static/img/play.png')
            $(this).data('status', '0')
        }
        else {
            $('#promo').get(0).play()
            $(this).prop('src', '/static/img/pause.png')
            $(this).data('status', '1')
        }
    })

    $('#start-page .classic-btn').click(function() {
        setTimeout(function() {
            $('.modal-backdrop.fade.show').remove()
        }, 300)
    })

    $('.rps p.text').click(function() {
        var id = $(this).data('id')
        $('#carousel' + id + ' .carousel-indicators li').each(function(index) {
            if(index == 0) {
                $(this).addClass('active')
                return
            }
        })
        $('#carousel' + id + ' .carousel-item').each(function(index) {
            if(index == 0) {
                $(this).addClass('active')
                return
            }
        })
        $('#carousel' + id).show()
        $('#slider-modal').modal('show')
    })

    /****************************** /MAIN ******************************/

})