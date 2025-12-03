from flask import Flask,jsonify, render_template, request
from utils.pipeline import add_resume_to_db , generate_final_results
from utils.verctorDB import vectorDB
from utils.personalEmail import sendmail
import os
global_results = [] 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    job_description = request.form["job_description"]
    resumes = request.files.getlist("resume")
    pdfData = []
    
    from utils.pipeline import db
    db.clear()
    db.save()

    for file in resumes:
        uploadFiles = os.path.join("uploads",file.filename)
        file.save(uploadFiles)
        add_resume_to_db(uploadFiles)
    
    output = generate_final_results(job_description)
    if isinstance(output, dict):
        output = [output]
    elif isinstance(output, str):
        try:
            import json
            obj = json.loads(output)
            if isinstance(obj, dict):
                output = [obj]
            elif isinstance(obj, list):
                output = obj
            else:
                output = []
        except:
            output = []
    print("FINAL RESULTS:", output)

    print("FINAL RESULTS PASSED TO TEMPLATE:")
    print("TYPE:", type(output))
    import pprint
    pprint.pprint(output)
    global global_results
    global_results = output
    return render_template("results.html",results=output,job_description=job_description)


@app.route("/get_candidate", methods=["POST"])
def get_candidate():
    data = request.get_json()
    index = int(data["index"])

    global global_results
    selected_candidate = global_results[index]

    email = selected_candidate["email"]
    name = selected_candidate["Candidate Name"]

    # 🟢 CALL YOUR EMAIL SENDING FUNCTION
    sendmail(email, name)

    return jsonify({"email": email})


if __name__ == "__main__":
    app.run(debug=True)
    