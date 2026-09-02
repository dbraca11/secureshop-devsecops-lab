# 🛡️ SecureShop DevSecOps Lab

Repository for SecureShop DevSecOps Pipeline & Infrastructure.

SecureShop es un proyecto integral diseñado para implementar y demostrar el ciclo de vida completo de **DevSecOps**, **Seguridad en Contenedores**, **Monitoreo en Tiempo de Ejecución (Runtime Security)** y **Observabilidad** sobre un clúster de Kubernetes.

---

## 🏗️ Diagrama de Arquitectura del Pipeline y Stack

```mermaid
graph TD
    subgraph sub1 ["🛡️ 1. Shift-Left Security (CI/CD)"]
        A[💻 Código Fuente FastAPI] --> B[🧪 Paso 2: Pruebas Unitarias pytest]
        B --> C[🔍 Paso 3: SAST - Análisis Estático]
        C --> D[📦 Paso 4: SCA - Dependencias]
        D --> E[🔑 Paso 5: Secret Scanning - Gitleaks]
    end

    subgraph sub2 ["🐳 2. Container & IaC Security"]
        E --> F[🏗️ Paso 6: Docker Build]
        F --> G[🛡️ Paso 7: Trivy Image Scan]
        H[📋 Manifiestos Kubernetes] --> I[🛠️ Paso 8: Checkov IaC Scan]
    end

    subgraph sub3 ["☸️ 3. Kubernetes Runtime & Security"]
        G --> J[🚀 Paso 9: Despliegue en K8s - Namespace secureshop]
        I --> J
        J --> K[⚡ Paso 10: DAST - OWASP ZAP API Testing]
        J --> L[🚨 Paso 11 & 12: Runtime Security - Falco eBPF & Detección]
    end

    subgraph sub4 ["📊 4. Observability Stack"]
        J --> M[📈 Paso 13: Prometheus & Grafana]
        M --> N[📊 Paso 14: Visualización de Métricas & Dashboards]
    end
