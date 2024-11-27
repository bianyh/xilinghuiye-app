import streamlit as st
import re
import os

# 读取指定文件夹中的所有Markdown文件
def get_markdown_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.md')]

# 显示Markdown内容和图片
def render_markdown_with_images(markdown_text):
    pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    last_pos = 0

    for match in pattern.finditer(markdown_text):
        st.markdown(markdown_text[last_pos:match.start()], unsafe_allow_html=True)
        img_url = match.group(1)
        st.image('md/'+img_url)
        last_pos = match.end()

    st.markdown(markdown_text[last_pos:], unsafe_allow_html=True)

# 设置Streamlit页面
st.title('Markdown 文件阅读器')

# 指定Markdown文件所在的文件夹
folder_path = 'md'

# 获取文件夹中的所有Markdown文件
markdown_files = get_markdown_files(folder_path)

# 创建一个选择框让用户选择文件
selected_file = st.selectbox('选择一个Markdown文件:', markdown_files)

# 读取用户选择的Markdown文件
with open(os.path.join(folder_path, selected_file), 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# 显示Markdown文件内容
render_markdown_with_images(markdown_text)