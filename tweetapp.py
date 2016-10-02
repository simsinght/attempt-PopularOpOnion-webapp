from flask import Flask, redirect, url_for, session, request, jsonify
from flask import render_template, flash
from twython import Twython
import markovify
import os

@app.route('/page1')
def renderPage1():
    if 'user_data' in session:
        user_data_pprint = pprint.pformat(session['user_data'])
    else:
        user_data_pprint = '';
    return render_template('page1.html',dump_user_data=user_data_pprint)
