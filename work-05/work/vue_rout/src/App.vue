<template>
    <div id="app">
            <h1>Navigation</h1>

            <router-link to="/HelloWorld">Home</router-link>
            <router-link to="/MessageBoard">MessageBoard</router-link>
            <router-link to="/Information">UserList</router-link>



        <hr>
        <router-view/>
    </div>
</template>

<script>
    export default {
        name: 'App'
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }

</style>
