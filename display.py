import flask, pandas as pd

app = flask.Flask(__name__)

df=pd.read_csv('result.csv') #read csv file
df_html=df.to_html(render_links=True, escape=False) #convert to html , set link clickable and escape html tags

@app.route('/')
def index():
    return df_html

if __name__ == '__main__':
    app.run(debug=True,port=8888)
