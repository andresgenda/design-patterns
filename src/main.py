from patterns import csv_utils
from patterns import web_report
from patterns import report

CSV_FILE = "taxi-data.csv"


def main():

    #Stategy design pattern
    htmlReport = report.HTMLReport()
    printReport = report.PrintReport()

    rides = csv_utils.parse_file(CSV_FILE)
    headers = ["TaxiID", "Pickup time", "Dropoff time",
    "Passenger count",
    "Trip Distance",
    "Total amount"]

    htmlReport = report.CreateReport(htmlReport, rides, headers)
    printReport = report.CreateReport(printReport, rides, headers)

    htmlReport.create_report()
    printReport.create_report()


if __name__ == '__main__':
    main()
