from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow.fields import Integer
from marshmallow import fields
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:3355@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos
class Product(db.Model):
    __tablename__ = 'product'
    Product_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.Text, nullable=True)
    Price = db.Column(db.Numeric(10, 2), nullable=False)
    Available_Quantity = db.Column(db.Integer, nullable=False)
    Location = db.Column(db.String(255), nullable=True)
    Supplier_ID = db.Column(db.Integer, db.ForeignKey('supplier.Supplier_ID', name='product_supplier_fk'), nullable=True)
    supplier = db.relationship('Supplier', backref='products')

class Sale(db.Model):
    __tablename__ = 'sale'
    Sales_ID = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    Total = db.Column(db.Numeric(10, 2), nullable=False)
    Client_ID = db.Column(db.Integer, db.ForeignKey('client.Client_ID', name='sale_client_fk'), nullable=True)
    client = db.relationship('Client', backref='sales')

class Client(db.Model):
    __tablename__ = 'client'
    Client_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255), nullable=True)
    Email = db.Column(db.String(255), nullable=True)
    Telephone = db.Column(db.String(20), nullable=True)

class User(db.Model):
    __tablename__ = 'user'
    User_ID = db.Column(db.Integer, primary_key=True)
    User_Name = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Role = db.Column(db.String(50), nullable=True)

class Supplier(db.Model):
    __tablename__ = 'supplier'
    Supplier_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255), nullable=True)
    Telephone = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(255), nullable=True)

class SalesDetail(db.Model):
    __tablename__ = 'sales_detail'
    SalesDetail_ID = db.Column(db.Integer, primary_key=True)
    Sales_ID = db.Column(db.Integer, db.ForeignKey('sale.Sales_ID', name='sales_detail_sale_fk'), nullable=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey('product.Product_ID', name='sales_detail_product_fk'), nullable=True)
    Quantity = db.Column(db.Integer, nullable=False)
    Unit_Price = db.Column(db.Numeric(10, 2), nullable=False)

class UserSale(db.Model):
    __tablename__ = 'user_sale'
    UserSale_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('user.User_ID', name='user_sale_user_fk'), nullable=True)
    Sales_ID = db.Column(db.Integer, db.ForeignKey('sale.Sales_ID', name='user_sale_sale_fk'), nullable=True)

# Esquemas
class ProductSchema(SQLAlchemyAutoSchema):
    Supplier_ID = Integer()  # Usamos Integer directamente
    class Meta:
        model = Product
        load_instance = True

class SaleSchema(SQLAlchemyAutoSchema):
        Client_ID = Integer()  # Usamos Integer directamente
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
    Sales_ID = Integer()
    Product_ID = Integer()
    Unit_Price = fields.Decimal(as_string=True)
    class Meta:
        model = SalesDetail
        load_instance = True

class UserSaleSchema(SQLAlchemyAutoSchema):
    User_ID = Integer()
    Sales_ID = Integer()
    class Meta:
        model = UserSale
        load_instance = True

# Inicializar esquemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
sale_schema = SaleSchema()
sales_schema = SaleSchema(many=True)
client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)
sales_detail_schema = SalesDetailSchema()
sales_details_schema = SalesDetailSchema(many=True)
user_sale_schema = UserSaleSchema()
user_sales_schema = UserSaleSchema(many=True)

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Rutas CRUD para Product
@app.route('/product', methods=['POST'])
def add_product():
    try:
        data = request.json
        supplier_id = data.get('Supplier_ID')
        if supplier_id is not None:
            supplier = Supplier.query.get(supplier_id)
            if not supplier:
                return jsonify({'error': 'Supplier_ID does not exist'}), 400
        
        new_product = Product(
            Name=data['Name'],
            Description=data.get('Description'),
            Price=data['Price'],
            Available_Quantity=data['Available_Quantity'],
            Location=data.get('Location'),
            Supplier_ID=supplier_id
        )
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

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
    try:
        product = Product.query.get_or_404(id)
        data = request.json
        supplier_id = data.get('Supplier_ID')
        if supplier_id is not None:
            supplier = Supplier.query.get(supplier_id)
            if not supplier:
                return jsonify({'error': 'Supplier_ID does not exist'}), 400

        product.Name = data.get('Name', product.Name)
        product.Description = data.get('Description', product.Description)
        product.Price = data.get('Price', product.Price)
        product.Available_Quantity = data.get('Available_Quantity', product.Available_Quantity)
        product.Location = data.get('Location', product.Location)
        product.Supplier_ID = supplier_id if supplier_id is not None else product.Supplier_ID
        
        db.session.commit()
        return product_schema.jsonify(product)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

