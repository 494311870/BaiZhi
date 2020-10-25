<template>
    <div>
        This is My First Components!
        <p>{{ msg }}</p>
        <button @click="func">What happen?</button>

    </div>

</template>

<script>
    export default {
        name: "First",
        data() {
            return {
                msg: 'This msg from First.'
            }
        },
        methods:{
            func(){
                this.msg = "Nothing happen."
            }
        }
    }
</script>

<style scoped>
    div {
        color: blueviolet;
    }
</style>
