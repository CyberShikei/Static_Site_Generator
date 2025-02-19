const images = "/images";

const icons = [
    { name: "profile_pic", url: "/", img: `${images}/profile_pic.jpg` },
    { name: "GitHub", url: "https://github.com/CyberShikei", img: `${images}/github_logo.png` },
    { name: "LinkedIn", url: "https://www.linkedin.com/in/jacobus-petrus-ferreira-b888141a1/", img: `${images}/linkedin_logo.png` },
    { name: "Gmail", url: "mailto:cyber.shikei.com", img: `${images}/gmail_logo.png` },
];

const iconContainer = document.getElementById("icon-container");

icons.forEach(icon => {
    const iconElement = document.createElement("div");
    iconElement.classList.add("icon");

    iconElement.innerHTML = `
        <a href="${icon.url}" target="_blank" class="icon-link", id="${icon.name}">
            <img src="${icon.img}" alt="${icon.name}" class="icon-image" id="${icon.name}">
        </a>
    `;

    iconContainer.appendChild(iconElement);
});

