<div id="top"></div>

<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo2.png" alt="Logo" width="120" height="80">
  </a>

  <h3 align="center">Web Scraping with Selenium</h3>

  <p align="center">
    Web scraping de información de ofertas laborales con selenium
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Este proyecto es un demo de las características que provee selenium para el scraping de información de la web.

Que hace en el proyecto:
* Scraping de la información de páginas de reclutamiento con selenium.
* Enriquecimiento de información con el API de google maps.
* Persistencia de información a una BD postgres
* Generación de archivo con información persistida

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

Este proyecto se puede desplegar en cualquier ambiente que tenga python 3.8, sin embargo, algunas librerías dependen de componentes adicionales del SO. Esta probado en ambiente ubuntu 20.04

* [python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Los siguientes pasos son los pasos requeridos para ejecutar el proyecto en un SO ubuntu 20.04.

### Prerequisites

* python 3.8
* postgres

### Installation

1. Obtener un API Key en [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials) para acceder al API de google maps
2. Clonar el repo
  ```sh
    git clone https://github.com/ivancho82/scraping-greenhouse.git
  ```
3. Instalar dependencias de librerías
  ```sh
    sudo apt-get update
    sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4
    sudo apt-get install libpq5
    sudo apt install ./chromedriver/google-chrome-stable_current_amd64.deb
  ```
4. Instalar los requerimientos
  ```sh
    pip install -r requirements.txt
  ```
4. Setear las variables de entorno
  ```sh
    export KEY_GCP=GCP_API_KEY_GOOGLE_MAPS
    export PG_HOST=POSTGRES_HOST_URI_IP
    export PG_DATABASE=POSTGRES_DATABASE_NAME
    export PG_USER=POSTGRES_USER_WITH_DB_ACCESS
    export PG_PASSWORD=POSTGRES_USER_PASSWORD
    export PG_TABLE=POSTGRES_TABLE_NAME
  ```

4. Configurar el archivo `params.py` con la lista de las urls a hacer scraping
  ```python
    self.pages =[
            "LIST",
            "PAGES",
            "TO SCRAP"
        ]
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

  El script genera un archivo data.out con la información que queda persistida e la tabla de postgres
  ```sh
    python3 main.py
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog
- [ ] Add docker compose
- [ ] Add README in english

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

**greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Ivan Cuervo - [@ivan_cuervo](https://twitter.com/ivan_cuervo) - ivan.cuervom@gmail.com

Project Link: [https://github.com/ivancho82/scraping-greenhouse](https://github.com/ivancho82/scraping-greenhouse)

<p align="right">(<a href="#top">back to top</a>)</p>
