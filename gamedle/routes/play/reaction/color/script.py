import time
import js  # type: ignore
from pyodide.ffi import create_proxy  # type: ignore
from pyodide.ffi.wrappers import set_timeout  # type: ignore
import random

background = js.document.getElementById("game_background")
loading = js.document.getElementById("loading")
start = js.document.getElementById("start")
game = js.document.getElementById("game")
game_over = js.document.getElementById("failed")
end = js.document.getElementById("end_game")
on_start = js.document.getElementById("on_start")
on_restart = js.document.getElementById("on_restart")
print("initializing game")
background.style.display = "flex"
loading.style.display = "none"
start.style.display = "none"
game.style.display = "none"
game_over.style.display = "none"
end.style.display = "none"
on_restart.style.display = "none"
print("initialized game")

game_logic = {"press_now": False, "isPlaying": False, "start_time": 0, "end_time": 0}


def start_game(*args):
    # reset game
    start.style.display = "none"
    game.style.display = "none"
    game_over.style.display = "none"
    end.style.display = "none"
    on_restart.style.display = "none"
    background.style.background = "inherit"

    game_logic["isPlaying"] = True

    print("starting game")
    on_start.style.display = "none"
    start.style.display = ""
    random_seconds = random.randint(1, 5)
    set_timeout(show_green, random_seconds * 1000)


def show_green():
    if not game_logic["press_now"]:
        print("showing green")
        start.style.display = "none"
        game.style.display = ""
        background.style.background = "green"
        game_logic["press_now"] = True
        game_logic["start_time"] = time.time()


def handle_keypress(event):
    if event.key == " ":
        if not game_logic["press_now"] and game_logic["isPlaying"]:
            print("you pressed too early")
            game.style.display = "none"
            game_over.style.display = ""
            background.style.background = "red"
            end.style.display = ""
            on_restart.style.display = ""
            game_logic["isPlaying"] = False
            game_logic["press_now"] = False
            return
        elif game_logic["press_now"] and game_logic["isPlaying"]:
            print("you pressed on time")
            game_logic["end_time"] = (time.time() - game_logic["start_time"]) * 1000
            game.style.display = "none"
            background.style.background = "green"
            end.style.display = ""
            end.innerHTML = (
                f"you pressed on time, your time was {int(game_logic['end_time'])} ms"
            )
            on_restart.style.display = ""
            game_logic["isPlaying"] = False
            game_logic["press_now"] = False
            return


js.document.addEventListener("keypress", create_proxy(handle_keypress))

on_start.addEventListener("click", create_proxy(start_game))
on_restart.addEventListener("click", create_proxy(start_game))
