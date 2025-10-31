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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c45a4b01-278e-31c9-a8be-b17527c8e863 | -18.2867 | -54.2933 | 2025-10-31 04:59:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 454d279e-3d91-3298-8f6f-9d9a11b68d3c | -16.76492 | -53.83741 | 2025-10-31 04:59:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8d025c0-05e0-3050-9f36-0025369c98a9 | -13.25191 | -54.35713 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 95edf10b-5b97-3961-ba36-91ca07a531c6 | -16.37316 | -45.24704 | 2025-10-31 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6758cb0f-2038-34e2-8be6-44f919fd2cf8 | -16.22674 | -52.45559 | 2025-10-31 04:59:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f2a315d-328b-36f1-9247-2b65a161676b | -14.4581 | -55.83855 | 2025-10-31 04:59:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1192f321-c910-30e1-8edc-c921e96082c8 | -13.2279 | -54.35704 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec8fd8f2-28ac-32bc-b00e-1f797fc68f31 | -16.37522 | -45.25328 | 2025-10-31 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7fc5fd80-fe7b-38ed-9834-afb77c9c7f8f | -13.23291 | -54.34664 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f2a54173-a5c9-34d4-bf8f-c23920880fe2 | -18.29132 | -54.28578 | 2025-10-31 04:59:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8a60d15-3cea-3848-b0cf-8f3f2afb7f55 | -17.12924 | -55.73668 | 2025-10-31 04:59:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 627a88f0-56f4-372d-bfe6-0d43a0ac3637 | -18.34068 | -52.40678 | 2025-10-31 04:59:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78cef39c-badd-3bc5-8629-04e747d6df8a | -15.85232 | -44.90167 | 2025-10-31 04:59:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b21e52d5-63d2-3607-bb96-8ac1cfd57995 | -14.74839 | -46.58267 | 2025-10-31 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c00daaf3-076b-31ed-a61f-c99cc72e8f96 | -13.2346 | -54.3581 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b9d7185-e9b0-3052-9744-4374e05df92e | -13.24131 | -54.35916 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f689fca1-4fd8-38b2-bef4-be10f645e39c | -13.34448 | -54.28181 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7f537f4-c11a-3129-9a57-ec1a3c858eb8 | -13.22598 | -53.87828 | 2025-10-31 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1d3f30f-74e6-30a3-83fd-a7fdf08f497e | -13.23346 | -54.34299 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d25c250f-b7ac-3415-b203-bd045e5e23e1 | -13.22845 | -54.3534 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e6a9a956-4df6-3393-8154-95f19d8aadee | -16.36975 | -45.24805 | 2025-10-31 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f637e8b-2987-304e-a788-5b00be7211ad | -13.22315 | -53.87401 | 2025-10-31 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6dbc8201-c0a0-307e-aebb-55d280c8d779 | -13.24801 | -54.36023 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82423b84-490e-3f50-8038-5b9d77f4a768 | -15.01073 | -46.3164 | 2025-10-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a39d5a3-0a3d-3b4e-ad7b-32d0d78ceaa2 | -12.14073 | -64.28129 | 2025-10-31 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 361ad5f5-bfc7-3d00-8e1c-4e596023c5b3 | -18.01613 | -53.62359 | 2025-10-31 04:59:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60a49831-203b-3254-9d92-b97b03d88e41 | -14.61253 | -56.22008 | 2025-10-31 04:59:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a13db4e-559b-313e-851c-4d835881cf3d | -13.23236 | -54.35029 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 707af732-2d50-31f8-9248-d2070018789b | -17.9603 | -52.68464 | 2025-10-31 04:59:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2988276-39c5-3c86-bcf3-7c9eeb20b461 | -13.2251 | -54.35287 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 886d6c2a-2767-381e-bdb4-a4f4e3a23980 | -13.23626 | -54.34717 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 152396ec-3761-32b6-8dd4-2c43ffc2e3b1 | -13.23792 | -54.33623 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b92975c0-3184-38f7-89f5-173562bc330b | -13.22901 | -54.34976 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 721fe67f-50a7-39d6-be68-b2a037556746 | -16.769 | -53.83393 | 2025-10-31 04:59:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33a23f99-d2f0-3477-850e-b73f92c75363 | -15.85282 | -44.89697 | 2025-10-31 04:59:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2c49701-2c13-3b18-b9db-08e4986e4293 | -13.23961 | -54.3477 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9409027-eb10-3431-94bb-775f456e79da | -16.3757 | -45.24879 | 2025-10-31 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82ac5ad8-d6f7-3d6f-a743-a37f28294748 | -12.14133 | -64.27816 | 2025-10-31 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c625fd73-0654-3549-b1a8-8cde92ac4d63 | -13.24296 | -54.34824 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e33aa72d-56b6-3744-81e0-66eae0d46bc7 | -16.37271 | -45.25154 | 2025-10-31 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0cbf64dc-994a-34a1-9841-4727f3f766ca | -17.12536 | -55.73977 | 2025-10-31 04:59:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f226b4ab-7c97-3146-8f3a-4181001b6742 | -15.00408 | -46.31645 | 2025-10-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 852f75a6-fa02-3355-b3eb-6d38855518e2 | -13.23682 | -54.34352 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1fd751c-30f2-3ea4-a2c6-4e1184220b3f | -16.3672 | -45.24628 | 2025-10-31 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08dc4441-78d5-3d13-92ee-e143e67f0c4c | -16.30062 | -45.09663 | 2025-10-31 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7e3214b-89c4-36a4-8e54-8dd297b17cb0 | -12.259 | -60.54856 | 2025-10-31 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13579a97-42d5-3fbd-9528-cd9522e2355f | -13.22565 | -54.34923 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef1d8f06-ef62-3a13-9c15-2694899bdd9e | -13.24186 | -54.35552 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 9d0d25eb-7ffe-3246-8f94-6096816b098f | -13.23011 | -54.34247 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fb3efb2b-5433-39b5-87fd-3ee24a1c3268 | -13.24576 | -54.35242 | 2025-10-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| a1369468-618d-3ade-86c8-1d7d9336f34e | -10.5483 | -44.7773 | 2025-10-31 05:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 2c0a31dc-b5d9-3e67-a44e-06a73976de7e | -7.3136 | -44.9343 | 2025-10-31 05:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 8cb59855-58f1-3159-898c-3d1870d1a43f | -12.2878 | -48.0454 | 2025-10-31 05:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 85b4f11b-b3a4-3583-84e5-edb0dc34c6a5 | -7.3324 | -44.9326 | 2025-10-31 05:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 568d48d4-a117-312a-a8d3-d96d0cd27f91 | -3.017 | -49.4482 | 2025-10-31 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ebf1d989-5abd-3453-a97a-7e4ebce0496f | -7.3134 | -44.9572 | 2025-10-31 05:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e19cc096-9d49-3d73-bce2-66a01cedf8c3 | -19.65996 | -53.56027 | 2025-10-31 05:01:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76b1693e-12af-3b9b-9126-2e237327dc9b | -19.66362 | -53.5608 | 2025-10-31 05:01:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c535875a-94b4-3655-b980-2ecbb9fced06 | -19.81566 | -54.73941 | 2025-10-31 05:01:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edd2f975-f264-3787-bc78-b2d1b9bb066b | -19.66424 | -53.55632 | 2025-10-31 05:01:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48b0bf75-e970-3dc9-886b-d26e441d0cfc | -7.6491 | -43.5876 | 2025-10-31 05:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| bb562ae7-a852-3cdf-a3f9-4286d3af049c | -7.3136 | -44.9343 | 2025-10-31 05:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 79324295-b5c0-34c1-b6ff-de7069dbc13f | -9.8631 | -44.8425 | 2025-10-31 05:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 3741d801-d2b0-309d-b5e0-a0b66b00e1d5 | -12.2878 | -48.0454 | 2025-10-31 05:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 9305fb6a-f84e-3264-8ff3-1abacf12b0e2 | -7.6488 | -43.6109 | 2025-10-31 05:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 44ad0fe2-b286-359d-9e70-d919e16d05cf | -4.8409 | -42.7465 | 2025-10-31 05:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 63764333-a49e-34c9-8f0f-a7b06e681c5c | -12.307 | -48.0428 | 2025-10-31 05:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d0b4be49-ab6d-32c9-a244-7752c967c5fe | -7.3324 | -44.9326 | 2025-10-31 05:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6acfbc49-4a5b-353a-8f0a-376cb06cfe99 | -3.017 | -49.4482 | 2025-10-31 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| e1b82ac5-508b-38c5-8b4c-22139a05f5df | -13.2401 | -54.351 | 2025-10-31 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 18b6758a-d842-3f64-bab5-18fe187cb6f8 | -12.2882 | -48.0232 | 2025-10-31 05:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 47d25eb8-a873-3ab7-b873-49b060f73078 | -13.2398 | -54.3716 | 2025-10-31 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 8b2c8d0f-da83-3553-a95f-759162522e64 | -4.8411 | -42.7229 | 2025-10-31 05:10:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a1b01978-3b83-37a7-a7ac-648028b0eb3c | -7.3322 | -44.9554 | 2025-10-31 05:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5bca6128-d908-3952-9532-bf2185bd2eb8 | -13.2209 | -54.353 | 2025-10-31 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 55bd87d3-9188-3727-b2dd-d48e06920aaf | -7.3134 | -44.9572 | 2025-10-31 05:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 897baaeb-34b7-3594-a03f-103e804f914e | -7.668 | -43.5857 | 2025-10-31 05:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 650d4b45-5207-3f5c-9a0f-73b68d4e44d3 | -3.3024 | -51.9254 | 2025-10-31 05:20:00 | GOES-19 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| e86f640e-9823-37f7-829f-29f0969c4eff | -4.8411 | -42.7229 | 2025-10-31 05:20:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2bae04b9-263a-309c-bbf5-3d32d3ecfcf2 | -11.5782 | -47.0717 | 2025-10-31 05:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 04b92e64-0276-361f-8598-902722317c7e | -7.3136 | -44.9343 | 2025-10-31 05:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6946682d-cb31-39ab-a2c3-3ae6d7fa0d6c | -11.5587 | -47.0966 | 2025-10-31 05:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 375a0ee1-7a75-351b-81a5-db13860059c8 | -11.559 | -47.0742 | 2025-10-31 05:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 0868e4d7-7b1b-3cf5-a363-cb4ebcb2f7a4 | -4.82 | -43.0294 | 2025-10-31 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7e7a2cf3-1aa7-32bc-8d83-26db6d943a3b | -4.8015 | -43.0072 | 2025-10-31 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 9c07cd5b-5b8f-331a-9f60-4da55ed95128 | -11.5399 | -47.0767 | 2025-10-31 05:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b7d4166e-496a-367e-b2fe-e77d652d7aec | -4.8409 | -42.7465 | 2025-10-31 05:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 6657e377-7b54-32a9-93d6-6d57e92d1006 | -3.017 | -49.4482 | 2025-10-31 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 11c8621a-7cb4-3177-83d7-c0a3a6db08e5 | -11.5594 | -47.0518 | 2025-10-31 05:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c31bb096-efbd-3c94-b951-026e9c65032d | -4.8013 | -43.0306 | 2025-10-31 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| acc8b1fd-ad12-3718-8bdd-e2ea59ec139f | -7.3134 | -44.9572 | 2025-10-31 05:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| d144a6ce-5880-3d43-9edf-444ceac0ac1a | -4.8202 | -43.006 | 2025-10-31 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e2fc4348-6986-3bd7-9d8e-7ea01a3a36ed | 2.07742 | -50.90295 | 2025-10-31 05:23:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c19dde2b-de63-323c-aa75-4d6359f9a07f | 1.10568 | -52.41892 | 2025-10-31 05:23:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c70bbed0-3bc5-3501-8314-4bd895a84e6e | 1.14533 | -59.52909 | 2025-10-31 05:23:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a327c27-9094-3b28-a6c4-86c9b7a0d805 | 1.28279 | -60.43894 | 2025-10-31 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9afc8e37-2e1e-33fb-a977-e6aa235b48f2 | 3.22066 | -61.19772 | 2025-10-31 05:23:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51891467-36c7-369f-a29c-fad932a99067 | 2.4389 | -51.40368 | 2025-10-31 05:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e621a88b-95a2-3d05-bced-b2eaf90ab3b8 | 1.29708 | -60.41803 | 2025-10-31 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc77b5c7-14fd-3079-934f-940c41705f51 | 2.4436 | -51.40302 | 2025-10-31 05:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README41.md)
