<template>
    <div class="grid grid-cols-1 relative w-1/5 ml-10 mt-20 mb-4 font-oswald font-bold bg-white px-6 pt-4 pb-6 rounded shadow-md text-darkblue">
        <a href=# class="text-lg">Cripto</a>
            <div class="flex flex-row place-content-between place-items-center text-xxs text-gray-400 text-align-center">
                <p class="mt-2 text-center">Name</p>
                <p class="mt-2 text-center">Price</p>
                <p class="mt-2 text-center">Change(24h)</p>
            </div>
        <div id="cripto" v-for="(cripto, idx) in criptoList" :key="idx">
            <div class="flex place-content-between flex-row text-sm">
                <p class="mt-2 text-center">{{cripto.code}}</p>
                <p class="mt-2 text-center">{{cripto.criptoPricestr}}</p>
                <p class="mt-2 text-center" :style="cripto.changeDay>0 ? 'color: #059669 ' : 'color: #DC2626'">{{cripto.changeDaystr}}</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        el: "#cripto",
        props:["criptoList"],
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