import Vue from 'vue'
import Router from 'vue-router'

import HelloWorld from '@/components/HelloWorld'
import MessageBoard from "../components/MessageBoard";
import Information from "../components/Information";
import Detail from "../components/Detail";

Vue.use(Router)

export default new Router({
    routes: [

        {
            path: '/HelloWorld',
            name: 'HelloWorld',
            component: HelloWorld
        },
        {
            path: '/MessageBoard',
            name: 'MessageBoard',
            component: MessageBoard
        },
        {
            path: '/Information',
            name: 'Information',
            component: Information
        },
        {
            path: '/Detail/:id',
            name: 'Detail',
            component: Detail
        },
        {
            path: '/*',
            name: 'HelloWorld',
            component: HelloWorld
        },
    ]
})
