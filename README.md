# ChatAPI Server Module: ChatGLM-6B

The `ChatAPI` server module for providing API service and running instance of [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B).

# Source

Files:
```
chatapi-chatglm-6b.py
```

## chatapi-chatglm-6b.py

### Requirements

```bash
python -m pip install -r requirements.txt
```

See details at `requirements.txt`.

### First Running

In the first running, the program will download the `ChatGLM-6B` model from the Internet (about ??? GB). The model will be cached under `./.cache/`.

### Quick Start

And running with:
```bash
python3 chatapi-chatglm-6b.py
```

When you see:
```bash
[Info <time>]: Loaded.
[Info <time>]: Running...
```
That represents the prepare work has been done.

Now, you can send a request by save a file into the `requests` folder (will be craete at python work dictory):
```bash
echo '' > requests/1.history #Filename must ends with ".history".
echo '我喜欢吃橘子，你呢？' > requests/1.request #Filename must ends with ".request".
```
After the program finished work, the request and history file will be delete and a new file with extname ".back" which including the result of your request will be create:
```bash
cat requests/1.back
```

### Exit Program

You can send `Ctrl+C` key as normal.

Or you can create a file named `quit.flag` into `flags` folder:
```bash
touch flags/quit.flag
```
If the program detects the flag file (**the detect work is after generate text**), the program will quit.

### Get Status Info

Or you can create a file named `status.flag` into `flags` folder:
```bash
touch flags/status.flag
```
And you will get the status info:
```bash
cat flags/status.back
```

**In fact, the `Status` value will always be `running` (** because the detect work is after generate text**).**

# Reference

```
@inproceedings{
  zeng2023glm-130b,
  title={{GLM}-130B: An Open Bilingual Pre-trained Model},
  author={Aohan Zeng and Xiao Liu and Zhengxiao Du and Zihan Wang and Hanyu Lai and Ming Ding and Zhuoyi Yang and Yifan Xu and Wendi Zheng and Xiao Xia and Weng Lam Tam and Zixuan Ma and Yufei Xue and Jidong Zhai and Wenguang Chen and Zhiyuan Liu and Peng Zhang and Yuxiao Dong and Jie Tang},
  booktitle={The Eleventh International Conference on Learning Representations (ICLR)},
  year={2023},
  url={https://openreview.net/forum?id=-Aw0rrrPUF}
}
@inproceedings{
  du2022glm,
  title={GLM: General Language Model Pretraining with Autoregressive Blank Infilling},
  author={Du, Zhengxiao and Qian, Yujie and Liu, Xiao and Ding, Ming and Qiu, Jiezhong and Yang, Zhilin and Tang, Jie},
  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={320--335},
  year={2022}
}
```

---

View this repository on [GitHub](https://github.com/Orange23333/chatapi-server-module-chatglm6b)
