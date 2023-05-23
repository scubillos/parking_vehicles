
# Parking Vehicles - ArchiPlus

## Compilacion
1. Clonar este repositorio.
2. Ubicarse en una terminal en el proyecto clonado.
3. Ejecutar `docker build . -t archiplus/parking-vehicles`
4. Verficar imagen creada `docker image ls`


## Instalación con docker compose
1. Clonar este repositorio.
2. Ubicarse en una terminal en el proyecto clonado.
3. Ejecutar `docker compose build`
4. Ejecutar `docker compose up -d`
5. Listo 

**Nota:** Asegurarse de que el puerto *8001* se encuentre libre antes de ejecutar el paso 4.

## Despliegue con Kubernetes
1. Clonar este repositorio.
2. Ubicarse en una terminal en el proyecto clonado.
3. Ejecutar `docker build . -t archiplus/parking-vehicles`
4. Solo en K3S `docker save archiplus/parking-vehicles | sudo k3s ctr images import -`
5. Ejecutar `kubectl apply -f mysql-pv.yml`
6. Ejecutar `kubectl apply -f parking-vehicles.yml`
7. Listo

## Tecnologías
- Python3
- MySQL 5.7
- Kubernetes
- Docker

## Postman
La colección de postman con los servicios GET y POST es el archivo ***parking.vehicles.postman_collection.json***.

## Jmeter
You are going to find a file with name "Test-Plan.jmx" to use it you need to have
the application jmeter configured in your machine.
Into the create user thread you can change the defauld values to simulate the user concurrency 
period and anothers things.
The request are configureted to generate the random values to create users
Also we have some validations to make sure the follow designed is running such as we are expected

If you deploy the application with K3s you have to change into the file "GeneralVariables" the variable endPoint by "http:/localhost" if you deploy with docker the solution you won't have problems with the defaul end Point value because is configurated "http:/localhost:3000"
