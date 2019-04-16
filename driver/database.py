import pymongo,datetime


#
def get_total_miner_config(username,mongo_user,mongo_pass,mongo_url):
    try:
        myclient = pymongo.MongoClient("mongodb://" + mongo_user + ":" + mongo_pass + "@" + mongo_url)
        mydb = myclient["monitoring"]
        mycol = mydb["configurations"]
        return mycol.find({"username" : username})
    except:
        print("something happend in total config")


def get_miner_config(username,zone_id,mongo_user,mongo_pass,mongo_url):
    try:
        myclient = pymongo.MongoClient("mongodb://"+mongo_user+":"+mongo_pass+"@"+mongo_url)
        mydb = myclient["monitoring"]
        mycol = mydb['configurations']
        out = []
        for item in mycol.find({"username" : username}):
            for id in item['zones']:
                #if id['id'] == zone_id:
                #print(id['id']+'ded')
                for miner in id['miner_list']:
                    out.append(miner)
        return(out)
    except:
        print('There is some Error in collecting data from mongo configuration')
        return []
def add_miner_config(old_data,new_data,id,mongo_user,mongo_pass,mongo_url):
    try:
        myclient = pymongo.MongoClient("mongodb://" + mongo_user + ":" + mongo_pass + "@" + mongo_url)
        mydb = myclient["monitoring"]
        mycol = mydb["configurations"]
        old = old_data
        query = { "$set": {'zones.0.miner_list.'+str(id):new_data}}
        mycol.update(old, query)
        return True
    except:
        print('can not add new value')
        return False

def mongo_test():
    try:
        #if db.authenticate(username, password):


        return True
    except:
        print("Please check your connection")
        return True



def get_last_hour(mongo_user,mongo_pass,mongo_url):
    try:
        myclient = pymongo.MongoClient("mongodb://"+mongo_user+":"+mongo_pass+"@"+mongo_url)
        mydb = myclient["monitoring"]
        mycol = mydb["vahid"]
        out = []
        for item in mycol.find({"timestamp" : {'$gt':datetime.datetime.now().timestamp()}}):
            out.append({'hash': item['log']['summary']['ghsav'],"miner":item['miner_id'],"time":item['timestamp'],'temp':item['log']['devs'][0]['temp']})
        return out
    except:

       print('test')
       return []
## 'temp':item['log']['devs'][0]['temp'],