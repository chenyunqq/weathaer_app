import streamlit as st
import requests
hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# 设置页面标题和布局（适配移动端）
st.set_page_config(page_title="天气查询", layout="wide")
st.title("🌤️ 天气查询工具")

# 输入城市名
city = st.text_input("请输入城市名（如：北京）", placeholder="例如：上海")

# 当用户输入城市并点击按钮时查询天气
if st.button("查询天气") and city:
    try:
        # 调用免费天气API（这里用高德开放平台，需先注册获取key）
        # 高德开放平台注册地址：https://lbs.amap.com/，注册后申请「天气查询」API的key
        api_key = "0292807e8d9c2a5f059b3f920da766b0"  # 替换为你自己的key
        url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city}&key={api_key}"

        # 发送请求
        response = requests.get(url)
        data = response.json()

        # 解析并显示结果
        if data["status"] == "1" and len(data["lives"]) > 0:
            weather = data["lives"][0]
            st.success(f"📌 {weather['city']} 的实时天气：")
            col1, col2 = st.columns(2)  # 分两列显示（适配手机）
            with col1:
                st.write(f"🌡️ 温度：{weather['temperature']}℃")
                st.write(f"💧 湿度：{weather['humidity']}%")
            with col2:
                st.write(f"🌬️ 风向：{weather['winddirection']}")
                st.write(f"💨 风力：{weather['windpower']}级")
            st.write(f"☁️ 天气状况：{weather['weather']}")
            st.write(f"📅 更新时间：{weather['reporttime']}")
        else:
            st.error("未查询到该城市的天气，请检查城市名是否正确")
    except Exception as e:
        st.error(f"查询失败：{str(e)}")