import streamlit as st
import google.generativeai as genai

# 1. 填入你的 API Key
genai.configure(api_key=st.secrets["GEMINI_KEY"])

# 2. 设置页面标题和图标
st.set_page_config(page_title="播客灵感大师", page_icon="🎙️")

st.title("🎙️ 播客内容大师")
st.write("输入灵感碎片，剩下的交给 播客灵感大师。")

# 3. 侧边栏配置
with st.sidebar:
    st.header("设置")
    style = st.selectbox("内容风格", ["深度对话", "犀利观点", "轻松幽默", "专业教学"])
    model_choice = st.selectbox("选择模型", ["gemini-1.5-flash", "gemini-1.5-pro"])

# 4. 主界面输入
topic = st.text_input("播客主题", placeholder="例如：出海品牌如何做本土化营销？")
reference = st.text_area("背景资料/参考大纲", placeholder="粘贴一些网页内容、采访草稿或关键点...", height=200)

if st.button("🚀 生成全套脚本"):
    if not topic:
        st.warning("请至少输入一个主题。")
    else:
        model = genai.GenerativeModel(model_choice)
        with st.spinner("播客灵感大师 正在头脑风暴中..."):
            prompt = f"""
            你是一个资深的播客制作人，请为播客《出海两面谈》制作一份内容方案。
            主题：{topic}
            背景资料：{reference}
            风格偏好：{style}
            
            输出要求：
            1. 抓人的开场白（Hook）：用 3 种不同的方式开头。
            2. 核心大纲：包含 5 个关键的讨论环节。
            3. 访谈金句：预设 3 个能引起听众共鸣的观点。
            4. 宣发文案：写一段适合发在社交媒体上的 Show Notes。
            """
            response = model.generate_content(prompt)
            
            st.markdown("---")
            st.markdown(response.text)
            st.balloons() # 庆祝一下
