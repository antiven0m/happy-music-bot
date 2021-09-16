# happy the music bot

## Install Guide

1. Clone this repository using the GitHub website or GitHub/git CLI.
2. Install `pipenv`, the Python dependency manager, if necessary. Also, ensure `opus` and `ffmpeg` are installed on your machine and available in your environment. Both are used for media streaming.
3. Navigate into the project directory and run `pipenv install` to install dependencies.
4. Activate the Pipenv using `pipenv shell`. Run the bot using `python -m musicbot`.
5. On first startup, a default `config.toml` will be generated without an API token, so the bot will abort complaining that `No token has been provided.` Fill your bot's token into `config.toml`.
6. Run the bot using `python -m musicbot`.

## Commands

From the bot's `help` command:

  uptime    Tells how long the bot has been running.
  leave     Leaves the voice channel, if currently in one.
  play      Plays audio from a URL.
  help      Shows this message
  