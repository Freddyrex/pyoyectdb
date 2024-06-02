# P*UNTO DE VENT*A

En este repositorio se aloja un proyecto de un punto de venta diseñado para abordar una problemática de la materia de Base de Datos. Este proyecto está programado utilizando HTML, CSS, JavaScript y Python.
Dentro del archivo "api.py" se encuentra la API con todos los métodos actualmente implementados. El modelo lógico de la base de datos está adjunto en el archivo "modelo_logico_page-0001.jpg". Además, en la carpeta "ejemplo_interface" se encuentra una demostración de cómo será la página web del punto de venta, donde se han implementado varias de las funcionalidades.

## Esquema de base de datos

| Campo              | Tipo              | Restricciones              |
|--------------------|-------------------|-----------------------------|
| Product_ID         | INT               | PRIMARY KEY                 |
| Name               | VARCHAR(255)      | NOT NULL                    |
| Description        | TEXT              |                             |
| Price              | DECIMAL(10, 2)    | NOT NULL                    |
| Available_Quantity | INT               | NOT NULL                    |
| Location           | VARCHAR(255)      |                             |
| Supplier_ID        | INT               |                             |
| FOREIGN KEY (Supplier_ID) | REFERENCIAS Supplier(Supplier_ID) |

### Tabla: Sale

| Campo       | Tipo       | Restricciones            |
|-------------|------------|---------------------------|
| Sales_ID    | INT        | PRIMARY KEY               |
| Date        | DATE       | NOT NULL                  |
| Total       | DECIMAL(10, 2) | NOT NULL                |
| Client_ID   | INT        |                           |
| FOREIGN KEY (Client_ID) | REFERENCIAS Client(Client_ID) |

### Tabla: Client

| Campo      | Tipo         | Restricciones        |
|------------|--------------|-----------------------|
| Client_ID  | INT          | PRIMARY KEY           |
| Name       | VARCHAR(255) | NOT NULL              |
| Address    | VARCHAR(255) |                       |
| Email      | VARCHAR(255) |                       |
| Telephone  | VARCHAR(20)  |                       |

## Tabla: User

| Campo      | Tipo         | Restricciones        |
|------------|--------------|-----------------------|
| User_ID    | INT          | PRIMARY KEY           |
| User_Name  | VARCHAR(255) | NOT NULL              |
| Password   | VARCHAR(255) | NOT NULL              |
| Role       | VARCHAR(50)  |                       |

### Tabla: Supplier

| Campo        | Tipo         | Restricciones        |
|--------------|--------------|-----------------------|
| Supplier_ID  | INT          | PRIMARY KEY           |
| Name         | VARCHAR(255) | NOT NULL              |
| Address      | VARCHAR(255) |                       |
| Telephone    | VARCHAR(20)  |                       |
| Email        | VARCHAR(255) |                       |

### Tabla: SalesDetail

| Campo           | Tipo         | Restricciones            |
|-----------------|--------------|---------------------------|
| SalesDetail_ID  | INT          | PRIMARY KEY               |
| Sales_ID        | INT          |                           |
| Product_ID      | INT          |                           |
| Quantity        | INT          | NOT NULL                  |
| Unit_Price      | DECIMAL(10, 2) | NOT NULL                |
| FOREIGN KEY (Sales_ID)   | REFERENCIAS Sale(Sales_ID)     |
| FOREIGN KEY (Product_ID) | REFERENCIAS Product(Product_ID) |

### Tabla: UserSale

| Campo       | Tipo       | Restricciones            |
|-------------|------------|---------------------------|
| UserSale_ID | INT        | PRIMARY KEY               |
| User_ID     | INT        |                           |
| Sales_ID    | INT        |                           |
| FOREIGN KEY (User_ID)  | REFERENCIAS User(User_ID)      |
| FOREIGN KEY (Sales_ID) | REFERENCIAS Sale(Sales_ID)     |

───────────────────────────────────────
───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────
───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────
──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────
▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────
─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────
─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────
──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────
────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────
