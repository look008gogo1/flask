from flask import Flask
from views import views,student



app=Flask(__name__)
app.register_blueprint(views,url_prefix='/views', name='views_v1')
app.register_blueprint(student,url_prefix='/student', name='student_v1')


    
if __name__=='__main__':

    app.run(debug=True)