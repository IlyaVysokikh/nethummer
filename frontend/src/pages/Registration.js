import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { faVk } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import axios from 'axios';

const RegistrationPage = () => {
  const [formData, setFormData] = useState({
    username: '',
    password1: '',
    password2: '',
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:8000/auth/users/', {
        username: formData.username,
        password1: formData.password1,
        password2: formData.password2
      });

      console.log('Успешно зарегистрирован:', response.data);
    } catch (error) {
      console.error('Ошибка регистрации:', error);
    }
  };

  return (
    <div
      className="d-flex justify-content-center align-items-center vh-100"
      style={{
        backgroundImage: `url('/img/fon.png')`,
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backdropFilter: 'blur(5px)',
      }}
    >
      <div style={{ backgroundColor: 'rgba(255, 255, 255, 0.3)', padding: '20px', borderRadius: '10px', backdropFilter: 'blur(1px)',}}>
        <h2 className="text-center mb-4">Регистрация</h2>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="formUsername">
            <Form.Control
              type="text"
              placeholder="Введите имя пользователя"
              name="username"
              value={formData.username}
              onChange={handleInputChange}
              style={{ marginBottom: '10px' }}
              required
            />
          </Form.Group>

          <Form.Group controlId="formPassword">
            <Form.Control
              type="password"
              placeholder="Введите пароль"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              style={{ marginBottom: '10px' }}
              required
            />
          </Form.Group>

          <div className="d-flex justify-content-between align-items-center mt-3">
            <Button variant="primary" type="submit"  >
              Зарегистрироваться
            </Button>
            <div className="d-flex">
            <FontAwesomeIcon icon={faVk} style={{ cursor: 'pointer', fontSize: '42px',marginLeft: '10px', marginRight: '10px', color: '#4a76a8', }} onClick={() => {
              console.log('Авторизация через ВКонтакте');
            }} />
            </div>
          </div>
        </Form>
      </div>
    </div>
  );
};

export default RegistrationPage;
