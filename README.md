# ScavBot

## A Discord bot that assists players in the popular realistic survival FPS game Escape From Tarkov. Utilizes ***Selenium*** and ***Discord.py*** libraries.

## Built With:
 * Selenium
 * Discord.py

### Features

* Commands are prefixed with a "$"
* Current commands are:
  * ping
  * price
  * commands
  * help
* ***ping***
  * Pings the mentioned user 15 times.
* ***price***
  * Utilizes Selenium to interact with https://tarkov-market.com which keeps updated records on the flea market prices of items in the game. It returns
  the name, current market price, and a picture of the requested item in a *embed* object.
* ***commands***
  * Returns a list of all current commands with usage format and a description.
* ***help***
  * General bot information such as prefix, useful commands, and repository information.
  
  #### Sample Run
  
  ![demo](http://g.recordit.co/7dVzDSRmTE.gif)
