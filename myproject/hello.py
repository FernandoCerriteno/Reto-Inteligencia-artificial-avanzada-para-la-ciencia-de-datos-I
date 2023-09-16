from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        x = []
        x.append(request.form['back_x'])
        x.append(request.form['back_z'])
        x.append(request.form['thigh_x'])
        x.append(request.form['thigh_z'])

        loaded_model = pickle.load(open('D:/fcmdr/Documents/Programas/Python/Semestre7/Flask/myproject/finalized_model.sav', 'rb'))
        result = loaded_model.predict(np.reshape(x, (-1, 4)))
        return f'Label: {result}'

    return '''
        <form method="post">
            <p>Introduzca el valor de:</p>
            <p>back_x: <input type="text" name="back_x"></p>
            <p>back_z: <input type="text" name="back_z"></p>
            <p>thigh_x: <input type="text" name="thigh_x"></p>
            <p>thigh_z: <input type="text" name="thigh_z"></p>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run()