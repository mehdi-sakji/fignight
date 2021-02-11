<template>
    <div class="searchfilters">
      <div class="searchpanel">
        <div class="slct_ct">
          <label class="lbl"> Category:</label>
          <b-form-select
          class="slct_ct_frm" v-model="cat_selected" :options="cat_options"
          @change='changeSelectedCat'>
          </b-form-select>
        </div>
        <div class="slct_tg">
          <label class="ltg"> Tags:</label>
          <b-form-tags
            tag-variant="primary"
            class="slct_tg_frm"
            tag-pills
            separator=" "
            v-model="tags"
            placeholder="Add tags"
            :limitTagsText="limitTagsText">
          </b-form-tags>
        </div>
        <div class="npt_prps">
          <label class="lpr"> Purpose:</label>
          <b-form-input
            class="npt_prps_frm"
            v-model="purpose"
            type="text"
            @keyup.enter.native='submittedPurpose'
            ></b-form-input>
        </div>
        <div class="npt_cd">
          <label class="lcd"> Code:</label>
          <b-form-input class="npt_cd_frm" v-model="code" type="text"></b-form-input>
        </div>
      </div>
      <div class="newentry">
        <b-button
          class="nw_hlpr_btn"
          variant="outline-primary"
          href="#/insert"> New Helper! </b-button>
      </div>
    </div>
</template>

<script>
/* eslint-disable */
import { mdbSelect } from "mdbvue";
import axios from 'axios'

// const cat_api = 'https://casacoding-back-dot-casacoding.nw.r.appspot.com/api/allcategories'
// const cat_tags = 'https://casacoding-back-dot-casacoding.nw.r.appspot.com/api/alltags'
const cat_api = 'http://35.187.86.233:8080/api/allcategories'
const cat_tags = 'http://35.187.86.233:8080/api/alltags'

export default {
  name: 'Searchfilters',
  components: {
    mdbSelect
  },
  data () {
    return {
      cat_selected: null,
      cat_options: [
          { value: null, text: 'All categories'},
        ],
      tags: [],
      purpose: null,
      code: null
    }
  },
  methods: {
   changeSelectedCat(event) {
      this.$emit('changeSelectedCat', this.cat_selected)
    },
    submittedPurpose(event) {
      this.$emit('submittedPurpose', this.purpose)
    }
  },
  mounted () {
    axios.get(cat_api).then(response => {
      for (let i = 0; i < response.data.response.length; i++)
      {
        this.cat_options.push(
          {
            text: response.data.response[i], value: response.data.response[i]
          })
      }
      })
  }
}
</script>

<style scoped>
.searchfilters {
  width: 30%;
}
.searchpanel {
  background-color:cornsilk;
  padding: 1em;
  border-radius: 0.6em;
  box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
}
.newentry {
  margin-top: 2em;
  padding: 1em;
}
.lbl, .ltg, .lpr, .lcd{
  display: inline-block;
  width: 20%;
  font-weight: bold;
  text-align: left;
  font-size: 1em;
}
.slct_ct_frm, .slct_tg_frm, .npt_prps_frm, .npt_cd_frm{
  display: inline-block;
  width: 60%;
  margin-left:2em;
}
.slct_ct, .slct_tg, .npt_prps, .npt_cd {
  margin-bottom: 1.2em;
}
</style>