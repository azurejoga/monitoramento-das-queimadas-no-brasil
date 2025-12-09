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
| 455adf39-924a-3d70-b5ef-505fde45030b | -4.3144 | -45.9375 | 2025-12-09 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 3925618b-fc07-3685-8e2f-0fa59c87bdbe | -3.4449 | -41.6653 | 2025-12-09 00:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 314.8 |
| b880eb57-a4bc-303d-aebd-3ec9bee32cca | -3.4451 | -41.6413 | 2025-12-09 00:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 235.8 |
| df6727c4-f146-369a-9f7f-65d84867302d | -4.1821 | -46.2782 | 2025-12-09 00:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 523d330f-d1bd-3f4b-8763-c7672f0328cc | -3.4262 | -41.6662 | 2025-12-09 00:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 225.5 |
| e2e39f54-a010-307b-aada-f0462367b7a3 | -4.2959 | -45.9161 | 2025-12-09 00:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 95651147-d55b-3b85-8953-c41a56ebba79 | -4.2958 | -45.9385 | 2025-12-09 00:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 0c9dd20b-86ca-3c1b-b3a4-0c30aa1a900d | -4.1635 | -46.2791 | 2025-12-09 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4021ff2e-c070-3b3f-a6e7-dae5be68d449 | -4.2772 | -45.9394 | 2025-12-09 00:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d89c28db-8f97-30c2-9141-5282e39a5b09 | -3.4449 | -41.6653 | 2025-12-09 00:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 284.0 |
| 695944ec-9ae6-384e-8869-5b252dd3ab07 | -4.3144 | -45.9375 | 2025-12-09 00:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| ab7110f1-7b7d-3575-ab48-fbf662dd10ba | -1.5293 | -45.812 | 2025-12-09 00:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 9d3c18da-49a6-33ae-b054-8981f489153a | -4.1819 | -46.3004 | 2025-12-09 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 05702adc-fcfa-3f76-80d5-152a5c2923b9 | -3.4264 | -41.6423 | 2025-12-09 00:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 192.6 |
| 9e5c34d3-fb1c-3f35-80a1-c986eb7e60f8 | -4.04426 | -45.64976 | 2025-12-09 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| a85fd6ff-d9a0-3632-aa6a-8e29f4591a4e | -4.59922 | -45.9915 | 2025-12-09 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 856faee0-9aa0-3c08-a1d3-408c91acf22e | -4.1702 | -46.28624 | 2025-12-09 00:32:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 29.7 |
| f03e5ff9-9a68-3927-a4d8-b67524cc8d9c | -4.18172 | -46.27808 | 2025-12-09 00:32:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 48675b5e-4f11-3e78-a5f2-1a8857778319 | -4.17058 | -46.27955 | 2025-12-09 00:32:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 0c327382-3e2a-38e2-a329-3c687198723c | -4.95812 | -40.52217 | 2025-12-09 00:32:00 | TERRA_M-M | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 30.8 |
| b23be02e-9df3-3727-86bb-9244a6a0e972 | -4.29086 | -45.92241 | 2025-12-09 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 849b2074-7203-3e35-bf5d-3d836350459c | -4.29307 | -45.93791 | 2025-12-09 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 341.7 |
| f0a2fa7c-eca5-3d49-88e4-36545c0712ab | -4.30233 | -45.92975 | 2025-12-09 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 95b7da29-12f5-3dc5-a16a-17ab375966e1 | -4.18491 | -43.81818 | 2025-12-09 00:32:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bb953478-64f1-308c-bb57-ec19dc8da49e | -4.29525 | -45.95316 | 2025-12-09 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 04b2e32a-0bfe-38b6-bf96-6595a6e52423 | -4.17274 | -46.29404 | 2025-12-09 00:32:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 40d926b4-7c13-3f7d-9a28-cb8742d03782 | -4.29097 | -45.9317 | 2025-12-09 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 299.2 |
| 209485b7-7c20-3b30-9d84-52b1a1efca49 | -4.29325 | -45.9468 | 2025-12-09 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 120.8 |
| aec86364-580f-3d65-a97e-f2a890e8019c | -4.18215 | -43.83478 | 2025-12-09 00:32:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| bc1732ec-95e3-3f3f-a45f-bba0fa74fd20 | -4.18385 | -46.29252 | 2025-12-09 00:32:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e139574e-cb68-3226-ab77-2550c672bb1a | -0.18824 | -50.23217 | 2025-12-09 00:34:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 54aa6bc0-1101-3b3c-a72c-2291fdf63052 | -2.5722 | -45.51128 | 2025-12-09 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5217e34d-dbc2-3a73-9979-36bd5dcb34a5 | -1.46512 | -53.46745 | 2025-12-09 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| e9f4eadb-d691-38eb-989b-74b30102af4b | -2.10465 | -45.37315 | 2025-12-09 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 23a405ec-a95f-3e16-9f92-f9909bde2bb5 | -2.33184 | -45.58348 | 2025-12-09 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 8e638eb9-38e1-3a3f-b766-c4c3ba84b3f9 | 0.76555 | -50.79971 | 2025-12-09 00:34:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c8c3f0ad-c2de-33da-b9b8-89c98c00a19e | -2.69895 | -45.66339 | 2025-12-09 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f1dfb451-93d8-3e29-9d62-c8f9228b315b | -2.32781 | -45.58957 | 2025-12-09 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 26f8bf08-7f49-33c0-bc28-a5eaf719c6c6 | -2.80147 | -45.48326 | 2025-12-09 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e1ae7dbd-f6cb-3612-a26b-01eb0f76fd10 | -3.84424 | -47.81958 | 2025-12-09 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 9ceb0d56-1348-3e22-bad6-8727b38642f4 | -3.23943 | -43.27723 | 2025-12-09 00:34:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7623d7a9-fade-3160-92a1-1db4e5e2a63a | -1.48392 | -53.53448 | 2025-12-09 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3e421174-49a0-31fe-9f74-16212b39fcde | -1.71993 | -46.18283 | 2025-12-09 00:34:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 25805125-b6e0-3928-8893-2a4a0ddc874e | -2.70147 | -45.68038 | 2025-12-09 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 2bed3171-dda0-32a5-955f-8c4564278b5f | -2.37183 | -45.85618 | 2025-12-09 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 46b5b542-2d26-3f97-a9cf-bab827e1de68 | -0.39427 | -51.98648 | 2025-12-09 00:34:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d48d4863-1b41-3e55-a412-0fad5a8f1f0c | 3.39148 | -51.26851 | 2025-12-09 00:34:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 47ad268a-ce08-3c04-8b3d-1aa4ea192e60 | -3.41082 | -45.42192 | 2025-12-09 00:34:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 4a5b8f64-347d-32f1-88b1-8af3b51d9218 | -2.70576 | -45.66815 | 2025-12-09 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f042e66d-e6e3-3af2-9275-b45c5633c96d | -2.54477 | -45.69833 | 2025-12-09 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| bb7ed03e-eaea-3d13-8d41-1ed33c2b4d79 | -2.56713 | -46.0153 | 2025-12-09 00:34:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1c784533-ac8f-3473-8588-6c683f51759e | -1.10155 | -52.24083 | 2025-12-09 00:34:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96eb09ec-022b-3ce4-b6d0-16fbd17ad092 | -2.03668 | -45.82695 | 2025-12-09 00:34:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f0121c8e-eb07-357d-9467-215657d9d068 | -2.74808 | -45.31608 | 2025-12-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 57437f26-22fa-3ce6-ad09-64a42f36a46e | -2.57133 | -46.02044 | 2025-12-09 00:34:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4e83c3d1-4ea9-36ec-b8c0-8e33c1c3dd46 | -2.32926 | -45.56592 | 2025-12-09 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e8cbab8c-4081-3b8f-92f5-deab5fcb664d | -2.11228 | -45.35903 | 2025-12-09 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 69901776-527e-3786-b7e9-b12a496e5b37 | -0.85191 | -51.96393 | 2025-12-09 00:34:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8f62685-9dd2-3a57-a21a-84706585bc1c | -2.08821 | -52.04483 | 2025-12-09 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5a233ed-8ec6-380a-bc74-1f09da40fe32 | -1.46647 | -53.47718 | 2025-12-09 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 8e44fedc-93c8-3e37-adf5-9b79c9ca733c | -2.73866 | -45.31106 | 2025-12-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f2a01214-1144-3ebc-8566-809207b0fbc2 | -0.32787 | -51.701 | 2025-12-09 00:34:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a7bc50be-9652-3d23-b9bd-0e1570f2df5f | -2.54724 | -45.71529 | 2025-12-09 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| ba265cc8-334d-3c46-b07f-7bee47fb80e9 | -1.07054 | -47.12354 | 2025-12-09 00:34:00 | TERRA_M-M | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e8bfe1d1-5aea-30a0-b014-867c0ec02b20 | -2.37606 | -45.7179 | 2025-12-09 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| e0d0eb0b-b20a-3a52-973a-e3f89670986c | 3.394 | -51.25018 | 2025-12-09 00:34:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dc5b3de4-6d5d-3b4f-a7c8-81c41f0ae608 | -1.91858 | -46.28733 | 2025-12-09 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 96a26cf7-eb2b-304d-bf11-c150690046ae | -2.53712 | -45.21006 | 2025-12-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8cfc0fd8-bc25-36f5-8266-68a3d676b8f4 | -1.5212 | -45.8159 | 2025-12-09 00:34:00 | TERRA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4126a73e-fcdb-3eb5-9301-98dd2f63f61c | -2.52915 | -45.22346 | 2025-12-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 19c257b2-07df-3e52-9f1b-a14f967c2678 | -2.37426 | -45.87279 | 2025-12-09 00:34:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 57200031-ec92-3504-9bcd-0c5a3d271381 | 3.39274 | -51.25935 | 2025-12-09 00:34:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 78250a12-78d8-3bd2-83da-15d543ac3c82 | -2.5416 | -45.22162 | 2025-12-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 38474574-887d-30eb-a491-d12d3c0c11f2 | 0.4938 | -51.17103 | 2025-12-09 00:34:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e410ab1f-8976-3e9f-a22d-1c6e2c7e5844 | -3.26939 | -46.09315 | 2025-12-09 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f2883a0e-e142-3967-bd38-8775b8fbcc5d | -2.32536 | -45.57201 | 2025-12-09 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 49fb4288-5be3-3325-9feb-7d1653cacfd0 | -2.09988 | -45.36096 | 2025-12-09 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 2c7fe4e1-868e-39d6-9ef4-a10c56036dac | -2.03426 | -45.81001 | 2025-12-09 00:34:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 300bb408-ed37-31b6-b6aa-9aa2c4246fc1 | -3.84591 | -47.83106 | 2025-12-09 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 3ad2e715-5eb2-31d9-b925-7385a4cae772 | -2.10194 | -45.35477 | 2025-12-09 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6abf1dbb-9755-38e8-a933-2eea799181cb | -1.51879 | -45.79855 | 2025-12-09 00:34:00 | TERRA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 0bf8b4f1-8d57-317e-b15b-98795e86f758 | -2.53974 | -45.22865 | 2025-12-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| a751caf8-9dfd-3c29-9c83-b92e453cf456 | -1.48254 | -53.52464 | 2025-12-09 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e4c1c381-ff78-3c18-afee-a9fc08f5d792 | -0.18695 | -50.22281 | 2025-12-09 00:34:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dae6f4ba-3e1c-3998-87a9-e056627a327f | -1.52579 | -45.80885 | 2025-12-09 00:34:00 | TERRA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 1e278bb9-0f10-308d-b482-2d673ece2202 | -2.70813 | -45.68511 | 2025-12-09 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1039a9c3-f7a5-3d08-8857-1bf6e2d7a158 | -2.11026 | -46.34279 | 2025-12-09 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 18233b14-1b79-3ebc-8e20-4904311d173c | -3.4262 | -41.6662 | 2025-12-09 00:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 194.6 |
| 0976fde7-d5cc-3a07-b344-c7e41ef192e4 | -3.4449 | -41.6653 | 2025-12-09 00:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 261.4 |
| 6fbb82f8-5b47-3544-98f6-324f5eaa733b | -4.2958 | -45.9385 | 2025-12-09 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 188.4 |
| a6926ca4-f1d7-341a-a792-574e32c7e9cb | -4.2957 | -45.9608 | 2025-12-09 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 19091261-d756-3b6a-ab94-d1b1749601f0 | -4.1821 | -46.2782 | 2025-12-09 00:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ecaa7273-7c66-3e91-b7a2-fd62158c993e | -2.2691 | -46.4614 | 2025-12-09 00:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 57d0c24e-8410-3bf3-99de-c650df7a4dbd | -3.4264 | -41.6423 | 2025-12-09 00:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 148.0 |
| 848ad02b-81a6-3368-8d87-b9009a9ffec9 | -4.1635 | -46.2791 | 2025-12-09 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0969de07-0777-364e-8e84-aa1621a7944c | -2.2506 | -46.4619 | 2025-12-09 00:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 05590e0c-d871-3ffc-8192-ae491ddb4f87 | -3.4451 | -41.6413 | 2025-12-09 00:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 200.0 |
| 81cd4c80-ea6d-3539-9eca-24be270e9aa6 | -4.2772 | -45.9394 | 2025-12-09 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 219fdf5d-0dd1-36a1-85cf-12a12fb145a5 | -4.3144 | -45.9375 | 2025-12-09 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e88bb32d-b88c-3759-8181-2ee5cbac8fcb | -3.4448 | -41.6892 | 2025-12-09 00:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |


[Clique aqui para ver as próximas entradas](README3.md)
