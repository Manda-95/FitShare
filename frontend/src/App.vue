<script setup>
import TrainingPlans from './components/TrainingPlans.vue';
</script>

<template>
  <div id="app">
    <header>
      <h1 class="title">Programme d'entraînement</h1>
    </header>
    <main>
      <TrainingPlans />
    </main>
  </div>
</template>

<style scoped>

html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background-color: #fff;
  color: #000; 
  font-family: Arial, sans-serif;
}


#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  text-align: center;
}


header {
  width: 100%;
  padding: 1rem 0;
  background-color: #fff; 
  color: #000; 
}


.title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 2rem;
  color: #000; 
}

main {
  flex: 1;
  width: 100%;
  max-width: 800px; 
  padding: 1rem;
  background-color: transparent; 
  border-radius: 0; 
  box-shadow: none; 
}
</style>