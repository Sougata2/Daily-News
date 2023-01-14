let contentCardsExpandBtn = document.querySelectorAll(".expand-btn")
let contentCardsCloseBtn = document.querySelectorAll(".close-card-container")
let contentCards = document.querySelectorAll(".content-card")

for (let i = 0 ; i < contentCardsExpandBtn.length; i++){
    contentCardsExpandBtn[i].addEventListener('click', function(){
        contentCards[i].classList.remove('hidden')
    })
}
for (let i = 0 ; i  < contentCardsCloseBtn.length; i++){
    contentCardsCloseBtn[i].addEventListener('click', function(){
        contentCards[i].classList.add('hidden')
    })
}
// document.querySelector('.expand-btn').addEventListener('click', function(){
//     document.querySelector('.content-card').classList.remove('hidden')
// })
// document.querySelector('.close-card-container').addEventListener('click', function(){
//     document.querySelector('.content-card').classList.add('hidden')
// })