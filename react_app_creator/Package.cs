using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace react_app_creator
{
    public record Package
    {
        public int Id { get; init; }
        public string Name { get; init; }
        public ImmutableList<string> NodeNames { get; init; }

        private Package(int id, string name, string[] nodeNames)
        {
            (Id, Name) = (id, name);
            NodeNames = nodeNames.ToImmutableList();
        }

        // ReSharper disable once InconsistentNaming
        public static readonly Package MaterialUI = new(1, "MaterialUI", new []
        {
            "@mui/material@latest",
            "@emotion/react@latest",
            "@emotion/styled@latest",
            "@fontsource/roboto@latest",
            "@mui/icons-material@latest",
            "@mui/lab@latest",
            "@mui/x-date-pickers@latest"
        });
        public static readonly Package ReactRouter = new(2, "ReactRouter", new []
        {
            "react-router-dom@latest",
        });
        public static readonly Package Formik = new(3, "Formik", new []
        {
            "formik@latest"
        });
        public static readonly Package Axios = new(4, "Axios" , new[]
        {
            "axios@latest"
        });
        public static readonly Package MobX = new(5, "MobX", new[]
        {
            "mobx@latest",
            "mobx-react-lite@latest"
        });
        public static readonly Package Toastify = new(6, "Toastify", new[]
        {
            "react-toastify@latest"
        });
        public static readonly Package Yup = new(7, "Yup", new[]
        {
            "yup@latest"
        });
        public static readonly Package Uuid = new(8, "Uuid" , new[]
        {
            "uuid@latest",
            "@types/uuid@latest"
        });

        public static readonly IReadOnlyCollection<Package> All = new[]
        {
            MaterialUI,
            ReactRouter,
            Formik,
            Axios,
            MobX,
            Toastify,
            Yup,
            Uuid,
        };

        public static Package FromName(string name) =>
            All.FirstOrDefault(p => p.Name.Equals(name, StringComparison.OrdinalIgnoreCase)) ??
            throw new ArgumentException($"{name} is an invalid package name");

        public static Package FromId(int id) =>
            All.FirstOrDefault(p => p.Id == id) ??
            throw new ArgumentException($"{id} is an invalid package ID");

        public string ToNodeName() => string.Join(" ", NodeNames);
    }
}
