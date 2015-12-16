#!/usr/bin/env python3
# encoding: utf-8


import unittest


from lib.reply import TextReply
from lib.oxford import Oxford
from lib.xml_lib import XMLStore


class TestMethods(unittest.TestCase):

    def test_TextReply_render(self):
        msg = {"target": "A", "source": "b"}
        content = "text......."
        tr = TextReply(message=msg, content=content)
        rs = tr.render()
        print(rs)

    @unittest.skip("time consuming operation")
    def test_Oxford_analysis(self):
        #pic_url = "http://mmbiz.qpic.cn/mmbiz/TcgvszBrJ3zv2loeNAqGmWgYbqIVLVOibk6Fn8Cpb8aUG1Q0NoPTCdo4x6DkJAyf0cACJiaUJFibN4tickqxQY1XMQ/0"
        pic_url = "http://how-old.net/Images/faces2/scroll005.jpg"
        oxf = Oxford(pic_url)
        ages = oxf.get_ages()
        print(ages)


    def test_XMLStore_xml2dict(self):
        msg = {"target": "A", "source": "b"}
        content = "text......."
        tr = TextReply(message=msg, content=content)
        rs = tr.render()

        xmls = XMLStore(rs)
        d = xmls.xml2dict
        print(d)


if __name__ == "__main__":
    unittest.main()


