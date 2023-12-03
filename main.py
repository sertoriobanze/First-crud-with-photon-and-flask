from flask import Flask, render_template, request, redirect, flash,session,jsonify
import mysql.connector


connexao = mysql.connector.connect(
    host= 'localhost',
    user= "root",
    database= 'aula3',
    password=''
)

cursor = connexao.cursor()


app = Flask(__name__)
app.secret_key = 'root{}root'  # Defina uma chave secreta para a sessão

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


@app.route("/dashboard")
def dashboard():
    # Verifica se o usuário está autenticado
    if 'user_id' in session:
        user_id = session['user_id']

        # Agora você tem o user_id disponível no dashboard
        # Pode usar para buscar os dados do usuário no banco de dados

        cursor.execute(f"SELECT nome,email FROM Users WHERE id = {user_id}")
        user = cursor.fetchone()

        total_despesas, total_receitas = obter_totais(user_id)

        saldo = total_receitas - total_despesas

        return render_template("Dashboard.html", user_id=user_id, user=user, total_despesas=total_despesas, total_receitas=total_receitas, saldo=saldo, jsonify=jsonify)
    else:
        # Se o usuário não estiver autenticado, redireciona para a página de login
        return redirect("/")


@app.route("/autenticarUser", methods=["POST"])
def autenticar_user():
    if request.method == "POST":
        senha = request.form['userPass']
        nome = request.form['Username']

        cursor.execute(f"SELECT id, nome, senha FROM Users WHERE nome='{nome}' AND senha='{senha}'")
        user = cursor.fetchone()  # Apenas uma linha deve ser retornada

        if user:
            # Se a autenticação for bem-sucedida, armazena o ID do usuário na sessão
            session['user_id'] = user[0]
            return redirect("/dashboard")
        else:
            print("Algo deu errado")

    return "Método não permitido", 405

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect("/")

@app.route("/adcionarDispesa", methods=['POST'])
def adcionarDispesa():
    user_id = session['user_id']
    if request.method == 'POST':
        nome = request.form['nomeDispesa']
        valor = request.form['ValorDispesa']
        categoria = request.form['categoriaDispesa']


        query =f"insert into Despesas(nome,valor,categoria,data, idUser) values ('{nome}','{valor}','{categoria}',NOW(),'{user_id}')"
        cursor.execute(query)
        connexao.commit()
        print("deu certo")
        return jsonify({"message": "Dispesa adicionada com sucesso!"})  # Adicione este retorno

    return jsonify({"message": "Requisição inválida"})


@app.route("/adcionarReceita", methods=['POST'])
def adcionarReceita():
    user_id = session['user_id']
    if request.method == 'POST':
        nome = request.form['NomeReceita']
        valor = request.form['ValorReceita']
        categoria = request.form['categoriaReceita']

        query =f"insert into Receitas(nome,valor,categoria,data, idUser) values ('{nome}','{valor}','{categoria}',NOW(),'{user_id}')"
        cursor.execute(query)
        connexao.commit()
        print("deu certo")
        return jsonify({"message": "Receita adicionada com sucesso!"})  # Adicione este retorno

    return jsonify({"message": "Requisição inválida"})



def obter_totais(user_id):
    cursor.execute(f"SELECT SUM(valor) FROM Despesas WHERE idUser = {user_id}")
    total_despesas = cursor.fetchone()[0] or 0

    cursor.execute(f"SELECT SUM(valor) FROM Receitas WHERE idUser = {user_id}")
    total_receitas = cursor.fetchone()[0] or 0

    return total_despesas, total_receitas


if __name__ == "__main__":
    app.run(debug=True,port=9000)


