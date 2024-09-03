

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
Question: I am walking to Brassica in Bexley from South Wind Motel, Via Parsons Ave and E Main St. After reaching E Main St, where should I go next?
Options: (A) Turn left onto S Ohio Ave (B) Turn left onto College Ave (c) Turn left onto S 18th St (d) Turn right onto E Whittier St
Metadata: {"skill":"Fetch Information from map and mention the POI"}

google maps response: The JSON data contains one route starting from 919 S High St, Columbus, OH 43206, USA, 
and ending at 2212 E Main St, Bexley, OH 43209, USA. The total route covers 4.0 miles and takes approximately 92 minutes. 
The first leg begins at 919 S High St and ends at E Main St & Parsons Ave, Columbus, OH, covering 1.8 miles in 42 minutes. 
The steps include heading west on S Wall St, turning right onto S Wall St, right onto Shumacher Alley, 
left onto S High St, right onto E Whittier St, and finally left onto Parsons Ave. The second leg continues from 
E Main St & Parsons Ave to 2212 E Main St, covering 2.2 miles in 50 minutes, heading east on E Main St, 
left onto College Ave, and a slight right to the destination. The fastest route is the only provided route, 
covering the entire distance in the specified duration.

Solution: After comparing all the routes and steps, we found that the next step after reaching E Main St is to 
turn left onto College Ave, which is option (B) in the list. Therefore, the answer is B.


Now Answer the question following.
#Question

"""
