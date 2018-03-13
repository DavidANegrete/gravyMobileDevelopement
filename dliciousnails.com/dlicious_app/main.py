from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

import random, string

import httplib2 #Comprehensive HTTP library in Python
import json #Used for converting in memory Python objects to a syreializxed 
            # representation, known as JSON, or Java Script Object Notation 
from flask import make_response #converts the return value from a function into a real response object 
import requests #Apache 2.0 licensed HTTP library written in Python like urlib

app = Flask(__name__)



@app.route('/')
@app.route('/dliciousnails.com')
def home():
    '''Main template for DLicious Nails '''
    title = '''D'Licious Nails | Nail Art Studio'''
    desc = ("We are a new concept nail art studio, where nail artists and nail art aficionados "
            "work together to come up with amazing designs. We offer everything to pamper your "
            "hands and feet in our nail salon.")
    
    return render_template('home.html', title = title, desc=desc)

@app.route('/about')
def about():
    '''About template '''
    title = '''D'Licious Nails | El Paso Nail Art Studio and Nail Salon'''
    desc = ("We are a nail salon in El Paso Texas that is able to offer it's clients high quality "
            "nail art and pedicures. We accomplish this by putting high quality products and embelishments in the hands "
            "of educated nail artists with the ability to make real the look you are after."
    		)
    
    return render_template('about.html', title = title, desc=desc)


@app.route('/services')
def services():
    '''Services template '''
    title = '''D'Licious Nails | Services Available at our Nail Salon'''
    desc = ("At our nail salon you can get everything from a simple gel polish manicure and pedicure to"
             "3D acryclic nail art. If you are a nail artist looking to improve your skills you have a"
             " place to learn in our studio from our certified instructors.")
    
    return render_template('services.html', title = title, desc=desc)

@app.route('/classes')
def classes():
    '''Services template '''
    title = '''D'Licious Nails | Nail Art Classes'''
    desc = ("If you want to learn to create nail art, you can come learn at our studio. "
             "We bring to the El Paso nail art community instructors that have been certified to show "
             "you how to correctly use products and and embelishments.")
    
    return render_template('classes.html', title = title, desc=desc)

@app.route('/blog')
def blog():
    '''Services template '''
    title = '''D'Licious Nails | Nail Art Blog'''
    desc = ("The nail insutry is always changing and so are things at our nail art studio."
             "Here you can get product reviews, tips and tricks or learn about changes in our"
             "nail salon.")
    
    return render_template('blog.html', title = title, desc=desc)

@app.route('/portfolio')
def portfolio():
    '''Portfolio '''
    title = '''D'Licious Nails | Nail Art done at our Nail Art Studio'''
    desc = ("We believe in doing amazing nails for each our clients. Take a look at some of the nail art"
             " we created in our East El Paso nail salon. Follow us on Instagram @dliciousnails or Facebook "
             "@DLiciousNailsNailArtStudio.")
    
    return render_template('portfolio.html', title = title, desc=desc)

@app.route('/appointments')
def appointments():
    '''Appointments function'''
    title = '''DLicious Nails | Booking an Appointment with Us'''
    desc = ("We always want for it to be easy for you to book an appointment with your favorite artist"
             " using our booking system you can book in advance. You can also check if we can take you as walk-in  "
             " or if something happens you can change or cancel your appointment 24 hours in before your appointments.")
    
    return render_template('appointments.html', title = title, desc=desc)

@app.route('/contact')
def contact():
    '''Contact form'''
    title = '''DLicious Nails | Contact our East El Paso Nail Salon'''
    desc = ("You can call us or message us if you need to get in contact with us. We are avaible to reply"
             " Tuesday - Saturday, from 10am-7pm. Our nail salon is in East El Paso one block past El Dorado High School "
             " in the Quail Park Professional Plaza.")
    
    return render_template('contact.html', title = title, desc=desc)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

