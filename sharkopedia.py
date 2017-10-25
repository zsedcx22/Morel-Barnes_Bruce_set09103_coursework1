from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)

@app.route('/sharkopedia/', methods=['POST','GET'])
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
        sharks=sharks) #launches the jinja2 template
    elif finddir!=None:
      directory+="/{0}".format(finddir)
      if sharkgenus!=None: #if 'genus' has a value
        for file in files: #for each file in the directory
          if file.endswith(".txt"): #if it ends with '.txt' then
            sharks.append(file[:-4]) #remove the .txt and put the file name
                                     #into a list
        return render_template('sharktemplate.html', sharkorder=sharkorder,
          sharkfamily=sharkfamily, sharkgenus=sharkgenus, sharkname=sharkname,
          sharks=sharks) #launches the jinja2 template
      else:
        sharks=os.listdir(directory) #insert each of the directory or file names from the current directory
        return render_template('sharktemplate.html', sharkorder=sharkorder,
          sharkfamily=sharkfamily, sharkgenus=sharkgenus, sharkname=sharkname,
          sharks=sharks) #launches the jinja2 template
  elif request.method=='GET':
    sharks=os.listdir(directory) #insert each of the directory names from the base directory (i.e. the Orders)
    return render_template('sharktemplate.html', sharkorder=sharkorder,
      sharkfamily=sharkfamily, sharkgenus=sharkgenus, sharkname=sharkname,
      sharks=sharks) #launches the jinja2 template
directory="sharks" #setting the base directory for navigating the shark store
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
