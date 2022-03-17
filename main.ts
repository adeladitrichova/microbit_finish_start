// START
let elapsed = 0
radio.setGroup(1)
RunComp.SetLightLevel()
elapsed = control.millis()
RunComp.OnLightDrop(function on_light_drop() {
    if (true) {
        
        music.playTone(Note.C, music.beat())
        radio.sendNumber(elapsed)
    }
    
})
// FINISH
radio.setGroup(1)
RunComp.SetLightLevel()
RunComp.OnLightDrop(function on_light_drop2() {
    if (true) {
        music.playTone(Note.D4, music.beat())
        radio.onReceivedNumber(function on_received_number(elapsed: number) {
            input.onButtonPressed(Button.A, function on_button_pressed_a() {
                basic.showNumber(elapsed)
            })
        })
    }
    
})
