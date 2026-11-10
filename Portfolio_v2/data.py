"""Contenido estático del portfolio.

No hay base de datos ni estado de servidor: todo el contenido vive aquí y se
renderiza directamente desde los componentes de Reflex.
"""

LINKS = {
    "github": "https://github.com/rodlobcarlos",
    "linkedin": "https://www.linkedin.com/in/carlos-rodr%C3%ADguez-lobato-211b27330/",
    "linkedin-portfolio": "http://linkedin.com/feed/update/urn:li:activity:7482869738788958208/",
    "linkedin_devops": "https://www.linkedin.com/feed/update/urn:li:activity:7524784448567943169/",
    "gmail": (
        "https://mail.google.com/mail/u/0/#inbox?compose="
        "CllgCJftLcKqXBjHKjGmBcrrsGTzTCRgwMwGjZRGvmFtKkMLljWKnlQtkJTDgMVCSQHGzggCwSV"
    ),
    "infojobs": "https://www.infojobs.net/candidate/cv/view/index.xhtml",
    "certifications": (
        "https://www.linkedin.com/in/carlos-rodr%C3%ADguez-lobato-211b27330/"
        "details/certifications/"
    ),
}

PROFILE = {
    "name": "Carlos Rodríguez Lobato",
    "short_name": "CRL",
    "role": "Desarrollador Full-Stack · DevOps",
    "tagline": "Bienvenido a mi portfolio personal, donde encontraras información sobre"
    " mí que te puede interesar!",
    "location": "Sevilla, España",
    "availability": "Remoto / desplazamiento",
    "focus": "Backend · Frontend · DevOps",
    "current": "En busqueda activa de trabajo",
    "bio": (
        "Me llamo Carlos Rodríguez Lobato y soy desarrollador full-stack y DevOps. "
        "Resido en Sevilla (España) y estoy abierto a trabajar en remoto o a "
        "desplazarme dentro del país. Me interesa especialmente el desarrollo "
        "backend/frontend y el trabajo como DevOps."
    ),
    "bio_2": (
        "He realizado prácticas en Atos (Eviden), donde he trabajado con Java, "
        "Spring Boot y Azure, y he formado parte de un proyecto real de Ferrovial "
        "con el equipo de DevOps. Me gustan los retos, el trabajo en equipo y seguir "
        "aprendiendo rodeado de buenos profesionales. Prefiero Python para "
        "desarrollo, y también trabajo con Angular, JavaScript y Java."
    ),
    "cv": "cv_carlos_rodriguez_lobato.pdf",
}

SOCIALS = [
    {"name": "GitHub", "icon": "git_branch", "url": LINKS["github"]},
    {"name": "LinkedIn", "icon": "external_link", "url": LINKS["linkedin"]},
    {"name": "Gmail", "icon": "mail", "url": LINKS["gmail"]},
    {"name": "InfoJobs", "icon": "briefcase", "url": LINKS["infojobs"]},
]

STACK = [
    {
        "name": "Backend",
        "icon": "code",
        "items": [
            {"name": "Python", "icon": "python.png"},
            {"name": "Java", "icon": "java.png"},
            {"name": "Spring Boot", "icon": "springboot.png"},
            {"name": "Node.js", "icon": "node.png"},
            {"name": "FastAPI", "icon": "fastapi.png"},
        ],
    },
    {
        "name": "Frontend",
        "icon": "code",
        "items": [
            {"name": "Angular", "icon": "angular.png"},
            {"name": "JavaScript", "icon": "JavaScript.png"},
            {"name": "TypeScript", "icon": "typescript.png"},
            {"name": "HTML / CSS", "icon": "htmlcss.png"},
            {"name": "Reflex", "icon": "reflex.png"},
        ],
    },
    {
        "name": "DevOps",
        "icon": "git-branch",
        "items": [
            {"name": "Azure", "icon": "azure.png"},
            {"name": "Azure DevOps", "icon": "azureDevOps.png"},
            {"name": "Terraform", "icon": "terraform.png"},
            {"name": "CodeQL", "icon": "codeql.jpeg"},
            {"name": "CI/CD", "icon": "cicd.png"},
            {"name": "Kubernetes", "icon": "kubernetes.png"},
            {"name": "GitOps", "icon": "gitops.png"},
            {"name": "Trivy", "icon": "trivy.png"},
            {"name": "Prometheus", "icon": "prometheus.png"},
            {"name": "Grafana", "icon": "grafana.png"},
            {"name": "Git / GitHub", "icon": "github.png"},
            {"name": "GitHub Copilot", "icon": "copilot.png"}
        ],
    },
    {
        "name": "Base de datos",
        "icon": "database",
        "items": [
            {"name": "MongoDB", "icon": "mongo.png"},
            {"name": "MySQL", "icon": "mysql.png"},
            {"name": "Oracle PL/SQL", "icon": "plsql.png"},
        ],
    },
]

