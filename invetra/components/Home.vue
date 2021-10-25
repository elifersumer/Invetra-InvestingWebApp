<template>
  <div>
    <div class="flex flex-row">
      <Hero/>
      <PariteWidget :pariteList="pariteListFirst5"/>
      <CriptoWidget :criptoList="criptoListFirst5" />
    </div>
    <div class="flex flex-row">
      <Video/>
      <StocksWidget :stockList="stockListTopGainers"/>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import Navbar from "@/components/Navbar.vue"
import Hero from "@/components/Hero.vue"
import Video from "@/components/Video.vue"
import CriptoWidget from '@/components/CriptoWidget.vue'
import PariteWidget from '@/components/PariteWidget.vue'
import StocksWidget from '@/components/StocksWidget.vue'
export default {
  components:{
    Hero,
    Video,
    CriptoWidget,
    PariteWidget,
    StocksWidget
  },
  data(){
    return{
      criptoList:[],
      criptoListFirst5:[],
      pariteList:[],
      pariteListFirst5:[],
      stockList: [],
      stockListTopGainers: [],

      code: "",
      criptoPricestr: "",
      changeDay: null,
      changeDaystr:"",
      
      pariteName: "",
      buying: null,
      buyingstr: "",
      selling: null,
      sellingstr: "",
      rate: null,

      stockName: "",
      stockPrice: null,
      stockRate: null
    }
  },
  mounted(){
    //Cripto
      axios.get("https://api.collectapi.com/economy/cripto",{'headers':{
        'Authorization':'apikey 46dtTLfQwLSIArdVV2JER4:1Ic99sgbbftK8I4ZRWNLf3',
        'Content-type':'application/json'
      }})
      .then(response=>{
        response.data.result.forEach((res, idx) => {
          this.criptoList.push({
            code: res.code,
            criptoPricestr: res.pricestr,
            changeDaystr: res.changeDaystr,
            changeDay: res.changeDay,
            id: idx,
          });
        });
        this.criptoListFirst5 = this.criptoList.slice(0, 5)
      })
      .catch(e=>{
        console.log(e)
      })
    //Parite
      axios.get("https://api.collectapi.com/economy/parite",{'headers':{
        'Authorization':'apikey 46dtTLfQwLSIArdVV2JER4:1Ic99sgbbftK8I4ZRWNLf3',
        'Content-type':'application/json'
      }})
      .then(response=>{
        response.data.result.forEach((res, idx) => {
          this.pariteList.push({
            name: res.name,
            buyingstr: res.buyingstr,
            sellingstr: res.sellingstr,
            buying: res.buying,
            selling: res.selling,
            rate: res.rate,
            id: idx,
          });
        });
        this.pariteListFirst5 = this.pariteList.slice(0, 5)
      })
      .catch(e=>{
        console.log(e)
      })
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
