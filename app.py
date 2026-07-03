from flask import Flask
from urllib.parse import quote
import requests
import os


app = Flask(__name__)
redfox = "made by jone nunes"

html = "https://raw.githubusercontent.com/jone-nunes/redfox/refs/heads/main/index.html"

@app.route("/")
def imprimir():
	return requests.get(html).text
	
@app.route("/chatbot/<string:t>")
def chatbot(t):
	re = requests.get(f"https://gen.pollinations.ai/text/{t}/?key={key}")
	return re.text

@app.route("/somar/<int:n>/<int:m>")
def somar(n, m):
	sum = n + m
	return f"{n} + {m} = {sum}"

@app.route("/mult/<int:p>/<int:i>")
def multiplicacao(p, i):
	mult = p * i
	return f"{p} x {i} = {mult}"
	
@app.route("/subt/<int:q>/<int:w>")
def subtracao(q, w):
	subt = q - w
	return f"{q} - {w} = {subt}"

@app.route("/divid/<int:z>/<int:x>")
def divisao(z, x):
	try:
		divid = z / x
		return f"{z} ÷ {x} = {divid}"
	except ZeroDivisionError:
		return "erro: não é possivel dividir por 0."
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=10000)
