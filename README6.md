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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 655527b0-52b9-385b-8849-98d4bb73ef3a | -14.368 | -54.5562 | 2025-10-12 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 51bb90a2-ff08-379b-803b-02a555e0d13b | -2.5423 | -47.811 | 2025-10-12 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 140.6 |
| a06bceeb-8880-3b82-a35c-1a68dcf60aab | -15.682 | -46.6481 | 2025-10-12 00:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1dd82262-dabd-3aca-8f4f-9d527fd440c4 | -13.6973 | -43.8389 | 2025-10-12 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 93c7a1db-4969-3cca-b254-f6d5c83d6e91 | -15.6825 | -46.625 | 2025-10-12 00:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 118.0 |
| b9e6e626-4250-3ea0-90b7-f34acc286579 | -19.0515 | -57.5564 | 2025-10-12 00:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 79464145-bf1c-3ac2-8697-9e3aff5457f2 | -7.5212 | -46.538 | 2025-10-12 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 9c83399e-2069-3e8c-b397-585a6f1bb66a | -13.6778 | -43.8424 | 2025-10-12 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 33345140-166b-3b64-b538-95b7b24b8a82 | -19.0316 | -57.5589 | 2025-10-12 00:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 77a752ae-eb2c-3995-9c88-cd361b091dfc | -14.0161 | -43.4703 | 2025-10-12 00:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| af87f346-3c22-3744-b651-e7e856621c61 | 1.9134 | -55.7419 | 2025-10-12 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| b6f97863-5c02-3e27-9a38-fe808656f69d | -7.5215 | -46.5157 | 2025-10-12 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 50203fcf-2176-3f7e-a17c-13b9d94b5de3 | 1.895 | -55.7421 | 2025-10-12 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| e3a9808f-62c7-34be-b66d-a39dd23d2dfa | -15.6628 | -46.6287 | 2025-10-12 00:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 66b15726-1c9e-3621-b85d-fb1c7a38a4f6 | -13.6783 | -43.8186 | 2025-10-12 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| bdd1176f-f1d9-3a14-9009-3750f989df1c | -4.271 | -46.9369 | 2025-10-12 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 9f7c6bfa-ad15-338c-82a9-dc045c327841 | -9.0161 | -67.4275 | 2025-10-12 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3c4315d6-e1e0-304c-847e-acef4e527b6b | -9.016 | -67.446 | 2025-10-12 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6b37a16d-1449-3867-92dd-4896b9a20f7d | -19.0519 | -57.5356 | 2025-10-12 00:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| e087067b-97f7-3785-80d9-7fb296a7bf4e | -3.5371 | -48.9195 | 2025-10-12 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c38491ab-cf17-3549-add5-dbc54c3d161b | -11.752 | -54.7255 | 2025-10-12 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e6ba3154-ea3d-3a73-ab36-919c29afcd17 | -17.5897 | -42.4246 | 2025-10-12 00:20:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 5ee2f9d1-8b43-3c32-9fa3-462699bd694a | -9.5359 | -46.5155 | 2025-10-12 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0ee74913-e9a7-3098-a8e1-817366e3e08c | -7.5025 | -46.5396 | 2025-10-12 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 5b330353-a650-369f-999b-fc6107b1d7ca | -10.9856 | -61.6021 | 2025-10-12 00:20:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 428ec450-1b40-31d3-ac70-5221be36b5f1 | -2.5238 | -47.8115 | 2025-10-12 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a477a55c-975c-39c4-9cda-e2743d7a4dcb | -4.2711 | -46.9149 | 2025-10-12 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| cf500f1a-1c4d-30da-a1a1-0a3226178d15 | -19.0319 | -57.5382 | 2025-10-12 00:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 119.7 |
| 64cfb19f-9926-3061-a8bb-28c3f96b4401 | -11.7331 | -54.7272 | 2025-10-12 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 043f6f9b-9669-35bc-8d71-70759e9c00ef | -10.9668 | -61.6031 | 2025-10-12 00:20:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9dcdc6af-a272-3ac0-8533-9d4a89f44238 | -14.0155 | -43.4943 | 2025-10-12 00:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 331fc155-11c1-3c43-bfe4-48fafe1847ff | -9.5362 | -46.4931 | 2025-10-12 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 85627f6d-38af-3958-9873-859560dde610 | -2.5424 | -47.7893 | 2025-10-12 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 73a864df-244a-347d-a42f-78eda6e8d7b8 | -4.2896 | -46.936 | 2025-10-12 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 37aba3ef-d977-3ca8-8b95-2d378800a7a0 | -13.6578 | -43.8697 | 2025-10-12 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 246.4 |
| 663204af-ee57-30e1-864b-b1144c9fb591 | -11.752 | -54.7255 | 2025-10-12 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 410e85e3-4ae9-3dc6-969b-ec396fb250d1 | -7.5025 | -46.5396 | 2025-10-12 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 07b14b0e-185a-3924-93b1-4ce92e580bf1 | -2.5424 | -47.7893 | 2025-10-12 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 0137605c-c56a-3eba-9f73-d948e3ae3cf1 | -9.016 | -67.446 | 2025-10-12 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b8fb2dd8-38b6-37e5-9750-5604abf2b0d3 | -2.5423 | -47.811 | 2025-10-12 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 3481a15f-bbcd-3a60-921e-31835a29cc73 | -7.5215 | -46.5157 | 2025-10-12 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ffe1f877-a207-3870-90b1-f2079a53817d | -19.0316 | -57.5589 | 2025-10-12 00:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 099a2474-ce81-3f1a-986c-2d60e65df4ce | 1.9134 | -55.7419 | 2025-10-12 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| bfcec615-5905-3ac6-bcd9-aa0e05c20ff1 | -14.0155 | -43.4943 | 2025-10-12 00:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| b47d71ce-7c88-33d6-b002-c389624fe05a | 1.8582 | -55.861 | 2025-10-12 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9441fb5c-ed12-34cf-b226-50d93b863b46 | -4.4241 | -43.4735 | 2025-10-12 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| a7b418fc-638a-36e6-a48e-1d87ba526ec8 | -13.6973 | -43.8389 | 2025-10-12 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 3de11d0b-18f5-33ee-84da-acdfb3cf0a9d | 1.895 | -55.7421 | 2025-10-12 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 2d43ee22-22fd-3a8d-ba23-18db89923d9a | -19.0519 | -57.5356 | 2025-10-12 00:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| f6c947be-3ebf-3dcf-8c8f-cfbd2382ef12 | -13.6773 | -43.8662 | 2025-10-12 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 245.9 |
| 3e099502-4e35-3a50-8be4-9adb8f84ac10 | -14.0161 | -43.4703 | 2025-10-12 00:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 2d291c58-46b6-3ac5-a067-186c9688c493 | -13.6968 | -43.8627 | 2025-10-12 00:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e211c5bc-8191-3f6f-b545-72224063c26a | -3.5371 | -48.9195 | 2025-10-12 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| c94edf53-437c-3eaf-9909-391139a6818b | -7.5212 | -46.538 | 2025-10-12 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 8343792c-b1f2-38c5-a58e-92ed57a10883 | -4.2711 | -46.9149 | 2025-10-12 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 65b228bb-ef61-3475-bb2b-4682bb8f4773 | 1.895 | -55.7619 | 2025-10-12 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ad3b1c0b-a02f-3c32-81ce-82e2905a7365 | -19.0319 | -57.5382 | 2025-10-12 00:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 4b80ad21-008f-33a3-b640-05d056d11179 | 1.9133 | -55.7616 | 2025-10-12 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d3519d31-518d-30e3-8174-90d118c79e36 | 1.9134 | -55.7221 | 2025-10-12 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| bff3907a-7b67-300d-bdc8-676971aab7e3 | -11.7331 | -54.7272 | 2025-10-12 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| c15d98eb-8403-3bc8-9178-91e017a6a733 | -17.5897 | -42.4246 | 2025-10-12 00:30:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 129.9 |
| af554bf5-c23f-3daf-8a6c-f579d04e894d | -13.6778 | -43.8424 | 2025-10-12 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 9b3bbfaf-6604-3c81-b31c-59bd0f559212 | 1.8582 | -55.8413 | 2025-10-12 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 30378e56-e51d-3d8b-88ba-234ede5e023b | -9.0161 | -67.4275 | 2025-10-12 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 55e40f88-4cc2-3824-b3da-4cb1eb5ddd14 | -4.2896 | -46.936 | 2025-10-12 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 02c4217a-309d-3510-901f-06fe9bee8130 | -13.6583 | -43.8459 | 2025-10-12 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 183.3 |
| e05dd598-7b5a-36e0-9eed-0cafe7f5c894 | -4.271 | -46.9369 | 2025-10-12 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 71370b22-b16b-372f-aa38-0ab0a25eba18 | 1.9134 | -55.7419 | 2025-10-12 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 84035da9-7361-31b8-8643-0cb25595cf16 | -2.5238 | -47.8115 | 2025-10-12 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| eb0dd799-08f2-3bca-b386-16f480eed0cc | -9.0161 | -67.4275 | 2025-10-12 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b936ce97-84f4-350e-8b94-e2d7eba6d7ff | -13.6778 | -43.8424 | 2025-10-12 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| b584499b-9c0d-31f9-98a2-78b3c488f9d3 | -7.0474 | -45.2538 | 2025-10-12 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 62138b35-9e27-31ac-9583-9b5c434ec58e | -19.0319 | -57.5382 | 2025-10-12 00:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| c84f1e50-2578-3455-a579-8a41d0a1bb4c | -6.5851 | -44.6098 | 2025-10-12 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| fe79000d-1026-30cb-9f14-a2c4f1cb12cb | -13.6583 | -43.8459 | 2025-10-12 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 7fe677ce-e262-328e-96c2-d82c722602e0 | -2.5424 | -47.7893 | 2025-10-12 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 9ada6869-c8b2-3288-9c4d-2c511a56f399 | -9.016 | -67.446 | 2025-10-12 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| bb591a96-6616-37b4-9948-f89709fb7638 | -4.2711 | -46.9149 | 2025-10-12 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e86006b6-2807-39b6-87ff-1a63184e0abe | -7.5212 | -46.538 | 2025-10-12 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| fdcb4560-cdc7-3649-82cc-10d6cfa5d824 | -14.0351 | -43.4906 | 2025-10-12 00:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| e00275cf-55cc-3bde-ae97-5f78294b9ee4 | -10.6431 | -69.5184 | 2025-10-12 00:40:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7fb00c61-752c-3d1b-a95c-191bb32a06a0 | 1.8582 | -55.861 | 2025-10-12 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f25e78ae-056b-35bf-bb20-cf16b467234d | -17.5897 | -42.4246 | 2025-10-12 00:40:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 137.2 |
| b9f93259-b285-306a-bb06-634c17f8e542 | -11.7331 | -54.7272 | 2025-10-12 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 7a5cf084-18ed-361d-8cb9-d6bee04912b0 | -19.0519 | -57.5356 | 2025-10-12 00:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 6404db4e-8898-34cc-bc31-49a8d805ade2 | 1.895 | -55.7421 | 2025-10-12 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 78ad283f-9fd6-33b2-9590-df8157ebd00e | -2.5423 | -47.811 | 2025-10-12 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| eb8e2699-93c1-3fd9-819d-d2f7ab1ea74c | -13.6578 | -43.8697 | 2025-10-12 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| b21f4993-8b92-3a6c-9cfc-f0fbaad08b31 | -7.0661 | -45.2521 | 2025-10-12 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| bedd2cd9-c892-3478-a5cc-a04c4faeba2a | -4.271 | -46.9369 | 2025-10-12 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 23d0a751-c36a-3c7e-b4ec-417272a85cf0 | -13.6773 | -43.8662 | 2025-10-12 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 281.5 |
| 4ea2f6c7-8209-33f4-9df7-dcc8200ff19f | -12.5089 | -47.4362 | 2025-10-12 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8043f50a-115b-3677-a3f7-9085bdc58508 | -14.0155 | -43.4943 | 2025-10-12 00:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 40c8822b-a07f-34cf-9463-21da1d4f0d55 | -19.0319 | -57.5382 | 2025-10-12 00:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 149b4141-02e2-357a-93f6-047735a73266 | -13.6773 | -43.8662 | 2025-10-12 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 843051bc-9811-301d-b4f8-be9d90bfb876 | -2.5423 | -47.811 | 2025-10-12 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 1afaf96d-e661-334b-8064-1036f3b5cba0 | -17.5897 | -42.4246 | 2025-10-12 00:50:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 148.2 |
| fecdb00d-20b4-369c-9bfc-1ed709f73818 | -7.0664 | -45.2294 | 2025-10-12 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 9ae6792f-5058-3a3a-8b1c-36289905b8e5 | -7.0476 | -45.2311 | 2025-10-12 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| f9ec6117-824a-3563-8759-5c8b103251c7 | -14.0351 | -43.4906 | 2025-10-12 00:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |


[Clique aqui para ver as próximas entradas](README7.md)
