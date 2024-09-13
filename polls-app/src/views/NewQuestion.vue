<template>
  <div>
    <h1>Add New Poll Question</h1>

    <form @submit.prevent="SubmitEvent()">
      <label for="question_text"> Question: </label>
      <input type="text" v-model="questionText" name="question_text" id="question_text" /> <br />

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import sileo from 'sileo'
const Questions = new sileo.Model('polls', 'questions')

export default {
  data() {
    return {
      questionText: null
    }
  },
  methods: {
    SubmitEvent() {
      if (this.questionText == null) {
        alert('Input something')
      } else {
        const data = { question_text: this.questionText, pub_date: this.getCurrentDate() }
        Questions.objects
          .create(data)
          .then(function (data) {
            console.log(data)
          })
          .catch(function (xhr) {
            console.log('Something went wrong!')
            console.log(xhr)
          })
        this.$router.push('/')
      }
    },
    getCurrentDate() {
      const today = new Date()
      const year = today.getFullYear()
      const month = (today.getMonth() + 1).toString().padStart(2, '0') // Months are zero-based
      const day = today.getDate().toString().padStart(2, '0')
      return `${year}-${month}-${day}` // Format as yyyy-mm-dd
    }
  }
}
</script>
