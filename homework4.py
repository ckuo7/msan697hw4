

from flask import Flask, request,jsonify
from pymongo import MongoClient
import pymongo


app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def index():

    # connecting the remote mongodb
    client = MongoClient('mongodb://daniel:daniel@linus.mongohq.com:10024/MSAN_697')
    db = client['MSAN_697']
    test = db['wishlist2']

    if request.method == "GET":

        wishlist = []
        for i in test.find():
            wishlist.append(i)

        if len(wishlist) == 0:
            return "No data in the collections\n"
        else:
            return jsonify(wishlist=wishlist)
    else:
        data = request.get_json(force=True)
        count = 0
        insert = True
        while(insert):
            insert = False
            try:
                test.insert(data)
            except pymongo.errors.DuplicateKeyError, e:
                count += 1
                data['_id'] = str(count)
                insert = True
        return "insert completed\n"


if __name__ == '__main__':
    app.debug = True
    app.run()