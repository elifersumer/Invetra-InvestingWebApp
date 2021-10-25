<template>
<div class="flex flex-row">
<div class="flex flex-col relative w-90 h-full mt-20 mr-auto ml-auto font-oswald font-bold bg-white p-10 rounded shadow-md text-darkblue">
        <div class="flex flex-row justify-between">
            <p class="text-lg mb-4 cursor-default">Stocks</p>
            <div class="flex flex-row">
                <input class="rounded-lg w-64 h-4 py-4 px-6 bg-lightblue text-gray-700 leading-tight mr-2 focus:outline-none 
                focus:ring focus:border-gray shadow" id="search" type="text" placeholder="Search">
                <img @click="search()" src="@/static/searchicon.png" class="w-8 h-8 rounded-md cursor-pointer">
            </div>
        </div>
        <div class="flex flex-row place-content-between place-items-center text-xs text-gray-400">
            <p class="mt-2 text-center">Name</p>
            <p class="mt-2 text-center">Price</p>
            <p class="mt-2 mr-6 text-center">Rate</p>
        </div>
        <div class="h-96 overflow-auto w-full">
            <div id="cripto" v-for="(stock, idx) in stockList" :key="idx">
                <div class="flex flex-row justify-between text-sm">
                    <p class="mt-2 w-10 cursor-pointer" id="row">{{stock.stockName}}</p>
                    <p class="grid mt-2">{{stock.stockPrice}}</p>
                    <p class="mt-2 mr-2" :style="stock.stockRate>0 ? 'color: #059669 ' : 'color: #DC2626'">{{stock.stockRate}}</p>
                </div>
            </div>
        </div>
        <Footer/>
        
    </div>
</div>
    

    
</template>

<script>
import Footer from '@/components/Footer.vue'
    export default {
        props:["stockList"],
        methods: {
            
        },
        components:{
            Footer
        }
    }
</script>

<style scoped>

</style>