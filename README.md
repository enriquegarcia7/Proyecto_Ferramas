<p align="center">
  <img width="180" src="AppFerreteria Frontend/static/images/icons/8.png">
</p>
<div align="center">
<!-- Download -->
<a href="https://github.com/enriquegarcia7/Proyecto_Ferramas">
   <img src="https://img.shields.io/badge/App-DOWNLOAD-green?logo=microsoftstore&logoColor=green">
  </a>
</div>


# APP FERRAMAS

FERRAMAS es un proyecto de e-commerce desarrollado en Django, que ofrece una experiencia de compra en línea dinámica y completa. Descubre una amplia variedad de productos, gestiona tus compras y maneja tu cuenta a tu gusto, todo en un sitio web intuitivo y fácil de usar.
<p align="center">
  <img width="600" src="AppFerreteria Frontend/static/images/icons/7.png">
</p>

## ¿En qué consiste?

Este proyecto es un e-commerce desarrollado en Django, un potente Framework de Python. El entorno virtual se ha configurado cuidadosamente para asegurar una experiencia de desarrollo óptima y segura. La tecnología utilizada incluye Python, JavaScript, HTML, Bootstrap/CSS, jQuery y PostgreSQL, contine tres APIs que se enlazan con el Banco Central, con PayPal y con la Base de Datos.

## Características destacadas

### Administrador

- **Agregar nuevos productos:** Incluye información detallada, como nombre, categoría, imagen, precio, stock y disponibilidad.
- **Gestionar reviews:** Visualiza el usuario que realizó la compra, su calificación, reseña y el producto evaluado.
- **Ver órdenes de productos:** Muestra el número de orden, nombre del cliente, teléfono, email, ciudad, costo total, impuestos, estado y fecha de la orden.
- **Acceder a información de pagos:** Incluye el usuario, PaymentID, método de pago, cantidad y estado de la transacción.
- **Visualizar productos solicitados:** Detalles como pago, costo, usuario y variaciones del producto.

### Categorías

- **Agregar nuevas categorías:** Clasifica productos y facilita la navegación y búsqueda de los usuarios.

### Carritos de compra

- **Acceso al carrito:** Identificado por un cartID único.
- **Sección "CartItems":** Muestra los productos seleccionados, el ID del carrito, la cantidad de cada producto y su disponibilidad.

### Gestión de cuentas

- **Sistema de grupos de Django:** Asigna roles con características específicas para el manejo del sistema.

### Usuarios

- **Perfiles de usuarios:** Contienen información relevante como imagen de perfil, nombre de usuario, país, ciudad y código postal.

### Cuentas

- **Información de cuentas:** Email, primer nombre, último nombre, nombre de usuario, última conexión, fecha de registro y estado de la cuenta (activa o pendiente de confirmación por correo).

## Ejecución

Es necesario tener instalados los requerimientos necesarios para ejecutarlo posteriormente con `python manage.py runserver` desde la terminal en el directorio de la carpeta clonada. Una vez realizado, abre `localhost:8000` para visualizar el sistema.

## Instalación

Para poder utilizar el proyecto o modificarlo puedes:

1. **Clonar el repositorio en tu máquina local:**
    ```bash
    git clone https://github.com/enriquegarcia7/Proyecto_Ferramas.git
    ```

2. **Crear un entorno virtual e instalar las dependencias necesarias:**
    ```bash
    cd ecommerce
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Configurar la base de datos y realizar las migraciones:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Ejecutar el servidor de desarrollo de Django:**
    ```bash
    python manage.py runserver
    ```

## Uso y cómo acceder al administrador

Para acceder al área de administración, sigue los siguientes pasos:

1. El sistema se maneja con `localhost:8000/securelogin`. Para acceder a la ventana de administrador, necesitas crear una cuenta desde la CMD o BASH utilizando:
    ```bash
    winpty python manage.py createsuperuser
    ```

## Ventanas del E-commerce

La mayoría de las ventanas se pueden acceder sin tener una cuenta, pero para comprar y ver pedidos es necesario crear una.

<p align="center">
  <img width="600" src="AppFerreteria Frontend/static/images/icons/5.png">
</p>
### Registro e Inicio de Sesión

El sistema ofrece a los usuarios la posibilidad de registrarse y crear una cuenta utilizando su correo electrónico de Gmail. La cuenta se verifica mediante un proceso de codificación en Base64 para mayor seguridad. Además, los usuarios registrados pueden iniciar sesión fácilmente para acceder a todas las funcionalidades del sitio.

### Sección de Olvidé mi Contraseña

En caso de que los usuarios olviden su contraseña, el e-commerce cuenta con una sección dedicada para restablecerla de forma segura. Los usuarios recibirán un correo electrónico con instrucciones para recuperar su contraseña y volver a acceder a su cuenta.

### Sección de Categorías

La navegación y búsqueda de productos se simplifica gracias a la sección de categorías. Los usuarios pueden explorar y filtrar productos por categorías específicas, lo que facilita la búsqueda de artículos de su interés.
<p align="center">
  <img width="600" src="AppFerreteria Frontend/static/images/icons/4.png">
</p>

### Apartado de Búsqueda de Productos

Para una experiencia de compra más ágil, el e-commerce proporciona un apartado de búsqueda de productos. Los usuarios pueden ingresar palabras clave y encontrar rápidamente los productos que desean comprar.

### Apartado de Mi Cuenta

Los usuarios tienen acceso a su área personal a través del apartado "Mi Cuenta". Aquí, pueden ver el historial de sus pedidos, revisar sus órdenes de compra anteriores, cambiar su contraseña para garantizar la seguridad y editar su perfil para mantener su información actualizada.
<p align="center">
  <img width="600" src="AppFerreteria Frontend/static/images/icons/2.png">
</p>

### Carrito

El carrito de compra es una funcionalidad esencial en el e-commerce. Los usuarios pueden agregar productos seleccionados a su carrito, ver el resumen de sus compras y ajustar las cantidades antes de proceder al pago.
<p align="center">
  <img width="600" src="AppFerreteria Frontend/static/images/icons/3.png">
</p>

### Dirección de Envío

Antes de finalizar la compra, los usuarios pueden proporcionar y verificar su dirección de envío para garantizar que los productos sean entregados correctamente.

<p align="center">
  <img width="600" src="AppFerreteria Frontend/static/images/icons/1.png">
</p>

### Pagar

El proceso de pago se lleva a cabo en una ventana dedicada, donde los usuarios pueden seleccionar el método de pago preferido y completar la transacción de forma segura.

### Ventana de Venta Exitosa

Una vez completada la transacción, los usuarios recibirán una ventana de venta exitosa que confirmará su compra y proporcionará detalles importantes, como el número de orden y la fecha estimada de entrega.


