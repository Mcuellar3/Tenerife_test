# Prueba práctica
 
 * El módulo fue creado para ser utilizado en la version Community de Odoo 17
 * El ambiente de desarrollo se levantó usando Docker, se subirán los archivos en dado caso que lo necesiten replicar

INSTALACIÓN

El módulo ya tiene en el manifest las dependencias que necesita.
debe ir a Aplicaciones, Actualizar la lista de aplicaciones y Activar el módulo de "tenerife_test"
se recomienda usar una base de datos  que ya tenga infromación para poder revisar todas la funcionalidades

* Para el punto número 1 entra a la vista de prodcut.template y tendrá el smart button.
* Para el punto número 2 Entra a ventas, el submenú de prodcutos y verá la opción "Asignar Etiquetas Masivas" allí seleccionar lso rpdcutos y las etiquetas que necesite.
* Para el punto número 3 en prodcut.template se agregó un grupo donde puede ver el campo M2M para las etiquetas.
* Para el punto número 4 en prodcut.template se agregó un campo para la descipoción breve, en al parte superior debe hacer click en Acciones y en Reporte de Prodcuto.



Dockerfile

*FROM odoo:17

*USER root
*RUN apt-get update -y
*RUN apt-get upgrade -y
*RUN pip3 install xmltodict
*RUN pip3 install ipdb
*RUN apt-get install python3-openssl -y
*RUN pip3 install odoo-test-helper
