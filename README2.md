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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5a20185-f092-3877-8bb6-f2796aa6b33d | -5.0399 | -43.6205 | 2025-11-03 01:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| a0e3f217-c517-315f-929c-a23fd013264c | -3.4937 | -50.298 | 2025-11-03 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b8929c1b-19b9-3ca8-bb11-e78867dce55b | -12.6625 | -50.8478 | 2025-11-03 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 485dd8d8-ddc3-30bc-a84d-3ed404f6b0a4 | -5.0399 | -43.6205 | 2025-11-03 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 3e1d4f4a-5039-31cf-b8e5-f0b809a6cc8e | -10.1033 | -36.3101 | 2025-11-03 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| d4f96c38-7425-350a-bc33-e43dfacbe3fb | -5.0212 | -43.6218 | 2025-11-03 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f9b44ba0-08b0-35bd-8385-99098d4418b3 | -5.0399 | -43.6205 | 2025-11-03 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 2066b49e-307a-3057-a363-2b2709a8eee8 | -5.0212 | -43.6218 | 2025-11-03 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ce59a24a-0c3e-32e2-a269-b8a502b10064 | -5.0399 | -43.6205 | 2025-11-03 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 2a77149a-40a6-3292-90c9-7e7bd357e401 | -5.0212 | -43.6218 | 2025-11-03 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0de8d635-4280-3544-a9d4-5e7634fc1d5b | 3.2922 | -60.686 | 2025-11-03 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4e377cb1-1ea2-3927-a4b7-5b8cec484572 | -5.0212 | -43.6218 | 2025-11-03 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 4b584c63-5859-3cfb-9cc5-a54459c147cf | -5.0399 | -43.6205 | 2025-11-03 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 837198f1-1b73-3196-99ea-68eed86e6fb5 | -3.4936 | -50.319 | 2025-11-03 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 7c7efe0f-dd9a-3d0c-97ee-672d98f941c6 | -3.4937 | -50.298 | 2025-11-03 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5ab18690-c75a-353e-9bd3-d10b439fa9bb | -5.0399 | -43.6205 | 2025-11-03 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 95ae8988-8bb7-3d7b-931a-f03904b45958 | -9.5343 | -40.3282 | 2025-11-03 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 9a8c852e-4d15-3e84-9d71-efdb92776481 | -9.553 | -40.3503 | 2025-11-03 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 175.4 |
| 0c02de92-c9ce-3c2d-922d-8843ae13f2e1 | -9.5534 | -40.3254 | 2025-11-03 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 207.1 |
| 5a86598c-8bb1-3eb9-bb6c-b65fde75db8a | -9.5339 | -40.3531 | 2025-11-03 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 0b4d527f-33a8-329a-b92f-2525dc047e37 | -5.0399 | -43.6205 | 2025-11-03 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| de236136-dfe8-3041-8b3f-0fd92bc05d48 | -5.0399 | -43.6205 | 2025-11-03 02:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 03d311ad-41e8-3e77-aa86-9daa48ecbe08 | -9.5534 | -40.3254 | 2025-11-03 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 194.8 |
| 7dc7dad3-abf7-3a97-92fa-8f233bdc36fb | -3.4936 | -50.319 | 2025-11-03 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| cce81089-12d0-3d42-934d-1970396b0ec9 | -9.553 | -40.3503 | 2025-11-03 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 125.2 |
| e46b86c5-21ed-342a-8908-4af54d3c6573 | -9.5343 | -40.3282 | 2025-11-03 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 99388d57-63b3-3e9a-b96e-48d540919a6e | -5.0399 | -43.6205 | 2025-11-03 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 497627e8-976d-3898-9990-aa711dc0584f | -9.553 | -40.3503 | 2025-11-03 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 129.7 |
| e8160335-c1bf-38e2-b2d3-cb72500bb4bc | -3.4936 | -50.319 | 2025-11-03 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| b6caaa78-97d4-3694-8c78-3cd24ae6eb71 | -9.5343 | -40.3282 | 2025-11-03 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 7cd43523-2ff4-3105-b0e4-d674464d950a | -9.5534 | -40.3254 | 2025-11-03 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 226.3 |
| 03f542cd-21d4-3cd2-8e36-a26026a38d96 | -5.0212 | -43.6218 | 2025-11-03 03:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d4575cd1-eb1d-3fef-80a7-07f3a5720bf5 | -3.4936 | -50.319 | 2025-11-03 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| bb61cf94-8be8-34dc-87c9-4e0059a770e6 | -5.0399 | -43.6205 | 2025-11-03 03:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| bc4c5468-6207-36b2-9793-9f6e2f2294e8 | -9.54458 | -40.33841 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 016019b8-dcd9-32d5-94bb-7be713402b94 | -9.35842 | -35.94685 | 2025-11-03 03:10:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4761cbb6-5b51-3d85-b06c-f3e3dd5a4199 | -7.95898 | -39.62384 | 2025-11-03 03:10:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f27c3400-91ea-344c-88ee-a560eeb20d7b | -9.54342 | -40.34206 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 93a66894-6954-353f-8a6b-6ef6dd3d52a3 | -9.54452 | -40.33652 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 3f4453d0-10cb-32a5-a3b2-65ddb1d4f942 | -9.54352 | -40.34396 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 0c7ecb36-df0f-3c66-b60b-143f7e8a3f98 | -7.96314 | -39.62883 | 2025-11-03 03:10:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| da1cac92-725e-3d54-a03c-35b09b9f5af2 | -7.96439 | -39.63005 | 2025-11-03 03:10:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ff405bf-5a28-3d14-9e3d-79720c3c279c | -9.67573 | -37.09072 | 2025-11-03 03:10:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 88f31f68-4e69-3e8e-aa1e-3071bdf70407 | -9.53705 | -40.34261 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0358b314-2b55-3083-9662-8ee2c5e73089 | -9.54232 | -40.3476 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| c4ebbc2c-fb97-38e0-b69d-95203035a1fa | -10.04487 | -36.25793 | 2025-11-03 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3bf68f1a-6ad3-38e0-8cd7-c49d1d9f9453 | -9.35742 | -35.95247 | 2025-11-03 03:10:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0449ab09-3465-33e6-8283-1417e36cb394 | -9.53696 | -40.34073 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5881853e-2553-39e3-9c0f-9a59f47b901e | -9.53812 | -40.33707 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b22ccf5f-caf9-3d89-b06e-d4e1c56f17c5 | -9.36333 | -35.94782 | 2025-11-03 03:10:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 07aedaec-2f41-3ce0-8a9a-22ad5192007a | -9.67636 | -37.08735 | 2025-11-03 03:10:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 355c016e-2fca-3eb2-a4bf-0bf493c506c2 | -9.54989 | -40.34336 | 2025-11-03 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| f1b98469-0eaa-3824-ace0-5abc88b5eea7 | -11.11681 | -41.09761 | 2025-11-03 03:12:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3568a967-ad85-3834-98df-9543d3dd8ce7 | -5.0399 | -43.6205 | 2025-11-03 03:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| af17ca3b-553f-3ce7-b106-a823c28155bc | -10.0463 | -36.2664 | 2025-11-03 03:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 68bf5907-b4c8-3891-b030-f6c2db0a8a67 | -5.0399 | -43.6205 | 2025-11-03 03:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f24bbf26-9aed-3f1d-afd8-5d424983ad1d | -3.4936 | -50.319 | 2025-11-03 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 2035d5c2-9320-3687-8e3a-e411f243885a | -5.0399 | -43.6205 | 2025-11-03 03:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 576bf49b-15ce-3423-8d4f-efc9b83ce89d | -5.0399 | -43.6205 | 2025-11-03 03:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 6328f87b-66c7-39a7-bef3-81bf89af9ce1 | -1.24133 | -46.03034 | 2025-11-03 03:57:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ed13a759-ed85-324f-9da6-4e21e15baf83 | -1.25557 | -46.03253 | 2025-11-03 03:57:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 74d28110-929f-37f2-b419-1520b2fa6d40 | 0.86685 | -51.25114 | 2025-11-03 03:57:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 25e9c876-d00b-3a81-bd96-74a6f6235e22 | -5.7906 | -40.83108 | 2025-11-03 03:59:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d44ab771-ed35-3911-8b3d-ec9cc76052b5 | -2.53198 | -45.28329 | 2025-11-03 03:59:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ff42d89-3b7b-3fc8-9895-d58b3e73ac94 | -5.26521 | -42.71992 | 2025-11-03 03:59:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b76ef109-8134-3610-8605-87de24bf2dee | -6.10158 | -41.74214 | 2025-11-03 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d80de704-c4ff-3f3a-9bb7-eef8532e1047 | -3.17266 | -46.57902 | 2025-11-03 03:59:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92e1a697-33bb-32e3-96fa-6f827adbf902 | -5.08552 | -44.20609 | 2025-11-03 03:59:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 555c3fba-b073-336b-80bd-dc0e1dd1b0a8 | -4.30751 | -41.45074 | 2025-11-03 03:59:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4a40bcaf-96cb-3cf3-9d68-e03492a8a8bc | -7.0398 | -43.16355 | 2025-11-03 03:59:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed4ecda8-dcea-313d-9674-30c58e5706f5 | -7.0441 | -43.15998 | 2025-11-03 03:59:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f05525c3-d6f8-33f3-88ec-26524e55ca07 | -3.17179 | -46.58419 | 2025-11-03 03:59:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de95e463-7b09-3104-9819-86d1bb172345 | -4.21344 | -44.23049 | 2025-11-03 03:59:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5e4ee47-799b-391e-becc-ac7e2d2e3f29 | -2.49209 | -48.15367 | 2025-11-03 03:59:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4a49eb0-e9ad-33d0-adb1-bdcfe7077907 | -6.70941 | -40.83307 | 2025-11-03 03:59:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bb1f5f91-8f27-3edd-b525-c090b613b10b | -7.96418 | -39.62477 | 2025-11-03 03:59:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 443d81e0-25c3-3a54-a03d-dccb263425c4 | -5.65401 | -46.59635 | 2025-11-03 03:59:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 354a25ec-139f-32bf-8a99-7ad3b8152e3c | -3.24673 | -50.79373 | 2025-11-03 03:59:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c004602b-0839-3ab3-aec4-7d2b05cc57bb | -4.65582 | -42.51777 | 2025-11-03 03:59:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 22269511-3396-3dbe-adb9-d7250ee2f5be | -2.49319 | -48.14685 | 2025-11-03 03:59:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cefae6a0-1ee6-3dea-adfe-708e75158498 | -4.39217 | -45.94574 | 2025-11-03 03:59:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2fdc454-2a25-34b7-93b0-0abb3ec0e8f7 | -4.29653 | -41.45317 | 2025-11-03 03:59:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ab0f842-0c72-36cf-98b4-296b6b62449f | -5.79004 | -40.83462 | 2025-11-03 03:59:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 16e91b69-30e4-3399-b582-aaf2a75f1cb2 | -3.62778 | -40.39254 | 2025-11-03 03:59:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b35d829a-c7f1-3f9d-81a8-7ae4c20f5c4a | -2.75153 | -44.90551 | 2025-11-03 03:59:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6946d504-3ef2-3140-afef-fd628062ae4c | -5.79225 | -40.84227 | 2025-11-03 03:59:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7edb1f69-38c4-3f4b-b6e2-cde3d55a6217 | -4.65942 | -42.51832 | 2025-11-03 03:59:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81c5608b-0ba6-321b-a836-27076b3129a3 | -5.72105 | -42.1893 | 2025-11-03 03:59:00 | NOAA-21 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 676b7c58-738c-3639-af5a-c1263902b4c6 | -2.31472 | -48.58318 | 2025-11-03 03:59:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 846b863c-9fbf-3d42-88a1-df88000fd0cb | -7.04341 | -43.16417 | 2025-11-03 03:59:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a94c2f19-b2ef-38fa-b19c-4c8e239c6808 | -4.84551 | -42.92384 | 2025-11-03 03:59:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc1bfd43-532d-3da2-bf9b-5471e9e569cd | -5.42997 | -46.36084 | 2025-11-03 03:59:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea67fe66-2abf-3707-be56-d7728aef446b | -3.36131 | -42.12631 | 2025-11-03 03:59:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd81987a-298c-3a7f-8781-8fd1bc93a107 | -4.31096 | -41.4512 | 2025-11-03 03:59:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 02e9aace-cfba-3b2e-a5a8-34ee75cef330 | -6.22181 | -42.68292 | 2025-11-03 03:59:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 57d10534-25f9-3db5-b8aa-7530d7555479 | -7.37498 | -45.5154 | 2025-11-03 03:59:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cdec7d32-ee16-3ea8-b716-588cfceb1385 | -5.26881 | -42.7205 | 2025-11-03 03:59:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a7b31608-d2f1-33d5-ab0f-0dca7284e756 | -3.24266 | -50.79999 | 2025-11-03 03:59:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d8eb32f-88dc-3806-b6aa-789d3c768a7b | -4.25721 | -44.24951 | 2025-11-03 03:59:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac7a4887-c91f-3162-9b4f-096141395660 | -6.10502 | -41.74261 | 2025-11-03 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README3.md)
