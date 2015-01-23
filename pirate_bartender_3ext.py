# Pirate Bartender with selected revisions from sample solution

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

def drink_style_input():
  """Ask user what style of drink they like"""
  # Define answered style questions dictionary
  answers_style = {} 
  # Loop through style questions
  for style, question in questions.iteritems():
    # Ask whether they like a drink style and set to lower case
    # Test if answer is yes, then add drink style and boolean to dictionary
    answers_style[style] = raw_input(questions[style] + " Please answer (y)es or (n)o.").lower() in ["y","yes"]
  return answers_style
      
def drink_make(drink_styles):
  """Construct drink using user's style preferences and ingredients by style"""  
  # Define empty list for drink
  drink_ingredients = []  
  # Loop through styles and add random ingredient to drink list
  for style, selected in drink_styles.iteritems():
    # Test whether style selected by user
    if selected == True:
      drink_ingredients.append(random.choice(ingredients[style]))
  # Return drink
  return drink_ingredients

def main():
  """Run Pirate Bartender - Ask user for styles and return drink ingredients"""
  answers_style = drink_style_input()
  drink = drink_make(answers_style)
  print ""
  print "Your drink includes:"
  for ingredient in drink:
    print "A {}".format(ingredient)
      
if __name__ == "__main__":
  main()