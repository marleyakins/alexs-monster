from core import *
import toml

def main() -> int:
    bot = Alex()
    
    config = toml.load("config.toml")

    for extension in config["bot"]["extensions"]:
        bot.load_extension(extension)

    bot.run(config["bot"]["token"])
    return 0
