import React, { useState } from 'react';

const Header: React.FC = () => {
  const [isNavOpen, setIsNavOpen] = useState(false);

  const toggleNav = () => {
    setIsNavOpen(!isNavOpen);
  };

  const closeNav = () => {
    setIsNavOpen(false);
  };

  return (
    <header className="site-header">
      <div className="container header-inner">
        <div className="brand">
          <div className="logo">CSISM</div>
          <span className="brand-sub">CONSULTANCY</span>
        </div>

        <button
          className="mobile-nav-toggle"
          onClick={toggleNav}
          aria-label="Toggle navigation"
        >
          {isNavOpen ? '✕' : '☰'}
        </button>

        <nav className={`nav ${isNavOpen ? 'nav-open' : ''}`}>
          <a href="#" onClick={closeNav}>Home</a>
          <a href="#about" onClick={closeNav}>About</a>
          <a href="#services" onClick={closeNav}>Services</a>
          <a href="#expertise" onClick={closeNav}>Expertise</a>
          <a href="#faq" onClick={closeNav}>FAQ</a>
          <a href="#contact" className="btn btn-primary" onClick={closeNav}>Contact Us</a>

          <div className="lang-wrapper">
            <select className="lang">
              <option value="en">EN</option>
              <option value="hi">HI</option>
            </select>
          </div>
        </nav>
      </div>
    </header>
  );
};

export default Header;
