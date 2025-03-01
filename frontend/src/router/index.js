import { createRouter, createWebHistory } from 'vue-router'
import RealTimeHealthSupport from '../components/RealTimeHealthSupport.vue'
import AskSani from '../components/AskSani.vue'
import AuthLogin from '../components/Auth.vue'

const routes = [
  // ... 其他路由 ...
  {
    path: '/real-time-health-support',
    name: 'RealTimeHealthSupport',
    component: RealTimeHealthSupport
  },
  {
    path: '/ask-sani',
    name: 'AskSani',
    component: AskSani
  },
  {
    path: '/auth',
    name: 'auth',
    component: AuthLogin
  },
]

// ... 其他路由配置 ...