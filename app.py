import streamlit as st

st.set_page_config(page_title="自我介绍",page_icon="🍨", layout="wide")

st.title("关于我")

st.sidebar.header("目录")
section = st.sidebar.radio("跳转至", ["转专业原因", "成绩", "所作努力", "未来期望"])

#转专业原因
if section == "转专业原因":
    st.header("转专业原因")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**理科优势**\n\n相比于医学的强记忆性，更喜欢和擅长理科")
    with col2:
        st.success("**计算机兴趣**\n\n喜欢编程与新技术，希望将计算机作为终身事业。")
    st.markdown("---")
    st.caption("从口腔医学跨出，是因为我内心更向往代码世界的创造与逻辑之美。")

#学业成绩
elif section == "成绩":
    st.header("学业成绩")


    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("上学期绩点", "3.99", "专业排名 11/85")
    with col2:
        st.metric("高等数学", "100分", "总评 98")
    with col3:
        st.metric("四级成绩", "560分")

    col4, col5 = st.columns(2)
    with col4:
        st.metric("高考数学", "123分")
    with col5:
        st.metric("高考英语", "135分")

    st.markdown("---")



#3. 为转专业所做的努力
elif section == "所作努力":
    st.header("为转专业所作的努力")

    # 用 expander 展示详细项目
    with st.expander("自学Python"):
        st.write("""
        - 系统学习Python基础、面向对象 
        - 学习过程中完成 **大量代码片段**（列表，元组，函数等）   
        """)
        code_images = [
            "img.png",
            "img_1.png",
            "img_2.png",
            "img_3.png",
            "img_4.png",
            "img_5.png",
            "img_6.png"
        ]

        if "img_index_code" not in st.session_state:
            st.session_state.img_index_code = 0

        current_idx = st.session_state.img_index_code
        st.image(code_images[current_idx], caption=f"代码截图 {current_idx + 1}/{len(code_images)}",
                 use_container_width=True)

        col_left, col_mid, col_right = st.columns([1, 2, 1])
        with col_left:
            if st.button("◀ 上一张", key="prev_code"):
                st.session_state.img_index_code = (current_idx - 1) % len(code_images)
                st.rerun()
        with col_right:
            if st.button("下一张 ▶", key="next_code"):
                st.session_state.img_index_code = (current_idx + 1) % len(code_images)
                st.rerun()


    with st.expander("人体器官交互程序"):
        st.write("""
        - 引入 **tkinter**  
        - 自己编写程序获取部位的坐标，形成矩形区域 
        - 点击部位后显示名称 
        - **项目亮点**：将医学解剖知识与编程结合
        """)
        st.image("./img_8.png",
                 caption="项目示意图")

    with st.expander("大模型部署与API调用"):
        st.write("""
        - 使用 **Ollama** 本地部署 **DeepSeek** 开源模型  
        - 学会调用官方API，并用 **Apifox** 进行接口测试  
        - 能够完成文本生成、对话等基础任务  
        """)
        st.image("img_7.png",
                 caption="项目示意图")

    st.success("通过自学和实践，对于计算机专业的兴趣只增不减。")


else:
    st.header("未来的展望")

    st.subheader("短期目标")
    st.markdown("""
    - 深入学习python，并接触其他语言 
    - 尝试**云服务平台** 上部署大模型
    
    """)
    st.subheader("长期目标")
    st.markdown("""
        - 转入计算机专业深度学习

        """)

# 底部统一信息
st.sidebar.markdown("---")
