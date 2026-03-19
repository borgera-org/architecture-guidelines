FROM mcr.microsoft.com/dotnet/sdk:{{ dotnetImageTag }} AS build
WORKDIR /src

COPY ["Directory.Build.props", "./"]
COPY ["src/{{ rootNamespace }}/{{ rootNamespace }}.csproj", "src/{{ rootNamespace }}/"]

RUN dotnet restore "src/{{ rootNamespace }}/{{ rootNamespace }}.csproj"

COPY . .

RUN dotnet publish "src/{{ rootNamespace }}/{{ rootNamespace }}.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:{{ dotnetImageTag }} AS final
WORKDIR /app

COPY --from=build /app/publish .

EXPOSE 8080

ENV ASPNETCORE_URLS=http://+:8080

ENTRYPOINT ["dotnet", "{{ rootNamespace }}.dll"]
