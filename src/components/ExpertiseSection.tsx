import React from 'react';

const expertiseItems = [
  {
    title: 'NCISM Regulatory Framework',
    description: 'Comprehensive understanding of NCISM-mandated procedures and processes for college establishment. All guidance provided adheres strictly to the National Commission for Indian System of Medicine regulations and official guidelines.'
  },
  {
    title: 'Education & Professional Qualifications',
    description: 'Detailed requirements for faculty qualifications, teacher codes assignment, and compliance with NCISM norms for teaching staff. Ensuring all academic structures meet official regulatory standards.'
  },
  {
    title: 'Affiliation & Recognition Rules',
    description: 'Complete guidance on affiliation procedures, college recognition processes, and relationship with affiliated universities. Understanding the complete pathway to institutional validation.'
  },
  {
    title: 'Compliance & Audit Standards',
    description: 'Verification and validation of institutions against NCISM standards. Regular compliance audits and maintenance of all statutory requirements for continuous operational excellence.'
  }
];

const ExpertiseSection: React.FC = () => {
  return (
    <section id="expertise" className="expertise-section">
      <div className="container">
        <div className="expertise-grid">
          {expertiseItems.map((item, index) => (
            <div key={index} className="expertise-card">
              <h3 className="expertise-title">{item.title}</h3>
              <p className="expertise-description">{item.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ExpertiseSection;
