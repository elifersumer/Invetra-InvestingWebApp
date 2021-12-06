<template>
  <div>
      <CriptoList :criptoList="criptoList"/>
  </div>
</template>

<script>
import axios from "axios"
import CriptoList from '@/components/CriptoList.vue'
export default {
  components:{
    CriptoList
  },
  data(){
    return{
      criptoList: [],

      criptoCode: "",
      criptoPrice: null,
      criptoChangeDay: null,
      criptoChangeHour: null
    }
  },
  mounted(){
    //LiveBorsa
    axios.get("https://api.collectapi.com/economy/cripto",{'headers':{
        'Authorization':'apikey 4YUSnM4i0gYB19AlZGPtsB:0hc4tJLIVpkOVd6ZiwfiQF',
        'Content-type':'application/json'
      }})
      .then(response=>{
        response.data.result.forEach((res, idx) => {
          this.criptoList.push({
            criptoCode: res.code,
            criptoPrice: res.price,
            criptoChangeDay: res.changeDay,
            criptoChangeHour: res.changeHour,
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
