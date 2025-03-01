// front/src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import PersonalizedCycleTracking from './components/PersonalizedCycleTracking.vue'
import AskSani from './components/AskSani.vue'
import RealTimeHealthSupport from './components/RealTimeHealthSupport.vue'
import ChangeMood from './components/ChangeMood.vue'
import AboutUs from '@/components/AboutUs.vue'
import NextInspection from './components/NextInspection.vue'
import SanitaryProducts from './components/SanitaryProducts.vue'
import DietAdvice from './components/Diet.vue'
import AuthLogin from './components/Auth.vue'

import 'vue-cal/dist/vuecal.css'

const routes = [
  { path: '/', component: PersonalizedCycleTracking },
  { path: '/personalized-cycle-tracking', component: PersonalizedCycleTracking },
  { path: '/ask-sani', component: AskSani },
  { path: '/real-time-health-support', component: RealTimeHealthSupport },
  { path: '/change-mood', component: ChangeMood },
  { path: '/about-us', component: AboutUs },
  // 添加新的路由
  { path: '/next-inspection', component: NextInspection },
  { path: '/sanitary-products', component: SanitaryProducts },
  { path: '/diet', component: DietAdvice },
  { path: '/auth', component: AuthLogin }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

createApp(App).use(router).mount('#app')