import json
from operator import itemgetter
from os.path import exists

def load(filename):
    if exists(filename) == False:
        return None
    with open(filename, 'r', encoding='utf-8') as json_file:
        data_list = json.load(json_file)
        sorted_list = sorted(data_list, key=itemgetter('project_id'))
    if sorted_list != None:
        return sorted_list
    if sorted_list == None:
        return None

def get_project_count(db):
    return len(db)

def get_project(db, id):
    for project in db:
        if project.get('project_id') == id:
            return project
    return None

def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):
    if not db:
        return []
    
    if search_fields == []:
        return []

    projects = db

    # Filter by techniques
    if techniques:
        #A list comprehension that loops through all the projects in the list. 
        #For each project it checks if there are any techniques (tech) in the techniques list (techniques) that is stored in the 'techniques_used' part of the json list. 
        #If there is a match for the selected technique it returns that. If there's no match it prints nothing, and if there is no technique searched for displays everything.

        # Working order:
        
        #Variable 'project' (the current project looked at)
        #For loop which checks the project in projects (all projects in the list.)
        #If any expression which checks if any of the techniques chosen (tech) is in the techniques list in the json file (project.get('techniques_used', []) for tech in techniques).
        projects = [project for project in projects if any(tech in project.get('techniques_used', []) for tech in techniques)]

    # Filter by search string in specified fields
    if search and search_fields:
        filtered_projects = []
        for project in projects:
            for field in search_fields:
                #Convert the value of 'field' in the project dictionary to a string, if none is found, return an empty string.
                #Then turns everything lowercase, this way the user input won't matter if it's using capitalisation or not.
                #Then checks if the search string was found in the field string, if it wasn't found it returns -1, which is why we're telling it (!= -1).
                #This way it only continues if the string is found. 
                if str(project.get(field, '')).lower().find(search.lower()) != -1:
                    filtered_projects.append(project)
                    break
        #Once all the projects have been searched, we append the projects which had a matching string, then add that value to the projects variable.
        projects = filtered_projects

    # Sort the projects
    if sort_by:
        #Returns True of False, depending on sort_order. If sort_order == desc = True
        #if sort_order == something else = False. This is needed since the sorted function needs(iterable('projects'), sorting function('desc'), reverse='True or False')
        reverse = sort_order == 'desc'
        projects = sorted(projects, key=itemgetter(sort_by), reverse=reverse)

    return projects


def get_techniques(db):
    techs = []
    for i in db:
        for item in i["techniques_used"]:
            if not item in techs:
                techs.append(item)
    techs.sort()
    return techs

def get_technique_stats(db):
    stats = {}
    for project in db:
        for technique in project.get('techniques_used', []):
            if technique not in stats:
                stats[technique] = []
            stats[technique].append({'id': project.get('project_id'), 'name': project.get('project_name')})
    return stats

data = load("projektuppgift/data.json")
print(data)