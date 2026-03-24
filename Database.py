import streamlit as st
import random

anime_database = [  
    {
        "title": "Jujutsu Kaisen",
        "studio": "MAPPA",
        "creator": "Gege Akutami",
        "genre": ["Action", "Dark Fantasy", "Supernatural"],
        "imdb_rating": 8.5,
        "description": "A high schooler joins a secret organization of Jujutsu Sorcerers to eliminate a powerful Curse named Ryomen Sukuna, of whom he becomes the host."
    },
    {
        "title": "One Piece",
        "studio": "Toei Animation",
        "creator": "Eiichiro Oda",
        "genre": ["Action", "Adventure", "Fantasy"],
        "imdb_rating": 9.0,
        "description": "Follows the adventures of Monkey D. Luffy and his pirate crew in order to find the greatest treasure ever left by the legendary Pirate, Gold Roger."
    },
    {
        "title": "Attack on Titan",
        "studio": "Wit Studio",
        "creator": "Hajime Isayama",
        "genre": ["Action", "Dark Fantasy", "Drama"],
        "imdb_rating": 9.1,
        "description": "After his hometown is destroyed, young Eren Yeager vows to cleanse the earth of the giant humanoid Titans that have brought humanity to the brink of extinction."
    },
    {
        "title": "Death Note",
        "studio": "Madhouse",
        "creator": "Tsugumi Ohba",
        "genre": ["Psychological Thriller", "Supernatural", "Mystery"],
        "imdb_rating": 8.9,
        "description": "An intelligent high school student goes on a secret crusade to eliminate criminals after discovering a notebook capable of killing anyone whose name is written into it."
    },
    {
        "title": "Neon Genesis Evangelion",
        "studio": "Gainax",
        "creator": "Hideaki Anno",
        "genre": ["Mecha", "Psychological", "Sci-Fi", "Drama"],
        "imdb_rating": 8.5,
        "description": "Teenagers pilot giant mechs to fight bizarre alien beings called Angels, but the true battle is the crippling existential dread and psychological trauma of the pilots."
    },
    {
        "title": "Vinland Saga",
        "studio": "Wit Studio",
        "creator": "Makoto Yukimura",
        "genre": ["Action", "Adventure", "Historical", "Drama"],
        "imdb_rating": 8.8,
        "description": "A young Viking warrior embarks on a quest for revenge against his father's killer, only to discover the heavy, tragic burden of violence and what it means to be a true warrior."
    },
    {
        "title": "Your Name (Kimi no Na wa)",
        "studio": "CoMix Wave Films",
        "creator": "Makoto Shinkai",
        "genre": ["Romance", "Supernatural", "Drama"],
        "imdb_rating": 8.4,
        "description": "Two teenagers who have never met suddenly begin magically swapping bodies. They must learn to communicate across time and distance to prevent an impending disaster."
    },
    {
        "title": "Samurai Champloo",
        "studio": "Manglobe",
        "creator": "Shinichirō Watanabe",
        "genre": ["Action", "Adventure", "Historical", "Comedy"],
        "imdb_rating": 8.5,
        "description": "A fiercely independent waitress recruits two wildly different ronin—a disciplined traditionalist and a wild, breakdancing vagabond—to help her find the 'samurai who smells of sunflowers.'"
    },
    {
        "title": "Monster",
        "studio": "Madhouse",
        "creator": "Naoki Urasawa",
        "genre": ["Psychological Thriller", "Mystery", "Drama"],
        "imdb_rating": 8.7,
        "description": "A brilliant neurosurgeon's life falls into turmoil after he chooses to save a young boy's life over the city's mayor, only to realize years later that the boy has grown into a terrifying serial killer."
    },
    {
        "title": "Cowboy Bebop",
        "studio": "Sunrise",
        "creator": "Shinichirō Watanabe",
        "genre": ["Sci-Fi", "Space Western", "Action", "Drama"],
        "imdb_rating": 8.9,
        "description": "A ragtag crew of bounty hunters travel the galaxy in their spaceship, the Bebop, trying to make a living while being constantly haunted by the inescapable ghosts of their pasts."
    },
    {
        "title": "Hunter x Hunter",
        "studio": "Madhouse",
        "creator": "Yoshihiro Togashi",
        "genre": ["Action", "Adventure", "Fantasy"],
        "imdb_rating": 9.0,
        "description": "A young boy sets out on a dangerous journey to become a licensed Hunter—an elite member of humanity—in order to track down his father who abandoned him to pursue the same profession."
    },
    {
        "title": "Steins;Gate",
        "studio": "White Fox",
        "creator": "Chiyomaru Shikura",
        "genre": ["Sci-Fi", "Thriller", "Drama"],
        "imdb_rating": 8.8,
        "description": "After accidentally discovering a way to send text messages back in time, a self-proclaimed 'mad scientist' and his friends must outsmart a global conspiracy."
    },
    {
        "title": "Haikyuu!!",
        "studio": "Production I.G",
        "creator": "Haruichi Furudate",
        "genre": ["Sports", "Comedy", "Drama"],
        "imdb_rating": 8.7,
        "description": "Determined to be like the volleyball championship's star player, a short boy joins his school's club, only to find his former middle school rival is now his teammate."
    },
    {
        "title": "Spirited Away",
        "studio": "Studio Ghibli",
        "creator": "Hayao Miyazaki",
        "genre": ["Fantasy", "Adventure", "Family"],
        "imdb_rating": 8.6,
        "description": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a surreal world ruled by gods, witches, and spirits, where she must work to free her parents."
    },
    {
        "title": "Cyberpunk: Edgerunners",
        "studio": "Studio Trigger",
        "creator": "Mike Pondsmith",
        "genre": ["Sci-Fi", "Action", "Tragedy"],
        "imdb_rating": 8.3,
        "description": "A street kid trying to survive in a technology and body modification-obsessed city of the future chooses to stay alive by becoming an edgerunner—a mercenary outlaw."
    },
    {
        "title": "Violet Evergarden",
        "studio": "Kyoto Animation",
        "creator": "Kana Akatsuki",
        "genre": ["Drama", "Fantasy", "Slice of Life"],
        "imdb_rating": 8.4,
        "description": "In the aftermath of a great war, a young female ex-soldier gets a job as a ghostwriter, creating letters that connect people while she tries to understand the meaning of the words 'I love you.'"
    },
    {
        "title": "Demon Slayer",
        "studio": "ufotable",
        "creator": "Koyoharu Gotouge",
        "genre": ["Action", "Dark Fantasy", "Historical"],
        "imdb_rating": 8.6,
        "description": "After his family is slaughtered, a kind-hearted boy joins a secretive society of swordsmen to avenge them and find a cure for his sister, who was turned into a demon."
    },
    {
        "title": "Kaguya-sama: Love is War",
        "studio": "A-1 Pictures",
        "creator": "Aka Akasaka",
        "genre": ["Comedy", "Romance", "Psychological"],
        "imdb_rating": 8.5,
        "description": "Two brilliant, prideful high school student council members who have a mutual crush try to outsmart one another into confessing their love first."
    },
    {
        "title": "Fullmetal Alchemist: Brotherhood",
        "studio": "Bones",
        "creator": "Hiromu Arakawa",
        "genre": ["Action", "Adventure", "Fantasy", "Drama"],
        "imdb_rating": 9.1,
        "description": "Two brothers search for a legendary Philosopher's Stone to restore their damaged bodies after a disastrous, forbidden alchemical experiment goes horrifyingly wrong."
    },
    {
        "title": "Serial Experiments Lain",
        "studio": "Triangle Staff",
        "creator": "Chiaki J. Konaka",
        "genre": ["Psychological", "Sci-Fi", "Mystery", "Horror"],
        "imdb_rating": 8.1,
        "description": "An introverted middle school girl becomes obsessed with an immersive virtual reality network called 'The Wired,' leading to terrifying questions about consciousness, identity, and existence."
    }
]

