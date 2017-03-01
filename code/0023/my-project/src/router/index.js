import Vue from 'vue'
import Router from 'vue-router'
import Comments from '@/components/Comments'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Comments',
      component: Comments
    }
  ]
})
