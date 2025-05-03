
# Sistema Experto para Diagnóstico de Fallas Vehiculares

Este sistema experto en Prolog permite diagnosticar fallas comunes en vehículos con base en síntomas reportados, códigos OBD2 y condiciones de operación. También sugiere soluciones, urgencia del problema, mantenimiento preventivo y estimación de costos.

---

## 📌 Hechos Básicos sobre Vehículos

```prolog
marca(vehiculo, marca).
modelo(vehiculo, modelo).
anio(vehiculo, anio).
kilometraje(vehiculo, kilometros).
```

---

## 🛑 Síntomas Comunes

```prolog
sintoma(vehiculo, luz_check_engine).
sintoma(vehiculo, ruidos_anormales).
sintoma(vehiculo, perdida_potencia).
sintoma(vehiculo, problemas_electricos).
sintoma(vehiculo, consumo_excesivo_combustible).
sintoma(vehiculo, vibraciones).
```

---

## 🔍 Reglas de Diagnóstico Principal

```prolog
diagnostico(vehiculo, Problema) :-
    sintoma(vehiculo, luz_check_engine),
    sintoma(vehiculo, consumo_excesivo_combustible),
    codigo_error(vehiculo, 'P0172'),
    Problema = 'Mezcla rica de combustible: posible falla en sensor de oxígeno o filtro de aire obstruido'.

diagnostico(vehiculo, Problema) :-
    sintoma(vehiculo, vibraciones),
    sintoma(vehiculo, ruidos_anormales),
    condiciones(vehiculo, en_frio),
    Problema = 'Bujías en mal estado o con brecha incorrecta'.

diagnostico(vehiculo, Problema) :-
    sintoma(vehiculo, vibraciones),
    sintoma(vehiculo, ruidos_anormales),
    condiciones(vehiculo, en_caliente),
    Problema = 'Posible problema de balanceo de ruedas o neumáticos desgastados'.

diagnostico(vehiculo, Problema) :-
    sintoma(vehiculo, perdida_potencia),
    sintoma(vehiculo, consumo_excesivo_combustible),
    kilometraje(vehiculo, Km),
    Km > 50000,
    Problema = 'Filtro de combustible obstruido o inyectores sucios'.
```

---

## 🚨 Reglas para Determinar Urgencia

```prolog
urgencia(Problema, Urgencia) :-
    member(Problema, ['Falla en sistema de frenos', 'Fuga de combustible', 'Sobrecalentamiento del motor']),
    Urgencia = critica.

urgencia(Problema, Urgencia) :-
    member(Problema, ['Mezcla rica de combustible', 'Bujías en mal estado', 'Filtro de aire obstruido']),
    Urgencia = importante.

urgencia(Problema, Urgencia) :-
    member(Problema, ['Neumáticos desgastados', 'Aceite necesita cambio']),
    Urgencia = mantenimiento.
```

---

## 🔧 Reglas para Tipo de Solución

```prolog
solucion(Problema, TipoSolucion) :-
    member(Problema, ['Bujías en mal estado', 'Filtro de aire obstruido', 'Cambio de aceite']),
    TipoSolucion = 'Puede hacerlo usted mismo con guía del sistema'.

solucion(Problema, TipoSolucion) :-
    member(Problema, ['Problema de transmisión', 'Falla en computadora', 'Reparación de motor']),
    TipoSolucion = 'Requiere taller especializado'.
```

---

## 🧰 Mantenimiento Preventivo

```prolog
mantenimiento_preventivo(vehiculo, 'Cambio de aceite y filtro') :-
    kilometraje(vehiculo, Km),
    Km >= 10000.

mantenimiento_preventivo(vehiculo, 'Revisión de frenos') :-
    kilometraje(vehiculo, Km),
    Km >= 25000.

mantenimiento_preventivo(vehiculo, 'Cambio de bujías') :-
    kilometraje(vehiculo, Km),
    Km >= 50000.
```

---

## 📟 Interpretación de Códigos OBD2

```prolog
codigo_error(vehiculo, Codigo) :-
    sintoma(vehiculo, luz_check_engine),
    interpretar_codigo(Codigo, Descripcion).

interpretar_codigo('P0172', 'Sistema demasiado rico (Banco 1)').
interpretar_codigo('P0300', 'Fallos de encendido aleatorios/múltiples').
interpretar_codigo('P0420', 'Eficiencia del catalizador por debajo del umbral (Banco 1)').
```

---

## 🌡️ Condiciones de Operación

```prolog
condiciones(vehiculo, en_frio) :-
    sintoma(vehiculo, ocurre_al_arrancar).

condiciones(vehiculo, en_caliente) :-
    sintoma(vehiculo, ocurre_despues_de_conducir).
```

---

## 💰 Estimación de Costos

```prolog
costo_estimado(Problema, Rango) :-
    member(Problema, ['Bujías en mal estado']),
    Rango = '500-1500 MXN'.

costo_estimado(Problema, Rango) :-
    member(Problema, ['Falla en sensor de oxígeno']),
    Rango = '1500-3500 MXN'.

costo_estimado(Problema, Rango) :-
    member(Problema, ['Problema de transmisión']),
    Rango = '5000-15000 MXN'.
```

---

## 📋 Consulta Principal del Sistema

```prolog
consultar_diagnostico(Vehiculo) :-
    diagnostico(Vehiculo, Problema),
    urgencia(Problema, Urgencia),
    solucion(Problema, TipoSolucion),
    costo_estimado(Problema, Costo),
    write('Diagnóstico: '), write(Problema), nl,
    write('Urgencia: '), write(Urgencia), nl,
    write('Solución: '), write(TipoSolucion), nl,
    write('Costo estimado: '), write(Costo), nl.
```
