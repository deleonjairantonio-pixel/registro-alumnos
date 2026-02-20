from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        nombre = request.form["nombre"]
        matricula = request.form["matricula"]
        carrera = request.form["carrera"]
        semestre = request.form["semestre"]
        fecha = request.form["fecha"]

        return f"""
        <h2>Datos enviados</h2>
        Nombre: {nombre}<br>
        Matrícula: {matricula}<br>
        Carrera: {carrera}<br>
        Semestre: {semestre}<br>
        Fecha: {fecha}
        """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
