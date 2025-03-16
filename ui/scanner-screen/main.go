package main

import (
	"embed"
	"log"
	"os/exec"
	"runtime"

	"github.com/wailsapp/wails/v2"
	"github.com/wailsapp/wails/v2/pkg/options"
	"github.com/wailsapp/wails/v2/pkg/options/assetserver"
)

//go:embed all:frontend/dist
var assets embed.FS

func (a *App) RunRFIDScan() (string, error) {
	cmd := exec.Command("python3", "/home/dev/scanner/ui/scanner-screen/backend/rfid_reader.py")
	output, err := cmd.CombinedOutput()
	return string(output), err
}

func LaunchChromiumKioskMode() {
	var cmd *exec.Cmd
	url := "http://localhost:8080" // Replace with the URL or your Wails app's local URL

	// Adjust the command depending on the OS
	switch runtime.GOOS {
	case "linux":
		cmd = exec.Command("chromium", "--kiosk", "--no-first-run", "--disable-translate", url)
	case "windows":
		cmd = exec.Command("C:\\Program Files (x86)\\Chromium\\chromium.exe", "--kiosk", "--no-first-run", "--disable-translate", url)
	case "darwin": // macOS
		cmd = exec.Command("/Applications/Chromium.app/Contents/MacOS/Chromium", "--kiosk", "--no-first-run", "--disable-translate", url)
	default:
		log.Fatalf("Unsupported OS: %s", runtime.GOOS)
	}

	// Start Chromium in kiosk mode
	err := cmd.Start()
	if err != nil {
		log.Fatalf("Failed to start Chromium: %v", err)
	}
	log.Println("Chromium launched in kiosk mode")
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
