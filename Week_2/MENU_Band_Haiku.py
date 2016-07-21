import random
#"equus caballus", "ovis aries", "capra aegagrus hircus", "sus scrofa domesticus", "anas platyrhynchos", "gallus gallus domesticus", "bos taurus", "equus africanus asinus", "canis lupus familiaris", "felis catus"

food = ["turkey", "pork", "chicken", "ham", "tuna", "tilapia", "tofu", "quinoa", "rice", "beef"]
colour = ["red", "orange", "yellow", "green", "blue", "purple", "indigo", "black", "white", "pink"]
portion_size = ["miniscual", "itty-bitty", "small", "medium", "big", "large", "massive", "ginormous", "hulk size", "universe size"]
number = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10."]

print("MENU")
for i in range(10):
    portion_size_number = random.randint(0, len(portion_size)-1)
    colour_number = random.randint(0, len(colour)-1)
    food_number = random.randint(0, len(food)-1)
    print(number[i] + portion_size[portion_size_number] + " " + colour[colour_number] + " " + food[food_number])

band_colour = ["unmellow yellow", "banana mania", "razzmatazz", "jazzberry jam", "magic mint", "wild blue yonder", "inchworm", "tickle me pink", "purple monutain's majesty", "mango tango"]
band_animal = ["horse", "donkey", "duck", "chicken", "pig", "goat", "sheep", "rooster", "dog", "cat"]
band_job = ["doctors", "grave diggers", "garden tenders", "computer programmers", "baristas", "mail boys", "pen makers", "authors", "paranormal investigators", "dream catchers"]

print("BAND NAME")
for i in range(10):
    band_colour_number = random.randint(0, len(band_colour)-1)
    band_animal_number = random.randint(0, len(band_animal)-1)
    band_job_number = random.randint(0, len(band_job)-1)
    print(number[i] + band_colour[band_colour_number] + " " + band_animal[band_animal_number] + " " + band_job[band_job_number])

haiku_line_1 = ["Paper towels can be", "When you drive you should", "It's 3001", "Never tickle me", "Warning: if you don't", "You can waddle to", "Nobody knows that", "Mitochondria", "The chicken crossed the", "Juggling can be"]
haiku_line_2 = ["florists if they want to be", "never drive on the wrong side", "and not 3002 yet", "unless you wish to die...yeah", "moon walk, you cannot enter", "the grocery store today", "knees look like baby faces", "are power houses in cells", "street and did make it across", "really really dangerous"]
haiku_line_3 = ["believe in yourself", "because that's stupid", "obviously so", "so please don't do that", "the vicinity", "and waddle back too", "but seriously", "Thanks Mr. Hamner", "

print("HAIKU")
for i in range(10):
    haiku_line_1_number = random.randint(0, len(haiku_line_1)-1)
    haiku_line_2_number = random.randint(0, len(haiku_line_2)-1)
    haiku_line_3_number = random.randint(0, len(haiku_line_3)-1)
    print(number[i] + haiku_line_1[haiku_line_1_number] + " " + haiku_line_2[haiku_line_2_number] + " " + haiku_line_3[haiku_line_3_number])
                
