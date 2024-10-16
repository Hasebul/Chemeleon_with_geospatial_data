# prompt for generating input for google maps
prompt_1 = """
Read the following question and metadata, then extract information about query, location, region and type and current_location and give as 
dictionary format.

Question: I am walking to Brassica in Bexley from South Wind Motel, Via Parsons Ave and E Main St. After reaching E Main St, where should I go next?

Options: (A) Turn left onto S Ohio Ave (B) Turn left onto College Ave (c) Turn left onto S 18th St (d) Turn right onto E Whittier St

Metadata: {"skill":"Fetch Information from map and mention the POI"}

{"origin":"South Wind Motel", "destination":"Brassica in Bexley", "mode":"walking", "waypoints":"Parsons Ave and E Main St.", "alternative":"False"}


Question: What's the fastest driving route from D03 Flame Tree Ridge to Aster Cedars Hospital, Jebel Ali?

Options: (A) Via Hessa St/D61 (B) Via Garn Al Sabkha St/D59 (C) Via D57 (D) Via Al Asayel St/D72

Metadata: {"skill":"Fetch Information from map and mention the POI"}

{"origin":"D03 Flame Tree Ridge", "destination":"Aster Cedars Hospital, Jebel Ali", "mode":"driving", "waypoints"= "None", "alternative"="True"}


Question: I am driving from The Ritz Carlton to the Bellagio Hotel in Las Vegas. What is the quickest route to take?

Options: (A) Turn left onto S Las Vegas Blvd (B) Turn right onto E Flamingo Rd (C) Turn right onto Paradise Rd (D) Turn left onto Sands Ave

Metadata: {"skill":"Fetch Information from map and mention the POI"}

{"origin":"The Ritz Carlton", "destination":"Bellagio Hotel in Las Vegas", "mode":"driving", "waypoints":"None", "alternative":"True"}


Question: What is the best walking route from Times Square to the Empire State Building?

Options: (A) Turn right onto 7th Ave (B) Turn left onto Broadway (C) Turn right onto 34th St (D) Turn left onto 5th Ave

Metadata: {"skill":"Fetch Information from map and mention the POI"}

{"origin":"Times Square", "destination":"Empire State Building", "mode":"walking", "waypoints":"None", "alternative":"True"}


Read the following question and metadata, then extract information about origin, destination, mode, waypoints and alternative and give as 
dictionary format. Put only the five fields: origin, destination, mode, waypoints and alternative.
"""

# prompt for question and using the information find the
prompt_2 = """
Read the following question and metadata, and generate the query for browser search as the context information that could be helpful for answering the question.

Question: Which property do these two objects have in common?

Options: (A) hard (B) bendable

Metadata: {'pid': 329, 'has_image': True, 'grade': 2, 'subject': 'natural science', 'topic': 'physics', 'category': 'Materials', 'skill': 'Compare properties of objects'}

Detected text in the image: [([[41, 183], [131, 183], [131, 199], [41, 199]], 'rubber gloves'), ([[245, 183], [313, 183], [313, 197], [245, 197]], 'rain boots')]

Search Query: Common material properties of jump tope and rubber gloves





Question: Which better describes the Shenandoah National Park ecosystem? 

Context: Figure: Shenandoah National Park.\nShenandoah National Park is a temperate deciduous forest ecosystem in northern Virginia.

Options: (A) It has warm, wet summers. It also has only a few types of trees. (B) It has cold, wet winters. It also has soil that is poor in nutrients.

Metadata: {'pid': 246, 'has_image': True, 'grade': 3, 'subject': 'natural science', 'topic': 'biology', 'category': 'Ecosystems', 'skill': 'Describe ecosystems'}

Search Query: Temperature and climate of Shenandoah National Park ecosystem





Question: Does this passage describe the weather or the climate? 

Context: Figure: Marseille.\nMarseille is a town on the southern coast of France. Cold winds from the north, called mistral winds, are common in Marseille each year during late winter and early spring.\nHint: Weather is what the atmosphere is like at a certain place and time. Climate is the pattern of weather in a certain place. 

Options: (A) weather (B) climate

Metadata: {'pid': 321, 'has_image': True, 'grade': 5, 'subject': 'natural science', 'topic': 'earth-science', 'category': 'Weather and climate', 'skill': 'Weather and climate around the world'}

Query: Weather or climate of Marseille, France



Question: Is the following statement about our solar system true or false?\nJupiter's volume is more than ten times as large as Saturn's volume. 

Context: Use the data to answer the question below. 

Options: (A) true (B) false

Metadata: {'pid': 649, 'has_image': True, 'grade': 8, 'subject': 'natural science', 'topic': 'earth-science', 'category': 'Astronomy', 'skill': 'Analyze data to compare properties of planets'}

Query: Volume comparison between Jupiter and Saturn



Read the following question and metadata, and generate the query for browser search as the context information that could be helpful for answering the question.
"""

