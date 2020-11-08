<template>
    <div class="box">
        <img src="../../static/image/1111.jpg" alt="">
        <div class="register">
            <div class="register_box">
                <div class="register-title">摸鱼教育在线平台注册</div>
                <div class="inp">
                    <input v-model="phone" type="text" placeholder="手机号码" class="user" @blur="check_phone">
                    <input v-model="password" type="password" placeholder="登录密码" class="user">

                    <div class="sms-box">
                        <input v-model="code" type="text" maxlength="6" placeholder="输入验证码" class="user">
                        <div v-if="smsbtn" class="sms-btn" @click="get_code">
                            获取验证码
                        </div>
                        <div v-else class="sms-btn uninteractive">
                            {{ wait }}秒后重新发送
                        </div>
                    </div>
                    <button class="register_btn" @click="user_register">注册</button>
                    <p class="go_login">已有账号直接登陆
                        <router-link to="/login">开始摸鱼</router-link>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import SMSCode from "./common/SMSCode";

    import Header from "./common/Header";
    import Footer from "./common/Footer";
    import Banner from "./common/Banner";

    export default {
        name: "Register",
        components: {
            SMSCode: SMSCode,
        },
        data() {
            return {
                phone: "",
                password: "",
                code: "",
                smsbtn: true,
                wait: 60,
            }
        },
        methods: {
            // 用户注册的逻辑
            user_register() {
                this.$axios({
                    url: this.$settings.HOST + "user/register/",
                    method: "post",
                    data: {
                        phone: this.phone,
                        password: this.password,
                        code: this.code,
                    }
                }).then(res => {
                    console.log(res.data);
                    if (res.data.token) {
                        // 将token信息保存
                        sessionStorage.token = res.data.token;

                        this.$message.success("注册成功，即将跳转到首页")
                        // 跳转到首页
                        setTimeout(() => this.$router.push("/"), 1000)

                    }
                }).catch(error => {
                    this.$message.error("用户名或密码不合格")
                })
            },
            // 检查手机号是否被注册
            check_phone() {
                this.$axios({
                    url: this.$settings.HOST + "user/phone/",
                    method: "get",
                    params: {
                        phone: this.phone,
                    }
                }).catch(error => {
                    this.$message.error(error.response.data)
                })
            },

            // 根据手机号获取验证码
            get_code() {
                this.$axios({
                    url: this.$settings.HOST + "user/send/",
                    method: "get",
                    params: {
                        phone: this.phone
                    }
                }).then(res => {
                    console.log(res);
                    this.smsbtn = false;
                    this.wait = res.data.wait;
                    this.wait_send();

                }).catch(error => {
                    console.log(error);
                })
            },
            // 等待重新发送短信
            wait_send() {
                setTimeout(() => {
                    if (--this.wait <= 0) {
                        this.smsbtn = true;

                    } else {
                        this.wait_send();
                    }
                }, 1000)
            }
        },
    }
</script>

<style scoped>
    .box {
        width: 100%;
        height: 100%;
        position: relative;
        overflow: hidden;
    }

    .box img {
        width: 100%;
        min-height: 100%;
    }

    .box .register {
        position: absolute;
        width: 500px;
        height: 400px;
        top: 0;
        left: 0;
        margin: auto;
        right: 0;
        bottom: 0;
        top: -338px;
    }

    .register .register-title {
        width: 100%;
        font-size: 24px;
        text-align: center;
        padding-top: 30px;
        padding-bottom: 30px;
        color: #4a4a4a;
        letter-spacing: .39px;
    }

    .register-title img {
        width: 190px;
        height: auto;
    }

    .register-title p {
        font-family: PingFangSC-Regular;
        font-size: 18px;
        color: #fff;
        letter-spacing: .29px;
        padding-top: 10px;
        padding-bottom: 50px;
    }

    .register_box {
        width: 400px;
        height: auto;
        background: #fff;
        box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
        border-radius: 4px;
        margin: 0 auto;
        padding-bottom: 40px;
    }

    .register_box .title {
        font-size: 20px;
        color: #9b9b9b;
        letter-spacing: .32px;
        border-bottom: 1px solid #e6e6e6;
        display: flex;
        justify-content: space-around;
        padding: 50px 60px 0 60px;
        margin-bottom: 20px;
        cursor: pointer;
    }

    .register_box .title span:nth-of-type(1) {
        color: #4a4a4a;
        border-bottom: 2px solid #84cc39;
    }

    .inp {
        width: 350px;
        margin: 0 auto;
    }

    .inp input {
        border: 0;
        outline: 0;
        width: 100%;
        height: 45px;
        border-radius: 4px;
        border: 1px solid #d9d9d9;
        text-indent: 20px;
        font-size: 14px;
        background: #fff !important;
    }

    .inp input.user {
        margin-bottom: 16px;
    }

    .inp .rember {
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        margin-top: 10px;
    }

    .inp .rember p:first-of-type {
        font-size: 12px;
        color: #4a4a4a;
        letter-spacing: .19px;
        margin-left: 22px;
        display: -ms-flexbox;
        display: flex;
        -ms-flex-align: center;
        align-items: center;
        /*position: relative;*/
    }

    .inp .rember p:nth-of-type(2) {
        font-size: 14px;
        color: #9b9b9b;
        letter-spacing: .19px;
        cursor: pointer;
    }

    .inp .rember input {
        outline: 0;
        width: 30px;
        height: 45px;
        border-radius: 4px;
        border: 1px solid #d9d9d9;
        text-indent: 20px;
        font-size: 14px;
        background: #fff !important;
    }

    .inp .rember p span {
        display: inline-block;
        font-size: 12px;
        width: 100px;
        /*position: absolute;*/
        /*left: 20px;*/

    }

    #geetest {
        margin-top: 20px;
    }

    .register_btn {
        width: 100%;
        height: 45px;
        background: #84cc39;
        border-radius: 5px;
        font-size: 16px;
        color: #fff;
        letter-spacing: .26px;
        margin-top: 30px;
    }

    .inp .go_login {
        text-align: center;
        font-size: 14px;
        color: #9b9b9b;
        letter-spacing: .26px;
        padding-top: 20px;
    }

    .inp .go_login span {
        color: #84cc39;
        cursor: pointer;
    }

    .sms-box {
        position: relative;
    }

    .sms-btn {
        font-size: 14px;
        color: #ffc210;
        letter-spacing: .26px;
        position: absolute;
        right: 16px;
        top: 10px;
        cursor: pointer;
        overflow: hidden;
        background: #fff;
        border-left: 1px solid #484848;
        padding-left: 16px;
        padding-bottom: 4px;
    }

    .sms-box .uninteractive {

        color: #9b9b9b;
        cursor: not-allowed;
    }
</style>
