# automation-flink

Para ejecutar el proyecto desde su maquina, debe de abrir la consola de PowerSell y ejecutar el comando:
behave -f allure_behave.formatter:AllureFormatter -o src\allure-results src/features/pruebaFlink.feature --tags=@Prueba_Saucedemo

1.- Debe de tener instalada la libreria de allure para que el comando pueda ejecutar se correctamente.
2.- Dentro de PowerSell debe de ubicarse en la ruta donde haya guardado el proyecto.
3.- Ejemplo de como ejecutarlo una vez ubicado en la ruta:
C:\prueba-automation-flink> behave -f allure_behave.formatter:AllureFormatter -o src\allure-results src/features/pruebaFlink.feature --tags=@Prueba_Saucedemo

Para ejecutar el reporte en una vista grafica debe de ejecutar se debe el comando: allure serve C:\prueba-automation-flink\src\allure-results  
Al terminar se de ejecutar el comando se abrira en el browser el reporte generado por allure el cual puede ser comartido y leido por cualquier persona.
1.- Ejemplo de como ejecutar el reporte:  C:\prueba-automation-flink> allure serve C:\prueba-automation-flink\src\allure-results 
2.- Resultado del reporte: http://192.168.1.81:60093/index.html# 

Tambien puede abrir el .json qeu se encuentra (opcional).
1.- Ir a la carpeta src\allure-results que se encuentra dentro de la carpeta del proyecto.
2.- Abrir el archivo JSON


Evidencia de ejecución de proyecto y reporte: https://drive.google.com/file/d/11zbeMpJGq0lG8dVQVxIHHhIOqGQwXsB_/view?usp=sharing 
