# First version of Pirate Bartender

import random

# Define drink style questions
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

# Define ingredient types by style
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

# Define answered style questions dictionary
answers_style = dict()

def drink_style_input():
  """Ask user what style of drink they like"""
  # Loop through style questions
  for question in questions:
    # Ask whether they like a drink style and set to lower case
    answer = raw_input(questions[question] + " Please answer (y)es or (n)o.").lower()
    # Test if answer is yes, then add drink style and boolean to dictionary
    if answer == "y":
      answers_style[question] = True
    else:
      answers_style[question] = False
      
def drink_construct(drink_styles):
  """Construct drink using user's style preferences and ingredients by style"""  
  # Define empty list for drink
  drink_ingredients = list()  
  # Loop through styles and add random ingredient to drink list
  for style in drink_styles:
    # Test whether style selected by user
    if drink_styles[style] == True:
      drink_ingredients.append(random.choice(ingredients[style]))
  # Return drink
  return drink_ingredients
      
if __name__ == "__main__":
  drink_style_input()
  print drink_construct(answers_style)