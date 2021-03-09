<template>
    <div class="searchboard">
      <div v-for="(item, $index) in list" :key="$index"> <capsule :content=item></capsule> </div>
      <infinite-loading ref="infiniteLoading" @infinite="infiniteHandler" spinner="spiral">
        <div class="nmrmssg" slot="no-more"> That's all folks ! </div>
      </infinite-loading>
      <b-table striped hover :items="items"></b-table>
    </div>
</template>

<script>
/* eslint-disable */
import Capsule from './Capsule'
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'

//var host = 'https://casacoding-back-dot-casacoding.nw.r.appspot.com'
// const host = 'http://127.0.0.1:8080'
const api = 'http://127.0.0.1:8080/api/codeHelper'

export default {
  name: 'Searchboard',
  components: { Capsule, InfiniteLoading },
  props: ['cat_selected', 'purpose'],
  data () {
    return {
      page_order: 0,
      page_size: 2,
      list: []
    }
  },
  computed: {
      filters() {
        return `${this.cat_selected}|${this.purpose}`
      },
    },
  watch: {
    filters: function() {
      this.list = [];
      this.page_order = 0
      this.page_size = 10,
      this.$refs.infiniteLoading.stateChanger.reset();
    }
  },
  methods: {
    infiniteHandler ($state) {
      axios.get(api, {
        params: {
          page_order: this.page_order,
          page_size: this.page_size,
          category: this.cat_selected,
          purpose: this.purpose
        }
      }).then(({ data }) => {
        if (data.response.length) {
          this.page_order += 1
          this.list.push(...data.response)
          $state.loaded()
        } else {
          $state.complete()
        }
      })
    },
  }
}
</script>

<style scoped>
.searchboard {
  width: 65%;
}
h1 {
  margin-left: 1.3em;
  font-size: 1.5em;
}
.nmrmssg {
  font-size: 1.2em;
  font-family:'Lucida Sans Unicode';
}
</style>
