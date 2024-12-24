import xml.dom.minidom
def main():
    path=r"C:\BAI TAP\CHUONG2\3.xml"
    doc=xml.dom.minidom.parse(path)
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__=="__main__":
    main()