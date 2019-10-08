$(function() {
    
    var Utils = {
        playOrPauseVideo: playOrPauseVideo,
        soundOnOrOffVideo: soundOnOrOffVideo
    }
    window.Utils = Utils;

    function playOrPauseVideo() {
        var playOrPauseButton = $('#pause-video');
        var status = parseInt(playOrPauseButton.data('status'))
        if(status == 1) {
            $('#promo').get(0).pause()
            playOrPauseButton.prop('src', '/static/img/play.png')
            playOrPauseButton.data('status', '0')
        }
        else {
            $('#promo').get(0).play()
            playOrPauseButton.prop('src', '/static/img/pause.png')
            playOrPauseButton.data('status', '1')
        }
    }

    function soundOnOrOffVideo() {
        var soundOnOrOffButton = $('#soff-video');
        var status = parseInt(soundOnOrOffButton.data('status'))
        if(status == 1) {
            $('#promo').prop('muted', true)
            soundOnOrOffButton.prop('src', '/static/img/sound_off.png')
            soundOnOrOffButton.data('status', '0')
        }
        else {
            $('#promo').prop('muted', false)
            soundOnOrOffButton.prop('src', '/static/img/sound_on.png')
            soundOnOrOffButton.data('status', '1')
        }
    }

});