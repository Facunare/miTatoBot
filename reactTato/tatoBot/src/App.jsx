import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    
    <body>
      <head>
        <meta charset="UTF-8"></meta>
        <meta http-equiv="X-UA-Compatible" content="IE=edge"></meta>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta>
        <title>Document</title>
        <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css"/>
        <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'/>
        <link rel="preconnect" href="https://fonts.googleapis.com"/>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
        <link href="https://fonts.googleapis.com/css?family=Lato&display=swap" rel="stylesheet"/>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet"/>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous"/>
        <link rel="stylesheet" href="https://unpkg.com/swiper@8/swiper-bundle.min.css" />
      </head>
       <header id="header">
        <nav class="navbar navbar-expand-lg">
          <div class="container-fluid">
            <div class="logo-container">
              <a href="index.html">
                <img class="img-logo" src="/img/logo-et36.png" alt="logo-et36"></img>
              </a>
              <h1 class="header-title">E.T36 D.E.15</h1>
        </div>
        <button class="navbar-toggler" id="navbar-toggler" type="button" data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-center" id="navbarSupportedContent">
          <ul class="navbar-nav mb-2 mb-lg-0">
            <li class="nav-item">
              <div data-aos="zoom-out">
                <a class="nav-link active" aria-current="page" href="#">INICIO</a>
              </div>
            </li>
            <li class="nav-item">
              <div data-aos="zoom-out">
                <a class="nav-link active" aria-current="page" href="#">PROYECTOS</a>
              </div>
            </li>
            <li class="nav-item">
              <div data-aos="zoom-out">
                <a class="nav-link active" aria-current="page" href="contacto.html">CONTACTO</a>
              </div>
            </li>
          </ul>
            </div>
          </div>
        </nav>
       </header>
       <section class="titulo">
            <div data-aos="fade-down-right">
              <div id="message" class="hidden">
                <div class="message-content">
                  ¿Querés inscribirte en el colegio?
                </div>
                <a href="https://buenosaires.gob.ar/educacion/estudiantes/inscripcionescolar">Preciona aqui</a>
                <div class="arrow"></div>
              </div>
            </div>
            <div class="row justify-content-center">
              <div class="col-lg-12 col-md-12 col-sm-12">
              <div class="main-img" src="/img/polo-educativo-saavedra.png" alt="colegio et36">                
              </div>
                <div class="main-text-container">
                <h4 class="main-img-text text-focus-in"><span class="main-img-text-span">Escuela Tecnica N°36</span>
                  <span class="main-img-text-span2">"Almirante Guillermo Brown"</span>
                </h4>
                      <p class="main-img-text">Es una escuela que forma técnicos/as en Computación y Maestros mayores de obra e
                  integra el
                  Polo Educativo Saavedra.
                  Cuenta con equipamiento tecnológico como impresoras 3D y drones. Fue ganadora del 1.er premio en las
                  Olimpiadas de
                  Computación.</p>
                </div>
                <div class="social-links">
          <ul>
            <li><a href="https://www.instagram.com/et36de15brown/" class="instagram"><i
                  class='bx bxl-instagram'></i><span class="sr-only">Facebook</span></a></li>
            <li><a
                href="https://www.facebook.com/escuelatecnica36?paipv=0&eav=AfaytHmLUJlZHgFK7LRC8dWNvMiSBbzsvolZmHqc__z2e3Yo_vuI3AtGQo8oNoMnLoQ&_rdr"
                class="facebook"><i class='bx bxl-facebook'></i><span class="sr-only">Twitter</span></a></li>
          </ul>
        </div>
              </div>
            </div>

       </section>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous">
        </script>
        <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
        <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
        <script src="https://unpkg.com/swiper@8/swiper-bundle.min.js"></script>
        <script src="app.js"></script>
        <script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
        <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
        <script>
          AOS.init();
        </script>
    </body>
  )
}

export default App
