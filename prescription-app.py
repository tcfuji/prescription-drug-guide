from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

import pandas as pd
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

# app = Flask(__name__)

class PandasForm(Form):
    name = StringField('Type in Rx query:', validators=[Required()])
    submit = SubmitField('Submit')

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SECRET_KEY'] = '123456'

    #target = pd.read_csv("LowCostDrugsTarget.csv")
    #walmart = pd.read_csv("LowCostDrugsWalmart.csv")
    #df = pd.concat([target, walmart], axis=1)

    db = pd.read_csv("lowcostdrugs.csv")

    '''@app.route('/df/<filename>')
    def df(filename):
        dataframe = pd.read_csv(filename)
        return render_template('df.html', name=filename, data=dataframe.to_html())

    @app.route('/user2/<name>')
    def user2(name):
        return render_template('user2.html', name=name)'''


    @app.route('/', methods=['GET', 'POST'])
    def index2():
        q = None
        form = PandasForm()
        if form.validate_on_submit():
            # print form.name.data
            q = form.name.data
            form.name.data = ''
        print db[db['DX'] == q]
        return render_template('index.html', form=form, data=db[db['DX'] == q].to_html())

    return app

if __name__ == "__main__":
    create_app().run(debug=True)