<template>
  <div>
      <CurrencyList :currList="currList"/>
  </div>
</template>

<script>
import axios from "axios"
import CurrencyList from '@/components/CurrencyList.vue'
export default {
  components:{
    CurrencyList
  },
  data(){
    return{
      currList: [],

      currName: "",
      currBuying: null,
      currSelling: null,
      currRate: null
    }
  },
  mounted(){
    //LiveBorsa
    axios.get("https://api.collectapi.com/economy/parite",{'headers':{
        'Authorization':'apikey 18E4jglC7L6Upc1zMqoniu:4n8zaE3WRox1NEQhSMRcQG',
        'Content-type':'application/json'
      }})
      .then(response=>{
        response.data.result.forEach((res, idx) => {
          this.currList.push({
            currName: res.name,
            currBuying: res.buying,
            currSelling: res.selling,
            currRate: res.rate,
            id: idx,
          });
        });
      })
      .catch(e=>{
        console.log(e)
      })
    },
    methods: {
    },

  

}
</script>
