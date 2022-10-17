from patterns.csv_utils import Ride
from patterns import web_report
from patterns import print_report

class Report():
    def __init__(self):
        pass

class HTMLReport:

    def create_report(self, rides):
        html_report = web_report.create_content(rides)
        web_report.create_file(html_report)

class PrintReport:

    def create_report(self, rides):
        service = print_report.PrintReport()

        createContent = print_report.CreateContentCommand(rides, service)
        myContent = createContent.execute()
        createFile = print_report.CreateFileCommand(myContent, service)
        createFile.execute()

class CreateReport:

    def __init__(self, strategy, rides):
        self.strategy = strategy
        self.rides = rides

    def create_report(self):
        return self.strategy.create_report(self.rides)