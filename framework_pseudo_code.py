class Layer1:  # Layer 1: Chameleon
    def __init__(self, prompt_policy, llm, query):
        self.prompt_policy = prompt_policy  # The prompt_policy is responsible for planning and fetching all modules to solve the problem.
        self.llm = llm  # The llm used by layer1
        self.query = query
        self.pipeline(prompt_policy, llm, query)

    def pipeline(self, prompt_policy, llm, query) -> list:
        # call planner and select all module
        modules = self.planner(prompt_policy=prompt_policy, llm=llm,
                               query=query)  # modules contain all the module to solve the task
        input_info = "Query"
        output_info = None
        for module in modules:
            output_info = eval(module)(input_info)  # execute the module ans fetch the output of the module
            input_info = output_info
        answer = output_info
        return answer

    @staticmethod
    def planner(prompt_policy, llm, query):
        """
        based on query select all module to solve the task using prompt_policy as prompt of llm
        """
        modules = ["googlemaps", "solution_generator", "answer_generator"]  # "all the module as a list"
        return modules

    def googlemaps(self, input_info):
        layer2 = Layer2()
        layer2.take_action(query)

        return

    def solution_generator(self):
        pass

    def answer_generator(self):
        pass


# Layer 2: Agent-Based System interacting with tools
class Layer2:
    def __init__(self):
        self.tools = ['nearby_poi_tools', 'routing_tools', 'trip_tools', 'geospatial_dataset_tools']
        self.agent = "prepare an agent with tools"

    def take_action(self,query):
        """call the appropriate tools based on query and fetch information """
        pass

    def nearby_poi_tools(self):
        pass

    def routing_tools(self):
        pass

    def trip_tools(self):
        pass

    def geospatial_data_fetch_tools(self):
        pass


"""
Step 1:
  Call Layer1.planner with prompt_policy and query
  Set module_list to the output of Layer1.planner

Step 2:
  For each module in module_list:
    Call module with query and store the output in result
    Update the input with the output for the next module
    If module is google_maps:
      Call Layer2.take_action()
      This agent will use appropriate tools to solve the query and fetch information
    End If
  End For

Step 3:
  Display the final output



"""
