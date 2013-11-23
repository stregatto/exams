#from sqlalchemy import *
import sqlalchemy

class sqlCommands():

    def do_sqlmoduleversion(self,line):
        """
        Print sqlalchemy version
        """
        print sqlalchemy.__version__
        return

    def do_courseslist(self,line):
        """
         couseslist: give the list of all courses
        """
        result = engine.execute("select course from courses;") 
        for row in result:
            print " -> ", row['course']
        result.close()
        return
        
    def do_whichsqlconnection(self,line):
        """"
         whichsqlconnection: give the connection string
        """
        print "Sql Connection -> ", dbstring

    def do_questionlist(self,line):
        """
         questionlist: give the entire(!) question list
        """
        result = engine.execute("select questions_id, description from questions;")
        for row in result:
            print " -> id %s ) %s" %(row['questions_id'], row['description'])
        result.close
        return

    def do_showqestionanswers(self,line):
        """
         showquestionanswers <ID>: give all the answers for a specific question ID
                                 The answer with * is marked as "correct"                           
                                 To know which ID, use questionlist command 
        """
        if not line:
            print " plese give me one ID: showquestionanswers <ID>"
        else:
            query = "SELECT description FROM questions WHERE questions_id='%s';" % line
            qresult = engine.execute(query) 
            query = "SELECT result, correct FROM qAnswers WHERE questions_questions_id='%s';" % line
            aresult = engine.execute(query)
            for row in qresult:
                print " -> %s" % row['description']       
            for row in aresult:
                if row['correct'] == 1:
                   print "    * %s" % row['result'] 
                else:
                   print "      %s" % row['result']
        #qresult.close
        #aresult.close
        return

with open('./db.config', 'r') as content_file:
        dbstring= content_file.read()

engine = sqlalchemy.create_engine(dbstring, pool_recycle=3600)
connection = engine.connect()


#result = engine.execute("select name from mytable")
#for row in result:
#    print "name:", row['name']
#    result.close()


#import sqlalchemy
#engine = sqlalchemy.create_engine('mysql://user:password@server') # connect to server
#engine.execute("CREATE DATABASE dbname") #create db
#engine.execute("USE dbname") # select new db
