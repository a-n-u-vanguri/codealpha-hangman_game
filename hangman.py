import random

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

categories = {
    "Science": {
        "atom": "The basic unit of matter.",
        "biology": "The study of living organisms.",
        "chemistry": "The branch of science dealing with substances and their reactions.",
        "physics": "The science of matter, energy, and the forces of nature.",
        "quantum": "A branch of physics dealing with subatomic particles.",
        "molecule": "A group of atoms bonded together.",
        "enzyme": "Proteins that speed up chemical reactions in the body.",
        "gravity": "The force that attracts objects toward the center of the Earth."
    },
    "Movies": {
        "inception": "A sci-fi movie about dreams and subconscious.",
        "avatar": "A film set on a distant planet, featuring blue-skinned creatures.",
        "godfather": "A classic film about a mafia family.",
        "jaws": "A thriller about a giant shark.",
        "matrix": "A film about a simulated reality.",
        "joker": "A movie based on the Batman villain.",
        "gladiator": "A film set in ancient Rome about a fighting champion.",
        "titanic": "A movie about a famous sinking ship."
    },
    "Cities": {
        "newyork": "A major city in the United States known for its skyscrapers.",
        "tokyo": "The capital city of Japan, known for its technology and culture.",
        "paris": "The capital of France, known for the Eiffel Tower and art museums.",
        "london": "The capital of the UK, home to Big Ben and Buckingham Palace.",
        "mumbai": "The financial capital of India and the center of Bollywood.",
        "sydney": "A major Australian city known for the Opera House and Harbour Bridge.",
        "moscow": "The capital of Russia, known for the Red Square and Kremlin.",
        "dubai": "A city in the UAE known for its modern architecture and shopping."
    },
    "Famous Landmarks": {
        "eiffel": "The iconic tower in Paris, France.",
        "pyramids": "Ancient structures in Egypt built as tombs for pharaohs.",
        "colosseum": "A large amphitheater in Rome, Italy, used for gladiator games.",
        "greatwall": "A series of fortifications built to protect China from invasions.",
        "tajmahal": "A famous white marble mausoleum in India.",
        "machupicchu": "An ancient Incan city set high in the Andes mountains of Peru.",
        "statueofliberty": "A colossal sculpture in New York Harbor symbolizing freedom.",
        "christredeemer": "A giant statue of Jesus in Rio de Janeiro, Brazil."
    },
    "Music": {
        "beatles": "A famous British rock band from the 1960s.",
        "mozart": "A prolific and influential composer from the Classical era.",
        "beethoven": "A German composer known for his symphonies.",
        "elvis": "An iconic American singer known as the 'King of Rock'.",
        "bach": "A famous German composer and musician from the Baroque period.",
        "madonna": "An American singer known as the 'Queen of Pop'.",
        "nirvana": "A rock band led by Kurt Cobain, popular in the 1990s.",
        "adele": "A British singer known for her soulful voice and ballads."
    },
    "Space": {
        "planet": "A celestial body that orbits a star.",
        "galaxy": "A system of stars, planets, and other space matter.",
        "astronaut": "A person trained for space travel.",
        "blackhole": "A region of space where the gravitational pull is so strong that not even light can escape.",
        "mars": "The fourth planet from the sun, often called the 'Red Planet'.",
        "neptune": "The eighth planet from the Sun, known for its blue color.",
        "telescope": "An instrument used to observe distant objects in space.",
        "asteroid": "A small rocky body that orbits the Sun, mostly found in the asteroid belt."
    }
}

def display_man(wrong_guesses):
    """Display the hangman figure based on incorrect guesses."""
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    """Display the current hint with guessed letters and underscores."""
    print(" ".join(hint))

def display_answer(answer):
    """Display the answer with correctly guessed letters."""
    print(" ".join(answer))

def choose_category():
    """Choose a category from available categories."""
    print("Choose a category:")
    for idx, category in enumerate(categories.keys(), start=1):
        print(f"{idx}. {category}")
    choice = int(input("Enter the number of the category: ")) - 1
    return list(categories.values())[choice], list(categories.keys())[choice]

def main():
    """Main function to run the hangman game."""
    selected_words, category_name = choose_category()
    answer = random.choice(list(selected_words.keys()))
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    print(f"\nCategory: {category_name}")
    print(f"Hint: {selected_words[answer]}")  
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()
