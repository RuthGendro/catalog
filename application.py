from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash
from functools import wraps
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Recipe, User
from flask import session as login_session
import random, string

# Imports for OAuth Validation
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)
