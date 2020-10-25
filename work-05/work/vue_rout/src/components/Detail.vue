<template>
    <div>
        <h3>UserDetail</h3>
        <table>
            <tr>
                <td>Id</td>
                <td>{{ $route.params.id }}</td>
            </tr>
            <tr>
                <td>Username</td>
                <td>{{ username }}</td>
            </tr>
            <tr>
                <td>Birthday</td>
                <td>{{ birthday }}</td>
            </tr>
            <tr>
                <td>Information</td>
                <td>{{ information }}</td>
            </tr>
        </table>

    </div>
</template>

<script>
    export default {
        name: "Detail",
        data() {
            return {
                username: "",
                birthday: "",
                information: "",
            }
        },
        methods: {
            init() {
                let id = parseInt(this.$route.params.id);
                let user = JSON.parse(localStorage.users).find(x => x.id === id);
                console.log(user);
                this.username = user.username;
                this.birthday = user.birthday;
                this.information = user.information;
            },
        },
        created: function () {
            this.init();
        },
    }
</script>

<style scoped>
    table {
        margin: auto;
        border: dashed 1px blueviolet;
        padding: 10px;

    }
</style>
