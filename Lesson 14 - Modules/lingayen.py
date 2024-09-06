from random import choice

capital = "Lingayen"
bird = "Lovebirds"
flower = "Tulips"
song = "Call it what you want"

def randomfunfact():
    funfacts = [
        "Lingayen is one of the most culturally rich provinces in the Philippines.",
        "Lingayen is famous for its production of bagoong (fermented fish), a popular Filipino condiment.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "The town celebrates Pistay Dayat, or the Sea Festival, every May 1 to honor the bountiful blessings from the sea."
    ]
    
    index = choice([0, 1, 2, 3])  # Choose a random integer between 0 and 3
    print(funfacts[index])         # Print the fun fact at the chosen index


# if __name__ == "__main__":
randomfunfact()
