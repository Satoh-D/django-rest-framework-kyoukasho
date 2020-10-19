<template>
  <div id="app">
    <!-- Vue Routerに関連するディレクティブ -->
    <!-- URLにマッチングしたコンポーネントが描画される -->
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
main.container {
  border: 1px solid #ccc;
  margin-top: 4em;
  padding: 2em;
  width: 600px;
}
</style>
