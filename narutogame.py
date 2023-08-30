print("Welcome Ninja to the Village Hidden in the Leaves!")

# Initial path choice 
print("Choose your path:")
print("A) Go left to the Ninja Academy")
print("B) Go right to the Ramen Shop")
print("C) Go straight to the Forest")

path = input("Enter A, B or C:\n").upper()

if path == "A":
    choice1 = "academy"
elif path == "B":
    choice1 = "ramen"
else:
    choice1 = "forest"

# Academy story

if choice1 == "academy":

    print("You arrive at the Ninja Academy.")
    print("What do you want to do?")

    print("A) Train hard")
    print("B) Sleep in and rest")
    print("C) Skip class and go home")

    action = input("Choose A, B or C:\n").upper()

    if action == "A": 
        print("You train tirelessly, pushing your limits.")
        print("Your hard work pays off, and you improve your skills!")
    elif action == "B":
        print("You decide to rest and recover from your previous missions.")
        print("A well-deserved rest leaves you refreshed and ready for new challenges!")
    else:
        print("You chose to skip class and head home.")
        print("However, your sensei finds out and scolds you for your lack of dedication.")
        print("You realize the importance of commitment and training. Game over!")

    print("After your initial choice, time passes and new challenges await!")

    print("Question 2:")
    print("A) Accept a sparring challenge")
    print("B) Study ancient scrolls")
    print("C) Take a break")

    choice2 = input("Choose A, B or C:\n").upper()

    if choice2 == "A":
        print("You engage in intense sparring matches, learning valuable combat techniques.")
        print("Your skills improve significantly!")
    elif choice2 == "B":
        print("You spend hours studying the ancient scrolls of ninja wisdom.")
        print("Your knowledge deepens, enhancing your strategic thinking!")
    else:
        print("You decide to take a break and chat with fellow students.")
        print("While relaxing, you learn about their experiences and gain valuable insights!")

    print("Question 3:")
    print("A) Participate in a stealth exercise")
    print("B) Attend a lecture on history")
    print("C) Explore the academy grounds")

    choice3 = input("Choose A, B or C:\n").upper()

    if choice3 == "A":
        print("You excel in the stealth exercise, moving silently and avoiding detection.")
        print("Your mastery of stealth grows, making you a shadow in the night!")
    elif choice3 == "B":
        print("You attentively listen to the history lecture, absorbing tales of legendary ninjas.")
        print("The stories inspire you, sparking your imagination!")
    else:
        print("You wander the academy grounds, stumbling upon hidden training spots.")
        print("You discover secret training techniques, enhancing your skills!")

    # Continue with more questions...

    print("Question 4:")
    print("A) Join a teamwork exercise")
    print("B) Meditate for inner focus")
    print("C) Help organize an event")

    choice4 = input("Choose A, B or C:\n").upper()

    if choice4 == "A":
        print("You work together with your teammates, honing your coordination and communication.")
        print("Your teamwork improves, making you an invaluable asset!")
    elif choice4 == "B":
        print("You enter deep meditation, finding inner peace and clarity.")
        print("Your mental fortitude strengthens, allowing you to remain calm under pressure!")
    else:
        print("You assist in organizing a ninja event, gaining experience in event management.")
        print("Your organizational skills grow, and you make valuable connections!")

    print("Question 5:")
    print("A) Engage in a one-on-one duel")
    print("B) Learn the art of disguise")
    print("C) Teach a younger student")

    choice5 = input("Choose A, B or C:\n").upper()

    if choice5 == "A":
        print("You engage in a challenging duel, testing your combat prowess.")
        print("The duel hones your reflexes and adaptability, making you a formidable fighter!")
    elif choice5 == "B":
        print("You immerse yourself in the art of disguise, mastering the ability to change your appearance.")
        print("Your disguise skills become extraordinary, granting you an advantage in covert operations!")
    else:
        print("You take on the role of a mentor, teaching younger students basic ninja skills.")
        print("Your teaching abilities shine, and you find joy in passing on your knowledge!")

    print("Question 6:")
    print("A) Undertake a night mission")
    print("B) Experiment with new jutsu")
    print("C) Rest and reflect")

    choice6 = input("Choose A, B or C:\n").upper()

    if choice6 == "A":
        print("You embark on a challenging night mission, navigating the darkness with precision.")
        print("Your night vision and adaptability improve significantly!")
    elif choice6 == "B":
        print("You dedicate time to experimenting with new jutsu, expanding your ninja techniques.")
        print("You develop innovative jutsu, setting new standards in combat!")
    else:
        print("You take a moment to rest and reflect on your journey so far.")
        print("Through introspection, you gain a deeper understanding of yourself and your goals!")

    # Continue with more questions...

    print("Question 7:")
    print("A) Collaborate on a group project")
    print("B) Attend a lecture on tactics")
    print("C) Explore the village for inspiration")

    choice7 = input("Choose A, B or C:\n").upper()

    if choice7 == "A":
        print("You work closely with a group on a challenging project, learning to coordinate and delegate.")
        print("Your leadership skills improve, and you become an effective team leader!")
    elif choice7 == "B":
        print("You attend a tactical lecture, delving into the intricacies of battle strategy.")
        print("Your strategic thinking becomes unparalleled, allowing you to outmaneuver opponents!")
    else:
        print("You explore the village, immersing yourself in its culture and gaining fresh perspectives.")
        print("Your creativity flourishes, and you adapt newfound ideas into your training!")

    print("Question 8:")
    print("A) Assist in training younger students")
    print("B) Attend a mentorship session")
    print("C) Investigate a mysterious occurrence")

    choice8 = input("Choose A, B or C:\n").upper()

    if choice8 == "A":
        print("You spend time training younger students, imparting your knowledge and skills.")
        print("Your teaching abilities reach new heights, and you become a beloved mentor!")
    elif choice8 == "B":
        print("You attend a mentorship session, receiving guidance from experienced ninja.")
        print("The mentorship shapes your outlook and broadens your horizons!")
    else:
        print("You uncover a mysterious occurrence in the village, putting your investigative skills to the test.")
        print("Your intuition and deduction abilities shine, leading you to the truth!")

    print("Question 9:")
    print("A) Participate in a ninja tournament")
    print("B) Devote time to master a specific jutsu")
    print("C) Complete a challenging obstacle course")

    choice9 = input("Choose A, B or C:\n").upper()

    if choice9 == "A":
        print("You compete in a thrilling ninja tournament, showcasing your diverse abilities.")
        print("Your performance captures attention, and you earn recognition as a skilled ninja!")
    elif choice9 == "B":
        print("You dedicate yourself to mastering a specific jutsu, refining its execution.")
        print("Your jutsu mastery becomes extraordinary, setting you apart in battles!")
    else:
        print("You conquer a challenging obstacle course, demonstrating your physical prowess.")
        print("Your agility and endurance reach peak levels, making you a force to be reckoned with!")

    print("Your time at the Ninja Academy has been a journey of growth and learning.")
    print("With newfound skills and experiences, you are ready to face the challenges of the ninja world!")


