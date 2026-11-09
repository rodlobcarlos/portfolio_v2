# Portfolio — Carlos Rodríguez Lobato

Portfolio personal construido íntegramente en Python con [Reflex](https://reflex.dev). Diseño minimalista oscuro, navegación por secciones y contenido estático: sin base de datos, sin backend propio y sin estado de servidor.

**Repositorio:** [github.com/rodlobcarlos/portfolio_v2](https://github.com/rodlobcarlos/portfolio_v2)

## Características

- Página principal con secciones **Inicio**, **Sobre mí** y **Trayectoria** con scroll suave.
- Página **Proyectos** en `/proyectos`, abierta en una pestaña nueva desde la navbar.
- Stack técnico agrupado por área (Desarrollo y DevOps) con iconos.
- Certificaciones, experiencia y formación con etiquetas de tecnologías.
- Enlaces a GitHub, LinkedIn, Gmail e InfoJobs.
- Descarga del CV en PDF desde la navbar y el hero.
- Diseño responsive verificado en móvil, tablet y escritorio.
- Tipografías Inter y JetBrains Mono; tema oscuro con acento monocromo.

## Stack

- **Python 3.12**
- **Reflex 0.10.x**
- **Radix Themes** (tema oscuro), **Tailwind v4** y **Sitemap** mediante plugins de Reflex
- Componentes propios en Python; CSS global mínimo en `assets/styles.css`

## Estructura del proyecto

```
portfolio_v2/
├── assets/                     # Imágenes, iconos, CSS global y CV
│   ├── cv_carlos_rodriguez_lobato.pdf
│   ├── profile.jpg
│   ├── styles.css
│   └── ...
├── Portfolio_v2/
│   ├── Portfolio_v2.py         # Entrada de la app y definición de rutas
│   ├── data.py                 # Todo el contenido estático (fuente de verdad)
│   ├── components/             # Piezas reutilizables (enlaces, stack, tags...)
│   ├── styles/                 # Colores, fuentes y estilos base
│   └── views/                  # Secciones y páginas (navbar, hero, proyectos...)
├── rxconfig.py                 # Configuración de Reflex y plugins
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.12 o superior
- Node.js y npm (Reflex los usa para compilar el frontend)
- Reflex 0.10.x

## Puesta en marcha

```bash
# 1. Crear y activar el entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# 2. Instalar Reflex
pip install "reflex>=0.10,<0.11"

# 3. Arrancar en modo desarrollo
reflex run --env dev
```

La app queda disponible en <http://localhost:3000> y el backend en <http://localhost:8000>.

> **Nota:** el `requirements.txt` actual contiene un `pip freeze` del sistema completo (paquetes de escritorio incluidos). Para un entorno limpio basta con instalar `reflex>=0.10,<0.11`; si quieres fijar versiones, genera un archivo nuevo desde el `.venv`.

## Comandos útiles

```bash
# Desarrollo con recarga en caliente
.venv/bin/reflex run --env dev

# Producción en un solo puerto
.venv/bin/reflex run --env prod --single-port

# Comprobar que compila sin arrancar el servidor
.venv/bin/reflex compile --dry
```

Si un cambio no aparece tras la recarga, fuerza la caché del navegador con `Ctrl+Shift+R`.

## Dónde editar el contenido

Todo el texto y los datos viven en **`Portfolio_v2/data.py`**:

| Constante        | Contenido                                                |
| ---------------- | -------------------------------------------------------- |
| `LINKS`          | URLs de GitHub, LinkedIn, Gmail, InfoJobs y certificados |
| `PROFILE`        | Nombre, rol, tagline, ubicación, biografía y CV          |
| `SOCIALS`        | Redes mostradas en el hero y el footer                   |
| `STACK`          | Tecnologías agrupadas por área                           |
| `CERTIFICATIONS` | Certificaciones, emisor, descripción e imagen            |
| `CAREER`         | Experiencia y formación, con periodo y etiquetas         |
| `PROJECTS`       | Proyectos de la página `/proyectos`                      |

No hace falta tocar componentes para cambiar textos: edita `data.py` y el cambio se refleja en toda la web.

## Assets y CV

- Los archivos se guardan en `assets/` y se referencian por **nombre exacto** desde `data.py`.
- Usa nombres **sin espacios ni tildes** (por ejemplo `cv_carlos_rodriguez_lobato.pdf`). Un nombre distinto provoca un `FileNotFoundError` al compilar y tumba el worker.
- El CV se sirve desde `assets/cv_carlos_rodriguez_lobato.pdf` y debe coincidir con:

  ```python
  "cv": "cv_carlos_rodriguez_lobato.pdf",
  ```

- La descarga se hace con `rx.download` desde un `<button>` en `Portfolio_v2/components/links.py`. No se usa un `<a download>` porque el router de React intercepta el clic y abriría el PDF en el navegador.

## Rutas

| Ruta         | Página                                            |
| ------------ | ------------------------------------------------- |
| `/`          | Inicio, Sobre mí y Trayectoria (scroll por anclas) |
| `/proyectos` | Proyectos personales y académicos                 |

## Despliegue

El proyecto no necesita base de datos ni servicios externos: es frontend estático servido por Reflex. Para producción:

```bash
.venv/bin/reflex run --env prod --single-port
```

También puede desplegarse en cualquier plataforma que ejecute Reflex (Reflex Cloud, un contenedor Docker o un servidor propio con Python).
