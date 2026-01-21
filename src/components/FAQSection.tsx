import React, { useState } from 'react';

const faqs = [
  {
    id: 'faq-1',
    question: 'What is NCISM and why is it important?',
    answer: 'The National Commission for Indian System of Medicine (NCISM) is the statutory body regulating the education and practice of the Indian systems of medicine. Adhering to its regulations is crucial for the legal establishment and operation of ISM colleges.'
  },
  {
    id: 'faq-2',
    question: 'How long does ISM college establishment typically take?',
    answer: 'The timeline varies depending on infrastructure readiness and regulatory approvals, but the process generally takes 1-2 years from application to final approval.'
  },
  {
    id: 'faq-3',
    question: 'What are the minimum infrastructure requirements?',
    answer: 'Requirements include specific land area, hospital bed capacity based on student intake, properly equipped laboratories, herbal gardens, and library facilities as per NCISM norms.'
  },
  {
    id: 'faq-4',
    question: 'What qualifications are required for faculty members?',
    answer: 'Faculty must hold relevant post-graduate qualifications in their respective disciplines, with specific experience requirements for senior positions like Professors and Readers.'
  },
  {
    id: 'faq-5',
    question: 'How does your consultancy ensure compliance?',
    answer: 'We conduct rigorous pre-audits, assist in document preparation, and provide step-by-step guidance based on the latest NCISM gazette notifications and regulations.'
  },
  {
    id: 'faq-6',
    question: 'Is this a government website or private consultancy?',
    answer: 'This is a private consultancy service provided by Kashish Gupta, offering expert guidance on NCISM regulations. We are not a government entity.'
  }
];

const FAQSection: React.FC = () => {
  const [activeId, setActiveId] = useState<string | null>(null);

  const toggleAccordion = (id: string) => {
    setActiveId(activeId === id ? null : id);
  };

  return (
    <section id="faq" className="faq-section">
      <div className="container">
        <h2 className="section-title text-center">Frequently Asked Questions</h2>
        <div className="faq-list">
          {faqs.map((faq, index) => (
            <div key={faq.question} className={`faq-item ${activeIndex === index ? 'active' : ''}`}>
              <button
                className="faq-question"
                onClick={() => toggleAccordion(faq.id)}
                aria-expanded={activeId === faq.id}
              >
                {faq.question}
                <span className="faq-icon">{activeId === faq.id ? '−' : '+'}</span>
              </button>
              <div
                className="faq-answer"
                style={{ maxHeight: activeId === faq.id ? '200px' : '0' }}
              >
                <div className="faq-answer-content">
                  <p>{faq.answer}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FAQSection;
