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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9532a62-7c33-35f4-93fb-64fb5bf573c1 | -14.4467 | -48.9063 | 2025-06-24 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 136.5 |
| d0543f82-e611-380d-9fcc-cdd70c558681 | -17.3442 | -42.6333 | 2025-06-24 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 018da0c8-0021-3c3f-a5b5-dad5c73d03b0 | -17.3435 | -42.6581 | 2025-06-24 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 260.6 |
| 6ca8695b-7c08-3517-a73c-a2da089d96ee | -10.883 | -56.4567 | 2025-06-24 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d304b1a6-397e-3aee-9747-77a98037b4b5 | -13.0793 | -48.8196 | 2025-06-24 00:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c77f6ef9-8ffd-3261-9982-8da713053303 | -5.77 | -43.6148 | 2025-06-24 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| e66de607-bb46-3e22-a22b-86b3842a7e3a | -13.0789 | -48.8417 | 2025-06-24 00:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 388ec08f-d2a9-3b7e-a849-9275d95d07c8 | -7.2025 | -43.1171 | 2025-06-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 794b3418-b218-3d18-ba39-22896ab4608b | -17.3235 | -42.663 | 2025-06-24 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 5646cf51-7505-3881-92c7-46bb0c0aa754 | -5.7887 | -43.6134 | 2025-06-24 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b8ea4d77-496d-3a9e-a1ea-d20330095b39 | -4.543 | -47.9934 | 2025-06-24 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3325e807-2a6a-3c0b-80aa-5af8e665479b | -4.5429 | -48.0151 | 2025-06-24 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0aa47462-c381-39fc-a744-475701f7ff9d | -8.5722 | -51.5761 | 2025-06-24 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b60d20ba-db01-3c97-9944-72a79ba629e4 | -14.1669 | -50.4353 | 2025-06-24 00:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 42e719b7-174e-3f3a-bfd1-779b3a3af9c2 | -14.4273 | -48.9093 | 2025-06-24 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1429f09a-c0bb-365f-9430-30c933d98829 | -8.07 | -43.1216 | 2025-06-24 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 62a3a651-11f0-395b-abac-c9018e951383 | -8.0703 | -43.0981 | 2025-06-24 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| a9679aa7-fe6f-3408-9ac4-8e9c27d73f95 | -14.4463 | -48.9285 | 2025-06-24 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7e66210c-ae2e-33b8-a037-a0276c90d61e | -7.2028 | -43.0936 | 2025-06-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.8 |
| 0702b745-54b8-3141-9dd8-a144e92819b7 | -8.572 | -51.597 | 2025-06-24 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b83c111b-977d-394a-8f02-e5563e3ca6f6 | -16.58636 | -43.66098 | 2025-06-24 00:01:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| fa37ee6d-ee48-315c-a009-4b698b46627e | -17.33719 | -42.65516 | 2025-06-24 00:01:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 332.3 |
| 8493b836-aa26-3562-abff-5d71d979b2c7 | -16.32469 | -43.62738 | 2025-06-24 00:01:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3f8c253b-2d9d-310c-98e1-2eaa6cbb44c6 | -16.58423 | -43.64199 | 2025-06-24 00:01:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 30.7 |
| b6e50a9c-b7f5-3a8b-ac00-afbc54acd8b9 | -17.34885 | -42.65366 | 2025-06-24 00:01:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2fdab98b-dd7c-322e-a466-90a30c996421 | -17.33905 | -42.67192 | 2025-06-24 00:01:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 273.0 |
| 05449890-3959-3715-b429-a913a3308e2b | -17.34092 | -42.68881 | 2025-06-24 00:01:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 88819e52-4a99-3f3b-adcd-f7718bbc454f | -13.08268 | -48.86488 | 2025-06-24 00:03:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 0216c35f-329c-3deb-bcda-346eb5f0c6ed | -13.77238 | -44.10849 | 2025-06-24 00:03:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| f51f1232-fa2b-3b95-885e-ed5792400ba7 | -7.21281 | -43.11104 | 2025-06-24 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 01efb7d5-b007-3510-8cae-cceb1e10395d | -7.20083 | -43.10012 | 2025-06-24 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| c7e8bc69-74c3-3e02-8aa6-585dae880c4d | -13.77026 | -44.08998 | 2025-06-24 00:03:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| d9bbfaf1-0e23-3f5e-a29e-cb6554f7be97 | -10.6602 | -44.50092 | 2025-06-24 00:03:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 490266ed-00f3-3f83-88dd-f8fbd1c58aea | -10.64803 | -44.50244 | 2025-06-24 00:03:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ead19f8b-4db0-354f-bfc2-ad9722176075 | -8.06651 | -43.10039 | 2025-06-24 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| a206770f-5366-347e-9c09-7fdcdc9d8931 | -11.36612 | -43.74342 | 2025-06-24 00:03:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 74580f35-c925-38c7-b966-85ac65d3848c | -12.40433 | -43.81174 | 2025-06-24 00:03:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 7279ae76-4d50-3891-821c-44f410a3eb33 | -13.55055 | -44.09194 | 2025-06-24 00:03:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0a03f9d9-df13-3c64-a3c9-ed3845b90f26 | -8.0698 | -43.12582 | 2025-06-24 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c6a460c7-2f81-3535-9906-5bf04b078e1a | -11.36808 | -43.75947 | 2025-06-24 00:03:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 67105ecf-8f88-369a-98cd-564f351ffa89 | -12.75162 | -44.42022 | 2025-06-24 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 6b9af24b-37ca-3c90-a3dc-9ae1b16bdc46 | -8.24725 | -44.95403 | 2025-06-24 00:03:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| abd5bb8d-baa5-38ca-80ed-20afeb456719 | -7.29658 | -43.20773 | 2025-06-24 00:03:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 325807e9-b616-3f02-a331-51a328ba74b8 | -7.20781 | -43.09325 | 2025-06-24 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| e552fbdd-cc4f-3530-a967-2f7adabb864b | -7.32683 | -43.22288 | 2025-06-24 00:03:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7ff5f665-b790-340a-9ec5-5f8b1ccfe985 | -12.40226 | -43.79473 | 2025-06-24 00:03:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c677bb45-4125-3279-8027-1ff2f04be97b | -9.1203 | -37.1152 | 2025-06-24 00:03:00 | TERRA_M-M | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4f3a14ba-049d-368e-bdbc-2fda48f98a24 | -8.05769 | -43.11448 | 2025-06-24 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 55ad5fbb-9ab0-3c9b-bd34-0fd016c78a43 | -7.9202 | -49.64927 | 2025-06-24 00:03:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 2fbc1889-41f3-3423-94d0-7e870962117c | -10.4611 | -47.00596 | 2025-06-24 00:03:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 2820d1e7-ae15-3909-85af-28b4729cb667 | -7.20249 | -43.11245 | 2025-06-24 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| e7fd4d89-3044-3105-9d3c-d98019052823 | -8.05606 | -43.10178 | 2025-06-24 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| bd0e026d-831d-331a-8ff2-f30379571ebb | -13.07809 | -48.81447 | 2025-06-24 00:03:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d982a5e4-10b1-3b96-8c28-d23c84cbbcac | -7.20939 | -43.1056 | 2025-06-24 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 165.0 |
| f009f25a-190a-305f-9c4c-ed39f40e4cd4 | -8.06815 | -43.11308 | 2025-06-24 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| f93d7681-7fc3-3194-8c67-e767d6ffb633 | -13.25591 | -41.33328 | 2025-06-24 00:03:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 31e66d93-29bb-38d7-b523-eb4c3ee19293 | -12.74936 | -44.40121 | 2025-06-24 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 765cd9b0-b647-3df3-a1a0-30f5f724e889 | -7.48012 | -45.59476 | 2025-06-24 00:03:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 7ed9fa1a-dba6-3828-ae10-8bbb5bd8ded9 | -13.07814 | -48.82144 | 2025-06-24 00:03:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ae587727-492c-369d-ac19-384723ed78fb | -7.91926 | -49.65595 | 2025-06-24 00:03:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 7b1b3465-ea46-3a84-8daa-9df63303058f | -8.05933 | -43.12722 | 2025-06-24 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| ccd1a8c0-7716-3f65-87d7-48915a889ecb | -13.08237 | -48.85817 | 2025-06-24 00:03:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 56001507-c4a6-325b-b15d-d81ad400e0f3 | -7.21114 | -43.09872 | 2025-06-24 00:03:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 4cab1671-e3e3-34ca-9dfc-9143e6de2172 | -4.71397 | -42.76255 | 2025-06-24 00:05:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ecc6636-6376-3d3b-bfd0-b9485445a8b0 | -5.13177 | -45.04276 | 2025-06-24 00:05:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3e1c6fa4-7f04-34f9-94a6-a4a4bfdd19a3 | -7.09503 | -44.37445 | 2025-06-24 00:05:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 75f49abe-de9b-374f-875b-0da2fe1ca258 | -7.01077 | -44.60106 | 2025-06-24 00:05:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 68441c66-03a6-32b3-a081-0a0041150f15 | -3.02515 | -49.43777 | 2025-06-24 00:05:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 7e6ad7c4-f7e8-3c27-bd8c-19d9db06a086 | -4.54734 | -47.99772 | 2025-06-24 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 20a3f9a5-d63d-3f41-bca0-5ec9231727f4 | -5.78944 | -43.61613 | 2025-06-24 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 2f618883-8007-3ca8-8aa2-1d2b33b87573 | -4.9849 | -37.40577 | 2025-06-24 00:05:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e5d4a3ea-6994-330d-9515-98b8571f09ba | -5.9218 | -43.47026 | 2025-06-24 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1162861f-1427-35bc-9497-aea5a09608c2 | -5.76069 | -43.40343 | 2025-06-24 00:05:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f51e46d1-948d-3ce6-9f46-bea8a6323774 | -5.2078 | -43.31767 | 2025-06-24 00:05:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 828fcc02-848e-3bb5-ac24-693dc8b31845 | -5.78774 | -43.60354 | 2025-06-24 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 60500825-ada9-3f98-b11d-466e6c33f1ad | -5.92347 | -43.48289 | 2025-06-24 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 42826c80-40eb-3882-8848-000ee2800671 | -5.48734 | -42.14122 | 2025-06-24 00:05:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| b93d24e5-d549-3f9c-8f24-c803cfb0be53 | -4.53275 | -48.00011 | 2025-06-24 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c91c81bd-0fc6-33c1-bb3f-8071b2ae1521 | -5.1406 | -43.73369 | 2025-06-24 00:05:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 70e0e464-1a68-327e-a4a4-777bcbafaa17 | -6.00766 | -43.753 | 2025-06-24 00:05:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 744f778a-f6f2-30b8-8f38-2c306b911ae8 | -5.77726 | -43.60494 | 2025-06-24 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8bcd8084-955c-3e9d-977a-29c6e1e74432 | -7.01282 | -44.61673 | 2025-06-24 00:05:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7f979497-828b-339c-bc18-bcebbc40acfd | -7.09664 | -44.38056 | 2025-06-24 00:05:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8274b0f6-6b13-3099-a042-989ca85ae738 | -5.99749 | -42.65797 | 2025-06-24 00:05:00 | TERRA_M-M | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3e0589ec-afce-3628-ac0c-1aac5be9934e | -6.25211 | -44.83661 | 2025-06-24 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ab601d2d-c108-3647-8d0a-03ebe866685f | -5.91306 | -43.48423 | 2025-06-24 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 37ea84dc-75d6-39f8-a710-581860717ea3 | -5.12968 | -45.02697 | 2025-06-24 00:05:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 0c3e43fd-282e-3d20-8e3b-96d5bac9f725 | -4.79259 | -37.79323 | 2025-06-24 00:05:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 1b4fc44a-6170-37c5-b913-97caa63813db | -5.20618 | -43.30578 | 2025-06-24 00:05:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8b0d9e07-0120-3ab9-a5d2-bf9b98dbfdf3 | -4.53164 | -48.00556 | 2025-06-24 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7c88676c-d8b0-3b51-ab29-b2fced0718ee | -6.62923 | -44.13528 | 2025-06-24 00:05:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 318bd552-4c3a-3345-b24c-44cf0e0eed74 | -6.00158 | -43.74628 | 2025-06-24 00:05:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d171a8cc-5700-316a-928f-4da711f8125d | -5.98209 | -43.76229 | 2025-06-24 00:05:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a9caf94-25d7-3b73-947b-f062abb183ee | -5.77895 | -43.61751 | 2025-06-24 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e5558126-bbdf-3518-8dbc-5c28ccd71d38 | -5.48874 | -42.15147 | 2025-06-24 00:05:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 78a994f4-5dd7-3e2a-836b-47183ea2597c | -6.2504 | -44.8465 | 2025-06-24 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 941bd6bd-1fc2-3c8e-8db6-70c9de55f7db | -4.54624 | -48.00328 | 2025-06-24 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1992cf0b-281a-3188-bb8a-3955620db5e8 | -6.95649 | -42.80323 | 2025-06-24 00:05:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| aeba6d24-45f1-33e3-ab0e-186aee342602 | -5.75903 | -43.39116 | 2025-06-24 00:05:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9dc6ceca-7f6d-367d-b4c2-d00d1a1951da | -7.09464 | -44.36555 | 2025-06-24 00:05:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README2.md)
