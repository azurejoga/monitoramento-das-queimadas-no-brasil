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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc3742b7-f5c1-3c50-8e31-52c29d603414 | -7.22066 | -43.08017 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 5098887b-4513-364b-8156-fa316b252eb6 | -7.20799 | -43.08984 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e3f290ea-b37f-3976-999b-6b964e0f5838 | -5.61679 | -44.01075 | 2025-06-28 04:49:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 562b4b1f-23ba-3ad4-be9d-f5de3a996d62 | -3.51636 | -47.21566 | 2025-06-28 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64a89e5b-ef12-3b5c-95ee-36aaf52f0fcd | -6.90784 | -43.98278 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c04c2cac-7f57-3ceb-93f6-96ed5ca7c811 | -7.21613 | -43.07185 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f5df5265-bb5d-301e-86b2-950d57a5a53c | -8.10653 | -47.13483 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9c9b3ac-237a-3ca7-ae8e-148ebfb039e2 | -6.90692 | -43.9892 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8e4fadd2-5f20-3a84-8280-f7e1f86f35e1 | -6.90353 | -43.97562 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d84d7a83-2cec-34c3-b4d4-9f3721c634c0 | -6.9443 | -42.88721 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 65bb3719-ff75-343f-9dd3-ad800e172f79 | -6.94537 | -42.87954 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7435cc71-d223-3566-9795-54cb9e460348 | -7.22572 | -43.08469 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7a556a44-5c73-3e4b-89f8-7622778dd8d1 | -6.60243 | -55.30559 | 2025-06-28 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9591a24a-fd68-365e-ab72-9ffb75bd589a | -9.7228 | -56.183 | 2025-06-28 04:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 421495fc-8bb1-3aec-952f-0cd98f6075e4 | -11.2664 | -52.7527 | 2025-06-28 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8571b0b2-d283-359e-88a3-618314f44159 | -11.0455 | -55.3773 | 2025-06-28 04:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| f2244f6d-a8c8-3ada-b842-9ae6d2d0259f | -9.11322 | -49.48588 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 073d6f28-a53d-3a39-9fe1-115c33e98df7 | -10.0299 | -54.31727 | 2025-06-28 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73920313-9453-36bf-a574-ec658c77ca0c | -11.04665 | -55.37021 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9845dfa9-fedc-38be-859c-f1627040dbd6 | -10.27467 | -44.6461 | 2025-06-28 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02d6dbc8-2de7-3ad8-8f6c-51ea4459174a | -11.8275 | -57.76803 | 2025-06-28 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41004b24-5f7e-3502-b33d-e7368e18e8ce | -12.25974 | -46.77134 | 2025-06-28 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| dd702546-d2c5-3d46-b0ba-f1f8bb98a071 | -11.69489 | -51.63221 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5062f453-beb0-3a1a-af5d-67e4590f4eea | -11.05326 | -56.7472 | 2025-06-28 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a199719-e7cb-35a6-9596-94e146174064 | -10.83285 | -53.75353 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6266c886-5487-313f-a371-248d86c32d58 | -9.44069 | -63.46194 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0b64e4e-bb1f-3808-92e6-6c3c555ff3c1 | -11.27511 | -52.74496 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fec3b274-ae71-3dec-9f8f-a834605cd73b | -9.71379 | -56.18565 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 98cd378f-e14a-38a2-9484-acbc7c63d5b4 | -11.03589 | -55.37222 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d62913fc-d1b8-3cc6-953d-84dd9b0b695d | -11.5789 | -52.12171 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca399409-81a5-3eee-bcf8-c8dbba81556e | -14.21425 | -57.40238 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7912553d-110a-314f-977c-1a68f3fbef4b | -12.21426 | -51.46421 | 2025-06-28 04:51:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac506be6-a47f-3d8f-8b22-3dc41137fa73 | -13.94018 | -54.49105 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1effb31-ceca-382c-8bcf-c5ae9cd19642 | -11.57947 | -52.11801 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7aa23ea5-dcc3-3458-8f82-3a1772e69cc5 | -11.58023 | -52.118 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 197e4bf0-8f48-3693-8e7e-ea20e59613ed | -10.29848 | -57.13778 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8671a455-4259-32b7-97a2-fd43f3bef4a6 | -9.70606 | -56.18851 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 73a4d599-bd41-345f-aacc-55c8478b1408 | -11.84249 | -43.80033 | 2025-06-28 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0013f459-db70-3521-96de-3af551b0929b | -14.68893 | -53.3848 | 2025-06-28 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9170fda9-7601-3b71-82f5-07fbff4467f1 | -13.8271 | -59.67171 | 2025-06-28 04:51:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3b9edea-87af-3b61-b1fa-5772e622b829 | -8.5472 | -55.03363 | 2025-06-28 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57db3b33-cf84-3c05-8bc8-1d1e2741569a | -11.69836 | -51.63274 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 197e24f0-908e-35cf-bd48-36c28c1543ac | -11.05024 | -55.07056 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b95e0ca0-54fd-32f2-bc79-31c4ba2eaed4 | -11.059 | -55.37984 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3b37828-8fb2-3381-b35d-6d91fc79c581 | -10.05363 | -59.3587 | 2025-06-28 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c30cc78b-ffe8-3861-a8ba-385986104e74 | -11.03928 | -55.37277 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ab86935f-9b91-3af3-a07c-e8213710658f | -12.03707 | -48.7511 | 2025-06-28 04:51:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b27890a-a636-3f96-857a-38bf4140c32d | -11.66376 | -46.73005 | 2025-06-28 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3c3eac4-d26a-3841-bd50-a4b947fe91a5 | -11.27791 | -52.46539 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df6b49b6-3eb8-362b-9b16-d4d0bec3aa8d | -11.9179 | -54.81586 | 2025-06-28 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d14a0014-c0aa-3cef-a545-c4d60fd61cc8 | -11.43592 | -54.47042 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaebaa54-c494-3bbf-919c-9ce5e27f01ed | -15.26285 | -51.46921 | 2025-06-28 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea125736-8a8a-3824-b547-bfc8b2225346 | -16.45516 | -49.51475 | 2025-06-28 04:51:00 | NOAA-20 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c7e6739-d7bc-36ef-9f79-42a0b20ca875 | -12.26038 | -46.7664 | 2025-06-28 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 21a80920-4943-3599-b104-fc0262e1463a | -11.19556 | -55.92245 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fda951e3-c1de-38c8-bc58-dea984eb22ec | -9.35384 | -58.83369 | 2025-06-28 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 834ce1a7-a10d-3fc6-b0ec-e9d883de44ac | -13.14302 | -56.80797 | 2025-06-28 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da762b9a-cc46-3098-9163-837fc3e637f2 | -11.04148 | -55.38068 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 592b51dc-042e-32fe-821e-8c07d5be727f | -13.99743 | -44.03194 | 2025-06-28 04:51:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54aba569-d706-3a67-948f-11a43d178a14 | -9.74131 | -48.34074 | 2025-06-28 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40040ae0-2f26-3e12-bba0-d1ba95281312 | -10.82734 | -53.74547 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa8ad2f8-c7ca-3988-9908-228fe7ffe7cf | -11.27176 | -52.74444 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f15680a8-5936-31a5-b38d-4530d4bae33b | -15.35402 | -49.05022 | 2025-06-28 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6de2b941-04f0-3716-a2f2-60012186e873 | -11.44037 | -54.46392 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b076c91-83da-3bdd-9a0a-b09ae7c4038c | -11.83968 | -43.79808 | 2025-06-28 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 589538cb-6a64-372b-8323-a4aa2e106839 | -9.08877 | -47.96857 | 2025-06-28 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9dfa56e-d847-3581-b659-072d521182e1 | -11.60699 | -47.61584 | 2025-06-28 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35b1ec9e-8871-3641-9189-760e9f5decf8 | -11.80274 | -56.96447 | 2025-06-28 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3de4b7d2-7dfb-310e-a14b-2812ef408345 | -10.2867 | -57.00648 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84d6d22f-1e61-3243-b98f-6a9158c3d209 | -11.2779 | -52.74905 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35d94b62-4087-336f-80e4-980fd1cce733 | -11.32718 | -51.45185 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c3d463c-de44-3c1c-9102-7cd117eb0ac1 | -11.44369 | -54.46447 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1bbad70-0dab-3e6e-88d1-452583bbad1c | -9.11762 | -49.48195 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b7c38c68-488c-3c36-a279-39f824992548 | -13.72635 | -58.67825 | 2025-06-28 04:51:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eff99257-06ac-398b-baad-b2c1391944d0 | -9.12001 | -49.49158 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 92e904ab-705b-3791-ac51-a4896e146546 | -9.09025 | -59.49751 | 2025-06-28 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd628b22-b143-3d0a-9b8f-d630b3fb99da | -8.54379 | -55.03307 | 2025-06-28 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08c25a78-73fe-3296-8c52-81b900999aa9 | -8.86054 | -50.16071 | 2025-06-28 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47d62758-11e3-3546-be13-d9c1c77b6eb9 | -11.05751 | -56.74368 | 2025-06-28 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7601795-d6ef-301e-81d2-6af818213663 | -11.27845 | -52.74548 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ad21775-23cf-3b2b-acb3-7c7c444cfb65 | -12.65599 | -49.46773 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7521a351-473b-32c3-8e51-ae70cbb75630 | -13.29272 | -57.08077 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97bbbd9f-21c0-3843-a869-32e7044d48c7 | -12.10511 | -54.66394 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 862aa573-c0fd-3e8d-98aa-94d77253e11e | -12.50436 | -58.35387 | 2025-06-28 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f46d017-a737-3e86-a1b1-37f2bf5e2115 | -11.57324 | -52.11324 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bdf3d2e-b879-3648-87f0-13d45f442485 | -9.4367 | -63.46505 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecb599cd-7867-387e-8bdd-5d249db907d2 | -9.42952 | -63.45959 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb60d853-9930-3e93-9aba-06a7ef37f219 | -14.83431 | -59.79738 | 2025-06-28 04:51:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d28c2847-0c45-36ee-8abd-486bc2dbb8b3 | -9.69966 | -56.18332 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ae24fd5-f7e1-3606-90b3-27ab302d2b12 | -10.60273 | -52.83599 | 2025-06-28 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77559c18-d08b-36b8-bda2-c816bc543429 | -9.35471 | -58.85335 | 2025-06-28 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe8f00b9-c16d-37f7-b2aa-d5be7efaaa92 | -10.29995 | -57.12904 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f3a5889-1c98-33bf-bf7b-f2de1dbbb8bd | -12.10981 | -54.59204 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f543959d-dbbc-3b2e-8f43-6d0a94b890d8 | -12.65683 | -54.09962 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e22e4d48-e77e-36db-b91d-5e96a29cc4f9 | -12.1073 | -54.67158 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fc9d931-7572-3835-9402-9a765203e8ad | -11.65914 | -46.72934 | 2025-06-28 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a17a4a88-764e-30ad-ad90-f0952a362272 | -11.18585 | -55.91692 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a20abd3b-d719-3331-8116-f690de15be34 | -11.00938 | -55.0673 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea960b98-8a80-30e9-a45c-66b09ddf36df | -11.56462 | -47.62421 | 2025-06-28 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6cdaba2-ab1d-3f2e-9b2d-88a69ecf3ec0 | -10.95428 | -49.25401 | 2025-06-28 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README23.md)
