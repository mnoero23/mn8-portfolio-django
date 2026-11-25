from django.db import migrations


ARTICULOS = [
    {
        "titulo": "De la planilla al producto: por qué construí FARO",
        "contenido": """Durante años trabajé con información financiera distribuida entre bancos, brokers, comprobantes y planillas. El problema no era la falta de datos, sino la dificultad para reconstruir qué había ocurrido y responder una pregunta simple: ¿cómo está evolucionando realmente mi patrimonio?

FARO nació para ordenar esa complejidad. El primer paso no fue programar una pantalla, sino definir conceptos: aportes, retiros, saldos, movimientos internos, resultados y evidencia. Cuando esas definiciones no son claras, cualquier indicador puede parecer preciso y aun así conducir a una conclusión equivocada.

El proyecto combina análisis de datos, automatización y diseño de experiencia. Cada resultado debe poder rastrearse hasta su origen; cuando la evidencia no alcanza, la aplicación lo informa en lugar de inventar una respuesta. Esa decisión es tan importante como cualquier funcionalidad.

Construir FARO me enseñó que un producto de datos útil necesita tres capas: información confiable, reglas de negocio explícitas y una interfaz que ayude a decidir. Python y la tecnología son el medio. El verdadero valor está en transformar registros dispersos en una lectura comprensible y accionable.""",
    },
    {
        "titulo": "ALQIVO: diseñar una operación de alquileres con trazabilidad",
        "contenido": """Administrar un alquiler temporario parece sencillo hasta que reservas, pagos, gastos, propietarios, tareas del equipo y mensajes a huéspedes empiezan a convivir en canales diferentes. ALQIVO surge de ese problema real: reducir la fragmentación sin perder el detalle de la operación.

La plataforma organiza unidades, reservas, liquidaciones, gastos y experiencia del huésped en un mismo flujo. También incorpora asignaciones y trazabilidad para saber quién realizó cada acción. No se trata solamente de guardar información, sino de construir una fuente compartida de verdad.

El diseño se apoya en una idea: cada persona debe ver lo que necesita para actuar. El administrador requiere control; el propietario, transparencia; el equipo operativo, instrucciones claras; y el huésped, una experiencia simple. Modelar esos recorridos antes de agregar funciones evita convertir el sistema en otra planilla difícil de usar.

ALQIVO representa mi manera de trabajar: entender el negocio desde adentro, ordenar el proceso y recién después elegir la tecnología. El resultado es un producto que evoluciona con casos reales y convierte tareas aisladas en una operación medible.""",
    },
    {
        "titulo": "Aprender Django construyendo un proyecto real",
        "contenido": """Este sitio comenzó como una entrega académica y terminó convirtiéndose en una pieza de portfolio. Esa evolución cambió la forma de aprender: cada concepto de Django pasó a resolver una necesidad visible del producto.

Los modelos representan publicaciones y perfiles; las vistas coordinan las operaciones; los formularios validan la entrada; las URLs conectan cada recorrido; y los templates separan estructura y presentación. El CRUD dejó de ser un ejercicio aislado cuando incorporó imágenes, autenticación, mensajes y permisos por propietario.

También aprendí que una aplicación no está completa porque funciona en mi computadora. Debe poder reconstruirse desde un repositorio limpio, proteger sus secretos con variables de entorno, declarar dependencias y explicar su instalación. Las migraciones, el archivo requirements.txt, el .gitignore y el README forman parte del producto.

Las pruebas automatizadas cumplen un papel central: permiten mejorar el diseño sin perder comportamientos anteriores. Este proyecto valida modelos, vistas, formularios, autenticación, imágenes, autoría y permisos. Aprender Django construyendo algo propio me permitió conectar código, experiencia de usuario y propósito profesional.""",
    },
]


def crear_articulos(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    for articulo in ARTICULOS:
        Post.objects.get_or_create(
            titulo=articulo["titulo"],
            defaults={
                "contenido": articulo["contenido"],
                "autor_legacy": "Matías Noero",
                "estado": "publicado",
            },
        )


def eliminar_articulos(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    Post.objects.filter(
        titulo__in=[articulo["titulo"] for articulo in ARTICULOS],
        autor__isnull=True,
        autor_legacy="Matías Noero",
    ).delete()


class Migration(migrations.Migration):
    dependencies = [("posts", "0003_post_autor_usuario")]

    operations = [migrations.RunPython(crear_articulos, eliminar_articulos)]
