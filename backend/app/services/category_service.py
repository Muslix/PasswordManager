from app import db
from models import Category

def get_all_categories():
    categories = Category.query.all()
    return [{"id": category.id, "name": category.name} for category in categories]

def add_category(name):
    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()
    return new_category

def delete_category_by_id(category_id):
    category = Category.query.get(category_id)

    # Überprüfen, ob die Kategorie in Verwendung ist
    if category.is_in_use():  # Ersetzen Sie 'is_in_use()' durch die tatsächliche Methode zum Überprüfen der Beziehung
        return False  # oder geben Sie eine entsprechende Fehlermeldung zurück

    db.session.delete(category)
    db.session.commit()
    return True