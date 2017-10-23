from flask import Flask, render_template
app = Flask(__name__)

@app.route('/sharkopedia/')
@app.route('/sharkopedia/<sharkorder>/')
@app.route('/sharkopedia/<sharkorder>/<sharkfamily>/')
@app.route('/sharkopedia/<sharkorder>/<sharkfamily>/<sharkgenus>/')
@app.route('/sharkopedia/<sharkorder>/<sharkfamily>/<sharkgenus>/<sharkname>')
def shark(sharkorder=None, sharkfamily=None, sharkgenus=None, sharkname=None):
  return render_template('sharktemplate.html', sharkorder=sharkorder,
  sharkfamily=sharkfamily, sharkgenus=sharkgenus, sharkname=sharkname)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
