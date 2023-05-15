# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:17:36 2023

@author: kavya
"""
import torch
import streamlit as st



if __name__ == '__main__':
    torch.multiprocessing.freeze_support()

    import sys
    sys.path.append("")
    import streamlit as st
    #from pages import Info_dashboard, Multi_search, Analysis, , Scatter_map, analogies_idioms

    # page config
    st.set_page_config(page_title='Adaptive E-learning System(ADES)', page_icon=':capital_abcd:')

    # about
    st.sidebar.markdown(" \nThis Proof-of-Concept dashboard was developed by the **_GM AI Foundry_**.")
    
    #sidebar navigation
    options = st.sidebar.radio('Select a page:', 
        ['Info', 'Search', 'Analysis', 'Maps'])
    
    
    if options == "Info":
        st.markdown("# ADES -Search System❄️ \n Welcome to ADES, an E-Farming sytem to connect the farmers to investors. \n**_ADES_** is developing an app that utilizes AI technologies to automatically evaluate "
            + "the accessibility and inclusivity intelligence for farmers to investors/buyers")
        st.sidebar.markdown("# Information")
    elif options == "Search":
        st.markdown("# Connect to Farm-lands 🎉")
        st.sidebar.markdown("# Search by category🎉")
    elif options == "Analysis":
        st.markdown("#   Visualization❄️")
        st.sidebar.markdown("#     Data Visualization❄️")
    
    #elif options == "Maps":
    #st.markdown("# Mapping according to region ")
    #st.sidebar.markdown("# Plotting on the map ")


      
   
 