# для загрузки сохранений мира
import json

world_state: dict = {
    ...
}


def save_world_state(filename: str) -> None:
    with open(filename, "w") as file:
        json.dump(world_state, file, indent=4)


def load_world_state(filename: str) -> dict:
    global world_state
    try:
        with open(filename, "r") as file:
            world_state = json.load(file)
    except FileNotFoundError:
        print("Файл сохранения не найден.")