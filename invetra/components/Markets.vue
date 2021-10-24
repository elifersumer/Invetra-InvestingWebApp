<template>
  <div>
    <Navbar/>
    <StocksWidget :stockList="stockListTopGainers"/>
    
  </div>
</template>

<script>
import axios from "axios"
import Navbar from '@/components/Navbar.vue'
import StocksWidget from '@/components/StocksWidget.vue'
export default {
  components:{
    Navbar,
    StocksWidget
  },
  data(){
    return{
      stockList: [],
      stockListTopGainers: [],

      stockName: "",
      stockPrice: null,
      stockRate: null
    }
  },
  mounted(){
    //LiveBorsa
    axios.get("https://api.collectapi.com/economy/liveBorsa",{'headers':{
        'Authorization':'apikey 46dtTLfQwLSIArdVV2JER4:1Ic99sgbbftK8I4ZRWNLf3',
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
        this.stockListTopGainers = this.stockList.slice(0, 10)
      })
      .catch(e=>{
        console.log(e)
      })
    }

  

}
</script>
