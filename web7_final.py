import os
import time
import streamlit as st
import streamlit.components.v1 as components
import sklearn
from sklearn import datasets 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from st_aggrid import AgGrid
from st_aggrid.shared import GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from mynav2 import mynav
from ketcher import ketcher
from mycarousel import mycarousel
import base64

import warnings
# 不显示warning提示
def warn(*args, **kwargs):pass
warnings.warn = warn

def config(title='Web Server', layout='wide', icon='🦈'):
    ### init page config
    st.set_page_config(page_title=title, layout=layout, page_icon=icon, menu_items={})
    ### init session
    st.session_state.host = 'http://localhost:80'
    session_init = [('nav_click_time', 0), ('nav_search_time', 0), ('page_id', '0'), ('query', None), 
    ('choice', None), ('select', None), ('afrom', '0')]
    for key, value in session_init:
        if key not in st.session_state:  st.session_state[key] = value
    ### when loading by url
    query = st.experimental_get_query_params()
    if 'afrom' in query and query['afrom'][0]=='1':
        for key, value in query.items():
            st.session_state[key] = value[0]
        st.experimental_set_query_params(afrom='0')
        #st.write(st.session_state)

def page_redirect(params = {}):
    st.session_state.update(params) # 更新session
    #st.write(params)
    #time.sleep(3)
    st.experimental_rerun()

def navigation(items=[('0', 'Home')], nav_times=[0, 0], default=[0, 0, '0', '']):
    nav_click_time, nav_search_time, page_id, nav_input = mynav(items=items, times=nav_times, default=default)
    #st.write(nav_click_time, nav_search_time, page_id, nav_input)
    if int(nav_click_time) > int(st.session_state.nav_click_time):
        page_redirect({'page_id':page_id, 'nav_click_time':nav_click_time})
    if int(nav_search_time) > int(st.session_state.nav_search_time):
        #st.write(nav_click_time, nav_search_time, page_id, nav_input)
        #time.sleep(3)
        page_redirect({'page_id':'2', 'nav_search_time':nav_search_time, 'query':nav_input, 'choice':'navigation'})

def page_home():
    mycarousel()
    st.info('This is Home')
    with st.form("my_form"):
        query = st.text_input('Query:')
        choice = st.radio('Type:', ['type1', 'type2'])
        submitted = st.form_submit_button("Submit")
        #st.write(submitted)
        if submitted:
            page_redirect({'page_id':'2', 'query':query, 'choice':choice})

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def page_2():
    with st.container():
        st.write('''
        <style>
        p {
            font-size:18px;
        }
        a {
            font-size:18px;
        }
        .st-af {
            font-size: 18px;
        }
        </style>
        <script src="http://code.jquery.com/jquery-2.1.1.min.js"></script>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
        ''', unsafe_allow_html=True)
    with st.container():
        st.write('''
        <div class="jumbotron">
            <div class="container">
                <div class="jumbotron">
                    <h1>Hello, world!</h1>
                    <p>xxxxxx xxxxxxxxxxxx xxxx xx xx xx   xxxxxxxxxxx xxx xxxxxxxxx xxxx xxx xxxxxxx </p>
                    <p><a class="btn btn-default btn-lg" href="#" role="button">Learn more</a></p>
                </div>
            </div>
        </div>
        </br></br>

        <div class="container">
            <ul>
            <li><a href="?page_id=3&select=1&afrom=1" target="_parent">1. 高升</a></li>
            <li><a href="?page_id=3&select=2&afrom=1" target="_parent">2. 高文星</a></li>
            <li><a href="?page_id=3&select=3&afrom=1" target="_parent">3. 陶丽雯</a></li>
            </ul>
        </div></br></br>
        ''', unsafe_allow_html=True)
    with st.container(): # h3中纯中文存在首次载入滚动底部的bug@！
        st.write(f'''
        <meta http-equiv="Content-Type" content="text/html; charset=gbk" />
        <div class="row">
            <div class="col-sm-6 col-md-4"><div class="thumbnail">
                <a href="?page_id=3&select=1&afrom=1" target="_parent"><img src="data:image/png;base64, {get_base64_of_bin_file('./streamlit/resources/1.png')}" width="500px" /></a>
                <div class="caption">
                    <h3><span style="display:none;">1. </span><span>高升</span></h3>
                    <p>xxx</p>
                </div>
            </div></div>
            <div class="col-sm-6 col-md-4"><div class="thumbnail">
                <a href="?page_id=3&select=2&afrom=1" target="_parent"><img src="data:image/png;base64, {get_base64_of_bin_file('./streamlit/resources/2.png')}" width="500px" /></a>
                <div class="caption">
                    <h3><span style="display:none;">1. </span><span>高文星</span></h3>
                    <p>xxxx</p>
                </div>
            </div></div>
            <div class="col-sm-6 col-md-4"><div class="thumbnail">
                <a href="?page_id=3&select=3&afrom=1" target="_parent"><img src="data:image/png;base64, {get_base64_of_bin_file('./streamlit/resources/3.png')}" width="500px" /></a>
                <div class="caption">
                    <h3><span style="display:none;">1. </span><span>陶丽雯</span></h3>
                    <p>xxx</p>
                </div>
            </div></div>
        </div>
        </br>
        ''', unsafe_allow_html=True)
        
            
