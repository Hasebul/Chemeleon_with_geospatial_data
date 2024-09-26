# # Create tools
# import os
# import googlemaps
# from dotenv import load_dotenv
# from langchain_openai import AzureChatOpenAI
# from typing import Annotated
# from langchain.tools import tool
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_openai import ChatOpenAI
# from pydantic import BaseModel
# from typing import Literal
# import functools
# import operator
# from typing import Sequence, TypedDict
#
# from langchain_core.messages import BaseMessage, HumanMessage
# from langgraph.graph import END, StateGraph, START
# from langgraph.prebuilt import create_react_agent
#
# load_dotenv()
#
# from langchain_community.tools.tavily_search import TavilySearchResults
# from langchain_experimental.tools import PythonREPLTool
#
# tavily_tool = TavilySearchResults(max_results=5)
# python_repl_tool = PythonREPLTool()
# gmaps = googlemaps.Client(key='AIzaSyBnsinvIK8T2C8Kv5Q3gKyVWaTMgINDhVw')
#
#
# @tool
# def nearest_poi_tool(query: str, location: dict, type: str) -> str:
#     """Extract information from google maps"""
#     places_results = gmaps.places(
#         query=query,
#         location=location,
#         type=type
#     )
#     all_poi = places_results["results"]
#     extract_information = f"The following location are the nearest location and all the location has a destination form the current location {location}:\n"
#
#     def distance(loc1, loc2):
#         from math import sin, cos, sqrt, atan2, radians
#         # approximate radius of earth in km
#         R = 6373.0
#         lat1 = radians(loc1['lat'])
#         lon1 = radians(loc1['lng'])
#         lat2 = radians(loc2['lat'])
#         lon2 = radians(loc2['lng'])
#
#         dlon = lon2 - lon1
#         dlat = lat2 - lat1
#         a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
#         c = 2 * atan2(sqrt(a), sqrt(1 - a))
#         distance = R * c
#         return distance
#
#     for poi in all_poi:
#         dist = distance(loc1=poi['geometry']['location'], loc2=location)
#         rating = poi['rating'] if 'rating' in poi.keys() else 0
#         total_user = poi['user_ratings_total'] if 'user_ratings_total' in poi.keys() else 0
#         extract_information = extract_information + f"{poi['name']} has {rating} rating," + f"where {total_user} people give their rating, " + f"the location distance from current location is {dist} kilometers\n"
#     return extract_information
#
#
# @tool
# def routing_tool(origin, destination, mode=None, waypoints=None, alternatives=True) -> str:
#     """add two numbers."""
#
#     def directions(origin, destination, mode=None, waypoints=None, alternatives=True):
#         # origin = "D03 Flame Tree Ridge", destination = "Aster Cedars Hospital, Jebel Ali", mode = "driving", waypoints = None, alternatives = True
#         all_routes = gmaps.directions(
#             origin=origin, destination=destination, mode=mode, waypoints=waypoints, alternatives=alternatives
#         )
#
#         extract_information = {}
#         extract_information["number of route"] = len(all_routes)
#         counter = 0
#         for route in all_routes:
#             counter = counter + 1
#             extract_information[f"route_number_{counter}"] = route
#         print(extract_information)
#         return extract_information
#
#     return directions(origin, destination, mode, waypoints, alternatives)
#
#
#
# @tool
# def trip_tool(a: int, b: int) -> int:
#     """add two numbers."""
#     return a + b
#
# # Helper Utilities
#
#
# def agent_node(state, agent, name):
#     result = agent.invoke(state)
#     return {"messages": [HumanMessage(content=result["messages"][-1].content, name=name)]}
#
#
# # Create Agent Supervisor
#
#
# members = ["nearest_poi", "routing", "trip"]
# system_prompt = (
#     "You are a supervisor tasked with managing a conversation between the"
#     f" following workers:  {members}. Given the following user request,"
#     " respond with the worker to act next. Each worker will perform a"
#     " task and respond with their results and status. When finished,"
#     " respond with FINISH."
# )
# # Our team supervisor is an LLM node. It just picks the next agent to process
# # and decides when the work is completed
# options = ["FINISH"] + members
#
#
# class routeResponse(BaseModel):
#     next: Literal[*options]
#
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         MessagesPlaceholder(variable_name="messages"),
#         (
#             "system",
#             "Given the conversation above, who should act next?"
#             " Or should we FINISH? Select one of: {options}",
#         ),
#     ]
# ).partial(options=str(options), members=", ".join(members))
#
# # llm = ChatOpenAI(model="gpt-4o")
# script_dir = os.path.dirname(__file__)
# root_dir = os.path.dirname(script_dir)
#
# token = open(os.path.join(root_dir, "token"), "r").read()
#
# # print(token.token)
# os.environ["AZURE_OPENAI_API_KEY"] = token
#
#
# llm = AzureChatOpenAI(
#     azure_deployment="gpt3",
#     temperature=0.6,
# )
#
#
# def supervisor_agent(state):
#     supervisor_chain = (
#             prompt
#             | llm.with_structured_output(routeResponse)
#     )
#     return supervisor_chain.invoke(state)
#
#
# # Construct Graph
#
#
# # The agent state is the input to each node in the graph
# class AgentState(TypedDict):
#     # The annotation tells the graph that new messages will always
#     # be added to the current states
#     messages: Annotated[Sequence[BaseMessage], operator.add]
#     # The 'next' field indicates where to route to next
#     next: str
#
#
# nearest_poi_agent = create_react_agent(llm, tools=[nearest_poi_tool])
# nearest_poi_node = functools.partial(agent_node, agent=nearest_poi_agent, name="Researcher")
#
# # NOTE: THIS PERFORMS ARBITRARY CODE EXECUTION. PROCEED WITH CAUTION
# routing_agent = create_react_agent(llm, tools=[routing_tool])
# routing_node = functools.partial(agent_node, agent=routing_agent, name="Coder")
#
# workflow = StateGraph(AgentState)
# workflow.add_node("Researcher", nearest_poi_node)
# workflow.add_node("Coder", routing_node)
# workflow.add_node("supervisor", supervisor_agent)
#
# for member in members:
#     # We want our workers to ALWAYS "report back" to the supervisor when done
#     workflow.add_edge(member, "supervisor")
# # The supervisor populates the "next" field in the graph state
# # which routes to a node or finishes
# conditional_map = {k: k for k in members}
# conditional_map["FINISH"] = END
# workflow.add_conditional_edges("supervisor", lambda x: x["next"], conditional_map)
# # Finally, add entrypoint
# workflow.add_edge(START, "supervisor")
#
# graph = workflow.compile()
#
# # Invoke the team
# # for s in graph.stream(
# #     {
# #         "messages": [
# #             HumanMessage(content="Code hello world and print it to the terminal")
# #         ]
# #     }
# # ):
# #     if "__end__" not in s:
# #         print(s)
# #         print("----")
#
#
# if __name__ == "__main__":
#     # for s in graph.stream(
#     #         {"messages": [HumanMessage(content="Write a brief research report on pikas.")]},
#     #         {"recursion_limit": 100},
#     # ):
#     #     if "__end__" not in s:
#     #         print(s)
#     #         print("----")
#
#     for s in graph.stream(
#         {
#             "messages": [
#                 HumanMessage(content="Code hello world and print it to the terminal")
#             ]
#         }
#     ):
#         if "__end__" not in s:
#             print(s)
#             print("----")
