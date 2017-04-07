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
group=df['reports'].groupby(df['id']).sum()
# print group.size()
group.to_csv('reports.csv',encoding='utf-8')

# for j in group:
  # print i
  # print('-------')

  # print j
  # file_name="F:\\Git Repository\\comments.txt"
  # with open(file_name,"w") as f:
  #   for x in text:
  #     f.write(str(x))

# phase=[]
# for i in range(0,11):
#   phase.append(df['text'][i])
# a=' '
# phase=a.join(phase)
# print phase
#
# pynlpir.open()
# result=pynlpir.segment(phase,pos_tagging=False)
# pynlpir.close()
# print result