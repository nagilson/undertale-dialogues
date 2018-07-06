#
#
#Script.py 
#Consider this to be __main__.
#
#This is where the dialogue and character configuration goes. 
#If you want to pull a new character, you will need to trim their audio files. I would suggest decorating callback with a rand function for chars with multiple flavors.  
#
#
init python:
    config.quit_action = Quit(confirm=False)
    config.nearest_neighbor = True
    config.windows_icon = "images/under.ico"
    config.use_drawable_resolution = False
    config.default_text_cps = 36
    config.screen_width = 640
    config.screen_height = 480
    talk = True
    
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("sound/GENERIC.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def callbackFox(event, **kwargs):
       if event == "show":
           renpy.music.play("sound/GENERIC.wav", channel="sound", loop=True)
       elif event == "slow_done" or event == "end":
           renpy.music.stop(channel="sound")

define virru = Character("", callback = callback, what_font="font/utAuto.otf", what_size = 26, what_xpos = 60, what_ypos = -50)
# The game starts here.
label main_menu:
     return 

label start:

    scene bg clear

    transform iconTalk: 
        yalign 0.9109
        xalign 0.06
    # These display lines of dialogue.
    # Template for img: show obj arg at transformarg:
    # xalign param { 0 <- 0.5  -> 1.0 } yalign param , hide obj 
    # tranform obj: params
    virru "* Editing this script is pretty simple."
    virru "* Go to script.rpy and create character objects where virru is."
    virru "* Characters can have icons by using 'show obj arg at iconTalk.'"
    virru "* You can change the font to match a specific character."
    virru "* For characters with multiple sounds, randomly generate #s to use a sound effect."
    virru "* Sounds have extra white space at the end so you will need to clip them."
    # This ends the game.
    $ renpy.pause(1.0)
    $ renpy.quit()
    return
