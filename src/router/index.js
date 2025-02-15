import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SubjectView from '@/views/SubjectView.vue'
import SyllabusView from '@/views/SyllabusView.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/:year(1|2|3|4)',
      name: 'exam',
      component: SubjectView
    },
    {
      path: '/syllabus/:code',
      name: 'syllabus',
      component: SyllabusView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/:catchAll(.*)*',
      component: NotFoundComponent
    }
  ]
})

export default router
