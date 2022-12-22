![hunty-logo](/media/GF-Logo.png)
# gigflow_challenge
Desafio de BackEnd Gigflow - Yeison Arias


## Requisitos Previos

Necesitará:

- `python 3.9`
- `postgres >= 11`

Seleccione un método de ejecución:
- (Recomendado) `docker` con [versión al menos](https://docs.docker.com/compose/compose-file/#compose-and-docker-compatibility-matrix) `19.03`
- Entorno local con linux o WSL
- Si está utilizando `docker`, asegúrese de utilizar las siguientes versiones:
  - `Docker >=  20.10.21`
  - `Docker Compose >=  2.13.0`

## Entorno de desarrollo local

##### Crear un entorno virtual
- Instalar virtualenv
```console
python -m pip install virtualenv
```
- Crear entorno virtual
```console
virtualenv venv
```

- Activar entorno virtual

Para linux
```console
source bin/activate
```

Windows - powershell
```console
.\Scripts\activate
```
[Otros activadores](https://virtualenv.pypa.io/en/latest/user_guide.html#activators)

- Instalar paquetes requeridos  
```console
pip install -r requirements.txt
```

- Iniciar el servidor Django
```console
python manage.py runserver 0.0.0.0:8080
```

### Docker

#### Crea contenedores y reconstruye las imágenes.

Linux
```console
sudo docker-compose up --build
```

Windows
```console
docker compose up --build
```

## Documentación

### Crear y configurar archivo de entorno

#### Por favor creé un nuevo archivo en la raíz del proyecto llamado `.env`, luego pegue la configuración por defecto que se encuentra en el archivo `.env.template` y cambie las variables de entorno según sus necesidades.

Puede utilizar el siguiente comando para Linux
```console
sudo cp .env.template .env
```

### Migración de base de datos

#### Si está utilizando `docker`, debe ingresar al contenedor con el siguiente comando:
```console
docker-compose exec web bash
```

#### Utilice el siguiente comando para realizar la migración de la base de datos:
```console
python manage.py migrate
```

#### Diagrama entidad relación resultado
![hunty-logo](/media/ER.png)

### Seeder
- Puede alimentar su base de datos con datos de prueba desde la línea de comando usando el comando:
```console
python manage.py seed --seeds 50
```
<sup>El comando anterior poblará el modelo service_type con la cantidad solicitada(50 registros por defecto), el modelo package con 3 paquetes para cada tipo de servicio y el modelo deliverable con 3 entregables para cada paquete.</sup>

### Documentación de los endpoints con Postman
<sup>Importante: Se utilizó la version v2.1 para exportar la colección desde el software postman.</sup>
- En la carpeta `/collections/service` encontrará la colección de Postman para llevar a cabo pruebas a los Endpoints del proyecto.
- Por favor, previamente debe configurar un entorno dentro del software Postman para configurar las variables requeridas para su correcto funcionamiento.
  - Para crear el entorno puede llevar a cabo los siguientes pasos:
  
![hunty-logo](/media/Postman_1.png)

  1. Diríjase a la pestaña `Enviroments`.
  2. Agregue un nuevo entorno seleccionando el signo más `+` y defina un nombre de su preferencia.
  3. Agregue una nueva variable llamada `DOMAIN`, para esta nueva variable defina el valor de `INITIAL VALUE` en `http://localhost:8000`.
  4. Ya puede seleccionar el nuevo entorno como el entorno por defecto dentro de postman.

### Pruebas unitarias
- En la carpeta `/test` puede encontrar las pruebas unitarias empleadas para probar los endpoints principales de Service.
- La cobertura final de las pruebas es del 97%.

![hunty-logo](/media/Test.png)
