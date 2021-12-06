<template>
    <div class="flex flex-col mx-auto font-oswald relative text-darkblue">
        <h class="text-lg font-bold mx-auto mt-24">CHARTS</h>
        <br>
        <div class="h-full bg-white p-6 rounded shadow-md mx-auto">
            <p class="text-lg font-bold">Stocks - Most Actives</p>
            <ul class="font-semibold text-sm list-style-type list-disc">
                <li class="ml-5"><router-link to="/charts/aapl">Apple Inc. (AAPL)</router-link></li>
                <li class="ml-5"><router-link to="/charts/tsla">Tesla, Inc. (TSLA)</router-link></li>
                <li class="ml-5"><router-link to="/charts/nvda">Nvidia Corporation (NVDA)</router-link></li>
                <li class="ml-5"><router-link to="/charts/amd">Advanced Micro Devices, Inc. (AMD)</router-link></li>
                <li class="ml-5"><router-link to="/charts/fb">Meta Platforms, Inc. (FB)</router-link></li>
                <li class="ml-5"><router-link to="/charts/amzn">Amazon.com, Inc. (AMZN)</router-link></li>
            </ul>
            <br>
            <p class=" text-lg font-bold">Currencies - Most Actives</p>
            <ul class="font-semibold text-sm list-style-type list-disc">
                <li class="ml-5"><router-link to="/charts/usd">USD</router-link></li>
                <li class="ml-5"><router-link to="/charts/tsla">EUR</router-link></li>
                <li class="ml-5"><router-link to="/charts/nvda">JPY</router-link></li>
                <li class="ml-5"><router-link to="/charts/amd">GBP</router-link></li>
                <li class="ml-5"><router-link to="/charts/fb">RUB</router-link></li>
                <li class="ml-5"><router-link to="/charts/amzn">TRY</router-link></li>
            </ul>
        </div>
        
    </div>
</template>

<script>
export default {}

</script>

<style scoped>

</style>