def page_1():
    st.info('This is Page')
    rawdata = datasets.load_breast_cancer()
    data = pd.DataFrame(rawdata['data'], columns=rawdata['feature_names'], index=range(len(rawdata['data'])))
    data['Index'] = range(len(rawdata['data']))
    columns = ['Index']
    columns.extend(rawdata['feature_names'])
    data = data[columns]
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_selection(selection_mode="single")
    gridOptions = gb.build()
    reponse = AgGrid(data, gridOptions=gridOptions, enable_enterprise_modules=False, allow_unsafe_jscode=True, 
                     update_mode=GridUpdateMode.SELECTION_CHANGED)
    if reponse['selected_rows']:
        page_redirect({'page_id':'3', 'select':reponse['selected_rows'][0]['Index']})

def page_search_result():
    st.info('This is search result page')
    # 搜索内容 ...
    if type(st.session_state['query'])==type(None): st.error('No Query')
    else:
        query = st.session_state['query']
        choice = st.session_state['choice']
        st.success(f'Success!')
        st.write(f'<h1>文章内容</h1><h3>{query}</h3><p>{choice}</p><br/><br/><br/>', unsafe_allow_html=True)

def page_info():
    st.info('This is Info page')
    if type(st.session_state['select'])==type(None): st.error('No Query')
    else:
        st.header('个人简介:')
        index = str(st.session_state['select']).strip()
        from PIL import Image
        if index not in ['1', '2', '3']: index = '1'
        image = Image.open('./streamlit/resources/'+index+'.png')
        st.image(image, caption='', width=300)
        html = ''.join(open('./streamlit/resources/'+index+'.txt', 'r').readlines())
        st.write(html, unsafe_allow_html=True)
        

def chemial_search():
    st.empty()
    with st.container():
        mol = ketcher() # https://lifescience.opensource.epam.com/ketcher/developers-manual.html#access-ketcher
        time.sleep(1) #ketcher插件比较大， 等待一会让他加载完文件
        html = """
            <script>
                // ！！！注意这里1为ketcher所在的第1个iframe，如果前面插入了多个iframe，需要修改
                var ifketcher = parent.document.getElementsByTagName("iframe")[1];
                var ketcher = ifketcher.contentWindow.document.getElementById('ifKetcher').contentWindow.ketcher;
                ketcher.setMolecule('c1ccccc1'); // 载入后在屏幕上添加一个苯环
                
                var mybtn = ifketcher.contentWindow.document.getElementById('mybtn');
                var myinput = ifketcher.contentWindow.document.getElementById('myinput');
                mybtn.addEventListener("click", function() {
                    ketcher.getSmiles().then((data)=>{ //getMolfile; getSmiles
                        myinput.value = data;
                        ifketcher.contentWindow.sendDataToPython({
                            value: myinput.value,
                            dataType: "json",
                        });
                    });
                })
            </script>
        """
        components.html(html)
        st.subheader('分子Smiles:')
        st.write(mol)

def set_page_style():
    hide_streamlit_markings = """
        <style>
        div[data-testid="stToolbar"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        div[data-testid="stDecoration"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        div[data-testid="stStatusWidget"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        #MainMenu {
            visibility: hidden;
            height: 0%;
        }
        header {
            visibility: hidden;
            height: 0;
        }
        div[class="block-container css-18e3th9 egzxvld2"] {
            padding-top: 0rem;
        }
        div[data-testid="stAppViewContainer"] {
            padding-top: 0px;
        }
        footer {
            visibility: visible;
            height: 60px;
        }
        </style>
    """
    st.markdown(hide_streamlit_markings, unsafe_allow_html=True)

def set_footer():
    footer = """
        <script>
            var footer = parent.document.getElementsByTagName('footer')[0]
            footer.innerHTML = '';
            var p = document.createElement("p");
            p.innerText = 'TJ CADD';
            p.style.color='white';
            footer.appendChild(p);
            footer.style.background='black';
            footer.style.height='60px';
        </script>
    """
    components.html(footer)

def main():
    config()
    with st.container():
        pages = [('0', 'Home'), ('1', 'Page'), ('5', 'Page2'), ('4', 'Ketcher')]
        nav_times = [st.session_state.nav_click_time, st.session_state.nav_search_time]
        navigation(pages, nav_times)
    with st.container():
        page_redirection = {'0':page_home, '1':page_1, '2':page_search_result, '3':page_info, '4':chemial_search, '5':page_2}
        #st.write(st.session_state.page_id)
        page_redirection[st.session_state.page_id]()
    #time.sleep(3)
    
if __name__ == '__main__':
    main()
    set_page_style()
    set_footer()