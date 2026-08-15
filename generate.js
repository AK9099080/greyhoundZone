const fs = require("fs");
const path = require("path");

const gamesFolder = "./games";
const mediaFolder = "./media";
const placeholder = "placeholder.png"; // default image

const gameFiles = fs.readdirSync(gamesFolder).filter(f => f.endsWith(".html"));
const mediaFiles = fs.readdirSync(mediaFolder);

const games = gameFiles.map(file => {
  const base = file.replace(".html", "");
  
  const logo = mediaFiles.find(img =>
    img.toLowerCase().startsWith(base.toLowerCase())
  );

  return {
    name: base.replace(/-/g, " ").replace(/\b\w/g, c => c.toUpperCase()),
    file: file,
    logo: logo || placeholder
  };
});

fs.writeFileSync("games.json", JSON.stringify(games, null, 2));
console.log("games.json generated with placeholder images!");