# Ramen story 

elif choice1 == "ramen":

    print("You arrive at the Ramen Shop.")
    
    print("A) Eat 5 bowls of ramen")
    print("B) Eat 2 bowls of ramen")
    print("C) Eat too much ramen")
    
    amount = input("Choose A, B or C:\n").upper()
    
    if amount == "A":
        print("You devour 5 bowls of ramen with gusto.")
        print("You're full but energized, ready for any mission!")
    elif amount == "B":
        print("You enjoy 2 bowls of ramen, savoring each bite.")
        print("Your moderate eating keeps you light on your feet!")
    else:
        print("You give in to temptation and eat too much ramen.")
        print("You feel sluggish and unable to move. Game over!")

    print("After your satisfying ramen meal, your adventure continues!")

    print("Question 2:")
    print("A) Visit the local market")
    print("B) Train at the dojo")
    print("C) Help a villager in need")

    choice2 = input("Choose A, B or C:\n").upper()

    if choice2 == "A":
        print("You explore the bustling market, discovering rare items and meeting interesting people.")
        print("Your curiosity rewards you with valuable finds!")
    elif choice2 == "B":
        print("You head to the dojo and train diligently, refining your combat techniques.")
        print("Your skills improve further, making you a more formidable ninja!")
    else:
        print("You lend a hand to a villager in need, earning their gratitude and respect.")
        print("Your kindness resonates, and you forge strong bonds in the village!")

    print("Question 3:")
    print("A) Attend a cultural festival")
    print("B) Investigate a local mystery")
    print("C) Rest and enjoy the scenery")

    choice3 = input("Choose A, B or C:\n").upper()

    if choice3 == "A":
        print("You immerse yourself in the vibrant cultural festival, experiencing the village's traditions.")
        print("The festival brings joy to your heart and strengthens your connection to the village!")
    elif choice3 == "B":
        print("You become intrigued by a local mystery and embark on an investigation.")
        print("Your sharp instincts lead you to unravel secrets and unveil the truth!")
    else:
        print("You take a moment to rest and enjoy the beauty of the village landscape.")
        print("The tranquility refreshes your spirit, making you ready for upcoming challenges!")

    # Continue with more questions...
    print("Question 4:")
    print("A) Participate in a village competition")
    print("B) Help organize a community event")
    print("C) Explore the outskirts of the village")

    choice4 = input("Choose A, B or C:\n").upper()

    if choice4 == "A":
        print("You join the village competition and showcase your skills.")
        print("Your performance captures attention, and you earn recognition as a talented ninja!")
    elif choice4 == "B":
        print("You play a vital role in organizing a community event, bringing people together.")
        print("Your event planning skills shine, and you foster a sense of unity!")
    else:
        print("You venture to the outskirts of the village, uncovering hidden paths and secrets.")
        print("Your exploration leads to discoveries that deepen your connection to the land!")

    print("Question 5:")
    print("A) Train with a fellow ninja")
    print("B) Learn about local legends")
    print("C) Offer assistance to a traveler")

    choice5 = input("Choose A, B or C:\n").upper()

    if choice5 == "A":
        print("You engage in joint training with a fellow ninja, exchanging techniques and knowledge.")
        print("Your collaborative efforts result in shared growth and enhanced skills!")
    elif choice5 == "B":
        print("You listen to tales of local legends and myths, expanding your cultural understanding.")
        print("The stories inspire you and influence your perspective!")
    else:
        print("You help a weary traveler by offering guidance and support.")
        print("Your kindness leaves a lasting impression, and you gain a valuable ally!")

    print("Question 6:")
    print("A) Join a volunteer project")
    print("B) Study herbal remedies")
    print("C) Investigate a rumored treasure")

    choice6 = input("Choose A, B or C:\n").upper()

    if choice6 == "A":
        print("You contribute to a volunteer project, making a positive impact on the community.")
        print("Your dedication to helping others leaves a legacy of goodwill!")
    elif choice6 == "B":
        print("You immerse yourself in the study of herbal remedies, learning to heal with nature.")
        print("Your knowledge of herbs and their medicinal uses becomes invaluable!")
    else:
        print("You embark on a treasure hunt to uncover a rumored hidden treasure.")
        print("Your perseverance pays off, as you unearth a treasure with historical significance!")

    # Continue with more questions...
    print("Question 7:")
    print("A) Join a group of travelers")
    print("B) Train in a new style of combat")
    print("C) Create a piece of artwork")

    choice7 = input("Choose A, B or C:\n").upper()

    if choice7 == "A":
        print("You decide to join a group of fellow travelers on their journey.")
        print("Through shared experiences, you forge bonds and gain diverse insights!")
    elif choice7 == "B":
        print("You explore a new style of combat training, broadening your skillset.")
        print("Your adaptability grows, making you a more versatile and unpredictable fighter!")
    else:
        print("You channel your creativity into creating a unique piece of artwork.")
        print("Your creation resonates with others, sparking emotions and inspiration!")

    print("Question 8:")
    print("A) Mentor a younger ninja")
    print("B) Solve a village dispute")
    print("C) Embark on a solo mission")

    choice8 = input("Choose A, B or C:\n").upper()

    if choice8 == "A":
        print("You take on the role of a mentor, guiding a younger ninja on their path.")
        print("Your guidance shapes their growth, and you leave a lasting positive impact!")
    elif choice8 == "B":
        print("You step in to mediate and solve a dispute within the village.")
        print("Your diplomacy and fairness bring harmony and resolution to the situation!")
    else:
        print("You embark on a challenging solo mission, testing your self-reliance.")
        print("Your successful completion boosts your confidence and independence!")

    print("Question 9:")
    print("A) Attend a festival in a neighboring village")
    print("B) Master a specialized technique")
    print("C) Help rebuild a damaged structure")

    choice9 = input("Choose A, B or C:\n").upper()

    if choice9 == "A":
        print("You visit a neighboring village's festival, experiencing their traditions.")
        print("The cross-cultural experience broadens your horizons and fosters friendship!")
    elif choice9 == "B":
        print("You devote time to mastering a specialized technique, achieving mastery.")
        print("Your expertise in this technique sets you apart as a specialist in its use!")
    else:
        print("You contribute to the rebuilding of a damaged structure in the village.")
        print("Your efforts restore hope and symbolize the strength of unity!")

    print("Your time in the village has been enriching, and you've grown in many ways.")
    print("With new skills and connections, you're prepared for the challenges that lie ahead!")


