# Algoritmo de Identificación de Números Primos  

Este software está disponible bajo una licencia dual:  

## Uso Académico  
- Gratuito bajo los términos de la Licencia Pública General GNU (GPL) versión 3.  
- Ver LICENSE_GPL.txt para más detalles.  

## Uso Comercial  
- Requiere un acuerdo de licencia específico y el pago de royalties.
- Ver LICENSE_COMMERCIAL.txt para más detalles.  
- Para solicitar una licencia comercial, contacte a:  
  - Nombre: José Ignacio Peinador Sala  
  - Email: [joseignacio.peinador@gmail.com]  
  - Teléfono: [+34 652458171]  


## Instrucciones de Uso

### 1. Requisitos Previos
Asegúrate de tener instalado Python 3.8 o superior. Puedes descargarlo desde [python.org](https://www.python.org/).

### 2. Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio


2. Ejecución del Algoritmo
Abre el archivo algoritmo.py

Configura k_max (el límite superior para k):

python
Copy
if __name__ == "__main__":
    k_max = 1000000  # Cambia este valor según tus necesidades
Ejecuta el script:

bash
python src/algoritmo.py

3. Personalización
Cambia el valor de k_max para ajustar el rango de búsqueda.

Añade más primos base editando la función inicializar_primos_base.

4. Ejemplo de Salida
Copy
k=1, 6k -1 = 5: PRIMO ✅ (k_min=4)
k=1, 6k +1 = 7: PRIMO ✅ (k_min=8)
...
k=100, 6k -1 = 599: COMPUESTO 🚫
k=100, 6k +1 = 601: PRIMO ✅ (k_min=602 > 100, NO SE AÑADE)

Resumen Final:
Total de Primos: 108
Total de Compuestos: 92
Condiciones iniciales: 6
Condiciones finales: 7
Condiciones utilizadas (k_min <= 100): 7
Condiciones utilizadas (n <= 601): 9 = 7 + 2 (añadiendo los primos 2 y 3)

5. Uso en Proyectos Académicos
Cita este repositorio en tus publicaciones:

Peinador Sala, J. I. (2023). Algoritmo de Identificación de Números Primos. Disponible en: https://github.com/tu_usuario/tu_repositorio

6. Uso Comercial
Contacta al autor para obtener una licencia comercial.

7. Contribuciones
Haz un fork del repositorio.

Crea una rama con tu contribución:

bash
Copy
git checkout -b mi_contribucion
Envía un pull request.

8. Soporte
Para reportar errores o hacer preguntas, abre un issue o contacta al autor en [joseignacio.peinador@gamil.com]

## Créditos  
Este proyecto contó con la asistencia de DeepSeek Chat, un modelo de inteligencia artificial desarrollado por DeepSeek, para la implementación del algoritmo, pruebas empíricas y redacción de documentación.
