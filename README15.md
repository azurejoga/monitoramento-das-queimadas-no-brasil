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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a5f5bda-38de-30aa-bfe8-ec7d9ed9970b | -11.06091 | -43.18024 | 2025-06-28 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3034f5b5-c4f6-3991-ae9b-478f6ed4b7ea | -8.91246 | -49.84049 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88fd228a-c90d-341d-834d-f3c8ee7be2de | -5.2483 | -35.68767 | 2025-06-28 04:27:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4ede2267-8f1c-30e7-babb-ab7835454e5c | -6.15948 | -47.27531 | 2025-06-28 04:27:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97c3eb91-755f-3c76-bad8-3fc4dde30f56 | -11.06276 | -43.17836 | 2025-06-28 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7361875-5e39-30d5-978d-aca0a4e9ec67 | -6.90283 | -43.97169 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1eafb21a-8e7d-39d0-9d5f-f32fd9e8b2d2 | -9.87697 | -48.05351 | 2025-06-28 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9aa862e4-5310-3b5b-8172-57c011aa4e5f | -4.51812 | -42.07749 | 2025-06-28 04:27:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6fe5613-a9f5-3e7b-b6c4-f0429d2837db | -6.89754 | -43.9829 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bce1613-7563-33f6-b856-29d7e7fb37e3 | -6.91095 | -43.98891 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64e01682-b4e2-31b3-9fe5-f2cd6d2e604f | -7.55109 | -45.83213 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16f4e9f3-264a-30b0-b8e5-c04cb09a2043 | -6.16004 | -47.27177 | 2025-06-28 04:27:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40a0519b-dbb2-37ec-9b46-c7fefb3641bf | -5.86285 | -46.48204 | 2025-06-28 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f7c0a67-5976-3201-93b4-fc08ef3f7e46 | -6.90805 | -43.98448 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a39fca8e-59af-31c7-9270-5bb4d6846ba3 | -6.89985 | -43.99123 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 221b0074-6664-3719-8809-7a4e22dbbcf5 | -7.21367 | -43.07238 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c7808b04-c5de-3ee5-82fe-df0e1e60d499 | -5.46691 | -43.07386 | 2025-06-28 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f02d017-2f49-3b8e-939b-3b1a60cf9d6b | -8.04589 | -47.6488 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3642c37e-1aa2-3005-83e1-1e01f97a53c3 | -8.90888 | -49.83988 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ee93e68-2328-3ee9-8c36-98fc4bc121bb | -6.73272 | -47.37725 | 2025-06-28 04:27:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 849a8fb2-c05b-3276-a06f-b5f0b2cd0a0f | -6.54602 | -54.9848 | 2025-06-28 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a05619ea-624a-37f5-bb0d-7852676cd38a | -8.73644 | -47.85403 | 2025-06-28 04:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 828cddbc-567c-3ebf-be95-7f949a25f898 | -9.87546 | -48.60884 | 2025-06-28 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93f9187e-6c0a-37f1-91e5-222e542350b0 | -7.15219 | -43.37963 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 02d40414-2bbe-355b-8a55-1deadc5ff003 | -8.79644 | -44.99392 | 2025-06-28 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aef6ad70-e1d9-36bf-b63f-fc0d1d6f2358 | -6.90455 | -43.98395 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 508908a9-b2ca-3090-87ce-a71cbde822ff | -6.68929 | -43.07042 | 2025-06-28 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad10521e-cbc5-339e-86a5-91578a8bdca3 | -8.79587 | -44.99765 | 2025-06-28 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6974c081-3339-3fbd-a650-f0137c61f154 | -7.10102 | -43.66464 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46625abf-7984-3487-8275-1b5728dc27bf | -7.18994 | -45.32658 | 2025-06-28 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b07fe9cd-34fa-39b6-9170-eace863139cf | -8.74036 | -47.85104 | 2025-06-28 04:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 921b463a-2e00-3675-b5ac-a894f05f8c3f | -9.44534 | -47.95794 | 2025-06-28 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 770bdb5a-7af6-39a7-b606-2cd5f5b2863a | -8.56234 | -51.57304 | 2025-06-28 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39e844cb-661d-3eba-873c-52e7b5a01899 | -9.43414 | -47.96342 | 2025-06-28 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c210a15-21ab-3485-ab5c-eab668b02065 | -3.46375 | -47.6791 | 2025-06-28 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 987b62fc-c39a-3c6b-bd40-908497776d13 | -8.56543 | -51.57882 | 2025-06-28 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8a549de-eb5c-32eb-b4e8-f5de79303df1 | -5.41669 | -47.56867 | 2025-06-28 04:27:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 889b8b59-b282-3109-8948-39408fd3b3cf | -9.18733 | -49.66336 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f03d2e3-3105-322b-9728-31995880b23c | -6.90223 | -43.9756 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f1a0e9b-438a-3f6b-8bb2-c98e29d33a4c | -6.90924 | -43.97667 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7aa190b4-ce72-328f-91f7-f2681ad8f120 | -6.90104 | -43.98342 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 32cb6506-f5b0-3741-ac15-5a2e871d5574 | -5.41748 | -47.56846 | 2025-06-28 04:27:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25f2821a-e3e7-3ca8-9a22-8cc6b7a42271 | -8.04197 | -47.65181 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 974ad664-0a51-368a-b357-9aa1cc9b4a6e | -4.43156 | -47.6161 | 2025-06-28 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2411a4e5-96df-3a6d-9f33-2ebb13084fd0 | -6.71809 | -44.40137 | 2025-06-28 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29f9b6d9-1e80-3ed4-820a-8c6acdf78b70 | -7.11372 | -43.36532 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 839b2b89-bc4b-30ec-89dd-3d119a79b4cf | -5.8634 | -46.47857 | 2025-06-28 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82677073-d246-3e5d-95f8-697813ad08fe | -6.89694 | -43.9868 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b343762-cf07-38b7-b632-a51b3fafd14b | -8.03027 | -47.63902 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8f5fbac-d8dc-3214-8e1f-27cc1541fefb | -6.55173 | -54.98265 | 2025-06-28 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 338b4988-209b-325e-ab4f-63deb0f59643 | -9.97002 | -48.24383 | 2025-06-28 04:27:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ccc15f2-5641-3275-b329-c67087d2ca45 | -9.15462 | -46.37563 | 2025-06-28 04:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56e4a33b-2fef-38bd-ba6e-150bc8373239 | -4.37556 | -48.06677 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edc45689-9e17-3a9e-825f-fb037837a0b8 | -6.90566 | -44.00008 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1bc8cfb-9aa1-3640-8980-5e02eabc8382 | -10.32231 | -45.16412 | 2025-06-28 04:27:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8c0ba1e-b0d7-34e5-8e7c-0d97046a8a0b | -9.11386 | -49.49545 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 844effa4-6221-3085-9226-ba9abae5d3a1 | -9.12119 | -49.49211 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c5b64369-b900-3667-a39e-e4ffaea0f11a | -5.44092 | -46.56115 | 2025-06-28 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91c49757-570a-3ce3-b213-c4cbc27d243f | -8.03919 | -47.64772 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3866157-3954-390b-a09a-f0e04211ebd7 | -9.11259 | -49.47857 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5b74f58d-d35a-3862-b679-362506339548 | -5.6208 | -44.01126 | 2025-06-28 04:27:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c29afa6-f915-359f-b5c8-d97480eb3694 | -7.1131 | -43.36946 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60512a04-b9a7-34b4-878d-fb15277cdf22 | -5.20545 | -46.83115 | 2025-06-28 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ba3e3d2-178b-332c-be7a-fa57ebaae1a8 | -6.89873 | -43.97507 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fea5eaf8-27b2-3d8d-869b-765461b381f7 | -6.55553 | -54.98238 | 2025-06-28 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d723ba8b-80e6-35b2-ba9a-9c644d34dd26 | -9.11226 | -49.48303 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6f19124c-dcbe-32fc-802d-f79a7c538fca | -8.8539 | -47.50654 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03ae3eef-353e-3840-9064-5f59a3cb612b | -9.36867 | -47.63279 | 2025-06-28 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10227b41-81bf-35b8-aa6a-ddd1efd4bc34 | -9.11193 | -49.48251 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 915356bc-bd58-3e95-9b87-1e8d68cca237 | -7.20744 | -43.08911 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ae9bfb58-16d5-3621-885e-4c59cc2e7440 | -8.85 | -47.50951 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a184aa9-abc5-305a-bd97-c6bd8fce216e | -7.20808 | -43.0848 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c480776b-fbcf-3f36-959e-3863e4cf56d7 | -4.8142 | -47.32178 | 2025-06-28 04:27:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee3e522b-79ca-3ed5-9b8d-232a8af03624 | -8.84307 | -49.85846 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9afe878-f7a0-3e05-bfa3-251660b01872 | -8.3186 | -46.22931 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b0484d5-e769-3a60-8351-27167327fffa | -6.90865 | -43.98057 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f019e39-658d-399c-bffd-42c8c769f045 | -7.54551 | -45.82403 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 47256da8-e8b3-3fc9-8372-93bd72f61074 | -7.5483 | -45.82809 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb0a1482-3a3e-326c-bb8f-ec6b6a82db6b | -8.85333 | -47.51006 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74ff1969-fe09-3356-aa4c-ae4b32472514 | -6.90276 | -43.99565 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0e96977-1da2-3e5c-b730-e10d28930db8 | -6.94891 | -42.8778 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4be5d2ad-dead-3cc3-9351-5f40a49651a3 | -8.05094 | -47.63869 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63fb1bb4-eb2b-32b6-a7c2-d104a57316cd | -6.90685 | -43.99228 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90fca282-dfd7-35f3-983e-0de5314d74d3 | -10.0059 | -48.12857 | 2025-06-28 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1c38a8f-6d6f-397b-aa72-97f1516dc5e3 | -9.69642 | -48.33276 | 2025-06-28 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7637246-3347-3c48-8473-1b73b82c2c3b | -10.00532 | -48.13214 | 2025-06-28 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a3147c8-2c36-3770-8f5f-b196f834196a | -9.11546 | -49.48308 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a3585187-9bf6-302b-b47a-08a742d6b351 | -9.11612 | -49.47913 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 75337b2f-e023-3712-8139-df38faed290e | -6.23501 | -44.52607 | 2025-06-28 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92a87b93-d7b1-3b71-8908-b525c6b7fb64 | -4.37904 | -48.06732 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe98902f-7b19-33a2-abdd-a633419a5ca6 | -7.21909 | -43.08648 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| fd48569b-b676-3424-8670-2b1f79bca890 | -7.10155 | -52.58729 | 2025-06-28 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dd3218d-1abc-3e7f-89a5-e66f0bf82bc0 | -6.95238 | -42.90511 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9f6aced-f42e-38d2-9e33-ac49279efa3c | -6.94521 | -42.87722 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| ca8477f5-7351-345c-9283-b5e1b1ac3db1 | -9.36924 | -47.62926 | 2025-06-28 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89bd5095-fb37-3723-8a7c-3cf349cbe654 | -6.44753 | -44.57295 | 2025-06-28 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| effd5462-9f6d-34fa-9661-9aad3ae8351a | -9.36534 | -47.63225 | 2025-06-28 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ed634ed-5c39-3a28-ac27-347ef26166f7 | -6.73959 | -47.22624 | 2025-06-28 04:27:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 632e2ada-6f6b-31bd-935c-9701dfaacb7d | -11.01398 | -45.24247 | 2025-06-28 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 77145f62-c552-34ab-bae2-0065872275f5 | -2.49628 | -54.13201 | 2025-06-28 04:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README16.md)
