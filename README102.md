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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35dfdfce-257a-3a7a-bc5a-59b4235ebf1b | -10.8626 | -57.16185 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cdfcd4c-a66e-3ef7-8a83-9cdce85312ac | -9.55227 | -66.01837 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bd4ff91-7d8e-37f1-b388-fc6a2d84f860 | -9.68507 | -54.33863 | 2026-09-21 05:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ed3620c-867b-3865-a7bd-7e7508976e1e | -10.87558 | -54.0737 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12479b8b-ee09-37bc-aa4a-cf8b2e47c7a6 | -9.82698 | -65.00863 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 928065f5-f74b-3459-8c05-9364329b766f | -11.99326 | -58.06924 | 2026-09-21 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b427d6b9-371e-3e1b-baf9-3f0625f82723 | -16.01647 | -52.53236 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13572b84-1395-3f78-920d-88984febc931 | -10.6201 | -67.92891 | 2026-09-21 05:44:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dffdef7c-b062-366a-8733-43fe5ae32582 | -16.0534 | -52.51851 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe50b519-6082-337f-a756-b4b1df46b003 | -10.20874 | -68.74892 | 2026-09-21 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ca509d2-84f2-34f0-97c2-ca89ea087429 | -12.83368 | -54.05775 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| c15e720f-1b1d-32d5-b86b-14d421863585 | -16.3965 | -54.72093 | 2026-09-21 05:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e1aaff9-7ba1-3747-a79c-e1e47af5808d | -16.05005 | -52.51485 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 94db6b03-005c-35f4-877a-49cf780a40d8 | -16.04376 | -52.51421 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0ca32281-1d27-335d-8b41-75d219d5beb1 | -10.09844 | -64.33107 | 2026-09-21 05:44:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e5013e0-09fa-3f56-88e9-64bb5837f4d1 | -11.99584 | -58.0687 | 2026-09-21 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b48aed3c-cee0-3227-b21d-597da091262b | -10.89067 | -69.34406 | 2026-09-21 05:44:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6011dd61-4335-3081-9ca6-68ebeb917383 | -11.74739 | -54.571 | 2026-09-21 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c324cb2-0f25-3658-9404-eb882aede527 | -11.98448 | -58.07187 | 2026-09-21 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd6c3b1e-b9c2-3877-8962-d42d6749daed | -14.6551 | -54.45696 | 2026-09-21 05:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c018548-925b-3041-9d9b-14a9b4c64e2b | -9.22493 | -71.87215 | 2026-09-21 05:44:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adef8a93-9fe7-3b3b-a3ae-fcd38cc4364e | -16.3222 | -53.84209 | 2026-09-21 05:44:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 464d3926-c5fe-33cb-b265-0a2ff3229933 | -12.83458 | -54.0506 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ea5fdd23-bd36-3c52-b314-379e930308eb | -11.72041 | -54.57368 | 2026-09-21 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d64f36-9dd8-3e90-9fd3-1896881c0f8f | -13.34343 | -51.81312 | 2026-09-21 05:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ce9250f-3485-378e-a625-565d04778a35 | -12.83478 | -54.04919 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c6b95b8c-5c87-3f8c-9cba-9ce92c4afdcb | -12.80087 | -54.05352 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a967d10-e381-30e7-b10f-e63b44c262b4 | -12.83436 | -54.05278 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| c6b9ee79-ebc7-37b8-b247-bf920b8da6ea | -12.30601 | -49.18943 | 2026-09-21 05:44:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e18bc774-09dc-3a94-b3f9-34ae8856cc48 | -9.64474 | -67.49142 | 2026-09-21 05:44:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70b04b07-cbd6-34a9-8a93-72ea3e70dd0f | -11.99534 | -58.07244 | 2026-09-21 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c0e75e14-9c9e-3e6c-83f4-b53048409924 | -16.9967 | -56.45632 | 2026-09-21 05:44:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 38f631e4-ccf5-30a3-8318-a207503f8e46 | -12.77118 | -52.85027 | 2026-09-21 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33b5e380-9ccf-3465-b2b9-116f11eedb9b | -16.04951 | -52.51997 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b7bc1906-d0fc-3e04-b4fc-bd9af5392c73 | -10.47069 | -69.19833 | 2026-09-21 05:44:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18f1d771-5c00-3f02-b1d2-dede04ebdf66 | -12.9188 | -50.97146 | 2026-09-21 05:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c1f5466-515a-3ece-99f0-76ff894d7f4d | -11.99273 | -58.07301 | 2026-09-21 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ed5ce59b-cac7-348a-a353-2c5888cb80a4 | -14.66978 | -54.47318 | 2026-09-21 05:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0441849a-13f5-3c8e-be48-88d31efe9117 | -12.80043 | -54.05708 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f457863f-51e2-322d-b36e-e65f6ab9689c | -11.72082 | -54.57058 | 2026-09-21 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74421f15-0fe3-3af8-b498-3cb2c81a195e | -12.77707 | -52.85119 | 2026-09-21 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83ff46ef-7afb-3f24-a948-16cbeb8ba1a2 | -16.038 | -52.50851 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fa3a3866-02a1-3df4-8ea6-f317a5014f2a | -9.89276 | -66.98337 | 2026-09-21 05:44:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c48dd477-b912-3c7b-97ab-c3ac6112b3a9 | -16.01125 | -52.52142 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d3d1fb6-3ab6-3a4c-9d86-49d0d3a7714e | -12.77066 | -52.85452 | 2026-09-21 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7db77299-d507-306b-9139-14aeee869a02 | -14.93037 | -49.89966 | 2026-09-21 05:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b368d062-f377-336b-a6be-4b1c4b08322c | -12.83413 | -54.05418 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ef1bbb6e-0ac4-3e8d-872f-9cdf2389ddcc | -12.32074 | -50.69528 | 2026-09-21 05:44:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85650fc7-3fcb-3599-aefa-22a3c630d289 | -16.99899 | -56.51978 | 2026-09-21 05:44:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 12b0e4da-76bc-3735-90fc-a0564ecc15b8 | -16.39689 | -54.71739 | 2026-09-21 05:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d9b98af9-e184-3d75-9d6f-0b93cd3ed4cd | -11.9886 | -58.07244 | 2026-09-21 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edd64030-5ffa-3d9d-b435-eece8b9b032b | -10.92944 | -61.41225 | 2026-09-21 05:44:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 393da498-31f4-3aa5-8abd-93d923292eb1 | -11.7526 | -54.57169 | 2026-09-21 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c160a46f-3eeb-3ec3-91cc-940c8036ca49 | -12.83393 | -54.05637 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 0cf1f0bb-029e-3ed3-a836-f8630746b762 | -11.753 | -54.56855 | 2026-09-21 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b88472c-09e1-38dc-836a-94b35002834a | -16.01592 | -52.53761 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d05e50c3-d1da-3a0c-bd46-183af87b976e | -12.76844 | -52.84923 | 2026-09-21 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 210fb13a-311f-3634-baf8-4ef57bf9adb9 | -12.76795 | -52.85351 | 2026-09-21 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b9596ad-94fd-3929-a2d8-9d6bf406ddf0 | -12.8291 | -54.04996 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a91d258f-1d0a-3c28-b6eb-7b26a2f869ca | -16.31631 | -53.84225 | 2026-09-21 05:44:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825d3c23-805f-30f5-8fe2-b1dd50bf864e | -14.66434 | -54.47242 | 2026-09-21 05:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83a8ef57-1772-35d9-a042-e7aa1553768f | -12.82362 | -54.04929 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1354c29f-8978-3bf9-a1a6-543a7cce8e49 | -15.75706 | -56.44799 | 2026-09-21 05:44:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10962fc2-db00-36c0-9303-c7ea3deaa3ab | -16.01072 | -52.52657 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5d354aa-4733-377e-8ab0-1521fc55a487 | -16.03747 | -52.51361 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b21c74ec-d3f1-33e6-acd4-9d3844e24bba | -12.81268 | -54.04788 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03acf58c-7eb7-33fb-9f0b-0342ea98275f | -14.6509 | -54.44555 | 2026-09-21 05:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87e96d74-6c62-3d10-8b2d-c27f4993aa83 | -11.99121 | -58.07187 | 2026-09-21 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cbeff6ce-cc94-3b0c-935b-75abc1bddbea | -12.82888 | -54.05212 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 8ab210e3-d4b8-3e97-9ecc-62bbed3a3a13 | -10.93344 | -61.40908 | 2026-09-21 05:44:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0d601e3-233c-346a-86f3-295365511f66 | -12.8293 | -54.04854 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f6801954-7f1c-3b27-86f9-5f0e0a8193a6 | -10.10354 | -69.13294 | 2026-09-21 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c961b12e-473e-3ec7-9b97-1194923b3ed6 | -10.09785 | -64.33471 | 2026-09-21 05:44:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42fd7079-e427-3488-b442-60ae688e59e0 | -12.91216 | -50.97064 | 2026-09-21 05:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4330a172-58e8-3cdf-99f0-fe258897aa74 | -12.82865 | -54.05354 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ea88cf3b-7dfa-3c94-bedf-d65cf7d99e1e | -12.82845 | -54.05571 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 869781f1-6196-3033-8820-20653a3af8b2 | -9.42509 | -68.75911 | 2026-09-21 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59459e4f-e0e7-323c-8764-0b5aa48163d4 | -16.03117 | -52.51308 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d3d251f6-4d4a-3f64-8122-86cd0caf82d2 | -12.8282 | -54.05711 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f47ab54e-a5aa-3689-adf2-2a4326e835fd | -9.22025 | -71.86795 | 2026-09-21 05:44:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b815ba0a-f22b-3e67-90fd-064e4d785f1b | -9.67214 | -66.82493 | 2026-09-21 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a534baef-83c1-35cb-8a16-4f51379f7078 | -14.66937 | -54.47659 | 2026-09-21 05:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d648c44b-108f-3ccd-b4a2-db7409286da3 | -16.0317 | -52.50797 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d03751df-53e7-3487-8335-6e205a09d8ff | -12.82318 | -54.05286 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7cdf88e9-4796-37dc-aef5-4557b8634dae | -14.65591 | -54.45 | 2026-09-21 05:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca0d9e6-9e30-3112-b22e-6b6ccd2ffb6d | -11.97288 | -63.13518 | 2026-09-21 05:44:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 442911b9-f793-36ce-aed3-de25c56858f4 | -11.91392 | -63.27055 | 2026-09-21 05:44:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b3641dc-928e-3d51-83c2-e45bad53f5b4 | -14.67486 | -54.47697 | 2026-09-21 05:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cafa9f84-750e-358b-abf5-34ae6432d2ee | -16.04847 | -52.52984 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 416adfb5-517e-31c7-b2ef-652ed0ee407a | -12.81815 | -54.0486 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 435cb77d-ef52-3a7d-8e51-2a1fb063df3f | -10.93287 | -61.41278 | 2026-09-21 05:44:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9742adba-8648-3c92-a4a0-d0126f18b516 | -14.92329 | -49.89732 | 2026-09-21 05:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 40d54de6-885d-3cde-b1f0-315d79c717ef | -12.77434 | -52.85008 | 2026-09-21 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdfd23e6-a8e8-3967-bb42-ba57f98fee90 | -11.0368 | -68.49944 | 2026-09-21 05:44:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6a128d7-58a4-3f7e-ab18-b8cb54d85adf | -16.05391 | -52.5134 | 2026-09-21 05:44:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0a7a40b-3d3e-37da-affe-4d488a6ff3ce | -10.62407 | -67.92965 | 2026-09-21 05:44:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aefd8492-2f8c-3599-8925-7189ae048917 | -12.81859 | -54.04504 | 2026-09-21 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd43b0f4-1cc1-3786-bc48-5efd3f471ecb | -12.30683 | -49.1819 | 2026-09-21 05:44:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cc13945-ef40-3e85-89fa-1f237b0df28f | -14.6555 | -54.4535 | 2026-09-21 05:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59ecc286-4272-389c-b489-ff44eb6a6f88 | -11.98914 | -58.06866 | 2026-09-21 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README103.md)
