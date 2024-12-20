from datetime import datetime
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# this is to create connection with database
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['DEBUG']=True
db=SQLAlchemy(app)

# this is to create tables in database but this will be the model only.
class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} {self.title}"

# this will create the all table of database
with app.app_context():
    db.create_all()

@app.route("/",methods=['POST','GET'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    MyTodo=Todo.query.all()
    return render_template("index.html",MyTodo=MyTodo)

@app.route('/update/<int:sno>',methods=['POST','GET'])
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo=Todo.query.filter_by(sno=sno).first()
    return render_template("update.html",todo=todo)


@app.route("/delete/<int:sno>")
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=8000)