all_genres = set()
for anime in anime_database:
    for genre in anime["genre"]:
        all_genres.add(genre)
dynamic_genre_list = sorted(list(all_genres))
dynamic_studio_list = ["Any"] + sorted(list(set(anime["studio"] for anime in anime_database)))
dynamic_creator_list = ["Any"] + sorted(list(set(anime["creator"] for anime in anime_database)))

def get_random_recommendation(filtered_list):
    if len(filtered_list) == 0:
        return None
    return random.choice(filtered_list)

def master_anime_filter(database, requested_genres, min_imdb, requested_studio, requested_creator):
    matching_anime = []
    
    # Turn the user's genre choices into a mathematical set
    request_set = set(requested_genres)
    
    # Loop through every single anime in your database
    for anime in database:
        # THE BOOLEAN FLAG: We start by assuming this anime is a perfect match
        is_match = True
        
        # Test 1: Does it have the right genres?
        if len(request_set) > 0:
            anime_genre_set = set(anime["genre"])
            if not request_set.issubset(anime_genre_set):
                is_match = False # Failed! Flag turned to False.
                
        # Test 2: Is the rating high enough?
        if anime["imdb_rating"] < min_imdb:
            is_match = False # Failed!
            
        # Test 3: Is it the right studio? (Ignore if they picked "Any")
        if requested_studio != "Any":
            if anime["studio"] != requested_studio:
                is_match = False # Failed!
                
        # Test 4: Is it the right creator? (Ignore if they picked "Any")
        if requested_creator != "Any":
            if anime["creator"] != requested_creator:
                is_match = False # Failed!
                
        # The Final Verdict: If it survived all 4 tests, the flag is still True!
        if is_match == True:
            matching_anime.append(anime) # Add it to our final list
            
    # Hand the final list of surviving anime back to the website
    return matching_anime

