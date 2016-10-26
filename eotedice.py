from collections import Counter
from sopel.module import commands
import random

SUCCESS = {
    "Success": 1
}

ADVANTAGE = {
    "Advantage": 1
}

TRIUMPH = {
    "Success": 1,
    "Triumph": 1
}

FAILURE = {
    "Success": -1
}

THREAT = {
    "Advantage": -1
}

DESPAIR = {
    "Success": -1,
    "Despair": 1
}

DARK = {
    "Dark": 1
}

LIGHT = {
    "Light": 1
}

BLANK = {
}

DIE_OPTIONS = {
    # Boost die
    "B": (
        (BLANK,),
        (BLANK,),
        (SUCCESS,),
        (ADVANTAGE,),
        (ADVANTAGE, ADVANTAGE,),
        (ADVANTAGE, SUCCESS,)
    ),
    # Ability die
    "G": (
        (BLANK,),
        (ADVANTAGE, ADVANTAGE,),
        (SUCCESS,),
        (ADVANTAGE,),
        (SUCCESS, SUCCESS,),
        (ADVANTAGE, SUCCESS,),
        (ADVANTAGE,),
        (SUCCESS,)
    ),
    # Proficiency die
    "Y": (
        (BLANK,),
        (SUCCESS,),
        (SUCCESS,),
        (SUCCESS, SUCCESS,),
        (SUCCESS, SUCCESS,),
        (ADVANTAGE,),
        (ADVANTAGE, SUCCESS,),
        (ADVANTAGE, SUCCESS,),
        (ADVANTAGE, SUCCESS,),
        (ADVANTAGE, ADVANTAGE,),
        (ADVANTAGE, ADVANTAGE,),
        (TRIUMPH,)
    ),
    # Setback die
    "X": (
        (BLANK,),
        (BLANK,),
        (FAILURE,),
        (FAILURE,),
        (THREAT,),
        (THREAT,)
    ),
    # Difficulty die
    "P": (
        (BLANK,),
        (THREAT,),
        (THREAT, THREAT,),
        (THREAT,),
        (THREAT,),
        (THREAT,),
        (THREAT, THREAT,),
        (FAILURE, THREAT,)
    ),
    # Challenge die
    "R": (
        (BLANK,),
        (FAILURE,),
        (FAILURE,),
        (FAILURE, FAILURE,),
        (FAILURE, FAILURE,),
        (THREAT,),
        (THREAT,),
        (FAILURE, THREAT,),
        (FAILURE, THREAT,),
        (THREAT, THREAT,),
        (THREAT, THREAT,),
        (DESPAIR,)
    ),
    # Force die
    "W": (
        (DARK,),
        (DARK,),
        (DARK,),
        (DARK,),
        (DARK,),
        (DARK,),
        (DARK, DARK,),
        (LIGHT,),
        (LIGHT,),
        (LIGHT, LIGHT,),
        (LIGHT, LIGHT,),
        (LIGHT, LIGHT,)
    )
}


@commands('eote', 'ed')
def eote(bot, trigger):
    """Create a dictionary of die results for an Edge of the Empire dice roll."""
    die_dict = Counter({})
    for letter in trigger.group(2):
        for result in random.choice(DIE_OPTIONS[letter]):
            die_dict.update(Counter(result))
    # Return dict without 0 values
    die_dict = dict_print(trigger.nick, {k: v for k, v in die_dict.items() if v})
    bot.say(die_dict)


def dict_print(name, die_dict):
    """Convert a dictionary of die results to text output."""
    fancy = ''
    bonus = ''
    for keys, values in list(die_dict.items()):
        if keys == 'Triumph' or keys == 'Despair':
            if not bonus:
                bonus = "They also rolled {} {}!".format(str(values), keys)
            else:
                bonus = bonus[:-1]
                bonus += " and {} {}!".format(str(values), keys)
        else:
            if values < 0:
                if keys == 'Success':
                    keys = 'Failure'
                if keys == 'Advantage':
                    keys = 'Threat'
                values = abs(values)
            fancy += '{}: {}, '.format(keys, str(values))
    if not fancy and not bonus:
        return "{}'s roll canceled out. No result.".format(name)
    else:
        return "{} rolled {}. {}".format(name, fancy[:-2], bonus)


# @commands('roll', 'dice')
# def roll(bot, trigger):
#     """Roll dice in NdN format."""
#     try:
#         rolls, limit = map(int, trigger.group(2).split('d'))
#     except ValueError:
#         bot.say('Format has to be in NdN!')
#         return
#     result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#     bot.say('{} rolls {} {}-sided dice: \x02{}\x0F'.format(trigger.nick, rolls, limit, result))
