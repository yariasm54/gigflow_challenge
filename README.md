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

## Entorno de desarrollo

- Crear un entorno virtual
```console
# Instalar virtualenv
python -m pip install virtualenv
# Crear entorno virtual
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

#### Por favor creé un nuevo archivo en la raíz del proyecto llamado .env, luego pegue la configuración por defecto que se encuentra en el archivo .env.template y cambie las variables de entorno según sus necesidades.

Puede utilizar el siguiente comando para Linux
```console
sudo cp .env.template .env
```

### Migración de base de datos

#### Utilice el siguiente comando para realizar la migración de la base de datos:
```console
python manage.py migrate
```
#### Si está utilizando `docker`, previamente debe ingresar al contenedor con el siguiente comando:
```console
docker-compose exec web bash
```