# --- THE FACE (Your Frontend UI) ---

st.title("🎬 Anime Recommender")
st.write("Decision fatigue? Let the algorithm choose your next binge-watch!")

# We split the screen into two columns for a clean, modern look
col1, col2 = st.columns(2)

with col1:
    # Notice we are feeding it 'dynamic_genre_list' now, not a hardcoded list!
    user_genres = st.multiselect("Select Genres:", dynamic_genre_list)
    user_min_rating = st.slider("Minimum IMDb Rating:", 0.0, 10.0, 8.0, 0.1)

with col2:
    # Feeding our dynamic studio and creator lists here
    user_studio = st.selectbox("Preferred Studio:", dynamic_studio_list)
    user_creator = st.selectbox("Specific Creator:", dynamic_creator_list)

# The bridge between the Face and the Brain
if st.button("🎲 Get Recommendation"):
    # 1. We hand the user's choices to the Master Filter
    results = master_anime_filter(anime_database, user_genres, user_min_rating, user_studio, user_creator)
    
    st.divider() 
    
    # 2. We handle the output
    if len(results) == 0:
        st.error("No anime matched all of those exact filters! Try broadening your search.")
    else:
        # We use our randomizer to pick the ultimate winner
        final_pick = get_random_recommendation(results)
        
        # 3. We display the winner beautifully
        st.success("Here is your perfect recommendation!")
        st.subheader(f"📺 {final_pick['title']}")
        st.write(f"**⭐ IMDb Rating:** {final_pick['imdb_rating']}")
        st.write(f"**🏢 Studio:** {final_pick['studio']}")
        st.write(f"**👤 Creator:** {final_pick['creator']}")
    
        st.write("---")
        st.write(f"**📖 Synopsis:** {final_pick['description']}")
        st.balloons()