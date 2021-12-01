<template>

    <div class="col-md-8 font-oswald">
        <div class="py-20">
            <p class="font-bold w-1/4 text-center mx-auto">Apple Inc. (AAPL)</p>
            <p class="text-center text-sm">NasdaqGS - NasdaqGS Real Time Price. Currency in USD</p>
            <p class="text-center text-xxs">At close: 04:00PM EST</p>
            <div id="myDiv"></div>
        </div>     
    </div>
</template>

<script>
import Plotly from "plotly.js"
import axios from "axios"
    export default {  
        data(){
            return{
                temp:[],
                open:[],
                close:[],
                high:[],
                low:[],
                x:[],
                trace1: {},
                layout: {},
                data: [],
            }
        }, 
        mounted() {
            axios.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?timeseries=180&apikey=b6b90c304ec78fa2c95ce348d5d2447a")
                .then(res=>{
                    this.temp=res.data.historical
                    for(var item of this.temp){
                        this.open.push(item.open)
                        this.close.push(item.close)
                        this.high.push(item.high)
                        this.low.push(item.low)
                        this.x.push(item.date)
                    }

                    this.trace1 = {
                        x: this.x, 
                        close: this.close, 
                        decreasing: {line: {color: '#D0010A'}}, 
                        high: this.high, 
                        increasing: {line: {color: '#00D10F'}}, 
                        line: {color: 'rgba(31,119,180,1)'}, 
                        low: this.low, 
                        open: this.open, 
                        type: 'candlestick', 
                        xaxis: 'x', 
                        yaxis: 'y'
                    };
                    
                    this.data.push(this.trace1);

                    this.layout = {
                        dragmode: 'zoom', 
                        margin: {
                            r: 60, 
                            t: 10, 
                            b: 60, 
                            l: 60
                        }, 
                        showlegend: false, 
                        xaxis: {
                            autorange: true, 
                            title: 'Date', 
                            type: 'date'
                        }, 
                        yaxis: {
                            autorange: true, 
                            range: [50, 60], 
                            type: 'linear'
                        }
                    };

                    Plotly.newPlot('myDiv', this.data, this.layout);
                })
                .catch(err=>console.log(err))
        },
    }
</script>

<style scoped>

</style>