

Usuarios - Eventos:         Un usuario puede crear muchos eventos.
Eventos - Participantes:    Muchos usuarios pueden estar invitados a muchos eventos.
Eventos - Tareas:           Un evento puede tener muchas tareas.


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AnahiVera/event-planner-db">
  </a>

<h3 align="center">Event-planner-Db</h3>

  <p align="center">
    This project involves the development of an API that facilitates the creation, reading, updating, and deletion (CRUD) of data within a PostgreSQL database. The API is designed to automatically generate the necessary database tables and establish connections to the database. It is fully configured to run in a Docker environment, ensuring seamless deployment and scalability. 
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This API serves as the backend for a front-end application dedicated to event planning, enabling users to manage their events effectively. By providing robust data handling capabilities, it enhances the overall user experience and operational efficiency.
       - Key Features:
    *  Database Management PostgreSQL: The API automatically creates and configures the necessary database tables, ensuring a streamlined setup process for developers. 
    *  CRUD Functionality: Utilizing standard CRUD methods, the API allows for efficient management of event-related data, including creating new events, retrieving event details, updating existing records, and deleting events as needed.
    *  Docker Integration: The entire application is containerized using Docker, which simplifies deployment and ensures consistent environments across development and production stages.
    
    

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Once installed, ensure you can access the database using a management tool such as DBeaver or the database feature in Visual Studio Code.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them. (python - pipenv)
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/AnahiVera/event-planner-db.git
   ```
2. Open environment
   ```sh
   pipenv shell
   ```
3. Install packages
   ```sh
   pipenv install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin AnahiVera/event-planner-db
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/AnahiVera/event-planner-db/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/AnahiVera/event-planner-db/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AnahiVera/event-planner-db" alt="contrib.rocks image" />
</a>



<!-- CONTACT -->
## Contact

Anahi vera Rogel - vera.anahi.93@gmail.com

Project Link: [https://github.com/AnahiVera/event-planner-db](https://github.com/AnahiVera/event-planner-db)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AnahiVera/event-planner-db.svg?style=for-the-badge
[contributors-url]: https://github.com/AnahiVera/event-planner-db/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AnahiVera/event-planner-db.svg?style=for-the-badge
[forks-url]: https://github.com/AnahiVera/event-planner-db/network/members
[stars-shield]: https://img.shields.io/github/stars/AnahiVera/event-planner-db.svg?style=for-the-badge
[stars-url]: https://github.com/AnahiVera/event-planner-db/stargazers
[issues-shield]: https://img.shields.io/github/issues/AnahiVera/event-planner-db.svg?style=for-the-badge
[issues-url]: https://github.com/AnahiVera/event-planner-db/issues
[license-shield]: https://img.shields.io/github/license/AnahiVera/event-planner-db.svg?style=for-the-badge
[license-url]: https://github.com/AnahiVera/event-planner-db/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/anahi-vera-rogel
[product-screenshot]: images/screenshot.png
