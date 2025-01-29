const username = "CyberShikei"; // Replace with your GitHub username
const repoList = document.getElementById("repo-list");

async function fetchRepos() {
    try {
        const response = await fetch(`https://api.github.com/users/${username}/repos`);
        if (!response.ok) throw new Error("Failed to fetch repositories");

        const repos = await response.json();
        console.log(repos); // Check if repos are fetched successfully
        
        repos.sort((a, b) => a.name.localeCompare(b.name)); // Sort repos alphabetically
        
        // Clear any previous content
        repoList.innerHTML = '';

        // Loop through each repository and fetch the icon
        for (const repo of repos) {
            const repoIconUrl = `https://raw.githubusercontent.com/${username}/${repo.name}/main/icon.png`;

            // Make a HEAD request to check if the icon exists
            const iconResponse = await fetch(repoIconUrl, { method: 'HEAD' });

            // Only display the repo if the icon exists
            if (iconResponse.ok) {
                const repoCard = `
                    <div class="repo-card">
                        <!-- Only the box is a clickable link -->
                        <a href="${repo.html_url}" target="_blank">
                            <div class="repo-image">
                                <img src="${repoIconUrl}" alt="${repo.name}" onError="this.onerror=null;this.src='https://via.placeholder.com/150';">
                            </div>
                            <h3>${repo.name}</h3>
                        </a>
                        <!-- Plain text description without a link -->
                        <p>${repo.description || "No description available"}</p>
                    </div>
                `;
                repoList.innerHTML += repoCard;
            }
        }
    } catch (error) {
        console.error("Error loading repositories:", error); // Log error if any
        repoList.innerHTML = `<p>Error loading repositories: ${error.message}</p>`;
    }
}

fetchRepos();




