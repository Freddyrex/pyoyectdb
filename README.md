# P*UNTO DE VENT*A

Este proyecto es un sistema de gestión de ventas desarrollado para permitir a los usuarios administrar las ventas de una tienda o negocio de manera eficiente. Proporciona funcionalidades para agregar nuevas ventas, ver ventas existentes y eliminar ventas según sea necesario.

### Características
- Agregar nuevas ventas con información detallada, incluyendo fecha, total y cliente asociado.
- Ver una lista de todas las ventas registradas en la base de datos.
- Eliminar ventas específicas según la necesidad del usuario.

## Uso

### Para utilizar este proyecto, sigue estos pasos:

Clona el repositorio a tu máquina local utilizando el siguiente comando:

bash
Copiar código
git clone https://github.com/tuusuario/sistema-gestion-ventas.git
Abre el proyecto en tu editor de código preferido.

Configura el servidor de backend (no incluido en este repositorio) que proporcionará los endpoints necesarios para la comunicación del frontend con la base de datos. Asegúrate de tener las rutas correctas para agregar, ver y eliminar ventas.

Abre el archivo index.html en tu navegador web para acceder al sistema de gestión de ventas.

Utiliza el sistema para agregar nuevas ventas, ver las existentes y eliminarlas según sea necesario.

## Tecnologías Utilizadas
HTML
CSS
JavaScript

Para poder usar este proyecto se debe berificar el puerto de salida de la api y el de la base de datos para permiter una correcta comunicacion entre las dos ademas de instalar todas las dependiencias que usa nuestra api

## Resumen
Este repositorio contiene un proyecto de punto de venta diseñado para abordar una problemática de la materia de Base de Datos. Está programado en HTML, CSS, JavaScript y Python. Incluye una API en "[api.py](https://github.com/Freddyrex/pyoyectdb/blob/main/api.py)" con los métodos implementados, el modelo lógico de la base de datos en "[modelo_logico_page-0001.jpg](https://github.com/Freddyrex/pyoyectdb/blob/main/modelo%20logico_page-0001.jpg)" y una demostración de la interfaz en la carpeta "[ejemplo_interface](https://github.com/Freddyrex/pyoyectdb/tree/main/ejemplo_interface)".

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


## Créditos
Este proyecto fue desarrollado por Tu "[Freddy Valenzuela](https://github.com/Freddyrex)".
