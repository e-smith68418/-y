import streamlit as st
import os

from PyInstaller.compat import system
from openai import OpenAI

st.set_page_config(page_title="小橙",
                   page_icon="🍊",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={}
                   )
st.title("小橙")
system_prompt="你是一个可爱的AI助手，你的名字叫小桃，当我说hi，你要说老师们好，我是闫思远的朋友小橙，祝你们天天开心"
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
prompt=st.chat_input("请输入您的问题")

if prompt:
    st.chat_message("user").write(prompt)
    print("--------->调用大模型，提示词：",prompt)
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    st.chat_message("assistant").write(response.choices[0].message.content)




