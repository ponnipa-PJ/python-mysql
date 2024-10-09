from flask import Blueprint, request, jsonify, Response
from models.post import Post, db
from models.user import User
from validators.postValidator import validatePostdata
import json

postsBp = Blueprint('posts', __name__)

@postsBp.route('/', methods=['POST'])
def createPost():
    data = request.get_json()

    valid, error_message = validatePostdata(data)
    if not valid:
        return jsonify({'error': error_message}), 400

    new_post = Post(userId=data['userId'], title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201

@postsBp.route('/', methods=['GET'])
def getPosts():
    posts = Post.query.all()
    
    posts_list = [post.to_dict() for post in posts]
     # สร้าง JSON จาก OrderedDict ด้วย json.dumps() และกำหนด ensure_ascii=False เพื่อรองรับภาษาไทย
    json_data = json.dumps(posts_list, ensure_ascii=False)
    
    # ใช้ Response และกำหนด content-type เป็น application/json
    return Response(json_data, content_type='application/json')


@postsBp.route('/<int:postId>', methods=['GET'])
def getPost(postId):
    post = Post.query.get_or_404(postId)
    return jsonify(post.to_dict())

@postsBp.route('/<int:postId>', methods=['PUT'])
def updatePost(postId):
    post = Post.query.get_or_404(postId)
    data = request.get_json()

    valid, error_message = validatePostdata(data)
    if not valid:
        return jsonify({'error': error_message}), 400

    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify(post.to_dict())

@postsBp.route('/<int:postId>', methods=['DELETE'])
def deletePost(postId):
    post = Post.query.get_or_404(postId)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'}), 204
