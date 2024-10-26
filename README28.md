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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cca9ce7d-a555-3dc7-9842-74105877600e | -3.00234 | -50.49195 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e4fca9df-7939-37af-88bb-2f05c04f35b6 | -3.00157 | -50.48403 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 8537ec44-3228-3e17-9239-32e868f68011 | -3.00055 | -50.49009 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b699916f-b750-31a9-b24f-4907da0659ee | -2.99952 | -50.49624 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 37cc9aea-af96-3390-938e-a1bf37115795 | -2.99662 | -50.48482 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 70cefc7e-1bc4-3158-96d2-673a8640d791 | -2.99557 | -50.49085 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ed1b5aab-2bc4-3170-99be-fb089296c08b | -2.99478 | -50.48302 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b46aa052-cd7d-35ee-af0a-4638af70b053 | -2.99451 | -50.49695 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3bdb9a0d-c5fc-3978-a18b-0898c6546f76 | -2.99377 | -50.48901 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3342c1c3-3932-3d34-b30a-65885d129b78 | -2.98981 | -50.48393 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9e9acac1-5861-3bb7-9510-8c2cd92eaa0e | -2.98794 | -50.4823 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 501fa39d-7ca2-3ec0-9499-57217aef88df | -2.96673 | -50.41763 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4dfb373f-e887-3e08-8db9-41633a7b12e1 | -2.96567 | -50.4236 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6597a71-e5af-387a-8eb7-21fe14db9e20 | -2.96461 | -50.42962 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed1e072c-e993-3c88-9421-11f6805a57c3 | -2.96452 | -50.41549 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3648520-6ece-3ca2-8539-cb4e3fea9e20 | -2.96349 | -50.4215 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50c780f9-4c80-3e94-befc-af9c962a21f6 | -2.96247 | -50.42752 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2f80ecef-badc-3f9f-8c43-1b788f9ec452 | -2.95674 | -50.42043 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35daf5a5-074a-3213-aef6-881a9a497d2f | -2.95571 | -50.42645 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1a98fcf5-1db9-3418-9ad5-ba4fb65f318c | -2.95467 | -50.43254 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 74eda02e-75a1-3734-834d-0793f92aff1a | -2.19058 | -50.49862 | 2024-10-26 03:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a97166a9-b122-31e5-a1c8-3dbcb7ba7c5a | -4.74393 | -43.25379 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ae6feaf-9651-3628-80b1-ed208afd94cf | -4.74334 | -43.25745 | 2024-10-26 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f99eb07d-6a8a-388c-bf37-fbc014d25e9c | -5.44109 | -40.82365 | 2024-10-26 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dcfa6b8a-6d13-3ba7-a5a1-0115265e1e54 | -6.22613 | -35.2508 | 2024-10-26 03:55:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b20e7844-f900-3c5f-bf0f-a65798f00886 | -6.22402 | -35.24785 | 2024-10-26 03:55:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 075c6b92-746d-3895-b99f-70ccb0e005c9 | -6.22338 | -35.25197 | 2024-10-26 03:55:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 336a7a79-081b-3741-867e-7f86ab8198c3 | -6.21981 | -35.25141 | 2024-10-26 03:55:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| b0f06ce6-82fc-3c05-a61d-7f062d7e40b0 | -5.56063 | -35.58515 | 2024-10-26 03:55:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 77dbddba-68e5-3ae5-a242-d63b89d46925 | -7.45463 | -34.91352 | 2024-10-26 03:55:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0dfca6e9-9235-3b8d-8f8b-a1b65a6c0a40 | -7.36659 | -34.89581 | 2024-10-26 03:55:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3fd01d75-b5b3-328d-8a55-de03f90c37fd | -7.36365 | -34.89703 | 2024-10-26 03:55:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2d8018a0-0263-3eed-99e2-ac333a48d9bb | -8.97324 | -35.1844 | 2024-10-26 03:55:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 41afdc72-02e1-32fd-a07b-7ac962f01639 | -8.89404 | -36.24052 | 2024-10-26 03:55:00 | NOAA-21 | ANGELIM | PERNAMBUCO | Brasil | 2601003 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9124f8c-3752-33e9-a78a-0b9abb323153 | -8.89053 | -36.23999 | 2024-10-26 03:55:00 | NOAA-21 | ANGELIM | PERNAMBUCO | Brasil | 2601003 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a9e26c6a-d755-3b29-9630-191836777cd1 | -8.88702 | -36.23947 | 2024-10-26 03:55:00 | NOAA-21 | ANGELIM | PERNAMBUCO | Brasil | 2601003 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| afdc308f-86d7-3b49-b8ee-9cbc351dcad5 | -8.07347 | -34.97669 | 2024-10-26 03:55:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e569a946-f9b4-38e7-9630-782e3c455274 | -9.70759 | -36.53689 | 2024-10-26 03:55:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0d0b7e53-781a-32c3-bb45-8463c1265f34 | -11.83635 | -37.94716 | 2024-10-26 03:55:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c0b05cfb-394e-30de-8f5a-29781afc6522 | -5.17965 | -37.989 | 2024-10-26 03:55:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 74247b85-ec1e-3618-bb13-b5c3c7d9e817 | -7.57473 | -39.02815 | 2024-10-26 03:55:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4999d7e8-bd1f-3cdf-986c-95cea859ff98 | -7.55406 | -38.75169 | 2024-10-26 03:55:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9a25b4d8-3801-39af-b8f9-5d61b47b2e9e | -6.81507 | -38.23372 | 2024-10-26 03:55:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3825482-9ffa-3a6f-ba3a-884ed9932d9e | -6.71519 | -37.50015 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7b9771ee-cff7-35cd-b768-f595c6de2e7c | -6.71187 | -37.49967 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bf50d896-0801-3c98-8203-80ced6f944a5 | -11.20933 | -39.91091 | 2024-10-26 03:55:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| adc15f76-dfaf-308c-ba58-6397e840a33a | -12.4075 | -38.83924 | 2024-10-26 03:55:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2a06d6fe-696e-3e5d-a537-548fa17f3856 | -6.50549 | -39.35443 | 2024-10-26 03:55:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90dfdd06-7f8b-3824-8a4a-5f32e9408a87 | -6.33246 | -39.51922 | 2024-10-26 03:55:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e98db3a8-dbf6-3a7a-be0d-a8ed222525ad | -5.99778 | -39.07899 | 2024-10-26 03:55:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 247bf202-c2e0-351d-975c-989750ab0261 | -5.94659 | -39.68077 | 2024-10-26 03:55:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c2c7b959-8915-37f3-8767-168d3ab066a7 | -5.47033 | -39.67521 | 2024-10-26 03:55:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d9709b5f-829f-3fb3-bb52-9b7fba181aba | -5.44672 | -39.77919 | 2024-10-26 03:55:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52e70e39-28b7-31df-baba-c4e0ebd8a639 | -7.30454 | -39.14502 | 2024-10-26 03:55:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5677063f-07ca-3ab3-8b17-4b535b724415 | -7.01976 | -40.05151 | 2024-10-26 03:55:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9ccb04cb-128b-3e2f-bb2e-b502b93672a7 | -6.97544 | -39.24587 | 2024-10-26 03:55:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c6fe1cdf-fc2c-3ed1-a70b-f4ea00176024 | -6.97489 | -39.24936 | 2024-10-26 03:55:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6da30d9e-b6b5-3b76-bbd5-2ae5d38e4a42 | -6.97158 | -39.24881 | 2024-10-26 03:55:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41f1a7ef-99be-3710-b545-9881f652b3d6 | -6.96549 | -39.24428 | 2024-10-26 03:55:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 55413c1c-d939-3d09-89e9-58d935831d91 | -6.90256 | -40.00686 | 2024-10-26 03:55:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 081f3307-1bf8-3adf-8c3b-c33dc2f26a18 | -6.89918 | -40.00633 | 2024-10-26 03:55:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4ea05f47-374d-348f-a849-5b4e788d8785 | -9.35581 | -39.9224 | 2024-10-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb845056-e7e5-3034-abc6-83acb7846fd3 | -9.35248 | -39.92186 | 2024-10-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6b3a432f-14d9-38ca-96d6-8d80a304b858 | -9.35192 | -39.92538 | 2024-10-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66838ee6-d23b-31b0-8f72-e7fad2f29066 | -9.34583 | -39.92078 | 2024-10-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b5dde945-7017-3adf-bf74-ea803a9e8804 | -9.34526 | -39.9243 | 2024-10-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 293a52c8-a40c-3cb3-a036-b96ccd23fe63 | -8.81456 | -40.26611 | 2024-10-26 03:55:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a276e84e-28cd-37cf-b170-60ddba3d824a | -8.20655 | -39.83037 | 2024-10-26 03:55:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74ef393a-9639-32e0-836d-51cab0e9f8bd | -8.20599 | -39.83391 | 2024-10-26 03:55:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 770b5e66-d588-3147-9029-9eaa0e084ce1 | -7.9725 | -40.45929 | 2024-10-26 03:55:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c68d2e0-83e8-310c-a833-684c4c2c1f55 | -9.53424 | -40.33919 | 2024-10-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75e5d373-7e5f-39e2-add5-5788c0fb4943 | -9.53089 | -40.33865 | 2024-10-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fab5b478-6535-3f2a-82a8-d2c9d63e6b10 | -12.16479 | -40.87437 | 2024-10-26 03:55:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be679ee0-2a19-398d-950a-f40d22f885ee | -11.73242 | -40.195 | 2024-10-26 03:55:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b2590070-a18c-3d81-a35c-0370358d8563 | -5.05679 | -40.88855 | 2024-10-26 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 54249ca0-6698-3bfa-83a2-8401fcd76e50 | -5.05324 | -40.888 | 2024-10-26 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1e8d6bfd-8a3c-3df1-bc9f-7baea859c6c1 | -5.04613 | -40.88689 | 2024-10-26 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83ded8e1-7e50-3890-8dc5-a00f569a8cab | -5.97954 | -41.51356 | 2024-10-26 03:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 32e77500-b6c8-343c-af15-b191716c0263 | -5.65408 | -41.82769 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 22b3d638-26ad-3ce7-824c-733806eef457 | -5.65336 | -41.83208 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d1c92256-a982-3c1a-ac75-a823d2e34cec | -5.24701 | -41.17113 | 2024-10-26 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e221e63-5e3f-34b8-a15d-1d28b54919cf | -5.24274 | -41.17474 | 2024-10-26 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c47b4c2b-d15d-31f0-ba33-5ae77fdeaea9 | -5.24207 | -41.17888 | 2024-10-26 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 956420f0-5f32-388f-a21c-0b4ff25c1c8a | -5.23105 | -40.5742 | 2024-10-26 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9cca6c0-3edd-34a5-94c2-9b060963f495 | -7.91008 | -41.35811 | 2024-10-26 03:55:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6628bbde-d1a0-37b4-b320-1e6620054e6a | -7.76646 | -41.23483 | 2024-10-26 03:55:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a84ceacd-ad89-37e4-993f-1a08032adf53 | -7.76518 | -41.24275 | 2024-10-26 03:55:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 6384c71e-7a1a-3bdc-8878-c67feccd6e30 | -7.2569 | -41.22296 | 2024-10-26 03:55:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ebe59df-0bb1-3227-bd62-f5f5651cf9ad | -7.25626 | -41.22689 | 2024-10-26 03:55:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8fd5486d-5cab-3b9b-b8b2-2ac9009e6cf2 | -7.00473 | -41.29911 | 2024-10-26 03:55:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3d9f6ce-e7d7-3518-86ea-8f320cd63418 | -6.95753 | -41.32072 | 2024-10-26 03:55:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d7635d6-1f0c-3f6e-81d2-155de6053550 | -6.6901 | -40.89123 | 2024-10-26 03:55:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3a146c89-ae29-3604-bbd9-c76f4bbc1e05 | -6.68947 | -40.8951 | 2024-10-26 03:55:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e1832f44-d7f0-3d33-ac53-625b642708a3 | -6.68886 | -41.23303 | 2024-10-26 03:55:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7fd9a8b4-6deb-3e70-a8e0-58a125e6f4b1 | -6.5526 | -41.70755 | 2024-10-26 03:55:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 894b55b9-0871-31b6-95d0-39a2af7d831c | -6.5519 | -41.71178 | 2024-10-26 03:55:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ca74771b-0a2b-30f9-9462-258f242a01d0 | -6.5512 | -41.716 | 2024-10-26 03:55:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fd486d2d-1cec-3164-b7b6-8a74eceba033 | -6.54897 | -41.70691 | 2024-10-26 03:55:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7863bacb-31ee-3382-8c96-136a1fc09f40 | -6.54827 | -41.71114 | 2024-10-26 03:55:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3fae16de-496f-37d8-aa60-2eea384d2ebc | -6.54757 | -41.71537 | 2024-10-26 03:55:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |


[Clique aqui para ver as próximas entradas](README29.md)
