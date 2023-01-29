from flask import render_template, request, redirect, url_for
from web3.exceptions import ContractLogicError, TimeExhausted

from app import app
import deploy_smart_contract
import generate_key
from encrypt_decrypt import AESCipher

"  test 1"

network_info = {"HTTP": None, "ID": None, "myAddress": None}

user_info = {'friendList': None, 'friendMsg': None, 'userAddress': None}
# http_provider = "https://goerli.infura.io/v3/0dc1865d3cb84781999f5781077d8ddb"
http_provider = "https://serene-wider-slug.ethereum-goerli.discover.quiknode.pro/e7ea9294e3c8a1396ce7175a378d32aa42d9cb31/"
# http_provider = "https://eth-goerli.g.alchemy.com/v2/B2aodlHQEDk4pHjhcoeLzBz4k6qDTN56"

selected_friend = ''


@app.route('/')
def mainPage():
    return render_template("mainPage.html")


@app.route('/chat_page', methods=["GET", "POST"])
def chat_page():
    friend_list = user.showfriendList(sender_address=user_info['userAddress'])
    alreadyFriends = None
    if request.method == "POST":
        try:
            req = request.form
            address = req['friendAddress']
            name = req['friendName']

            user.addFriend(friendName=name, friendAddress=address, sender_address=user_info['userAddress'])
            friend_list = user.showfriendList(sender_address=user_info['userAddress'])
        except ContractLogicError:
            alreadyFriends = 'you both already friends'
            return render_template("chatPage.html", friend_list=friend_list,
                                   alreadyFriends=alreadyFriends)
        except TimeExhausted:
            time_exhausted = 'time out of 120 sec, please redo it'
            return render_template("chatPage.html", friend_list=friend_list,
                                   alreadyFriends=time_exhausted)
        except:
            error = 'some thing went rong, please retry again '
            return render_template("chatPage.html", friend_list=friend_list,
                                   alreadyFriends=error)

    return render_template("chatPage.html", friend_list=friend_list,
                           alreadyFriends=alreadyFriends)


@app.route('/network', methods=["GET", "POST"])
def network():
    error = None
    if request.method == "POST":
        # try:
            req = request.form
            network_info["myAddress"] = req["publicKey"]
            name = req["username"]
            private_key = req["privateKey"]
            user_info['userAddress'] = network_info["myAddress"]
            global private
            private = private_key
            global user
            user = deploy_smart_contract.SmartContract(HTTP=http_provider, private_key=private_key)

            # global user
            # user = deploy_smart_contract.SmartContract(HTTP=http_provider,
            #                                            ,
            #                                            publicKey=req["publicKey"], name=name)
            if user.checkUserExists(Address=network_info["myAddress"]):
                # user.private_key = private_key
                return redirect(url_for("chat_page"))
            else:
                user.create_account(name=name, sender_address=network_info["myAddress"], private_key=private_key,
                                    x= generate_key.get_x_y(int(private_key, 16))[0],
                                    y=generate_key.get_x_y(int(private_key, 16))[1])
                return redirect(url_for("chat_page"))
        # except:
        #     error = "something went rong ..." \
        #             "reconnect again "
        #
        #     return render_template("network.html", error=error)

    return render_template("network.html", error=error)


@app.route('/message/<string:friend_address>', methods=["GET", "POST"])
def msg(friend_address):
    print('user.get_public_key_points(friend_address)')
    print(user.get_public_key_points(friend_address))
    key = generate_key.generate_key(public_key=user.get_public_key_points(friend_address),
                                    my_private_key=int(private, 16))
    friend_address = friend_address
    selected_friend = friend_address
    if request.method == "POST":
        req = request.form
        try:
            user.sendMessage(receiverAddress=friend_address, msg=AESCipher(
                key=key).encrypt(
                data=req['msg'])
                             , sender_address=user_info['userAddress'])
            # user.sendMessage(receiverAddress=friend_address, msg=req['msg']
            #                  , sender_address=user_info['userAddress'])
        except TimeExhausted:
            return render_template("msg.html", receiver=friend_address,
                                   msgs=upgrade_msgs(friend_address)[1], side=upgrade_msgs(friend_address)[0],
                                   error=f'resend the msg,{TimeExhausted.args}')
        except ValueError:
            return render_template("msg.html", receiver=friend_address,
                                   msgs=upgrade_msgs(friend_address)[1], side=upgrade_msgs(friend_address)[0],
                                   error=f'resend the msg,{ValueError.args}')

        return render_template("msg.html", receiver=friend_address,
                               msgs=upgrade_msgs(friend_address)[1], side=upgrade_msgs(friend_address)[0], error=None)
    return render_template("msg.html", receiver=friend_address,
                           msgs=upgrade_msgs(friend_address)[1], side=upgrade_msgs(friend_address)[0], error=None)


def upgrade_msgs(friend_address):
    msgs_encrypted = user.readMessages(friend_address, sender_address=user_info['userAddress'])
    key = generate_key.generate_key(user.get_public_key_points(friend_address),
                                    my_private_key=int(private, 16))
    msgs_decrypt = {}
    print("messages is ")
    print(msgs_encrypted)
    try:
        # for x in range(len(msgs_encrypted)):
        #     msgs_decrypt[x] = AESCipher(
        #         key=key).decrypt(
        #         data=msgs_encrypted[x][2])
        for x in range(len(msgs_encrypted)):
            msgs_decrypt[x] = msgs_encrypted[x][2]
    except Exception as e:
        redirect(url_for("msg", friend_address=selected_friend))
    return msgs_encrypted, msgs_decrypt
