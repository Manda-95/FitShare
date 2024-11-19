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
/* Global styles */
#app {
  font-family: Arial, sans-serif;
  margin: 0 auto;
  text-align: center; /* Centrer le texte */
  background-color: #f5f5f5; /* Fond clair */
  min-height: 100vh; /* Assurer une hauteur minimale de la page */
  display: flex;
  flex-direction: column; /* Disposition en colonne */
  align-items: center; /* Centre horizontalement */
  justify-content: flex-start; /* Met le contenu en haut */
  padding: 1rem;
}

/* Titre principal */
.title {
  font-size: 2.5rem; /* Taille du texte plus grande */
  font-weight: bold; /* Texte en gras */
  margin-bottom: 2rem; /* Espacement en dessous */
  color: #333; /* Couleur sombre pour le titre */
}

/* Main content styling */
main {
  width: 100%;
  max-width: 600px; /* Limiter la largeur maximale */
  padding: 1rem;
  background: white; /* Fond blanc pour contraster */
  border-radius: 10px; /* Arrondir les bords */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Ajouter une ombre subtile */
}

label {
  display: block; /* Chaque label sur une nouvelle ligne */
  margin-bottom: 0.5rem; /* Espacement sous le label */
  font-weight: bold; /* Texte des labels en gras */
  color: #555; /* Couleur des labels */
}

select {
  width: 100%; /* Sélecteurs prennent toute la largeur */
  padding: 0.5rem;
  margin-bottom: 1rem; /* Espacement entre chaque champ */
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
}
</style>
