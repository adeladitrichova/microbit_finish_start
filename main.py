#FINISH

radio.set_group(1)
RunComp.set_light_level()
def on_light_drop2():
    if True:
        music.play_tone(Note.D4, music.beat())
        def on_received_number(elapsed):
            def on_button_pressed_a():
                basic.show_number(elapsed)
            input.on_button_pressed(Button.A, on_button_pressed_a)
        radio.on_received_number(on_received_number)
RunComp.on_light_drop(on_light_drop2)

#START

elapsed = 0
radio.set_group(1) 
RunComp.set_light_level()
elapsed = control.millis()
def on_light_drop():
    if True:
        global elapsed
        music.play_tone(Note.C, music.beat())
        radio.send_number(elapsed)
RunComp.on_light_drop(on_light_drop)
 

 