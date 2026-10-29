'''
Brand Name Generator:->
Features to implement
1) Generate multiple brand name ideas
2) Combine Words baed on the business type
3) Remove duplicate names
4) Let users generate new suggestions
5) Save their favaorite names to a text file.

'''

ai_tech_brands = [
    "OpenAI", "Google DeepMind", "Anthropic", "Microsoft", "NVIDIA", 
    "Meta", "Amazon AWS", "Databricks", "Snowflake", "Palantir", 
    "Mistral AI", "xAI", "Cohere", "Hugging Face", "Stability AI", 
    "Perplexity AI", "Midjourney", "Runway", "ElevenLabs", "Scale AI", 
    "Jasper", "Canva", "Grammarly", "Cursor", "GitHub Copilot", 
    "IBM watsonx", "Salesforce", "ServiceNow", "Oracle", "SAP", 
    "C3.ai", "DataRobot", "Dataiku", "Abacus.AI", "Inflection AI", 
    "Character.ai", "Glean", "Heimdall AI", "Hebbia", "Definitive Intelligence", 
    "Aleph Alpha", "Baidu", "SenseTime", "Alibaba Cloud", "Tencent AI", 
    "ByteDance", "DeepSeek", "01.AI", "Moonshot AI", "Baichuan AI", 
    "MiniMax", "Cognition AI", "Figure AI", "Boston Dynamics", "1X Technologies", 
    "Covariant", "Shield AI", "Anduril Industries", "Waymo", "Zoox", 
    "Cruise", "Nuro", "Tesla", "Intel", "AMD", 
    "Qualcomm", "Broadcom", "Graphcore", "Cerebras Systems", "SambaNova Systems", 
    "Groq", "CoreWeave", "Vultr", "Lambda Labs", "Pinecone", 
    "Weaviate", "Milvus", "Qdrant", "LangChain", "LlamaIndex", 
    "UiPath", "Automation Anywhere", "Fractal Analytics", "Tata Elxsi", "Uniphore", 
    "Yellow.ai", "PolyAI", "Haptik", "Tractable", "Suno", 
    "Leonardo.Ai", "HeyGen", "Pika Labs", "ElevenLabs", "Synthesia", 
    "Descript", "Otter.ai", "SoundHound", "Cerence", "CrowdStrike"
]

food_brands = [
    # Cereal & Breakfast
    "Kellogg's", "General Mills", "Quaker Oats", "Post Consumer Brands", "Weetabix",
    
    # Snacks & Confectionery
    "Lay's", "Doritos", "Pringles", "Cheetos", "Tostitos", 
    "Ruffles", "Ritz", "Oreo", "Chips Ahoy!", "Triscuit",
    "Cheez-It", "Goldfish", "Hershey's", "Reese's", "Kit Kat", 
    "Cadbury", "Milka", "Toblerone", "Snickers", "Twix", 
    "M&M's", "Skittles", "Starburst", "Haribo", "Ferrero Rocher", 
    "Nutella", "Kinder", "Ghirardelli", "Lindt", "Godiva",
    
    # Dairy & Plant-Based Alternatives
    "Danone", "Yoplait", "Chobani", "Fage", "Kraft", 
    "Philadelphia", "Tillamook", "Land O'Lakes", "Anchor", "Alpro", 
    "Oatly", "Silk", "Blue Diamond", "Fairlife", "Lactalis",
    
    # Beverages & Coffee
    "Coca-Cola", "Pepsi", "Sprite", "Fanta", "Dr Pepper", 
    "Gatorade", "Powerade", "Red Bull", "Monster Energy", "Tropicana", 
    "Minute Maid", "Ocean Spray", "Nesquik", "Starbucks", "Nespresso", 
    "Folgers", "Dunkin'", "Lipton", "Twinings", "Tetley",
    
    # Frozen & Convenience Foods
    "Nestlé", "Stouffer's", "Lean Cuisine", "DiGiorno", "Red Baron", 
    "Birdseye", "Green Giant", "McCain Foods", "Tyson Foods", "Perdue", 
    "Hot Pockets", "Eggo", "Amy's Kitchen", "Dr. Oetker", "Iglo",
    
    # Condiments, Sauces & Pantry Staples
    "Heinz", "Hellmann's", "French's", "McCormick", "Tabasco", 
    "Sriracha (Huy Fong)", "Kikkoman", "Barilla", "De Cecco", "Ragu", 
    "Prego", "Campbell's", "Progresso", "Del Monte", "Dole", 
    "Jif", "Skippy", "Smucker's", "Peter Pan", "Nutrexpa",
    
   
    # International & Major Conglomerate Brands
    "Maggi", "Knorr", "Amul", "Britannia", "Indomie", 
    "Nissin", "Maruchan", "Lee Kum Kee", "Ajinomoto", "Meiji",
    "Bimbo", "Barcel", "Goya Foods", "Old El Paso", "Ortega"
]

