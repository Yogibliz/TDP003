from flask import Flask, render_template, url_for, request, abort
import logging
app = Flask(__name__)
from logging.handlers import RotatingFileHandler
import data

#Load the data.json file. If it doesn't exist, return a error message.
def load_data():
    if data.load('data.json') == None:
        print('No data.json file')
    return data.load('data.json')

@app.route('/')
@app.route('/index/')
#Print out the home page for the route (/) and (/index/) and display the data filtered.
#Get the last 3 projects. Uses search function to get the last 3 projects by sorting by start date.
def home_page():
    projects = data.search(load_data(), sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None)
    return render_template('index.html', data=projects)

#Print out the projects page for the route (/projects) and display all the projects.
#Also handles the search functionality in different cases. Depending on what the user provided for sort_by, sort_order and search_fields.
#It has project_name (search_field), Descending order (sort_order) and start_date (sort_by) as default values. These are checked by default in the form.
@app.route('/projects/', methods=["POST", "GET"])
def projects_page():
    
    if request.method == 'POST':
        sort_by = request.form.get("sort_by")
        sort_order = request.form.get("sort_order")
        techniques = request.form.getlist("techniques")
        search = request.form.get("searchterm")
        search_fields = request.form.getlist("search_fields")
        if search_fields == []:
            search_fields = None

    else:
        sort_by = "start_date"
        sort_order = "desc"
        techniques = []
        search = None
        search_fields = None

    projects = load_data()

    #Has to check is not None since python doesn't like None as a possible value.
    if sort_by and sort_order is not None:
        project_search = data.search(projects, sort_by, sort_order, techniques, search, search_fields)
        return render_template("projects.html", data=project_search)
    
    #Does the same since flask wants a else statement as a backup. But it doesn't do anything different. It just gives the values that are already selected in the form by default.
    else:
        sort_by = "start_date"
        sort_order = "desc"
        search_fields = "project_name"
        project_search = data.search(projects, sort_by, sort_order, techniques, search, search_fields)
        return render_template("projects.html", data=project_search)

#Print out the projects page for the route (/projects) and display the selected project(id) where id is the project_id in data.json.
@app.route('/project/<id>')
def project_page(id):
    
    #Returns 404.html in case the project doesn't exist.    
    try: id = int(id)
    
    except:
        app.logger.error(f'Projekt id: {id} kunde inte hittas.')
        abort(404, id)
    
    if data.get_project(load_data(), id) == None:
        app.logger.error(f'Projekt id: {id} kunde inte hittas.')
        abort(404, id)
    
    projects = data.get_project(load_data(), int(id))
    techniques = data.get_techniques(load_data())
    
    #Make it so that the template is rendered if a id matches.
    return render_template('projectpage.html', data=projects, tech=techniques)
        
#Display the techniques page for the route (/techniques/) and display a filter at the top.
#Displays all the techniques which have one of the techniques selected.
#Could add a filter for it to include all options or exclusivly search for projects which match all of the techniques selected.
@app.route('/techniques/', methods=["POST", "GET"])
def technique_page():

    if request.method == "POST":
        techniques = request.form.getlist("techniques")
        sort_by = "start_date"
        sort_order = "desc"
        search = None
        search_fields = None
    else:
        techniques = []
        sort_by = "start_date"
        sort_order = "desc"
        search = None
        search_fields = None
        
    projects = load_data()
    techs = data.get_techniques(projects)
        
    projects_filtered = data.search(projects, sort_by, sort_order, techniques, search, search_fields)

    return render_template('techniques.html', data=projects_filtered, tech=techs)

#Default error handler for 404 page. Returns 404.html in case the page doesn't exist.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


if __name__ == "__main__":
    #No error output to the file?
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler('server.log')
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run(debug = True)
