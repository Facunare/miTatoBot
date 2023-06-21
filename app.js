function toggleCardButtonColors() {
    const card = document.querySelector('.card');
    const button = document.querySelector('.boton-verFotos');

    card.classList.toggle('card-hover');
    button.classList.toggle('boton-hover');
}

// const carousel = document.getElementById('carouselExample-proyectos1');
// const carouselItems = carousel.querySelectorAll('.carousel-item');

// // Función para actualizar el tamaño y posición de las tarjetas
// function updateCardSizes() {
//   carouselItems.forEach((item, index) => {
//     const tarjeta = item.querySelector('.my-tarjeta');

//     if (index === 0) {
//       tarjeta.classList.add('my-tarjeta-large');
//       tarjeta.classList.remove('my-tarjeta-small');
//     } else {
//       tarjeta.classList.remove('my-tarjeta-large');
//       tarjeta.classList.add('my-tarjeta-small');
//     }
//   });
// }

// // Evento para actualizar las tarjetas al cambiar de slide
// carousel.addEventListener('slid.bs.carousel', () => {
//   updateCardSizes();
// });

// // Llamada inicial a la función para configurar el tamaño y posición inicial
// updateCardSizes();


// var TrandingSlider = new Swiper('.tranding-slider', {
//     // Opciones del Swiper

//     on: {
//       slideChange: function () {
//         // Obtén todas las tarjetas
//         var slides = document.getElementsByClassName('tranding-slide');

//         // Elimina la clase 'active' de todas las tarjetas
//         for (var i = 0; i < slides.length; i++) {
//           slides[i].classList.remove('active');
//         }

//         // Agrega la clase 'active' a la tarjeta actualmente visible en el medio
//         slides[this.activeIndex].classList.add('active');
//       },
//     },
//   });

var topSlider = new Swiper('.top-slider', {
    on: {
        slideChangeTransitionEnd: function () {
            var activeIndex = this.activeIndex;

            // Remover la clase active de todas las tarjetas del top-slider
            var topSliderCards = document.querySelectorAll('.top-slider .swiper-slide');
            topSliderCards.forEach(function (card) {
                card.classList.remove('active');
            });

            // Agregar la clase active a la tarjeta correspondiente en el top-slider
            var activeCard = topSliderCards[activeIndex];
            activeCard.classList.add('active');
        }
    },
    on: {
        transitionEnd: function () {
            updateActiveCard(this, '.top-slider');
        },
        touchEnd: function () {
            updateActiveCard(this, '.top-slider');
        }
    },
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: 'auto',
    coverflowEffect: {
        rotate: 5,
        stretch: 0,
        depth: 100,
        modifier: 1,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    }
});

var bottomSlider = new Swiper('.bottom-slider', {
    on: {
        slideChange: function () {
            // Obtén todas las tarjetas de ambos conjuntos
            var slides = document.querySelectorAll('.tranding-slider .tranding-slide');

            // Elimina la clase 'active' de todas las tarjetas
            for (var i = 0; i < slides.length; i++) {
                slides[i].classList.remove('active');
            }

            // Agrega la clase 'active' a la tarjeta actualmente visible en el medio del primer conjunto
            slides[this.activeIndex].classList.add('active');

            // Calcula el índice correspondiente para el segundo conjunto
            var secondIndex = this.activeIndex + slides.length / 2;

            // Agrega la clase 'active' a la tarjeta correspondiente del segundo conjunto
            slides[secondIndex].classList.add('active');
        },
    },
    on: {
        transitionEnd: function () {
            updateActiveCard(this, '.bottom-slider');
        },
        touchEnd: function () {
            updateActiveCard(this, '.bottom-slider');
        }
    },
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: 'auto',
    coverflowEffect: {
        rotate: 5,
        stretch: 0,
        depth: 100,
        modifier: 1,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    }
});

function updateActiveCard(swiper, sliderSelector) {
    var sliderWidth = swiper.width; // Ancho del carrusel
    var slides = swiper.slides; // Slides del carrusel
    var activeIndex = swiper.activeIndex; // Índice del slide activo
  
    // Remover la clase active de todas las tarjetas
    var sliderCards = document.querySelectorAll(sliderSelector + ' .swiper-slide');
    sliderCards.forEach(function(card) {
      card.classList.remove('active');
    });
  
    // Agregar la clase active al slide actual
    var activeCard = slides[activeIndex];
    activeCard.classList.add('active');
  }

const sliderPrev = document.getElementById('slider-prev');
const sliderNext = document.getElementById('slider-next');
const slider = document.querySelector('.tranding-slider');

// Agregar el evento click a los elementos de flecha y fondo
sliderPrev.addEventListener('click', () => {
    swiper.slidePrev(); // Mover el carrusel hacia la izquierda
});

sliderNext.addEventListener('click', () => {
    swiper.slideNext(); // Mover el carrusel hacia la derecha
});



window.addEventListener('scroll', function () {
    var message = document.getElementById('message');
    var pageHeight = document.documentElement.scrollHeight;
    var windowHeight = window.innerHeight;
    var scrollPosition = window.scrollY || window.pageYOffset || document.body.scrollTop + (document.documentElement && document.documentElement.scrollTop || 0);

    if (scrollPosition > (pageHeight / 2 - windowHeight / 2)) {
        message.classList.remove('hidden');
    } else {
        message.classList.add('hidden');
    }
});

