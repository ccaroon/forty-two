"""
Advise - Magic Eight Ball Predictions
"""
import random

import click

RESPONSES = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."
]

# advise
@click.command()
@click.argument("question")
def advise(question):
    """ Ask the Magic Eight Ball """
    answer = random.choice(RESPONSES)
    print(f'"{question.title()}"? 🎱 {answer} 🎱')
    # print(F"")
