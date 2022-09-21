import flask, json

app = flask.Flask(__name__)

f = open("result.json", "r") #open json file with result from Cve.py
f2 = open("resultAll.json", "r") #open json file with result from CveAll.py

#transform json to html
def json2html(json):
    table =f'<table border="3"><tr>'
    table += f'<th>CVE</th>'
    table += f'<th>Score</th>'
    table += '</tr>'
    for row in json:
        table += '<tr>'
        table += f'<td><a href={row["url"]}>{row["cve"]}</td>'
        table += f'<td>{row["score"]}</td>'
        table += '</tr>'
    table += '</table>'
    return table

result1 = json2html(json.load(f))
result2 = json2html(json.load(f2))
@app.route('/all')
def All(): 
    return result2

@app.route('/')
def index():
    return result1

if __name__ == '__main__':
    app.run(debug=False,port=80,host='0.0.0.0') #run app

