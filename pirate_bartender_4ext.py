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

# Define customers dictionary - customer name:style answer dictionary
customers = {}

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
  customer_name = ""
  
  # Test whether customer wants a drink
  while raw_input("Greetings you pirate rascal, would you like a drink?  Please answer (y)es or (n)o.") in ["y","yes"]:
    print ""
    # Test whether return customer
    if raw_input("Hey buddy, have I seen you before?") in ["y","yes"]:
      customer_name = raw_input("Ah, what's your name again?")
      # Set drink preferences either with customer info or customer input                     
      if customer_name in customers:
        if raw_input("Good to see you {}. Do you want me to use your past drink preferences?".format(customer_name)) in ["y","yes"]:
          drink_preferences = customers[customer_name]
        else:     
          # Ask customer for preferred drink styles
          drink_preferences = drink_style_input()
      else:
        print "Sorry {}, doesn't ring a bell so let me ask you a few questions.".format(customer_name)
        drink_preferences = drink_style_input()
    else:
      print "Welcome, let's find out what you like."
      drink_preferences = drink_style_input()

    # Test whether any styles are selected
    if not drink_preferences:
      print "Don't care for a drink, eh?"
    else:
      # Make drink and print name and ingredients
      drink = drink_make(drink_preferences)
      print ""
      print "Here is your: {}, which includes:".format(drink_name())
      for ingredient in drink:
        print "A {}".format(ingredient)
      print ""
        
      # Offer to save customer drink preferences if not an existing customer
      if not customer_name:
        customer_name = raw_input("Didn't catch your name. If you give it to me, I'll remember what you like.  Gotta mind like a steel trap.")                               
      # Save customer drink preferences to customers dictionary
      customers[customer_name] = drink_preferences  
                               
      
if __name__ == "__main__":
  main()
