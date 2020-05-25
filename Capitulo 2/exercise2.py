from flask import Flask
import time


app = Flask(__name__)
@app.route("/date")
def date():
    date = (time.strftime("%y/%m/%d"))
    hour = (time.strftime("%I:%M:%S"))
    data = {"Date":date,"Hour":hour}
    times = []
    times.append(data)
    return {"La fecha y hora actual es: ":data}

if __name__ == '__main__':
    app.run()