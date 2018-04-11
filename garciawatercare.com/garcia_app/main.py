from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

import random, string

import httplib2 #Comprehensive HTTP library in Python
import json #Used for converting in memory Python objects to a syreializxed 
            # representation, known as JSON, or Java Script Object Notation 
from flask import make_response #converts the return value from a function into a real response object 
import requests #Apache 2.0 licensed HTTP library written in Python like urlib

app = Flask(__name__)



@app.route('/')
@app.route('/garciawatercare.com')
def home():
    '''Main template for Garcia Water Care '''
    title = '''Garcia Water Care | Water Softeners and Filtration solutions'''
    desc = ("A water filtration company based out of El Paso. We offer products that are"
            "made in America. Our certified water softeners and reverse"
            " osmosis systems are engineered by Puronics.")
    
    return render_template('home.html', title = title, desc=desc)

@app.route('/about')
def about():
    '''About template for Garcia Water Care'''
    title = '''Garcia Water Care | RO's and Water Softeners in El Paso'''
    desc = ("Our service calls are always free. We know our certified systems will soften "
            " and purity water In your home or place of business. Softened water in your"
            " home protects your home and family.")
    
    return render_template('about.html', title = title, desc=desc)


@app.route('/water-test')
def water_test():
    '''Water Tests template '''
    title = '''Garcia Water Care | Complementary water test and '''
    desc = ("Get a water test El Paso and learn why a water softener and reverse osmosis "
            "system in El Paso is a must have. Let us show you why choosing us for your "
            "water care needs will be a lifelong investment.")
    
    return render_template('water-test.html', title = title, desc=desc)


@app.route('/water-news')
def water_news():
    '''Services template '''
    title = '''Garcia Water Care | Water Care News'''
    desc = ("Water in part of the Southwest is shared between two countries "
            "and three states. Our goal is to educate the public about the "
            "quality of the water in our community.")
    
    return render_template('water-news.html', title = title, desc=desc)

@app.route('/products')
def products():
    '''Products template'''
    title = '''Garcia Water Care | Water softeners and filters from Puronics'''
    desc = ("Our systems are certified by the EPA and WQA to do the job they "
            "are advertised to do. We stand behind our Puronics products and "
            "will test them to insure they ware working to the level we say they do.")
    
    return render_template('products.html', title = title, desc=desc)


@app.route('/contact')
def contact():
    '''Contact form Garcia Water Care'''
    title = '''Garcia Water Care | Located in East El Paso but serving the Southwest'''
    desc = (" Let's talk about why our water softeners, reverse osmosis systems"
            " and our service after the installation is the best you will find"
            " in EL Paso, if you are looking to have filtered water in El Paso."
             " in the Quail Park Professional Plaza.")
    
    return render_template('contact.html', title = title, desc=desc)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

