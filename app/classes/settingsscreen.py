import os

from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen

CONFIG_DIR = os.path.join(
    App.get_running_app().APP_DIR, os.path.normcase("data/gameconfig.json")
)
DATA_DIR = os.path.join(
    App.get_running_app().APP_DIR, os.path.normcase("data/gamestate.json")
)


class SettingsScreen(Screen):

    store = JsonStore(CONFIG_DIR)

    def on_enter(self):
        for config_name in self.ids.keys():
            if not self.store.exists(config_name):
                self.store.put(config_name, value=1)
            self.set_config_value(config_name)

    def set_config_value(self, config_name):
        value_to_set = {
            "background_volume": self.store.get(config_name)["value"],
            "effects_volume": self.store.get(config_name)["value"],
            "auto_input": "down"
            if self.store.get(config_name)["value"] == 1
            else "normal",
        }.get(config_name)

        if value_to_set in {"down", "normal"}:
            self.ids[config_name].state = value_to_set
        elif type(value_to_set) in {float, int} and (
            value_to_set >= 0 or value_to_set <= 1
        ):
            self.ids[config_name].value_normalized = value_to_set

    def save_settings(self, to_save):
        new_value = {
            "background_volume": self.ids.background_volume.value_normalized,
            "effects_volume": self.ids.effects_volume.value_normalized,
            "auto_input": 1 if self.ids.auto_input.state == "down" else 0,
        }.get(to_save)

        if type(new_value) in {int, float} and (new_value >= 0 or new_value <= 1):
            if to_save == "background_volume":
                self.manager.get_screen("main_screen").music.volume = new_value
            self.store.put(to_save, value=new_value)

    def delete_saved_games(self, popup):
        JsonStore(DATA_DIR).clear()
        popup.dismiss()
