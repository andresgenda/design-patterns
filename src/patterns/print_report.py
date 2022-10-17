class CreateContentCommand:

    def __init__(self, rides, service, headers):
        self.rides = rides
        self.service = service
        self.headers = headers
    
    def execute(self):
        return self.service.create_content(self.rides, self.headers)

class CreateFileCommand:

    def __init__(self, content, service):
        self.content = content
        self.service = service
    
    def execute(self):
        self.service.create_file(self.content)

class PrintReport:

    def __init__(self):
        pass

    def format_tolls_amount(self, tolls_amount):
        if tolls_amount > 0:
            return str(tolls_amount)
        return f"({tolls_amount})"

    def create_content(self, rides, headers):
        myContent = "Taxi Report\n"
        for header in headers:
            myContent += "{:<20}".format(header)
        for ride in rides:
            myContent += "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(ride.taxi_id, ride.pick_up_time.isoformat(
            ), ride.drop_of_time.isoformat(), ride.passenger_count, ride.trip_distance, self.format_tolls_amount(ride.tolls_amount))
        return myContent
    
    def create_file(self, content):
        with open("financial-report.txt", "w") as file:
            file.write(content)