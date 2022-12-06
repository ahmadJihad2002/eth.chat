from flask import render_template, request, redirect, url_for
from app import app
import deploy_smart_contract

network_info = {"HTTP": None, "ID": None, "myAddress": None}

user_info = {'friendList': None, 'friendMsg': None}


@app.route('/')
def mainPage():
    return render_template("mainPage.html")


@app.route('/chat_page', methods=["GET", "POST"])
def chat_page():
    friend_list = None
    if request.method == "POST":
        req = request.form
        address = req['friendAddress']
        name = req['friendName']
        user.addFriend(friendName=name, friendAddress=address)
        friend_list = user.showfriendList()
        print("friend been added")
    return render_template("chatPage.html", friend_list=friend_list,
                           is_connected=network_info["HTTP"])


@app.route('/network', methods=["GET", "POST"])
def network():
    if request.method == "POST":
        req = request.form
        network_info["HTTP"] = req["HTTP"]
        network_info["ID"] = req["ID"]
        network_info["myAddress"] = req["publicKey"]
        global user
        user = deploy_smart_contract.SmartContract(HTTP=req["HTTP"], chainId=int(req["ID"]),
                                                   privateKey=req["privateKey"],
                                                   publicKey=req["publicKey"], name=req["username"])
        if user.checkUserExists(Address=network_info["myAddress"]):
            return redirect(url_for("chat_page"))

    return render_template("network.html", network_info=network_info)


@app.route('/message/<string:friend_address>', methods=["GET", "POST"])
def msg(friend_address):
    friend_address = friend_address
    if request.method == "POST":
        req = request.form
        user.sendMessage(receiverAddress=friend_address, msg=req['msg'])
    return render_template("msg.html", receiver=friend_address,
                           msgs=user.readMessages(friend_address))

#
# def chick_if_connected():
#     pass

# @app.errorhandler(404)
# def error():
#     return render_template("errors/logInErrors.html")
