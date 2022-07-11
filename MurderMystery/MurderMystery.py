import random

friends = ["Tera", "Charlie", "Lexus", "Tyler", "Patrick", "Noah", "Leila", "Oliver", "Xena", "Castiel", "Luna", "Lilith", "Lucifer", "Penny", "Butters", "Stacie", "Anita", "Stephanie", "Simona", "Harley", "Karen", "Devon", "Billy", "Riley", "Cosmo", "Kemah", "Danny"]
deaths = ["arrow to the knee", "poisoned by arsenic", "multiple stab wounds", "gunshot wounds", "staged suicide", "christian witch trial", "fed m80's - kaboom", "fed to tigers", "fed to Carol Baskin", "pencil lobotomy", "forced overdose", "pushed off the amarillo tower", "vehicular sabotage", "suffocated in sleep", "crushed by anvil", "slapped to death", "buried alive", "mummified with ace bandages", "flash frozen into a screaming statue", "exlax poisoning", "crushed by tractor tire", "angry mob of grannies", "triple artillery firework to the chest", "drawn and quartered"]
location = ["washed up on lake clarendon shore", "in their front yard", "Rock Island Rail Trail", "Skate Plex", "Wonderland", "in the closet", "Tascosa high courtyard", "Amarillo club", "in a golf course sandpit", "Charlie's backyard", "Lex and Tyler's backyard", "Noah and Tera's tiny patio", "Amarillo College financial aid office", "Some guy's uber car", "Africa", "the Flea Market", "Jason's Deli Salad bar", "Starlight Ranch", "Smushed into Amarillo Blvd", "the highway to hell", "Cadillac Ranch", "Palo Duro Canyon Zipline", "the graveyard, respectfully", "dismembered and put in a wicker basket outside the fire station", "Walmart - clean up on aisle 5", "Fantasy gifts", "Welcome to Chili's", "Escape Warehouse", "Cynergy in the laser tag course", "Western Bowl - center lane"]
alibi = ["Was at the 212", "Wasn't even in town", "Taking grandma to the bingo hall", "Playing DnD with the gang", "Was napping alone", "Took an extra shift on at work", "Had a Grindr date", "Putting up the laundry", "Drinking away their sorrows alone", "Tipping cows", "Was performing an exorcism", "Was storm chasing", "Filming a paranormal investigation", "Writing the book they've been working on for five years.", "No alibi at all", "At a crossfit gym", "Taking a long walk at the park", "Grilling with the friends", "Playing Fortnite and chilling in the discord lounge", "Reading the bible, obviously", "Was at a PRISM club meeting", "At a job interview", "Filing for unemployment", "Spur of the moment road trip to OKC", "at a Sod Poodles game paying too much for drinks", "Scrolling TikTok aimlessly for hours"]

print("Welcome to Murder with Friends. May the odds be ever in your favor." + "\n")
input("Press Enter to continue..." + "\n" + "\n")

print("You wake today, still groggy from a rough night of not enough sleep, and open up your phone screen. ")
print("You're expecting a casual message or two, maybe a few memes, but what you find instead is that your phone has blown up overnight...")
print("There's been a murder... a little too close to home..." + "\n")
input("Press Enter to continue..." + "\n" + "\n")

print(random.choice(friends) + " has been tragically murdered.")
print("How did they die?" + "\n")
input("Press Enter to continue..." + "\n" + "\n")

print(random.choice(deaths))
print("Truly a tragedy. I understand if you want to turn back now. Do you continue?" + "\n")
input("Press Enter to continue..." + "\n" + "\n")

print("Where was the body found?")
print(random.choice(location) + "\n")
print("It's time to solve a murder, friend. Are you ready?" + "\n")
input("Press Enter to continue..." + "\n" + "\n")

print("Who found the body?")
print(random.choice(friends) + "\n")
input("Press Enter to continue..." + "\n" + "\n")

print("Who is the lead investigator?")
print(random.choice(friends) + "\n")
input("Press Enter to continue..." + "\n" + "\n")

print("Who are the suspects? & What are their alibis?" + "\n")
print("The First suspect is " + random.choice(friends))
print("And their alibi? " + random.choice(alibi) + "\n")
input("Press Enter to continue..." + "\n" + "\n")
print("The Second suspect is " + random.choice(friends))
print("And their alibi? " + random.choice(alibi) + "\n")
input("Press Enter to continue..." + "\n" + "\n")
print("The Third suspect is " + random.choice(friends))
print("And their alibi? " + random.choice(alibi) + "\n")
input("Press Enter to continue..." + "\n" + "\n")

print("Hm, interesting. So who actually committed the crime? Who is truly the murderer?")
print(random.choice(friends) + "\n")
input("Press Enter to continue..." + "\n" + "\n")
print("That's the end of the story my friends, but don't forget yo"
      "u can always play again." + "\n")
input("Press Enter to exit the game...")
