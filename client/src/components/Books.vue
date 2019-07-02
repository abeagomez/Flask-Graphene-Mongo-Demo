<template>
    <div>
        <!-- <div class="upper bar">
            <v-toolbar color="blue darken-1" dark fixed app>
                <v-toolbar-title>Books</v-toolbar-title>
            </v-toolbar>
        </div> -->
        <div>
            <v-data-table
                :headers="headers"
                :items="books"
                class="elevation-1"
            >
            <template v-slot:items="props">
                <td>{{ props.item.name }}</td>
                <td class="text-xs-right">{{ props.item.author }}</td>
                <td class="text-xs-right">{{ props.item.read }}</td>
            </template>
            </v-data-table>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      headers: [
        {
          text: 'BOOKS',
          align: 'left',
          sortable: false,
          value: 'name',
        },
        { text: 'Author', value: 'author' },
        { text: 'Read?', value: 'read' },
      ],
      books: [
        {
          name: 'Los miserables',
          author: 'Victor Hugo',
          read: 'Yes',
        },
        {
          name: 'Nuestra Señora de París',
          author: 'Victor Hugo',
          read: 'No',
        },
      ],
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
