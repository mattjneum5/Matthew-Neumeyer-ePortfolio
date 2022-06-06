SELECT *
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
ORDER BY 3,4

SELECT *
FROM PortfolioPortfolio..CovidVaccinations
WHERE continent is not null
ORDER BY 3,4

--total cases vs total deaths
--shows likeilihood of dying if you contract covid in your country

SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Death_percentage
FROM PortfolioPortfolio..CovidDeaths
WHERE LOCATION like '%States' and continent is not null
ORDER BY 1,2

--total cases vs population
-- percentage of population that contracted covid

SELECT location, date, total_cases, population, (total_cases/population)*100 as Case_Percentage
FROM PortfolioPortfolio..CovidDeaths
WHERE LOCATION like '%States' and continent is not null
ORDER BY 1,2

-- countries with highest infection rate compared to population
SELECT location, population, MAX(total_cases) as HighestInfectionCount, (total_cases/population)*100 as Case_Percentage
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
GROUP BY location, population, total_cases
ORDER BY Case_Percentage desc


-- countries with highest death count per population
SELECT location,  MAX(cast(total_deaths as int)) as TotalDeathCount
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
GROUP BY location
ORDER BY TotalDeathCount desc

--continents with highest death count per population
SELECT continent,  MAX(cast(total_deaths as int)) as TotalDeathCount
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
GROUP BY continent
ORDER BY TotalDeathCount desc

SELECT location,  MAX(cast(total_deaths as int)) as TotalDeathCount
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is null
GROUP BY location
ORDER BY TotalDeathCount desc

SELECT continent, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Death_percentage
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
ORDER BY 1,2

SELECT continent, date, total_cases, population, (total_cases/population)*100 as Case_Percentage
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
ORDER BY 1,2

SELECT continent, population, MAX(total_cases) as HighestInfectionCount, (total_cases/population)*100 as Case_Percentage
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
GROUP BY continent, population, total_cases
ORDER BY Case_Percentage desc

SELECT continent,  MAX(cast(total_deaths as int)) as TotalDeathCount
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
GROUP BY continent
ORDER BY TotalDeathCount desc

--global numbers

SELECT date, SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as Death_percentage
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
GROUP BY date
ORDER BY 1,2

SELECT SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as Death_percentage
FROM PortfolioPortfolio..CovidDeaths
WHERE continent is not null
ORDER BY 1,2

SELECT *
FROM PortfolioPortfolio..CovidVaccinations

SELECT*
FROM PortfolioPortfolio..CovidDeaths dea
Join PortfolioPortfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
FROM PortfolioPortfolio..CovidDeaths dea
Join PortfolioPortfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null and vac.new_vaccinations is not null
ORDER BY 1,2,3

--total population vs vaccinations

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(Cast(vac.new_vaccinations as int)) OVER (Partition by dea.location)
FROM PortfolioPortfolio..CovidDeaths dea
Join PortfolioPortfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null 
ORDER BY 2,3

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
, (RollingPeopleVaccinated/population)*100
FROM PortfolioPortfolio..CovidDeaths dea
Join PortfolioPortfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null 
ORDER BY 2,3

With PopvsVac(continent, location, date, population, new_vaccinations, RollingPeopleVaccinated)
as
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
FROM PortfolioPortfolio..CovidDeaths dea
Join PortfolioPortfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null 
)
SELECT *, (RollingPeopleVaccinated/population)*100
FROM PopvsVac

Create Table #PercentPopulationVaccinated
(
continent nvarchar(255),
location nvarchar(255),
date datetime,
population numeric,
new_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
FROM PortfolioPortfolio..CovidDeaths dea
Join PortfolioPortfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null 

SELECT *, (RollingPeopleVaccinated/population)*100
FROM #PercentPopulationVaccinated


-- creating view to store data for later visualizations

Create View PercentPopulationVaccinated as
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
FROM PortfolioPortfolio..CovidDeaths dea
Join PortfolioPortfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null 







 















