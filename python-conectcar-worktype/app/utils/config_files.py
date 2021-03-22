from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
class ConfigFiles:
    def Token():  
        return config['conect_token']['_token']
        
    def SecretKey():  
        return config['conect_token']['_secret_key']

    def Conn(): 
        host =  config['conect_conn']['_host']
        port =  config['conect_conn']['_port']
        user =  config['conect_conn']['_user']
        password =  config['conect_conn']['_password']
        db_name =  config['conect_conn']['_db_name'] 

        connection = "mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, db_name)
        return connection

    def setUerId(self, userId):  
        globals()['userId'] = userId
    
    def getUserId():  
        return globals()['userId']