# prompt for generating input for google maps
prompt_3 = """
Read the following question and metadata, and generate the query for browser search as the context information that could be helpful for answering the question.

Question: Which property do these two objects have in common?

Options: (A) hard (B) bendable

Metadata: {'pid': 329, 'has_image': True, 'grade': 2, 'subject': 'natural science', 'topic': 'physics', 'category': 'Materials', 'skill': 'Compare properties of objects'}

Detected text in the image: [([[41, 183], [131, 183], [131, 199], [41, 199]], 'rubber gloves'), ([[245, 183], [313, 183], [313, 197], [245, 197]], 'rain boots')]

Search Query: Common material properties of jump tope and rubber gloves





Question: Which better describes the Shenandoah National Park ecosystem? 

Context: Figure: Shenandoah National Park.\nShenandoah National Park is a temperate deciduous forest ecosystem in northern Virginia.

Options: (A) It has warm, wet summers. It also has only a few types of trees. (B) It has cold, wet winters. It also has soil that is poor in nutrients.

Metadata: {'pid': 246, 'has_image': True, 'grade': 3, 'subject': 'natural science', 'topic': 'biology', 'category': 'Ecosystems', 'skill': 'Describe ecosystems'}

Search Query: Temperature and climate of Shenandoah National Park ecosystem





Question: Does this passage describe the weather or the climate? 

Context: Figure: Marseille.\nMarseille is a town on the southern coast of France. Cold winds from the north, called mistral winds, are common in Marseille each year during late winter and early spring.\nHint: Weather is what the atmosphere is like at a certain place and time. Climate is the pattern of weather in a certain place. 

Options: (A) weather (B) climate

Metadata: {'pid': 321, 'has_image': True, 'grade': 5, 'subject': 'natural science', 'topic': 'earth-science', 'category': 'Weather and climate', 'skill': 'Weather and climate around the world'}

Query: Weather or climate of Marseille, France



Question: Is the following statement about our solar system true or false?\nJupiter's volume is more than ten times as large as Saturn's volume. 

Context: Use the data to answer the question below. 

Options: (A) true (B) false

Metadata: {'pid': 649, 'has_image': True, 'grade': 8, 'subject': 'natural science', 'topic': 'earth-science', 'category': 'Astronomy', 'skill': 'Analyze data to compare properties of planets'}

Query: Volume comparison between Jupiter and Saturn



Read the following question and metadata, and generate the query for browser search as the context information that could be helpful for answering the question.
"""