CERTIFICATIONS = [
    {
        "name": "GitHub Foundations",
        "issuer": "GitHub",
        "description": (
            "Fundamentos de Git y GitHub, colaboración, gestión de proyectos, "
            "privacidad y seguridad."
        ),
        "image": "github-foundations.svg",
        "url": LINKS["certifications"],
    },
    {
        "name": "NexoNeural",
        "issuer": "IA Power Bootcamp II edition",
        "description": (
            "Fundamentos de la IA, la importancia de los datos, "
            "la inteligencia artificial en las empresas, funcionalidades y operatividad con la IA."
        ),
        "image": "nexoneural.jpg",
        "url": LINKS["certifications"],
    }
]

CAREER = [
    {
        "period": "Febrero — Mayo 2026",
        "type": "Experiencia",
        "title": "Prácticas en Atos",
        "organization": "Proyecto Ferroviario · Equipo DevOps",
        "description": (
            "Me incorporé al proyecto real ferroviario con el equipo de DevOps. "
            "Aprendí sobre DevOps, CI/CD, Jira, IaC y Azure Portal / Azure DevOps "
            "para desplegar aplicaciones en infraestructura cloud."
        ),
        "tags": ["DevOps", "CI/CD", "Jira", "IaC", "Azure", "Azure DevOps"],
    },
    {
        "period": "Septiembre 2025 — Mayo 2026",
        "type": "Formación",
        "title": "2 DAM",
        "organization": "Grado Superior de Desarrollo de Aplicaciones Multiplataforma",
        "description": (
            "Utilicé JavaScript, TypeScript, Angular, Spring Boot (Java), MongoDB y "
            "Oracle PL/SQL. Proyecto final: prototipo de gestión personal de tareas "
            "con IA usando Angular para web y Android Studio para móvil."
        ),
        "tags": [
            "Angular",
            "Spring Boot",
            "MongoDB",
            "Oracle",
            "TypeScript",
            "Android Studio",
        ],
    },
    {
        "period": "Abril — Mayo 2025",
        "type": "Experiencia",
        "title": "Prácticas en Eviden",
        "organization": "Formación en Java y Spring Boot",
        "description": (
            "Realicé un periodo de un mes de prácticas en Atos (Eviden), donde "
            "aprendí conocimientos sobre Java con JPA, Hibernate y Spring Boot."
        ),
        "tags": ["Java", "JPA", "Hibernate", "Spring Boot"],
    },
    {
        "period": "Septiembre 2024 — Mayo 2025",
        "type": "Formación",
        "title": "1 DAM",
        "organization": "La Algaba, Sevilla",
        "description": (
            "Comencé el Grado Superior de Desarrollo de Aplicaciones Multiplataforma. "
            "Aprendí HTML, CSS, Java, Python, XML y MySQL."
        ),
        "tags": ["HTML", "CSS", "Java", "Python", "XML", "MySQL"],
    },
]

PROJECTS = [
    {
        "title": "Cloud-Native DevOps & SRE Showcase Platform",
        "description": (
            "Proyecto monorepo integral que reproduce a coste cero un ciclo de vida de desarrollo de software (SDLC) "
            " completo con enfoque Cloud-Native, DevSecOps y observabilidad SRE."
        ),
        "tech": [
            "Python",
            "FastAPI",
            "Kubernetes",
            "Terraform",
            "ArgoCD",
            "Trivy",
            "Prometheus",
            "Grafana",

        ],
        "github": "https://github.com/rodlobcarlos/devops-end-to-end-project",
        "linkedin_devops": "https://www.linkedin.com/feed/update/urn:li:activity:7524784448567943169/",
        "demo": None,
        "icon": "git-branch",
        "image": "devops-platform.png"
    },
    {
        "title": "Portfolio personal con Reflex",
        "description": (
            "Este mismo portfolio, construido en Python con Reflex, "
            "sin base de datos ni backend propio. Diseño minimalista oscuro y "
            "navegación por secciones."
        ),
        "tech": ["Python", "Reflex"],
        "github": "https://github.com/rodlobcarlos/portfolio_v2",
        "linkedin_portfolio": "http://linkedin.com/feed/update/urn:li:activity:7482869738788958208/",
        "demo": None,
        "icon": "code",
        "image": "portfolio.png"
    },
]
