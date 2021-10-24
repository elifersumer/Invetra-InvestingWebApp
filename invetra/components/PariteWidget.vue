<template>
    <div class="grid grid-cols-1 relative w-1/5 ml-10 mt-20 mb-4 font-oswald font-bold bg-white px-6 pt-4 pb-6 rounded shadow-md text-darkblue">
        <a href=# class="text-lg">Currency</a>
            <div class="flex flex-row place-content-between place-items-center text-xxs text-gray-400 text-align-center">
                <p class="mt-2 text-center">Name</p>
                <p class="mt-2 text-center">Buying</p>
                <p class="mt-2 text-center">Selling</p>
                <p class="mt-2 text-center">Rate</p>
            </div>
        <div id="cripto" v-for="(parite, idx) in pariteList" :key="idx">
            <div class="flex place-content-between flex-row text-sm">
                <p class="mt-2 text-center">{{parite.pariteName}}</p>
                <p class="mt-2 text-center">{{parite.buyingstr}}</p>
                <p class="mt-2 text-center">{{parite.sellingstr}}</p>
                <p class="mt-2 text-center" :style="parite.rate>0 ? 'color: #059669 ' : 'color: #DC2626'">{{parite.rate}}</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props:["pariteList"],
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