# Rutas CRUD para Sale
@app.route('/sale', methods=['POST'])
def add_sale():
    try:
        data = request.json
        new_sale = Sale(
            Date=data['Date'],
            Total=data['Total'],
            Client_ID=data.get('Client_ID')
        )
        db.session.add(new_sale)
        db.session.commit()
        return sale_schema.jsonify(new_sale), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/sale', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    return sales_schema.jsonify(sales)

@app.route('/sale/<int:id>', methods=['GET'])
def get_sale(id):
    sale = Sale.query.get_or_404(id)
    return sale_schema.jsonify(sale)

@app.route('/sale/<int:id>', methods=['PUT'])
def update_sale(id):
    try:
        sale = Sale.query.get_or_404(id)
        data = request.json
        sale.Date = data.get('Date', sale.Date)
        sale.Total = data.get('Total', sale.Total)
        sale.Client_ID = data.get('Client_ID', sale.Client_ID)
        db.session.commit()
        return sale_schema.jsonify(sale)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/sale/<int:id>', methods=['DELETE'])
def delete_sale(id):
    sale = Sale.query.get_or_404(id)
    db.session.delete(sale)
    db.session.commit()
    return jsonify({'message': 'Sale deleted successfully'}), 204

# Rutas CRUD para SalesDetail
@app.route('/salesdetail', methods=['POST'])
def add_sales_detail():
    try:
        data = request.json
        new_sales_detail = SalesDetail(
            Sales_ID=data['Sales_ID'],
            Product_ID=data['Product_ID'],
            Quantity=data['Quantity'],
            Unit_Price=data['Unit_Price']
        )
        db.session.add(new_sales_detail)
        db.session.commit()
        return sales_detail_schema.jsonify(new_sales_detail), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/salesdetail', methods=['GET'])
def get_sales_details():
    sales_details = SalesDetail.query.all()
    return sales_details_schema.jsonify(sales_details)

@app.route('/salesdetail/<int:id>', methods=['GET'])
def get_sales_detail(id):
    sales_detail = SalesDetail.query.get_or_404(id)
    return sales_detail_schema.jsonify(sales_detail)

@app.route('/salesdetail/<int:id>', methods=['PUT'])
def update_sales_detail(id):
    try:
        sales_detail = SalesDetail.query.get_or_404(id)
        data = request.json
        sales_detail.Sales_ID = data.get('Sales_ID', sales_detail.Sales_ID)
        sales_detail.Product_ID = data.get('Product_ID', sales_detail.Product_ID)
        sales_detail.Quantity = data.get('Quantity', sales_detail.Quantity)
        sales_detail.Unit_Price = data.get('Unit_Price', sales_detail.Unit_Price)
        db.session.commit()
        return sales_detail_schema.jsonify(sales_detail)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/salesdetail/<int:id>', methods=['DELETE'])
def delete_sales_detail(id):
    sales_detail = SalesDetail.query.get_or_404(id)
    db.session.delete(sales_detail)
    db.session.commit()
    return jsonify({'message': 'Sales detail deleted successfully'}), 204

# Rutas CRUD para Client
@app.route('/client', methods=['POST'])
def add_client():
    try:
        data = request.json
        new_client = Client(
            Name=data['Name'],
            Address=data.get('Address'),
            Email=data.get('Email'),
            Telephone=data.get('Telephone')
        )
        db.session.add(new_client)
        db.session.commit()
        return client_schema.jsonify(new_client), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/client', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return clients_schema.jsonify(clients)

