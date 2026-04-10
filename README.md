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
| 5039950a-665e-3af1-b283-d8273d33c30b | -18.4921 | -55.505 | 2026-04-10 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| f8ffdbcb-f57d-3748-8154-588f56ce300d | 2.9094 | -60.3698 | 2026-04-10 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 861cce28-0aa6-3fbb-a793-72ca70fc7dd7 | -18.4921 | -55.505 | 2026-04-10 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 5c64d6b8-8ef1-35fd-83a6-b4e4d9babad4 | -18.4921 | -55.505 | 2026-04-10 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 757066d8-79c4-3dd9-a74a-5ef4c5001584 | -18.4921 | -55.505 | 2026-04-10 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| e23a98b5-79f5-31ae-8a62-34f486202c45 | -18.4921 | -55.505 | 2026-04-10 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 95030118-ac97-3ec5-aacc-0f0935379b7c | 2.9094 | -60.3698 | 2026-04-10 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c444a480-df19-3e40-8edf-b84617f29292 | 2.9094 | -60.3698 | 2026-04-10 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e130abdd-5598-3962-9257-a29f6a3d2268 | -18.4921 | -55.505 | 2026-04-10 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| b933cd85-6c8e-35c6-a262-8b982b209b90 | -18.4921 | -55.505 | 2026-04-10 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| a5c374a0-f630-3909-87f7-caacb67fa0ca | -18.4918 | -55.497501 | 2026-04-10 01:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 27b13de6-ab86-3060-8398-3bbc1d8863fc | -18.496201 | -55.515999 | 2026-04-10 01:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f8d3a916-391a-3d96-b9bc-bf4733b36209 | -21.2043 | -48.6548 | 2026-04-10 01:02:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b20b0b6f-4af7-3c18-b944-f7fd980041aa | -18.489599 | -55.4883 | 2026-04-10 01:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f9607074-5378-397b-aa73-9871e9568cc4 | -18.493999 | -55.506802 | 2026-04-10 01:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b24644d5-5c2a-35cb-8016-ad36adfe8fb2 | -18.4993 | -55.485699 | 2026-04-10 01:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 95e81afe-474f-3fce-a057-3ce34a49f525 | -21.1982 | -48.632999 | 2026-04-10 01:02:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f20b8a9-cb17-3ac1-918b-d025f555992c | -18.501499 | -55.4949 | 2026-04-10 01:02:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f86551bc-70cd-3afb-bb23-0ba30daeae33 | -18.4921 | -55.505 | 2026-04-10 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 0c1ae3e9-896a-3bf8-9d2a-df4330a328d3 | -18.4921 | -55.505 | 2026-04-10 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 33b019db-06c7-387b-bdd0-41073e5ee6fc | -18.4921 | -55.505 | 2026-04-10 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| cd24e27d-c003-303d-9415-91596ef7fcc0 | -18.494699 | -55.504601 | 2026-04-10 01:35:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8274e0ab-94c3-3387-8a06-70c1a600059f | -18.504499 | -55.501999 | 2026-04-10 01:35:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bdaca2f3-c94c-32be-8458-d11130bdb2b2 | -18.4998 | -55.483002 | 2026-04-10 01:35:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 23a86749-1337-301b-8d17-55eed02b4912 | -21.2148 | -48.648499 | 2026-04-10 01:35:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8dd33c45-52e6-3b10-b5de-4e03df93bdbd | -18.497101 | -55.514099 | 2026-04-10 01:35:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 07e1f828-d755-37be-b335-ecabc913ee9a | -18.492399 | -55.495098 | 2026-04-10 01:35:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 31b17af8-4020-396a-9d94-bc3f73005b78 | -18.502199 | -55.4925 | 2026-04-10 01:35:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fa11cae3-d624-37d9-8e3c-ffd0fba1390b | -18.4921 | -55.505 | 2026-04-10 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 410d6a10-1905-322a-9e0e-08d48babc777 | -18.4921 | -55.505 | 2026-04-10 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| f2f8fd1a-9d9f-3e0f-b057-d4178e042c16 | -18.4921 | -55.505 | 2026-04-10 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 5b2b9af1-6c2e-354f-a9a7-7f96b9018f0d | -18.4921 | -55.505 | 2026-04-10 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.3 |
| cc74f774-1e30-33f0-9461-cdce3a0dc7c6 | -11.04293 | -38.35216 | 2026-04-10 03:32:00 | NPP-375D | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b0d52d9-26cd-3d53-a8ea-d723d4648e6b | -11.04743 | -38.35306 | 2026-04-10 03:32:00 | NPP-375D | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d8f1fa53-871a-311e-8cea-1879c47f3439 | -13.37092 | -42.13353 | 2026-04-10 03:32:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c43b5476-1b52-39a9-a0b7-a66e7ffa9adc | -11.60567 | -38.92088 | 2026-04-10 03:32:00 | NPP-375D | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 601f83af-1265-36ab-b20d-d74ba1dcbe06 | -13.37013 | -42.13741 | 2026-04-10 03:32:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8e96bce2-3430-3295-b65a-e6e806c176f0 | -9.3764 | -37.8123 | 2026-04-10 03:32:00 | NPP-375D | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a23e0b18-8d05-3dfd-b489-0d9f4588156a | -8.84211 | -37.03004 | 2026-04-10 03:32:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 59570fbf-e421-3c35-a464-bf16111b9318 | -11.04644 | -38.35555 | 2026-04-10 03:32:00 | NPP-375D | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3392795f-023f-3415-8891-30005fd26aa1 | -9.3756 | -37.81679 | 2026-04-10 03:32:00 | NPP-375D | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a505130-40b8-34fd-868b-3e44bf1c98ba | -15.2838 | -43.06942 | 2026-04-10 03:34:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 69ff99cc-c8db-3d30-b2b9-f613ccb9caf3 | -19.5933 | -40.07427 | 2026-04-10 03:34:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a29c166c-15dd-3ade-81fa-5df0bda5f0f3 | -15.28464 | -43.06536 | 2026-04-10 03:34:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d3f19cae-1c70-3954-a42f-00db7809b176 | -19.59246 | -40.07864 | 2026-04-10 03:34:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 364bafa0-eb79-3c97-a479-ac8354e92060 | -26.47355 | -48.75364 | 2026-04-10 03:36:00 | NPP-375D | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6336f07c-a455-34c1-9823-2df9ef86496c | -9.60495 | -36.90365 | 2026-04-10 03:51:00 | NOAA-20 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b9dec50-1048-3cdc-886d-e5a5a5bbf359 | -10.35683 | -36.74355 | 2026-04-10 03:51:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3acc6258-0e21-300f-894a-3d176f78d2e5 | -10.35945 | -36.74413 | 2026-04-10 03:51:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a44a3784-0ac2-3edc-8cf7-f6eb69df43eb | -12.65277 | -39.16993 | 2026-04-10 03:51:00 | NOAA-20 | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d8fc200-231e-3877-9ac6-e3959abc1e26 | -12.10368 | -41.31228 | 2026-04-10 03:51:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76f95c36-73cd-3ac3-9c2f-eff3f78f5ffa | -9.42114 | -39.30162 | 2026-04-10 03:51:00 | NOAA-20 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bb1d91cc-9c2c-3d89-8f70-2b07157477ab | -12.40132 | -38.83151 | 2026-04-10 03:51:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e545f75a-873d-379a-9223-078c0d383403 | -13.50535 | -39.92613 | 2026-04-10 03:51:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0427e84e-a411-3f4c-94d9-4149c72bf000 | -14.11853 | -41.84946 | 2026-04-10 03:51:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0cc9fbe9-1f0c-3340-bb98-b94c2f1480d4 | -13.36725 | -42.13565 | 2026-04-10 03:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc99df71-6a53-369e-b5ad-be20d1a734c3 | -9.37648 | -37.81467 | 2026-04-10 03:51:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7e987f9-cb6a-3d2c-bded-e3b594223a3d | -9.37704 | -37.81119 | 2026-04-10 03:51:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b810edcf-d833-312a-8d18-26a1983366e3 | -11.0442 | -38.3516 | 2026-04-10 03:51:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c1cd51ba-be6c-39a3-be07-f03ba0ccdb32 | -11.04363 | -38.35511 | 2026-04-10 03:51:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2134a232-a3d6-31a3-b35c-c228dd434e68 | -11.6056 | -38.91937 | 2026-04-10 03:51:00 | NOAA-20 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b7dc916-ac23-3e7f-aa36-d82be544f759 | -9.54528 | -40.60339 | 2026-04-10 03:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d9ec369-b165-3b42-947c-31950d462c96 | -15.38001 | -43.06058 | 2026-04-10 03:53:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb0d840d-8610-3654-bb9d-64bcc77bb45b | -15.28519 | -43.07012 | 2026-04-10 03:53:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e4b3d964-1ce6-34a1-aa55-70c114c5e592 | -15.9743 | -41.84734 | 2026-04-10 03:53:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 278645be-b4bb-3992-916c-b018b289f524 | -20.18168 | -46.59484 | 2026-04-10 03:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 832eb435-78e1-3d76-8e4a-d780a32e8177 | -15.78738 | -41.94366 | 2026-04-10 03:53:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ef952cf-5b1c-3d94-8ee8-63f002756fcb | -20.18347 | -46.5856 | 2026-04-10 03:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33584b80-b820-3c1d-8047-8efd6b68f671 | -20.18602 | -46.59561 | 2026-04-10 03:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7685a05a-78bd-3c3b-be56-b9788805fb88 | -15.28603 | -43.06532 | 2026-04-10 03:53:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| fb714dac-172b-37c9-a9fb-3f78aa4bda7e | -17.50218 | -42.35647 | 2026-04-10 03:53:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22d5eea1-6417-3eb3-ac81-b0c14a2cc60f | -15.28141 | -43.06937 | 2026-04-10 03:53:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 88761ea3-46b3-36d8-9a2a-8686956fb7c3 | -20.19035 | -46.59648 | 2026-04-10 03:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b3c192e-41d3-3fab-a5e5-535810824633 | -19.59228 | -40.07633 | 2026-04-10 03:53:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 32ee5ccf-f0f5-3323-91ac-257af9a2e179 | -21.20428 | -48.66441 | 2026-04-10 03:55:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4093ea3e-9e5e-318b-a0c3-a6c854cbc830 | -21.20549 | -48.65873 | 2026-04-10 03:55:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 63e51086-ac45-37fc-8089-74d3f9a00c44 | -22.87745 | -48.6514 | 2026-04-10 03:55:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9b4676a-cffc-317b-8a44-1f5102505b31 | -20.83638 | -47.28152 | 2026-04-10 03:55:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51b96e5a-c7ef-33fa-a2ef-061ed559653d | -22.88207 | -48.65267 | 2026-04-10 03:55:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf72b9fd-270c-3319-93b3-d0969565539e | -21.20641 | -48.66381 | 2026-04-10 03:55:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f8162090-fe22-3414-8041-06ae16235fea | -27.44836 | -48.44603 | 2026-04-10 03:55:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 33bb8dcc-cdf7-321a-937f-79893e03432b | -21.21029 | -48.65993 | 2026-04-10 03:55:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| db13fec6-9e59-3a79-89bd-621f05c608ca | -7.10257 | -49.93354 | 2026-04-10 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5f63eed-84cd-3cb8-882d-84d2cb8b9013 | -15.28718 | -43.07276 | 2026-04-10 04:42:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a57a33e2-b3ca-3dbd-bd52-d85abee9a2ba | -15.28661 | -43.07261 | 2026-04-10 04:42:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 43da0be5-c8d2-3548-9f5c-1c1cd70efbfb | -15.28732 | -43.06683 | 2026-04-10 04:42:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2eb5b563-faad-3e1a-8242-dd5c26728427 | -15.28219 | -43.07217 | 2026-04-10 04:42:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 51659588-926f-3024-b08e-8071ced5e969 | -15.28784 | -43.06698 | 2026-04-10 04:42:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 4dd9508e-fa8b-388d-917c-a63cbcedcf81 | -18.49515 | -55.49748 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 334ec266-5b43-36b1-8138-224c61b9c31f | -18.49438 | -55.50185 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 32829aa0-37ed-3349-86d4-8e5770847fa4 | -22.88049 | -48.6518 | 2026-04-10 04:44:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2bdf85d1-c751-35d1-b70e-3b0813d69bb3 | -18.49798 | -55.50254 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3d0d15ca-845d-307c-8289-18b1bb137c6c | -21.71836 | -48.43574 | 2026-04-10 04:44:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a333a31a-fb2c-35d5-b7b1-6bc05e0a249d | -18.48856 | -52.24944 | 2026-04-10 04:44:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee73b861-5336-3f1c-8a9c-6420ebbddf02 | -18.49875 | -55.49817 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b5bdf0b1-5d76-3e02-886d-7a9a528c6826 | -21.20859 | -48.65886 | 2026-04-10 04:44:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 51a53ecc-46b8-3da4-990c-df768f3d6f08 | -18.49644 | -55.51127 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9c1cef91-08bc-3909-927b-e5894f252d6a | -18.49952 | -55.49381 | 2026-04-10 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 87efbaa7-a6d6-32a6-84ae-c414c3786fa3 | -20.83765 | -47.283 | 2026-04-10 04:44:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 846a0b88-339b-3394-9219-3aa12e427784 | -21.20794 | -48.66371 | 2026-04-10 04:44:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README2.md)
