# 🥐 Paulina Salgados

![Licença](https://img.shields.io/badge/Licença-MIT-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-red)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-orange)
![Status](https://img.shields.io/badge/Status-Funcional-success)
[![Deploy na DigitalOcean](https://img.shields.io/badge/Deploy-DigitalOcean-blue?style=for-the-badge&logo=digitalocean)](https://paulina-app-hmgir.ondigitalocean.app/)

## 📋 Descrição do Projeto

Sistema web minimalista para gestão de catálogo de salgados, desenvolvido com Flask 3, SQLAlchemy e interface HTML responsiva. Ideal para microempreendedores ou pequenos negócios do ramo alimentício que precisam controlar e divulgar seus produtos.

### 🎯 Funcionalidades

- **Autenticação de Administrador**: Acesso seguro via Flask-SimpleLogin
- **CRUD de Produtos**: Cadastro, edição, listagem e exclusão de salgados
- **Upload de Imagens**: Suporte para fotos dos produtos com validação de formato
- **Página de Contato**: Informações institucionais e de atendimento
- **Feedback ao Usuário**: Mensagens de erro e sucesso via Flask flash
- **Interface Responsiva**: Templates HTML com Jinja2 e assets estáticos
- **Pesquisa de Produtos**: Busca por nome de salgados no catálogo

## 🚀 Tecnologias Utilizadas

- **Python 3.12**: Linguagem de programação principal
- **Flask 3.x**: Framework web leve e flexível
- **SQLAlchemy 2.x**: ORM para interação com banco de dados
- **Flask-SQLAlchemy**: Integração do SQLAlchemy com Flask
- **Flask-SimpleLogin**: Sistema de autenticação simplificado
- **Flask-WTF**: Gerenciamento de formulários
- **Werkzeug**: Utilitários web, incluindo validação de arquivos
- **SQLite**: Banco de dados padrão (sem instalação adicional)
- **HTML/CSS**: Interface de usuário responsiva
- **Jinja2**: Sistema de templates para renderização dinâmica

## 📦 Pré-requisitos

Antes de começar, você precisará ter instalado:

- Python 3.12 ou superior
- Pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

## ⚙️ Instalação e Execução

### Usando Poetry (recomendado)

1. Clone este repositório:
```bash
git clone https://github.com/ezerodrigues/paulina-salgados.git
cd paulina-salgados
```

2. Instale as dependências com Poetry:
```bash
poetry install
```

3. Ative o ambiente virtual:
```bash
poetry shell
```

4. Execute a aplicação:
```bash
python app.py
```

### Usando Pip

1. Clone este repositório:
```bash
git clone https://github.com/ezerodrigues/paulina-salgados.git
cd paulina-salgados
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python app.py
```

5. Acesse a aplicação em seu navegador: http://localhost:5000

## 🔐 Credenciais de Acesso

Para acessar a área administrativa, utilize:
- **Usuário**: admin
- **Senha**: Silver2@@

> ⚠️ **Importante**: Em ambiente de produção, altere as credenciais e a chave secreta no arquivo app.py.

## 📁 Estrutura de Diretórios

```
paulina-salgados/
├── instance/              # Banco de dados SQLite
├── static/                # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/               # Estilos da aplicação
│   ├── js/                # Scripts JavaScript
│   └── imagens/           # Imagens dos produtos
├── templates/             # Templates HTML com Jinja2
│   ├── index.html         # Página inicial
│   ├── produtos.html      # Listagem de produtos
│   ├── cadastrar.html     # Formulário de cadastro
│   ├── editar.html        # Formulário de edição
│   └── contatos.html      # Página de contatos
├── .gitignore             # Arquivos ignorados pelo Git
├── app.py                 # Aplicação principal Flask
├── Procfile               # Configuração para deploy (Heroku/Render)
├── pyproject.toml         # Configuração do Poetry
├── poetry.lock            # Lock de dependências do Poetry
├── requirements.txt       # Dependências para pip
└── README.md              # Documentação do projeto
```

## 💻 Detalhes de Implementação

### Modelo de Dados

O sistema utiliza um modelo simples para os produtos:

```python
class Product(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500))
    ingredientes = db.Column(db.String(500))
    origem = db.Column(db.String(100))
    imagem = db.Column(db.String(100))
```

### Rotas Principais

- **/** - Página inicial
- **/listar_produtos** - Listagem e pesquisa de produtos
- **/cadastrar_produtos** - Formulário de cadastro
- **/editar_produtos/<id>** - Edição de produto existente
- **/deletar_produto/<id>** - Remoção de produto
- **/meus_contatos** - Página de contato

### Validação de Imagens

O sistema implementa validação de segurança para uploads de imagens:

```python
def validar_imagem(nome_imagem):
    extensoes_permitidas = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
    nome_seguro = secure_filename(nome_imagem)
    extensao = os.path.splitext(nome_seguro)[1].lower()
    if extensao in extensoes_permitidas:
        return nome_seguro
    else:
        return None
```

## 🖥️ Exemplos de Uso

### Fluxo de Administração

1. Acesse a aplicação e faça login com as credenciais de administrador
2. Na página de produtos, visualize o catálogo atual
3. Para adicionar um novo produto, clique em "Cadastrar Produto"
4. Preencha o formulário com nome, descrição, ingredientes, origem e imagem
5. Para editar um produto existente, clique no botão "Editar" na listagem
6. Para remover um produto, clique no botão "Deletar"

### Pesquisa de Produtos

1. Na página de produtos, utilize o campo de pesquisa
2. Digite o nome ou parte do nome do produto desejado
3. Clique em "Pesquisar" para filtrar os resultados

## 🔄 Deploy

O projeto está configurado para deploy em plataformas como Heroku, Render ou PythonAnywhere:

1. Para Heroku/Render, o Procfile já está configurado
2. Para outras plataformas, configure o WSGI para apontar para `app:app`
3. Certifique-se de configurar variáveis de ambiente para as credenciais e chave secreta

## 🛣️ Roadmap

Melhorias planejadas para futuras versões:

- [ ] Implementar sistema de categorias para produtos
- [ ] Adicionar painel de estatísticas de visualização
- [ ] Criar API REST para integração com aplicativos móveis
- [ ] Implementar sistema de pedidos online
- [ ] Adicionar suporte para múltiplos idiomas
- [ ] Melhorar a segurança com variáveis de ambiente para credenciais
- [ ] Implementar testes automatizados

## 👨‍💻 Autor

**Eliézer Rodrigues**

- GitHub: [ezerodrigues](https://github.com/ezerodrigues)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
