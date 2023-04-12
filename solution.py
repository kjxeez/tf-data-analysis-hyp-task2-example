import pandas as pd
import numpy as np


chat_id = 584664949 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: #выборки параметра F
    alpha = 0.05
    p_val = stats.anderson_ksamp([x, y])[2]
    return p_val < alpha
