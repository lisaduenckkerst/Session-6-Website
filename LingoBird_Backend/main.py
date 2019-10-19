from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")#CONTROLLER
def Index():
    return render_template("Index.html")#VIEW

if __name__ == '__main__':
    app.run()