resource "kubernetes_namespace" "app" {
  metadata {
    name = "devops"
  }
}

resource "kubernetes_deployment" "app" {
  metadata {
    name      = "devops-app"
    namespace = kubernetes_namespace.app.metadata[0].name
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "devops-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "devops-app"
        }
      }

      spec {
        container {
          name  = "app"
          image = "devops-app:local"

          port {
            container_port = 8080
          }

          env {
            name  = "APP_MODE"
            value = "production"
          }

          resources {
            limits = {
              cpu    = "500m"
              memory = "256Mi"
            }
            requests = {
              cpu    = "100m"
              memory = "128Mi"
            }
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "app" {
  metadata {
    name      = "devops-app"
    namespace = kubernetes_namespace.app.metadata[0].name
  }

  spec {
    selector = {
      app = "devops-app"
    }

    port {
      port        = 80
      target_port = 8080
    }
  }
}
