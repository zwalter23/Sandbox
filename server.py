# Flask stuff (server, routes, request handling, session, etc.)
# This layer should consist of logic that is related to Flask. (This should be the only file importing from Flask.)


from flask import Flask, request, redirect, render_template
import data_manager
import util

app = Flask(__name__)

@app.route("/list")
@app.route("/")
def main_page():
    return render_template("list.html", fields=util.fields, questions=util.questions)


@app.route("/question/<question_id>", methods=['GET','POST'])
def selected_question_page(question_id):
    return render_template("question.html", question_title=request.form['question_title'], question=request.form['question'])


@app.route("/add-question", methods=['GET','POST'])
def add_question():
    return render_template("add-question.html", question_id=util.new_id)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
