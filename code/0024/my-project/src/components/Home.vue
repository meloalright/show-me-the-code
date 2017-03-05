<template>
  <div class="home">
    <h3 v-for="(str, index) in arr" class="can-through" @click="pop(index)">{{ index+1 }}. {{ str }}</h3>
    <h3 v-show="status">+. <input v-model="newone" placeholder="在这里创建TODO" class="unvisible"/></h3>
    <div class="mt30">
      <button v-show="!status" class="btn-cell blue-btn" @click="enew()">NEW</button>
    </div>
    <div class="mt30">
      <button class="btn-cell blue-btn" @click="save()">SAVE</button>
    </div>
  </div>

</template>

<script>
export default {
  name: 'todo-home',
  data: () => {
    return {
      'arr': [],
      'status': false,
      'newone': ''
    }
  },
  methods: {
    /**
     @ 添加
     **/
    enew: function(index) {
      this.status = true;
    },
    /**
     @ 弹出
     **/
    pop: function(index) {
      let newArr = [];
      for (let i = 0; i < this.arr.length; i++) {
        if (index !== i) {
          newArr.push(this.arr[i]);
        }
      }
      this.arr = newArr;
    },
    /**
     @ 检测cokkie
     @
     @
     **/
    fetchData: function () {
      fetch('http://localhost:8002/fetch/').then((res) => {
        return res.json()
      }).then((data) => {
        this.arr = data.data;
        this.status = false;
        this.newone = '';
      });
    },
    /**
     @ 弹出
     **/
    save: function () {
      let data = {
        'arr': this.arr
      };
      if (this.newone !== '') {
        data.arr.push(this.newone);
      }
      fetch('http://localhost:8002/update/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: encodeURI('arr=' + JSON.stringify(this.arr))
      }).then((res) => {
        return res.json();
      }).then((data) => {
        console.log(data);
        //重刷
        this.fetchData();
      });
    }
  },
  beforeMount: function () {
    this.fetchData();
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

.can-through:hover {
  cursor: pointer;
  color: #ff0000;
  text-decoration:line-through;
}

.unvisible {
  font-size: 16px;
  border: none;
}
</style>
