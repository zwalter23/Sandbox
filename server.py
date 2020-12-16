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


@app.route("/question/<question_id>")
def selected_question_page(question_id):
    title = request.form["question_title"]  
    message = request.form["question"]  
    return render_template("question.html", question_id, title, message, submission_time=util.actual_time, view_number=0, vote_number=0 )


@app.route("/add-question", methods=['GET','POST'])
def add_question():
    return render_template("add-question.html", question_id=util.new_id)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
