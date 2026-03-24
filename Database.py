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
        "title": "Naruto: Shippuden",
        "studio": "Pierrot",
        "creator": "Masashi Kishimoto",
        "genre": ["Action", "Adventure", "Fantasy"],
        "imdb_rating": 8.7,
        "description": "An older, more powerful Naruto returns to his village to rescue his friend from the darkness and face a rising, apocalyptic threat."
    },
    {
        "title": "Bleach",
        "studio": "Pierrot",
        "creator": "Tite Kubo",
        "genre": ["Action", "Supernatural", "Adventure"],
        "imdb_rating": 8.2,
        "description": "A teenager with the ability to see ghosts gains the powers of a Soul Reaper and must protect humanity from evil spirits called Hollows."
    },
    {
        "title": "My Hero Academia",
        "studio": "Bones",
        "creator": "Kohei Horikoshi",
        "genre": ["Action", "Superhero", "Comedy"],
        "imdb_rating": 8.3,
        "description": "In a world where 80% of the population has superpowers, a boy born without them inherits the power of the world's greatest hero."
    },
    {
        "title": "Chainsaw Man",
        "studio": "MAPPA",
        "creator": "Tatsuki Fujimoto",
        "genre": ["Action", "Dark Fantasy", "Horror"],
        "imdb_rating": 8.4,
        "description": "A desperately poor young man makes a contract with a chainsaw dog demon, reviving him from the dead to become a brutal devil hunter."
    },
    {
        "title": "Mob Psycho 100",
        "studio": "Bones",
        "creator": "ONE",
        "genre": ["Action", "Comedy", "Supernatural"],
        "imdb_rating": 8.6,
        "description": "A socially awkward middle school boy with god-level psychic powers just wants to live a normal life and impress his crush."
    },
    {
        "title": "One Punch Man",
        "studio": "Madhouse",
        "creator": "ONE",
        "genre": ["Action", "Comedy", "Superhero"],
        "imdb_rating": 8.7,
        "description": "An overwhelmingly powerful hero who can defeat any opponent with a single punch struggles to find meaning and excitement in his life."
    },
    {
        "title": "JoJo's Bizarre Adventure",
        "studio": "David Production",
        "creator": "Hirohiko Araki",
        "genre": ["Action", "Supernatural", "Adventure", "Fantasy"],
        "imdb_rating": 8.5,
        "description": "The multi-generational, globe-trotting saga of the Joestar family, who use unique supernatural powers to battle bizarre and terrifying villains."
    },
    {
        "title": "Code Geass",
        "studio": "Sunrise",
        "creator": "Ichiro Okouchi",
        "genre": ["Mecha", "Psychological Thriller", "Sci-Fi", "Action"],
        "imdb_rating": 8.7,
        "description": "An exiled prince gains a mysterious power that allows him to command anyone to do his bidding, which he uses to lead a massive rebellion against a global empire."
    },
    {
        "title": "Gurren Lagann",
        "studio": "Gainax",
        "creator": "Hiroyuki Imaishi",
        "genre": ["Mecha", "Action", "Sci-Fi", "Comedy"],
        "imdb_rating": 8.3,
        "description": "Two brothers from a subterranean village break through to the surface and pilot a giant mech to free humanity from the tyrannical Spiral King."
    },
    {
        "title": "Fate/Zero",
        "studio": "ufotable",
        "creator": "Gen Urobuchi",
        "genre": ["Action", "Dark Fantasy", "Supernatural"],
        "imdb_rating": 8.2,
        "description": "Seven mages summon legendary historical heroes to fight to the death in a brutal, secret war for the wish-granting Holy Grail."
    },
    {
        "title": "A Silent Voice",
        "studio": "Kyoto Animation",
        "creator": "Yoshitoki Oima",
        "genre": ["Drama", "Romance", "Slice of Life"],
        "imdb_rating": 8.1,
        "description": "A former elementary school bully seeks out the deaf girl he tormented years ago in a desperate attempt to make amends and find redemption."
    },
    {
        "title": "Princess Mononoke",
        "studio": "Studio Ghibli",
        "creator": "Hayao Miyazaki",
        "genre": ["Fantasy", "Adventure", "Historical"],
        "imdb_rating": 8.3,
        "description": "A cursed prince journeys to find a cure and finds himself caught in a massive war between forest gods and a human mining colony."
    },
    {
        "title": "Akira",
        "studio": "TMS Entertainment",
        "creator": "Katsuhiro Otomo",
        "genre": ["Sci-Fi", "Cyberpunk", "Action"],
        "imdb_rating": 8.0,
        "description": "In a dystopian Neo-Tokyo, a biker gang leader must save his friend who has developed dangerous, god-like telekinetic powers."
    },
    {
        "title": "Psycho-Pass",
        "studio": "Production I.G",
        "creator": "Gen Urobuchi",
        "genre": ["Sci-Fi", "Cyberpunk", "Psychological Thriller"],
        "imdb_rating": 8.2,
        "description": "In a future where a computer network constantly measures citizens' criminal intent, an idealistic rookie inspector begins to question the system."
    },
    {
        "title": "Erased",
        "studio": "A-1 Pictures",
        "creator": "Kei Sanbe",
        "genre": ["Mystery", "Psychological Thriller", "Supernatural"],
        "imdb_rating": 8.5,
        "description": "A man with the involuntary ability to jump back in time must use his power to solve the abduction and murder of his childhood classmate."
    },
    {
        "title": "Re:Zero - Starting Life in Another World",
        "studio": "White Fox",
        "creator": "Tappei Nagatsuki",
        "genre": ["Isekai", "Dark Fantasy", "Psychological Thriller"],
        "imdb_rating": 8.0,
        "description": "A teenager is transported to a fantasy world and discovers he has the agonizing power to rewind time by dying."
    },
    {
        "title": "KonoSuba",
        "studio": "Studio Deen",
        "creator": "Natsume Akatsuki",
        "genre": ["Isekai", "Comedy", "Fantasy"],
        "imdb_rating": 7.9,
        "description": "After a pathetic death, a boy is reincarnated in a fantasy world with a useless goddess, a masochistic knight, and an explosion-obsessed wizard."
    },
    {
        "title": "Sword Art Online",
        "studio": "A-1 Pictures",
        "creator": "Reki Kawahara",
        "genre": ["Action", "Sci-Fi", "Romance", "Adventure"],
        "imdb_rating": 7.5,
        "description": "Players of a highly immersive virtual reality MMORPG discover they are trapped inside the game, and dying in the game means dying in real life."
    },
    {
        "title": "Fruits Basket",
        "studio": "TMS Entertainment",
        "creator": "Natsuki Takaya",
        "genre": ["Romance", "Comedy", "Drama", "Supernatural"],
        "imdb_rating": 8.6,
        "description": "An orphaned high school girl moves in with a wealthy family and discovers their dark secret: they transform into animals of the Chinese Zodiac when hugged."
    },
    {
        "title": "Toradora!",
        "studio": "J.C.Staff",
        "creator": "Yuyuko Takemiya",
        "genre": ["Romance", "Comedy", "Slice of Life"],
        "imdb_rating": 8.0,
        "description": "An intimidating but gentle boy and a tiny but ferocious girl form an unlikely alliance to help each other confess to their respective crushes."
    },
    {
        "title": "Your Lie in April",
        "studio": "A-1 Pictures",
        "creator": "Naoshi Arakawa",
        "genre": ["Romance", "Drama", "Music"],
        "imdb_rating": 8.5,
        "description": "A former piano prodigy who lost his ability to hear the piano after a trauma has his world turned upside down by a free-spirited violinist."
    },
    {
        "title": "Horimiya",
        "studio": "CloverWorks",
        "creator": "HERO",
        "genre": ["Romance", "Comedy", "Slice of Life"],
        "imdb_rating": 8.1,
        "description": "Two high schoolers who hide their true personalities at school discover each other's secrets and form a deeply supportive bond."
    },
    {
        "title": "Kuroko's Basketball",
        "studio": "Production I.G",
        "creator": "Tadatoshi Fujimaki",
        "genre": ["Sports", "Action", "Comedy"],
        "imdb_rating": 8.2,
        "description": "The phantom sixth member of a legendary middle school basketball team joins a new high school with the goal of defeating his former, overpowered teammates."
    },
    {
        "title": "Blue Lock",
        "studio": "8bit",
        "creator": "Muneyuki Kaneshiro",
        "genre": ["Sports", "Psychological", "Action"],
        "imdb_rating": 8.2,
        "description": "Japan's top high school soccer strikers are locked in a brutal, prison-like training facility to create the ultimate, ego-driven forward for the national team."
    },
    {
        "title": "Hajime no Ippo",
        "studio": "Madhouse",
        "creator": "George Morikawa",
        "genre": ["Sports", "Action", "Comedy"],
        "imdb_rating": 8.8,
        "description": "A timid, heavily bullied high schooler discovers a hidden talent for boxing and begins a grueling journey to the professional ring."
    },
    {
        "title": "Great Teacher Onizuka",
        "studio": "Pierrot",
        "creator": "Tooru Fujisawa",
        "genre": ["Comedy", "Drama", "Slice of Life"],
        "imdb_rating": 8.5,
        "description": "A former gang member decides to become the greatest high school teacher in the world, using highly unconventional methods to help his troubled students."
    },
    {
        "title": "Assassination Classroom",
        "studio": "Lerche",
        "creator": "Yusei Matsui",
        "genre": ["Action", "Comedy", "Sci-Fi"],
        "imdb_rating": 8.0,
        "description": "A class of misfits must learn how to assassinate their homeroom teacher—a yellow, tentacled alien who has threatened to destroy the Earth."
    },
    {
        "title": "Dr. Stone",
        "studio": "TMS Entertainment",
        "creator": "Riichiro Inagaki",
        "genre": ["Sci-Fi", "Adventure", "Comedy"],
        "imdb_rating": 8.1,
        "description": "Thousands of years after a mysterious flash turns all of humanity to stone, a brilliant teenager awakens and vows to rebuild civilization using science."
    },
    {
        "title": "Made in Abyss",
        "studio": "Kinema Citrus",
        "creator": "Akihito Tsukushi",
        "genre": ["Adventure", "Dark Fantasy", "Sci-Fi", "Mystery"],
        "imdb_rating": 8.4,
        "description": "A young girl and a robot boy descend into a massive, uncharted, and terrifyingly dangerous chasm in the earth searching for her mother."
    },
    {
        "title": "The Promised Neverland",
        "studio": "CloverWorks",
        "creator": "Kaiu Shirai",
        "genre": ["Psychological Thriller", "Mystery", "Horror", "Sci-Fi"],
        "imdb_rating": 8.3,
        "description": "A group of highly intelligent orphans discover the horrifying truth about their idyllic orphanage and must engineer a flawless escape plan."
    },
    {
        "title": "Parasyte: The Maxim",
        "studio": "Madhouse",
        "creator": "Hitoshi Iwaaki",
        "genre": ["Action", "Sci-Fi", "Horror", "Psychological"],
        "imdb_rating": 8.3,
        "description": "A high schooler's right hand is infected by an alien parasite, forcing the two to form an uneasy alliance to survive against other, more hostile parasites."
    },
    {
        "title": "Black Lagoon",
        "studio": "Madhouse",
        "creator": "Rei Hiroe",
        "genre": ["Action", "Crime", "Adventure"],
        "imdb_rating": 7.9,
        "description": "A mild-mannered Japanese businessman is kidnapped by modern-day pirates and eventually decides to join their mercenary crew in a lawless city."
    },
    {
        "title": "Bocchi the Rock!",
        "studio": "CloverWorks",
        "creator": "Aki Hamaji",
        "genre": ["Comedy", "Music", "Slice of Life"],
        "imdb_rating": 8.4,
        "description": "A girl with severe social anxiety who plays guitar alone in her closet is suddenly drafted into a desperate indie rock band."
    },
    {
        "title": "Oshi no Ko",
        "studio": "Doga Kobo",
        "creator": "Aka Akasaka",
        "genre": ["Drama", "Supernatural", "Mystery", "Psychological"],
        "imdb_rating": 8.3,
        "description": "A doctor is murdered and reincarnated as the child of his favorite pop idol, plunging him into the dark, manipulative underbelly of the entertainment industry."
    },
    {
        "title": "Ghost in the Shell: Stand Alone Complex",
        "studio": "Production I.G",
        "creator": "Masamune Shirow",
        "genre": ["Sci-Fi", "Cyberpunk", "Action", "Mystery"],
        "imdb_rating": 8.5,
        "description": "An elite cybernetics police force investigates highly complex cyber-crimes and terrorism in a futuristic Japan."
    },
    {
        "title": "Gintama",
        "studio": "Sunrise",
        "creator": "Hideaki Sorachi",
        "genre": ["Comedy", "Action", "Sci-Fi", "Historical"],
        "imdb_rating": 8.7,
        "description": "In an alternate-history Japan conquered by aliens, an eccentric samurai and his oddball crew take on odd jobs to make ends meet."
    },
    {
        "title": "Mushoku Tensei: Jobless Reincarnation",
        "studio": "Studio Bind",
        "creator": "Rifujin na Magonote",
        "genre": ["Isekai", "Fantasy", "Adventure", "Drama"],
        "imdb_rating": 8.3,
        "description": "A socially outcast man dies and is reincarnated in a fantasy world as a baby, determined to live his new life without regrets."
    },
    {
        "title": "Nana",
        "studio": "Madhouse",
        "creator": "Ai Yazawa",
        "genre": ["Drama", "Romance", "Music", "Slice of Life"],
        "imdb_rating": 8.5,
        "description": "Two wildly different young women, both named Nana, move to Tokyo, become roommates, and navigate the extreme highs and lows of adulthood, love, and the music industry."
    },
    {
        "title": "Ping Pong the Animation",
        "studio": "Tatsunoko Production",
        "creator": "Taiyo Matsumoto",
        "genre": ["Sports", "Psychological", "Drama"],
        "imdb_rating": 8.6,
        "description": "An incredibly unique visual exploration of two childhood friends navigating the intense, psychologically demanding world of competitive high school table tennis."
    },
    {
        "title": "March Comes In Like A Lion",
        "studio": "Shaft",
        "creator": "Chica Umino",
        "genre": ["Drama", "Slice of Life", "Psychological"],
        "imdb_rating": 8.3,
        "description": "A deeply depressed, orphaned teenage professional shogi player slowly learns to open up and heal through his relationship with three warm-hearted sisters."
    }
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
    
    request_set = set(requested_genres)
    
    for anime in database:
        is_match = True
        
        if len(request_set) > 0:
            anime_genre_set = set(anime["genre"])
            if not request_set.issubset(anime_genre_set):
                is_match = False
                
        if anime["imdb_rating"] < min_imdb:
            is_match = False #fail
         
        if requested_studio != "Any":
            if anime["studio"] != requested_studio:
                is_match = False #fail
                
        if requested_creator != "Any":
            if anime["creator"] != requested_creator:
                is_match = False #fail
            
        if is_match == True:
            matching_anime.append(anime) #main list
            
    return matching_anime

