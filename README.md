# automation-flink

Para ejecutar el proyecto desde su maquina, debe de abrir la consola de PowerSell y ejecutar el comando:
behave -f allure_behave.formatter:AllureFormatter -o src\allure-results src/features/pruebaFlink.feature --tags=@Prueba_Saucedemo

1.- Debe de tener instalada la libreria de allure para que el comando pueda ejecutarse correctamente.
2.- Dentro de PowerSell debe de ubicarse en la ruta donde haya guardado el proyecto.
3.- Ejemplo de como ejecutarlo una vez ubicado en la ruta:
C:\prueba-automation-flink> behave -f allure_behave.formatter:AllureFormatter -o src\allure-results src/features/pruebaFlink.feature --tags=@Prueba_Saucedemo

Una vez ejecutado el proyecto debe de ejecutar el comando allure serve C:\prueba-automation-flink 

1.- Ir a la carpeta src\allure-results que se encuentra dentro de la carpeta del proyecto.
2.- Abrir el archivo JSON


Evidencia de ejecución de proyecto y reporte: https://drive.google.com/file/d/11zbeMpJGq0lG8dVQVxIHHhIOqGQwXsB_/view?usp=sharing 
