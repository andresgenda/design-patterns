from patterns.csv_utils import Ride
from patterns import web_report
from patterns import print_report

class Report():
    def __init__(self):
        pass

class HTMLReport:

    def create_report(self, rides, headers):
        html_report = web_report.create_content(rides, headers)
        web_report.create_file(html_report)

class PrintReport:

    def create_report(self, rides, headers):
        service = print_report.PrintReport()

        createContent = print_report.CreateContentCommand(rides, service, headers)
        myContent = createContent.execute()
        createFile = print_report.CreateFileCommand(myContent, service)
        createFile.execute()

class CreateReport:

    def __init__(self, strategy, rides, headers):
        self.strategy = strategy
        self.rides = rides
        self.headers = headers

    def create_report(self):
        return self.strategy.create_report(self.rides, self.headers)