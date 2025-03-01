<template>
    <div class="auth-container gradient-bg">
      <div class="auth-card">
        <div class="auth-header">
          <h1 class="gradient-text">{{ isLogin ? 'Welcome Back' : 'Create Account' }}</h1>
          <p>{{ isLogin ? 'Sign in to access your health services' : 'Join us to get personalized health support' }}</p>
        </div>
        
        <div class="auth-form">
          <div v-if="errorMessage" class="error-message">
            {{ errorMessage }}
          </div>
          
          <!-- 注册时才显示的字段 -->
          <div v-if="!isLogin" class="form-group">
            <label for="name">Full Name</label>
            <input 
              type="text" 
              id="name" 
              v-model="user.name" 
              placeholder="Enter your full name"
            />
          </div>
          
          <div class="form-group">
            <label for="email">Email Address</label>
            <input 
              type="email" 
              id="email" 
              v-model="user.email" 
              placeholder="Enter your email"
            />
          </div>
          
          <div class="form-group">
            <label for="password">Password</label>
            <input 
              type="password" 
              id="password" 
              v-model="user.password" 
              placeholder="Enter your password"
            />
          </div>
          
          <div v-if="!isLogin" class="form-group">
            <label for="confirmPassword">Confirm Password</label>
            <input 
              type="password" 
              id="confirmPassword" 
              v-model="user.confirmPassword" 
              placeholder="Confirm your password"
            />
          </div>
          
          <button @click="submitForm" class="auth-button">
            {{ isLogin ? 'Sign In' : 'Create Account' }}
          </button>
          
          <div class="auth-toggle">
            {{ isLogin ? 'Don\'t have an account?' : 'Already have an account?' }}
            <span @click="toggleAuthMode" class="toggle-link">
              {{ isLogin ? 'Sign Up' : 'Sign In' }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'AuthLogin',
    data() {
      return {
        isLogin: true,
        user: {
          name: '',
          email: '',
          password: '',
          confirmPassword: ''
        },
        errorMessage: ''
      };
    },
    methods: {
      toggleAuthMode() {
        this.isLogin = !this.isLogin;
        this.errorMessage = '';
        this.user = {
          name: '',
          email: '',
          password: '',
          confirmPassword: ''
        };
      },
      async submitForm() {
        this.errorMessage = '';
        
        // 表单验证
        if (this.isLogin) {
          if (!this.user.email || !this.user.password) {
            this.errorMessage = '请填写所有必填字段';
            return;
          }
        } else {
          if (!this.user.name || !this.user.email || !this.user.password || !this.user.confirmPassword) {
            this.errorMessage = '请填写所有必填字段';
            return;
          }
          
          if (this.user.password !== this.user.confirmPassword) {
            this.errorMessage = '两次输入的密码不一致';
            return;
          }
        }
        
        try {
          let response;
          
          if (this.isLogin) {
            // 登录请求 - 只需要email和password
            response = await axios.post('http://localhost:8000/api/auth/login', {
              email: this.user.email,
              password: this.user.password
            });
          } else {
            // 注册请求 - 根据users表结构，只需要email和password
            response = await axios.post('http://localhost:8000/api/auth/register', {
              email: this.user.email,
              password: this.user.password
            });
          }
          
          if (response.data.success) {
            // 只存储用户信息，不使用token
            localStorage.setItem('user', JSON.stringify(response.data.user));
            localStorage.setItem('userId', response.data.user.user_id);
            
            // 重定向到首页或仪表板
            this.$router.push('/dashboard');
          } else {
            this.errorMessage = response.data.message || '操作失败，请重试';
          }
        } catch (error) {
          console.error('Auth error:', error);
          this.errorMessage = error.response?.data?.message || '服务器错误，请稍后重试';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .gradient-bg {
    background: linear-gradient(135deg, #fff0f6, #faf5ff);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
  }
  
  .auth-container {
    width: 100%;
  }
  
  .auth-card {
    background: white;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(213, 63, 140, 0.1);
    max-width: 800px; /* 调整宽度为800px */
    width: 90%; /* 添加宽度百分比确保响应式 */
    margin: 0 auto;
    overflow: hidden;
  }
  
  /* 添加更多内部间距，使表单看起来更宽敞 */
  .auth-form {
    padding: 2.5rem 4rem 4rem; /* 增加左右内边距 */
  }
  
  /* 在小屏幕上保持合理的内边距 */
  @media (max-width: 768px) {
    .auth-card {
      max-width: 100%;
      width: 95%;
    }
    
    .auth-header, .auth-form {
      padding: 1.5rem 2rem;
    }
  }
  .auth-header {
    padding: 2.5rem 2.5rem 1.5rem;
    text-align: center;
  }
  
  .gradient-text {
    font-size: 2.2rem;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #d53f8c, #805ad5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  
  .auth-header p {
    color: #4a5568;
    font-size: 1.1rem;
    margin-bottom: 0;
  }
  
  .auth-form {
    padding: 2rem 3rem 3rem; /* 增加内边距 */
  }
  
  .form-group {
    margin-bottom: 1.8rem; /* 增加表单组之间的间距 */
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
    color: #2d3748;
    font-weight: 500;
    font-size: 1.05rem; /* 稍微增加标签字体大小 */
  }
  
  input {
    width: 100%;
    padding: 1.2rem; /* 增加输入框内边距 */
    border: 2px solid rgba(213, 63, 140, 0.2);
    border-radius: 12px;
    font-size: 1.05rem; /* 增加输入框字体大小 */
    transition: all 0.3s ease;
  }
  
  input:focus {
    outline: none;
    border-color: #d53f8c;
    box-shadow: 0 0 0 3px rgba(213, 63, 140, 0.1);
  }
  
  .auth-button {
    width: 100%;
    padding: 1.3rem; /* 增加按钮高度 */
    background: linear-gradient(135deg, #d53f8c, #805ad5);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 1.2rem; /* 增加按钮字体大小 */
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 1.5rem; /* 增加按钮上方间距 */
  }
  
  .auth-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(213, 63, 140, 0.2);
  }
  
  .auth-toggle {
    text-align: center;
    margin-top: 2rem; /* 增加切换链接上方间距 */
    color: #4a5568;
    font-size: 1.05rem; /* 增加字体大小 */
  }
  
  .toggle-link {
    color: #d53f8c;
    cursor: pointer;
    font-weight: 600;
    margin-left: 0.5rem;
  }
  
  .toggle-link:hover {
    text-decoration: underline;
  }
  
  .error-message {
    background-color: #fff5f5;
    color: #e53e3e;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(229, 62, 62, 0.2);
  }
  
  @media (max-width: 768px) {
    .auth-card {
      max-width: 100%;
    }
    
    .auth-header, .auth-form {
      padding: 1.5rem;
    }
  }
  </style>