<template>
  <div class="root">
    <div class="input">
      <input class="input-name" placeholder="姓名" v-model="input.name">
      <input class="input-comment" placeholder="内容" v-model="input.comment">
    </div>
    <div class="submit">
      <button class="input-submit" v-on:click="postComment()">发布</button>
    </div>
    <div class="list">
      <h3 v-for="item in commentsList">{{ item.name }}:{{ item.comment }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Comments',
  data: function () {
    return {
      input: {
        'name': '',
        'comment': ''
      },
      commentsList: [
        {
          'name': '正在',
          'comment': '加载数据...'
        }
      ]
    }
  },
  methods: {
    /*
     @ 请求获取信息
     **/
    fetchComments: function () {
      fetch('http://localhost:8002/fetch/').then((res) => {
        return res.json()
      }).then((data) => {
        this.commentsList = data.data
      })
    },
    /*
     @ 请求提交信息
     **/
    postComment: function () {
      var that = this
      var obj = {
        'name': this.input.name,
        'comment': this.input.comment
      }
      obj.name = (obj.name === '' ? 'vue' : obj.name)
      obj.comment = (obj.comment === '' ? '什么也没说' : obj.comment)
      //

      //
      fetch('http://localhost:8002/submit/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: encodeURI('name=' + obj.name + '&comment=' + obj.comment)
      }).then((res) => {
        if (res.ok) {
          // 重置
          that.resetInput()
          // 再拉新请求
          setTimeout(that.fetchComments, 1000)
        }
      })
    },
    /*
     @ 重置
     **/
    resetInput: function () {
      this.input.name = ''
      this.input.comment = ''
      this.commentsList = [
        {
          'name': '正在',
          'comment': '加载数据...'
        }
      ]
    }
  },
  beforeMount: function () {
    this.fetchComments()
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

.input-name {
  font-size: 16px;
  text-indent: 5px;
  line-height: 26px;
  width: 100px;
}

.input-comment {
  font-size: 16px;
  text-indent: 5px;
  line-height: 26px;
  width: 450px;
}

.submit {
  border: 0;
  margin: 20px 0 0 0;
}
.input-submit {
  border: 0;
  color: #FFF;
  width: 100px;
  font-size: 16px;
  line-height: 26px;
  text-align: center;
  background-color: rgb(65, 184, 131);
}
.input-submit:hover{
  cursor: pointer;
  background-color: rgb(53, 73, 94);
}

</style>
