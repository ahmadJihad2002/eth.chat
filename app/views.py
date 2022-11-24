from flask import render_template, request, redirect
from app import app
import deploy_smart_contract


@app.route('/mainPage')
def mainPage():
    # chat=deploy_smart_contract.SmartContract( )

    return render_template("mainPage.html")


@app.route('/chatPage', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        req = request.form
        return redirect(request.url)
    return render_template("chatPage.html")


@app.route('/network', methods=["GET", "POST"])
def network():
    if request.method == "POST":
        req = request.form
        req["ID"]
        req["network_name"]
        req["HTTP"]
        req["privateKey"]
        req["publicKey"]
        req["username"]

        deploy_smart_contract.SmartContract(HTTP=req["HTTP"], chainId=req["ID"], privateKey=req["privateKey"],
                                            publicKey=req["publicKey"], username=req["username"])

    return render_template("network.html")
