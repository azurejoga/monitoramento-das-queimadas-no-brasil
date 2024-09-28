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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bacb0efa-f2dd-3034-803b-1f8e45e8c0cb | -8.74589 | -49.78231 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 03ae99a8-e85a-3d76-97bb-5749ddcad0cf | -8.3497 | -51.73446 | 2024-09-28 05:23:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1e86616b-3b23-33c3-8826-004fe1022374 | -8.34442 | -47.56092 | 2024-09-28 05:23:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 44b7ace1-5754-3171-9be0-e2f6383ee8ce | -8.33823 | -47.54185 | 2024-09-28 05:23:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 986963ed-260e-3913-b854-e4ae5276e84f | -8.23433 | -49.38273 | 2024-09-28 05:23:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 92fe45a4-4c40-3532-b269-6dfd5a5cebf8 | -8.10292 | -49.51672 | 2024-09-28 05:23:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 156d2619-f840-3116-b608-aeecbc9e9163 | -8.10138 | -49.52663 | 2024-09-28 05:23:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6b7d3819-e148-31a4-a19f-b52125faaad8 | -8.09361 | -49.51532 | 2024-09-28 05:23:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 03a36180-f238-39a9-928f-1830bb294ffa | -8.09207 | -49.52521 | 2024-09-28 05:23:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b74e3d35-f3ff-36d3-8cfb-78849e307273 | -7.58982 | -49.19068 | 2024-09-28 05:23:00 | AQUA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5140609-63fc-3c19-90cd-c05f297fb0ee | -7.28258 | -46.1354 | 2024-09-28 05:23:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c759e408-8b04-3ac6-bbf4-4e05941ce5f9 | -7.25939 | -46.61092 | 2024-09-28 05:23:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2eeeb5ae-956e-3b9f-8268-ca1d6405ec91 | -13.02644 | -48.60336 | 2024-09-28 05:23:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2751186e-3979-36a3-93d0-96587d8c648c | -12.7975 | -47.45774 | 2024-09-28 05:23:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8b015db5-b979-3211-83ce-ab5881902a82 | -12.52882 | -50.6273 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 42eb8652-00f5-3fac-84dc-0ec9b22ea6eb | -12.5272 | -50.63744 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d3e55d9c-7349-37fa-b050-1800205b5791 | -12.38996 | -50.45823 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 95e0d055-d447-3d3d-86c1-7977a7e649ab | -12.38838 | -50.46823 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c7d32e3d-7a01-3a57-99b2-94f9d202a887 | -12.31865 | -50.441 | 2024-09-28 05:23:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f6005f12-7f62-3601-956a-cd0f1e1dc710 | -11.01739 | -50.18736 | 2024-09-28 05:23:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cdd45f76-8ef7-3eeb-996a-47b05ffcbc43 | -10.98635 | -50.16548 | 2024-09-28 05:23:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 96b229f1-c12d-3ec8-8b5a-8fb118d6ef6e | -10.9848 | -50.17546 | 2024-09-28 05:23:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2310c30b-43ee-311d-a891-71eba1df3d0d | -10.9315 | -54.25439 | 2024-09-28 05:23:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 7171cf7b-e8e7-30c0-8f04-71903cd5c180 | -10.87886 | -46.38356 | 2024-09-28 05:23:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5614bf63-6356-3537-b4c4-02878f9bfdc3 | -10.60649 | -51.08714 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7af9b948-d1c7-3ade-a8aa-f952eb657add | -10.60468 | -51.09837 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d53be588-c6c9-3fcc-8927-669a71b3562f | -10.59482 | -51.09678 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2b9821b0-8767-3eb8-bc33-715f0561ad6f | -10.57471 | -46.06569 | 2024-09-28 05:23:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f5f1cb45-84cc-3dc0-90d8-dcff28f61e99 | -10.56683 | -46.05448 | 2024-09-28 05:23:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 61f71a5e-8bca-30ac-9d50-53f37e520245 | -10.55896 | -46.04318 | 2024-09-28 05:23:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7d034b14-ed05-3310-9a5c-57b23e601f17 | -10.54285 | -48.0529 | 2024-09-28 05:23:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd800859-6772-35b8-ba31-8ceb9979675f | -10.54258 | -51.09406 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3e578fa-b078-3626-be12-250ce5f46caf | -10.53535 | -48.04264 | 2024-09-28 05:23:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7a123d8-1c10-388b-a7ff-6c9037c420e6 | -10.53101 | -51.10313 | 2024-09-28 05:23:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 89fe660f-d2fd-3933-9b09-4c5da4628ff5 | -10.0403 | -53.41064 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1a6e7de7-b525-38dc-b2d2-039a237c69ef | -10.03762 | -53.42717 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| d449778b-05ae-3c69-99d1-24b1274fc8c8 | -10.03562 | -53.41531 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 3883fd44-2fd5-3ea5-be88-960020e95a9d | -10.03281 | -53.43185 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 3c58f503-b786-3f1e-a457-c6546962e3c4 | -10.02952 | -53.47721 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1a780541-328b-3923-80da-ce400987bdee | -10.0285 | -53.40861 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| fe995537-f1bd-3341-b085-d588234f998e | -10.02718 | -53.46499 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 779a77a8-1c5d-3b8e-bbd6-3ce2163183d2 | -10.0258 | -53.42518 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 221.5 |
| ef6f0000-7eda-39c0-a766-65c0f313fd79 | -10.02433 | -53.48175 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 801cac8a-27f9-3334-86b3-095fd1e71fc5 | -10.02383 | -53.41329 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4873416f-d27d-3910-b931-2aec9d554ec9 | -10.021 | -53.42983 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 576722fb-0ea8-3cef-b8e6-23706df86cd1 | -10.0204 | -53.45831 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b89190ba-9a20-38d3-998b-381718cdb1ff | -10.01768 | -53.475 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 03457f07-85bd-3416-92d6-749015696398 | -10.014 | -53.42302 | 2024-09-28 05:23:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| c05abb67-886a-35b7-8dd9-6ce38d3f437d | -17.43807 | -42.61005 | 2024-09-28 05:25:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 000a098f-ac63-30c4-ae0e-10e73e8616c8 | -17.1398 | -47.6212 | 2024-09-28 05:25:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 222f3852-d946-378a-acc2-8e698fc949b5 | -17.1384 | -47.63127 | 2024-09-28 05:25:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| a3b56857-1753-371e-956f-428c397ce4ee | -16.8837 | -45.31589 | 2024-09-28 05:25:00 | AQUA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d47792ab-d1bd-387a-95ce-d9007cb92afb | -15.63155 | -47.22157 | 2024-09-28 05:25:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0295b53b-da5d-35c1-a081-552004aff965 | -15.63015 | -47.23169 | 2024-09-28 05:25:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 45b1dbcf-ed89-3fcc-8bc8-a565f07d0b5b | -15.62229 | -47.22016 | 2024-09-28 05:25:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 12ee752b-08c4-3a82-9cde-19b5d69442d3 | -15.62088 | -47.23029 | 2024-09-28 05:25:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 38.1 |
| b1c36fce-9b87-31d6-9c10-b0bcef52b564 | -15.53393 | -47.6544 | 2024-09-28 05:25:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83eda0aa-d502-3672-b401-6a06ced4a453 | -15.51368 | -43.5536 | 2024-09-28 05:25:00 | AQUA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 47303313-1b90-31ba-a725-2ba419cc9783 | -15.40616 | -47.45015 | 2024-09-28 05:25:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7a9fedd7-9e91-3a76-9b35-d4b09cff824f | -15.25669 | -48.29471 | 2024-09-28 05:25:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3cdfcd66-5897-3a35-87ab-0d44b414833e | -14.85102 | -48.92534 | 2024-09-28 05:25:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f98338f4-1e7c-3879-9f6c-a413b25622cc | -14.87616 | -51.54563 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c5d6b5a5-c87d-3729-ab91-529137ac8006 | -14.86836 | -51.53337 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4be55a8-0105-3187-9ec3-2b82d754c753 | -14.86819 | -51.45024 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 3c781789-c246-3200-9e3f-4945f42a591d | -14.86662 | -51.54403 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 06b9c6b0-4b4e-3e6a-8643-7cb2517e2582 | -14.86651 | -51.46081 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 43fa3c2b-5002-3242-8e32-6dda36c7dbd4 | -14.86426 | -51.53679 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c2b56a93-b1a2-323d-a32f-4596f66a275d | -14.86257 | -51.54747 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cb233022-4b73-3daa-bc3d-4eeed844fca7 | -14.8587 | -51.44864 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7cc083ab-2483-3e1c-aa22-f635679b0637 | -14.85592 | -51.40491 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 60bee615-c31f-3131-8112-dff4156eb4ac | -14.81803 | -51.39857 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d29ca597-15dc-3904-86a5-531554ab660d | -14.81633 | -51.40908 | 2024-09-28 05:25:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e92ff51f-0f15-3bb6-832b-89613aa51ac9 | -14.77725 | -53.85242 | 2024-09-28 05:25:00 | AQUA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e8d7b120-b841-3df2-9e79-483a9b799a36 | -13.20969 | -51.23674 | 2024-09-28 05:25:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ce0a0ff6-b44b-3887-b86a-750007a082df | -12.81167 | -53.98782 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d3cdae7a-0bab-308a-b97a-2f5fb9f81993 | -12.80883 | -54.00425 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 6d0c19e6-cc7c-389f-8c36-35cad2d36871 | -12.8033 | -53.99624 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 3a76f2a7-5965-336b-abc4-9f516b91e128 | -12.7971 | -54.00222 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| f8930968-f05d-3092-88f8-3de40a018da8 | -12.79158 | -53.99416 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ca0f9fd8-0315-3397-abdd-0ad121295f4a | -12.78885 | -54.01055 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| fab79362-3b83-3f39-8697-9632b4542ccd | -12.78538 | -54.00013 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 7a442b1f-8e16-3e49-b5e0-e5c669e01070 | -12.7825 | -54.01655 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8785bdd1-de85-365e-84d5-f037a0ca0ec9 | -12.77987 | -53.99205 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| b313905f-b17a-3e86-b34d-ad1e004bf59c | -12.77712 | -54.00844 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 364.0 |
| d864b332-fac8-3117-8b28-50648d9b6de0 | -12.77433 | -54.02505 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 6f85c082-40df-31fb-a680-92163fd42c6d | -12.76537 | -54.0064 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bc17e317-9d25-3d7d-9aab-bee9e79244fd | -12.76257 | -54.02298 | 2024-09-28 05:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 36cd46e0-3cd7-3063-9ad8-03f45b1451bd | -12.67986 | -54.67012 | 2024-09-28 05:25:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| b937cc26-1f46-35e0-a737-82b19b4dac1b | -23.56172 | -47.34838 | 2024-09-28 05:27:00 | AQUA_M-M | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 6475bab3-628e-3439-a62d-629947edbbe6 | -22.59932 | -49.19387 | 2024-09-28 05:27:00 | AQUA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 37bcb1e4-cadc-3308-8534-f85aca72c62a | -22.5979 | -49.20399 | 2024-09-28 05:27:00 | AQUA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8c84ba21-663b-3b1f-b2cb-6b45eb51267c | -22.35143 | -49.31709 | 2024-09-28 05:27:00 | AQUA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| b2ba1817-f74f-333b-8e27-fb0318734ecc | -21.95679 | -45.81039 | 2024-09-28 05:27:00 | AQUA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.6 |
| c7c8bc10-bbbe-3b08-9411-2486fc7ed9fa | -21.95501 | -45.82563 | 2024-09-28 05:27:00 | AQUA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| bd37bac7-12f4-31e3-9a5e-2a2bf3c344c7 | -21.94577 | -45.80868 | 2024-09-28 05:27:00 | AQUA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 4eb30131-548b-31aa-89a4-2b719bb0c74a | -21.88474 | -48.49357 | 2024-09-28 05:27:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cd94d8da-f29d-3592-8fa9-4e222877d68b | -21.8401 | -48.20843 | 2024-09-28 05:27:00 | AQUA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c8386bb3-57d6-3109-a71b-72213f1c68fc | -21.62424 | -47.76068 | 2024-09-28 05:27:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2f95e664-cc30-394b-8a4c-a60cca67e468 | -21.61603 | -47.74809 | 2024-09-28 05:27:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d1423229-c93b-3635-800f-395582e2298d | -21.61456 | -47.75941 | 2024-09-28 05:27:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |


[Clique aqui para ver as próximas entradas](README98.md)
