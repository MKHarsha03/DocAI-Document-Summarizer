import { createApp } from 'vue'
import App from './App.vue'
import Header from './components/Header.vue'
import PromptCenter from './components/PromptCenter.vue'

const app=createApp(App)
app.component('heading',Header)
app.component('promptpad',PromptCenter)
app.mount('#app')
