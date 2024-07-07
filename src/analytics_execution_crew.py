from db_execution_task import DbexecutionTask
from data_visualization_task import DataVisualization
from db_execution_agent import DbexecutionAgent
from data_visualization_agent import DataVisualizationAgent

from crewai import Agent, Task, Crew, Process

class AnalyticsCrew():
    def __init__(self,schema, query) -> None:
        self.schema = schema
        self.query = query
        
    def run(self):
        dbagent =DbexecutionAgent.genericdbexecutionAgent()
        chartagent = DataVisualizationAgent.unifiedstreamlitchartingAgent_o()

        datatask = DbexecutionTask.genericdbtask(self.schema, self.query, dbagent)
        charttask = DataVisualization.convertinputtocompatiblecharting_o(chartagent)
        crew = Crew(
                agents=[dbagent,chartagent],
                tasks=[datatask,charttask],
                verbose=2
             )

        res = crew.kickoff()
        return res