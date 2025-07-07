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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da65ecab-95df-3057-aa19-448146769ca0 | -9.35552 | -58.83868 | 2025-07-07 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e14c412e-6886-3b2c-8fd3-c9ff15538c2b | -10.88858 | -56.45424 | 2025-07-07 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7b5679e-57f3-3a70-bef1-af75a5a882dc | -9.33507 | -58.84846 | 2025-07-07 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 875fd4e7-7f99-394e-a728-a0c169bee778 | -9.62981 | -61.45895 | 2025-07-07 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5db6edc-fd5b-31f6-ac89-d182bab833ae | -10.58207 | -49.12412 | 2025-07-07 05:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2e552d82-26f5-32c3-bb5f-09efcf8b619e | -10.37208 | -57.50709 | 2025-07-07 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 629423e3-202b-3509-ae8b-90f465974eda | -10.67287 | -56.54492 | 2025-07-07 05:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87ff2b46-3118-3962-8b0a-54f06c3e2773 | -11.32726 | -51.44627 | 2025-07-07 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb221d6f-7d6b-34bd-8ca7-32e053f9f8e1 | -11.32864 | -51.446 | 2025-07-07 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8976ae53-62de-3f04-beb8-d895ba11d7e9 | -9.35086 | -58.84599 | 2025-07-07 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e507c946-3d3d-3dc1-bdb0-0c59f9ddaefc | -10.12741 | -57.77852 | 2025-07-07 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26526bb5-1c01-300e-96a9-c7c004289d61 | -9.35959 | -58.83532 | 2025-07-07 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbb3734d-500e-3db6-bf5c-bc81eefbd33c | -10.04804 | -59.10666 | 2025-07-07 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6792fbc1-a365-3835-9749-abc6baec3712 | -10.28865 | -60.54297 | 2025-07-07 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc8936a7-c34c-3b67-9cf6-2e87a0d71c99 | -9.35378 | -58.85043 | 2025-07-07 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3235668-6c48-3ee3-863d-47080c6a48eb | -9.34737 | -58.84546 | 2025-07-07 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f223c9b9-34e3-3e5b-8acb-f97009627904 | -10.88862 | -56.45422 | 2025-07-07 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0977f49b-4e55-39bc-a49e-538d7f645860 | -10.57365 | -49.11276 | 2025-07-07 05:25:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6ad2e750-6ad1-3f3f-894c-95d1ee887ae7 | -10.67237 | -56.54853 | 2025-07-07 05:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b10f405f-0003-395a-9d05-147092ccb390 | -9.01544 | -59.5406 | 2025-07-07 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fb0f395-2f7d-3ae1-945d-94e4f79c4ab9 | -14.12434 | -51.29996 | 2025-07-07 05:27:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 38769a84-f68b-3c93-afd8-c925f7d2fcc1 | -17.16775 | -42.83174 | 2025-07-07 05:27:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 976f3170-92cf-3a41-8140-7e2b9dba672e | -6.1792 | -48.0494 | 2025-07-07 05:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2abeb826-8e0b-318c-b52e-41aebcbb6bc5 | -6.1606 | -48.0507 | 2025-07-07 05:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| bda71b92-bf37-31d6-9113-56ae9f3a2241 | -6.1792 | -48.0494 | 2025-07-07 05:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| dd882ea9-e3b6-33a4-b46a-bb9ac4847371 | -6.1792 | -48.0494 | 2025-07-07 05:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| cd37df9c-a822-36e7-b3e2-63b6c936a2a5 | -14.1324 | -51.3017 | 2025-07-07 06:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 3c3b48dd-e5d1-3127-aa53-4b98f88adf85 | -6.1792 | -48.0494 | 2025-07-07 06:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 181c7293-3a5e-3625-b433-c1b3606820c0 | -6.1606 | -48.0507 | 2025-07-07 06:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| edb9ebf7-03d7-3fc4-a838-ff29334d3186 | -6.1792 | -48.0494 | 2025-07-07 06:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| b8cc70fd-3440-3b36-ace3-14d2e5702efd | -14.1324 | -51.3017 | 2025-07-07 06:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 858ee702-cc11-38b4-b339-db5507e483e9 | -6.1792 | -48.0494 | 2025-07-07 06:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| cea98abe-750c-37e3-9364-cac316485cfa | -6.1792 | -48.0494 | 2025-07-07 06:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 24404513-0d42-34a3-95c5-d3fb5acaf82a | -14.054 | -46.2472 | 2025-07-07 08:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| d7caea9c-1ba5-3377-8cb0-1899cefccdcc | -14.0351 | -46.2275 | 2025-07-07 08:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b01a9123-7830-34d7-95d0-1a1f35e8a563 | -14.0346 | -46.2505 | 2025-07-07 08:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d435125e-face-3b27-9ae5-00bd4fa6a9de | -7.2796 | -44.6174 | 2025-07-07 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| b93b8ed9-640b-3db3-9cd6-7c3c6568e1e1 | -6.0052 | -44.5189 | 2025-07-07 11:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 7656b9b5-81a7-3313-860e-3f6ae135f954 | -7.2793 | -44.6404 | 2025-07-07 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 66fc3c40-9cd2-38a7-abb1-86adbec7027d | -6.0052 | -44.5189 | 2025-07-07 11:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| dc7f2f7b-3d19-36d6-9465-cff8c0a625e9 | -7.2793 | -44.6404 | 2025-07-07 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f27db6bb-a26f-3732-b5c5-39d665d9a248 | -7.2796 | -44.6174 | 2025-07-07 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d925e1dc-052c-3b32-be15-d41573544794 | -6.0052 | -44.5189 | 2025-07-07 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5a9e0d74-09e8-3907-800b-662760036c33 | -6.0052 | -44.5189 | 2025-07-07 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 6901bddd-0184-310e-91b6-d58626738e65 | -6.005 | -44.5418 | 2025-07-07 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| b7f7f1e9-a18c-3468-8268-8d90d11222a0 | -6.0052 | -44.5189 | 2025-07-07 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 05817cb6-8e3b-30db-97f0-7a25cf1a535b | -6.005 | -44.5418 | 2025-07-07 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 31f93358-c7b6-3e6d-a0db-78d21668ff5e | -9.7526 | -53.3038 | 2025-07-07 12:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| ee6e8afb-dbeb-3822-8d36-c52dd48e471d | -6.0052 | -44.5189 | 2025-07-07 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| b4a73c2a-e3a0-3e07-a2de-b90c0ddeb98e | -12.6636 | -45.2776 | 2025-07-07 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 90df13d5-ade8-34d0-bd05-6be43411c2a3 | -6.0052 | -44.5189 | 2025-07-07 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| cab4e55c-93b4-39d7-b685-f9e764b1bfe7 | -6.005 | -44.5418 | 2025-07-07 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 7f6ddb46-d726-3205-a271-dffd9e9db64e | -6.19823 | -45.1727 | 2025-07-07 12:46:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1b160bf4-cb5b-337f-bbbf-bd60cf78ef98 | -7.26812 | -44.62967 | 2025-07-07 12:46:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| c5bad8e6-b96c-3940-9a8a-acab85e0dc34 | -6.73266 | -45.71843 | 2025-07-07 12:46:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 12221f24-f43e-3719-bec4-8462a819656e | -6.19512 | -45.1974 | 2025-07-07 12:46:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| c31859fa-7927-3be6-90ac-645b0fb3091b | -6.0054 | -44.53011 | 2025-07-07 12:46:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 07ebe1dc-440d-3a62-8c13-347121068dc6 | -7.62856 | -45.36507 | 2025-07-07 12:46:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 4911f4d1-6eea-3764-9e25-3b3ba6f2c351 | -5.56254 | -45.21598 | 2025-07-07 12:46:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 488a6974-af11-383d-aca4-579a92995e27 | -5.60182 | -45.17821 | 2025-07-07 12:46:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 526b3b4c-eb02-3feb-bedf-aa5b1040fe4a | -4.59718 | -47.71571 | 2025-07-07 12:46:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 964c545d-0880-309c-ae87-7ccd996e75ae | -4.58589 | -47.71467 | 2025-07-07 12:46:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| b22f2a4e-01e0-3465-ad97-c3dba285338a | -6.16901 | -48.05885 | 2025-07-07 12:46:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 4645c27f-6e3f-3a35-adf6-400f0acb3585 | -6.1912 | -45.19141 | 2025-07-07 12:46:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| c9e7a53a-710a-3661-a655-da798b3de9b3 | -6.00811 | -44.50901 | 2025-07-07 12:46:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 4bf5dd6a-42cf-3e06-bac2-6c918931fa46 | -4.49559 | -47.53751 | 2025-07-07 12:46:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0db6838b-35b0-3937-945c-37f9264f9dd0 | -6.17064 | -48.04974 | 2025-07-07 12:46:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 96795c30-674d-30cd-9c5a-ba323cd685b1 | -6.0091 | -44.50227 | 2025-07-07 12:46:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 6a443216-96dc-33ad-9d16-e31b8a889ae8 | -6.00466 | -44.53661 | 2025-07-07 12:46:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| c908f4dc-9e1d-3a33-83c7-d98f72da86d2 | -6.16869 | -48.06474 | 2025-07-07 12:46:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 8233a468-0cf8-3fed-b89a-5a215dd874d9 | -9.75626 | -53.29121 | 2025-07-07 12:49:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 03a173e2-21c1-31d0-8c39-85820e475cea | -10.1889 | -49.49395 | 2025-07-07 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| c1f6e706-9042-381f-a1d9-410fa6e7e89f | -8.71027 | -50.00867 | 2025-07-07 12:49:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3b5e0d04-fbd7-375b-a35b-42552b40f0fd | -8.81946 | -44.56571 | 2025-07-07 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b36d0dfb-6f6d-33d9-8534-19f12e27d290 | -8.80814 | -44.55892 | 2025-07-07 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 41.6 |
| ea6a88d1-adec-3f0e-ba7b-29f90f25d08c | -12.67093 | -45.26985 | 2025-07-07 12:49:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| b1de6227-f60e-31e1-b45a-c8cceed560d6 | -11.26457 | -52.47252 | 2025-07-07 12:49:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 101f202b-d6c3-3b14-95a9-1cf6b8d05f9e | -8.06544 | -43.10781 | 2025-07-07 12:49:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.9 |
| a5babef4-eeaf-3ef1-86be-8c1007039d68 | -10.37789 | -49.90665 | 2025-07-07 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b2751a45-a220-3d6d-ac68-85166a6cf441 | -12.10861 | -54.58027 | 2025-07-07 12:49:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4e0625a2-5a1a-35cc-9938-8c923b0ad312 | -13.02556 | -46.3014 | 2025-07-07 12:49:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| c48b8a83-7baf-3412-a616-7ff3a71b39d6 | -10.79496 | -49.24419 | 2025-07-07 12:49:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d25ddbd3-3f59-3ab6-8d32-2830cdb6d589 | -13.40556 | -47.85319 | 2025-07-07 12:49:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 8ea63802-5ed3-36d0-b697-5e17a4e91d01 | -14.03165 | -46.23731 | 2025-07-07 12:49:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 467778bf-c6f1-3566-bf7a-1fbaf210ff94 | -12.10992 | -54.57127 | 2025-07-07 12:49:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0b49c457-628a-34a6-aa68-e582c5f67f1e | -9.75499 | -53.30012 | 2025-07-07 12:49:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| e90f3258-3cc1-3b73-abf8-617afea66dfe | -11.91897 | -54.41446 | 2025-07-07 12:49:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| da08d1cc-aead-33af-8680-dba1fbdc79e1 | -9.80294 | -53.23169 | 2025-07-07 12:49:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0abb8da2-1606-3aad-8633-e057098ef5ab | -11.28459 | -46.75303 | 2025-07-07 12:49:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7648f487-a51d-31ac-b896-07200d7284e8 | -13.41581 | -47.87612 | 2025-07-07 12:49:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| a8158c0f-6e9b-37b6-bfc0-d79d78db922f | -7.71358 | -50.78234 | 2025-07-07 12:49:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| e87412e3-3a85-32e2-8fb3-962e68fbeae0 | -10.37955 | -49.89402 | 2025-07-07 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b2472c78-debc-3b65-9b29-5ef0f465a734 | -10.79653 | -49.25014 | 2025-07-07 12:49:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8eb453f2-2b68-3f41-be47-3c7f28f7ba5e | -7.71502 | -50.77205 | 2025-07-07 12:49:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f02f216c-2105-35fa-a001-b083f8ba9297 | -12.58719 | -56.98091 | 2025-07-07 12:49:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a3aeb71a-9955-3d74-b356-b876c617c672 | -8.0626 | -43.10249 | 2025-07-07 12:49:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 565ca143-5623-3bb8-8c74-4ea82a7ecc3a | -7.63182 | -45.37115 | 2025-07-07 12:49:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1012751e-f85c-3612-91cb-d6bc6f452c95 | -11.29515 | -46.73665 | 2025-07-07 12:49:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| be07615a-e4c7-3008-9f71-eb6700d5a1ac | -10.18713 | -49.50728 | 2025-07-07 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 66d20226-cccb-30ab-9bb3-783f4c7e235d | -8.74699 | -46.49635 | 2025-07-07 12:49:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README13.md)
