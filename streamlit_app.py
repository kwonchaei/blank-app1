
import streamlit as st

st.title("나의 수학실력은 얼마나 될까?")
st.write("아래 6문항에 답해 자신의 수학 능력을 점검해보세요. (1: 전혀 아니다 ~ 5: 매우 그렇다)")

questions = [
    "1. 수학 수업 내용을 이해하는 데 어려움이 없다.",
    "2. 수학 문제를 읽고 핵심을 빠르게 파악할 수 있다.",
    "3. 수학 공식이나 개념을 잘 기억하고 있다.",
    "4. 다양한 유형의 문제를 논리적으로 해결할 수 있다.",
    "5. 수학 공부에 흥미를 느끼고 자주 복습한다.",
    "6. 어려운 문제도 포기하지 않고 끝까지 도전한다."
]

responses = []
for q in questions:
    responses.append(st.slider(q, 1, 5, 3, key=q))

if st.button("자가진단 결과 확인"):
    total = sum(responses)
    avg = total / len(questions)
    st.subheader(f"총점: {total}점 (평균: {avg:.2f})")
    if avg >= 4.5:
        st.success("수학 능력이 매우 우수합니다! 자신감을 가지세요.")
    elif avg >= 3.5:
        st.info("수학 능력이 좋은 편입니다. 꾸준히 연습하면 더 좋아질 수 있어요.")
    elif avg >= 2.5:
        st.warning("기본기는 있지만, 더 많은 연습이 필요합니다.")
    else:
        st.error("수학에 대한 흥미와 기초부터 차근차근 다져보세요!")
