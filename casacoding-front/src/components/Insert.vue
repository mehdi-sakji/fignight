<template>
  <div id="root">
    <meta name="viewport" content="width=device-width, user-scalable=no">
    <pageheader></pageheader>
    <div id="content">
      <div class="insertpanel">
        <b-form @submit="onSubmit" @reset="onReset">
          <div class="npt_ct">
            <label class="lbl"> Category:</label>
            <b-form-input
              class="npt_ct_frm"
              v-model="form.category">
            </b-form-input>
          </div>
          <div class="npt_tg">
            <label class="ltg"> Tags:</label>
            <b-form-tags
              tag-variant="primary"
              class="npt_tg_frm"
              tag-pills
              separator=" "
              v-model="form.tags"
              placeholder="Add tags"
              :limitTagsText="limitTagsText">
            </b-form-tags>
          </div>
          <div class="npt_prps">
            <label class="lpr"> Purpose:</label>
            <b-form-input
              class="npt_prps_frm"
              v-model="form.purpose">
            </b-form-input>
          </div>
          <div class="npt_cd">
            <label class="lcd"> Code:</label>
            <b-form-textarea
              class="npt_cd_frm" rows="6"
              placeholder="Place code here..."
              v-model="form.code">
            </b-form-textarea>
          </div>
          <div class="sbmt_rst">
            <b-button
              class="sbmt_btn" type="submit"
              variant="outline-primary"> Submit </b-button>
            <b-button
              class="rst_btn" type="reset"
              variant="outline-primary"> Reset </b-button>
          </div>
        </b-form>
      </div>
      <div class="backtotimeline">
        <b-button
          variant="outline-primary"
          href="#/"> Back to Timeline! </b-button>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import Pageheader from './Pageheader'
import axios from 'axios'

// const insert_api = 'https://casacoding-back-dot-casacoding.nw.r.appspot.com/api/codeHelper'
const insert_api = 'http://35.187.86.233:8080/api/codeHelper'

export default {
  name: 'Insert',
  components: {Pageheader},
  data() {
      return {
        form: {
          category: null,
          tags: [],
          purpose: null,
          code: null
        }
      }
    },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      axios.post(insert_api, {
        category: this.form.category,
        tags: this.form.tags,
        purpose: this.form.purpose,
        code: this.form.code
      }).then(response => {
        alert('New helper inserted !')
      })
    },
    onReset(event) {
      event.preventDefault()
      this.form.category = null
      this.form.tags = []
      this.form.purpose = null
      this.form.code = null
    }
  }
}
</script>

<style scoped>
#content > div{
  float:left;
  margin-left:1%;
  margin-top:7%;
}
#content {
  width: 40%;
  margin-top: 4em;
}
.insertpanel {
  background-color:cornsilk;
  padding: 1em;
  border-radius: 0.6em;
  box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  width: 90%;
}
.backtotimeline {
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
.npt_ct_frm, .npt_tg_frm, .npt_prps_frm{
  display: inline-block;
  width: 70%;
  margin-left:2em;
}
.npt_cd_frm {
  display: inline-block;
  background-color: midnightblue;
  font-family: 'Courier New', Courier, monospace;
  color: white;
}
.npt_ct, .npt_tg, .npt_prps, .npt_cd, .sbmt_rst {
  margin-bottom: 1.2em;
}
.sbmt_btn, .rst_btn {
  margin-right: 1em;
}
</style>
