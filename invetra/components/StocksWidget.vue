<template>
    <div class="grid grid-cols-1 relative w-2/3 h-full mt-2 ml-10 mb-4 font-oswald font-bold bg-white p-9 rounded shadow-md text-darkblue">
        <a href=# class="text-lg mb-4">Stocks</a>
            <div class="flex flex-row place-content-between place-items-center text-xxs text-gray-400">
                <p class="mt-2 text-center">Name</p>
                <p class="mt-2 text-center">Price</p>
                <p class="mt-2 text-center">Rate</p>
            </div>
        <div id="cripto" v-for="(stock, idx) in stockList" :key="idx">
            <div class="flex place-content-between flex-row text-sm">
                <p class="mt-2 text-center">{{stock.stockName}}</p>
                <p class="mt-2 text-center">{{stock.stockPrice}}</p>
                <p class="mt-2 text-center" :style="stock.stockRate>0 ? 'color: #059669 ' : 'color: #DC2626'">{{stock.stockRate}}</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props:["stockList"],
        data:{
        },
        methods: {
            
        },
        computed:{
            
        }
    }
</script>

<style scoped>

</style>