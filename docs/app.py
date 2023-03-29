from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def file_list():
    folder_path = "./Web design" # Change this to the path to your folder
    file_names = os.listdir(folder_path)
    return render_template("file_list.html", files=file_names)

if __name__ == "__main__":
    app.run(debug=True)
