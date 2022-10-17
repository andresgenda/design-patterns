class CreateContentCommand:

    def __init__(self, rides, service):
        self.rides = rides
        self.service = service
    
    def execute(self):
        return self.service.create_content(self.rides)

class CreateFileCommand:

    def __init__(self, content, service):
        self.content = content
        self.service = service
    
    def execute(self):
        self.service.create_file(self.content)

class PrintReport:

    def __init__(self):
        pass

    def create_content(self, rides):
        myContent = ""
        for ride in rides:
            myContent += "hola\n"
        return myContent
    
    def create_file(self, content):
        with open("financial-report.txt", "w") as file:
            file.write(content)