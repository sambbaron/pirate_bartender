# Pirate Bartender with multiple customers

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
    # Ask whether they like a drink style and return boolean
    style_answer = raw_input(questions[style]).lower() in ["y","yes"]
    # Test if answer is yes, then add drink style and boolean to dictionary
    if style_answer == True: 
      answers_style[style] = style_answer
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

def drink_name():
  """Create drink name based on random adjectives and nouns"""
  # Define drink name adjectives
  drink_adjectives = ["Hairy", "Smelly", "Gassy", "Angry", "Drowny", "Hanging"]
  # Define drink name nouns
  drink_nouns = ["Parrot's Leg", "Whore Whisker", "Sea Troll", "Treasure", "Sword"]  
  # Select random adjective and noun
  name_adjective = drink_adjectives[random.choice(range(0,len(drink_adjectives)))]
  name_noun = drink_nouns[random.choice(range(0,len(drink_nouns)))]  
  # Create drink name using random adjective and noun
  return name_adjective + " " + name_noun

def main():
  """Run Pirate Bartender - Ask user for styles and return drink ingredients"""
  # Define questions for subsequent drinks
  drink_questions = ["Would you like a drink?  Please answer (y)es or (n)o.", 
                    "How about another?",
                    "Must have been a hard day swabbing decks. Another drink?",
                    "Alright pal, do you want another drink?  You're not driving the ship home, are you?",
                    "You drunk bastard.  I'm cutting you off."]
  # Loop through customer questions
  for question in drink_questions:
    # Ask drink question
    print ""
    customer_answer = raw_input(question) in ["y","yes"]
    print ""
    # Test for positive answer - if so, then make drink
    if customer_answer == True and drink_questions.index(question) != len(drink_questions):
      print "Answer ye some riddles about your favorite libation. Please answer (y)es or (n)o."
      print ""
      answers_style = drink_style_input()
      print ""
      # Test whether any answers are yes
      if not answers_style:
        print "Don't care for a drink, eh?"
        break
      else:
        drink = drink_make(answers_style)
        print "Here is your: {}, which includes:".format(drink_name())
        for ingredient in drink:
          print "A {}".format(ingredient)
    else:
      if drink_questions.index(question) > 0:
        print "See ya later, and you better tip me well or I'll cut off your other leg."
      break
      
if __name__ == "__main__":
  main()
