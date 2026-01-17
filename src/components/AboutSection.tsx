import React from 'react';
import '../App.css';

const AboutSection: React.FC = () => {
  return (
    <section id="about" className="about-section section-padding">
      <div className="container">
        <div className="about-header">
          <h2 className="section-title">About <span className="text-dark">Kashish Gupta</span></h2>
          <p className="section-subtitle">
            Consultancy expert with extensive experience in Indian System of Medicine regulatory frameworks and institutional development.
          </p>
        </div>

        <div className="about-content-wrapper">
          {/* Professional Background Card */}
          <div className="professional-background-card">
            <h3 className="card-title text-dark">Professional Background</h3>
            <p className="card-text">
              With years of deep insider knowledge of NCISM regulations and procedures, Kashish provides simplified, transparent guidance to institutions seeking to establish or enhance their ISM colleges. Our approach combines regulatory compliance with practical implementation strategies.
            </p>

            <div className="contact-cards-row">
              <a href="mailto:kashish@csism.com" className="contact-mini-card">
                <span className="contact-icon">✉️</span>
                <span className="contact-label">Email</span>
                <span className="contact-value">kashish@csism.com</span>
              </a>

              <a href="https://wa.me/919999999999" className="contact-mini-card">
                <span className="contact-icon">📱</span>
                <span className="contact-label">WhatsApp</span>
                <span className="contact-value">+91 99999 99999</span>
              </a>
            </div>
          </div>

          {/* Credentials Section */}
          <div className="credentials-section">
            <div className="credentials-header">
              <div className="orange-line"></div>
              <h3 className="text-dark">Professional Credentials</h3>
            </div>

            <ul className="credentials-list">
              <li>
                <strong>Verified Expertise:</strong> Backed by professional recommendation letters from industry experts and regulatory bodies
              </li>
              <li>
                <strong>Attorney-Client Privilege:</strong> All consultations protected under attorney-client privilege and NDA
              </li>
              <li>
                <strong>Regulatory Knowledge:</strong> Deep insider understanding of NCISM regulations and compliance requirements
              </li>
              <li>
                <strong>Institutional Development:</strong> Expertise in college establishment, infrastructure planning, and operational excellence
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
