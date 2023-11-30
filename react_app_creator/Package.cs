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
            "@emotion/react",
            "@emotion/styled",
            "@fontsource/roboto",
            "@mui/icons-material",
            "@mui/lab",
            "@mui/material",
            "@mui/styles",
            "@mui/x-date-pickers"
        });
        public static readonly Package ReactRouter = new(2, "ReactRouter", new []
        {
            "react-router-dom",
        });
        public static readonly Package Formik = new(3, "Formik", new []
        {
            "formik"
        });
        public static readonly Package Axios = new(4, "Axios" , new[]
        {
            "axios"
        });
        public static readonly Package MobX = new(5, "MobX", new[]
        {
            "mobx",
            "mobx-react-lite"
        });
        public static readonly Package Toastify = new(6, "Toastify", new[]
        {
            "react-toastify"
        });
        public static readonly Package Yup = new(7, "Yup", new[]
        {
            "yup"
        });
        public static readonly Package Uuid = new(8, "Uuid" , new[]
        {
            "uuid",
            "@types/uuid"
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
