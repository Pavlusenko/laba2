import copy

from flask import render_template
from flask import Flask
from geometric import Circle

app = Flask(__name__)

@app.route('/')
def index():
    result = []

    c1 = Circle(3, 5, 3)
    c2 = Circle(7, 8, 2)

    print(c1)
    print(c2)

    result.append(c1)
    result.append(c2)

    print("Площадь круга: ", c1.area())
    print("Длина окружности: ", c2.perimeter())

    result.append("Площадь круга: " + str(c1.area()))
    result.append("Длина окружности: " + str(c2.perimeter()))

    print("c1 concentric c2 ", c1.concentrichnost(c2))
    result.append("c1 concentric c2 " + str(c1.concentrichnost(c2)))

    return render_template('base.html', results=result)

if __name__ == '__main__':
    app.run(debug=True)




