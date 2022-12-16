from psycopg2.extensions import cursor

# valid tables to query from in the needed functions
TABLE_NAME_PARAMS = set(["animals", "exotic", "food", "kittens", "land", "pets", "puppies", "sea"])

def update_choice_count(cur:cursor, table_name:str, requested_page_id:int):
    # prevent SQL injections
    assert int(requested_page_id) >= 0
    assert table_name in TABLE_NAME_PARAMS
    
    cur.execute(f"""
    update {table_name}
    set {table_name}countleft = 
        (select {table_name}countleft
        from {table_name} 
        where {table_name}.{table_name}id = {requested_page_id}) + 1
    where {table_name}.{table_name}id = {requested_page_id}
    """)

def select_page_data(cur:cursor, table_name:str, requested_page_id:int):
    # prevent SQL injections
    assert int(requested_page_id) >= 0
    assert table_name in TABLE_NAME_PARAMS

    # grab a row of data from a table so the html can reference the row data when called through app.py
    cur.execute("""
    select *
    from {table_name} 
    where {table_name}id = {requested_page_id}
    """)