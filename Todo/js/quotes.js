const quotes = [
    {
        quote: "나는 다른 사람의 행동을 비웃거나 탄식하거나 싫어하지 않았다. 오로지 이해하려고만 하였다. ",
        author: "스피노자"
    },
    {
        quote: "똥 마렵다",
        author : "박종국"
    },
    {
        quote : "인간의 힘으로 이해할 수 없는 일이 생기면, 인간은 새로운 말을 만든다.",
        author : "괴테"
    },
    {
        quote : "벽까지 몰아 붙이지 말아라.",
        author: "임어당"
    },
    {
        quote : "기대하는 대로 얻는다. ",
        author: "앤드류 매튜스"
    },
    {
        quote : "항상 성취를 목표로 삼아라. 그리고 성공은 잊어버려라.",
        author: "헬렌 헤이즈"
    },
    {
        quote : "나는 찬스가 올 것에 대비하여 배우고, 언제나 닥칠 일에 착수할 수 있는 태도를 갖추고 있다.",
        author: "링컨"
    },
    {
        quote : "옳은 행동을 하고 남보다 먼저 모범을 보이는 것이 교육이라는 것이다.",
        author: "순자"
    },
    {
        quote : "그 사람의 말을 듣고 그 사람의 눈동자를 보면 그 사람을 알 수가 있다. 그 사람이 어떻게 해서 자기를 숨길 수가 있단 말인가.",
        author: "맹자"
    },
    {
        quote : "고요한 마음에는 세상도 감복한다.",
        author: "도교"
    }
]

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const today_quote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = today_quote.quote;
author.innerText = today_quote.author;