<template>
  <div class="page-container">
    <h1>Programme d'entraînement</h1>

    <div class="filters">
      <label>Niveau:</label>
      <select v-model="filters.level">
        <option value="">Tous</option>
        <option value="Débutant">Débutant</option>
        <option value="Intermédiaire">Intermédiaire</option>
        <option value="Avancé">Avancé</option>
      </select>

      <label>Objectif:</label>
      <select v-model="filters.goal">
        <option value="">Tous</option>
        <option value="Perte de poids">Perte de poids</option>
        <option value="Renforcement musculaire">Renforcement musculaire</option>
      </select>

      <label>Sport:</label>
      <select v-model="filters.sport">
        <option value="">Tous</option>
        <option value="Musculation">Musculation</option>
        <option value="Running">Running</option>
      </select>
    </div>

    <div class="buttons-container">
      <button @click="fetchProgramExercises" class="fetch-program-btn">
        Obtenir exercices du programme
      </button>
      <button @click="toggleForm" class="add-program-btn">
        Ajouter un programme
      </button>
    </div>

    <div v-if="exercises.length" class="exercises-list">
      <h2>Exercices du programme</h2>
      <ul>
        <li v-for="exercise in exercises" :key="exercise.id">
          {{ exercise.name }}
        </li>
      </ul>
    </div>

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
        <div>
          <label>Exercices du programme :</label>
          <div v-if="loadingFormExercises">Chargement des exercices...</div>
          <div v-else class="exercise-list">
            <div v-for="exercise in formExercises" :key="exercise.id" class="exercise-item">
              <input
                type="checkbox"
                :value="exercise.id"
                v-model="newProgram.exercises"
              />
              <span>{{ exercise.name }}</span>
            </div>
          </div>
        </div>
        <button type="submit">Ajouter au planning</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showForm: false,
      newProgram: {
        level: "",
        goal: "",
        sport: "",
        title: "",
        exercises: [],
      },
      filters: {
        level: "",
        goal: "",
        sport: "",
      },
      exercises: [],
      formExercises: [],
      plans: [],
      loadingExercises: false,
      loadingFormExercises: false,
    };
  },
  methods: {
    toggleForm() {
      this.showForm = !this.showForm;
      if (this.showForm) {
        this.fetchFormExercises();
      }
    },
    fetchProgramExercises() {
      if (!this.filters.level && !this.filters.goal && !this.filters.sport) {
        alert("Veuillez sélectionner un niveau, un objectif et un sport pour chercher un programme.");
        this.exercises = [];
        return;
      }
      this.exercises = [
        { id: 1, name: "Squat" },
        { id: 2, name: "Push-up" },
        { id: 3, name: "Pull-up" },
      ];
      alert("Exercices récupérés avec succès !");
    },
    fetchFormExercises() {
      this.loadingFormExercises = true;
      setTimeout(() => {
        this.formExercises = [
          { id: 1, name: "Squat" },
          { id: 2, name: "Deadlift" },
          { id: 3, name: "Bench Press" },
          { id: 4, name: "Pull-up" },
          { id: 5, name: "Plank" },
        ];
        this.loadingFormExercises = false;
      }, 1000);
    },
    submitProgram() {
      const newPlan = { ...this.newProgram, id: Date.now() };
      this.plans.push(newPlan);
      this.newProgram = {
        level: "",
        goal: "",
        sport: "",
        title: "",
        exercises: [],
      };
      this.showForm = false;
      alert("Programme ajouté avec succès !");
    },
  },
};
</script>

<style scoped>
.page-container {
  background-color: #fff;
  color: #000;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  box-sizing: border-box;
  width: 100%;
}

.filters {
  width: 100%;
  max-width: 800px;
  margin-bottom: 2rem;
}

label {
  color: #000;
  margin-bottom: 0.5rem;
  display: block;
}

select {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  background-color: #f5f5f5;
  color: #000;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.buttons-container {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  width: 100%;
}

button {
  padding: 0.5rem 1rem;
  background-color: #87ceeb;
  color: #fff;
  font-weight: bold;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #00bfff;
}

.exercises-list {
  margin-top: 2rem;
  width: 100%;
  max-width: 800px;
}

.exercises-list h2 {
  color: #000;
  margin-bottom: 1rem;
}

.exercises-list ul {
  list-style: none;
  padding: 0;
}

.exercises-list li {
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  background-color: #f5f5f5;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
