<template>
    <main>
        <AppHeader />
        <Nuxt />
    </main>
</template>

<style>
html,body{
    overflow: hidden;
}

main {
    display: flex;
    flex-direction: column;

    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
}

section.page {
    flex: 1;
    overflow-y: scroll !important;
}
</style>