
prompt = """
You need to act as a policy model, that given a question and a modular set, determines the sequence of modules that can be executed sequentially can solve the question.

The modules are defined as follows:

- Query_Generator: This module generates a search engine query for the given question. Normally, we consider using "Query_Generator" when the question involves domain-specific knowledge.

- Bing_Search: This module searches the web for relevant information to the question. Normally, we consider using "Bing_Search" when the question involves domain-specific knowledge.

- google_maps: This module find location information from google maps. Normally we consider using "google_maps" when the question involves location type questions

- Image_Captioner: This module generates a caption for the given image. Normally, we consider using "Image_Captioner" when the question involves the semantic understanding of the image, and the "has_image" field in the metadata is True.

- Text_Detector: This module detects the text in the given image. Normally, we consider using "Text_Detector" when the question involves the unfolding of the text in the image, e.g., diagram, chart, table, map, etc., and the "has_image" field in the metadata is True.

- Knowledge_Retrieval: This module retrieves background knowledge as the hint for the given question. Normally, we consider using "Knowledge_Retrieval" when the background knowledge is helpful to guide the solution.

- Solution_Generator: This module generates a detailed solution to the question based on the information provided. Normally, "Solution_Generator" will incorporate the information from "Query_Generator", "Bing_Search", "Image_Captioner", "Text_Detector", and "Knowledge_Retrieval".

- Answer_Generator: This module extracts final answer in a short form from the solution or execution result. This module normally is the last module in the prediction pipeline.

Below are some examples that map the problem to the modules.

Question: Compare the average kinetic energies of the particles in each sample. Which sample has the higher temperature?

Context: The diagrams below show two pure samples of gas in identical closed, rigid containers. Each colored ball represents one gas particle. Both samples have the same number of particles. 

Options: (A) neither; the samples have the same temperature (B) sample A (C) sample B

Metadata: {'pid': 19, 'has_image': True, 'grade': 8, 'subject': 'natural science', 'topic': 'physics', 'category': 'Particle motion and energy', 'skill': 'Identify how particle motion affects temperature and pressure'}

Modules: ["Text_Detector", "Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]

Question: Which property do these three objects have in common? 

Options: (A) hard (B) soft (C) yellow

Metadata: {'pid': 43, 'has_image': True, 'grade': 4, 'subject': 'natural science', 'topic': 'physics', 'category': 'Materials', 'skill': 'Compare properties of objects'} 

Modules: ["Text_Detector", "Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]

Question: Which better describes the Shenandoah National Park ecosystem?

Context: Figure: Shenandoah National Park.\nShenandoah National Park is a temperate deciduous forest ecosystem in northern Virginia.

Options: (A) It has warm, wet summers. It also has only a few types of trees. (B) It has cold, wet winters. It also has soil that is poor in nutrients.

Metadata: {'pid': 246, 'has_image': True, 'grade': 3, 'subject': 'natural science', 'topic': 'biology', 'category': 'Ecosystems', 'skill': 'Describe ecosystems'}

Modules: ["Query_Generator", "Bing_Search", "Solution_Generator", "Answer_Generator"]

Question: Think about the magnetic force between the magnets in each pair. Which of the following statements is true?

Context: The images below show two pairs of magnets. The magnets in different pairs do not affect each other. All the magnets shown are made of the same material, but some of them are different shapes.  

Metadata: {'has_image': True, 'grade': 6, 'subject': 'natural science', 'topic': 'physics', 'category': 'Velocity, acceleration, and forces', 'skill': 'Compare magnitudes of magnetic forces'} 

Options: (A) The magnitude of the magnetic force is greater in Pair 1. (B) The magnitude of the magnetic force is greater in Pair 2. (C) The magnitude of the magnetic force is the same in both pairs.

Modules: ["Text_Detector", "Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]

Question: Which is in row C?

Options: (A) the diner (B) the grocery store (C) the library (D) the school

Metadata: {'pid': 375, 'has_image': True, 'grade': 3, 'subject': 'social science', 'topic': 'geography', 'category': 'Geography', 'skill': 'Use a letter-number grid'} 

Modules: ["Text_Detector", ≈"Solution_Generator", "Answer_Generator"]

Question: Which material is this screw driver made of?

Options: (A) cardboard (B) plastic

Metadata: {'pid': 264, 'has_image': True, 'grade': 2, 'subject': 'natural science', 'topic': 'physics', 'category': 'Materials', 'skill': 'Identify multiple materials in objects'} 

Modules: ["Image_Captioner", "Solution_Generator", "Answer_Generator"]

Question: How long is a garden snail?

Context: Select the best estimate.

Options: (A) 27 meters (B) 27 millimeters (C) 27 kilometers (D) 27 centimeters

Metadata: {'pid': '1351', 'has_image': False, 'grade': 6, 'subject': 'natural science', 'topic': 'units-and-measurement', 'category': 'Units and measurement', 'skill': 'Choose metric units of distance, mass, and volume'}

Modules: ["Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]


Question: Look at the models of molecules below. Select the elementary substance.

Options: (A) fluoromethanol (B) ozone (C) carbon tetrachloride

Metadata: {'pid': '411', 'has_image': True, 'grade': 6, 'subject': 'natural science', 'topic': 'chemistry', 'category': 'Atoms and molecules', 'skill': 'Identify elementary substances and compounds using models'}

Modules: ["Text_Detector", "Knowledge_Retrieval", "Bing_Search", "Solution_Generator", "Answer_Generator"]

Question: Which figure of speech is used in this text?\nHunter remarked that the new book on anti-gravity was impossible to put down.

Options: (A) alliteration (B) pun

Metadata: {'pid': '41', 'has_image': False, 'grade': 9, 'subject': 'language science', 'topic': 'figurative-language', 'category': 'Literary devices', 'skill': 'Classify figures of speech: review'}

Modules: ["Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]

Question: Which rhetorical appeal is primarily used in this ad?

Options: (A) ethos (character) (B) pathos (emotion) (C) logos (reason)

Metadata: {'pid': '1062', 'has_image': True, 'grade': 12, 'subject': 'language science', 'topic': 'writing-strategies', 'category': 'Persuasive strategies', 'skill': 'Identify appeals to ethos, pathos, and logos in advertisements'}

Modules: ["Text_Detector", "Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]

Question: Find the nearest hospital from Green Delta AIMS Tower, Mohakhali?

Options: (A) MOHAKHALI CANCER AND GENERAL HOSPITAL (B) Square Hospitals Limited (c) United Hospital Limited (d) Millennium Specialized Hospital

Metadata: {"skill":"Fetch Information from map and mention the POI"}

Modules: ["google_maps", "Solution_Generator", "Answer_Generator"]

Question: Find the nearest police station from Bashundhara Residential Area, Dhaka?

Options: (A) Bashundhara Police Station (B) Gulshan Police Station (C) Banani Police Station (D) Uttara Police Station

Metadata: {"skill":"Fetch Information from map and mention the POI"}

Modules: [ "google_maps", "Solution_Generator", "Answer_Generator"]

Question: Find the nearest supermarket from Baridhara Diplomatic Zone, Dhaka?

Options: (A) Meena Bazar (B) Agora Super Shop (C) Shwapno (D) Unimart

Metadata: {"skill":"Fetch Information from map and mention the POI"}

Modules: [ "google_maps", "Solution_Generator", "Answer_Generator"]

Question: Find the nearest gas station from Uttara, Dhaka?

Options: (A) Padma Oil Company Limited (B) Eastern Refinery Limited (C) Meghna Petroleum Limited (D) Petromax CNG Ltd.

Metadata: {"skill":"Fetch Information from map and mention the POI"}

Modules: ["google_maps", "Solution_Generator", "Answer_Generator"]

Question: I am walking to Brassica in Bexley from South Wind Motel, Via Parsons Ave and E Main St. After reaching E Main St, where should I go next?

Options: (A) Turn left onto S Ohio Ave (B) Turn left onto College Ave (c) Turn left onto S 18th St (d) Turn right onto E Whittier St

Metadata: {"skill":"Fetch Information from map and mention the POI"}

Modules: ["google_maps", "Solution_Generator", "Answer_Generator"]

Question: What's the fastest driving route from D03 Flame Tree Ridge to Aster Cedars Hospital, Jebel Ali?

Options: (A) Via Hessa St/D61 (B) Via Garn Al Sabkha St/D59 (C) Via D57 (D) Via Al Asayel St/D72

Metadata: {"skill":"Fetch Information from map and mention the POI"}

Modules: ["google_maps", "Solution_Generator", "Answer_Generator"]

Question: I am driving from The Ritz Carlton to the Bellagio Hotel in Las Vegas. What is the quickest route to take?

Options: (A) Turn left onto S Las Vegas Blvd (B) Turn right onto E Flamingo Rd (C) Turn right onto Paradise Rd (D) Turn left onto Sands Ave

Metadata: {"skill":"Fetch Information from map and mention the POI"}

Modules: ["google_maps", "Solution_Generator", "Answer_Generator"]

Question: What is the best walking route from Times Square to the Empire State Building?

Options: (A) Turn right onto 7th Ave (B) Turn left onto Broadway (C) Turn right onto 34th St (D) Turn left onto 5th Ave

Metadata: {"skill":"Fetch Information from map and mention the POI"}

Modules: ["google_maps", "Solution_Generator", "Answer_Generator"]
"""