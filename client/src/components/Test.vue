<template>
  <v-app>
    <v-toolbar color="blue darken-1" dark  app>
        <v-toolbar-title>Testing</v-toolbar-title>
    </v-toolbar>
    <v-spacer></v-spacer>

    <v-content>
        <v-container class="my-5">

<v-card v-for="project in projects.data.allEmployees.edges" :key="project.name">
                <v-layout row wrap>
                    <v-flex xs12 md6>
                        <div class="caption grey--text">Employee</div>
                        <div>{{ project.name }}</div>
                    </v-flex>
                    <v-flex xs6 sm4 md2>
                        <div class="caption grey-text">Department</div>
                        <div>{{ project.department.name }}</div>
                    </v-flex>
                    <!-- <v-flex xs6 sm4 md2>
                        <div class="caption grey--text">Due by</div>
                        <div>1st Jan</div>
                    </v-flex>
                    <v-flex xs2 sm4 md2>
                        <div class="caption grey-text">Status</div>
                        <div>{{ project.status.new_field }}</div>
                    </v-flex> -->
                </v-layout>
            </v-card>

        </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      projects: {
        data: [
          {
            title: 'design new web',
            person: 'me',
            due: 'Jan',
            status: {
              new_field: 'done',
            },
          },
          {
            title: 'design new web',
            person: 'me',
            due: 'Jan',
            status: {
              new_field: 'done',
            },
          },
          {
            title: 'design new web',
            person: 'me',
            due: 'Jan',
            status: {
              new_field: 'done',
            },
          },
        ],
      },
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:5000/';
      axios.get(path, {
        params: {
          query: `{
                    allEmployees {
                        edges {
                            node {
                                name
                                department {
                                    name
                                }
                            }
                        }
                    }
                }`,
        },
      })
        .then((res) => {
          this.projects = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getData();
  },
};
</script>
