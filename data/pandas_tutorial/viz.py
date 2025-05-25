import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time

df = pd.DataFrame({
    'x': np.random.randint(0, 100, size=1_000_000),
    'y': np.random.randint(0, 100, size=1_000_000)
})

# For loop / apply 慢很多
start = time.time()
print(df)
df['sum_apply'] = df.apply(lambda row: row['x'] + row['y'], axis=1)
t1 =  time.time() - start

# Vectorized 速度快很多
# 直接对列进行操作
start = time.time()
df['sum_vec'] = df['x'] + df['y']
t2=  time.time() - start




import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a': np.random.randint(0, 100, size=1_000_000),
    'b': np.random.randint(0, 100, size=1_000_000)
})

# ❌ 逐行处理（非向量化）
df['sum_apply'] = df.apply(lambda row: row['a'] + row['b'], axis=1)

# ✅ 向量化（整列处理）
df['sum_vec'] = df['a'] + df['b']







# 方法与耗时数据
methods = ['apply', 'vectorized']





times = [t1, t2]

# 创建图表
fig = go.Figure()

fig.add_trace(go.Bar(
    x=methods,
    y=times,
    text=[f"{t:.4f}秒" for t in times],  # 显示标签
    textposition='outside',
    marker=dict(
        color=["#F1948A", "#85C1E9"],  # 粉红和蓝色
        line=dict(color='black', width=1)  # 黑色边框
    ),
    width=0.5
))

# 设置图表样式
fig.update_layout(
    title=dict(text="向量化 vs apply 操作耗时对比(100万行数据进行加法)", font=dict(size=18)),
    xaxis_title="方法",
    yaxis_title="耗时（秒）",
    yaxis=dict(range=[0, max(times) + 0.5], gridcolor='rgba(142, 180, 200, 0.25)'),
    plot_bgcolor='white',
    font=dict(size=14),
    bargap=0.3
)

fig.show()
