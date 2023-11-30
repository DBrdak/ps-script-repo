using System.Collections.ObjectModel;
using System.Diagnostics;

namespace react_app_creator
{
    internal class Program
    {
        private static void Main()
        {
            do
            {
                try
                {
                    UserInterface.DisplayUserInterface();
                    break;
                }
                catch
                {
                    UserInterface.PrintError();
                    break;
                }
            }
            while (true);
        }
    }
}