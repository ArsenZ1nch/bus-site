from flask import Flask, redirect, render_template, request

server = Flask(__name__)


@server.route('/')
def homepage():
  return render_template("index.html")

@server.route('/sources', methods=['POST', 'GET'])
def sources():
  if request.method == 'POST':
    return render_template('/sources.html')
  return redirect('/')

@server.route('/<string:page_name>')
def page(page_name):
  if page_name == "index":
    return redirect('/')

  try:
    return render_template(f"{page_name}.html")
  except:
    return redirect('/')


if __name__ == "__main__":
  server.run(host='0.0.0.0', port=8080)