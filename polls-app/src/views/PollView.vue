<template>
    <div>
      <h1>{{ question }}</h1>
      <ul>
        <li v-for="choice in choices" :key="choice.id">
            {{ choice.choice }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  
  
  export default {
    data() {
      return {
        question: 'Bini bias?',
        choices: [
            { id: 1, choice: 'Aiah', votes: 9999 },
            { id: 2, choice: 'Colet', votes: 99999},
            { id: 3, choice: 'mikha', votes: 9999 }
        ],
      };
    },
    mounted() {
      console.log('QuestionView component has been mounted.');
    }
  }
  </script>
  
  