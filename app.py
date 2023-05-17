from flask import Flask, render_template,session,redirect,url_for,request
from models import raw_data,fea_data,generate_plots1,generate_plots2

app = Flask(__name__)
app.secret_key = 'jagan'

@app.route('/')
def index():
    return render_template('plot.html')
@app.route('/raw')
def raw_d():
    plot_data=raw_data()
    return render_template('plot.html', plot_data=plot_data)
@app.route('/fea')
def fea_d():
    feat_data=fea_data()
    return render_template('plot.html', feat_data=feat_data)
@app.route('/gen', methods=['GET','POST'])
def gen_d():
    if request.method == 'POST':
        if request.form.get("btn1") == "Submit":
            value = request.form['states']
            print(value)
            l1 = generate_plots1(value)
            l2 = generate_plots2(value)
            return render_template('plot.html', l1=l1, l2=l2)
    return render_template('plot.html')



@app.route('/toggle1')
def toggle1():
    if 'show_plots1' not in session:
        session['show_plots1'] = True
    else:
        session['show_plots1'] = not session['show_plots1']
    return redirect(url_for('raw_d'))

@app.route('/toggle2')
def toggle2():
    if 'show_plots2' not in session:
        session['show_plots2'] = True
    else:
        session['show_plots2'] = not session['show_plots2']
    return redirect(url_for('raw_d'))

@app.route('/toggle3')
def toggle3():
    if 'show_plots3' not in session:
        session['show_plots3'] = True
    else:
        session['show_plots3'] = not session['show_plots3']
    return redirect(url_for('fea_d'))

@app.route('/toggle4')
def toggle4():
    if 'show_plots4' not in session:
        session['show_plots4'] = True
    else:
        session['show_plots4'] = not session['show_plots4']
    return redirect(url_for('fea_d'))

@app.route('/toggle5')
def toggle5():
    if 'show_plots5' not in session:
        session['show_plots5'] = True
    else:
        session['show_plots5'] = not session['show_plots5']
    return redirect(url_for('fea_d'))


if __name__ == '__main__':
    app.run(debug=True)
