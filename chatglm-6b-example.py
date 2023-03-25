#!/bin/python3
# -*- coding: utf-8 -*-

from transformers import AutoTokenizer, AutoModel

#__model_name__ = 'THUDM/chatglm-6b'
__model_name__ = 'THUDM/chatglm-6b-int4-qe'

tokenizer = AutoTokenizer.from_pretrained(
	__model_name__,
	trust_remote_code=True,
	cache_dir='./.cache',
	resume_download=True
)
model = AutoModel.from_pretrained(
	__model_name__,
	trust_remote_code=True,
	cache_dir='./.cache',
	resume_download=True,
#	torch_dtype=torch.float16,
	low_cpu_mem_usage=True
).half().cuda()
model = model.eval()

#response, history = model.chat(tokenizer, "你好", history=[])
#print(response)
#response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
#print(response)

history=[]
while True:
	request = input('User: ')
	response, history = model.chat(tokenizer, request, history=history)
	print('ChatGLM-6B: ' + response)
