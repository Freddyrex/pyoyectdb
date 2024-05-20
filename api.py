from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:3355@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos
class Product(db.Model):
    Product_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.Text, nullable=True)
    Price = db.Column(db.Numeric(10, 2), nullable=False)
    Available_Quantity = db.Column(db.Integer, nullable=False)
    Location = db.Column(db.String(255), nullable=True)
    Supplier_ID = db.Column(db.Integer, db.ForeignKey('supplier.Supplier_ID'), nullable=True)
    supplier = db.relationship('Supplier', backref='products')

class Sale(db.Model):
    Sales_ID = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    Total = db.Column(db.Numeric(10, 2), nullable=False)
    Client_ID = db.Column(db.Integer, db.ForeignKey('client.Client_ID'), nullable=True)

class Client(db.Model):
    Client_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255), nullable=True)
    Email = db.Column(db.String(255), nullable=True)
    Telephone = db.Column(db.String(20), nullable=True)

class User(db.Model):
    User_ID = db.Column(db.Integer, primary_key=True)
    User_Name = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Role = db.Column(db.String(50), nullable=True)

class Supplier(db.Model):
    Supplier_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255), nullable=True)
    Telephone = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(255), nullable=True)

class SalesDetail(db.Model):
    SalesDetail_ID = db.Column(db.Integer, primary_key=True)
    Sales_ID = db.Column(db.Integer, db.ForeignKey('sale.Sales_ID'), nullable=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey('product.Product_ID'), nullable=True)
    Quantity = db.Column(db.Integer, nullable=False)
    Unit_Price = db.Column(db.Numeric(10, 2), nullable=False)

class UserSale(db.Model):
    UserSale_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('user.User_ID'), nullable=True)
    Sales_ID = db.Column(db.Integer, db.ForeignKey('sale.Sales_ID'), nullable=True)

# Esquemas
class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

class SaleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Sale
        load_instance = True

class ClientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Client
        load_instance = True

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class SupplierSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        load_instance = True

class SalesDetailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SalesDetail
        load_instance = True

class UserSaleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserSale
        load_instance = True

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Rutas CRUD para Product
@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(
        Name=data['Name'],
        Description=data.get('Description'),
        Price=data['Price'],
        Available_Quantity=data['Available_Quantity'],
        Location=data.get('Location'),
        Supplier_ID=data.get('Supplier_ID')
    )
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

@app.route('/product', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    product.Name = data.get('Name', product.Name)
    product.Description = data.get('Description', product.Description)
    product.Price = data.get('Price', product.Price)
    product.Available_Quantity = data.get('Available_Quantity', product.Available_Quantity)
    product.Location = data.get('Location', product.Location)
    product.Supplier_ID = data.get('Supplier_ID', product.Supplier_ID)
    db.session.commit()
    return product_schema.jsonify(product)

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
