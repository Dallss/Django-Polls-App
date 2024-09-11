import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import PollView from '@/views/PollView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView
    },
    { 
      path: '/poll/:id', 
      name: 'poll-detail', 
      component: PollView, 
      props: true 
    }
  ]
})

export default router
