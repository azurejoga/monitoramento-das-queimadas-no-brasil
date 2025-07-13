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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4da6d37-cc16-30a9-b8ad-cc51468c72a1 | -22.54027 | -48.81289 | 2025-07-13 04:23:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6a80bba-829c-30ee-8280-d99b4e745461 | -19.08807 | -56.04585 | 2025-07-13 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c7d674b5-0f3d-3c24-817f-1e820cbc9d8d | -17.98676 | -46.29071 | 2025-07-13 04:23:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f5ee0e6-d92c-3d75-9f31-a9a5a6f8c81d | -17.65426 | -50.48724 | 2025-07-13 04:23:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8677c859-ca85-3728-aef6-d0eb527055d0 | -19.08511 | -56.05276 | 2025-07-13 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 67580614-0da2-37af-a16b-6655f3d1770e | -18.45789 | -47.3701 | 2025-07-13 04:23:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d784d3b6-ccbf-3245-8016-37abaf24fc03 | -14.51708 | -59.15808 | 2025-07-13 04:23:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c02b61e-385a-3ade-9692-ebc582843cc5 | -22.74769 | -43.27183 | 2025-07-13 04:23:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 409ad4bb-bf87-3add-a7f5-c4990f513b52 | -19.88712 | -48.93509 | 2025-07-13 04:23:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 2de91b2e-285b-3942-9189-7f468a6bd10d | -17.69047 | -54.01121 | 2025-07-13 04:23:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8186f777-867d-3332-921a-a28c60384ad7 | -22.90892 | -43.48056 | 2025-07-13 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b1a37f6-0b41-35c9-b43b-3eafb2b48711 | -25.41454 | -49.15378 | 2025-07-13 04:25:00 | NOAA-21 | PINHAIS | PARANÁ | Brasil | 4119152 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec1d9ee3-5861-377e-9e80-6b55d7afcb4d | -25.19353 | -49.32905 | 2025-07-13 04:25:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1beb0fb7-6fa3-3b5d-98ad-76b75da24f5c | -13.8474 | -46.8964 | 2025-07-13 04:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 125bda90-659e-3d45-910d-3ce1aee23522 | -4.11785 | -54.91402 | 2025-07-13 04:46:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3972cdb-979c-38ab-9afb-88360a75fbe9 | -6.78789 | -43.96062 | 2025-07-13 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c82ff08a-d5fc-3993-a593-df7c5c3e1690 | -7.17956 | -43.00863 | 2025-07-13 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5cdddfbe-fb3f-385c-b36c-ae1bc044e07f | -6.87682 | -42.77952 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2a488926-e0a1-31e2-884d-96c7a7f70487 | -3.31587 | -48.714 | 2025-07-13 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cdb2b0c-ad49-3ba1-ad0a-bba6af960fad | -7.02246 | -43.29583 | 2025-07-13 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf186410-fd2d-3f26-a25e-71a14711d88c | -6.99559 | -44.10516 | 2025-07-13 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e452056d-7385-3381-a2e2-b55a7c9033c0 | -6.16057 | -45.89254 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a860d93c-688a-37fb-9291-7e335b524f4d | -4.77633 | -45.34872 | 2025-07-13 04:46:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41903957-942c-31f0-86a5-6d76a4da4925 | -6.7818 | -43.96976 | 2025-07-13 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36c99c42-4d0e-3471-ac70-95c26bea36e2 | -7.3375 | -44.0009 | 2025-07-13 04:46:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79c94b03-3709-33e7-8318-970abb91dffa | -6.95404 | -42.7302 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f0f25018-53b8-3c55-b1af-288d7ed3df75 | -3.40001 | -43.3657 | 2025-07-13 04:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3dda0a6-dbcb-3653-9668-374004566aca | -6.74302 | -44.69642 | 2025-07-13 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dad45ab3-897a-3e8c-968b-22ed0213abf6 | -5.72564 | -49.10817 | 2025-07-13 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a2803f8-786d-3c43-bd25-e4646fc58c84 | -3.5882 | -47.5263 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7ff995c-ff2d-3189-8469-0a8dc6178246 | -6.95317 | -42.73632 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 61025c73-7c33-3371-b238-806c8bccfb08 | -6.9536 | -42.73326 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 153b4f6d-2798-3f2c-8ca0-f2ad0f597705 | -6.42398 | -44.6428 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ad205c3-08d6-39b2-a2f8-17be900577c3 | -7.30844 | -45.30947 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 640bc261-6c6d-34dc-a463-a9930ac4c9a2 | -6.45058 | -45.35551 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 997811c6-6aa0-371c-a632-d62420a93332 | -6.49052 | -45.26065 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7bb147d-b8fa-3583-8d52-48b95b44588a | -7.32303 | -44.03465 | 2025-07-13 04:46:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b796d95-89e5-3aa7-ae2e-37a7b05e0a29 | -5.62875 | -44.26643 | 2025-07-13 04:46:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2aeb9a05-fe70-3eb4-81f6-0e03aebbba8c | -5.42613 | -49.08118 | 2025-07-13 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bae48859-4651-3c47-8154-cb61efa36995 | -3.78507 | -47.08846 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7428b095-f494-3b72-b430-6e963f89e71f | -6.79255 | -43.96143 | 2025-07-13 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a912febf-4718-3e42-9693-fbcd6ffb1212 | -2.9153 | -48.2391 | 2025-07-13 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0261a951-b8d8-3c2d-a837-ebeb7155790f | -7.31042 | -45.32612 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72ac9604-e543-3fb1-a749-7c7ad21cb879 | -4.45084 | -49.001 | 2025-07-13 04:46:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aae23549-bb37-3dd2-ae36-f8d4d218d620 | -7.28957 | -45.3189 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cda4192a-b595-37d5-9453-945164f62428 | -5.32498 | -55.94539 | 2025-07-13 04:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f0e5b7c-2507-31c9-86b7-a288b5597751 | -7.0944 | -44.06718 | 2025-07-13 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f5fd436-a8c5-365c-aabf-cd8a8b00ffd0 | -6.43967 | -45.40068 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5672751b-cc55-328b-8ac8-c1127313e54b | -6.45425 | -45.35993 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ba70ac3-a142-3f4c-97d3-a929cdcabbfb | -4.27962 | -48.19007 | 2025-07-13 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf49655f-4c45-3766-9728-621576784b15 | -7.11088 | -43.61084 | 2025-07-13 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb541e2e-6b51-3e21-a996-41c696e1e8f9 | -6.11959 | -45.86071 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4221517-73cd-3fc2-a5ea-c4caa8bdac6b | -7.311 | -45.32213 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f56df45-0b5e-34a2-963a-7f56a0b852b0 | -3.75613 | -47.1076 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 778640f6-d592-36a7-a4e1-86bb59ee999a | -7.29613 | -45.30356 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| deacca5b-d587-33d8-b971-5cf9d0f58cef | -7.28213 | -45.30963 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9bae18c-f8f5-304d-b659-f0b97725916c | -7.28928 | -44.62561 | 2025-07-13 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8238b692-7e04-3fd6-b5a3-0e33c1ab06fd | -3.62499 | -47.5484 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b546aeef-548f-3087-99b3-b2e5ad74ce71 | -7.29014 | -45.3149 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 846ec770-4afd-33d6-aa4e-cdb78ed0665f | -7.29556 | -45.30758 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 436b99e1-711b-35eb-9250-7aa275051b88 | -3.58612 | -47.52743 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc89d089-fa7a-3e68-8b1c-1569aa8311e5 | -6.44498 | -45.39378 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1ce15d4-752a-35a2-b1c3-fb622b4b21e9 | -3.78873 | -47.089 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bfceddf-d2fd-3cd2-b364-49edf5912a3c | -3.61428 | -47.54683 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b770e29a-8194-3128-93ff-b223b122047a | -4.27382 | -48.18131 | 2025-07-13 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 466d93db-5802-3d5b-a61f-6d5608f0f6a0 | -7.69341 | -44.34253 | 2025-07-13 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02e96e08-ca54-3018-9780-fd723111511d | -4.29342 | -48.05356 | 2025-07-13 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daa18725-869b-3592-a0a9-128e19ea6e5a | -6.65619 | -43.10845 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2ed24a5-c268-3650-9747-364dc8268914 | -6.45739 | -45.36796 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f94d4f8f-304f-303c-a86a-5e0d52d6275e | -6.44135 | -45.38922 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 482b7525-a39a-3be5-822c-35bc0c3ec373 | -3.81874 | -49.29007 | 2025-07-13 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9c4468f-c2a9-3a88-9423-0df19253a57b | -7.10931 | -40.39001 | 2025-07-13 04:46:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0f1ecb3d-02fa-3ec4-b920-e5ac1cf153fd | -2.91186 | -48.23856 | 2025-07-13 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4700aff9-2bc9-371f-ab18-7cca649eb3e5 | -6.87059 | -42.77013 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ffb2d4d-761b-3b8c-8472-398a4fae9b86 | -3.98041 | -48.4142 | 2025-07-13 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2674b8d6-ca77-36ec-88d6-806c60c9f5d0 | -6.94764 | -42.73864 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| de675a58-a43b-3c2a-8906-e1f364465297 | -6.10944 | -45.87347 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe660087-d604-3cbe-9152-92bede4e6ef2 | -3.3993 | -43.37046 | 2025-07-13 04:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08f367f6-493e-313e-a93a-c06f4b944a9f | -5.26716 | -44.86765 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c5a3192a-642b-3bae-8117-aa651533cb61 | -5.8461 | -46.94261 | 2025-07-13 04:46:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72b433f3-e336-31ce-b7a4-4983f051df26 | -3.62142 | -47.54787 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a54de00-4cb1-39bc-8d38-541f76c455f0 | -7.30101 | -45.30015 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 099a3d91-4a9f-3697-90d3-4f80a3aa25be | -5.748 | -44.98259 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72d8f14d-0d3c-3f24-abc1-3a7454457e1e | -6.16097 | -45.91779 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e90b509-0274-3200-85ac-084407bce3d6 | -7.30985 | -45.33012 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a548b31-5e9b-3223-88eb-c36466c840e8 | -6.83255 | -42.87218 | 2025-07-13 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2fd1435-d56c-3975-ae62-37324c2c4692 | -5.73397 | -44.98867 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1adaa200-e883-3691-84bc-faa6c7c994e1 | -6.63826 | -39.32402 | 2025-07-13 04:46:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8446ff4c-1ba4-335a-b9ef-eb4dba59e083 | -5.03058 | -47.97167 | 2025-07-13 04:46:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaa08e13-dec7-36c0-9f4b-1aa8abab7a10 | -6.82751 | -42.8714 | 2025-07-13 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e5b26a12-704a-3945-8f6a-1ee7854fd94b | -6.44023 | -45.39686 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c22125b-9fa3-3334-8d7b-45e684c4400c | -3.66429 | -48.31692 | 2025-07-13 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f873834-1bc7-35a8-bb89-54e192e9de5f | -6.62241 | -43.02373 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd679ee4-0202-30db-a2ce-75f66e52302b | -6.44387 | -45.40136 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8120af4-7706-3758-b19c-7fedd58cb528 | -6.95274 | -42.73936 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a60bc69b-c652-38cb-8a23-bfff3eb935ec | -4.27672 | -48.18569 | 2025-07-13 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e720c78-b3dc-399a-966a-ea6a80b5e285 | -6.74744 | -44.69719 | 2025-07-13 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 440c5a65-532b-3daf-bf2d-46e6baf72a3b | -6.46159 | -45.36866 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1afc9cda-89eb-3083-8c25-43a2e9d77177 | -7.28156 | -45.31365 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f29fe561-0e65-3966-b0c8-58122925b0b8 | -4.85902 | -43.22557 | 2025-07-13 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README10.md)
