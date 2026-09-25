// Hero mark animation (only present on the homepage).
// A static SVG of the same first frame sits behind the canvas and paints
// immediately on load; it's hidden once Rive has actually loaded and is
// ready to draw, so there's no blank gap while the runtime/asset fetch.
const heroCanvas = document.getElementById('hero-rive');
const heroFallback = document.getElementById('hero-fallback');
if (window.rive && heroCanvas) {
  new rive.Rive({
    src: '/assets/hero-z.riv',
    canvas: heroCanvas,
    autoplay: true,
    stateMachines: 'State Machine 1',
    layout: new rive.Layout({ fit: rive.Fit.Contain }),
    onLoad: function () {
      if (heroFallback) heroFallback.style.display = 'none';
    }
  });
}

// Hourglass: one-shot, plays once when scrolled into view
var hourglassCanvas = document.getElementById('hourglass-rive');
if (window.rive && hourglassCanvas) {
  var hourglass = new rive.Rive({
    src: '/assets/hourglass.riv',
    canvas: hourglassCanvas,
    artboard: 'Hourglass',
    stateMachines: 'Play Once',
    autoplay: false,
    onLoad: function () {
      hourglass.resizeDrawingSurfaceToCanvas();
      if (!('IntersectionObserver' in window)) { hourglass.play(); return; }
      var observer = new IntersectionObserver(function (entries) {
        if (entries[0].isIntersecting) {
          hourglass.play();
          observer.disconnect();
        }
      }, { threshold: 0.6 });
      observer.observe(hourglassCanvas);
    }
  });
}

// Animated service-card icons (only present on pages with service cards)
if (window.rive) {
  document.querySelectorAll('canvas.rive-icon').forEach(function (canvas) {
    var artboard = canvas.dataset.artboard;
    var card = canvas.closest('.card');
    var riveInstance = new rive.Rive({
      src: '/assets/icons.riv',
      canvas: canvas,
      artboard: artboard,
      stateMachines: 'Hover SM',
      autoplay: true,
      onLoad: function () {
        riveInstance.resizeDrawingSurfaceToCanvas();
        var inputs = riveInstance.stateMachineInputs('Hover SM');
        var hovered = inputs.find(function (i) { return i.name === 'Hovered'; });
        if (hovered && card) {
          card.addEventListener('mouseenter', function () { hovered.value = true; });
          card.addEventListener('mouseleave', function () { hovered.value = false; });
        }
      }
    });
  });
}

// Mobile nav toggle
const toggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

if (toggle && navLinks) {
  toggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
    toggle.classList.toggle('active');
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      toggle.setAttribute('aria-expanded', false);
      toggle.classList.remove('active');
    });
  });
}

// Contact form — AJAX submit with inline success message (homepage + contact page)
const form = document.getElementById('contact-form');
const successMsg = document.getElementById('form-success');
const submitBtn = document.getElementById('submit-btn');

var isAr = document.documentElement.lang === 'ar';
if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    submitBtn.disabled = true;
    submitBtn.textContent = isAr ? 'جارٍ الإرسال…' : 'Sending…';

    const data = new FormData(form);

    try {
      const res = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        body: data
      });
      const json = await res.json();

      if (json.success) {
        form.style.display = 'none';
        successMsg.style.display = 'flex';
      } else {
        throw new Error('Submission failed');
      }
    } catch {
      submitBtn.disabled = false;
      submitBtn.textContent = isAr ? 'إرسال الرسالة' : 'Send Message';
      alert(isAr ? 'حدث خطأ ما. يُرجى المحاولة مرة أخرى أو مراسلتنا مباشرة على support@ztactique.com' : 'Something went wrong. Please try again or email us directly at support@ztactique.com');
    }
  });
}
