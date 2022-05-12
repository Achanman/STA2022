from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="数値を入力してください。")

@app.route('/result', methods=["GET"])
def result_get():
    # GET送信の処理
    field = request.args.get("field","")
    n = int(field)
    if n % 2 == 0:
        return render_template('result.html', message = "{}は偶数です。".format(field))
    else:
        return render_template('result.html', message = "{}は奇数です。".format(field))

@app.route('/result', methods=["POST"])
def result_post():
    # POST送信の処理
    field = request.form["field"]
    i = int(field)
    j = 2
    isPrime = False
    while j <= i:
        if i % j == 0:
            break
        j += 1
    
    if j == i:
        isPrime = True

    if isPrime:
        return render_template('result.html', message = "{}は素数です.".format(field))
    else:
        return render_template('result.html', message = "{}は素数ではありません.".format(field))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)