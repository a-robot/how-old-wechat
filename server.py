#!/usr/bin/env python3


from flask import Flask
from flask import request, make_response, redirect


from lib.reply import TextReply
from lib.oxford import Oxford
from lib.xml_lib import XMLStore

app = Flask(__name__)


token = "123"
encoding_aes_key = "Ag4FdRP5prwhXjtJspoosrx1OIEBTJVK258WDYLpOlX"
corpid = "wx921fda8f1eb818b9"

SOURCE_ID = "gh_537c9c75646f"
DEBUG = True


@app.route("/", methods=["GET", "POST"])
def index():
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    if request.method == "GET":
        print(echostr)
        return echostr

    elif request.method == "POST":
        body_text = request.data

        xml_store = XMLStore(body_text)
        recv_data = xml_store.xml2dict

        if False:
            print("<<<<<<<<<< recv <<<<<<<<<<<<<<")
            print(recv_data)
            print("<<<<<<<<<< recv <<<<<<<<<<<<<<")

        target = recv_data.get("FromUserName", "")

        if recv_data.get("MsgType") == "image":
            msg = {"target": target, "source": SOURCE_ID}

            pic_url = recv_data.get("PicUrl", "")
            oxf = Oxford(pic_url)
            ages = oxf.get_ages()
            content = ages
            tr = TextReply(message=msg, content=content)
            rs = tr.render()


        else:
            msg = {"target": target, "source": SOURCE_ID}
            content = "Sorry, your input is not suported."
            tr = TextReply(message=msg, content=content)
            rs = tr.render()

        if DEBUG:
            print(">>>>>>>>>>> send >>>>>>>>>>>>>")
            print(rs)
            print(">>>>>>>>>>> send >>>>>>>>>>>>>")

        return make_response(rs)


@app.route('/hello')
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=DEBUG)
