<template>
  <div>
      <StockList :stockList="stockList"/>
  </div>
</template>

<script>
import axios from "axios"
import StocksWidget from '@/components/StocksWidget.vue'
import StockList from '@/components/StockList.vue'
export default {
  components:{
    StocksWidget, StockList
  },
  data(){
    return{
      stockList: [],

      stockName: "",
      stockPrice: null,
      stockRate: null
    }
  },
  mounted(){
    //LiveBorsa
    axios.get("https://api.collectapi.com/economy/liveBorsa",{'headers':{
        'Authorization':'apikey 18E4jglC7L6Upc1zMqoniu:4n8zaE3WRox1NEQhSMRcQG',
        'Content-type':'application/json'
      }})
      .then(response=>{
        response.data.result.forEach((res, idx) => {
          this.stockList.push({
            stockName: res.name,
            stockPrice: res.price,
            stockRate: res.rate,
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
