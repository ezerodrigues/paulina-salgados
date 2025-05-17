from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import url_for
from flask import get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_simplelogin import SimpleLogin, login_required
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "Silver!37242@"
app.config["SIMPLELOGIN_USERNAME"] = "admin"
app.config["SIMPLELOGIN_PASSWORD"] = "Silver2@@"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///salgados.db"
db = SQLAlchemy()
db.init_app(app)
SimpleLogin(app)


def validar_imagem(nome_imagem):
    extensoes_permitidas = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
    nome_seguro = secure_filename(nome_imagem)
    extensao = os.path.splitext(nome_seguro)[1].lower()

    if extensao in extensoes_permitidas:
        return nome_seguro
    else:
        return None

class Product(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500))
    ingredientes = db.Column(db.String(500))
    origem = db.Column(db.String(100))
    imagem = db.Column(db.String(100))

    def __init__(self, 
                 nome: str, 
                 descricao: str, 
                 ingredientes: str,
                 origem: str,
                 imagem: str ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.ingredientes = ingredientes
        self.origem = origem
        self.imagem = imagem

@app.route("/")
# @login_required
def home():
    return render_template("index.html")


@app.route("/listar_produtos", methods=["GET","POST"])
@login_required
def listar_produtos():
    if request.method == "POST":
        termo = request.form["pesquisa"]
        resultado = db.session.execute(
            db.select(Product).filter(Product.nome.like(f'%{termo}%'))
        ).scalars()
        return render_template('produtos.html', produtos=resultado)

    produtos = db.session.execute(db.select(Product)).scalars()
    mensagens = [
        (categoria, mensagem)
        for categoria, mensagem in get_flashed_messages(with_categories=True)
        if mensagem != "login com sucesso"
    ]
    return render_template("produtos.html", produtos=produtos, mensagens=mensagens)



@app.route("/meus_contatos")
# @login_required
def meus_contatos():
    return render_template("contatos.html")


@app.route("/cadastrar_produtos", methods=['GET', 'POST'])
@login_required
def cadastrar_produtos():
    if request.method == "POST":
        dados = request.form
        imagem = request.files['imagem']

        nome_valido = dados['nome'].strip() != ''
        imagem_valida = imagem and imagem.filename != '' and validar_imagem(imagem.filename)

        if not nome_valido or not imagem_valida:
            status = {"type": "erro", "message": "Houve um erro ao cadastrar o produto, corrija os campos."}
            return render_template("cadastrar.html", status=status, form=dados)

        nome_imagem = validar_imagem(imagem.filename)

        try:
            produto = Product(
                dados['nome'],
                dados['descricao'],
                dados['ingredientes'],
                dados['origem'],
                nome_imagem
            )
            imagem.save(os.path.join('static/imagens', nome_imagem))
            db.session.add(produto)
            db.session.commit()
            status = {"type": "sucesso", "message": "Produto cadastrado com sucesso!"}
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            status = {"type": "erro", "message": "Houve um erro ao cadastrar o produto."}
            return render_template("cadastrar.html", status=status, form=dados)

        return render_template('cadastrar.html', status=status)

    return render_template("cadastrar.html")


@app.route("/editar_produtos/<int:id>", methods=["GET", 'POST'])
@login_required
def editar_produto(id):
    produto = db.session.execute(db.select(Product).filter(Product.id == id)).scalar()

    if request.method == "POST":
        dados_editados = request.form
        imagem = request.files['imagem']

        produto.nome = dados_editados['nome']
        produto.descricao = dados_editados['descricao']
        produto.ingredientes = dados_editados['ingredientes']
        produto.origem = dados_editados['origem']
        
        if imagem.filename:
            nome_imagem = validar_imagem(imagem.filename)
            if not nome_imagem:
                status = {"type": "erro", "message": "Extensão de imagem não permitida."}
                return render_template("editar.html", produto=produto, status=status)

            produto.imagem = nome_imagem
            imagem.save(os.path.join('static/imagens', nome_imagem))

        db.session.commit()
        flash(f"Produto {produto.nome} atualizado com sucesso!", "sucesso")
        return redirect(url_for("listar_produtos"))

    return render_template("editar.html", produto=produto)

@app.route("/deletar_produto/<int:id>")
@login_required
def deletar_produto(id):
    produto_deletado = db.session.execute(db.select(Product).filter(Product.id == id)).scalar()
    if not produto_deletado:
        flash("Produto não encontrado.", "erro")
        return redirect(url_for("listar_produtos"))

    db.session.delete(produto_deletado)
    db.session.commit()
    flash(f"Produto '{produto_deletado.nome}' deletado com sucesso!", "sucesso")
    return redirect(url_for("listar_produtos"))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()


