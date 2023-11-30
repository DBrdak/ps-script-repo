using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace react_app_creator
{
    internal class Settings
    {
        public bool IsGithubRequired { get; private set; }
        private readonly List<Package> _packages;
        public ImmutableList<Package> Packages => _packages.ToImmutableList();
        public string AppName { get; init; }

        private void InitReactApp()
        {
            Cmd.Execute($"npx create-react-app {AppName} --template typescript");
        }

        private void ReplaceFiles()
        { 
            var processPath = Environment.ProcessPath;
            var i = processPath!.IndexOf(@"\bin\Debug\net7.0\react_app_creator.exe", StringComparison.Ordinal);
            var pathToBasicFiles = processPath[..i] + @"\BasicFiles\";

            Cmd.Execute($@"copy /Y {pathToBasicFiles}\App.tsx .\{AppName}\src\App.tsx");
            Cmd.Execute($@"copy /Y {pathToBasicFiles}\tsconfig.json .\{AppName}\tsconfig.json");
            Cmd.Execute($@"copy /Y {pathToBasicFiles}\index.html .\{AppName}\public\index.html");
            Cmd.Execute($@"copy /Y {pathToBasicFiles}\manifest.json .\{AppName}\public\manifest.json");
        }

        private void RemoveUnnecessaryFiles()
        {
            Cmd.Execute($@"del .\{AppName}\src\setupTests.ts");
            Cmd.Execute($@"del .\{AppName}\src\logo.svg");
            Cmd.Execute($@"del .\{AppName}\src\App.test.tsx");
            Cmd.Execute($@"del .\{AppName}\src\App.css");
            Cmd.Execute($@"del .\{AppName}\public\favicon.ico");
            Cmd.Execute($@"del .\{AppName}\public\logo192.png");
            Cmd.Execute($@"del .\{AppName}\public\logo512.png");

            if (IsGithubRequired) return;

            Cmd.Execute($@"del .\{AppName}\README.md");
            Cmd.Execute($@"del .\{AppName}\.gitignore");
        }

        public Settings(string appName)
        {
            IsGithubRequired = true;
            _packages = new List<Package>();
            AppName = appName;

            InitReactApp();
        }

        public void AddPackage(Package? package)
        {
            if (package is null || _packages.Contains(package))
            {
                return;
            }

            _packages.Add(package);
        }

        public void DisableGithub() => IsGithubRequired = false;

        public void AdjustReactApp()
        {
            RemoveUnnecessaryFiles();
            ReplaceFiles();
        }

        public void InstallPackages()
        {
            if (!_packages.Any())
            {
                return;
            }

            Console.WriteLine($"{string.Join(" ", _packages.SelectMany(p => p.NodeNames))}");

            Cmd.Execute($"npm install {string.Join(" ", string.Concat(_packages.SelectMany(p => p.NodeNames)), " --force")}", $"./{AppName}");
        }
    }
}
