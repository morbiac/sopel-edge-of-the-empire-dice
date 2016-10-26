Edge of the Empire dice roller for Sopel / Willie / Phenny IRC Bot
==============================

This is a modified version of https://github.com/StephenSwat/Edge-of-the-Empire-dice with some cleaned-up code and designed for the [Sopel IRC Bot](https://sopel.chat/) (Previously known as Willie and Phenny).

It allows for groups of players to enjoy the Star Wars Edge of the Empire RPG in an IRC chat room without having to use external websites to roll its specialized dice. 

Installation
------------

Installation is simple, if you're already using the [Sopel IRC Bot](https://sopel.chat/), which can greatly enhance any IRC community with its features. Just take the eotedice.py file and drop it into Sopel's Modules folder. If you already have a dice rolling module, you can also copy and paste the code from eotedice.py to combine them into one file. This module also features a standard die roller ported from [Rapptz's Discord bot](https://github.com/Rapptz/discord.py). If you need its capabilities to roll 6 or 20-sided dice, for example, just comment out the roll function at the bottom.  

Usage
-----

To roll Edge of the Empire dice in your IRC channel: 

	.eote <dice>

Examples:

	.eote YYGBPP
	.eote WWW
	.ed YYGBPP

Output examples:

    DarthHater rolled Threat: 2, Success: 2. They also rolled 1 Triumph!
    JarJarStinks rolled Advantage: 2, Success: 3.
    

Here, <dice> is a string representing the dice you want to roll. By default, the dice letters correspond to their color. You can change these triggers by modifying the keys of the DIE_OPTIONS dictionary.

	B = Boost die (Blue)
	G = Ability die (Green)
	Y = Proficiency die (Yellow)
	X = Setback die (Black)
	P = Difficulty die (Purple)
	R = Challenge die (Red)
	W = Force die (White)

To roll standard n-sided dice (Remember to uncomment the roll function to activate this, if needed):

    .roll 1d20
    .dice 1d20
    .roll 6d6
