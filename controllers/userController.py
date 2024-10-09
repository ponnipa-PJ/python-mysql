from flask import Blueprint, request, jsonify, Response
from models.user import User, db
from validators.userValidator import validateBirthdate
import json

usersBp = Blueprint('users', __name__)

@usersBp.route('/', methods=['POST'])
def createUser():
    data = request.get_json()

    valid, error_message = validateBirthdate(data['birthDate'])
    if not valid:
        return jsonify({'error': error_message}), 400

    new_user = User(name=data['name'], birthDate=error_message)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@usersBp.route('/', methods=['GET'])
def getUsers():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
     # สร้าง JSON จาก OrderedDict ด้วย json.dumps() และกำหนด ensure_ascii=False เพื่อรองรับภาษาไทย
    json_data = json.dumps(users_list, ensure_ascii=False)
    
    # ใช้ Response และกำหนด content-type เป็น application/json
    return Response(json_data, content_type='application/json')

@usersBp.route('/<int:userId>', methods=['GET'])
def get_user(userId):
    user = User.query.get_or_404(userId)
    return jsonify(user.to_dict())
    
@usersBp.route('/<int:userId>', methods=['PUT'])
def updateUser(userId):
    user = User.query.get_or_404(userId)
    data = request.get_json()

    valid, error_message = validateBirthdate(data['birthDate'])
    if not valid:
        return jsonify({'error': error_message}), 400

    user.name = data['name']
    user.birthDate = error_message
    db.session.commit()
    return jsonify(user.to_dict())

@usersBp.route('/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
    user = User.query.get_or_404(userId)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 204
