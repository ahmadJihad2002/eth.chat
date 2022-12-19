from flask import render_template, request, redirect, url_for
from app import app
import deploy_smart_contract

network_info = {"HTTP": None, "ID": None, "myAddress": None}

user_info = {'friendList': None, 'friendMsg': None, 'userAddress': None}
http_provider = "https://goerli.infura.io/v3/0dc1865d3cb84781999f5781077d8ddb"
is_connected = False


@app.route('/')
def mainPage():
    global user
    user = deploy_smart_contract.SmartContract(HTTP=http_provider)
    return render_template("mainPage.html")


@app.route('/chat_page', methods=["GET", "POST"])
def chat_page():
    friend_list = user.showfriendList(sender_address=user_info['userAddress'])
    if request.method == "POST":
        req = request.form
        address = req['friendAddress']
        name = req['friendName']
        user.addFriend(friendName=name, friendAddress=address, sender_address=user_info['userAddress'])
        friend_list = user.showfriendList(sender_address=user_info['userAddress'])
    return render_template("chatPage.html", friend_list=friend_list,
                           is_connected=user.is_connected)


@app.route('/network', methods=["GET", "POST"])
def network():
    if request.method == "POST":
        req = request.form
        network_info["myAddress"] = req["publicKey"]
        name = req["username"]
        user_info['userAddress'] = network_info["myAddress"]
        private_key = req["privateKey"]
        # global user
        # user = deploy_smart_contract.SmartContract(HTTP=http_provider,
        #                                            ,
        #                                            publicKey=req["publicKey"], name=name)
        if user.checkUserExists(Address=network_info["myAddress"]):
            user.private_key = private_key
            return redirect(url_for("chat_page"))
        else:
            user.create_account(name=name, sender_address=network_info["myAddress"], private_key=private_key)
            return redirect(url_for("chat_page"))

    return render_template("network.html", network_info=network_info, is_connected=user.is_connected)


@app.route('/message/<string:friend_address>', methods=["GET", "POST"])
def msg(friend_address):
    friend_address = friend_address
    if request.method == "POST":
        req = request.form
        user.sendMessage(receiverAddress=friend_address, msg=req['msg'], sender_address=user_info['userAddress'])
    return render_template("msg.html", receiver=friend_address,
                           msgs=user.readMessages(friend_address, sender_address=user_info['userAddress']))

#
# def chick_if_connected():
#     pass

# @app.errorhandler(404)
# def error():
#     return render_template("errors/logInErrors.html")
