# from flask import request, jsonify
# from app import app, db
# from models import Category
# from . import api_blueprint

# @app.route('/api/categories', methods=['POST'])
# def add_category():
#     category_name = request.json.get('name')
#     category = Category(name=category_name)
#     db.session.add(category)
#     db.session.commit()
#     return jsonify({'message': 'Category added successfully'}), 201

# @app.route('/api/categories/<int:category_id>', methods=['DELETE'])
# def remove_category(category_id):
#     category = Category.query.get_or_404(category_id)
#     db.session.delete(category)
#     db.session.commit()
#     return jsonify({'message': 'Category removed successfully'}), 200