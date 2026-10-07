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

## Dados Diários - Página 247

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb763255-6fdf-3971-86cf-6edc72fb4d9c | -4.3747 | -55.1683 | 2026-10-07 18:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| ede63c67-91bf-3217-9263-dc6df1fbcd4f | -5.496 | -42.8178 | 2026-10-07 18:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 896929c5-68db-35b7-811e-3d991bbdc276 | -2.0026 | -56.9575 | 2026-10-07 18:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8aec226b-9afc-3e99-8799-2a7b11e05626 | 1.6937 | -55.6461 | 2026-10-07 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| b9819f37-c41c-3541-b5da-3a3bab2dfc57 | -11.7362 | -43.5068 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b50e05b6-ec93-3c2c-9e45-e8ac3ee2d49a | -5.4958 | -42.8413 | 2026-10-07 18:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 220.9 |
| 3b860b41-efc8-3910-9def-d8d43dfa0b60 | -5.9835 | -40.9367 | 2026-10-07 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 185.4 |
| 8fc005b4-be02-37aa-a17f-3c995a40dbef | -9.0407 | -65.9215 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 75190fe6-92fd-3ed6-a2e4-ec0958db1ac0 | -9.806 | -65.0167 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 13b95c40-74fa-3b24-9038-447dbcf0bcca | -8.6118 | -66.7334 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 20fab4e2-875e-3e57-b4a3-641d98f69701 | -9.96 | -43.481 | 2026-10-07 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 97c178de-28ee-3ab2-9193-9795a3ed59cc | -2.7043 | -49.0533 | 2026-10-07 18:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| a7d97c8c-ad29-38f5-a941-fcba2210ee2c | -9.0592 | -65.9209 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4dec8dcf-732f-3f27-a4da-fa908fede638 | -6.9331 | -43.6566 | 2026-10-07 18:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 0c51d388-a7a1-39d9-927d-fe35dbc4ca04 | -3.0375 | -53.9066 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 266.1 |
| 8e472fc6-57aa-31e8-a839-d0b6d69caace | -7.9178 | -70.9245 | 2026-10-07 18:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 109.6 |
| f686162e-2062-3e6f-8047-c08f2d1c14ce | -6.6037 | -53.0321 | 2026-10-07 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 140.3 |
| c7f24e25-bb69-358f-ada1-14f56c49ffa8 | -13.3671 | -43.8742 | 2026-10-07 18:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 302.8 |
| 84d6d0fd-b5b4-304d-a49d-0df52ed8483d | -6.1973 | -52.85 | 2026-10-07 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| b4e0670d-bf07-3e1c-b035-2e85df10e5ea | -1.801 | -57.1161 | 2026-10-07 18:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 225.5 |
| 61726e06-7c86-3e5f-a751-6fbada389041 | -13.3865 | -43.8708 | 2026-10-07 18:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 20b4c183-3ab0-3d69-9069-e43ff94b24ea | -4.3045 | -50.77 | 2026-10-07 18:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e0212e18-6987-34a9-9993-842274f2d204 | -9.4509 | -45.8271 | 2026-10-07 18:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 3775b7ca-bade-3f21-9027-4a2ffa386e46 | -2.9271 | -53.9295 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5ad62bf8-02a1-32a2-9580-dbecb6aa159d | -5.8204 | -53.8457 | 2026-10-07 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 731e073a-6779-34f1-8619-417d547f5d92 | -2.6859 | -49.0539 | 2026-10-07 18:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 8278af78-87ec-3800-88e4-15906ab52983 | -11.7331 | -43.6727 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 13dcd62d-cf93-3844-a539-8fa386da57db | -6.6223 | -53.031 | 2026-10-07 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ecc21722-8b40-385a-95a4-5b4a53df5120 | -7.6802 | -70.086 | 2026-10-07 18:20:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 7b3b676c-cc71-3cb1-ac47-aff200797737 | 1.6385 | -55.785 | 2026-10-07 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c03be26e-45fe-3f61-adc1-a356e392c04c | -4.3044 | -50.7909 | 2026-10-07 18:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b27c5233-1be9-3846-ba1c-4be2e8630b5c | -5.9838 | -40.9123 | 2026-10-07 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| be54a656-3136-3d70-b6b8-5c0926071e70 | -9.7126 | -65.0951 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a48d4b87-7478-34bd-89ff-593ee648de60 | -11.7335 | -43.649 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 2ed61bf0-e992-3477-b42d-51bafdf0113a | -8.8696 | -67.0049 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 58b666ce-b270-3d57-b01d-c154773de44b | -4.3471 | -43.8021 | 2026-10-07 18:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 4b21ea5e-2b67-377a-af23-a8d9b4f97a26 | -12.0457 | -43.3864 | 2026-10-07 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 240.8 |
| de15c07c-8c12-3d66-8403-d43f7ee59595 | -9.0987 | -65.3783 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 53c90ea0-ef05-3b70-a45f-b53a93f59712 | -3.2398 | -53.8813 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 16b6620f-4c71-34e6-a48f-f30701b96065 | -5.5148 | -42.8164 | 2026-10-07 18:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| c6377f0a-32cd-3bb3-8b56-248b1974e1f6 | -5.7376 | -45.1533 | 2026-10-07 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1265.4 |
| 63d951a5-bb80-384c-b20d-16365d62f741 | -1.8011 | -57.0967 | 2026-10-07 18:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| db689721-c2b0-3723-850c-daf922184fa0 | -10.4594 | -46.8333 | 2026-10-07 18:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 18d5e070-c6ac-345b-a5b9-0358b367a2ac | 1.7671 | -55.5859 | 2026-10-07 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d003d1b2-b2aa-3259-9c75-9ab7f2bd8ce7 | -3.5875 | -54.3138 | 2026-10-07 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 017f487c-d7e4-300f-ab99-b9a6f0e5a10b | -11.8503 | -43.5598 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| e33603dd-dfc7-3dc0-bcd3-607891977bec | -3.476 | -54.6172 | 2026-10-07 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 41f2b3ef-951c-3dd1-8527-e6b20328702e | -9.1711 | -65.7682 | 2026-10-07 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| f12fb1ce-3f79-30a8-b44d-f6f818fe0009 | -3.0932 | -53.7239 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| be94605c-e44c-3583-a0fe-9b39490faba8 | 1.6385 | -55.8047 | 2026-10-07 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| e6e99f53-fd3d-3a37-9ba4-61e080d3addb | -2.8712 | -54.192 | 2026-10-07 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 1cd28803-e77a-3a13-b698-212c9c635a04 | 1.7121 | -55.6063 | 2026-10-07 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7cf080e2-136d-3a94-a5b0-e6cd2c8a9329 | -7.3085 | -73.0269 | 2026-10-07 18:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 0eee51c9-1aae-3d46-a25c-d9db670c9d3d | -5.9649 | -40.914 | 2026-10-07 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 153.9 |
| 8297e2f0-d2e4-3673-ac2d-139ff828d199 | -6.1747 | -53.4224 | 2026-10-07 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 65f03cbe-bd7c-37d6-b1a6-973cd1481d0c | 1.8768 | -55.7227 | 2026-10-07 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| f31b8b7a-a396-3040-9619-ae82f298592f | -17.4361 | -43.6393 | 2026-10-07 18:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 74d60194-6b65-38af-a422-9bf54fd5d896 | -6.1429 | -47.9432 | 2026-10-07 18:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 9fd0ce37-483f-38ef-a386-c32d6d973b80 | -6.8292 | -39.5472 | 2026-10-07 18:20:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 94903dbe-de2e-3bd4-aba7-a4e4afc83d81 | -6.2714 | -52.846 | 2026-10-07 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 0c4cdc6b-a741-381d-b956-b044667cef07 | -3.2213 | -53.9019 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 058c2e1a-2855-3f7e-aa0c-5c083d05571c | -9.7312 | -65.0944 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ca64ddcf-6735-3ba2-b3ae-48fa98b6b0b8 | -3.2951 | -53.8395 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1ecd4407-c0ed-30ef-9a3a-8b2bd4e4a46a | -3.2231 | -53.4174 | 2026-10-07 18:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 90fad9ed-ddec-365c-b575-15131bb2347f | -3.4762 | -50.0883 | 2026-10-07 18:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| c1cbb296-9fe8-3f7c-9b8d-6bbd2191dfff | -3.1114 | -53.7839 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 303.3 |
| 8fc5d434-cc71-33ab-a74f-1752b1d36573 | -5.2473 | -50.9149 | 2026-10-07 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 45a9cee4-2ad3-34d6-a071-c18b032e2d20 | -3.1787 | -50.5597 | 2026-10-07 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 200.0 |
| 6dbb2378-d6ae-3555-938d-7e24f2b4734a | -11.6946 | -43.6787 | 2026-10-07 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 0399aeed-ea01-3099-b9d7-c9edb8853e3e | -9.1076 | -67.7215 | 2026-10-07 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 11e51f07-89f2-3de5-8112-84c0a22e350f | -5.2274 | -48.4113 | 2026-10-07 18:20:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 71.3 |
| daf19cc9-7073-3825-bd81-d84e9caee36b | -14.7595 | -40.9203 | 2026-10-07 18:20:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| 0ae577a2-7598-3cdf-82bf-58a279ccf7a8 | -3.5678 | -54.6547 | 2026-10-07 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 9e29ac89-4d1a-3813-be84-84487c22e8c2 | -5.7189 | -45.1547 | 2026-10-07 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 493.8 |
| a0902aef-e534-3f2e-9254-24d03713958e | -3.0375 | -53.8865 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4761c517-22ec-35c4-bf64-e74dd2df8721 | -3.3141 | -49.1409 | 2026-10-07 18:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e2560931-ef71-39eb-b265-e9d198ffcfee | -3.1206 | -42.9337 | 2026-10-07 18:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 8a55df07-8543-3bf4-b081-b1485a797b6e | -9.9205 | -44.8124 | 2026-10-07 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 246d9649-24b9-317d-a6cd-950e72eaaa8a | -9.8061 | -64.9979 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| cbfb3c8e-040e-32cd-8fd9-a68f0cbcf42f | -3.2944 | -54.0207 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 244.2 |
| 145971c7-0b93-33b9-9491-b3199a099d2d | -1.1094 | -54.1601 | 2026-10-07 18:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5ad49943-3e3c-3361-ad13-d85db05c13f6 | -4.2348 | -49.9749 | 2026-10-07 18:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 46f04dc3-d91a-3bfe-9c24-f8219a31e8cf | -3.3637 | -50.4701 | 2026-10-07 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| e22d00f7-cd78-32ad-b100-95b02727ef76 | -3.4944 | -54.6167 | 2026-10-07 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| acab1886-dd0a-3f6a-891e-caf8036f5251 | -5.7305 | -53.4446 | 2026-10-07 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a23bc9f5-aa92-3c36-8a10-ba8808971cba | -3.1697 | -58.6244 | 2026-10-07 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| ac75d676-b1b2-3d91-8038-18153e453bf2 | -9.9589 | -43.5516 | 2026-10-07 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 8020e68a-be06-39b9-96f4-1a961de51db3 | -11.2333 | -44.8678 | 2026-10-07 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 879ee122-c15c-3f54-92ac-b323a402fdd2 | -3.0192 | -53.887 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| da6b17b8-c75d-3e1a-8ddd-0a3ad31f0c67 | -3.5684 | -54.4946 | 2026-10-07 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 57923e5a-a7db-37d7-ab93-73b98ff3ef77 | -9.8245 | -65.0348 | 2026-10-07 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 690a3836-a04e-321e-a278-81cd13d75b33 | -3.951 | -41.5426 | 2026-10-07 18:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 118.4 |
| 2fe596ab-d6f6-3e05-867b-46249878f4f3 | -5.8773 | -53.6202 | 2026-10-07 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e99c6d9f-67d8-33e3-8e64-c73da745d2f0 | -5.9887 | -53.5538 | 2026-10-07 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b530fe78-74fc-3472-93e8-cb243bab5eaa | -3.1115 | -53.7637 | 2026-10-07 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 1cce2a67-3261-340a-9c54-69ceab46b09b | -2.0447 | -54.3085 | 2026-10-07 18:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| e74e2edd-25b6-3b5c-91c7-b539b925e4f0 | -3.0787 | -58.4334 | 2026-10-07 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 1ca6e3b9-8e5a-36ff-b9f5-26f0720ecfd1 | -8.2184 | -46.3396 | 2026-10-07 18:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 37b43b8b-86c3-38ec-83aa-4fd09e26d458 | -5.9644 | -40.9627 | 2026-10-07 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 191.6 |
| e3b03aa0-56ff-3dd3-8901-d68a6ec3697e | -7.3935 | -46.2144 | 2026-10-07 18:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 184.6 |


[Clique aqui para ver as próximas entradas](README248.md)
