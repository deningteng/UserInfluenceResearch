import pandas as pd
loop = True
chunkSize = 10000
chunks = []
index=0
reader=pd.read_csv('H:\\SMPData\\Weibo.Corpus\\Weibo.data\\merge\\weibodata.csv',iterator = True)
while loop:
  try:
    chunk = reader.get_chunk(chunkSize)
    chunks.append(chunk)
    index=index+1
    print "Iteration %d"%(index)
    if index>2499 :
      loop = False
  except StopIteration:
    loop = False
    print "Iteration is stopped."
df = pd.concat(chunks, ignore_index=True)
df.columns=['id','reports','comments','source','time','text']
# print df['text'][0:10]
group=df['text'].groupby(df['id']).count()
# print group.size()
group.to_csv('message_count.csv',encoding='utf-8')