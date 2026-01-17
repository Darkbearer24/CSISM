import React from 'react';
import '../App.css';

const IntroSection: React.FC = () => {
  return (
    <section className="intro-section section-padding">
      <div className="container">
        <div className="intro-grid">
          <div className="intro-content">
            <h2 className="section-title">Why Choose <span className="text-highlight">CSISM</span></h2>

            <p className="intro-text">
              <strong className="text-dark">Kashish Gupta</strong>, a consultancy expert with extensive experience in Indian System of Medicine regulatory frameworks and institutional development.
            </p>

            <p className="intro-text">
              With years of deep insider knowledge of <strong className="text-dark">NCISM</strong> (National Commission for Indian System of Medicine) regulations and procedures, we provide simplified, transparent guidance to institutions seeking to establish or enhance their ISM colleges.
            </p>

            <p className="intro-text">
              Our approach combines <strong className="text-dark">regulatory compliance</strong> with practical implementation strategies, ensuring your institution meets all statutory requirements efficiently.
            </p>
          </div>

          <div className="intro-visual">
            <div className="expert-consultation-card">
              <div className="expert-card-content">
                <h3>Expert Consultation</h3>
                <p>Guiding you through every step of the regulatory process.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default IntroSection;
