import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Login from "../components/Login";
import Register from "../components/Register";

Vue.use(Router)

export default new Router({
    routes: [
        {path: "/", redirect: "/home"},
        {path: "/home", component: Home, meta: {title: "摸鱼在线教育平台"}},
        {path: "/login", component: Login, meta: {title: "登陆了就可以摸鱼了"}},
        {path: "/register", component: Register, meta: {title: "不注册怎么摸鱼？"}},
    ]
})