st.title("🎬 Anime Recommender")
st.write("Decision fatigue? Let the algorithm choose your next binge-watch!")

col1, col2 = st.columns(2)

with col1:
    user_genres = st.multiselect("Select Genres:", dynamic_genre_list)
    user_min_rating = st.slider("Minimum IMDb Rating:", 0.0, 10.0, 8.0, 0.1)

with col2:
    user_studio = st.selectbox("Preferred Studio:", dynamic_studio_list)
    user_creator = st.selectbox("Specific Creator:", dynamic_creator_list)

if st.button("🎲 Get Recommendation"):
    results = master_anime_filter(anime_database, user_genres, user_min_rating, user_studio, user_creator)
    
    st.divider() 
    
    if len(results) == 0:
        st.error("No anime matched all of those exact filters! Try broadening your search.")
    else:
        final_pick = get_random_recommendation(results)
        
        st.success("Here is your perfect recommendation!")
        st.subheader(f"📺 {final_pick['title']}")
        st.write(f"**⭐ IMDb Rating:** {final_pick['imdb_rating']}")
        st.write(f"**🏢 Studio:** {final_pick['studio']}")
        st.write(f"**👤 Creator:** {final_pick['creator']}")
    
        st.write("---")
        st.write(f"**📖 Synopsis:** {final_pick['description']}")
        st.balloons()
