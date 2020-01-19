from KCM.__main__ import KCM
import json, sys, requests, os, pyprind
def hybrid(ratioX, ratioY):
    hybridResult = {}
    for index, (i, j) in enumerate(zip(tmp, distance)):
        if i[0] == j[0]:
            hybridResult[i[0]] = hybridResult.setdefault(i[0], 0) + index
        else:
            hybridResult[i[0]] = hybridResult.setdefault(i[0], 0) + index * ratioX / (ratioX + ratioY)
            hybridResult[j[0]] = hybridResult.setdefault(j[0], 0) + index * ratioY / (ratioX + ratioY)
    return hybridResult

k = KCM('cht', './ptt', uri='mongodb://172.17.0.8:27017')
# k.removeDB()
# k.main()
name2add = json.load(open('台灣所有景點的地址.json', 'r'))

query = sys.argv[1]
print('以Correlation排序:\n')
tmp = [i for i in k.get(query, 10000) if i[0] in name2add and len(i[0]) > 2 ][:int(sys.argv[2])]
print(tmp[:int(sys.argv[3])])


print('\n以距離排序:\n')
distance = []
for i in pyprind.prog_bar(tmp):
    try:
        if os.path.isfile('json/query-' + i[0]+'.json'):
            res = json.load(open('json/query-' + i[0]+'.json','r'))
        else:
            res = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key=AIzaSyB20qKjF1ePtq9t1luvFd-433J41anlDGU'.format(name2add[query], name2add[i[0]])).json()
            json.dump(res, open('json/query-' + i[0]+'.json','w'))
        if res['rows'][0]['elements'][0]['status'] == 'OK':
            distance.append((i[0], res['rows'][0]['elements'][0]['distance']['value']))
    except Exception as e:
        pass
distance = sorted(distance, key=lambda x:x[1])[:int(sys.argv[3])]
print(distance)


print('\nHybrid方法排序,距離 : correlation = 2 : 8\n')
result = hybrid(2, 8)
result = sorted(result.items(), key=lambda x:-x[1])[:int(sys.argv[3])]
print(result)

print('\n印出類別：\n')
header = json.load(open('交通局class.json', 'r'))
print([(i[0], header.get(i[0], '未知')) for i in result])