from flask import Flask, render_template, request, redirect, flash
import mysql.connector


connexao = mysql.connector.connect(
    host= 'localhost',
    user= "root",
    database= 'aula3',
    password=''
)

cursor = connexao.cursor()

#inserir dados na table

# nome = "sertorio banze"
# email ="banzetuma@gmail.com.com"
# senha = "12335"
#
#
# query =f"insert into Users(nome,email,senha) values ('{nome}','{email}','{senha}')"
#
# cursor.execute(query)
#
# connexao.commit()


#atualizar dados do user

# atualizar = f"Update Users set nome = '{nome}', email = '{email}' , senha = '{senha}' where id = 1"
#
# cursor.execute(atualizar)
# connexao.commit()

# deletar dados no banco

# deletar = f"delete from Users where id = 1"
#
# cursor.execute(deletar)
# connexao.commit()


# lerdados

# ler = "select * from Users"
# cursor.execute(ler)
# dados = cursor.fetchall()
# print(dados)



app = Flask(__name__)

@app.route("/")
def Login():
    return render_template("index.html")

massage = "sertorio"

@app.route('/signup')
def Signup():

    return render_template('signup.html')

@app.route("/cadastrar", methods=[ 'POST'])
def Cadastrar():
    if request.method == 'POST':
        # Se o método da requisição for POST, você pode acessar os dados do formulário
        nome = request.form['NewUserName']
        email = request.form['newEmail']
        senha = request.form['NewPass']

        query =f"insert into Users(nome,email,senha) values ('{nome}','{email}','{senha}')"
        cursor.execute(query)
        connexao.commit()

   # Verifica se o cadastro foi bem-sucedido antes de redirecionar
        if cursor.rowcount > 0:
            return redirect("/tabela")
        else:
            return "Erro ao cadastrar usuário"

    return redirect("/signup")  # Redireciona de volta para a página de cadastro se não for um POST




@app.route("/update/<int:id>")
def Update(id):
    cursor.execute(f"select * from Users where id = {id}")
    dados = cursor.fetchall()

    return render_template("update.html", dados = dados)

@app.route("/Atualiar", methods=['POST'])
def Atualiar():
    if request.method == 'POST':
        id = request.form['id']
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        cursor.execute(f"update Users set nome = '{nome}', email = '{email}' , senha = '{senha}' where id = {id}")
        connexao.commit()
        return redirect("/tabela")

@app.route("/delete/<int:id>")
def Delete(id):
    cursor.execute(f"delete from Users where id = {id}")
    connexao.commit()
    return redirect("/tabela")
@app.route("/tabela")
def Tabela():
    ler = "select * from Users"
    cursor.execute(ler)
    dados = cursor.fetchall()
    return render_template("tabela.html", dados = dados)

if __name__ == "__main__":
    app.run()


