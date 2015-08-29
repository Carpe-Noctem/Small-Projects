console.log("Welcome to my block-letter program!");
console.log("\nYou are given twenty block with two letters on each block (one" +
" on a side, the other on another): \n(B O), (X K), (D Q), (C P), (N A), (G T" +
"), (R E), (T G), (Q D), (F S), (J W), (H U), (V I), (A N), (O B), (E R), (F " +
"S), (L Y), (P C), (Z M). \nThe rules are simple: \n\t1. Once a letter on a b" +
"lock is used, that block may not be used again.");

var b = ['B', 'O', 'X', 'K', 'D', 'Q', 'C', 'P', 'N', 'A', 'G', 'T', 'R', 'E',
'T', 'G','Q', 'D','F', 'S', 'J', 'W', 'H', 'U', 'V', 'I', 'A', 'N', 'O', 'B',
'E', 'R', 'F', 'S', 'L', 'Y', 'P', 'C', 'Z', 'M'];
// The .length of b === 40;

//Max amount of times a letter appears in b is 2. if (count >= 3)?
var p = 0;

function can_make_word(i, li) {
    var p = prompt("Input a word to determine whether or not in can be made: ");
    i = p.toUpperCase();
    if (!isNaN(i)) { // Rejects i if not an alpha string
        alert("Invalid input. Please enter only alphabetical characters.");
        return can_make_word(i, li);
    }
    var t_f = 0; // True or fFlse
    var s_c = 0; // Special count
    var chosen_w = "\nYour chosen word was as follows: " + "\n\t" + i;
    for (var r = 0; r < li.length; r += 2) { // Searchs through every element in the li array
        var count = 0;
        /* The "Special Letters" (only appear once instead of twice on the
        blocks) Graveyard */
        var x_c = 0; var k_c = 0; var j_c = 0; var w_c = 0; var h_c = 0;
        var u_c = 0; var v_c = 0; var i_c = 0; var l_c = 0; var y_c = 0;
        var z_c = 0; var m_c = 0; // "Special letter" count
        for (var le in i) { // Compares each element in the li array with every letter in i
            switch (i[le]) { // Special letters
                case "X":
                    x_c += 1;
                    break;
                case "K":
                    k_c += 1;
                    break;
                case "J":
                    j_c += 1;
                    break;
                case "W":
                    w_c += 1;
                    break;
                case "H":
                    h_c += 1;
                    break;
                case "U":
                    u_c += 1;
                    break;
                case "V":
                    v_c += 1;
                    break;
                case "I":
                    i_c += 1;
                    break;
                case "L":
                    l_c += 1;
                    break;
                case "Y":
                    y_c += 1;
                    break;
                case "Z":
                    z_c += 1;
                    break;
                case "M":
                    m_c += 1;
                    break;
                
            }
                if (x_c >= 2 || k_c >= 2 || j_c >= 2 || w_c >= 2 || h_c >= 2 ||
                    u_c >= 2 || v_c >= 2 || i_c >= 2 || l_c >= 2 || y_c >= 2 ||
                    z_c >= 2 || m_c >= 2) {
                    s_c = false; // These letters can not be used two or more times
                }
            else if (i[le] === li[r] || i[le] === li[r + 1]) { // If the letter in i is equal
                count += 1; // to the element in li or the one next to it, add one to count
            }
                if (count >= 3) {
                    t_f = false; // No lettter can be used three or more times
                }
        }
    }
    if (t_f === false || s_c === false) {
        console.log(chosen_w);
        console.log("\nYour word is unable to be made from the given blocks.");
    }
    else if (t_f === 0 || s_c === 0) {
        console.log(chosen_w);
        console.log("\nYour word can be made from the given blocks!");
    }
}

can_make_word(p, b);
