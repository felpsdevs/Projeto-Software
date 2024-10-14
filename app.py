from flask import Flask, render_template, request, redirect
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname='postgres_db',  
        user='postgres',       
        password='970202',     
        host='localhost',          
        port='5432'           
    )
    return conn

app = Flask(__name__)  

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name, completed FROM tasks') 
    tasks = cur.fetchall()  
    cur.close()
    conn.close()

    tasks_list = [{'id': task[0], 'name': task[1], 'completed': task[2]} for task in tasks] 
    return render_template('index.html', tasks=tasks_list)


@app.route('/add', methods=('POST',))
def add():
    task = request.form['task']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (name, completed) VALUES (%s, FALSE)', (task,)) 
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=('POST',))
def delete(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')


@app.route('/concluir/<int:task_id>', methods=['POST'])
def concluir_tarefa(task_id):
    conn = get_db_connection() 
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET completed = TRUE WHERE id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)