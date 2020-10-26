<template>

    <div>
        <p>HP:{{ $store.state.hp }}</p>
        <button @click="hp_lose">Click me</button>
    </div>
</template>

<script>
    export default {
        name: "First",
        methods: {
            hp_lose() {
                this.$store.commit("change_hp", -5);
            }
        }
    }
</script>

<style scoped>

</style>
