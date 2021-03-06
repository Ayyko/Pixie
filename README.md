# Pixie
* An open-source Discord bot built for weebs by a weeb.
* Here's the [invite link](https://discordapp.com/oauth2/authorize?client_id=175319652073734144&scope=bot&permissions=536083519) in case you want to add Pixie to your server. (Although she's not currently hosted by me), note that I am planning to host her quite soon now the addition of WeebMusic has been added!

# Current Features
* Owner
  * namechange (Changes the bots name)
  * gamechange (Changes the bots game)
  * avatar (Changes the bots avatar)
  * debug
  * REPL
* Moderation
  * purge (Deletes large amounts of messages) (Requires manage message permission)
  * ban (Bans a user from a server) (Requires ban members permission)
  * kick (Kicks a user from a server) (Requires kick members permission)
* Information
  * userinfo (Grabs information for a user)
  * serverinfo (Grabs general server information)
  * status (Shows some bot stats)
* WeebMusic (Only supports streaming music from [listen.moe](https://listen.moe))
  * music (a command group for using WeebMusic)
    * join (Joins voice channel and starts the stream)
    * pause (Pauses the stream)
    * resume (Resumes the stream)
    * volume (Sets the volume in the server you use the command in)
    * check_vol (Checks the volume of the server you're in)
    * disconnect (Leaves the voice channel and stops the stream)
* Weeb
  * mal (a command group for interacting with myanimelist)
    * anisearch (Searches an anime)
    * mangasearch (Searches a manga)
  * novel (Searches a novel)


# Planned Features
* Weeb Features
  * Anime
    * Integration with MyAnimelist (being able to use your account from Pixie!)
    * Integration with Hummingbird (being able to use your account from Pixie!)
    * Integration with Anilist (being able to use your account from Pixie!)
  * Manga
    * Coming soon! (Tbh I have no idea what I can do for this, help is appreciated when it comes to ideas)
* Custom server prefixes


# Information
* Pixie is built using [discord.py](https://github.com/Rapptz/discord.py/)
* Pixie is a reference to the character from [Mahouka Koukou no Rettousei](http://www.novelupdates.com/series/mahouka-koukou-no-rettousei/) light novels.

# Setup

Assuming you have the files in a folder it should work fine! Make sure the setup file is in the main folder.

But, now we're through all the boring stuff - here's what you need to get it running.
```
{
    "discord":{"owner_id": "Your discord id here",
                "command_prefix": "Whatever you want Pixies prefix to be (note that pinging pixie will always work)",
                "token": "Your discord API token"},

    "weeb":{"ani_list": "(LEAVE BLANK, NOT CURRENTLY USED)",
            "hummingbird": "(LEAVE BLANK, NOT CURRENTLY USED)",
            "MAL": {"username":"Your myanimelist username",
                    "password":"Your myanimelist password"}},

    "games":{"osu_api_key": "(Leave blank, not currently used)"},

  "log_level": "INFO"
}
```
# Requirements
* [Python 3.5+](https://python.org)
* [discord.py](https://github.com/Rapptz/discord.py)
* [lxml](https://github.com/lxml/lxml)
* [Shosetsu](https://git.vertinext.com/ccubed/Shosetsu)
* [PyAnimeList](https://github.com/GetRektByMe/PyAnimeList)
* [Raitonoberu](https://github.com/GetRektByMe/Raitonoberu)
