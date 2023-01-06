# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:57:11 2023

@author: tlebn
"""
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
