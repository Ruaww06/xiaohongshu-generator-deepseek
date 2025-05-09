import streamlit as st
from utils import generate_xiaohongshu

st.header("🖋️小红书爆款文案生成器")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入你的DeepSeek API密钥", type="password")
    st.markdown("[获取DeepSeek API密钥](https://api-docs.deepseek.com/zh-cn/)")

theme = st.text_input("🗒️请输入主题")
submit = st.button("开始创作")
if submit and not deepseek_api_key:
    st.info("请输入你的DeepSeek API密钥")
    st.stop()

if submit and not theme:
    st.info("请输入主题")
    st.stop()
if submit:
    with st.spinner("AI正在创作中，请稍后..."):
        result = generate_xiaohongshu(theme, deepseek_api_key)
    st.success("创作完成!!!")
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        i = 1
        for title in result.titles:
            st.write("##### 小红书标题%d" % i)
            st.write(title)
            i += 1
    with right_column:
        st.write("##### 小红书正文")
        st.write(result.content)