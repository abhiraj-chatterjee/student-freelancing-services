import datetime
from flask import Flask, jsonify, request, session
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

# Use a service account
if not firebase_admin._apps:
    cred = credentials.Certificate('keys/student-freelancing-services-firebase-adminsdk-h3s90-835c3d5cd4.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/api')
def apiIntro():
    return 'Unknown Page', 404

# Submit a new student
@app.route('/api/new/student', methods=['POST'])
def newStudent():
    student_data = {
        # Auto-generated ID is the student ID
        'created_at': datetime.datetime.now(), # Timestamp
        'name': 'Abhiraj Chatterjee',
        'college': 'Pennsylvania State University',
        'email': 'abhirajchatterjee@gmail.com',
        'phone': '+18148628746',
        'address': '206 Robinson Hall, University Park, State College, PA - 16802',
        'skills': [],
        'rating': 0, 
        'wallet': 0,
        'jobs': []
    }
    db.collection('students').document().set(student_data)
    return jsonify(student_data), 201

# Submit a new employer
@app.route('/api/new/employer', methods=['POST'])
def newEmployer():
    employer_data = {
        # Auto-generated ID is the post ID
        'created_at': datetime.datetime.now(), # Timestamp
        'name': 'ACM',
        'college': 'Pennsylvania State University',
        'phone': '+19831002862',
        'address': '172 Kankulia Road, Golpark, State College, PA - 16802'
    }
    db.collection('employers').document().set(employer_data) 
    return jsonify(employer_data), 201  

# Submit a new post
@app.route('/api/new/post', methods=['POST'])
def newPost():
    
    post_data = {
        # Auto-generated ID is the post ID
        'created_at': datetime.datetime.now(), # Timestamp
        'employer': 'EcxRdqJXhGULazvYlNNS',
        'location': 'State College, PA',
        'title': 'Research Assisstant',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in tellus sollicitudin, commodo elit quis, condimentum dui. Integer tristique consectetur lorem, pulvinar auctor metus faucibus et. Ut consectetur elit convallis imperdiet consequat. Nullam maximus arcu id consectetur mattis. Phasellus semper diam at quam condimentum varius.',
        'responsibilities': [
            'resp1',
            'resp2',
            'resp3'
        ],
        'skills': [
            'skill1',
            'skill2',
            'skill3'
        ],
        'apply': 'abc123@psu.edu',
        'fulfilled': False,
        'positions': 2,
        'completed': False
    }
    db.collection('posts').document().set(post_data)
    return jsonify(post_data), 201
    # random_hash = json.loads(request.data)
    # return (random_hash['name'], 201)

# Get all the posts
@app.route('/api/posts/all', methods=['GET'])
def allPosts():
    docs = db.collection('posts').stream()
    posts = []
    for each in docs:
        data = each.to_dict()
        data['id'] = each.id
        posts.append(data)
    return jsonify(posts), 200

# Update a post if fulfilled
@app.route('/api/post/<postID>/update', methods=['PUT'])
def updatePost(postID):
    new_post_data = {
        'employees': [
            'RGkmqiFr86A6BOatNDzG',
            'kAXxZWWH8JNROgyeoLOG'
        ]
    }
    db.collection('posts').document(postID).update({ 'fulfilled': True })
    db.collection('posts').document(postID).set(new_post_data, merge=True)
    return jsonify(new_post_data), 200

# Complete a post
@app.route('/api/post/<postID>/complete', methods=['PUT'])
def completePost(postID):
    sent_data = [
        {
            'id': 'RGkmqiFr86A6BOatNDzG',
            'rating': 2,
            'stipend': 1240.50
        },
        {
            'id': 'kAXxZWWH8JNROgyeoLOG',
            'rating': 3,
            'stipend': 2500.35
        }
    ]
    for each in sent_data:
        student_doc = db.collection('students').document(each['id']).get().to_dict()
        new_wallet_amount = student_doc['wallet'] + each['stipend']
        if len(student_doc['jobs']) == 0: # To prevent Division by Zero Error
            new_rating = each['rating']
        else:
            new_rating = (len(student_doc['jobs']) * student_doc['rating'] + each['rating']) / (len(student_doc['jobs'])+1)
        db.collection('students').document(each['id']).update({
            'rating': round(new_rating,1),
            'wallet': round(new_wallet_amount,2),
            'jobs': firestore.ArrayUnion([postID]),
            'completed': True
        })
    
    return jsonify(sent_data), 200


# Testing
@app.route('/api/test')
def test():
    # Cloud Firestore Database Testing
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })
    return 'Success!'
