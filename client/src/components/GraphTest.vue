// GraphQLTest.vue
<template>
    <div class="graphql-test">
        <h3 v-if="loading">Loading...</h3>
        <div v-else>
            <h4 v-for="user in users.data.allPeople.edges" :key="user.node.id">
                {{ user.node.firstName }} {{ user.node.lastName }}
            </h4>
        </div>
    </div>
</template>

<script>
import gql from 'graphql-tag';

export default {
  name: 'GraphQLTest',
  data() {
    return {
      loading: true,
      users: [],
    };
  },
  async mounted() {
    this.loading = true;
    this.users = await this.$apollo.query({ query: gql`query allPeople { allPeople{edges{node{id firstName lastName role{name } } } } }` });
    this.loading = false;
  },
};
</script>
