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
| 274795c7-02bd-3b54-8100-340bf0bf3838 | -11.90497 | -54.78532 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e230429-65fa-341a-9f02-90ae93046f89 | -3.40346 | -47.58413 | 2025-06-03 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd1fbc8e-b5b9-3377-8074-c9be5dcd0cb6 | -12.33522 | -46.30258 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 550b45eb-88d3-30ab-92d2-b5c4aa6e6142 | -9.17138 | -45.32474 | 2025-06-03 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63ef8ad4-ef54-3735-a0c7-00a22f79574d | -11.57835 | -47.44423 | 2025-06-03 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81735d11-8e7f-3247-b836-83130f6bc56a | -7.90474 | -50.36877 | 2025-06-03 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ae78095-d7cd-3aab-b403-7a73c1f5f6d5 | -12.37122 | -47.32299 | 2025-06-03 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 126a2183-eb50-37b5-8357-4ca68d1934a0 | -12.08057 | -54.58345 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f5e3ea-eeb3-390a-a10e-b7debfe18050 | -12.32585 | -46.29743 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 587ef5d2-23bb-36e9-9fec-ff779da92e36 | -3.04228 | -49.43407 | 2025-06-03 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8b4ae3b-428b-36ff-a8b7-00649eccd070 | -9.87484 | -49.33989 | 2025-06-03 04:19:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08a22b4d-b8b9-31fa-8894-e05b5e22188e | -12.08116 | -54.58036 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a59c567-801e-344e-af81-301a495f613c | -9.60627 | -49.02273 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f821806e-f9cd-3a8b-b088-b256c094079f | -8.90742 | -50.04952 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 792e3cdc-d813-34c0-a210-21ccbf6eaad1 | -9.5627 | -50.51598 | 2025-06-03 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd351640-e053-328b-8e9b-77f59c00a116 | -14.019 | -55.13732 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96223382-ef8f-3b62-b578-d348d9ff9ad5 | -9.17304 | -45.33571 | 2025-06-03 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa7b6a66-14d6-32a0-895d-bb0cedbce8a5 | -8.56396 | -48.86811 | 2025-06-03 04:19:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ec2affe-198a-3e8d-9b58-cfef90b056d3 | -13.36662 | -54.26248 | 2025-06-03 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aac2ea0a-4709-3827-a9cc-bd54b763d0fb | -11.55009 | -56.4333 | 2025-06-03 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ee6d55b-bf0b-3f04-9bc9-2ad37ade39c0 | -11.55169 | -56.42511 | 2025-06-03 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2fbd04a-bbf0-3e6d-a871-c1ff0c5e28f9 | -10.23728 | -52.22157 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3e0ba58-0a4a-3f81-9d48-472e14577bb8 | -9.39729 | -48.437 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a31694e-a876-3f71-82e7-e88bbe6a553f | -10.13628 | -52.1385 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92d654e6-1586-321b-8aa8-4d7874f00c40 | -13.08727 | -45.2708 | 2025-06-03 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c9cc8c7-4979-3844-8593-7757cf887081 | -11.92083 | -54.81487 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23878a9e-7ea8-3ed8-bc16-bf1349e7103d | -8.96761 | -47.96773 | 2025-06-03 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2aac8b6-5dd1-3c24-acf7-e3f7eb941794 | -12.36764 | -54.16485 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd8dd2d4-672f-3b7d-a3fb-95223332caf6 | -15.69786 | -43.42578 | 2025-06-03 04:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a58efe3-f5ab-39c3-9f1e-5b9e8848b644 | -10.94503 | -48.22271 | 2025-06-03 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58e00abb-a529-35de-9671-1d600b0437c3 | -11.25151 | -49.49236 | 2025-06-03 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aed0becf-f62a-31be-85bb-061c1c63b794 | -10.13705 | -52.13408 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9fd4696d-1a2d-340c-b62a-c0f1cf445de8 | -8.47742 | -46.49742 | 2025-06-03 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16561e51-65fd-3b96-9686-8ccd6e7098e3 | -9.87561 | -49.33536 | 2025-06-03 04:19:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17d6e3c6-47bf-3db9-8294-9b574be3a5b2 | -14.0169 | -55.12134 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ec3397ea-2a50-3430-a6d5-baf04a2ea366 | -9.39578 | -48.42392 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16894653-08e3-38b6-be9d-1ec7acc938e3 | -9.16476 | -45.32368 | 2025-06-03 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 79d228b9-2362-3547-a8b0-b7a913603e8a | -11.90162 | -47.44042 | 2025-06-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9adfb9e-56c2-343d-b539-b650335870ac | -11.24704 | -49.49617 | 2025-06-03 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c10058af-2db4-36b8-b109-529577f818fb | -11.25367 | -49.50197 | 2025-06-03 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a439a232-d57a-38ef-b1f1-04d81bef22ad | -9.33793 | -48.95012 | 2025-06-03 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef2c68a8-155a-3242-8db9-e31279890621 | -12.10099 | -54.66942 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb5f6779-bd82-348a-b379-7f4f6ffcef3a | -11.55663 | -56.43042 | 2025-06-03 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dda34ce-4499-322e-8285-5f6f0e2f1422 | -9.37853 | -48.41678 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ab0bb0d-ca6a-3e77-89ca-4d42df9ae067 | -9.40089 | -48.4376 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac84c98d-e1f3-38e4-a224-b99fe612b60f | -3.03518 | -49.42515 | 2025-06-03 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 95e28b07-1cd7-3fc2-a8d3-dc20569f9c98 | -14.0184 | -55.12321 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a593fe77-79d3-3051-acd7-3e2f61370487 | -13.41891 | -43.74917 | 2025-06-03 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 269240cc-b0b6-3ed5-b3a4-6e230b913377 | -8.91474 | -48.90341 | 2025-06-03 04:19:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 277998a9-395a-3c4d-91c2-7377c9c6b70c | -10.47152 | -47.94852 | 2025-06-03 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0367b6d3-08a6-3a2e-9ce3-1eb0008f8cfd | -13.14587 | -56.80493 | 2025-06-03 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e48ee5a9-3713-315a-8fd3-1a79431dc16b | -14.01631 | -55.12431 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f05d1873-322e-3b29-82f0-d89444fccecd | -7.90064 | -50.36806 | 2025-06-03 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94e2ae72-6509-3b2e-a78e-febff4667284 | -10.24585 | -47.59421 | 2025-06-03 04:19:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9376560f-f11b-35cb-b1b7-fe6e255b1408 | -12.09531 | -54.67151 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 632dcc2d-118d-3d51-8448-35ccf040e7ca | -10.69277 | -57.65082 | 2025-06-03 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 12786fbf-2d85-3d5a-adf4-fae7700fe2bf | -13.14505 | -56.80893 | 2025-06-03 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b04750b3-a598-35dc-958e-b6c777beb7d0 | -8.72062 | -50.2632 | 2025-06-03 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 830881f1-ad67-35bf-9056-7998256fbd34 | -12.37107 | -54.16438 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8f22f862-1c74-3f37-a437-e764bfe917fd | -9.16807 | -45.32421 | 2025-06-03 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ffcd4c43-db7d-339d-a112-5e49895b5f61 | -8.63271 | -47.13669 | 2025-06-03 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c13e0c1-780a-335c-af12-163ea08cec42 | -12.36657 | -54.17041 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0f48c85-331d-305b-8e12-776a5a2d3ba1 | -12.23064 | -54.31365 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48f40007-eadc-3497-b573-f975f2d7908e | -13.63572 | -52.18568 | 2025-06-03 04:19:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1afda9f6-beda-3a24-95ec-8d2ef8d9fab3 | -15.39831 | -44.25876 | 2025-06-03 04:19:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0bc5700f-959a-34f5-84a8-b359c663dfda | -9.38432 | -48.42628 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68efc202-1146-3c1e-aad1-89e063a603a7 | -3.40614 | -47.58315 | 2025-06-03 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dd275a8-e7ba-3433-98d3-d37b1e85c807 | -14.02739 | -55.13122 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27296b9d-c55e-3e12-8bb6-e3cce5edecfd | -10.2328 | -52.22079 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2272fe4-0fda-39a5-8e78-d3e58f57657f | -11.89925 | -54.78742 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4253224-ebd2-39f8-9067-7e6fc8fff6a5 | -12.37867 | -45.92006 | 2025-06-03 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 365f89e5-3c79-3a0f-9a37-17858b1e7ad4 | -8.96696 | -47.97173 | 2025-06-03 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1957b616-7e49-3654-91c8-92a1580c43c4 | -11.54456 | -47.31015 | 2025-06-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0173215-651f-3411-a8e8-05a7090df67f | -9.19382 | -49.69157 | 2025-06-03 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 70599b63-dd13-377a-a7b7-6f0b223c0f08 | -12.45593 | -54.91356 | 2025-06-03 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4600bfe-31af-3893-a313-e70e4e2a33b8 | -9.02985 | -46.59399 | 2025-06-03 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1a7b5df-1d0d-3fc6-8567-cd809da796f0 | -9.39799 | -48.43284 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7458abd0-fa4d-36f8-90b1-88d5fb1e2eed | -12.16365 | -55.16196 | 2025-06-03 04:19:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a438d6fd-31a6-3db1-94be-2bf2498b8cb4 | -11.90778 | -47.44524 | 2025-06-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3147049e-0073-3587-a29f-6ee11c9b4bd9 | -14.03419 | -55.1404 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c18c88c3-e1dc-3869-9caf-e53f4388d5c4 | -10.67169 | -44.38536 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 187ada76-02e7-316b-9096-33f537267c2c | -10.23808 | -52.21713 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9de39e4b-0b27-3846-9de2-8ad1c2ca7660 | -10.0007 | -48.48926 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 384a2d0f-4483-37da-9e9f-b896a2073b16 | -11.55743 | -56.42632 | 2025-06-03 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 274c00da-e8cd-3b14-a9f5-a03d0c426e3d | -9.40434 | -48.41685 | 2025-06-03 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24ad00ec-8c75-38b7-93d2-f1f9eeacb9e2 | -14.03151 | -55.12732 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3317c48-782a-3c40-a2ce-1ca56958c7e6 | -10.23647 | -52.22601 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 869e161a-e01f-3d91-9fe4-9bf71395648f | -11.92076 | -54.82292 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1189c18d-0955-3ddd-8130-f2ce324ddf05 | -14.02466 | -55.13531 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc65543b-ff76-3c14-95da-61b560e95748 | -12.66243 | -58.22038 | 2025-06-03 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a910dcf-ae6d-3b20-949f-736fb9e3e5b0 | -11.89806 | -54.79377 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6318a31a-cc19-3e97-b11b-5c8713a2cd0c | -10.71176 | -48.46915 | 2025-06-03 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6987884e-bbf4-3597-86fe-ce0c278698b4 | -11.91562 | -54.82187 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c42fd077-566b-3a88-b3bf-aed4bb69e627 | -14.01276 | -55.12516 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e93f4dd-365e-365a-9841-c5dd821974b7 | -12.36516 | -54.16893 | 2025-06-03 04:19:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cdad45f-d095-36a1-b95f-8e35ea24e487 | -14.02407 | -55.13832 | 2025-06-03 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 503b68b4-b9dd-3685-8343-348cf765f54c | -11.89983 | -54.78429 | 2025-06-03 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d5e0bac2-4f78-36d0-b5f8-46471e2ef4ef | -10.6097 | -44.76697 | 2025-06-03 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1acccbfa-a547-3af2-9147-bfd02fe91379 | -11.90381 | -47.44835 | 2025-06-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a45a33d6-8027-39cb-b5ab-f3daa8cfb419 | -13.7184 | -58.67527 | 2025-06-03 04:19:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README10.md)
