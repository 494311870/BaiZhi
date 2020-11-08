// 导包 vue  vuex
import Vue from 'vue'
import Vuex from 'vuex'

// 将vuex注入到vue实例中
Vue.use(Vuex)


// 将定义好的vuex导出
export default new Vuex.Store({
    state: {sms_code: ""},
    mutations: {},
    getters: {},
})