fitness_brands = [
    # Sportswear & Apparel Giants
    "Nike", "Adidas", "Under Armour", "Puma", "Reebok", 
    "Asics", "New Balance", "Mizuno", "Brooks Running", "Saucony", 
    "Hoka", "On Running", "Salomon", "Skechers", "Fila",
    
    # Athleisure & Activewear
    "Lululemon", "Gymshark", "Alo Yoga", "Fabletics", "Sweaty Betty", 
    "Athleta", "Vuori", "Rhone", "Nobull", "Alphalete", 
    "Vanquish Fitness", "YoungLA", "Oner Active", "Aybl", "NVGTN", 
    "Beyond Yoga", "Outdoor Voices", "Lorna Jane", "2XU", "Compressport",
    
    # Fitness Wearables & Tech
    "Garmin", "Apple Watch", "Fitbit", "Whoop", "Oura", 
    "Polar", "Suunto", "Coros", "Wahoo Fitness", "Withings",
    
    # Gym Equipment & Strength Training
    "Rogue Fitness", "Eleiko", "Hammer Strength", "Life Fitness", "Technogym", 
    "Matrix Fitness", "Precor", "Cybergym", "Titan Fitness", "Rep Fitness", 
    "Bells of Steel", "Kabuki Strength", "Fringe Sport", "Primal Strength", "Gym80",
    
    # Home Fitness & Cardio Equipment
    "Peloton", "Concept2", "NordicTrack", "Bowflex", "Schwinn", 
    "Sole Fitness", "Echelon", "Tonal", "Hydrow", "Assault Fitness", 
    "WaterRower", "Horizon Fitness", "ProForm", "Matrix Home", "Woodway",
    
    # Accessories, Recovery & Functional Gear
    "TRX", "CrossFit", "Hyperice", "Theragun (Therabody)", "Compex", 
    "CamelBak", "Hydro Flask", "BlenderBottle", "Nalgene", "Gatorade (Gear)",
    "Harbinger", "Schiek", "SBD Apparel", "A7", "Inzer", 
    "Bear KompleX", "Element 26", "Frog Grips", "RPM Training", "Rx Smart Gear",
    
    # Supplements & Nutrition Brands
    "Optimum Nutrition", "Myprotein", "MusclePharm", "Cellucor", "Ghost Lifestyle", 
    "BSN", "Dymatize", "Jym Supplement Science", "Transparent Labs", "Legion Athletics", 
    "Redcon1", "Animal", "Universal Nutrition", "EHP Labs", "Scivation", 
    "Vega", "Garden of Life", "Orgain", "Barebells", "Grenade"
]


import random
import json

def write_in_file(brand,category):
    try:
        with open("brand_category.json","r") as f:
            history = json.load(f)
    
    except (FileNotFoundError,json.JSONDecodeError):
        history = []
        
    for i in brand:
        record = {
            "brand":i,
            "category":category
        }
        
        if record not in history:
            history.append(record)
    
    with open("brand_category.json","w") as f:
        json.dump(history,f,indent=4)

list_food = ["food","cereal","breakfast","snacks","confectionery","dairy","plant-based alternatives","beverages","coffee","frozen","convenience foods","condiments","sauces","pantry Staples","international","major conglomerate brands"]
list_fitness = ["sportswear","apparel Giants","athleisure","activewear","fitness","wearables","gym equipment","strength training","home Fitness","cardio equipment","accessories","recovery","functional gear","supplements","nutrition brands"]

while True:
    print("=======:BRAND NAME GENERATOR:=======\n1.AI or Tech\n2.Food or Beverages\n3.Fitness\n4.Exit")
    
    user_category = input("Enter your business category : ").lower().strip()
    
    if  user_category in ["1","ai","tech","ml"]:
        result_ai = random.sample(ai_tech_brands,10)
        write_in_file(result_ai,user_category)
        print("Result AI name :\n")
        for i in result_ai:
            print(i)

        

    elif user_category in list_food or user_category == "2":
        result_food = random.sample(food_brands,10)
        write_in_file(result_food,user_category)
        print("Result Food Name : \n")
        for i in result_food:
            print(i)

            
    elif user_category in  list_fitness or user_category == "3":
        result_fitness = random.sample(fitness_brands,10)
        write_in_file(result_fitness,user_category)
        print("Result Fitness name : \n")
        for i in result_fitness:
            print(i)
       
    
    elif user_category in ["4","exit"]:
        print("Good Bye!")
        break
    
    else:
        print("Invalid Choice")
