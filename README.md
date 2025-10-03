# TestAutomationDemo# TestAutomationDemo

Automatización de pruebas de interfaz web usando **Selenium** junto con **Behave** (BDD) en Python.

---

## 📖 Descripción

Este proyecto es un ejemplo (“demo”) de framework de **automatización de pruebas web** usando:

* **Selenium WebDriver** para interactuar con el navegador
* **Behave** como motor BDD (Behavior-Driven Development) para definir escenarios en lenguaje natural (Gherkin)
* Python como lenguaje principal

Permite escribir escenarios en formato `*.feature` que describen comportamientos esperados y luego ejecutarlos mediante definiciones de pasos que abren un navegador, interactúan con elementos y validan resultados.

---

## 🛠 Tecnologías

* Python 3.8+
* Selenium
* Behave
* WebDriver (ChromeDriver, GeckoDriver, etc.)
* Dependencias en `requirements.txt`

---

## ✅ Prerequisitos

1. **Python 3** instalado en tu máquina.
2. **Pip** (gestor de paquetes de Python).
3. **WebDriver** correspondiente al navegador que quieras usar:

   * Chrome → [Descargar ChromeDriver](https://chromedriver.chromium.org/downloads)
4. Asegúrate de que el WebDriver esté accesible desde tu **PATH** o configura su ubicación en el proyecto.

---

## ⚙️ Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Alchemist2309/TestAutomationDemo.git
cd TestAutomationDemo

# 2. Crear un entorno virtual (recomendado)
python3 -m venv venv
# En Windows:
# python -m venv venv

# 3. Activar el entorno virtual
# Linux/Mac
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate.bat

# 4. Instalar dependencias
pip install -r requirements.txt
```

---

## 📂 Estructura del proyecto

```
TestAutomationDemo/
│
├── features/                # Archivos .feature de Behave (escenarios BDD)
│   ├── *.feature
│   └── steps/               # Definiciones de pasos (step definitions)
│       └── *.py
│
├── utils/                   # Utilidades y helpers para Selenium
│   └── *.py
│
├── pages/                   # Page Objects (si aplicas POM)
│   └── *.py
│
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

---

## ▶️ Ejecución de pruebas

### Ejecutar todos los escenarios

```bash
behave
```


---

## 📝 Buenas prácticas

* Implementar el **patrón Page Object Model (POM)** para mantener el código organizado.
* Usar **WebDriverWait** en lugar de `time.sleep()` para mejorar la estabilidad.
* Organizar steps de forma **reutilizable**.
* Añadir **tags** en escenarios para filtrar la ejecución.
* Configurar hooks (`before_all`, `after_all`) para iniciar/cerrar el navegador y generar capturas de pantalla en caso de fallo.
* Generar reportes HTML o JSON con plugins de Behave para tener evidencias de ejecución.

---

