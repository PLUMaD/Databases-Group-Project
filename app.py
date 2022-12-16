import psycopg2
from flask import Flask, render_template, request
from psycopg2.extras import RealDictCursor
from utils import safe_int
from sets import count_sets, search_sets, select_page_data, update_choice_count

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)

# TODO: create /sets HTML endpoint
#The tutorial for the game and the programming we did
@app.route('/test/info')
def instructions():
    return render_template('info_page.html')

#The page with the buttons and choices
@app.route('/test/question')
def would_you_rather():
    #The table we will query for the page data
    #The page data includes the button options, the verb for the question, and the options' counts
    table_name = request.args.get('table_name', 'animals')
    #The html page with a question should ask for a question ID to Display from a given table
    row_id = request.args.get('id', 0)
    with conn.cursor() as cur:
        #Calls set.py for the select sql to grab table data
        select = select_page_data(cur, table_name = table_name, requested_page_id = row_id)
        #Calls set.py for the update_choice_count function
        update = update_choice_count(cur, table_name = table_name)
        #Renders html using given data
        return render_template('questions_page.html', table_name = table_name, update = update, select = select)

#The page with the percentage results from the question
@app.route('/test/results')
def results():
    #We may need additional query requests for the last page's question and the chosen answer to be saved
    #If so, remember to put those in the section below this, like so
    #return(render_template('q', table_name = table_name, select = select, QUERY_NAME=PUT HERE))

    #The table we will query for the page data
    table_name = request.args.get('table_name', 'animals')
    #The page data id to get a specific row from the table above
    row_id = request.args.get('id', 0)
    #The html page with a question should ask for a question ID to Display from a given table
    with conn.cursor() as cur:
        #Calls set.py for the select sql to grab table data
        select = select_page_data(cur, table_name = table_name, requested_page_id = row_id)
        #Renders html using given data
        return render_template('q', table_name = table_name, select = select)





# import psycopg2
# from flask import Flask, render_template, request
# from psycopg2.extras import RealDictCursor
# from util import safe_int, safe_sort_by, safe_sort_dir
# from sets import count_sets, search_sets

# from choices import nameOfChoices

# conn = psycopg2.connect(
#     "host=db dbname=postgres user=postgres password=postgres",
#     cursor_factory=RealDictCursor)
# app = Flask(__name__)

# # TODO: create /sets HTML endpoint
# @app.route('/sets')
# def search_sets_html():
#     print(request.args)
#     nameOfChoices = request.args.get('nameOfChoices', '')
#     choiceData = request.args.get('s.choiceData', '')
#     selectedNumTimes = request.args.get('selectedNumTimes', '')
#     page = safe_int(request.args.get('page'), 1)
#     limit = safe_int(request.args.get('results_per_page'),50)
#     offset =  (page -1) * limit
#     safe_sort_by = safe_sort_by(request.args.get('safe_sort_by'), 'set_name')
#     safe_sort_dir  = safe_sort_dir(request.args.get('safe_sort_dir'), 'asc')
#     page_count = safe_int(request.args.get('page_count', 1))
#     if page_count is None:
#         page_count = 1            

#     with conn.cursor() as cur:
#         count = count_sets(cur, nameOfChoices = nameOfChoices, choiceData = choiceData, selectedNumTimes = selectedNumTimes,
#                 page = page, limit = limit, offset = offset, safe_sort_by = 'set_name', safe_sort_dir = 'asc')
#         results = search_sets(cur, nameOfChoices = nameOfChoices, choiceData = choiceData, selectedNumTimes = selectedNumTimes,
#                 page = page, limit = limit, offset = offset, safe_sort_by = 'set_name', safe_sort_dir = 'asc')
#         return render_template('choice_display.html', nameOfChoices = nameOfChoices, choiceData = choiceData, selectedNumTimes = selectedNumTimes,
#                 page = page, offset = offset)

# def update_id(cur.cursor, nameOfChoices:str, choiceData:str,
#                 selectedNumTimes:int, id:int
#     cur.execute(f"""
#         update choiceData
#         set id = id
#         where id = null
#     """)
# )

# def update_table(cur.cursor, table:str, nameOfChoices:str, 
#                 choiceData:str,selectedNumTimes:int,id:int
#     cur.execute("""
#         update table
#         set column=nameOfChoices
#         where column=null
#     """)
# )


