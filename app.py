from flask import Flask, render_template, request, redirect, url_for
from models.pila import PilaApoyos
from models.cola import ColaTarjetas

app = Flask(__name__)

# Instancias globales
pila = PilaApoyos()
cola = ColaTarjetas()

@app.route('/')
def index():
    return redirect(url_for('menu'))

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    mensaje_cola = ''
    mensaje_pila = ''
    if request.method == 'POST':
        if 'agregar_cola' in request.form:
            tarjeta = request.form.get('tarjeta')
            if tarjeta:
                cola.encolar(tarjeta)
                mensaje_cola = 'Tarjeta agregada a la cola.'
        elif 'atender_cola' in request.form:
            atendido = cola.desencolar()
            if atendido:
                mensaje_cola = f'Se atendió a: {atendido}'
            else:
                mensaje_cola = 'La cola está vacía.'
        elif 'agregar_pila' in request.form:
            apoyo = request.form.get('apoyo')
            if apoyo:
                pila.apilar(apoyo)
                mensaje_pila = 'Apoyo agregado al historial.'
        elif 'deshacer_pila' in request.form:
            deshecho = pila.desapilar()
            if deshecho:
                mensaje_pila = f'Se deshizo el apoyo: {deshecho}'
            else:
                mensaje_pila = 'El historial está vacío.'
    return render_template('menu.html', 
        cola=cola.mostrar(), mensaje_cola=mensaje_cola,
        pila=pila.mostrar(), mensaje_pila=mensaje_pila)

if __name__ == '__main__':
    app.run(debug=True)
