# Elusive Enigmas
By: Amphibian Alchemists

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Used by the Germans to send covert messages, the WWII Enigma Machine is the most famous encryption device of the 20th Century. As the role of a code receiver for the Germans, you must decipher the message given to you by the commander before the Allies capture you!

Table of Contents:
- Setup
- Tutorial
- Settings (Defaults)
- Background
- Sources

---
### Setup
1. Clone or download this repository.
2. Ensure you have pip, wheel setuptools and virtualenv in the latest version: `python3 -m pip install --upgrade pip wheel setuptools virtualenv`
3. Create a virtual environment in your terminal (e.g. `virtualenv venv`).
5. Activate it (`source venv/bin/activate` or, on Windows, do `venv\Scripts\activate`.
6. If you're in Windows, install the Kivy dependencies:
```
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
```
7. If you are in Linux, make sure you have the [SLD2 dependencies installed](https://kivy.org/doc/stable/installation/installation-linux-venvs.html?highlight=from%20source#dependencies-with-sdl2) and then install Kivy with: `pip install https://github.com/kivy/kivy/archive/stable.zip`
8. Go to the top directory where `requirements.txt` lives and `pip install -r requirements.txt`.
9. In terminal, run main.py by doing `python main.py` or `python3 main.py`

Troubles during setup? Check the installation instructions in the [Kivy website](https://kivy.org/doc/stable/gettingstarted/installation.html)

---
### Tutorial
In order to start decripting messages, you must first do two things: configure the rotors and the plugboard. In game, you are given a piece of paper with the machine's configurations. Configure the rotors (top) and the plugboard (bottom) according to the paper.

![](readme_images/gamescreen.png)

#### Rotors ####

Configure the three rotors with the + and - buttons until they match with the instructions on the paper.

![](readme_images/rotor.png)![](readme_images/rotorpaper.png)

#### Plugboard ####

Click two ports to create a wire that connects both of them. These ports are labeled with letters. You must connect each letter with its respetive letter pair listed on the paper.

![](readme_images/plugboard.png)![](readme_images/plugboardpaper.png)

#### Typing ####

Once you have those configured, you are ready to decipher! Type the ciphertext listed on the paper into the textbox. If Autoinput is enabled (enabled by default), your mistakes will be ignored. Turn off Autoinput in settings for a challenge!

Beware though, you only have a certain amount of time to decipher the message before the Allies capture you! Decipher the complete message to win the game!

Note: If you have Autoinput off and mistype once, you can no longer win (Remember, The Germans didn't have a backspace key).

You can also have a save point (executed from game menu, not main). You can save your current progress as a save point. If you ever mess up, you can restart that current game from that save point by pressing Load Game in the game menu located at the top left of a game.

---
### Settings (Defaults)
- Fullscreen: Off
- Autoinput: On
- Musics: On
- Sound effects: On

---
### Background
To gain the full experience, it's best to understand how the machine works.
- https://en.wikipedia.org/wiki/Enigma_machine
- [Numberphile Video](https://www.youtube.com/watch?v=G2_Q9FoD-oQ)

A diagram of the machine's internal functionality:
![](https://i.pinimg.com/originals/67/cc/c3/67ccc3a33d6fbbf4b2738e167b5cfa37.png)

---
### Sources
- [02246 key type shot strike typewriter.wav by Robinhood76](https://freesound.org/people/nebyoolae/sounds/318067/) - [License](https://creativecommons.org/licenses/by/3.0/)
- [Gear Clink by nebyoolae](https://freesound.org/people/nebyoolae/sounds/318067/) - [License](https://creativecommons.org/licenses/by/3.0/)
- [Pop, High, A (H1).wav by InspectorJ](https://freesound.org/people/InspectorJ/sounds/411642/) - [License](https://creativecommons.org/licenses/by/3.0/)
- [plug in.wav by caseymoura](https://freesound.org/people/caseymoura/sounds/445493/) - [License](https://creativecommons.org/licenses/by/3.0/)
- [Sneaky Snooper by Jason Shaw](https://audionautix.com/) - [License](https://creativecommons.org/licenses/by/4.0/)
- [Swooshing by man](http://soundbible.com/670-Swooshing.html) - [License](https://creativecommons.org/licenses/sampling+/1.0/)

---
### LICENSE
MIT License

Authors: [Pancho](https://github.com/Franccisco), [YoomamaFTW](https://github.com/YoomamaFTW), [sloopoo](https://github.com/flextian)
