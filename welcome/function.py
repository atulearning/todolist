import random
import time,os
from cryptography.fernet import Fernet as fer

def get_random_string(length):
    """
    生成指定长度的随机字符串
    大概生成长度为8-12
    """
    random.seed(time.time())
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

key =fer.generate_key()
def jiami(data,key):
    d = str(data).encode('utf-8')
    f = fer(key) # 生成密钥
    d = f.encrypt(d) # 加密
    d = d.decode() # 转成字符串
    return d
def jiemi(data,key):
    d = str(data).encode('utf-8')
    f = fer(key) # 生成密钥
    d = f.decrypt(d) # 解密
    d = d.decode() # 转成字符串
    return d


if __name__ == '__main__':
    data = '123456' # 要加密的数据
    jiami_data = jiami(data,key) # 加密
    print(f'加密后数据:{jiami}, key:{key}')
    jiemi_data = jiemi(jiami_data,key) # 解密
    print(f'解密后数据:{jiemi_data},原始数据{data}')