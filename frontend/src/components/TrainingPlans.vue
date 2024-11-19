<template>
  <div>
    <h1>Programme d'entraînement</h1>

    <!-- Filtres -->
    <div>
      <label>Niveau:</label>
      <select v-model="filters.level" @change="fetchPlans">
        <option value="">tous</option>
        <option value="Débutant">Débutant</option>
        <option value="Intermédiaire">Intermédiaire</option>
        <option value="Avancé">Avancé</option>
      </select>

      <label>Objectif:</label>
      <select v-model="filters.goal" @change="fetchPlans">
        <option value="">tous</option>
        <option value="Perte de poids">Perte de poids</option>
        <option value="Renforcement musculaire">Renforcement musculaire</option>
      </select>

      <label>Sport:</label>
      <select v-model="filters.sport" @change="fetchPlans">
        <option value="">tous</option>
        <option value="Musculation">Musculation</option>
        <option value="Running">Running</option>
      </select>
    </div>

    <!-- Liste des programmes -->
    <div v-if="loading">Loading...</div>
    <ul v-else>
      <li v-for="plan in plans" :key="plan.id">
        {{ plan.title }} - {{ plan.level }} - {{ plan.goal }} - {{ plan.sport }}
        <button @click="addToPlanning(plan)">Ajouter au planning</button>
      </li>
    </ul>

    <!-- Bouton pour ajouter un nouveau programme -->
    <button @click="toggleForm" class="add-program-btn">
      Ajouter un programme
    </button>

    <!-- Formulaire pour ajouter un programme -->
    <div v-if="showForm" class="form-container">
      <h2>Ajouter un nouveau programme</h2>
      <form @submit.prevent="submitProgram">
        <div>
          <label>Niveau:</label>
          <select v-model="newProgram.level" required>
            <option value="Débutant">Débutant</option>
            <option value="Intermédiaire">Intermédiaire</option>
            <option value="Avancé">Avancé</option>
          </select>
        </div>
        <div>
          <label>Objectif:</label>
          <select v-model="newProgram.goal" required>
            <option value="Perte de poids">Perte de poids</option>
            <option value="Renforcement musculaire">Renforcement musculaire</option>
          </select>
        </div>
        <div>
          <label>Sport:</label>
          <select v-model="newProgram.sport" required>
            <option value="Musculation">Musculation</option>
            <option value="Running">Running</option>
          </select>
        </div>
        <div>
          <label>Programme:</label>
          <input v-model="newProgram.title" type="text" placeholder="Nom du programme" required />
        </div>
        <button type="submit">Ajouter au planning</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      showForm: false, // Afficher ou masquer le formulaire
      newProgram: {
        level: "",
        goal: "",
        sport: "",
        title: "",
      },
      plans: [], // Liste des programmes
      filters: {
        level: "",
        goal: "",
        sport: "",
      },
      loading: false,
    };
  },
  methods: {
    async fetchPlans() {
      this.loading = true;
      try {
        const response = await axios.get("http://127.0.0.1:8000/plans", {
          params: this.filters,
        });
        this.plans = response.data;
      } catch (error) {
        console.error("Error fetching plans:", error);
      } finally {
        this.loading = false;
      }
    },
    toggleForm() {
      this.showForm = !this.showForm; // Alterner entre affichage et masquage du formulaire
    },
    submitProgram() {
      // Ajouter le nouveau programme à la liste
      const newPlan = { ...this.newProgram, id: Date.now() }; // Ajoute un ID unique
      this.plans.push(newPlan);

      // Réinitialiser le formulaire
      this.newProgram = {
        level: "",
        goal: "",
        sport: "",
        title: "",
      };

      // Masquer le formulaire
      this.showForm = false;

      alert("Programme ajouté avec succès !");
    },
    addToPlanning(plan) {
      alert(`Programme "${plan.title}" ajouté au planning.`);
    },
  },
  mounted() {
    this.fetchPlans();
  },
};
</script>

<style scoped>
/* Bouton principal */

.add-program-btn {
  margin-top: 2rem;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.add-program-btn:hover {
  background-color: #0056b3;
}

/* Formulaire */
.form-container {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 5px;
}

form div {
  margin-bottom: 1rem;
}

form label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

form select,
form input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  padding: 0.5rem 1rem;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

form button:hover {
  background-color: #218838;
}
</style>
