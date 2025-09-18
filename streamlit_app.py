import streamlit as st

import streamlit as st

st.title("Streamlit 요소 데모")

st.header("텍스트 요소")
st.write("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** _스타일링_ 지원!")

st.header("입력 요소")
name = st.text_input("이름을 입력하세요:")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("동의합니다")

st.header("버튼과 상호작용")
if st.button("인사하기"):
    st.success(f"안녕하세요, {name or '익명'}님! 나이: {age}")

st.header("슬라이더와 선택")
level = st.slider("난이도", 1, 10, 5)
color = st.selectbox("색상 선택", ["빨강", "초록", "파랑"])
st.write(f"선택한 난이도: {level}, 색상: {color}")

st.header("이미지와 차트")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.subheader("랜덤 데이터프레임")
df = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
st.dataframe(df)

st.subheader("라인 차트")
st.line_chart(df)

st.subheader("matplotlib 차트")
fig, ax = plt.subplots()
ax.plot(df["A"], label="A")
ax.plot(df["B"], label="B")
ax.legend()
st.pyplot(fig)
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
