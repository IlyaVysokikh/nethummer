
import React from 'react';
import styles from './Header.module.css';

function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>
      <img src="/img/logo.png" />
      <span>Обучающая платформа KGU</span>
      </div>
      <nav className={styles.navbar}>
        <ul>
          <li><a href="#home">Главная</a></li>
          <li><a href="#courses">Курсы</a></li>
          <li><a href="#about">О нас</a></li>
          <li><a href="#contact">Контакты</a></li>
          <li><a href="#home">Войти</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
