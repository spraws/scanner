package main

import (
	"embed"
	"fmt"
	"os"
	"os/exec"
	"strings"

	"github.com/wailsapp/wails/v2"
	"github.com/wailsapp/wails/v2/pkg/options"
	"github.com/wailsapp/wails/v2/pkg/options/assetserver"
)

//go:embed all:frontend/dist
var assets embed.FS

func (a *App) RunRFIDScan() (string, error) {
	// Use Python from virtual environment
	cmd := exec.Command("/home/dev/scanner/.venv/bin/python3", "/home/dev/scanner/main.py")

	// Set the working directory
	cmd.Dir = "/home/dev/scanner"

	// Set environment variables including virtual env activation
	cmd.Env = append(os.Environ(),
		"VIRTUAL_ENV=/home/dev/scanner/.venv",
		"PYTHONPATH=/home/dev/scanner/.venv/lib/python3.9/site-packages",
		"PATH=/home/dev/scanner/.venv/bin:"+os.Getenv("PATH"),
	)

	output, err := cmd.CombinedOutput()
	outputStr := string(output)

	// Log the output for debugging
	fmt.Printf("Python output: %s\n", outputStr)

	if err != nil {
		return "", fmt.Errorf("scanner error (%v): %s", err, outputStr)
	}

	if outputStr == "" {
		return "", fmt.Errorf("no output from scanner (check if card is present)")
	}

	return strings.TrimSpace(outputStr), nil
}

func main() {
	// Create an instance of the app structure
	app := NewApp()
	// LaunchChromiumKioskMode()
	// Create application with options
	err := wails.Run(&options.App{
		Title:     "scanner-screen",
		Width:     1280,
		Height:    720,
		Frameless: true,
		AssetServer: &assetserver.Options{
			Assets: assets,
		},
		BackgroundColour: &options.RGBA{R: 27, G: 38, B: 54, A: 1},
		OnStartup:        app.startup,
		Bind: []interface{}{
			app,
		},
		WindowStartState: options.Fullscreen,
		DisableResize:    true,
	})

	if err != nil {
		println("Error:", err.Error())
	}
}
