
import pymysql.cursors

class DB(object):
    def __init__(self):
        #aquest host es el localhost de l'equip on tenim el docker
        self.host = "host.docker.internal"
        self.port= 3306
        self.user= 'root'
        self.password=''
        self.database='vols'
        self.dbconfigurada=False

    def configuraDB(self,dbconfig):
        self.host = dbconfig.host
        self.port= dbconfig.port
        self.user= dbconfig.user
        self.password=dbconfig.password
        self.database=dbconfig.database
        self.dbconfigurada=True

    def conecta(self):
        #Conexion a la BBDD del servidor mySQL
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                     user=self.user,
                                     password=self.password,
                                     db=self.database,
                                     charset='utf8mb4',
                                     autocommit=True,
                                     cursorclass=pymysql.cursors.DictCursor)
        self.cursor=self.db.cursor()

    def desconecta(self):
        self.db.close()

    def cargaAeroports(self):
        self.conecta()
        sql="SELECT * from aeroports"
        self.cursor.execute(sql)
        ResQuery=self.cursor.fetchall()
        return ResQuery

