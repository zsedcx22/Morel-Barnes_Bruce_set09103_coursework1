from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)
#xd
@app.route('/sharkopedia/', methods=['POST','GET'])
@app.route('/sharkopedia/<sharkorder>/', methods=['POST','GET'])
@app.route('/sharkopedia/<sharkorder>/<sharkfamily>/', methods=['POST','GET'])
@app.route('/sharkopedia/<sharkorder>/<sharkfamily>/<sharkgenus>/',
methods=['POST','GET'])
@app.route('/sharkopedia/<sharkorder>/<sharkfamily>/<sharkgenus>/<sharkname>')

#MODIFIERS FOR DIR ENDING UP SOMETHING LIKE directory+="/{0}".format(sharkorder)
def shark(sharkorder=None, sharkfamily=None, sharkgenus=None, sharkname=None):
  global directory
  sharks=[]
  finddir=(str(request.form.getlist('submit'))[3:])[:-2]
  if request.method=='POST':
    #print(request.form.getlist('submit')[1:])
    if finddir=='all': #if the 'all' button has been pressed
      for root, dirs, files in os.walk(directory): #for all directories and
                                                   #files in the selected dir
        for file in files: #for each file in the directory
          if file.endswith(".txt"): #if it ends with '.txt' then
            sharks.append(file) #remove the .txt and put the file name
                                     #into a list
            #print(file)
      return render_template('sharktemplate.html', sharkorder=sharkorder,
        sharkfamily=sharkfamily, sharkgenus=sharkgenus, sharkname=sharkname,
        sharks=sharks)
    elif finddir!=None:
      directory+="/{0}".format(finddir)
      if sharkgenus!=None: #if 'genus' has a value
        for file in files: #for each file in the directory
          if file.endswith(".txt"): #if it ends with '.txt' then
            sharks.append(file[:-4]) #remove the .txt and put the file name
                                     #into a list
        return render_template('sharktemplate.html', sharkorder=sharkorder,
          sharkfamily=sharkfamily, sharkgenus=sharkgenus, sharkname=sharkname,
          sharks=sharks)
      else:
        sharks=os.listdir(directory)
        return render_template('sharktemplate.html', sharkorder=sharkorder,
          sharkfamily=sharkfamily, sharkgenus=sharkgenus, sharkname=sharkname,
          sharks=sharks)
  elif request.method=='GET':
    sharks=os.listdir(directory)
    return render_template('sharktemplate.html', sharkorder=sharkorder,
      sharkfamily=sharkfamily, sharkgenus=sharkgenus, sharkname=sharkname,
      sharks=sharks)
directory="sharks"
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
