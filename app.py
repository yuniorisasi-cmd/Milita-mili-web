
import os
from flask import Flask, render_template

app = Flask(__name__)

lista_productos = [
    {
        "nombre": "Natura Kaiak Oceano",
        "descripcion": "Desodorante corporal masculino - 100 ml",
        "precio": "2 x S/ 32.99",
        "imagen": "kaiak_oceano.png",
        "categoria": "Perfumes"
    },
    {
        "nombre": "Natura Homem Coraggio",
        "descripcion": "Perfume masculino",
        "precio": "2 x S/ 144.90",
        "imagen": "homem_coraggio.png",
        "categoria": "Perfumes"
    },
    {
        "nombre": "Natura Kaiak Urbe",
        "descripcion": "Perfume masculino - 100 ml",
        "precio": "2 x S/ 100.00",
        "imagen": "kaiak_urbe.png",
        "categoria": "Perfumes"
    },
    {
        "nombre": "Avon Care Aceite de Coco 6 en 1",
        "descripcion": "Aceite de coco para el cuidado de la piel",
        "precio": "2 x S/ 33.99",
        "imagen": "aceite_coco.png",
        "categoria": "Cuidado personal"
    },
    {
        "nombre": "Máscara Invisible",
        "descripcion": "Máscara para definir cejas y pestañas",
        "precio": "2 x S/ 15.99",
        "imagen": "mascara_invisible.png",
        "categoria": "Maquillaje"
    },
    {
        "nombre": "Avon Care Cereza 6 en 1",
        "descripcion": "Crema corporal con aroma a cereza",
        "precio": "2 x S/ 38.70",
        "imagen": "care_cereza.png",
        "categoria": "Cuidado personal"
    },
    {
        "nombre": "Avon Care Footworks 3 en 1",
        "descripcion": "Producto para el cuidado de los pies",
        "precio": "2 x S/ 20.00",
        "imagen": "footworks.png",
        "categoria": "Cuidado personal"
    }
]


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/productos")
def productos():
    return render_template(
        "productos.html",
        productos=lista_productos
    )


@app.route("/marcas")
def marcas():
    return render_template("marcas.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=puerto,
        debug=False
    )