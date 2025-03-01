<template>
  <div id="app">
    <nav>
      <div class="nav-left">
        <span class="brand-name">Lunova.cloud</span>
      </div>
      <div class="nav-center">
        <router-link to="/" class="nav-link">Solution</router-link>
        <router-link to="/personalized-cycle-tracking" class="nav-link">Resource</router-link>
        <router-link to="/personalized-cycle-tracking" class="nav-link">Platform</router-link>
        <router-link to="/pricing" class="nav-link">Pricing</router-link>
        <router-link to="/about-us" class="nav-link">About Us</router-link>
        <router-link v-if="!isLoggedIn" to="/auth" class="nav-link login">Login</router-link>
        <a v-else @click="logout" class="nav-link login">Logout</a>
      </div>
      <div class="nav-right">
        <div class="language-selector">
          <select v-model="selectedLanguage" class="language-select">
            <option value="en">🇺🇸 English</option>
            <option value="zh">🇨🇳 Chinese</option>
          </select>
        </div>
        <button class="icon-button notification">
          <i class="fas fa-bell"></i>
        </button>
        <button class="icon-button message">
          <i class="fas fa-envelope"></i>
        </button>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedLanguage: 'en',
      isLoggedIn: false // 添加登录状态变量
    }
  },
  mounted() {
    // 检查用户是否已登录
    this.isLoggedIn = !!localStorage.getItem('user');
  },
  methods: {
    logout() {
      // 弹出确认对话框
      if (confirm('Are you sure you want to quit?')) {
        // 清除用户信息并更新登录状态
        localStorage.removeItem('user');
        localStorage.removeItem('userId');
        localStorage.removeItem('username');
        this.isLoggedIn = false;
        this.$router.push('/'); // 可选：重定向到首页
        location.reload(); // 刷新页面
      }
    }
  },
  watch: {
    selectedLanguage(newLang) {
      console.log('Language changed to:', newLang);
    }
  }
}
</script>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

body {
  margin: 0;
  background-color: #ffffff;
  font-family: 'Arial', sans-serif;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 4rem;
  background-color: white;
  box-shadow: 0 4px 20px rgba(213, 63, 140, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-left {
  display: flex;
  align-items: center;
}

.brand-name {
  font-size: 2rem;
  font-weight: bold;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: 0.5px;
}

.nav-center {
  display: flex;
  gap: 2.5rem;
  align-items: center;
}

.nav-link {
  color: #4a5568;
  text-decoration: none;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 0.8rem 1.5rem;
  border-radius: 12px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover {
  color: white;
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(213, 63, 140, 0.2);
}

.nav-link.login {
  border: 2px solid #d53f8c;
  color: #d53f8c;
}

.nav-link.login:hover {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  border-color: transparent;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.icon-button {
  background: none;
  border: none;
  color: #4a5568;
  font-size: 1.2rem;
  cursor: pointer;
  padding: 0.8rem;
  border-radius: 50%;
  width: 45px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.icon-button:hover {
  background: linear-gradient(135deg, #d53f8c, #805ad5);
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(213, 63, 140, 0.2);
}

#app {
  min-height: 100vh;
}

.language-selector {
  position: relative;
  margin-right: 1rem;
}

.language-select {
  appearance: none;
  background: transparent;
  border: 2px solid #d53f8c;
  border-radius: 12px;
  padding: 0.8rem 2.5rem 0.8rem 1.2rem;
  font-size: 1rem;
  color: #d53f8c;
  cursor: pointer;
  transition: all 0.3s ease;
}

.language-select:hover {
  background-color: #fff0f6;
  border-color: #d53f8c;
}

.language-select:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(213, 63, 140, 0.2);
}

.language-selector::after {
  content: '▼';
  font-size: 0.8rem;
  color: #d53f8c;
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
}

@media (max-width: 1024px) {
  nav {
    padding: 1rem 2rem;
  }

  .nav-center {
    gap: 1.5rem;
  }

  .nav-link {
    padding: 0.6rem 1rem;
    font-size: 1rem;
  }
}

@media (max-width: 768px) {
  nav {
    flex-direction: column;
    padding: 1rem;
    gap: 1rem;
  }

  .nav-center {
    flex-direction: column;
    width: 100%;
    gap: 0.5rem;
  }

  .nav-link {
    width: 100%;
    text-align: center;
  }

  .nav-right {
    width: 100%;
    justify-content: center;
    gap: 1rem;
  }

  .language-select {
    padding: 0.6rem 2rem 0.6rem 1rem;
    font-size: 0.9rem;
  }
}
</style>