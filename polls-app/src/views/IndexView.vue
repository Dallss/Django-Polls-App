<template>
  <div>
    <h1>Polls</h1>
    <ul>
      <li v-for="poll in polls" :key="poll.id">
        <RouterLink :to="{ name: 'poll-detail', params: { id: poll.id } }">
          {{ poll.question_text }}
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios'


export default {
  data() {
    return {
      polls: []
    };
  },
  mounted() {
    console.log('IndexView component has been mounted.');
  },
  created() {
    this.fetchQuestions();
  },
  methods: {
    async fetchQuestions(){
      try{
        const response = await axios.get('http://127.0.0.1:8000/polls/question/');
        this.polls = response.data;
      }catch (error){
        console.error('Error in fetching Questions', error);
      }
    }
  }
}
</script>

