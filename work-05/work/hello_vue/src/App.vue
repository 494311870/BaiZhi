<template>
    <div id="app">
        <img src="./assets/logo.png">
        <First/>
        <HelloWorld/>

    </div>
</template>

<script>
    import HelloWorld from './components/HelloWorld'
    import First from "./components/First";

    export default {
        name: 'App',
        components: {
            HelloWorld,
            First,
        }
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
