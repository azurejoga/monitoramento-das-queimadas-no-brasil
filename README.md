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
| e655ef21-2f77-3585-abc8-eb011472c83e | -4.279 | -45.6485 | 2025-11-05 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d450a33d-5084-3afe-b63e-dc5d4fb96f19 | -18.5121 | -53.4856 | 2025-11-05 00:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e089d32d-11a8-36e4-a1af-3f9a1d034488 | -3.49 | -43.6152 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 883.9 |
| 50f93914-efba-3b1f-8750-a962732c0adc | -3.5085 | -43.6374 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 377.5 |
| eb3c1106-b639-3ddd-93b4-8f7537285a14 | -2.6508 | -48.52 | 2025-11-05 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 31fdc446-4d69-3381-8597-a19a2a681883 | -3.4898 | -43.6614 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 205.4 |
| c7fd167f-6ec5-3af0-8a3a-cd8d92fab687 | -3.4711 | -43.6623 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1265b0ec-58b5-30d4-8c14-6d22c8359bf8 | -2.6509 | -48.4985 | 2025-11-05 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e425fe3b-7694-372f-a71b-3c6c83e896c5 | -3.4712 | -43.6392 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 688.3 |
| be1b6f44-f505-3825-b261-e6e1aa44f063 | -4.5934 | -43.3239 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 641b7465-3409-309b-919e-00ed5c873ce5 | -8.05 | -49.6325 | 2025-11-05 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 103cd7ff-2201-3921-9dd7-792f72959e68 | -4.4819 | -43.2374 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 491.3 |
| 7572b39d-1209-31bf-9cf6-ac4c8e60763d | -3.5087 | -43.6143 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 198.4 |
| f6cd0498-2b5f-35bc-8bdf-61c9ce4911e0 | -4.5747 | -43.325 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 51a0d3fd-17c6-30e5-9c00-575f489c7b8a | -3.4899 | -43.6383 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1266.2 |
| 63d8b266-ff5b-3f32-aa69-6951a93f9bc0 | -4.426 | -48.9251 | 2025-11-05 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f1e63944-0975-3942-9fca-8d9b0a37ce7a | -4.4632 | -43.2386 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 479.9 |
| 15aa7abe-aa84-3d41-9182-b8cdc55be54b | -4.5932 | -43.3471 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 7b12f14d-8dd3-3bab-8f11-ca70779b6466 | -4.4633 | -43.2152 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 536.3 |
| 9edcde70-1c89-30d7-a31f-7049210b1b0c | -4.4446 | -43.2164 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 493dd4c1-0de6-3eb1-85a8-8fcf9178fe95 | -4.482 | -43.2141 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 294.8 |
| 73b160b2-46ed-3600-ae95-bc8a9fb31253 | -18.5317 | -53.5039 | 2025-11-05 00:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a4fa1e84-ce8c-3d92-a9f0-831a182ea308 | -11.8473 | -43.7256 | 2025-11-05 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c6eaf7d2-e2e0-37dd-be1e-f5e7ff5e74e1 | -4.4445 | -43.2397 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e4702b45-a8d0-3139-8c7b-b7f019d00785 | -10.1111 | -44.7652 | 2025-11-05 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c026b402-e888-3489-af73-cbc090687fbd | -2.5716 | -44.9321 | 2025-11-05 00:00:00 | GOES-19 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2b63eade-c01c-3cc5-bcc2-8cd145528aa9 | -2.7922 | -50.2986 | 2025-11-05 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 1637299e-5243-32a7-aac9-6948571fbfd1 | -4.4075 | -48.926 | 2025-11-05 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 32f2e6b2-d301-3c24-87d4-bca4a3fd52ad | -4.4258 | -48.9679 | 2025-11-05 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| aacd660d-2646-37a3-9b8e-9cbca67d2f3b | -5.4553 | -45.3988 | 2025-11-05 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 510dd686-23c1-3689-8406-e0f8b50f1a5d | -4.5745 | -43.3483 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c24a28b0-22f0-38e9-a01c-394013f72138 | -2.7921 | -50.3196 | 2025-11-05 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| bae2e1d0-865c-3c70-b724-126000bd9ea9 | -4.4073 | -48.9474 | 2025-11-05 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| d1e49cb2-e7da-3f9a-b578-5e347da42113 | -4.2789 | -45.6709 | 2025-11-05 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c815795f-86b8-3a76-9b48-e69ecd42c258 | -3.4714 | -43.616 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 340.4 |
| 42f6e66f-cec9-3142-9b92-6905033cf84d | -18.5117 | -53.5071 | 2025-11-05 00:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 8a26f37a-9d11-344e-bb27-a891ecd75cf8 | -3.4901 | -43.592 | 2025-11-05 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 5a7c0a74-b326-3e28-9f9f-6f2fa37cf386 | -4.4259 | -48.9465 | 2025-11-05 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 91a78d62-e0c8-3961-9868-df33e0a635fd | -4.4635 | -43.1919 | 2025-11-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a118620e-21c1-397e-b27f-39c4fde1388d | -4.4635 | -43.1919 | 2025-11-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b6b78879-badb-3ca9-a2df-e949585c45bd | -4.4632 | -43.2386 | 2025-11-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 424.7 |
| 544de0dc-7b7d-34c1-a2d5-5e559861e7e9 | -9.7745 | -36.395 | 2025-11-05 00:10:00 | GOES-19 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| 3fd497b4-4d34-3c58-99aa-391a2a2d4d8d | -3.49 | -43.6152 | 2025-11-05 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1107.5 |
| eb04bf38-3725-3d62-bab1-9da9a878c629 | -4.4446 | -43.2164 | 2025-11-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| edc3d3b8-0dbc-343a-9af1-743ba12254ea | -11.8473 | -43.7256 | 2025-11-05 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 29f2730b-90a7-391d-94c0-92c5b8c2c437 | -4.4445 | -43.2397 | 2025-11-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 510f65fe-8642-3bfc-b8dd-fd65cf30a7c3 | -3.2317 | -46.8716 | 2025-11-05 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 02148460-013c-3ad1-be27-f20f9b9bd736 | -5.4553 | -45.3988 | 2025-11-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 1f3becab-c2e8-3c39-9c34-d6847c90ba7c | -1.2822 | -49.168 | 2025-11-05 00:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 62604d40-8b4e-3960-8425-8a5f44f74a7e | -3.5087 | -43.6143 | 2025-11-05 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 36b00f7b-f768-347c-a279-ee0999e495bd | -1.3006 | -49.189 | 2025-11-05 00:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 3a3ecd5c-f625-393d-80c2-1c4934209f01 | -4.482 | -43.2141 | 2025-11-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 340.5 |
| cff311d0-6b5c-30dc-b571-bb1f76b8dffe | -3.4899 | -43.6383 | 2025-11-05 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1355.3 |
| 0fb0bff4-2158-3bd9-9464-c3587d6071ed | -18.5117 | -53.5071 | 2025-11-05 00:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 119.5 |
| e78f4838-d749-33e0-b2cd-2170765835de | -10.3833 | -44.3826 | 2025-11-05 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a11d5556-a78c-3117-a533-07335995c930 | -3.4712 | -43.6392 | 2025-11-05 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 502.5 |
| 99b0be46-722d-3821-8eec-eda5d9c9279e | -2.6508 | -48.52 | 2025-11-05 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 48f3a2c5-c18a-362b-a32d-61534801dbfb | -4.2789 | -45.6709 | 2025-11-05 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 00487e0d-17e1-3bc7-9d57-9b53308ae7f6 | -4.4633 | -43.2152 | 2025-11-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 584.2 |
| ea05c2be-5b1e-3d31-9233-4c7118389e6e | -4.2975 | -45.67 | 2025-11-05 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 280c4b3f-bc33-3259-b134-a1a94d86efdf | -4.4819 | -43.2374 | 2025-11-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 401.5 |
| a7a9cb93-dfa1-3d8f-9cd2-8ba20dde2e56 | -4.279 | -45.6485 | 2025-11-05 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 13fe8d24-88e8-3fff-b20b-e6af551b8f91 | -8.8328 | -50.014 | 2025-11-05 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 56e86ac2-ebf6-3fdb-905b-27d32809c859 | -10.4024 | -44.3801 | 2025-11-05 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| be6e534a-ab94-3461-b7c4-0a2fef9700cd | -3.5085 | -43.6374 | 2025-11-05 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 251.5 |
| 53c26625-94ff-34ea-83c6-5b611298892d | -1.3006 | -49.1677 | 2025-11-05 00:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| b360e5ea-d8d7-317b-9271-ac787e45e6ef | -2.6509 | -48.4985 | 2025-11-05 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 39cb2354-9a81-3399-befd-a158f1d98411 | -10.4215 | -44.3775 | 2025-11-05 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ba54af37-19d8-36a0-aaf4-786b4bbd5205 | -8.05 | -49.6325 | 2025-11-05 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a94b8652-2d64-3a68-a271-3c044fbf552f | -10.4028 | -44.3568 | 2025-11-05 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f74bb134-d9ed-395d-914a-8b0a074747b0 | -18.5317 | -53.5039 | 2025-11-05 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ff407b2a-8034-3add-b1b9-b11dee818fb4 | -3.4714 | -43.616 | 2025-11-05 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 344.5 |
| 57096b97-8e19-32c2-ade7-e5f8375c6388 | -2.7921 | -50.3196 | 2025-11-05 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 56e46247-46d9-3519-a830-2af11e5634e4 | -3.4898 | -43.6614 | 2025-11-05 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 0a0a654a-79e8-3167-930b-4510d3b6c3c7 | -2.7922 | -50.2986 | 2025-11-05 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| cd14e9ac-566c-360f-8374-48369aff64c3 | -1.2822 | -49.168 | 2025-11-05 00:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 53e1b752-1467-39ef-962e-50dd12c7552d | -4.2977 | -45.6475 | 2025-11-05 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7a18b676-7f0d-3737-9f11-40e4d5387cd0 | -5.4553 | -45.3988 | 2025-11-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 251.1 |
| 208e15e8-19da-3611-bcca-eaa171f684ff | -3.4711 | -43.6623 | 2025-11-05 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| f1e29c49-bea9-3b08-a0e8-dc53b49d1e6a | -4.279 | -45.6485 | 2025-11-05 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 51021896-1c4e-313c-b123-43024a56dde0 | -11.8473 | -43.7256 | 2025-11-05 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| f49b2adf-9f29-3d67-9e50-0093b9398b59 | -11.2956 | -44.5809 | 2025-11-05 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| c8e1034d-ff5c-3f56-bea0-2a1cc3e360b6 | -3.2317 | -46.8716 | 2025-11-05 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 3ef829a8-7e58-3b92-b96a-68861c941e18 | -4.4632 | -43.2386 | 2025-11-05 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 395.5 |
| 1eceb9d7-533a-34e3-8752-25c0640beb15 | -3.2503 | -46.8709 | 2025-11-05 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5e863c21-2b15-3b30-ba43-cc65ff77375c | -9.9208 | -44.7893 | 2025-11-05 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6f764c25-f4a5-3222-ba37-b3f4592400a7 | -3.5087 | -43.6143 | 2025-11-05 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 6ae721b9-07b0-34e5-8e0d-f2d1ff512773 | -10.3837 | -44.3593 | 2025-11-05 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c584e0d3-f76f-3d7f-8173-7de53b628e2c | -8.2335 | -49.98 | 2025-11-05 00:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8700b9fb-612e-341d-8e70-d0c7e2bc55c6 | -11.276 | -44.607 | 2025-11-05 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 47504e49-59b8-3274-a808-eb277eb374da | -3.4898 | -43.6614 | 2025-11-05 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| b9b44ede-e292-3193-95d1-f0f4ae73b456 | -2.6509 | -48.4985 | 2025-11-05 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 43c197a2-dc26-3989-adf3-29864f00aa78 | -10.3643 | -44.3852 | 2025-11-05 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 305c86b8-b93d-3597-8b32-c929109b23c3 | -4.4445 | -43.2397 | 2025-11-05 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 6a4fddd4-b873-3403-bac6-9d5cb9345611 | -2.7921 | -50.3196 | 2025-11-05 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f4193335-650b-32d5-bfe5-55a573953d87 | -9.9205 | -44.8124 | 2025-11-05 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| af390e07-a8a6-3c8c-b0a2-23542f2307b0 | -4.4446 | -43.2164 | 2025-11-05 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 50a6dee3-ae50-3d6a-8e1a-a8cf14f5069b | -1.3006 | -49.189 | 2025-11-05 00:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4cd79b36-e830-3d17-a2d5-742a7f92980f | -11.2756 | -44.6302 | 2025-11-05 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 2627cdca-3528-329c-8a61-2b7b3a1d8122 | -4.4633 | -43.2152 | 2025-11-05 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 511.1 |


[Clique aqui para ver as próximas entradas](README2.md)
