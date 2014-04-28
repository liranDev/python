from pymongo import MongoClient

port = 27017
ip = 'localhost'

class DBAPI:
    
    def __init__(self, ip = 'localhost', port = 27017):
        self.port = port
        self.ip = ip
        self.connection = None
        self.db = None


    def connect_to_db(self, db_name):

        try:
            print('Connecting to MongoDB...')
            self.connection =  MongoClient(self.ip, self.port)
            print('Setting connection to ' + db_name)
            self.db = self.connection[db_name]

        except Exception as exc:
            print(exc)
            
    def close_connection(self):

        print('Closing connection to mongoDB...')

        self.connection.close()
        
    def insert(self, collection_name, data):

        exec( 'self.db.%s.insert(%s)' % (collection_name, data))
              
    def show_collection(self, collection):

        collection = eval('self.db.%s.find' % (collection_name))

        for entry in collection:
            print(entry)

    def clean_collection(self, collection_name):

        exec('self.db.%s.drop()' % (collection_name))

    def set_unique_collection(self, collection, pk):

        print('Setting collection % s to be unique on pk: %s ...' %(collection, pk))
        exec('self.db.%s.ensureIndex({name:%s},{unique:true})' % (collection, pk))
        
    def create_collection(self, collection):

        print('Creating collection %s...' % collection )
        exec('self.db.createCollection(%s)' % collection)

    def exec_query(self, query):
    
        return self.db.rss.count()








    
    
