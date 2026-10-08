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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4063d0c-7815-39bb-85d5-3eb5d6f55976 | -3.0876 | -54.238201 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36014775-be53-385c-ad55-0e7ddbebbbf4 | -5.8577 | -57.553799 | 2026-10-08 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1d17b61-33e6-38e1-9b9b-ed8f8f25f147 | -3.8607 | -50.412498 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb2f5901-3c91-3197-80bb-0fbbe194fa3c | -2.1569 | -59.213699 | 2026-10-08 00:26:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aed1d945-8415-3a14-af4a-9c31252f0b8c | -6.5105 | -55.390301 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6016686-b4b2-3e12-ba11-bdb2f1ebb554 | -3.0131 | -54.182499 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d30565-af4e-30a5-a07b-189f0ac05221 | -2.802 | -54.070099 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abea9e77-75c9-3254-ad38-7b8d0794dbe0 | -3.201 | -50.543499 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44693820-4263-31d8-b6d7-3c60fe29cc11 | -6.6291 | -43.7565 | 2026-10-08 00:26:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af2a48b6-b47c-3375-bf59-ad81177ae87d | -6.3928 | -55.231899 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8c5c2b1-4896-381c-9b98-81fe4b486889 | -11.0693 | -54.5065 | 2026-10-08 00:26:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86bd440c-0098-31f4-b73e-97d5443af82c | -5.9013 | -53.506302 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d89cc5-151d-3c72-930e-d9b032c66f15 | -3.1706 | -50.590599 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f52ac92a-c4cd-3195-ac22-291c5ffb0f16 | -3.5773 | -54.3521 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6825ff5e-573c-388d-9277-0b3e0467afce | -10.3021 | -46.600498 | 2026-10-08 00:26:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51a73efc-8fb6-3107-a9fd-74accb5582a1 | -9.5157 | -54.739201 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a404664-804c-3f7e-be46-90af320e02b0 | -6.3315 | -55.326401 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c29b57b-b55e-39ad-9237-b2b2a82689a4 | -1.5224 | -54.565201 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a9b3dd-23ce-3c2b-94a0-bbf124ca171a | -3.0711 | -54.256302 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6fd1a59-ec89-328e-baa4-221edaf57440 | -3.6518 | -54.270802 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67b18841-f8bf-348d-b3c0-0c07829e30d1 | -3.0436 | -54.226299 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43bf497b-1752-3b16-a80f-943bc3c6fdcc | -3.0126 | -54.226002 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a470b06-8f58-33be-9b7b-872534a23262 | -6.0246 | -55.3354 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 681bb348-0d50-31fc-a96a-be9e04dd5124 | -14.9272 | -48.094601 | 2026-10-08 00:26:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2beb6a3-1312-3ea5-8258-8c8270b53a1a | -10.8766 | -49.141899 | 2026-10-08 00:26:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b6d6fe4-bbe8-3fee-8e07-589f8269f4e6 | -5.3332 | -50.9841 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c10de22-4631-3ee2-9824-a8f10429440e | -6.1097 | -55.717098 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a877c2c8-9992-3231-8c7f-906d5f3c6bdb | -2.9892 | -54.1227 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df84899a-fd90-3c7c-bf4c-2bfc92fa07cc | -4.2833 | -49.0886 | 2026-10-08 00:26:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb8a7724-01d2-3341-980a-c8bff1841f0b | -10.3087 | -46.627399 | 2026-10-08 00:26:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9760859b-a656-3df8-a069-48c91c2f2eaa | -5.8758 | -53.620998 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c46a338-bb8c-3dff-8eba-166b7a86b3ba | -3.1819 | -58.6488 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69df979b-1d3a-35cc-933b-8e8b649ceb41 | -2.9381 | -54.1703 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 834ad585-aef2-3e8e-8c27-e9aeeb878ed6 | -3.6989 | -50.6479 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f370b618-9b36-36d0-b34b-7585692a7f81 | -3.2933 | -61.003399 | 2026-10-08 00:26:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12b94293-6673-3a7d-bf1a-b6fe7947fa0f | -5.704 | -53.499699 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acca553d-4bf5-3c32-abb6-fb49a0f5ae1c | -6.1919 | -53.287399 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8407b209-26dc-3f77-8fec-2470e8452c63 | -2.983 | -54.0951 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec4bfb9a-a916-3ab2-b6ba-01b48edfd763 | -5.7436 | -53.447102 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 860f08eb-1706-3293-8c3f-54b1dc578b4b | -11.8504 | -43.547699 | 2026-10-08 00:26:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4afb687c-074e-3a98-8ef9-e18abb0aee44 | -9.4706 | -64.326401 | 2026-10-08 00:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d26af0e-f820-3c08-bc7e-adb9ddfc3511 | -3.4509 | -59.814899 | 2026-10-08 00:26:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e14fe62-c43b-390c-9359-d214c2a0e6b9 | -3.1009 | -54.980801 | 2026-10-08 00:26:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd243796-f066-3857-8d57-6e35d2504c0e | -3.0856 | -54.2747 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a67fe1-8d2f-3205-bb61-bc753d989b95 | -6.9514 | -45.257 | 2026-10-08 00:26:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bb4ab29-9870-3059-8997-68ab16149d68 | -3.3663 | -58.184101 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75027f11-7461-3d13-aaff-f36abe0f09b8 | -3.5054 | -54.626301 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 246634f1-5ae3-3b51-8eaf-4963f719f43e | -3.51 | -54.646702 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9d4e9f-1968-3a1d-92c4-23b1aca7e116 | -7.75 | -54.945801 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b051ec71-baa8-3f5a-ac61-0efc67351b6b | -7.2542 | -48.065102 | 2026-10-08 00:26:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7305fe3b-9949-38d0-bf09-d5a2af259920 | -3.2536 | -57.8633 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9179766f-1a41-38bc-b5ed-0bb92befc3ca | -2.8699 | -54.142101 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52b0c2e2-ead5-3676-b55e-d107acf696cd | -2.926 | -54.071499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df44b974-b09f-3274-8382-edcfc20b2841 | -3.1808 | -54.741402 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4c9774-3a95-3092-9bbe-f3ddc506783d | -2.5516 | -57.3936 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f68e572-5e7d-3b88-b8d1-eef4a9cb7953 | -3.0762 | -54.233501 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaf8d6c3-a1e4-39fc-bbbe-d1eee8239eb3 | -3.5188 | -54.594601 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7ea4e9-02f9-39b8-9025-b8e3adcd115c | -7.2011 | -45.3526 | 2026-10-08 00:26:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4491d99-ba97-3838-b4f4-f74dca4bdeb7 | -2.9037 | -54.018299 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c379964-827f-3247-b902-36a4d1b737db | -4.3764 | -54.740002 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 171f5ca7-3bbb-3142-89af-9200e3206799 | -8.2155 | -46.335999 | 2026-10-08 00:26:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45d9b388-4d2d-3b39-b7d8-ab5ab5fce61a | -11.3446 | -51.862999 | 2026-10-08 00:26:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b329f36-0a80-316b-be07-3763bdd7522f | -3.242 | -57.857399 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61b3fb45-5809-3b90-917b-347c8fab605d | -1.7417 | -57.180401 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec64f71e-b433-3ce2-96c8-afb95041e5ba | -3.2636 | -54.651501 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9971f4b-16c3-3f0f-a5c5-50fb1bc720cd | -19.9918 | -49.087002 | 2026-10-08 00:26:00 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07d313fe-3b53-34f4-a395-200caab07384 | -3.0254 | -54.100101 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0782298-dc8b-301d-94a5-b4605a878ad2 | -2.9676 | -54.163799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c969ce7d-daf5-398e-a6fb-5b27ca40a664 | -11.5235 | -47.578999 | 2026-10-08 00:26:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8dea2ce-3e09-350f-acb0-8b1a448f0448 | -6.2234 | -52.8367 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661b031d-8043-39b8-9e20-6c7d143d7f86 | -5.8998 | -53.499298 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ebecc97-d534-3b25-8c7d-0809852631f8 | -6.2183 | -53.266899 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feeb5ff6-a279-319e-9de3-21c49a51fa3c | -4.1331 | -54.256802 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34701fc2-a298-3732-a200-bbcda7738b02 | -3.8608 | -55.975601 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e70914a-e2c4-390a-a437-54a44861e80e | -2.9276 | -54.0784 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75dc4743-ca77-3edb-a04f-dba935e3a01b | -9.2811 | -50.302898 | 2026-10-08 00:26:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9744a820-42e8-3281-b8c1-53890b105a41 | -0.8458 | -51.8582 | 2026-10-08 00:26:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| dc65f331-d894-3608-80c0-d3298f47b536 | -6.2315 | -52.8722 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66a49efe-fbc0-3463-9562-c7e53249db82 | -4.2163 | -56.0452 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daa31419-e413-332b-b953-06b6770cdbb7 | -2.8358 | -54.127998 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13522320-80b9-30cc-991f-9a3b60cddf86 | -3.8913 | -59.440601 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae9b8add-b902-345d-951b-ea071083ba4e | -2.6501 | -56.547298 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 222be4ad-5dd0-3c82-92e0-b0fad5998f1e | -8.9051 | -49.976398 | 2026-10-08 00:26:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4db26c75-2652-36e1-84e5-7c86c660ddb1 | -3.084 | -54.267899 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8667c4da-6643-3882-97d1-e8b4bfd41808 | -7.2033 | -55.125999 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c45cd9-4651-39e3-90f3-58ba96ad032c | -2.9802 | -54.037601 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69a3b896-483d-38ef-bea7-c0c44ec74f9f | -3.1591 | -54.099201 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41bdfe82-5d71-309d-aecc-af2badcb5ca8 | -3.0304 | -53.895199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c682aff-865e-3fd3-a1bd-06dd9dab805a | -4.3779 | -54.746799 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3793427-2e6c-3bf6-a682-a53e66fb7821 | -2.9939 | -54.143398 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 473a9202-8f10-3a6d-b64e-a757e182cd3c | -3.7445 | -59.472401 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff2452a-dece-3ab8-96f9-24f16d05c535 | -2.7674 | -54.099602 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee73c467-05be-3f38-bf90-04101cc294f5 | -5.9704 | -55.369499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8dac991-801e-3b3d-bd05-8b433be980d8 | -4.5215 | -54.973 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c71ec2-aa70-303a-b56f-4c6b952c2cfe | -2.9672 | -54.207298 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22d59dc9-3e01-3102-925a-e1f9077595fa | -3.575 | -54.6609 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9988793-bcbf-34d3-bcfc-82ac6095c3e0 | -3.0871 | -54.281601 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32a5a9f7-7d77-38fb-ab07-ac755f66448b | -5.0669 | -56.9058 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d3def1-e860-34bc-a270-9ab196bcf261 | -12.2004 | -57.1147 | 2026-10-08 00:26:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8e07a6-e142-300a-9c47-75211d7a5de9 | -3.1243 | -53.764099 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
