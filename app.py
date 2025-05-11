# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

capitais = {
    "acre": "Rio Branco",
    "alagoas": "Maceió",
    "amapa": "Macapá",
    "amazonas": "Manaus",
    "bahia": "Salvador",
    "ceara": "Fortaleza",
    "distrito federal": "Brasília",
    "espirito santo": "Vitória",
    "goias": "Goiânia",
    "maranhao": "São Luís",
    "mato grosso": "Cuiabá",
    "mato grosso do sul": "Campo Grande",
    "minas gerais": "Belo Horizonte",
    "para": "Belém",
    "paraiba": "João Pessoa",
    "parana": "Curitiba",
    "pernambuco": "Recife",
    "piaui": "Teresina",
    "rio de janeiro": "Rio de Janeiro",
    "rio grande do norte": "Natal",
    "rio grande do sul": "Porto Alegre",
    "rondonia": "Porto Velho",
    "roraima": "Boa Vista",
    "santa catarina": "Florianópolis",
    "sao paulo": "São Paulo",
    "sergipe": "Aracaju",
    "tocantins": "Palmas"
}

@app.route('/capital')
def get_capital():
    estado = request.args.get('estado', '').lower()
    capital = capitais.get(estado)

    if capital:
        response = jsonify({"capital": capital})
    else:
        response = jsonify({"erro": "Não encontrado"}), 404

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

