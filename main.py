from flask import Flask, jsonify,request
from sql import get_tables

app = Flask(__name__)

@app.route("/" )
def landing_page():
    return "Hello again and Welcome to the Landing Page"


@app.route("/tables",methods=['GET'])
def see_tables():
    tables = get_tables()
    return jsonify(tables)


fruit_list = ["mango","lemon","pineapple","pear","berry"]
@app.route("/fruits",methods=['GET'])
def see_fruits():
    return jsonify({"fruit-list":fruit_list})

@app.route("/fruits/<fruitname>",methods=['POST'])
def add_fruit(fruitname):
    if fruitname not in fruit_list:
        fruit_list.append(fruitname)
        return jsonify({"Fruit added":fruitname,"New fruit list":fruit_list})
    return jsonify({"Error adding fruit":fruitname})


names = ["Wanja","Wanjiku","Mumbi"]
@app.route("/names",methods=['GET'])
def see_names():
    return jsonify(names)

@app.route("/names/<name>",methods=["DELETE"])
def remove_name(name):
    if name in names:
        names.remove(name)
        return jsonify({"name":f'{name} has been removed from list',"OtherNames":names})
    return jsonify({"name":f"{name} not found","List of names":names})

@app.route("/names/<name>",methods=["POST"])
def add_name(name):
    if name not in names:
        names.append(name)
        return jsonify({"name":f"{name} has been added","New list of names":names}),200
    return jsonify({"Error adding name":f"{name} to {names}"}),404


schools_list = ["College","University","HS"]
@app.route("/schools",methods=["GET"])
def see_school():
    # jsonify expects a list, a dictionary or a tuple
    return jsonify(schools_list)

@app.route("/schools/<oldschool>/<newschool>",methods=["PUT"])
def updateschool(oldschool,newschool):
    if oldschool in schools_list:
        index = schools_list.index(oldschool)
        schools_list[index] = newschool
        return jsonify({"School added":newschool,"Schools":schools_list}),200
    return jsonify({"Error":f'School {newschool} already added'}),404



if __name__ == "__main__":
    app.run(port=5000,debug=True)

