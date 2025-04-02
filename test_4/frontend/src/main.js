import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import { createMemoryHistory, createRouter } from 'vue-router'
import QueryData from './components/QueryData.vue'

const app = createApp(App)

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const routes = [
    { path: '/', component: QueryData}
  ]
  
  const router = createRouter({
    history: createMemoryHistory(),
    routes
  })
  
app.use(router)
app.config.globalProperties.$http = axios
app.mount('#app')
