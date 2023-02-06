var articles = [
    {name: "Bike", cost: 540},
    {name: "TV", cost: 1200},
    {name: "Laptop", cost: 3400}
];


var expensiveArticles = articles.filter(function (article){return article.cost > 600});
console.log("The most expensive articles: " + expensiveArticles);


var upperCaseArticles = articles.map(function (article){
    article.name = article.name.toUpperCase();
    return article;
});
console.log("Upper case artiles names: " + upperCaseArticles);


var articleFound = articles.find(function (article) {return article.name === "LAPTOP"});
console.log("I found this article: " + articleFound.name);


articles.forEach(function (article){
    console.log("The article is: " + article.name);
});

var newArticles = articles.some(function (article) { return article.cost < 600});
console.log("There is any article which is less than 600 USD? " + newArticles);