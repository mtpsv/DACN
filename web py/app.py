from flask import Flask, render_template, request
from bs import KiemTraPhatNguoi
app = Flask(__name__)

# Route để hiển thị và xử lý form
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        bienso = request.form['bienso']
        result = KiemTraPhatNguoi(bienso)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
