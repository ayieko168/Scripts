## This is a http file server based on pywebio

import pywebio
from pywebio import start_server, config
from pywebio.output import *
from pywebio.session import *
import logging
from logging.handlers import RotatingFileHandler
import os

ROOT_DIR = "D:/Projects and Research/Python Projects/Haron-CRM-Software/output"

log_file = os.path.join(ROOT_DIR, 'file_server.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(levelname)s [%(asctime)s] - %(message)s')
log_file_handler = RotatingFileHandler(log_file, mode='a', maxBytes=200*1000, backupCount=2, encoding=None, delay=0)
log_file_handler.setFormatter(log_formatter)
logger.addHandler(log_file_handler)


@config(title="Calm Recoveries LTD - File Server", description="A Debt Collection Web Application", theme='dark')
def index():
    
    ## remove the header
    run_js("""
    function HideFooter(){
        $(".footer").hide();
    };
    
    $(document).ready(function() {
        HideFooter();
    });
    
    """)


    logger.info(f"[NEW CONNECTION] DETAILS: {info}")

    put_markdown("# Calm Recoveries File Server")

    
    for f in os.listdir(ROOT_DIR):
        if f.endswith('.exe') or f.endswith('.txt'):
            
            put_html(f""" <a href="/static/{f}">{f}</a> <br>""")



if __name__ == '__main__':
    start_server(index, port=8100, debug=True, auto_open_webbrowser=False, static_dir=ROOT_DIR, )