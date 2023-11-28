#flask ortamını kendi kodlarımız içersine aktarmak
from flask import Flask, render_template, request, url_for

#uygulamamıza ismini verdik
app = Flask(__name__)

#dekarötör = fonksiyonlarımız veya bir fonksiyon sınıfın davranışını değiştirmek için kulanılır.
@app.route("/")
def ansayfa():
    return render_template("index.html")

@app.route("/sonuc", methods=['POST'])
def sonuc():

    name = request.form.get("isim"),
    email = request.form.get("emaill"),
    date = request.form.get("tarih")

    return render_template("sonuc.html",
                           name = name,
                           email =email,
                           date = date)


@app.route("/pelin")
def pelin():
    return render_template("örnek.html")

app.run(debug=True)