# Forest story
else:

    print("You arrive at the Forest.")
    print("What do you want to do?")
    
    print("A) Forage for food")
    print("B) Find water")
    print("C) Climb a tall tree")
    
    action = input("Choose A, B or C:\n").upper()

    if action == "A":
        print("You successfully forage for berries and edible plants.")
        print("Your survival skills are impressive, and you're well-fed!")
    elif action == "B":
        print("You locate a clean water source and quench your thirst.")
        print("Staying hydrated, you're ready to face any challenge!")
    else:
        print("You attempt to climb a tall tree to get a better view.")
        print("Unfortunately, you slip and fall from the tree. Game over!")

    print("After your forest exploration, your journey continues!")

    print("Question 2:")
    print("A) Build a shelter")
    print("B) Track animal footprints")
    print("C) Search for medicinal herbs")

    choice2 = input("Choose A, B or C:\n").upper()

    if choice2 == "A":
        print("You build a sturdy shelter from available resources, protecting yourself from the elements.")
        print("Your survival instincts shine, and you create a comfortable haven!")
    elif choice2 == "B":
        print("You follow animal footprints and uncover the habits of local wildlife.")
        print("Your tracking skills improve, making you an adept hunter and observer!")
    else:
        print("You search for medicinal herbs, discovering potent remedies for various ailments.")
        print("Your knowledge of herbal medicine grows, allowing you to heal effectively!")

    print("Question 3:")
    print("A) Construct traps for hunting")
    print("B) Navigate using the stars")
    print("C) Craft tools from natural materials")

    choice3 = input("Choose A, B or C:\n").upper()

    if choice3 == "A":
        print("You skillfully construct traps for hunting, successfully catching your prey.")
        print("Your resourcefulness as a hunter and gatherer increases, ensuring your sustenance!")
    elif choice3 == "B":
        print("You navigate through the forest using the stars, mastering celestial guidance.")
        print("Your navigational skills become precise, and you find your way effortlessly!")
    else:
        print("You craft essential tools from natural materials, enhancing your survival abilities.")
        print("Your adaptability and craftsmanship empower you to thrive in the wilderness!")

    # Continue with more questions...
    print("Question 4:")
    print("A) Fish in a nearby stream")
    print("B) Build a signal fire")
    print("C) Explore a hidden cave")

    choice4 = input("Choose A, B or C:\n").upper()

    if choice4 == "A":
        print("You fish in a nearby stream, catching plenty of fish for sustenance.")
        print("Your fishing skills improve, providing a reliable source of food!")
    elif choice4 == "B":
        print("You build a signal fire, sending a visible message to potential rescuers.")
        print("Your resourcefulness and communication skills attract attention and aid!")
    else:
        print("You explore a hidden cave, uncovering mysteries and valuable resources.")
        print("Your curiosity is rewarded with newfound knowledge and treasures!")

    print("Question 5:")
    print("A) Set up a primitive shelter")
    print("B) Identify edible plants")
    print("C) Construct a raft to cross a river")

    choice5 = input("Choose A, B or C:\n").upper()

    if choice5 == "A":
        print("You construct a primitive but effective shelter, protecting yourself from the elements.")
        print("Your survival skills are impressive, and you make a cozy home!")
    elif choice5 == "B":
        print("You identify various edible plants, expanding your foraging repertoire.")
        print("Your knowledge of local flora deepens, ensuring your sustenance!")
    else:
        print("You construct a sturdy raft and successfully cross a challenging river.")
        print("Your ingenuity and engineering skills allow you to overcome obstacles!")

    print("Question 6:")
    print("A) Befriend a woodland creature")
    print("B) Follow the sound of a distant waterfall")
    print("C) Climb a steep hill for a better view")

    choice6 = input("Choose A, B or C:\n").upper()

    if choice6 == "A":
        print("You befriend a friendly woodland creature, gaining a loyal companion.")
        print("Your bond with nature grows, and you gain a trustworthy ally!")
    elif choice6 == "B":
        print("You follow the sound of a distant waterfall, discovering a hidden oasis.")
        print("Your exploration reveals a serene spot of beauty and tranquility!")
    else:
        print("You climb a steep hill, gaining an elevated view of the forest surroundings.")
        print("Your vantage point offers insights, helping you navigate the wilderness!")

    # Continue with more questions...
    print("Question 7:")
    print("A) Build a rudimentary fishing trap")
    print("B) Follow the path of migrating birds")
    print("C) Create a map of the forest")

    choice7 = input("Choose A, B or C:\n").upper()

    if choice7 == "A":
        print("You construct a simple fishing trap, successfully catching fish for sustenance.")
        print("Your ingenuity as a survivalist grows, ensuring a steady food source!")
    elif choice7 == "B":
        print("You follow the path of migrating birds, leading you to a hidden treasure.")
        print("Your keen observation and intuition reward you with valuable discoveries!")
    else:
        print("You create a detailed map of the forest, marking significant landmarks.")
        print("Your mapping skills improve, providing valuable navigation resources!")

    print("Question 8:")
    print("A) Craft a makeshift bow and arrows")
    print("B) Build a shelter from tree branches")
    print("C) Search for rare herbs in a remote area")

    choice8 = input("Choose A, B or C:\n").upper()

    if choice8 == "A":
        print("You craft a makeshift bow and arrows, honing your hunting skills.")
        print("Your archery abilities become formidable, allowing precise target hits!")
    elif choice8 == "B":
        print("You build a shelter from sturdy tree branches, creating a comfortable refuge.")
        print("Your construction skills shine, providing protection against the elements!")
    else:
        print("You search for rare herbs in a remote area, discovering potent remedies.")
        print("Your herbal knowledge expands, making you a skilled healer in the wild!")

    print("Question 9:")
    print("A) Befriend a wise old hermit")
    print("B) Discover an ancient ruin")
    print("C) Traverse a treacherous mountain pass")

    choice9 = input("Choose A, B or C:\n").upper()

    if choice9 == "A":
        print("You befriend a wise old hermit who imparts ancient wisdom to you.")
        print("His guidance enhances your understanding of nature and life!")
    elif choice9 == "B":
        print("You stumble upon an ancient ruin hidden deep in the forest.")
        print("The discovery unlocks ancient secrets and knowledge!")
    else:
        print("You bravely traverse a treacherous mountain pass, testing your endurance.")
        print("Your determination and resilience allow you to conquer challenges!")

    print("Your time in the forest has been a transformative journey.")
    print("With newfound skills and connections to nature, you're prepared for the unknown!")

print("Thanks for playing!")
