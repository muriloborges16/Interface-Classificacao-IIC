from flask import Flask, request, render_template
import pickle

modelo = pickle.load(open('modelo.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html',titulo="Classificação do Cliente")

@app.route('/predicaoform',methods=['POST'])
def form():
    credit_score = request.form['credit_score']    
    gender = request.form['gender']
    age = request.form['age']
    tenure = request.form['tenure']    
    balance = request.form['balance']
    products_number = request.form['products_number']
    credit_card = request.form['credit_card']
    active_member = request.form['active_member']
    estimated_salary = request.form['estimated_salary']
    France = request.form['France']
    Germany = request.form['Germany']
    Spain = request.form['Spain']
    
    result = modelo.predict([[credit_score, gender, age, tenure, balance, products_number,	credit_card, active_member, estimated_salary, France, Germany, Spain]])
    
    if result[0]==0:
        resultado='O cliente saiu do banco em algum período'
    elif result[0]==1:
        resultado='O cliente não saiu do banco em nenhum período'

    return render_template('resultado.html',titulo="Classificação do Cliente", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
