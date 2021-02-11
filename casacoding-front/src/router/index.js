import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Insert from '@/components/Insert'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/insert',
      component: Insert
    }
  ]
})
