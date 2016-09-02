'''
Created on 2016年6月17日

@author: gionee
'''
def extract_from_tag(tag,line):
    opener = "<" + tag +">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer,start)
        return line[start:j]
    except ValueError:
        return None

initline = "<div>今天的天气好晴朗，处处好风光!</div>"
line = extract_from_tag("div", initline)
print("第一种方法：%s" % line)

def extract_from_tag2(tag,line):
    opener = "<" + tag +">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j = line.find(closer,start)
        if(j !=-1):
            return line[start:j]
    return None

line = extract_from_tag2("div", initline)
print("第二种方法：%s" % line)
