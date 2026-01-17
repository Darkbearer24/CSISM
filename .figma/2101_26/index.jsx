import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.aScreenContactsWithF}>
      <p className={styles.guide}>guide</p>
      <div className={styles.autoWrapper}>
        <div className={styles.textWrapper}>
          <p className={styles.heading4}>
            <span className={styles.heading}>Consultation for&nbsp;</span>
            <span className={styles.heading2}>NCISM</span>
            <span className={styles.heading}>&nbsp;</span>
            <span className={styles.heading3}>Compliant Medical Colleges</span>
          </p>
          <div className={styles.wrapper}>
            <div className={styles.contentWrapper}>
              <p className={styles.contactType}>Location</p>
              <p className={styles.contactData}>123 Main Street, City, Country</p>
            </div>
            <div className={styles.contentWrapper}>
              <p className={styles.contactType}>Phone</p>
              <p className={styles.contactData}>+1 234 567 890</p>
            </div>
            <div className={styles.contentWrapper}>
              <p className={styles.contactType}>Email</p>
              <p className={styles.contactData}>info@csismconsultation.com</p>
            </div>
          </div>
          <div className={styles.buttonWrap}>
            <div className={styles.ctaButton}>
              <p className={styles.ctaText}>Submit Inquiry</p>
            </div>
          </div>
        </div>
        <div className={styles.formWrapper}>
          <p className={styles.formHeading}>Enquiry Form</p>
          <div className={styles.colWrapper}>
            <div className={styles.fieldWrapper}>
              <div className={styles.frame26}>
                <p className={styles.name}>Name</p>
              </div>
              <div className={styles.smallField}>
                <p className={styles.john}>John</p>
              </div>
            </div>
            <div className={styles.fieldWrapper2}>
              <div className={styles.frame26}>
                <p className={styles.name}>Surname</p>
              </div>
              <div className={styles.smallField2}>
                <p className={styles.john}>Doe</p>
              </div>
            </div>
          </div>
          <div className={styles.frame2}>
            <div className={styles.frame28}>
              <p className={styles.name2}>Mail</p>
            </div>
            <div className={styles.smallField3}>
              <p className={styles.john}>johndoe@mail.net</p>
            </div>
          </div>
          <div className={styles.frame3}>
            <div className={styles.frame28}>
              <p className={styles.name2}>Address</p>
            </div>
            <div className={styles.smallField4}>
              <p className={styles.john}>Capitol, WA</p>
            </div>
          </div>
          <div className={styles.frame4}>
            <div className={styles.frame28}>
              <p className={styles.name2}>Description</p>
            </div>
            <div className={styles.bigField} />
          </div>
          <div className={styles.ctaButton2}>
            <p className={styles.ctaText2}>Submit Inquiry</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Component;