@app.route('/client/<int:id>', methods=['GET'])
def get_client(id):
    client = Client.query.get_or_404(id)
    return client_schema.jsonify(client)

@app.route('/client/<int:id>', methods=['PUT'])
def update_client(id):
    try:
        client = Client.query.get_or_404(id)
        data = request.json
        client.Name = data.get('Name', client.Name)
        client.Address = data.get('Address', client.Address)
        client.Email = data.get('Email', client.Email)
        client.Telephone = data.get('Telephone', client.Telephone)
        db.session.commit()
        return client_schema.jsonify(client)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/client/<int:id>', methods=['DELETE'])
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Client deleted successfully'}), 204

# Rutas CRUD para User
@app.route('/user', methods=['POST'])
def add_user():
    try:
        data = request.json
        new_user = User(
            User_Name=data['User_Name'],
            Password=data['Password'],
            Role=data.get('Role')
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get_or_404(id)
        data = request.json
        user.User_Name = data.get('User_Name', user.User_Name)
        user.Password = data.get('Password', user.Password)
        user.Role = data.get('Role', user.Role)
        db.session.commit()
        return user_schema.jsonify(user)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 204

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(User_Name=username).first()

        if user and user.Password == password:
            return jsonify({'success': True}), 200
        else:
            return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rutas CRUD para Supplier
@app.route('/supplier', methods=['POST'])
def add_supplier():
    try:
        data = request.json
        new_supplier = Supplier(
            Name=data['Name'],
            Address=data.get('Address'),
            Telephone=data.get('Telephone'),
            Email=data.get('Email')
        )
        db.session.add(new_supplier)
        db.session.commit()
        return supplier_schema.jsonify(new_supplier), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/supplier', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    return suppliers_schema.jsonify(suppliers)

@app.route('/supplier/<int:id>', methods=['GET'])
def get_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    return supplier_schema.jsonify(supplier)

@app.route('/supplier/<int:id>', methods=['PUT'])
def update_supplier(id):
    try:
        supplier = Supplier.query.get_or_404(id)
        data = request.json
        supplier.Name = data.get('Name', supplier.Name)
        supplier.Address = data.get('Address', supplier.Address)
        supplier.Telephone = data.get('Telephone', supplier.Telephone)
        supplier.Email = data.get('Email', supplier.Email)
        db.session.commit()
        return supplier_schema.jsonify(supplier)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/supplier/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    db.session.delete(supplier)
    db.session.commit()
    return jsonify({'message': 'Supplier deleted successfully'}), 204

# Rutas CRUD para UserSale
@app.route('/usersale', methods=['POST'])
def add_user_sale():
    try:
        data = request.json
        new_user_sale = UserSale(
            User_ID=data['User_ID'],
            Sales_ID=data['Sales_ID']
        )
        db.session.add(new_user_sale)
        db.session.commit()
        return user_sale_schema.jsonify(new_user_sale), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/usersale', methods=['GET'])
def get_user_sales():
    user_sales = UserSale.query.all()
    return user_sales_schema.jsonify(user_sales)

@app.route('/usersale/<int:id>', methods=['GET'])
def get_user_sale(id):
    user_sale = UserSale.query.get_or_404(id)
    return user_sale_schema.jsonify(user_sale)

@app.route('/usersale/<int:id>', methods=['PUT'])
def update_user_sale(id):
    try:
        user_sale = UserSale.query.get_or_404(id)
        data = request.json
        user_sale.User_ID = data.get('User_ID', user_sale.User_ID)
        user_sale.Sales_ID = data.get('Sales_ID', user_sale.Sales_ID)
        db.session.commit()
        return user_sale_schema.jsonify(user_sale)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/usersale/<int:id>', methods=['DELETE'])
def delete_user_sale(id):
    user_sale = UserSale.query.get_or_404(id)
    db.session.delete(user_sale)
    db.session.commit()
    return jsonify({'message': 'UserSale deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)


