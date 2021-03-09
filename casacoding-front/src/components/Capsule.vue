<template>
  <div class="capsule">
    <b-card no-body>
      <b-card-body>
        <div class="cp_dt"> {{ format_date(content.created) }} </div>
        <div class="cp_tgs">
          <b-badge class="ml-2 cat">
              {{ content.category }}
          </b-badge>
        </div>
        <div class="cp_tgs">
            <b-badge class="ml-2 tg" v-for="tag in content.tags.split(',')" v-bind:key="tag">
              {{tag}}
            </b-badge>
          </div>
        <div class="cp_prps">
          <b-icon icon="pen"></b-icon> <span> {{ content.purpose }} </span>
        </div>
        <div class="cp_cd_cntnr">
          <pre class="cp_cd"><code>{{content.code.replace('\t', '    ')}}</code></pre>
        </div>
      </b-card-body>
      <b-card-footer>
        <b-button variant="info" class="cp_btn"
                  v-clipboard:copy="content.code"> Copy </b-button>
      </b-card-footer>
    </b-card>
  </div>
</template>

<script>
/* eslint-disable */
import moment from 'moment'
import { BIcon } from 'bootstrap-vue'

export default {
  components: {
    BIcon
  },
  name: 'Capsule',
  props: ['content', 'tags', 'picture'],
  computed: {
    parsedTags: function () {
      return JSON.parse(this.tags)
    }
  },
  data () {
    return {
      image: require('../assets/' + this.picture),
      copiedCode: 'text code example'
    }
  },
  methods: {
      format_date(value){
         if (value) {
           return value
          }
      },
      handleSuccess(e) {
            console.log(e);
      },
      handleError(e) {
          console.log(e);
      }
   }
}
</script>

<style scoped>
b-card{
  border-color: coral;
}
.capsule {
  position: relative;
  left: 2em;
  box-shadow: 5px 5px 5px 5px rgba(0.2,0.2,0.2,0.2);
  border-radius: 0.6em;
  background-color: white;
  margin-bottom: 1.5em;
  width: 90%;
}
.cp_tgs
{
  line-height: 2%;
}
.tg, .cat
{
  background-color:blue;
  font-size: 1.1em;
  font-weight:lighter;
  cursor: pointer;
  margin-left: 0.4em;
  margin-bottom: 0.4em;
  border-radius: 0.6em;
}
.tg
{
  background-color:darkgreen;
}
.cat
{
  background-color:cadetblue;
}
.tg:hover {
  background-color:purple;
  transition-duration: 0.2s;
}
.cat:hover {
  background-color:purple;
  transition-duration: 0.2s;
}
.cp_prps, .cp_cd_cntnr, .cp_thr
{
  margin-left: 0.4em;
  margin-right: 0.4em;
  margin-bottom: 0.6em;
}
.cp_cd_cntnr {
  border-radius: 0.2em;
}
.cp_prps
{
  font-size: 1.2em;
}
.cp_cd_cntnr {
  background-color:midnightblue;
  padding: 1em;
  border-radius: 0.6em;
}
.cp_cd {
  color: white;
  font-size: 1.1em;
  font-family: 'Courier New', Courier, monospace;
}
.cp_dt
{
  margin-left: 0.4em;
  margin-bottom: 0.4em;
  color:cadetblue;
  font-weight:lighter;
  font-style: italic;
  font-size: 1.2em;
}
.cp_btn{
  font-size: 1.1em;
  border-radius: 0.6em;
}
</style>
