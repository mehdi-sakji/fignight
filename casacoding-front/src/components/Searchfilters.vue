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
            placeholder="Search tags"
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
        <div class="newentry">
          <b-button
            class="srch_hlpr_btn"
            variant="info"> Search Helper </b-button>
          <b-button
            class="nw_hlpr_btn"
            variant="info"
            href="#/insert"> New Helper </b-button>
        </div>
      </div>
    </div>
</template>

<script>
/* eslint-disable */
import { mdbSelect } from "mdbvue";
import axios from 'axios'


//var host = 'https://casacoding-back-dot-casacoding.nw.r.appspot.com'
//const host = 'http://127.0.0.1:8080'
const cat_api = 'http://127.0.0.1:8080/api/allcategories'
const tags_api = 'http://127.0.0.1:8080/api/alltags'


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
      tags_options: [],
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
    /*
    tagValidator(tags) {
      for (let i = 0; i < response.data.response.length; i++)
      {
        this.tags_options.push(response.data.response[i])
      }
      return tag in this.tags_options
    }
    */
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
      }),
    axios.get(tags_api).then(response => {
      for (let i = 0; i < response.data.response.length; i++)
      {
        this.tags_options.push(response.data.response[i])
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
  border-color: coral;
  background-color: cornsilk;
  padding: 1em;
  border-radius: 0.6em;
  box-shadow: 5px 5px 5px 5px rgba(0,0,0,0.2);
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
  font-size: 1.2em;
}
.slct_ct_frm, .slct_tg_frm, .npt_prps_frm, .npt_cd_frm{
  display: inline-block;
  width: 60%;
  margin-left:2em;
  font-size: 1.2em;
}
.slct_ct, .slct_tg, .npt_prps, .npt_cd {
  margin-bottom: 1.2em;
}
.nw_hlpr_btn, .srch_hlpr_btn {
  font-size: 1.1em;
  border-radius: 0.6em;
  margin-right: 1em;
}
</style>
