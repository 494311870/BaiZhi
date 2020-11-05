// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// 导入element-ui 以及样式
import ElementUI from 'element-ui'
import "element-ui/lib/theme-chalk/index.css"

// 导入全局演样式
import "../static/css/global.css"

import settings from "./settings";

Vue.prototype.$settings = settings;

// 配置axios
import axios from "axios"
// 将axios注入到vue实例
Vue.prototype.$axios = axios
// 极验验证码
import "../static/js/gt"
// 全局注册
Vue.use(ElementUI)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: {App},
    template: '<App/>'
})
