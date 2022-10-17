# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME

# Patrones de diseño implementados
- Command: Archivo print_report.py
- Strategy: Archivo report.py

# Principios SOLID
- SRP (Single Responsibility Principle) - print_report.py Línea 20
Dentro de la clase PrintReport en la línea 20 se encuentran tres distintas funciones que son diferentes entre sí y cada una tiene un propósito distinto; la primera función se encarga de hacer el formateo de las cantidades, la segunda se encarga de generar el contenido y la tercera se encarga de crear el archivo.
- OCP (Open Close Principle) - report.py Línea 25
Dentro de este archivo es posible generar nuevo código sin alterar la funcionalidad del que ya existe o sin la necesidad de cambiar el código actual.
- ISP (Interface Segregation Principle) - main.py Línea 10
Cada parte del código esta dividida en partes pequeñas, por lo que para realizar una función en específica solo se tiene que llamar a la función deseada, de tal manera que no se ejecute código innecesario.
