import Vue from 'vue'
// BootstrapVue
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import App from './App.vue'
import router from './router'
import store from './store'

// 実行モードを表す環境変数。Vue CLI 3を使っている場合は
//   「npm run build」実行時は「production」
//   「npm run serve」実行時は「development」
// 自動的にセットされる
Vue.config.productionTip = process.env.NODE_ENV === 'production'

Vue.use(BootstrapVue)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
