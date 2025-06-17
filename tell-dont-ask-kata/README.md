# Tell, don't ask

[Original](https://github.com/racingDeveloper/tell-dont-ask-kata)

Un kata de refactorización de código heredado, centrado en la violación del principio Tell, don’t ask y el modelo de dominio anémico.

## Instrucciones

Aquí encontrarás una sencilla aplicación de flujo de pedidos. Es capaz de crear pedidos, hacer algunos cálculos (totales e impuestos) y gestionarlos (aprobación/rechazo y envío).

El antiguo equipo de desarrollo no encontró el tiempo para construir un modelo de dominio adecuado, sino que prefirió usar un estilo procedimental, construyendo este modelo de dominio anémico. Afortunadamente, al menos se tomaron el tiempo para escribir pruebas unitarias para el código.

Su nuevo CTO, después de muchos errores causados por esta aplicación, te pidió que refactorizaras este código para hacerlo más mantenible y confiable.

## En qué centrarse

Como dice el título del ejercicio, por supuesto, el principio Tell, don’t ask. Deberías poder eliminar todos los setters que mueven el comportamiento en los objetos de dominio.

Pero no te detengas ahí.

Si puedes eliminar algunos casos de prueba porque ya no tienen sentido (por ejemplo: no puedes compilar el código), ¡no dudes en hacerlo!

## Contribuir

Si desea contribuir a este kata añadiendo nuevos casos o versiones: ¡abre un PR!

@racingDeveloper