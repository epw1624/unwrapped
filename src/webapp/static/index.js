// document.addEventListener('DOMContentLoaded', () => {
//     const form = document.getElementById('form');
//     const continue_button = document.getElementById('continue-button');
//     const song_option = document.getElementById('song-selection').value;

//     continue_button.addEventListener("click", getOptions(song_option)); 
// });

function show_selected_div() {
    let dropdown = document.getElementById("song-selection");

    // hide divs for all options
    for (i = 0; i < dropdown.options.length; i++) {
        let cur_option = dropdown.options[i];
        if (cur_option.value == "none") {
            continue;
        }
        let div = document.getElementById(cur_option.value);
        div.style.display = 'none';
    }

    // show the div for the selected option
    console.log(dropdown.value);
    if (dropdown.value.value != "none") {
        let cur_div = document.getElementById(dropdown.value);
        cur_div.style.display = 'block';
    }
}

// function getOptions(song_option) {
//     console.log(song_option)
//     const form = document.getElementById('form');

//     if (song_option === 'top-tracks') {
//         console.log("function got called");
        
//         //timeframe field
//         const timeframe_options = [
//             {value: 'short-term', text: 'Short term'},
//             {value: 'medium-term', text: 'Medium term'},
//             {value: 'long-term', text: 'Long term'},  
//         ];

//         const timeframe_field = document.createElement('select');
        
//         timeframe_options.forEach(option => {
//             const new_option = document.createElement('option');
//             new_option.value = option.value;
//             new_option.textContent = option.text;
//             timeframe_field.appendChild(new_option);
//         });

//         form.appendChild(timeframe_field);

//         //num_songs field
//         const num_songs_field = document.createElement('number');
//         num_songs_field.min = 1;
//         num_songs_field.max = 50;

//         form.appendChild(num_songs_field);
//     }
//     else if (song_option === 'playlists') {
//         const playlists = ["placeholder", "for", "api", "result"];

//         const playlist_field = document.createElement('select');
//         playlists.forEach(option => {
//             const new_option = document.createElement('option');
//             new_option.value = option;
//             new_option.textContent = option; // text and value will be the same for now for testing
//             playlist_field.appendChild(new_option);
//         });

//         form.appendChild(playlist_field);
//     }
//     else if (song_option === 'artist-top-tracks') {
//         const artist_field = document.createElement('input');

//         form.appendChild(artist_field);
//     }

//     const submit_button = document.createElement('button');
//     form.appendChild(submit_button);
// }