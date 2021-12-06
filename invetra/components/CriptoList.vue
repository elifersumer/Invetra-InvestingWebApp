<template>
<div class="flex flex-row">
<div class="flex flex-col relative w-90 h-full mt-20 mr-auto ml-auto font-oswald font-bold bg-white p-10 rounded shadow-md text-darkblue">
        <div class="flex flex-row justify-between">
            <p class="text-lg mb-4 cursor-default">Cripto Coins</p>
            <div class="flex flex-row text-xs">
                <input class="rounded-lg w-48 h-4 p-3 bg-lightblue text-gray-700 leading-tight mr-2 focus:outline-none" 
                id="search" type="text" placeholder="Search" >
                <img src="@/static/searchicon.png" class="w-6 h-6 rounded-md cursor-pointer">
            </div>
        </div>
        <div class="flex flex-row place-content-between place-items-center text-xs text-gray-400">
            <p class="mt-2 text-center">Code</p>
            <p class="mt-2 text-center">Price</p>
            <p class="mt-2 text-center">Change Rate(d)</p>
            <p class="mt-2 mr-3 text-center">Change Rate(h)</p>
            <p class="mt-2 mr-6 text-center">Al/Sat</p>
        </div>
        <div class="h-96 overflow-auto w-full">
            <div id="cripto" v-for="(cripto, idx) in criptoList" :key="idx">
                <div class="flex flex-row justify-between text-sm">
                    <p class="mt-2 w-10 cursor-pointer" id="row">{{cripto.criptoCode}}</p>
                    <p class="grid mt-2">{{cripto.criptoPrice}}</p>
                    <p class="mt-2 mr-2" :style="cripto.criptoChangeDay>0 ? 'color: #059669 ' : 'color: #DC2626'">{{cripto.criptoChangeDay}}</p>
                    <p class="mt-2 mr-2" :style="cripto.criptoChangeHour>0 ? 'color: #059669 ' : 'color: #DC2626'">{{cripto.criptoChangeHour}}</p>
                    <div class="flex flex-row">
                        <a href="/"><img src="@/static/greenarrow.png" class="w-3 h-4 mr-3"></a>
                        <a href="/"><img src="@/static/redarrow.png" class="w-3 h-4 mr-2"></a>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</div>
    

    
</template>

<script>
import Footer from '@/components/Footer.vue'
    export default {
        props:["criptoList"],
        methods: {
            
        },
        components:{
            Footer
        }
    }
</script>

<style scoped>

</style>