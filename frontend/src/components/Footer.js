import React from 'react';
import styles from './Footer.module.css';
import EmailIcon from '@mui/icons-material/Email'; 
import GitHubIcon from '@mui/icons-material/GitHub';
import TelegramIcon from '@mui/icons-material/Telegram';

function Footer() {
  return (
    <footer className={styles.footer}>
      <p>Обучайтесь с нами</p>
      <div className={styles.icons}>
        <EmailIcon />
        <GitHubIcon />
        <TelegramIcon />
      </div>
    </footer>
  );
}

export default Footer;