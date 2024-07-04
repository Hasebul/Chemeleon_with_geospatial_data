

# cot
prompt_cot = """

Given the question (and the context), select the answer from the options ["A", "B", "C", "D", "E"]. You should give consice and step-by-step solutions. Finally, conclude the answer in the format of "the answer is [ANSWER]", where [ANSWER] is one from the options ["A", "B", "C", "D", "E"]. For example, "the answer is A", "the answer is B", "the answer is C", "the answer is D", or "the answer is E". If the answer is not in the options, select the most possible option.

Question: Which property do these two objects have in common?

Context: Select the better answer. Image: A pair of scissors next to a pair of scissors.

Options: (A) hard (B) bendable

Solution: An object has different properties. A property of an object can tell you how it looks, feels, tastes, or smells.\nDifferent objects can have the same properties. You can use these properties to put objects into groups. Look at each object.\nFor each object, decide if it has that property.\nA bendable object can be bent without breaking. Both objects are bendable.\nA hard object keeps its shape when you squeeze it. The rubber gloves are not hard.\nThe property that both objects have in common is bendable.\n\nTherefore, the answer is B.

Question: Select the one substance that is not a mineral.

Context: Select the better answer.

Options: (A) turtle shell is not a pure substance. It is made by a living thing (B) Celestine is a pure substance. It is a solid. (C) Hematite is not made by living things. It is a solid.

Solution: Compare the properties of each substance to the properties of minerals. Select the substance whose properties do not match those of minerals.\nA turtle shell is made by a living thing. But minerals are not made by living things.\nA turtle shell is not a pure substance. But all minerals are pure substances.\nSo, a turtle shell is not a mineral.\nCelestine is a mineral.\nHematite is a mineral.\nTherefore, the answer is A.
"""

