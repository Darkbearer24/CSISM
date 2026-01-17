import React from 'react';
import '../App.css';

const ServicesSection: React.FC = () => {
  const services = [
    {
      title: "NCISM Regulatory Framework",
      description: "Comprehensive understanding of NCISM-mandated procedures and processes for college establishment, presented in simplified and actionable format."
    },
    {
      title: "Document Preparation & Compliance",
      description: "Expert guidance on preparing all required documents according to NCISM regulations and laws for seamless approval processes."
    },
    {
      title: "Faculty & Academic Structure",
      description: "Complete advisory on teacher codes assignment, faculty qualifications, and compliance with NCISM norms for teaching staff."
    },
    {
      title: "Infrastructure & Operations",
      description: "Detailed planning for Ayurvedic, Unani, and Siddha college infrastructure, facilities, and operational requirements."
    },
    {
      title: "Compliance Verification",
      description: "Verification and validation of your institution against NCISM standards to ensure full regulatory compliance."
    },
    {
      title: "Specialized Consulting",
      description: "Specialized advisory for unique queries related to ISM college establishment and regulatory matters not covered elsewhere."
    }
  ];

  return (
    <section id="services" className="services-section section-padding">
      <div className="container">
        <h2 className="section-title text-center">Areas of <span className="text-highlight">Expertise</span></h2>

        <div className="services-grid">
          {services.map((service, index) => (
            <div key={index} className="service-card">
              <h3 className="service-title">{service.title}</h3>
              <p className="service-description">{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ServicesSection;
