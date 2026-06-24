import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import io
from PIL import Image

st.title("Phân tích dữ liệu điểm số học sinh")
uploaded_file = st.file_uploader("Chọn file Excel (có cột 'Điểm số')", type=["xlsx"])

def calculate_average(scores):
    return sum(scores) / len(scores)

def percentage_distribution(scores):
    bins = {'90-100': 0, '80-89': 0, '70-79': 0, '60-69': 0, '<60': 0}
    for score in scores:
        if score >= 90:   bins['90-100'] += 1
        elif score >= 80: bins['80-89'] += 1
        elif score >= 70: bins['70-79'] += 1
        elif score >= 60: bins['60-69'] += 1
        else:             bins['<60'] += 1
    return bins
