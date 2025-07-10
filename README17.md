# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd886902-59e9-34b0-bd65-54137fd93544 | -6.86722 | -42.78217 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad404601-30a2-392c-9b33-e48d866c7e4b | -7.29106 | -44.64314 | 2025-07-10 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a965c205-a7ce-3688-b784-b5f18d439be4 | -8.49998 | -43.31063 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 7ccd1088-29ee-3c46-a43a-235c4f62cacc | -10.56756 | -49.1482 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c4f22c8-a8e6-32e6-bae9-a6f755014c02 | -8.50186 | -43.31766 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 0d51bbd9-f957-36a9-92fe-4311ba29a53b | -8.50619 | -43.31382 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 50ed0894-bfac-335c-bf5d-ee341356407b | -11.90494 | -44.90684 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03be39a6-ec26-35b6-b568-fe83c731bc9a | -4.2851 | -48.18648 | 2025-07-10 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4074ded1-7760-3ae5-84ca-e837b7a12564 | -8.50122 | -43.32205 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85f57f3d-11ed-3b7d-b637-306952718020 | -8.96265 | -47.2701 | 2025-07-10 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9c83283-d19e-3d22-8c5a-043bd67d4f92 | -8.50987 | -43.31437 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| da9fe19c-5181-3861-97c6-d7f7e21cee42 | -8.50264 | -43.29308 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 293c299e-16fd-3a99-a6d8-d448477fe874 | -9.83395 | -41.49561 | 2025-07-10 04:25:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0a277f1e-eb59-3661-b5a4-83cac6d2fe15 | -9.31961 | -49.22364 | 2025-07-10 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e06c503b-62f4-352f-8d95-aa9d450e520d | -9.65845 | -49.88986 | 2025-07-10 04:25:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99984101-9055-3272-9c28-9bd0802f4b9c | -10.71559 | -48.40476 | 2025-07-10 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c68594a4-e311-340f-b0d2-955e111398d8 | -6.85342 | -42.79838 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| adee0be2-48e0-3363-8f70-a0749eb7579d | -8.50314 | -43.30887 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| d5abb95e-4bd5-3bcd-8e01-2b730e31b983 | -11.36727 | -48.70287 | 2025-07-10 04:25:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b970802-fd36-361e-b397-b65d54d1571f | -6.68925 | -43.09996 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bbc189d-dcc3-37fd-93ee-4af58bf0f779 | -6.13098 | -42.9598 | 2025-07-10 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d65da7ab-f318-3c90-aea0-6b941d904c92 | -7.01138 | -43.49181 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45881496-86d0-3a0e-a67b-03e33fcb9577 | -7.22351 | -43.07689 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5aee7e6e-4db1-35c0-85d9-2d5d5d7dc546 | -6.84434 | -44.06459 | 2025-07-10 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c22e4bb8-005b-37a4-8761-7a939d26e6e0 | -9.82975 | -41.495 | 2025-07-10 04:25:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a907bcd6-cc50-3f0a-8121-4090cd21c5ac | -8.49762 | -43.30131 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 9cdd69a0-df44-3c34-974e-1ed11089fd20 | -10.62109 | -45.23367 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64d1671a-b79c-37d4-8660-5a8804bf1ab9 | -7.02871 | -43.4986 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0e25c7d-c2d7-3eb5-8d2c-fd80947c9f06 | -6.86458 | -42.8 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad151a5d-f447-33b0-a963-185d1aa08387 | -7.23152 | -43.07368 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b6e1d0ff-5c6c-3ee6-9351-f37d3feac1c8 | -6.64549 | -43.19084 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67d00afd-9a4f-3096-a08f-1ef409969889 | -10.65581 | -49.46768 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf177ec5-dcb1-3e0e-8838-1b02e8b8eb30 | -9.09028 | -47.96222 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe33c86f-4d25-3a7c-b640-932cd9736810 | -7.01847 | -49.18615 | 2025-07-10 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a7c15c0-dca5-3273-8bc1-f0fefa4962a4 | -8.50009 | -43.30392 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| ddda3d94-d69d-3618-87d2-723964268727 | -6.1419 | -45.87389 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f965a0f2-5fbc-3752-9665-a29a90dc4c7d | -6.68012 | -43.76794 | 2025-07-10 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c09ee177-e4a8-362f-95d6-dfbdb9f0e957 | -8.50491 | -43.3226 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 208c26a3-f2b2-387e-ad80-071acce2d9eb | -9.30608 | -40.2434 | 2025-07-10 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f55b1f8c-0d7a-346a-9ab0-d072a77ae933 | -10.65924 | -49.46826 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ab18e99b-a01d-39bf-b0d4-ae47ba957850 | -9.21201 | -48.59627 | 2025-07-10 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f5536ac-e4e2-32ae-8928-c1af4a92df59 | -8.50088 | -43.27248 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5a33c1c4-acb1-3c2d-844f-6ada00279ba1 | -6.99452 | -43.50628 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c184bbc-4ee2-3dce-a6ef-b6460b1aaec7 | -6.45484 | -44.56831 | 2025-07-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d96cc7fa-fb81-3122-a37d-0a147ddd7fd8 | -10.62396 | -45.238 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c3495350-78e0-3c9b-9180-75cd18f764b6 | -8.50531 | -43.27542 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| a1f7b289-00af-3801-9a51-b7968830d719 | -4.22831 | -47.20856 | 2025-07-10 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09102d53-fd49-31dd-b0c0-2a508389d3f7 | -10.62798 | -45.2347 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ebdc20-8dae-34df-a7ce-469d78bccc19 | -8.8877 | -47.33656 | 2025-07-10 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eae23c47-059f-396f-bc2f-0fe7e0d0f732 | -6.8473 | -42.78833 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c0d88b8-cfe9-372d-b6eb-919f31eb8414 | -7.11281 | -47.8335 | 2025-07-10 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4258c3b5-8f58-39d6-80d0-5f89677d4049 | -7.95011 | -49.65011 | 2025-07-10 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd6040b-acaa-38fd-bee0-c8174a1915ef | -11.36334 | -48.70591 | 2025-07-10 04:25:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 022b4d5d-e100-3e30-8a03-4cb8cb406e9a | -8.3334 | -49.18844 | 2025-07-10 04:25:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9005c7b9-0caf-31b2-8637-768f4d0aa988 | -6.67658 | -43.76743 | 2025-07-10 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b2543d4-e4a8-35ce-a468-b7f1835cae5b | -8.49828 | -43.29692 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| feeb6866-0ee7-31b8-967b-13c1f9aaa27b | -6.67938 | -46.30253 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4c37a3c-02db-3faf-afda-a5b80b5adb17 | -9.18079 | -47.18004 | 2025-07-10 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5f34e67-2859-3b5d-856d-5aaa3dbc53a0 | -10.57376 | -49.15302 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1b4847c6-79fa-3421-8947-e6b17d6fdd6a | -7.04284 | -43.28342 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 64393023-86b1-3d66-9460-2fe5284f449b | -6.80212 | -59.04877 | 2025-07-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b4af67e-e336-37b6-8fc4-aa857323f81a | -6.72536 | -43.89959 | 2025-07-10 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39f5c7f8-c383-3fb2-afe5-674ae19105d1 | -7.46259 | -49.39697 | 2025-07-10 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9791a8cc-8035-3be9-9ec1-f78608871bc4 | -6.95392 | -42.7127 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 02e617fe-9b7c-3878-b75e-c385bf7155fa | -10.61531 | -48.07566 | 2025-07-10 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 337deead-40d3-3165-8606-8f0e57a63b2e | -7.80945 | -46.57049 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc481d14-252a-3c22-8dce-82769f7311f8 | -7.00999 | -44.42132 | 2025-07-10 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea2932ec-416a-3fda-b10a-2254d7f3e70f | -11.67504 | -43.7816 | 2025-07-10 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2b9aac7-78e6-39ac-b891-f25092c59a4d | -8.49768 | -43.29457 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 9c514690-b442-38cc-9a21-14a5e45ae5f6 | -5.88928 | -45.57843 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43c93496-bcb9-31dd-ae84-82076f37c23e | -11.37962 | -48.05597 | 2025-07-10 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13a60938-6101-37cb-a8db-1ce9e164ebbe | -6.57365 | -42.90024 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 873c8384-74da-343b-a829-d6b238d6cfbb | -5.54997 | -43.8952 | 2025-07-10 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ede1aeaa-635c-3552-98b5-28dec663d6e1 | -11.46266 | -45.10879 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e794810-bc25-3c49-8aed-30ab4a3c0e36 | -8.8581 | -47.95026 | 2025-07-10 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 07f88f7b-ff43-3d16-b41b-604f81097933 | -6.72477 | -43.90348 | 2025-07-10 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73265839-c8a6-31a0-9b84-1f19abb2db4e | -10.96834 | -49.25178 | 2025-07-10 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f19a171-be22-3083-bb32-e6ebf370d46a | -10.66454 | -49.45742 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1b4d5068-b09a-3ed6-a51a-971ac5a0f967 | -8.50683 | -43.30943 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 7abe6385-1a70-359c-b771-19b7df8bf0cc | -10.98965 | -44.32985 | 2025-07-10 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e034540a-f3f0-3e9c-93c9-de94b456a2a9 | -8.49959 | -43.28135 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 3708047e-96ca-37a8-a4db-2459625eeee7 | -9.82919 | -41.49889 | 2025-07-10 04:25:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ad711bdd-f232-3944-8c1d-cb6f48732955 | -10.66048 | -49.46065 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d064f77d-e8da-3a4d-8abe-fb845d5bd829 | -6.9964 | -43.49382 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c7c798e-0d62-339a-8b58-9905ce6497e5 | -8.39289 | -44.03545 | 2025-07-10 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 929dff47-81e5-33c0-b6e8-0f6ecbcf599c | -8.35495 | -43.95234 | 2025-07-10 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5aac133f-47d9-398f-a354-7de8db4b22df | -8.5025 | -43.31327 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 6286c2a3-245b-345f-a178-46d47b8f2819 | -10.56938 | -49.13709 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1efcaee8-b260-38ea-98dc-7867eec7fd4d | -6.13163 | -42.95554 | 2025-07-10 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e837c8a2-44dd-3f17-b27b-9b4e6991c7c7 | -7.95366 | -49.65069 | 2025-07-10 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b49fd762-6784-3d75-bf92-b0878982597a | -6.67883 | -46.30598 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9c92ed4-c00a-303c-ab92-8bb4ea704951 | -8.49931 | -43.31502 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb3d2c9f-dcdf-3ac1-89be-c5046b2b8096 | -11.36668 | -48.70647 | 2025-07-10 04:25:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ca818b82-191b-3218-a02a-1fc3b0712948 | -6.93946 | -43.02482 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5432696e-95fa-32bf-a4f1-3c89f8b9aa02 | -9.21479 | -48.60047 | 2025-07-10 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f2aa86c-2171-32b4-91a6-abfd95c5263a | -10.56877 | -49.14079 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| dc2eb5f7-7753-3e7b-a68d-26d5584b0be8 | -9.30116 | -44.84494 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ae01dcd-6950-39f9-95a0-127ca5f178f5 | -7.00466 | -43.51197 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 851d612b-0e41-3579-b53d-16bb3a9c7c29 | -10.57678 | -49.13449 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 45fa6c64-79fd-31c9-be0b-95102561fef2 | -8.50875 | -43.29623 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |


[Clique aqui para ver as próximas entradas](README18.md)
