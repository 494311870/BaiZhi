<template>
    <div>

        <h3>UserList</h3>

        <table border="2">
            <tr>
                <td>ID</td>
                <td>Name</td>
                <td>Birthday</td>
                <td>Information</td>
                <td>Operation</td>
            </tr>
            <tr v-for="(user,index) in users" :key="user.id">
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.birthday }}</td>
                <td>{{ user.information }}</td>
                <td><a href="javascript:void(0)" @click="remove_user(index)">Delete</a> |
                    <router-link :to="`/detail/${user.id}`">Detail</router-link>
                </td>
            </tr>
        </table>

        <hr>
        <button @click="add_user">Add User</button>
        <table id="add">
            <tr>
                <td>用户名:</td>
                <td><input type="text" v-model="username"></td>
            </tr>
            <tr>
                <td>生日:</td>
                <td><input type="text" v-model="birthday"></td>
            </tr>
            <tr>
                <td>个人信息:</td>
                <td><input type="text" v-model="information"></td>
            </tr>
        </table>


    </div>
</template>

<script>
    export default {
        name: "Information",
        data() {
            return {
                users: [
                    {id: 1, username: "Tom", birthday: "2010-10-10", information: 'Hello'},
                    {id: 2, username: "Bob", birthday: "2011-11-11", information: 'You\'re a real talent'},
                    {id: 3, username: "Jerry", birthday: "2012-12-12", information: 'What happen?'},
                ],
                auto_id: 4, // 应该私有然后封装成属性
                username: "",
                birthday: "",
                information: "",
            }
        },
        methods: {
            init() {
                console.log("Init......");
                if (localStorage.users) {
                    this.users = JSON.parse(localStorage.users);
                } else {
                    localStorage.users = JSON.stringify(this.users);
                }
                if (localStorage.auto_id) {
                    this.auto_id = localStorage.auto_id;
                } else {
                    localStorage.auto_id = this.auto_id;
                }

            },
            add_user() {
                if (this.username.trim() && this.birthday.trim() && this.information.trim()) {
                    console.log(this.auto_id);
                    this.users.push({
                        id: this.auto_id++,
                        username: this.username.trim(),
                        birthday: this.birthday.trim(),
                        information: this.information.trim(),
                    })
                    this.username = "";
                    this.birthday = "";
                    this.information = "";

                } else {
                    alert("用户信息不能有任何一项为空！")
                }
                // 获取到三个用户信息
            },
            remove_user(index) {
                this.users.splice(index, 1);
            },
            save_data() {
                console.log("Save......");
                localStorage.users = JSON.stringify(this.users);
                localStorage.auto_id = this.auto_id;
            }
        },
        created: function () {
            this.init();
        },
        updated() {
            this.save_data();
        }

    }
</script>

<style scoped>
    table {
        margin: auto;

    }

    #add {
        text-align: right;
    }

</style>
