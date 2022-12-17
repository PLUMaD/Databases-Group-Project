import psycopg2
from flask import Flask, render_template, request
from psycopg2.extras import RealDictCursor

from sets import select_page_data, update_choice_count, TABLE_NAME_PARAMS
from util import safe_int, within_valid_values

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
    table_name_temp = request.args.get('table_name', 'animals')
    table_name = within_valid_values(table_name_temp, TABLE_NAME_PARAMS, 'animals')
    #The html page with a question should ask for a question ID to Display from a given table
    row_id = request.args.get('id', 0)
    with conn.cursor() as cur:
        #Calls set.py for the select sql to grab table data
        select = select_page_data(cur, table_name = table_name, requested_page_id = row_id)
        #Calls set.py for the update_choice_count function
        option_dir = request.args.get('option_dir', 'left')
        update = update_choice_count(cur, table_name = table_name, left_right=option_dir)
        #Renders html using given data
        return render_template('questions_page.html', table_name = table_name, row_id = row_id, update = update, select = select)

#The page with the percentage results from the question
@app.route('/test/results')
def results():
    #We may need additional query requests for the last page's question and the chosen answer to be saved
    #If so, remember to put those in the section below this, like so
    #return(render_template('q', table_name = table_name, select = select, QUERY_NAME=PUT HERE))

    #The table we will query for the page data
    table_name_temp = request.args.get('table_name', 'animals')
    table_name = within_valid_values(table_name_temp, TABLE_NAME_PARAMS, 'animals')
    #The page data id to get a specific row from the table above
    row_id = request.args.get('id', 0)
    #The html page with a question should ask for a question ID to Display from a given table
    with conn.cursor() as cur:
        #Calls set.py for the select sql to grab table data
        select = select_page_data(cur, table_name = table_name, requested_page_id = row_id)
        #Renders html using given data
        return render_template('', table_name = table_name, select = select)