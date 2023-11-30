using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace react_app_creator
{
    internal class UserInterface
    {
        private const string nameRegex = "^[a-z-]{3,25}$";
        private static int selectedOptionId = 1;
        private static int confirmedOptionId = 0;

        public static void DisplayUserInterface()
        {
            Console.Clear();

            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine("Running React App Creator");
            Console.ForegroundColor = ConsoleColor.White;

            Console.Write("App name: ");
            var appName = Console.ReadLine() ?? "react-app";

            if (!Regex.IsMatch(appName, nameRegex)) appName = "react-app";

            PrintInfo("Initialazing React app...");
            var settings = new Settings(appName);
            PrintSuccess("React app created!");

            Console.Write("Github enabled [y/n]: ");
            var isGitEnabled = GetGitInfo(Console.ReadLine()?.ToLower());

            if (!isGitEnabled)
                settings.DisableGithub();

            PrintInfo("Adjusting file structure...");
            settings.AdjustReactApp();
            PrintSuccess("Files are adjusted successfully!");

            Package? package;

            do
            {
                package = UserInterface.DisplayMenu();
                settings.AddPackage(package);
            }
            while (package is not null);

            PrintInfo("Installing packages...");

            settings.InstallPackages();

            PrintSuccess("Packages successfully installed!\nYour app is ready! ✅");
        }



        private static bool GetGitInfo(string? gitAnswer) => gitAnswer != "n";

        private static Package? DisplayMenu()
        {
            do
            {
                PrintMenu();

                ConsoleKeyInfo keyInfo = Console.ReadKey(true);

                switch (keyInfo.Key)
                {
                    case ConsoleKey.UpArrow:
                        selectedOptionId = Math.Max(1, selectedOptionId - 1);
                        break;
                    case ConsoleKey.DownArrow:
                        selectedOptionId = Math.Min(Package.All.Count + 1, selectedOptionId + 1);
                        break;
                    case ConsoleKey.Enter:
                        confirmedOptionId = selectedOptionId;
                        break;
                }
            }
            while (confirmedOptionId == 0);

            if (confirmedOptionId == Package.All.Count + 1)
            {
                return null;
            }

            var package = Package.FromId(confirmedOptionId);

            selectedOptionId = 1;
            confirmedOptionId = 0;

            return package;
        }

        private static void PrintMenu()
        {
            Console.Clear();
            Console.WriteLine("Choose package:");

            foreach (var package in Package.All)
            {
                PrintMenuItem(package.Id, package.Name);
            }

            PrintMenuItem(Package.All.Count + 1, "Exit");
        }

        private static void PrintMenuItem(int? menuItemId, string text)
        {
            if (selectedOptionId == menuItemId)
            {
                Console.ForegroundColor = ConsoleColor.Blue;
            }

            Console.WriteLine(menuItemId.HasValue ? $"{menuItemId}. {text}" : $"{text}");

            Console.ForegroundColor = ConsoleColor.White;
        }

        public static void PrintError()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Error occured, try again");
            Console.ForegroundColor = ConsoleColor.White;
            Thread.Sleep(1500);
        }

        public static void PrintSuccess(string successMessage)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.OutputEncoding = Encoding.UTF8;
            Console.WriteLine(successMessage);
            Console.ForegroundColor = ConsoleColor.White;
        }

        public static void PrintInfo(string info)
        {
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.OutputEncoding = Encoding.UTF8;
            Console.WriteLine(info);
            Console.ForegroundColor = ConsoleColor.White;
        }
    }
}
