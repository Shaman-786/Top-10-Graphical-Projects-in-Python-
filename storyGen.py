import random
def enchanted_forest():
    return """
    In a mystical land far beyond the mountains, where trees whispered ancient secrets, 
    there lay an enchanted forest. Lila, a curious young girl, heard tales of the forest’s 
    magical powers from her grandmother. One bright morning, she ventured into the woods, 
    her heart racing with excitement.

    As she walked deeper, golden rays of sunlight danced through the leaves, illuminating 
    a sparkling stream. Suddenly, Lila spotted a shimmering object half-buried in the ground. 
    It was a crystal flower that glowed with an otherworldly light. Transfixed, she reached 
    down to touch it.

    The moment her fingers brushed the petals, a warm breeze swirled around her. The trees 
    creaked, and she heard a voice echo, "You have awakened the magic, dear Lila. Use it wisely." 
    With newfound powers, Lila learned to communicate with nature, vowing to protect 
    the forest for generations to come.
    """


def lost_treasure():
    return """
    In a sleepy coastal town, there lived a boy named Jake who dreamt of adventure on the high seas. 
    One day, while cleaning his attic, he stumbled upon an old map covered in dust. His heart raced 
    as he realized it showed the location of buried pirate treasure!

    Determined to find it, Jake gathered his friends—Maya, a brave girl with a knack for solving 
    puzzles, and Leo, a tech genius—equipped with a compass and a sturdy boat. Together, they 
    sailed across the choppy waters, the salty breeze filling their sails.

    After hours of searching, they reached a mysterious island. Following the map, they discovered 
    a cave hidden behind a waterfall. Inside, glimmering jewels and gold coins lay strewn about. 
    Their laughter echoed as they filled their bags. Jake realized that the true treasure was the 
    adventure and friendship, making memories that would last a lifetime.
    """


def whisper_in_wind():
    return """
    Amara stood on the cliff’s edge, the wind tugging at her long hair. She had come to bid farewell 
    to her hometown, which held countless memories of her late grandmother. The sun set in vibrant hues, 
    casting a warm glow over the landscape.

    As she closed her eyes, she felt a gentle breeze brush past her cheek. In that moment, she remembered 
    her grandmother’s stories—how she had believed that souls linger in the wind, watching over their loved ones. 
    Amara opened her heart, speaking softly, “I miss you, Grandma. Thank you for every moment we shared.”

    Suddenly, a feather floated down from the sky, landing softly in her palm. Tears filled her eyes as she 
    felt a wave of warmth envelop her. Amara knew her grandmother was with her, guiding her as she 
    stepped into a new chapter of her life.
    """


def clockmakers_secret():
    return """
    In the bustling town of Eldridge, there was a modest clock shop run by an elderly man named Mr. Pennington. 
    His clocks were known for their intricate designs and uncanny ability to keep perfect time. However, the 
    townsfolk whispered about a hidden secret within the shop.

    Curious, a young girl named Eliza decided to investigate. One rainy afternoon, she watched Mr. Pennington 
    work, his hands expertly adjusting gears and springs. As she entered the shop, the delicate chime of the 
    clocks filled the air, creating a symphony of sound.

    “Every clock tells a story, dear Eliza,” Mr. Pennington smiled, noticing her curiosity. “But one holds 
    the greatest secret of all—a clock that can turn back time.” Intrigued, Eliza leaned closer as he revealed 
    a dusty, ornate clock hidden in a corner. With a gentle hand, he wound it, awakening the magic within. 
    As the clock chimed, Eliza felt a rush of memories flooding back—each tick an echo of moments long gone.
    """


def festival_of_lights():
    return """
    In the heart of a vibrant city, the Festival of Lights was approaching. Families decorated their homes 
    with colorful lanterns, and the streets buzzed with excitement. Among them was Ravi, a shy boy who loved 
    painting but always felt invisible.

    This year, he decided to gather his courage and display his artwork at the festival. He painted a mural 
    reflecting hope and joy, capturing the spirit of the festival. As the day of the event arrived, Ravi 
    hung his painting at the center of the square, his heart pounding.

    When the festival began, people gathered around, their faces glowing with admiration. They were captivated 
    by his vibrant colors and heartfelt message. “This is beautiful!” someone exclaimed. For the first time, 
    Ravi felt seen and celebrated. The festival lit up not just the city but also his spirit, showing him that 
    his voice mattered.
    """


def get_story(title):
    # Dictionary to map titles to functions
    stories = {
        "Enchanted Forest": enchanted_forest,
        "Lost Treasure": lost_treasure,
        "Whisper in the Wind": whisper_in_wind,
        "The Clockmaker’s Secret": clockmakers_secret,
        "Festival of Lights": festival_of_lights
    }

    # Get the story based on the title
    return stories.get(title, lambda: "Story not found. Please check the title. 🚫")()


if __name__ == "__main__":
    title = input("Enter the title of the story you want to read: ")
    print(get_story(title))
