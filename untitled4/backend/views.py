from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
import json
import sqlite3


def initDB():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS raspberries(serial TEXT PRIMARY KEY, owner TEXT, name TEXT)''')
    conn.commit()

def deleteRasp(serial):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM raspberries WHERE serial = ?''',(serial,))
    conn.commit()
    print("Raspberry with serial: {} deleted".format(serial))
    return

def addCameraToDB(serial, owner, name):
    initDB()
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO raspberries(serial,owner,name) VALUES(?,?,?)''',(serial,owner,name))
    conn.commit()
    print("Add Camera to DB: {} {} {}".format(serial, owner, name))
    return

def getCamerasByOwner(owner):
    print("Get Cameras by Owner: {}".format(owner))
    conn = sqlite3.connect('../db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''SELECT serial FROM raspberries WHERE owner = ?''',(owner,))
    data = cursor.fetchall()
    return data

def setCameraOwner(owner,serial):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''UPDATE raspberries SET owner = ? WHERE serial = ?''',(owner,serial))
    conn.commit()
    print("New owner of {} is {}".format(serial,owner))
    return

# Create your views here.

#PATH: /v1/camera_address
@api_view(['GET'])
def get_test_address(request,format=None):
    if request.method == 'GET':
        data = {"id":"http://52.236.165.15:80/hls/test.m3u8"}
        dump = json.dumps(data)
        return HttpResponse(dump, content_type="application/json")

#PATH: /v1/add_rasp
@api_view(['POST'])
def register_rasp(request,format=json):
    if request.method == 'POST':
        #read serial from json
        b_json = request.body.decode('UTF-8')
        data_json = json.loads(b_json)
        serial = data_json['serial_id']
#       print("SERIAL: {}".format(serial))

        #add to serial to db with default name "camera"
        addCameraToDB(serial, None, "Camera")

	#send back 200
        return HttpResponse(status.HTTP_200_OK)

#PATH: /v1/get_cameras/<owner>/
@api_view(['GET'])
def get_raspis(request,owner,format=json):
    if request.method == 'GET':
        #read owner from request
        #receive list of his raspies
        listOfCameras = getCamerasByOwner(owner)
        for camera in listOfCameras:
            print(camera)
        data = {"list":[x for x in listOfCameras]}
        json_data = json.dumps(data)
        return Response(data=json_data)

#PATH: /v1/connect
@api_view(['POST'])
def connect_rasp_with_user(request,format=json):
    if request.method == 'POST':
        #receive from json user and raspi serial
        b_json = request.body.decode('utf-8')
        data_json = json.loads(b_json)
        owner = data_json['email']
        raspberry = data_json['serial']
        setCameraOwner(owner,raspberry)
	#add another owner to rasp in db
        #send back 200
        return HttpResponse(status.HTTP_200_OK)

#PATH: /v1/post_sensors
@api_view(['POST'])
def sensors_update(request,format=json):
    if request.method == 'POST':
        b_json = request.body.decode('utf-8')
        data_json = json.loads(b_json)
        owner = data_json['email']
        raspberry = data_json['serial']
	#get devices connected with raspi
        #send to firebase POST request with data: devicesIDs and sensor data
        #send back 200
        return

#PATH: /v1/delete
@api_view(['POST'])
def delete_rasp(request):
    if request.method == 'POST':
        return

