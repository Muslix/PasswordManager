from flask import Blueprint, request, jsonify
from services.category_service import get_all_categories, add_category, delete_category_by_id

category_blueprint = Blueprint('category', __name__)

@category_blueprint.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        categories = get_all_categories()
        return jsonify(categories)

    elif request.method == 'POST':
        name = request.json['name']
        new_category = add_category(name)
        return jsonify({"message": "Category added", "id": new_category.id})

@category_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    # Hier können Sie überprüfen, ob die Kategorie in Verwendung ist.
    # Wenn sie in Verwendung ist, geben Sie eine entsprechende Antwort zurück.
    # if category_in_use(category_id):
    #     return jsonify({"success": False, "message": "Category is in use and cannot be deleted"})

    deleted = delete_category_by_id(category_id)
    if deleted:
        return jsonify({"success": True, "message": "Category deleted"})
    else:
        return jsonify({"success": False, "message": "Category not found or in use"})