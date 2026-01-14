## 安装
```
pip install pycvc
```
以及以下依赖仓库：  
```
https://github.com/librekeys/pypicokey-mirror
https://github.com/librekeys/pypicohsm
```

## 设置证书颁发机构（CA）：
```
openssl ecparam -out ESPICOHSMCA00001.pem -name prime256v1 -genkey
openssl pkcs8 -topk8 -nocrypt -in ESPICOHSMCA00001.pem -outform DER -out ESPICOHSMCA00001.pkcs8
cvc-create --role=cvca --type=at --chr=ESPICOHSMCA00001 --days=3650 --sign-key=ESPICOHSMCA00001.pkcs8 --scheme=ECDSA_SHA_256
```

## 设置验证机构（DV）：
```
openssl ecparam -out ESPICOHSMDV00001.pem -name prime256v1 -genkey
openssl pkcs8 -topk8 -nocrypt -in ESPICOHSMDV00001.pem -outform DER -out ESPICOHSMDV00001.pkcs8
openssl ec -in ESPICOHSMDV00001.pem -out ESPICOHSMDV00001.pub -pubout -outform DER
cvc-create --role=dv_domestic --type=at --chr=ESPICOHSMDV00001 --days=1820 --sign-key=ESPICOHSMCA00001.pkcs8 --scheme=ECDSA_SHA_256 --sign-as=ESPICOHSMCA00001.cvcert --public-key=ESPICOHSMDV00001.pub
```

## 修改 `picohsm/PicoHSM.py`

参考链接：https://github.com/librekeys/pypicohsm/blob/412aa07898a355beaec7f1b5da3895f8e85f5a09/picohsm/PicoHSM.py#L197

将其修改为：
```
            #j = get_pki_data('cvc', data=data)
            input_json = input("请输入 JSON 字符串：")
            j = json.loads(input_json)
```
并且把上面的
```
            #print(f'Public Point: {hexlify(Y).decode()}')
```
取消注释

## 运行 pico-hsm-tool.py
工具地址：https://github.com/librekeys/pico-hsm/blob/master/tools/pico-hsm-tool.py

```
python pico-hsm-tool.py --pin 114514 initialize --so-pin 57621880
```

脚本会暂停并等待输入 `请输入 JSON 字符串：`  
复制 `Public Point:` 后面的字符串内容。  
**请保持此窗口打开，不要关闭。**

## 运行 convertder.py
```
python convertder.py
```
将刚才复制的 `Public Point:` 后的字符串粘贴进来，按回车确认。

## 创建终端证书
```
cvc-create --role=terminal --type=at --chr=ESPICOHSMTR00002 --days=365 --sign-key=ESPICOHSMDV00001.pkcs8 --scheme=ECDSA_SHA_256 --sign-as=ESPICOHSMDV00001.cvcert --public-key=public_key.pub
```

## 运行 convertcvc.py
```
python convertcvc.py
```
打开一个记事本，复制所有输出的内容。

## 上传证书
将 `Json:` 后面的内容粘贴回 `pico-hsm-tool.py` 窗口。  
脚本应打印 `Certificate uploaded successfully!` 表示证书上传成功。

## 修改 SCS3 工具配置

参考文档：https://github.com/librekeys/pico-hsm/blob/master/doc/scs3.md  
但不要使用原来的格式：
```
ESPICOHSMCA00001: new CVC(new ByteString("***", HEX)),
ESPICOHSMCA00002: new CVC(new ByteString("***", HEX))
```
而是将 `SCS3:` 后面的字符串复制到 `***` 处，格式如下：
```
ESPICOHSMCA00001: new CVC(new ByteString("***", HEX))
```

现在即可使用 SCS3 管理 PicoHSM 设备：

![SCS3](SCS3.png)

---

### 补充说明
1. **环境要求**：建议在 Python 3.7+ 环境下运行，并确保已安装 `openssl` 命令行工具。
2. **文件路径**：以上命令默认在当前目录执行，请根据实际位置调整文件路径。
3. **密钥安全**：生成的 `.pem`、`.pkcs8` 等私钥文件请妥善保管，避免泄露。
4. **常见问题**：若遇到 JSON 解析错误，请检查粘贴内容是否完整，避免多余空格或换行。
