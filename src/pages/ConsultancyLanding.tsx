import { useMemo } from 'react'
import heroImg from '../assets/figma/hero-1883x588.png'
import section1 from '../assets/figma/section-1883x723.png'
import section2 from '../assets/figma/section-1883x980.png'
import section3 from '../assets/figma/section-1885x772.png'
import section4 from '../assets/figma/section-1884x658.png'
import section5 from '../assets/figma/section-1884x813.png'
import section6 from '../assets/figma/section-1884x400.png'
import section7 from '../assets/figma/section-1884x842.png'

export default function ConsultancyLanding() {
  const year = useMemo(() => new Date().getFullYear(), [])

  return (
    <div className="app figma-only">
      <header className="site-header">
        <div className="container header-inner">
          <div className="brand">
            <span className="logo">CSISM</span>
            <span className="brand-sub">Consultancy</span>
          </div>
          <nav className="nav">
            <a href="#about">About</a>
            <a href="#expertise">Expertise</a>
            <a href="#laws">NCISM Laws</a>
            <a href="#faq">FAQ</a>
            <a href="#contact">Contact</a>
            <select className="lang">
              <option>English</option>
            </select>
          </nav>
        </div>
      </header>

      <main id="main">
        <section className="hero">
          <div className="container hero-inner">
            <div className="hero-media figma-node">
              <img src={heroImg} alt="Hero" />
            </div>
          </div>
        </section>
        <section>
          <img src={section1} alt="Section 1" style={{ width: '100%', height: 'auto' }} />
        </section>
        <section>
          <img src={section2} alt="Section 2" style={{ width: '100%', height: 'auto' }} />
        </section>
        <section>
          <img src={section3} alt="Section 3" style={{ width: '100%', height: 'auto' }} />
        </section>
        <section>
          <img src={section4} alt="Section 4" style={{ width: '100%', height: 'auto' }} />
        </section>
        <section>
          <img src={section5} alt="Section 5" style={{ width: '100%', height: 'auto' }} />
        </section>
        <section>
          <img src={section6} alt="Section 6" style={{ width: '100%', height: 'auto' }} />
        </section>
        <section>
          <img src={section7} alt="Section 7" style={{ width: '100%', height: 'auto' }} />
        </section>
      </main>

      <footer className="site-footer">
        <div className="container footer-inner">
          <div className="footer-left">
            <span className="logo">CSISM</span>
            <span className="muted">© {year}</span>
          </div>
          <div className="footer-right">
            <a href="#privacy">Privacy</a>
            <a href="#terms">Terms</a>
          </div>
        </div>
      </footer>
    </div>
  )
}
