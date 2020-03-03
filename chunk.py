import pandas as pd

chunk_size = 200000
batch_no = 1

for chunk in pd.read_csv('APC.csv', chunksize = chunk_size):
	chunk.to_csv('APC' + str(batch_no) + '.csv', index = False)
	batch_no += 1