# chameleon
prompt_chameleon = """
Given the question (and the context), select the answer from the options ["A", "B", "C", "D", "E"]. You should give consice and step-by-step solutions. Finally, conclude the answer in the format of "the answer is [ANSWER]", where [ANSWER] is one from the options ["A", "B", "C", "D", "E"]. For example, "the answer is A", "the answer is B", "the answer is C", "the answer is D", or "the answer is E". If the answer is not in the options, select the most possible option.

#Example 1
Question: Find the nearest hospital from Green Delta AIMS Tower, Mohakhali?

Options: (A) MOHAKHALI CANCER AND GENERAL HOSPITAL (B) Square Hospitals Limited (c) United Hospital Limited (d) Millennium Specialized Hospital

Metadata: {"skill":"Fetch Information from map and mention the POI"}

google maps response: The following locations are the nearest locations, and all of them have a destination form from the current location {'lat': 23.7804576, 'lng': 90.407769} :\n
Bangladesh Specialized Hospital has 3.3 rating, where 1162 people give their rating, the location distance from current location is 4.597114747999699 kilometers
Square Hospital has 4.1 rating, where 2544 people give their rating, the location distance from current location is 4.068450279284913 kilometers
Badda General Hospital Pvt. Ltd. has 3.7 rating, where 116 people give their rating, the location distance from current location is 1.8612444354946194 kilometers
United Hospital Limited has 3.9 rating, where 1779 people give their rating, the location distance from current location is 2.810382237654217 kilometers
AMZ Hospital Ltd. has 4 rating, where 252 people give their rating, the location distance from current location is 1.905227966928624 kilometers
Samorita Hospital Ltd. has 4 rating, where 503 people give their rating, the location distance from current location is 3.8567577415160033 kilometers
Bangladesh Medical College Hospital has 4.1 rating, where 948 people give their rating, the location distance from current location is 5.1090398832567345 kilometers
Impulse Hospital has 3.8 rating, where 512 people give their rating, the location distance from current location is 1.65810016123089 kilometers
Rushmono Specialized Hospital has 3.5 rating, where 130 people give their rating, the location distance from current location is 3.486003020569616 kilometers
BIRDEM General Hospital has 4.2 rating, where 1425 people give their rating, the location distance from current location is 4.762908619455911 kilometers
CARe Medical College & Hospital has 3.5 rating, where 230 people give their rating, the location distance from current location is 4.189530628079116 kilometers
Farazy Hospital has 3.9 rating, where 535 people give their rating, the location distance from current location is 3.5189082157655864 kilometers
Cure Medical Center & Hospital has 4.3 rating, where 8 people give their rating, the location distance from current location is 1.2565995048550593 kilometers
Universal Medical College Hospital Ltd. has 3.8 rating, where 397 people give their rating, the location distance from current location is 1.3204718608663173 kilometers
Institute Of Leprosy Control Hospital has 4.3 rating, where 17 people give their rating, the location distance from current location is 0.16820194272999434 kilometers
Shaheed Suhrawardy Medical College and Hospital has 4.2 rating, where 1601 people give their rating, the location distance from current location is 3.9091223069781225 kilometers
York Hospital has 4 rating, where 49 people give their rating, the location distance from current location is 1.7652153462492584 kilometers
Square Hospitals Limited | Corporate Office has 5 rating, where 1 people give their rating, the location distance from current location is 0.06693517850470752 kilometers
ZAINUL HAQUE SIKDER WOMEN'S MEDICAL COLLEGE & HOSPITAL (PVT.) LTD. has 4 rating, where 24 people give their rating, the location distance from current location is 1.7593999301308518 kilometers
Better Life Hospital has 3.4 rating, where 248 people give their rating, the location distance from current location is 2.6071595159429655 kilometers

Solution: Compared to all the hospitals near your current location at Green Delta AIMS Tower, Mohakhali,
we found Square Hospitals Limited | Corporate Office to be the closest. We can confirm that Square Hospitals Limited Corporate Office is indeed the nearest option.\n
Therefore, the answer is B.

#Example 2
Question: Find the nearest Restaurant from West End School, Lalbagh, Dhaka?

Options: (A) Cafe Jannat Hotel & Restaurant (B) PIZZA Garage (C) Water Garden Restaurant & Convention Hall (D) Bhooter Bari Restaurant

Metadata: {"skill":"Fetch Information from map and mention the POI"}

google maps response: The following locations are the nearest locations, and all of them have a destination form from the current location {'lat': 23.7216189, 'lng': 90.38535639999999} :\n
Royal Restaurant has 4 rating, where 5173 people give their rating, the location distance from current location is 0.5750237305248831 kilometers
Bhooter Bari Restaurant has 4 rating, where 2117 people give their rating, the location distance from current location is 0.3571511328124262 kilometers
Mughal Darbar Restaurant has 3.9 rating, where 97 people give their rating, the location distance from current location is 0.28708285974538417 kilometers
Cafe Jannat Hotel & Restaurant (ক্যাফে জান্নাত হোটেল এন্ড রেস্টুরেন্ট) has 4.1 rating, where 163 people give their rating, the location distance from current location is 0.27615569809162305 kilometers
Cafe Jagannath has 4.4 rating, where 97 people give their rating, the location distance from current location is 0.46119628354183817 kilometers
Pafin Chinese Restaurant Lalbagh has 4 rating, where 424 people give their rating, the location distance from current location is 0.5283389241397418 kilometers
Green Leaf Restaurant has 3.9 rating, where 88 people give their rating, the location distance from current location is 0.37361583555914313 kilometers
Dark House Restaurant has 4.1 rating, where 199 people give their rating, the location distance from current location is 0.3605159063814061 kilometers
Lalbagh Restaurant & Party Center has 4.1 rating, where 62 people give their rating, the location distance from current location is 0.2714729648541973 kilometers
PIZZA Garage Lalbagh has 4.1 rating, where 257 people give their rating, the location distance from current location is 0.31143652843856084 kilometers
Jomidari Bhoj Restaurant has 4.2 rating, where 1686 people give their rating, the location distance from current location is 0.8876292897386362 kilometers
Vhorta Bari Restaurant has 4 rating, where 452 people give their rating, the location distance from current location is 1.0954230058865428 kilometers
Al Razzak Restaurant has 3.9 rating, where 9169 people give their rating, the location distance from current location is 2.3961387921469464 kilometers
Water Garden Restaurant & Convention Hall has 3.9 rating, where 140 people give their rating, the location distance from current location is 0.2446427209784578 kilometers
Pinewood Cafe n' Restaurant has 4.3 rating, where 4042 people give their rating, the location distance from current location is 3.556721745255204 kilometers
B cafe or Take a bite restaurent & party center has 3.5 rating, where 134 people give their rating, the location distance from current location is 0.437305811091622 kilometers
Vorta Vaji Restaurant has 4.2 rating, where 646 people give their rating, the location distance from current location is 1.9694382680213218 kilometers
Shader Bahar Hotel & Restaurant has 3.9 rating, where 47 people give their rating, the location distance from current location is 0.3364312934136029 kilometers
Xinxian Restaurant has 4.1 rating, where 4346 people give their rating, the location distance from current location is 2.6704769208018524 kilometers
Khaje Dewan Restaurant has 3.8 rating, where 37 people give their rating, the location distance from current location is 0.6752691881527221 kilometers

Solution: Compared to all the hospitals near your current location at Green Delta AIMS Tower, Mohakhali,
we found Water Garden Restaurant & Convention Hall to be the closest. We can confirm that Water Garden Restaurant & Convention Hall is indeed the nearest option.\n
Therefore, the answer is C.

Now Answer the question following.
#Question

"""
