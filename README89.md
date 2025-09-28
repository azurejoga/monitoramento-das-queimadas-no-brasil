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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db73f0ba-abaa-3ec4-b740-cf49a25e5325 | -16.59055 | -50.66372 | 2025-09-28 05:21:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d35f555a-3b52-3044-ba3c-e471460a8661 | -15.46407 | -50.23165 | 2025-09-28 05:21:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cd6e6f5-2265-359a-aab0-4c999d6b48f8 | -15.94788 | -57.49008 | 2025-09-28 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38ac593d-8198-3636-be32-3f3047ce8529 | -16.9613 | -53.68533 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 231313ec-17de-320f-b172-71f9766664d5 | -15.44882 | -48.22754 | 2025-09-28 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c284bb5d-c593-3f06-9293-35499e1e7828 | -14.53408 | -48.4202 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f0bf0c2-047b-3cdc-9491-0a10bf160feb | -15.98433 | -59.50014 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c7cda33-0760-343a-b667-875f59cd9039 | -16.96068 | -53.69066 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 67cc9e51-1f09-3b91-9a6d-5521e6b1774d | -18.17849 | -53.33018 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f608fd6c-b74f-358e-8574-b278ac9913d4 | -15.03296 | -46.96841 | 2025-09-28 05:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b6c2476-d5ab-305b-90b5-b9cda4f9caa5 | -20.69349 | -50.71435 | 2025-09-28 05:21:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e67ef990-b3f6-347e-b855-7919d65b927e | -16.0131 | -59.4935 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 528d65da-75af-3c76-a49c-6fb129089560 | -20.99694 | -50.01308 | 2025-09-28 05:21:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b95544c1-764f-3d22-9b33-5e7dc9781d47 | -16.59018 | -50.66646 | 2025-09-28 05:21:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5e893b5d-7c09-3986-acfb-fbf4370d92d3 | -16.96484 | -53.69654 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b8185cf8-c1a3-373f-98b5-77b845b1fa83 | -15.2825 | -49.48561 | 2025-09-28 05:21:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5545900-64fb-3743-8c37-bd3436e5a730 | -14.3865 | -54.94196 | 2025-09-28 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09353182-8d4c-327f-a1ae-f0d6ea42b1da | -12.8897 | -62.09774 | 2025-09-28 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 600a13eb-c098-3698-ba02-5401d39e95b0 | -15.94088 | -59.51231 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97ea0dfc-1e49-3600-9701-e31d2d83da8f | -15.44272 | -48.22123 | 2025-09-28 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c46576e-6c49-3d97-865b-bffa81eda50a | -18.17407 | -53.32456 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 503199c1-04a5-3b2e-8886-dbf0b5feab53 | -20.69391 | -50.70958 | 2025-09-28 05:21:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 91c104e5-80b0-3ee8-b0c9-0af24c9e8178 | -17.75863 | -48.75109 | 2025-09-28 05:21:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 028ed557-8897-3508-ab9f-a053332007fb | -12.62219 | -62.01877 | 2025-09-28 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06dea4b5-1ece-3a31-81df-fd4e15de162f | -18.20025 | -53.31631 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a0a36fb-7201-3e49-bf58-1ae42aa21c19 | -15.99788 | -59.50244 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d500b68a-34a4-32aa-b1dd-ba6778819ad9 | -15.92896 | -59.49909 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 032103d6-4881-3586-9d98-728cd1c03ef6 | -16.95943 | -53.70134 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 13a98d9f-1078-3200-a8ff-448494fff6ad | -17.11651 | -51.16411 | 2025-09-28 05:21:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 747b124c-c7df-372c-81eb-c9db76e2c19f | -18.19459 | -53.32173 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 18d2300d-b2f3-3d58-a6ea-2a45590a87ab | -18.18022 | -53.31466 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23f1135d-9ed8-3042-b9d4-f4f64041c65b | -15.9804 | -59.5033 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68b97189-3e9a-3d76-96a2-ccb78f61b2d5 | -14.5347 | -48.41445 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 678dcd13-953f-3f5b-b4c0-70d71a33e751 | -14.58284 | -48.26498 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 907b401a-9b92-329c-b0e4-7384cbf7a7a3 | -14.47776 | -48.57913 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5aae070-9e4f-3eac-8743-13d05116175a | -15.61545 | -53.16936 | 2025-09-28 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92f14bcb-6d2e-39b5-a430-2b23c65a0054 | -15.44818 | -48.23395 | 2025-09-28 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e63590ed-e1eb-3ffb-a90a-fd5da327118a | -16.96547 | -53.69121 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8c17aeac-3864-344d-b60d-d9b8a442bdc7 | -15.46456 | -50.22715 | 2025-09-28 05:21:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b34e8d5-99ea-3fa8-95cf-d18b36063fb4 | -14.59011 | -48.259 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc2ec240-6a02-3031-bcaf-e98214894f22 | -15.94481 | -57.48498 | 2025-09-28 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff5d95e5-2ca6-335c-8d8c-9c1fbb94d02e | -15.33639 | -47.88695 | 2025-09-28 05:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5c4ad8d-fbb0-373c-a3ac-0b60ee275a09 | -16.96899 | -53.70247 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6dd9681c-b8b7-3804-b3e4-4cedaf643817 | -18.20532 | -53.31612 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 504cee4d-9bb6-3ce4-b8a7-b754f23b4f38 | -18.18403 | -53.32578 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f08d76c1-ae85-303e-9326-eb4b801d659b | -15.22121 | -48.06131 | 2025-09-28 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| caa5e99e-c607-3363-bcc5-1ca5019f3154 | -15.44943 | -48.22136 | 2025-09-28 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 513d9996-e039-378e-9bf2-f99d12224459 | -14.58413 | -48.25234 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a87f40f0-1805-3fb7-bab7-0f82e0afa371 | -20.69956 | -50.7149 | 2025-09-28 05:21:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 4567c92b-2c47-38d5-a50b-31c2e0780f8b | -15.95221 | -57.48603 | 2025-09-28 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5e0cd42-8571-3960-92f3-196bc610067a | -12.19285 | -63.66678 | 2025-09-28 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b26534d8-94e7-315f-96de-2803c0045ba6 | -18.18958 | -53.32137 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2da4e10-62b5-3a36-b237-124f1bb6741f | -15.60638 | -53.16249 | 2025-09-28 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c52ab9fc-65ee-301e-a85c-449b31ef1d90 | -15.95158 | -57.49059 | 2025-09-28 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5faab6f5-9406-3f83-a99f-2aa59232cb03 | -14.47853 | -48.5813 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66ef0357-df42-3643-96c4-c5b3c1d36f6f | -15.98095 | -59.49957 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97c94ffb-ce4c-3e4b-b859-f0af690b1bd0 | -14.54022 | -48.42371 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a2ee3328-8e55-3f15-91f4-151eb34c9b65 | -15.44755 | -48.24028 | 2025-09-28 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d46b669f-6975-35ca-aac7-66d6b668401d | -15.92667 | -59.49106 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06b2e2e1-2c80-364c-a5b2-7b65223603c3 | -14.54078 | -48.4182 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f43d67b-1e0d-3db5-ba14-87b1992e4e4d | -15.60572 | -53.16816 | 2025-09-28 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bcd168a-4d8e-37cb-bde9-78352ffef178 | -13.80199 | -52.79066 | 2025-09-28 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c094ac30-4fce-311f-a506-104ef925e8b4 | -15.32837 | -47.89923 | 2025-09-28 05:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 36e0ab90-7b4d-361c-b8e1-7a37cdfc580c | -16.96963 | -53.69706 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fad4692e-51da-3486-a19b-f09da3a74f4e | -15.94416 | -57.4896 | 2025-09-28 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5d03a1f-c945-3a8e-b43e-495451a664de | -18.18458 | -53.32088 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e91740b7-078d-3378-b6f1-248e8a9bfa3f | -20.69305 | -50.71931 | 2025-09-28 05:21:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e73dbf9c-5498-312b-b70a-668ba6efbf96 | -15.55648 | -56.00039 | 2025-09-28 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b454803f-5f96-3ad0-9d01-87200b623a85 | -20.69912 | -50.71983 | 2025-09-28 05:21:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 7e8e8096-6a43-36ea-ba1f-e2acbcb404c5 | -16.96609 | -53.68589 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e4ce019f-d20d-3565-8191-34fb71ccca0f | -14.58944 | -48.26547 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff8bc0b9-62ca-3b0b-9406-d06e070215e9 | -15.43742 | -59.73231 | 2025-09-28 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9f650b0-c49a-377c-8b4c-0dd80a5ccb92 | -15.97756 | -59.49902 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8a422d3-bf92-3edb-9b2d-0ba591dc8984 | -15.97317 | -50.87523 | 2025-09-28 05:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0d13898-6603-33d4-9e31-42eba39757e2 | -18.19962 | -53.32184 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a48969fa-b717-3cde-ade4-cf8f24ea7dc8 | -12.86947 | -62.09434 | 2025-09-28 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48a3804d-2478-3058-a7a3-f14661faf9b4 | -15.99449 | -59.50188 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3f73b8e-d3de-3583-a73a-d80d674d4cb9 | -13.80514 | -52.79168 | 2025-09-28 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e44050d-d932-3e75-8a84-49c1ec3df363 | -15.53664 | -47.9185 | 2025-09-28 05:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a3aad26-e5ec-34ef-b24c-c6ff060963c2 | -14.57808 | -48.24648 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b7cef80-41ae-37bf-a571-f1a9ba4bdaa0 | -15.92841 | -59.50282 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 683cf95f-2839-34f1-b3c6-1a5d52ecb62d | -14.48415 | -48.58036 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96ea10df-9425-3d5d-b012-0ae532282d5b | -14.3217 | -52.92105 | 2025-09-28 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f72a79d1-1dd5-3cd1-ae76-7d530a990e51 | -14.31956 | -52.92792 | 2025-09-28 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4fdf29c-69b2-3cea-a17b-55190145117e | -14.59134 | -48.24697 | 2025-09-28 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6c02c52-aadd-3c66-ab95-496898255177 | -18.17464 | -53.31945 | 2025-09-28 05:21:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61ce2cb2-b543-3b29-88b8-9e3c7c1a8581 | -15.53425 | -47.91732 | 2025-09-28 05:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1b16027-d7ad-36b8-a406-6427ee9a0c42 | -15.77789 | -50.16116 | 2025-09-28 05:21:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ccbe142-29d8-3207-aae6-75964fa03859 | -16.96005 | -53.696 | 2025-09-28 05:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 574f81e4-dc1c-3ce9-9e39-2fcb91644a0e | -15.8395 | -59.60444 | 2025-09-28 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e10652d8-d84c-30a8-9c6f-140d54c4f330 | -22.9443 | -49.87952 | 2025-09-28 05:23:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 6b3f67e3-e9c1-3d36-bca8-fad1b09cb73f | -22.94472 | -49.87374 | 2025-09-28 05:23:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| ab691163-f8c8-37a5-aee4-f25113de1cd2 | -22.36064 | -49.96494 | 2025-09-28 05:23:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5584d5cd-4163-3be9-946a-c74024279359 | -1.62623 | -55.17191 | 2025-09-28 05:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1c2b8ca-5ee7-3201-84e8-9289d5829ee1 | -1.62675 | -55.16854 | 2025-09-28 05:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b8036a7-85e0-3666-8a03-d80b50718415 | -3.21142 | -51.27974 | 2025-09-28 05:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d087bdd3-ecdf-39b1-b3ba-a096195b41b1 | -2.19071 | -54.46458 | 2025-09-28 05:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8d5db07-06be-32fd-ab26-03740db20484 | -2.19337 | -54.46545 | 2025-09-28 05:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 117a3475-5675-3821-b789-ee35950b9180 | -1.62087 | -55.17109 | 2025-09-28 05:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db106087-e515-3604-9548-7dde60a7ecdb | -2.19637 | -54.46543 | 2025-09-28 05:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README90.md)
