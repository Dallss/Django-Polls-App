<template>
  <div>
    <h1>All Questions</h1>
    <ul>
      <li v-for="poll in polls" :key="poll.id">
        <RouterLink :to="{ name: 'poll-detail', params: { id: poll.pk } }">
          {{ poll.question_text }}
        </RouterLink>
      </li>
    </ul>

    <router-link :to="{ name: 'add-new' }">Add New Question</router-link>
  </div>
</template>

<script>
import sileo from 'sileo'
const Question = new sileo.Model('polls', 'questions')

export default {
  data() {
    return {
      polls: []
    }
  },
  mounted() {
    this.fetchQuestions()
    console.log('IndexView component has been mounted.')
    console.log(this.polls)
  },
  methods: {
    async fetchQuestions() {
      try {
        const data = await Question.objects.filter()
        this.polls = data
        console.log('Finished fetchingg: ')
        console.log(this.polls)
      } catch (error) {
        console.error('Error in fetching Questions', error)
      }
    }
  }
}
</script>
