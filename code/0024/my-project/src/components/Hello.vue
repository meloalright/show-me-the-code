<template>
  <div class="hello">
    <div class="input-line">
      <input placeholder="请输入访问密码" type="password" class="input-cell" v-model="password" @click="pop()"></input>
    </div>
    <div class="mt30">
      <button class="btn-cell blue-btn" @click="login()">LOGIN</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'todo',
  data: () => {
    return {
      'password': ''
    }
  },
  methods: {
    /**
     @
     @
     @ 登录
     @
     @
    **/
    login: function() {
      fetch('http://localhost:8002/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: encodeURI('password=' + this.password)
      }).then((res) => {
        return res.json();
      }).then((data) => {
        if (data.code === '200' || data.code === 200) {
          location.href = '/#/home';
        }
        else {
          this.password = '';
        }
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input,button,select,textarea {
  outline:none
}
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.input-line {
  margin: 10px 0;
}
.input-cell {
  width: 250px;
  font-size: 12px;
  line-height: 22px;
  text-indent: 5px;
  border: solid 1px #ccc;
}



.mt30 {
  margin-top: 30px;
}
.btn-line {
  margin: 10px 0 0 0;
}
.btn-cell {
  cursor: pointer;
  width: 200px;
  font-size: 12px;
  line-height: 22px;
  transition: 0.4s width ease-in-out;
}

.btn-cell:hover {
  cursor: pointer;
  width: 220px;
  font-size: 12px;
  line-height: 22px;
}

.blue-btn {
  border: solid 1px #38a6ec;
  background-color: #38a6ec;
  color: #FFF;
}
.light-btn {
  border: solid 1px #38a6ec;
  background-color: #FFF;
  color: #38a6ec;
}
</style>
