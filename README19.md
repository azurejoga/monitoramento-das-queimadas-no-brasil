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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0ab61eb-5a9f-3e2c-ab07-51d6cf5ae672 | -8.64455 | -54.70066 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 430ebc35-07b4-3a67-8ca6-7ef89b2bb6f7 | -6.85242 | -56.43647 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c66e3e4-559d-3c8b-8929-fb0d173240ec | -6.71479 | -58.93277 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3647c743-15fc-33ba-8943-feb0e5a8cf5f | -6.30868 | -43.61454 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 059afd44-091e-31d2-a38a-acb7b40dfad4 | -9.0881 | -61.40511 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98cf98a5-3203-38e9-b5af-c831b3514527 | -7.42389 | -60.03426 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5a513b4-9e20-30a6-842a-f4bd0708c678 | -6.83721 | -56.44359 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5b39955-346f-30f9-b4cb-20a2d9889df5 | -7.41048 | -60.01115 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c41c5d0f-60b9-34d8-a891-c59e9ac19bf8 | -8.40976 | -62.65808 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7464e7e-fb8f-3611-a08d-407836ac5800 | -6.83217 | -56.43864 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c177b0c-7714-3b1b-816b-57a889e2802e | -10.54104 | -44.8677 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7951270d-78b3-3ccb-8f11-8f3d0950ee92 | -6.8552 | -58.96812 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 987acf5a-06db-3b95-a1ad-84952e3bc3ac | -8.60083 | -54.67288 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed61b295-2dec-34fe-ac97-535d47b22f71 | -11.48205 | -46.58948 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c08e3382-31f2-302c-b0f3-c5eb3bb12f25 | -11.90743 | -45.98 | 2026-08-16 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8cdebe2-b52e-38ec-8ded-dcbefd1cb1a5 | -9.48536 | -51.64486 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 026fc910-2891-37fb-80c9-8c6e61dec86c | -8.16384 | -47.39496 | 2026-08-16 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5f8b85b-7d24-3808-9cdd-25bc135118c6 | -11.88407 | -51.94706 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff0f1c4d-6d63-3c89-8ccb-48e87d965c13 | -8.95558 | -60.53481 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 36927aaf-ac30-3d41-972e-b5127d4776ad | -8.66242 | -54.73701 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b65133d-bfcd-3ac5-a4c3-bef6a4c0ea28 | -7.17152 | -43.24136 | 2026-08-16 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6a68d93d-bcce-3361-94c9-1ef853eafeb7 | -6.53389 | -55.17811 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3439fda-5e52-3a80-b201-a49b8648cb14 | -7.49983 | -60.07904 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 432c61a8-06b1-371a-a956-bee6b6aabd2f | -6.9228 | -43.63641 | 2026-08-16 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0992a167-f8ec-3007-b3f1-0514f8e47bfb | -7.49864 | -60.07697 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93ad7b11-767b-3c51-97fb-db5eb1d5303f | -6.28679 | -47.7314 | 2026-08-16 04:40:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a87a2012-02db-33b0-ba66-36606642d8e4 | -8.64797 | -54.70351 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c48969d6-9a7a-3c04-bf81-ce55f33fff43 | -8.60921 | -54.69498 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2efc8285-26d8-38df-a798-7a96aa98127b | -8.8951 | -60.60013 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc9658e1-f1cd-3df9-9117-22a20e26ca47 | -10.26246 | -46.30564 | 2026-08-16 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 212967e7-83af-3295-94cd-813acd5718ca | -11.0444 | -47.25199 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42ddf4d8-5812-3001-9008-591f7e6126fe | -7.46099 | -44.86676 | 2026-08-16 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3efd6b5-69c1-369a-a9b8-9e01c9f21892 | -6.86751 | -43.87392 | 2026-08-16 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0337aaca-7de3-3a0f-8a19-892666f0030a | -12.03562 | -46.44245 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c66466c-fa77-3028-995c-113cd49bec1d | -7.06918 | -56.65485 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce50332-8c7c-3f0c-a5dc-6f72e0f46572 | -8.98653 | -60.52781 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57d439ff-d27b-353f-ade0-414b6a5bca9a | -12.14189 | -50.12902 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85adcb27-ed09-3c48-a6a7-b56585aba585 | -6.62998 | -59.05111 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0eabf05b-5eb0-335c-9f6c-8cfc8b946ca9 | -9.25608 | -56.90559 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0861fba5-dee7-3a25-bc10-be2885317f0c | -7.26176 | -44.69436 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fec8f98-0b5c-3cac-8413-63395ef8de74 | -6.8238 | -56.46085 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8b904464-edae-3b0b-82f7-b54782a3295f | -6.60502 | -59.00357 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31b68ab4-9b22-33c1-87f7-4f132dfb91ef | -7.40754 | -60.01596 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 821cf51a-b3ac-39e9-a03c-384be4f812d0 | -6.31663 | -43.61977 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4473cbdf-e6bc-3a4c-814f-be6c67bd9129 | -6.59833 | -58.9984 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39fe4535-00d7-3b12-bb71-2affdde77f83 | -11.0935 | -47.24665 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13e0c2db-54ec-3cba-8ebb-aa4bb786c898 | -6.59954 | -58.99144 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5995dc12-5e3b-3c24-871d-671f01ff3ce2 | -8.89583 | -60.59615 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ddc4a11-4b70-3e8e-8c9d-553d0c60d229 | -8.64228 | -54.68998 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 178df65f-acc0-36fb-914b-02e4f2793391 | -11.88073 | -51.9465 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ded374e-8229-3afe-a0a2-fb4a3046a9f4 | -11.47826 | -46.58889 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 11bce5e5-fa73-3a37-97b8-c9df6b9b7f12 | -8.40173 | -48.48308 | 2026-08-16 04:40:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8214c9c-721e-31bb-ba4f-43e5405e0461 | -12.24531 | -47.00929 | 2026-08-16 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76524b22-3b6c-3e3d-ba30-48b17a22127a | -9.99041 | -53.94843 | 2026-08-16 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa1af9af-adc2-3865-9bc9-49cb6ca869e9 | -10.54051 | -44.8715 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 351171a2-8b46-3d6a-b155-151858c97ab4 | -11.4832 | -54.61383 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33e27b89-82c9-36f9-a401-357fda37853a | -6.93082 | -43.64174 | 2026-08-16 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b6fcebd-112d-3f3a-b4be-0470cbe2e76a | -6.36473 | -58.31914 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49ed1c0c-ff2c-362f-aa17-53a65eee179b | -11.48243 | -54.6184 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed0f6d05-6a86-3c2a-8e13-e7895deec2bc | -8.97806 | -60.50967 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1454473e-3d89-3607-a296-4e59e7b134c4 | -12.03248 | -46.43673 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5794113-50bc-3587-bcf8-a7e0257ef85e | -11.45665 | -46.60518 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d580acca-acda-34d0-91d1-e283eaf48f6d | -7.42118 | -60.01693 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7c78192-e8d8-3556-b474-c83b6edce270 | -8.89654 | -60.59535 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f8b1a4ba-7668-39f9-bbcd-d7208158a61c | -8.95646 | -60.59365 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39406b81-a59a-3ddb-ac6a-4ab86a1e0aa9 | -12.56254 | -47.84549 | 2026-08-16 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 045d559f-8dcc-3b43-b68c-0d7f225e4a73 | -8.98004 | -60.53085 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f00c40bb-84cb-38d5-886c-53e495173b15 | -6.84414 | -56.43055 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 673d7c26-6f33-3fb6-b691-b0763a25d026 | -9.47682 | -51.62148 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 995885ff-a9bd-3034-a045-cb663101299c | -9.4774 | -51.61784 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42f58729-0f4a-3b35-92d8-1e85546ad44b | -9.47629 | -60.51252 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fc20c64-93e8-3f9c-886a-80fdd857590b | -8.90251 | -60.55972 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1c449155-26a8-3f06-b7ba-eb9806c0ab97 | -8.97657 | -60.51767 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 83b27db8-6e30-3388-ad49-2d6638739351 | -11.07347 | -47.25658 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7898234c-f8ff-3c3c-ba2d-6c2191613029 | -9.30305 | -56.80956 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 254a96ff-d597-3cd0-b398-47706321e61f | -6.7059 | -58.93572 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bbeaaa1c-74f0-3203-9303-159286e4fe10 | -6.37974 | -58.325 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96800c37-1ce2-3ca2-8113-e2361e66b110 | -8.64764 | -54.70633 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62939ea1-5179-37f2-b092-67c6a2e76806 | -12.64996 | -43.8998 | 2026-08-16 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d939d32-b323-3ca9-a6dd-cd5ead2e17b1 | -8.64492 | -54.69782 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c129d44-0073-32b4-a0b8-09bed8b714cc | -6.25323 | -47.69602 | 2026-08-16 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b55493d-c650-3b7b-862b-31b601f09d59 | -5.44548 | -48.92196 | 2026-08-16 04:40:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0a27da8-e5d8-3e9f-97ab-22f0cb519c16 | -6.8471 | -56.44033 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6921638a-eeb9-36c0-a2b1-fb3194eec66c | -8.89808 | -60.5873 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e19661cb-6d71-3743-9d5c-7564ceca9cbc | -8.64599 | -54.71635 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2938a4f8-d2dd-3bff-ba8e-c950338497af | -11.45731 | -46.60043 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77acbcc4-6b20-3b30-9c39-29b98f6a5331 | -11.50976 | -54.62199 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5f933b9-068f-3452-81de-915dcb5e02ce | -11.91167 | -50.23433 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 172c3bbb-de40-32c2-8c89-35025982e81c | -7.00528 | -45.90825 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d07625a-b743-3216-bb5f-faa2edf2fcaf | -6.78322 | -47.71499 | 2026-08-16 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56fb4674-0c1e-3764-a98f-b530ef397804 | -6.62902 | -55.30864 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5aded27-e127-3b22-b2a0-b0e49816a2f2 | -7.11137 | -55.12661 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a71e49e1-f9c7-34b4-819d-98a59a3b6994 | -12.03878 | -46.44798 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7e705fdd-029a-3775-8afa-27582244be8d | -9.54502 | -56.79905 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba248c11-87fd-3872-9b95-efc42f5cd3f2 | -6.8367 | -56.43939 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3bc85703-5804-339b-969d-b6e38e559d06 | -7.37204 | -46.81387 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0b6dbe6-3eb6-35bd-9655-89aee1505b45 | -7.42758 | -60.01407 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb52de71-0364-3276-9468-8ffeebee603c | -6.60051 | -59.12204 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb01345e-baad-3a33-b413-5d31cfa010e3 | -6.29019 | -47.73191 | 2026-08-16 04:40:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ad4f190-fa39-31a6-ab59-6482877b1b34 | -9.4661 | -60.53513 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README20.md)
