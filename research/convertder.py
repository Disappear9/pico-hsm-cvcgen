import base64
import binascii
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def convert_y_to_der(y_bytearray):
    """
    将Y字节数组转换为DER格式的SubjectPublicKeyInfo
    """
    # 确保是字节格式
    if isinstance(y_bytearray, bytearray):
        y_bytes = bytes(y_bytearray)
    else:
        y_bytes = y_bytearray
    
    # 验证格式和长度
    if len(y_bytes) != 65 or y_bytes[0] != 0x04:
        raise ValueError("无效的公钥格式，应为65字节以0x04开头")
    
    # 创建secp256k1公钥对象
    public_key = ec.EllipticCurvePublicKey.from_encoded_point(
        ec.SECP256K1(), 
        y_bytes
    )
    
    # 导出为DER格式
    der_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return der_bytes

# 你的Y值
input_y = input("Enter Y: ")
input_y = binascii.unhexlify(input_y)
Y = bytearray(input_y)

# 转换
der_data = convert_y_to_der(Y)

# 保存到文件
with open('public_key.pub', 'wb') as f:
    f.write(der_data)

# 输出信息
print(f"DER公钥长度: {len(der_data)} 字节")
print(f"DER十六进制: {der_data.hex()}")
print(f"文件已保存: public_key.pub")