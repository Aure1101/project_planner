# Colaborar en Github
## Clonar el repositori
Para descargar el repositorio a la computadora hay que ejecutar en el directorio donde vayan a trabajar el comando 

`git clone https://github.com/Aure1101/project_planner`

y luego hay que moverse a la carpeta generada, eso solo se hace la primera vez

## Actualizar el repo local

Antes de empezar a trabajar hay que asegurarse de que tenemos la version mas actualizada del repo, para esto ejecutamos

`git pull`

## Crear rama

Una vez actualizemos nos cambiamos a la rama `dev`, la rama main no la vamos a tocar hasta confirmar que todo funciona

`git checkout dev`

y ya estando en la rama `dev` creamos otra rama para trabajar

`git checkout -b <nombre de lo que estamos haciendo>`

## Subir la rama
una vez terminamos hacemos el commit, yo creo agregamos en el commit el nombre de la rama en la que trabajamos

`git add <archivo en el que trabajamos>`

`git commit -m <nombre de la rama>`

luego hacemos el push

`git push origin <nombre de la rama>`

## Solicitar Pull Request

Luego de subir la rama, hay que ir a github.com y hacer la solicitud de cambios, eso la verdad nunca lo he hecho, asi que les anexo el tutorial de gitub xD

https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request?tool=webui