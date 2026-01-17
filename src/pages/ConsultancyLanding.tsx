import React from 'react';
import Header from '../components/Header';
import HeroSection from '../components/HeroSection';
import IntroSection from '../components/IntroSection';
import AboutSection from '../components/AboutSection';
import ServicesSection from '../components/ServicesSection';
import ExpertiseSection from '../components/ExpertiseSection';
import TrustSection from '../components/TrustSection';
import FAQSection from '../components/FAQSection';
import CTASection from '../components/CTASection';

const ConsultancyLanding: React.FC = () => {
  return (
    <div className="consultancy-landing">
      <Header />
      <HeroSection />
      <IntroSection />
      <AboutSection />
      <ServicesSection />
      <ExpertiseSection />
      <TrustSection />
      <FAQSection />
      <CTASection />
    </div>
  );
};

export default ConsultancyLanding;
