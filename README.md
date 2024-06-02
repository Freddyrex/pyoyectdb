# PUNTO DE VENTA
En este repositorio se encuentra un proyecto de un punto de venta el cual fue diseñado para resolver una problematica de la materia de Base de datos, este proyecto se encuentra programado en HTML, CSS, javascrip y python.


En el documento "api.py" se encuentra la api con actualmente todos los metodos implementados.
El modelo logico de la base de datos se encuentra adjunto en el aechivo "modelo logico_page-0001.jpg".
Dentro de la carpeta "ejemplo interface" se encuentra una demo de como sera la pagina web del punto de venta se encuentran implementadas varias de las funcionalidades.

#Esquema de base de datos

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

## Tabla: Sale

| Campo       | Tipo       | Restricciones            |
|-------------|------------|---------------------------|
| Sales_ID    | INT        | PRIMARY KEY               |
| Date        | DATE       | NOT NULL                  |
| Total       | DECIMAL(10, 2) | NOT NULL                |
| Client_ID   | INT        |                           |
| FOREIGN KEY (Client_ID) | REFERENCIAS Client(Client_ID) |

## Tabla: Client

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

## Tabla: Supplier

| Campo        | Tipo         | Restricciones        |
|--------------|--------------|-----------------------|
| Supplier_ID  | INT          | PRIMARY KEY           |
| Name         | VARCHAR(255) | NOT NULL              |
| Address      | VARCHAR(255) |                       |
| Telephone    | VARCHAR(20)  |                       |
| Email        | VARCHAR(255) |                       |

## Tabla: SalesDetail

| Campo           | Tipo         | Restricciones            |
|-----------------|--------------|---------------------------|
| SalesDetail_ID  | INT          | PRIMARY KEY               |
| Sales_ID        | INT          |                           |
| Product_ID      | INT          |                           |
| Quantity        | INT          | NOT NULL                  |
| Unit_Price      | DECIMAL(10, 2) | NOT NULL                |
| FOREIGN KEY (Sales_ID)   | REFERENCIAS Sale(Sales_ID)     |
| FOREIGN KEY (Product_ID) | REFERENCIAS Product(Product_ID) |

## Tabla: UserSale

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
