#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as  list in the /films/ endpoint
 */

const util = require('util');
const request = util.promisify(require('request'));
const filmId = process.argv[2];

async function starwarsCharacters(filmId) {
  const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  try {
    const response = await request(endpoint);
    const filmData = JSON.parse(response.body);
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      try {
        const characterResponse = await request(characterUrl);
        const characterData = JSON.parse(characterResponse.body);
        console.log(characterData.name);
      } catch (error) {
        console.error('Error fetching character data:', error);
      }
    }
  } catch (error) {
    console.error('Error fetching film data:', error);
  }
}

starwarsCharacters(filmId);
