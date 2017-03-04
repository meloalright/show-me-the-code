<template>
  <div class="home">
    home
  </div>
</template>

<script>
export default {
  name: 'todo-home',
  data: () => {
    return {
    }
  },
  methods: {
    /**
     @ 检测cokkie
     @
     @
     **/
    fetchData: function () {
      fetch('http://localhost:8002/fetch/').then((res) => {
        return res.json()
      }).then((data) => {
        console.log(data);
      })
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
</style>
