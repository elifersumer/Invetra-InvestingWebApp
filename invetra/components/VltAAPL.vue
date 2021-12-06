<template>
    <div class="flex flex-col font-oswald h-full mx-auto relative">
        <div v-for="(item, idx) in aaplList" :key="idx" class="mt-20 text-center">
            <p class="font-semibold"><b>Volatility:</b> {{item.volatility}}</p>
            <img class="w-1/2 mx-auto" src="@/assets/aapl_vol.png"/>
        </div>
    </div>
</template>

<script>
export default {
    props:['aaplList']
}
</script>

<style>

</style>