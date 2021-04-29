import subprocess
import itertools

def mecab(text):
    P = subprocess.Popen(["mecab","-d","/usr/local/lib/mecab/dic/mecab-ipadic-neologd"],
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
    r =mecab(line)
    r=r.strip()
    result.append(r)

for detail in result:
    detail=detail.replace("\t",",")
    detail=detail.replace(","," ")
    Res= detail.split("\n")
    noun.append(Res)

for item in noun:
    for i in item:
        #print(i)
        i=i.split(" ",10)
        #print(i)
        if i[0]=="EOS":
            break
        if i[1] == "名詞":
            print(i)  

            text.append(i[0])
print(text)

#回数制限あり
import collections

Count = collections.Counter(text)
print(len(Count))
i=0

for word,freq in Count.most_common():
    print(str(word)+":"+str(freq)+"\n")
    i+=1
    if i==50:
        break
    
with open("test_re.txt","a") as f:
	f.write("単語,"+"出現回数,"+"TF値"+"\n")

with open("test_re.txt","a") as f:
	for word,freq in Count.most_common():
		f.write(str(word)+","+str(freq/len(Count))+"\n")

