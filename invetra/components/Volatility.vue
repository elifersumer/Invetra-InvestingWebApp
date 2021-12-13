<template>
    <div class="flex flex-col mx-auto font-oswald relative text-darkblue">
        <h class="text-lg font-bold mx-auto mt-24">VOLATILITY TOOL</h>
        <br>
        <div class="h-full bg-white p-6 rounded shadow-md mx-auto">
            <p class="text-lg font-bold">Stocks - Most Actives</p>
            <ul class="font-semibold text-sm list-style-type list-disc">
                <li class="ml-5"><router-link to="/analysis/volatility/aapl">Apple Inc. (AAPL)</router-link></li>
                <li class="ml-5"><router-link to="/analysis/volatility/tsla">Tesla, Inc. (TSLA)</router-link></li>
                <li class="ml-5"><a>Nvidia Corporation (NVDA)</a></li>
                <li class="ml-5"><a>Advanced Micro Devices, Inc. (AMD)</a></li>
                <li class="ml-5"><a>Meta Platforms, Inc. (FB)</a></li>
                <li class="ml-5"><a>Amazon.com, Inc. (AMZN)</a></li>
            </ul>
        </div>
        
    </div>
        
        
</template>

<script>
export default {
    
}
</script>

<style>

</style>