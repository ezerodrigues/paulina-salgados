# Paulina Salgados

Sistema web minimalista para gestão de catálogo de salgados, desenvolvido com Flask 3, SQLAlchemy e interface HTML responsiva. Ideal para microempreendedores ou pequenos negócios do ramo alimentício que precisam controlar e divulgar seus produtos.

---

## 📑 Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Stack e Dependências](#stack-e-dependências)
- [Instalação e Execução](#instalação-e-execução)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Detalhes de Implementação](#detalhes-de-implementação)
- [Roadmap](#roadmap)
- [Licença](#licença)
- [Contato](#contato)

---

## Visão Geral

O `paulina-salgados` automatiza o controle e apresentação de produtos para pequenas empresas do setor alimentício, centralizando o cadastro, edição e visualização de informações do catálogo via interface web simples e protegida por autenticação.

## Funcionalidades

- **Autenticação de Administrador** (Flask-SimpleLogin)
- **CRUD de Produtos**: Cadastro, edição, listagem e exclusão de salgados.
- **Página de Contato**: Informações institucionais e de atendimento.
- **Feedback ao usuário**: Mensagens de erro e sucesso via Flask flash.
- **Interface web responsiva**: Templates HTML com Jinja2 e assets estáticos.

## Stack e Dependências

- **Python 3.12**
- **Flask 3.x**
- **SQLAlchemy 2.x**
- **Flask-SQLAlchemy**
- **Flask-SimpleLogin**
- **Flask-WTF** (Formulários)
- **Gunicorn** (produção)
- **WTForms**
- **SQLite** (banco padrão)

*Dependências gerenciadas via Poetry e/ou requirements.txt.*

