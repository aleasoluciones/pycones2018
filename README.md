# :snake: PyConES 2018 Málaga :snake:
## TDD de cero a cien (o casi)
**05 octubre 2018, 15:00 - 17:30**
Taller a cargo de [Alberto de la cruz](https://www.linkedin.com/in/alberto-de-la-cruz-grijalvo-51501a21) y [Raúl Villares](http://raulvillares.com)
---

### Contexto/objetivo

Si has ido a alguna kata o taller de introducción a TDD habrás hecho algún ejercicio con tests unitarios y a lo mejor te has preguntado *"muy bien, pero en mi trabajo tengo que comunicarme con bases de datos, servicios web... ¿cómo haría eso?"*

Este taller pretende ir un paso más allá y que salgas con un idea general de cómo podrías desarrollar con TDD un sistema completo que se integra con componentes externos.

Queremos hacerlo mostrando las técnicas y herramientas concretas que utilizamos en el día a día en [Alea Soluciones](https://www.alea-soluciones.com/).

### Entorno de trabajo

#### Requisitos

* Python 3 (¡sorpresa! :tada:)
* Pip
* Git
* Virtualenv (o similar)
* Editor de código

#### Clonar repositorio

```
git clone https://github.com/aleasoluciones/pycones2018.git
```

#### Crear un entorno virtual

Instalación de virtualenv: http://rukbottoland.com/blog/tutorial-de-python-virtualenv/

Para crear el virtualenv hay dos opciones:

1. Usar directamente virtualenv:

  ```
  virtualenv pycones2018
  source pycones2018/bin/activate
  ```
2. Usar virtualenvwrapper (mkvirtualenv):

  ```
  mkvirtualenv pycones2018
  ```

  Si ya lo hemos creado usando `mkvirtualenv` con anterioridad, lo podemos activar de nuevo con:

  ```
  workon pycones2018
  ```

#### Instalación de dependencias

Una vez dentro del entorno virtual, instalar las dependencias:

```bash=
pip install -r requirements-dev.txt
pip install -r requirements.txt
```

### Las soluciones propuestas paso a paso

- [Fibonacci](https://hackmd.io/UIsQmhKIS1K6Z25o4udQbQ)
- [Nameday](https://hackmd.io/ZBZLtQ6XSkW7T9QmmKGfGw)

### Recursos

- [Diapositivas](https://github.com/aleasoluciones/pycones2018/blob/master/doc/PyConES_2018.pdf)
- [Mamba](https://nestorsalceda.com/mamba/)
- [Expects](https://expects.readthedocs.io/en/stable/)
- [Doublex](https://pypi.org/project/doublex/)
- [Doublex expects](https://github.com/jaimegildesagredo/doublex-expects)
- [TDD, Jason Gorman](http://www.codemanship.co.uk/tdd_jasongorman_codemanship.pdf)
- [Diseño ágil con TDD](https://librosweb.es/libro/tdd/)
- [Taxonomía de tests, Micael Gallego](https://docs.google.com/document/d/1tJSfw5nvkSB_cpAqBleHeoStcs0gPVg7uGrWxYmingI/edit#heading=h.498fp6zdnxpr)
- [Test categories, Martin Fowler](https://martinfowler.com/tags/test%20categories.html)
- [Curso de TDD, Codesai](https://www.codesai.com/curso-de-tdd/)
- [Curso de TDD, Codium](http://www.codium.team/curso-tdd.html)
