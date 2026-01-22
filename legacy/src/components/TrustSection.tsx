import React from 'react';

const TrustSection: React.FC = () => {
  return (
    <section className="trust-section">
      <div className="container">
        <div className="trust-grid">
          <div className="trust-card">
            <h3 className="trust-title">ATTORNEY-CLIENT PRIVILEGED</h3>
            <p className="trust-description">
              All consultations are protected under attorney-client privilege.
              Deep insider knowledge of NCISM regulations, procedures,
              and compliance requirements accumulated through years of
              practical experience. Confidentiality guaranteed.
            </p>
          </div>
          <div className="trust-card">
            <h3 className="trust-title">VERIFIED EXPERTISE</h3>
            <p className="trust-description">
              Backed by professional recommendation letters from industry
              experts and regulatory bodies in the ISM sector, recognizing
              expertise in NCISM compliance and institutional development.
              Non-disclosure agreements protect all client information.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default TrustSection;
