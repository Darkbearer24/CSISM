import React from 'react';

const CTASection: React.FC = () => {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Form submitted");
    alert("Thank you for your inquiry. We will contact you shortly.");
  };

  return (
    <section id="contact" className="cta-section">
      <div className="container cta-container">
        <div className="cta-content">
          <h2 className="section-title cta-title">Ready to Establish Your ISM College?</h2>
          <p className="cta-description">
            Have questions about establishing your ISM college? Share your details and we'll connect with you promptly.
          </p>
        </div>

        <form className="cta-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <input type="text" placeholder="Full Name" className="form-input" required />
          </div>
          <div className="form-group">
            <input type="email" placeholder="Email Address" className="form-input" required />
          </div>
          <div className="form-group">
            <select className="form-select" defaultValue="">
              <option value="" disabled>Inquiry Type</option>
              <option value="establishment">New College Establishment</option>
              <option value="compliance">Compliance & Audits</option>
              <option value="staffing">Faculty & Staffing</option>
              <option value="other">Other</option>
            </select>
          </div>
          <button type="submit" className="cta-button">SUBMIT INQUIRY</button>
        </form>
      </div>

      <div className="cta-footer">
        <div className="container">
          <p>© 2025 CSISM Consultancy. All rights reserved. | <a href="#">Privacy Policy</a></p>
        </div>
      </div>
    </section>
  );
};

export default CTASection;
