from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (name) VALUES (?)", (task_name,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
