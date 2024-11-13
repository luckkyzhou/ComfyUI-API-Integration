import hashlib
import time
import uuid


def generate_seed():
    """
    Generates a pseudo-random seed based on the current timestamp.
    The seed is constrained within a range (0 to 100000000) by applying a modulo operation.

    Returns:
        int: The generated seed value.
    """
    # 获取当前时间戳
    current_time = time.time()

    # 将时间戳转换为字符串并进行哈希处理
    time_str = str(current_time)
    hash_object = hashlib.md5(time_str.encode())
    hash_digest = hash_object.hexdigest()

    # 将哈希值转换为整数，并取模以限制范围
    seed = int(hash_digest, 16) % 100000000
    print(seed)
    return seed


def generate_client_id():
    return str(uuid.uuid4())
