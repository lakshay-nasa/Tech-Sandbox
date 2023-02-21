package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	// Parse the command-line arguments
	var repoURL string
	flag.StringVar(&repoURL, "repo", "", "the URL of the repository to fetch")
	flag.Parse()

	if repoURL == "" {
		fmt.Println("Please specify a repository URL using the -repo flag.")
		os.Exit(1)
	}

	// Split the URL into parts
	parts := strings.Split(repoURL, "/")
	if len(parts) < 4 {
		fmt.Println("Invalid repository URL:", repoURL)
		os.Exit(1)
	}
	owner := parts[len(parts)-2]
	repo := parts[len(parts)-1]

	// Create a temporary directory to download the repository into
	dirName, err := os.MkdirTemp("", "fetch-repo-*")
	if err != nil {
		fmt.Println("Failed to create temporary directory:", err)
		os.Exit(1)
	}

	// Fetch the repository contents
	url := fmt.Sprintf("https://api.github.com/repos/%s/%s/contents", owner, repo)
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		fmt.Println("Failed to create request:", err)
		os.Exit(1)
	}
	req.Header.Set("Accept", "application/vnd.github.v3+json")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Println("Failed to fetch repository contents:", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	// Parse the repository contents as JSON
	var contents []struct {
		Name string `json:"name"`
		URL  string `json:"download_url"`
	}
	err = json.NewDecoder(resp.Body).Decode(&contents)
	if err != nil {
		fmt.Println("Failed to parse repository contents:", err)
		os.Exit(1)
	}

	// Download the files from the repository
	for _, c := range contents {
		if c.Name == ".gitignore" || c.Name == ".gitattributes" {
			continue
		}

		resp, err := http.Get(c.URL)
		if err != nil {
			fmt.Printf("Failed to fetch file %s: %s\n", c.Name, err)
			os.Exit(1)
		}
		defer resp.Body.Close()

		// Create the file to write the contents to
		filePath := filepath.Join(dirName, c.Name)
		out, err := os.Create(filePath)
		if err != nil {
			fmt.Printf("Failed to create file %s: %s\n", c.Name, err)
			os.Exit(1)
		}
		defer out.Close()

		// Write the file contents to the file
		_, err = io.Copy(out, resp.Body)
		if err != nil {
			fmt.Printf("Failed to write file %s: %s\n", c.Name, err)
			os.Exit(1)
		}

		fmt.Printf("File %s downloaded and saved to %s\n", c.Name, filePath)
	}

	fmt.Printf("Repository downloaded to %s\n", dirName)
}
