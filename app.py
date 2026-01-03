from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista "Base de Datos" temporal (se borra si reinicias el servidor)
usuarios_registrados = []

@app.route("/")
def index():
    # Enviamos la lista de usuarios al HTML para verlos abajo
    return render_template("registro.html", usuarios=usuarios_registrados)

@app.route("/registrar", methods=["POST"])
def registrar():
    # Obtenemos los datos del formulario
    nombre = request.form.get("nombre")
    email = request.form.get("email")

    if nombre and email:
        # Guardamos en nuestra lista del backend
        usuarios_registrados.append({"nombre": nombre, "email": email})
    
    return redirect("/") # Recargamos la página para ver los cambios

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)