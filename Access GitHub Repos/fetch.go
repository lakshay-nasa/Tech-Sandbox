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
	var repo string
	flag.StringVar(&repo, "repo", "", "GitHub repository URL")
	flag.Parse()

	if repo == "" {
		fmt.Println("Please provide a GitHub repository URL using the -repo flag")
		os.Exit(1)
	}

	// Remove the protocol and "github.com/" from the URL to get the username and repo name
	parts := strings.Split(repo, "/")
	if len(parts) != 5 {
		fmt.Println("Invalid repository URL")
		os.Exit(1)
	}
	username := parts[3]
	repoName := parts[4]

	// Create the directory to save the repository contents
	dirName := fmt.Sprintf("%s-%s", username, repoName)
	err := os.Mkdir(dirName, 0755)
	if err != nil {
		fmt.Println("Failed to create directory:", err)
		os.Exit(1)
	}

	// Fetch the repository's contents
	resp, err := http.Get(fmt.Sprintf("https://api.github.com/repos/%s/%s/contents", username, repoName))
	if err != nil {
		fmt.Println("Failed to fetch repository contents:", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	// Parse the repository contents as JSON
	var contents []struct {
		Name string `json:"name"`
		URL  string `json:"url"`
	}
	err = json.NewDecoder(resp.Body).Decode(&contents)
	if err != nil {
		fmt.Println("Failed to parse repository contents:", err)
		os.Exit(1)
	}

	// Download each file in the repository
	for _, item := range contents {
		if item.Name == ".gitignore" || item.Name == ".gitattributes" {
			// Ignore Git-specific files
			continue
		}
		resp, err := http.Get(item.URL)
		if err != nil {
			fmt.Printf("Failed to fetch file %s: %s\n", item.Name, err)
			continue
		}
		defer resp.Body.Close()

		// Create the file to write the contents to
		filePath := filepath.Join(dirName, item.Name)
		out, err := os.Create(filePath)
		if err != nil {
			fmt.Printf("Failed to create file %s: %s\n", item.Name, err)
			continue
		}
		defer out.Close()

		// Write the file contents to the file
		buf := make([]byte, 4096) // create a buffer to use with io.CopyBuffer
		_, err = io.CopyBuffer(out, resp.Body, buf)
		if err != nil {
			fmt.Printf("Failed to write file %s: %s\n", item.Name, err)
			continue
		}
		fmt.Printf("File %s downloaded and saved to %s\n", item.Name, filePath)
	}

	fmt.Printf("Repository %s downloaded and saved to %s\n", repo, dirName)
}
