<template>
    <div class="sms-box">
        <input v-model="code" type="text" maxlength="6" placeholder="输入验证码" class="user">
        <div v-if="smsbtn" class="sms-btn" @click="get_code">
            获取验证码
        </div>
        <div v-else class="sms-btn uninteractive">
            {{ wait }}秒后重新发送
        </div>
    </div>
</template>

<script>
    export default {
        name: "SMSCode",
        data() {
            return {

                code: "",
                smsbtn: true,
                wait: 60,
            }
        },
        methods: {
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
