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
              class="npt_cd_frm" rows="12"
              placeholder="Place code here..."
              v-model="form.code">
            </b-form-textarea>
          </div>
          <div class="sbmt_rst">
            <b-button
              class="sbmt_btn" type="submit"
              variant="info"> Submit </b-button>
            <b-button
              class="rst_btn" type="reset"
              variant="info"> Reset </b-button>
            <b-button class="tmln_btn"
              variant="info"
              href="#/"> Back to Timeline </b-button>
          </div>
        </b-form>
        <!--
        <k-progress
          active
          status="error"
          type="lump"
          :cut-width="4"
          :percent="50" >
        </k-progress>
        -->
      </div>

    </div>
  </div>
</template>

<script>
/* eslint-disable */
import Pageheader from './Pageheader'
import axios from 'axios'

//var host = 'https://casacoding-back-dot-casacoding.nw.r.appspot.com'
// const host = 'http://127.0.0.1:8080'
const insert_api = 'http://127.0.0.1:8080/api/codeHelper'

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
        this.$router.push('/');
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
  width: 50%;
  margin: auto;
  margin-top: 4em;
}
.insertpanel {
  background-color:cornsilk;
  padding: 1em;
  border-radius: 0.6em;
  box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  width: 90%;
}
.lbl, .ltg, .lpr, .lcd{
  display: inline-block;
  width: 20%;
  font-weight: bold;
  text-align: left;
  font-size: 1.2em;
}
.npt_ct_frm, .npt_tg_frm, .npt_prps_frm{
  display: inline-block;
  width: 70%;
  margin-left:2em;
  font-size: 1.2em;
}
.npt_cd_frm {
  padding: 1em;
  border-radius: 0.6em;
}
.npt_cd_frm {
  display: inline-block;
  background-color: midnightblue;
  font-family: 'Courier New', Courier, monospace;
  color: white;
  font-size: 1.2em;
}
.npt_ct, .npt_tg, .npt_prps, .npt_cd, .sbmt_rst {
  margin-bottom: 1.2em;
}
.sbmt_rst {
   display: flex;
 }
.sbmt_btn, .rst_btn, .tmln_btn {
  margin-right: 1em;
  font-size: 1.1em;
  border-radius: 0.6em;
}
.tmln_btn{
  margin-left: auto;
}
</style>
