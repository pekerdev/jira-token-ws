# jira-token-ws
Servidor para exposición de Jira Token via webservice con autenticación

Debido a que Jira te deja utilizar el token durante 365 dias, para automatizar tareas de creación de tickets automáticas ante fallas de tarea se creó este webservice para recuperar de manera el token para creación de tickets.
El token debe pertenecer a un usuario con los permisos bien definidos.

Este docker-compose expone en http un nginx sirviendo un flask por detrás.

Por tu cuenta lo metés en un reverse_proxy para darle https con otro nginx proxy que tengas.
