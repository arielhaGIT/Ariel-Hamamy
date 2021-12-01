let Sentence = [6];
Sentence[0] = "More charming than Sarah Netanyahu";
Sentence[1] = "Nicer than Kim Gong On";
Sentence[2] = "More compassionate than Bashar Assad";
Sentence[3] = "Stronger than Iron Man";
Sentence[4] = "Faster then Usain Bolt";
Sentence[5] = "More reliable than Putin";




fetch('https://reqres.in/api/users?').then(
    response => response.json()
).then(
    responseOBJECT => userList(responseOBJECT.data)
).catch(
    err => console.log(err)
);

function userList (users) {
    console.log(users[0])
 const curr_main = document.querySelector("main");
    for (let i = 0; i<users.length ;  i++) {
        const user = users[i];
        const section = document.createElement('section');
        section.innerHTML =`
          <img src ="${user.avatar}" alt = "d"/>
          <div>
          <span>${user.first_name} ${user.last_name}</span>
          <br>
           <span>email : ${user.email} </span>
           <br>
           <span>"Dor is ${Sentence[i]}"</span>
          </div>
       
            `;
       curr_main.appendChild(section);

    }

}


