import subprocess

def juman(text):
    P = subprocess.Popen(["juman"],
        stdin = subprocess.PIPE,
        stdout =subprocess.PIPE
    )
    P.stdin.write(text)
    P.stdin.close()
    result = P.stdout.read()
    result = result.decode("utf-8")
    return result

result =[]
noun=[]
text=[]
for line in open("test.txt","rb"):
    r =juman(line)
    r=r.strip()
    result.append(r)
#print(result)

for detail in result:
    Res= detail.split("\n")
    noun.append(Res)
#print(noun)

for item in noun:
    for i in item:
        #print(i)
        i=i.split(" ",11)
        #print(i)
        if i[0]=="EOS":
            break
        if i[3]=="名詞":
            text.append(i[2])

import collections
i=0
Count = collections.Counter(text)
for word,freq in Count.most_common():
    print(str(word)+":"+str(freq)+"\n")
    i+=1
    if i ==50:
        break