# prompt for generating input for google maps
prompt_4 = """
Read the following question and metadata, and generate the query for browser search as the context information that could be helpful for answering the question.

Question: Which property do these two objects have in common?

Options: (A) hard (B) bendable

Metadata: {'pid': 329, 'has_image': True, 'grade': 2, 'subject': 'natural science', 'topic': 'physics', 'category': 'Materials', 'skill': 'Compare properties of objects'}

Detected text in the image: [([[41, 183], [131, 183], [131, 199], [41, 199]], 'rubber gloves'), ([[245, 183], [313, 183], [313, 197], [245, 197]], 'rain boots')]

Search Query: Common material properties of jump tope and rubber gloves





Question: Which better describes the Shenandoah National Park ecosystem? 

Context: Figure: Shenandoah National Park.\nShenandoah National Park is a temperate deciduous forest ecosystem in northern Virginia.

Options: (A) It has warm, wet summers. It also has only a few types of trees. (B) It has cold, wet winters. It also has soil that is poor in nutrients.

Metadata: {'pid': 246, 'has_image': True, 'grade': 3, 'subject': 'natural science', 'topic': 'biology', 'category': 'Ecosystems', 'skill': 'Describe ecosystems'}

Search Query: Temperature and climate of Shenandoah National Park ecosystem





Question: Does this passage describe the weather or the climate? 

Context: Figure: Marseille.\nMarseille is a town on the southern coast of France. Cold winds from the north, called mistral winds, are common in Marseille each year during late winter and early spring.\nHint: Weather is what the atmosphere is like at a certain place and time. Climate is the pattern of weather in a certain place. 

Options: (A) weather (B) climate

Metadata: {'pid': 321, 'has_image': True, 'grade': 5, 'subject': 'natural science', 'topic': 'earth-science', 'category': 'Weather and climate', 'skill': 'Weather and climate around the world'}

Query: Weather or climate of Marseille, France



Question: Is the following statement about our solar system true or false?\nJupiter's volume is more than ten times as large as Saturn's volume. 

Context: Use the data to answer the question below. 

Options: (A) true (B) false

Metadata: {'pid': 649, 'has_image': True, 'grade': 8, 'subject': 'natural science', 'topic': 'earth-science', 'category': 'Astronomy', 'skill': 'Analyze data to compare properties of planets'}

Query: Volume comparison between Jupiter and Saturn



Read the following question and metadata, and generate the query for browser search as the context information that could be helpful for answering the question.
"""

# prompt for generating input for google maps
prompt_5 = """
Read the following question and metadata, and generate the query for browser search as the context information that could be helpful for answering the question.

Question: Which property do these two objects have in common?

Options: (A) hard (B) bendable

Metadata: {'pid': 329, 'has_image': True, 'grade': 2, 'subject': 'natural science', 'topic': 'physics', 'category': 'Materials', 'skill': 'Compare properties of objects'}

Detected text in the image: [([[41, 183], [131, 183], [131, 199], [41, 199]], 'rubber gloves'), ([[245, 183], [313, 183], [313, 197], [245, 197]], 'rain boots')]

Search Query: Common material properties of jump tope and rubber gloves





Question: Which better describes the Shenandoah National Park ecosystem? 

Context: Figure: Shenandoah National Park.\nShenandoah National Park is a temperate deciduous forest ecosystem in northern Virginia.

Options: (A) It has warm, wet summers. It also has only a few types of trees. (B) It has cold, wet winters. It also has soil that is poor in nutrients.

Metadata: {'pid': 246, 'has_image': True, 'grade': 3, 'subject': 'natural science', 'topic': 'biology', 'category': 'Ecosystems', 'skill': 'Describe ecosystems'}

Search Query: Temperature and climate of Shenandoah National Park ecosystem





Question: Does this passage describe the weather or the climate? 

Context: Figure: Marseille.\nMarseille is a town on the southern coast of France. Cold winds from the north, called mistral winds, are common in Marseille each year during late winter and early spring.\nHint: Weather is what the atmosphere is like at a certain place and time. Climate is the pattern of weather in a certain place. 

Options: (A) weather (B) climate

Metadata: {'pid': 321, 'has_image': True, 'grade': 5, 'subject': 'natural science', 'topic': 'earth-science', 'category': 'Weather and climate', 'skill': 'Weather and climate around the world'}

Query: Weather or climate of Marseille, France



Question: Is the following statement about our solar system true or false?\nJupiter's volume is more than ten times as large as Saturn's volume. 

Context: Use the data to answer the question below. 

Options: (A) true (B) false

Metadata: {'pid': 649, 'has_image': True, 'grade': 8, 'subject': 'natural science', 'topic': 'earth-science', 'category': 'Astronomy', 'skill': 'Analyze data to compare properties of planets'}

Query: Volume comparison between Jupiter and Saturn



Read the following question and metadata, and generate the query for browser search as the context information that could be helpful for answering the question.
"""