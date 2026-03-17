# *Proyecto Urban Routes*

Este proyecto contiene pruebas automatizadas para la aplicación web Urban Routes, una plataforma de solicitud de taxis.

## Descripción
Urban Routes es una aplicación web que permite a los usuarios solicitar servicios de taxi de manera sencilla. Este proyecto implementa un conjunto completo de pruebas automatizadas que verifican el flujo completo de solicitud de un taxi, desde la configuración de direcciones hasta la confirmación del pedido.
### **_Funcionalidades probadas:_**
- Configuración de direcciones de origen y destino.
- Selección de tarifa Comfort.
- Registro y validación de número de teléfono.
- Agregado de tarjeta de crédito como método de pago.
- Envío de mensajes al conductor.
- Solicitud de servicios adicionales (manta, pañuelos, helados).
- Confirmación de solicitud de taxi.
- Verificación de asignación de conductor.

## Tecnologías y Herramientas utilizadas
- **Python** 
  - Como lenguaje principal de programación.
- **Selenium WebDriver** 
  - Como herramienta de automatización para las pruebas.
- **ChromeDriver (WebDriver para Chrome)** 
  - Como el navegador específico para ejecutar las pruebas.
- **DevTools**
  - Para inspección de elementos y análisis de funcionalidades web.

## Requisitos Previos
Antes de ejecutar las pruebas, asegúrate de tener instalado:

- **Python 3.7 o superior**
- **Google Chrome** (versión actualizada)
- **ChromeDriver** compatible con tu versión de Chrome
- **Selenium WebDriver** para Python

## Instalación

1. **Clona o descarga el proyecto** en tu máquina local

2. **Instala las dependencias necesarias:**
   ```bash
   pip install selenium
   ```
3. **Descarga ChromeDriver** 
- Ve a https://googlechromelabs.github.io/chrome-for-testing/
- Descarga la versión compatible con tu Chrome.
- Coloca el archivo en tu PATH del sistema

## Cómo ejecutar las pruebas

1. **Abre una terminal** en el directorio del proyecto

2. **Ejecuta el archivo principal de pruebas:**
   ```bash
   python test_urban_routes.py
   ```
   
## Resultados Esperados
Al ejecutar las pruebas exitosamente, deberías ver:
- Apertura automática del navegador Chrome.
- Ejecución secuencial de todas las funcionalidades.
- Confirmación de solicitud de taxi completada.