// Get the button and the app element from the HTML
const btnEl = document.getElementById('btn');
const appEl = document.getElementById('app');

// Add each saved note to the app
getNotes().forEach((note) => {
  // Create a textarea element for each note
  const noteEl = createNoteEl(note.id, note.content);
  // Insert the note element before the button
  appEl.insertBefore(noteEl, btnEl);
});

// Create a textarea element for a note
function createNoteEl(id, content) {
  const element = document.createElement('textarea');
  // Add the "note" class to the element
  element.classList.add('note');
  // Set the placeholder and initial value for the element
  element.placeholder = 'Empty Note';
  element.value = content;

  // Add an event listener for double-clicking the element
  element.addEventListener('dblclick', () => {
    // Display a warning message and ask the user if they want to delete the note
    const warning = confirm('Do you want to delete this note?');
    // If the user confirms, delete the note
    if (warning) {
      deleteNote(id, element);
    }
  });

  // Add an event listener for any input to the element
  element.addEventListener('input', () => {
    // Update the note in localStorage with the new content
    updateNote(id, element.value);
  });

  // Return the element
  return element;
}

// Delete a note from the app and from localStorage
function deleteNote(id, element) {
  // Get all notes except the one to delete
  const notes = getNotes().filter((note) => note.id != id);
  // Save the updated notes to localStorage
  saveNote(notes);
  // Remove the note element from the app
  appEl.removeChild(element);
}

// Update a note in localStorage
function updateNote(id, content) {
  // Get all notes from localStorage
  const notes = getNotes();
  // Find the note to update
  const target = notes.filter((note) => note.id == id)[0];
  // Update the content of the note
  target.content = content;
  // Save the updated notes to localStorage
  saveNote(notes);
}

// Add a new note to the app and to localStorage
function addNote() {
  // Get all notes from localStorage
  const notes = getNotes();
  // Create a new note object with a unique ID and empty content
  const noteObj = {
    id: Math.floor(Math.random() * 100000),
    content: '',
  };
  // Create a new note element and insert it before the button
  const noteEl = createNoteEl(noteObj.id, noteObj.content);
  appEl.insertBefore(noteEl, btnEl);

  // Add the new note to the notes array and save it to localStorage
  notes.push(noteObj);
  saveNote(notes);
}

// Save the notes to localStorage
function saveNote(notes) {
  localStorage.setItem('note-app', JSON.stringify(notes));
}

// Get the notes from localStorage
function getNotes() {
  return JSON.parse(localStorage.getItem('note-app') || '[]');
}

// Add an event listener to the button to add a new note
btnEl.addEventListener('click', addNote);
