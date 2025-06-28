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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c14bb2c-90f4-3ed3-93cd-e66a08d1fd75 | -9.69175 | -48.33261 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08e37575-66c6-3e7d-8467-5c55ddf0912c | -6.44882 | -44.57124 | 2025-06-28 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ecc3a93b-4c22-3eca-b6ee-ca2b4469fdfe | -5.86731 | -46.48267 | 2025-06-28 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d820429d-7254-3470-bd65-30016743d790 | -8.84208 | -49.85585 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d42968a9-ce82-3c9c-bc85-cd3d8992e536 | -8.03701 | -47.64766 | 2025-06-28 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c965a89-e744-30d6-8211-c89aff2647ba | -6.90838 | -43.9821 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ceb67724-e3f9-3631-b569-e0607ce7a9f5 | -8.74156 | -47.85225 | 2025-06-28 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59c6ab5f-ea77-388f-ac4f-e63ae60a40b0 | -8.73694 | -47.85126 | 2025-06-28 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b643575-404f-3a39-b199-0edd83384634 | -8.00322 | -49.70936 | 2025-06-28 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb9e7869-e2e9-3e2e-a3e9-f210bd62c174 | -10.83579 | -53.76768 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b8d2e2f9-3fcc-34a1-85c5-1eb157dd3a85 | -7.19777 | -43.18706 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86551dd9-5026-3e68-b39a-7460a344a060 | -4.54301 | -48.02185 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| c66f41e8-b519-3153-bc5d-3689e01577f4 | -9.11816 | -49.4968 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7e948d9e-f5f8-37ba-9958-0efff6d89f06 | -7.15291 | -43.37911 | 2025-06-28 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe59e30a-a19d-34db-9cd9-f1c032928444 | -9.12097 | -49.48128 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e3f2252-52a3-3504-99b0-22e3e3c9d453 | -6.9002 | -43.98532 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 06453235-070a-32c8-8506-e869f5fa60b5 | -10.53858 | -42.53349 | 2025-06-28 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b0928071-0dad-3ab8-ab4b-1c0b7d26449d | -7.21644 | -43.07483 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 03885311-c629-37b3-a7ce-9887cdf7e1c5 | -6.90466 | -43.98149 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 14df132c-b4f2-383d-ae43-6041c2fea804 | -12.47102 | -44.92598 | 2025-06-28 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7f0571d-94b8-3515-a980-ca0ad429db8d | -5.46836 | -43.07238 | 2025-06-28 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6daa1afb-f00d-304e-b869-5469ad7c7454 | -7.22293 | -43.0791 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1953341c-7c06-3718-9c61-dd3251c18d34 | -9.87465 | -48.60713 | 2025-06-28 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21e12c9e-c2b2-30a3-a167-2ae69201b9b9 | -7.20133 | -43.18763 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a76f68ef-734b-3b44-857c-9b98ed440bec | -8.84147 | -49.85926 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8314968e-429b-3af1-948e-505b9f624607 | -8.5633 | -51.5757 | 2025-06-28 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcc73f72-29a6-3026-a58f-682550c1c808 | -7.20201 | -43.18357 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b3e6f5f-83c0-30c1-8c84-cf289c371063 | -10.84458 | -53.75755 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 494d2704-8ae1-3a6f-b7cf-35e96e4461b2 | -7.21585 | -43.07796 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 9dec1cbe-ee21-35d3-9654-a40503579fee | -7.21516 | -43.08284 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| d92d0334-c686-35c2-a786-4dff3df24993 | -7.11402 | -43.36853 | 2025-06-28 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ed1d5b2b-8a28-3dfd-9cc4-f99257d48f99 | -6.90991 | -43.9961 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1253d11f-f4c5-3335-ba1e-ce26529c19e5 | -6.7176 | -44.40743 | 2025-06-28 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15edfd36-862c-3a4e-9710-3bd56686c647 | -4.54332 | -48.02618 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 1151f422-d26a-31cb-8911-7ffec48434a6 | -7.5442 | -45.83614 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15f0deab-be82-3eb1-b74c-699623a92218 | -11.66241 | -46.73401 | 2025-06-28 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 317af9bd-d346-3c0c-a4dc-4ff2e44f1b93 | -8.8613 | -50.16082 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af2c01ee-7892-31b8-bb71-0da0de34e5fd | -6.9151 | -43.98779 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce4b89d3-ffb9-3740-94d4-241d209e20d3 | -11.96018 | -47.19159 | 2025-06-28 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb0718c6-a908-3c29-997d-5459471752e8 | -8.90921 | -49.84125 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3ac27a9-75f0-3fce-8797-929e3f9a83e7 | -7.21518 | -43.08197 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 707264f4-45b0-3b6c-aa1b-bc77a6b42a41 | -8.04715 | -47.64436 | 2025-06-28 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba6e22af-1f95-3dd7-8ba6-40579a734c68 | -9.11298 | -49.49593 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c2e4ec3-54c4-38a7-a50c-cf06be8dcbee | -8.85466 | -47.50966 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 432675e9-7791-357b-8814-34b202192e76 | -10.53521 | -42.53296 | 2025-06-28 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96dd685c-5ab3-3c4d-a271-2bb2122618cd | -6.45189 | -44.57671 | 2025-06-28 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36ee4217-e3ff-38b7-9894-557bb80872e9 | -10.03301 | -54.3196 | 2025-06-28 04:02:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00c092a2-da83-3200-84de-a74198075d00 | -7.10141 | -44.36831 | 2025-06-28 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8d04957-a1e3-37a7-b6b2-fadd741995e3 | -5.20614 | -46.82937 | 2025-06-28 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cee375c-7a20-3a3c-81d1-c211cea59742 | -9.11522 | -49.4836 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 26a57d90-b550-3d93-9d7e-bdc96ea126e2 | -7.18803 | -45.32485 | 2025-06-28 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfb79566-42cb-334e-9509-8eae00ea1051 | -5.46046 | -43.07543 | 2025-06-28 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 599161b5-0663-3413-b201-9f5494a6c4bb | -11.54133 | -43.24308 | 2025-06-28 04:02:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1effcdb8-360b-3e78-9a5b-e56dc1341ee7 | -7.32358 | -43.17313 | 2025-06-28 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6226ca4c-569c-3213-92db-1fff8f1b1635 | -11.67194 | -46.72798 | 2025-06-28 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a93310a8-92e9-36ab-ac4b-12330b8f842f | -6.95027 | -42.88129 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 345a3602-2ef9-34c8-953b-8ca62583657f | -10.84348 | -53.76315 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4fb54e3d-a82d-33c3-904f-cfdb5aae0529 | -5.46408 | -43.07598 | 2025-06-28 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37b5a59c-6156-35ba-b259-61843c1b7110 | -6.91214 | -43.1811 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9189798-00f0-3c24-8f53-1dcbcd9bf2d8 | -6.9474 | -42.87679 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d39421cb-5c8c-3063-903d-bbd0a7002402 | -4.54935 | -48.02113 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e76e5e44-2596-38fb-9120-89986c1d1857 | -9.43439 | -47.96328 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c90e8787-07d6-3b93-a34a-9e3b6defd4aa | -10.83806 | -53.75619 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1fcf7e6c-9ddb-3b88-b5e5-e72445cd0533 | -11.66782 | -46.72734 | 2025-06-28 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b0141ae-5478-357b-9665-10c471dd884c | -7.19052 | -44.18098 | 2025-06-28 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3f6fe8e-8794-3423-af65-f9968298ea7a | -5.44087 | -46.56232 | 2025-06-28 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb665ea8-8ff3-3221-bfb7-d149e6704329 | -10.82614 | -53.74776 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76fcc4db-c61e-3c18-9f28-8df65a90e249 | -7.22581 | -43.08367 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| d37a46ba-4ddc-3405-bf6b-2f2ecd45d20c | -6.90985 | -43.97319 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 043629a2-34d7-39b9-b14c-ea631daaf297 | -7.70674 | -44.58592 | 2025-06-28 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e7a3c7-d177-3969-b35f-3fb459aa2cd0 | -10.95944 | -48.15553 | 2025-06-28 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6f391ec2-a5c4-3283-b180-27e80d45e58c | -4.54886 | -48.02409 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 901abe64-abcf-3421-aec1-b92a351e22a6 | -6.90912 | -43.97765 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 77fa0f68-fe8b-3435-bb47-fc2deebad49c | -8.56926 | -51.57682 | 2025-06-28 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 332b7d51-a43a-3528-b8e5-1c2844b62141 | -7.21873 | -43.08253 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7c82fdf3-fdfe-34b4-b7a0-300e50e6cb3c | -8.85522 | -50.16342 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a2bb40a-d06a-3571-9d6b-74f59de79d95 | -7.549 | -45.83299 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a6f1bb3-b7e5-3287-a82b-99749afcb86c | -9.73972 | -48.34373 | 2025-06-28 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b6cdbd1-300c-3f60-91bd-78dcf22943e6 | -8.05264 | -47.64024 | 2025-06-28 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca349c99-d91d-3c18-8358-ee70a924a389 | -5.43866 | -46.56351 | 2025-06-28 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1913610e-c058-3a64-b580-452b0fce1d2b | -6.74234 | -47.22153 | 2025-06-28 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a28e2c9-78ea-3adf-8fe5-17e5a3798065 | -8.00261 | -49.71277 | 2025-06-28 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 289f4997-9a24-303c-8b7d-e75a781ed005 | -10.82504 | -53.75333 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51196799-b195-3374-89db-fa7103ad8f67 | -7.55378 | -45.82991 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82b7cd0c-4461-3164-afb4-4aa40b15584a | -6.89795 | -43.9758 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca2a6267-0384-37a6-abb0-ab63d8531041 | -6.90094 | -43.98087 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4347c323-6551-3856-91f4-5b487fc94c2a | -10.52905 | -42.52821 | 2025-06-28 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 44fd54a1-7f60-368f-bc27-26f0a3dd1cc4 | -5.45979 | -43.07961 | 2025-06-28 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c0ea34a0-7a1d-3070-a996-a2ee9f862431 | -6.91437 | -43.99224 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b91cdda-0578-3b56-8cf1-04a9ebfd1fee | -15.55286 | -42.65755 | 2025-06-28 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 32985b10-10f8-3bcf-b4af-f1f6fde8622d | -16.45275 | -49.51828 | 2025-06-28 04:04:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c58644c-de67-3ef0-b034-ad72922a3333 | -11.57845 | -52.10915 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 922b96aa-fd9e-3024-ad09-a3411b4e5a85 | -10.83498 | -53.7656 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9ae4f557-f91e-3f3a-bb1f-c5515f15d615 | -17.09466 | -43.80552 | 2025-06-28 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0417b40d-bfe8-36f5-96a6-81e005f3c873 | -12.25904 | -46.77037 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5b5ea3ca-c3ae-3f56-8c88-460c7a0fd237 | -13.6462 | -46.81579 | 2025-06-28 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e68ec77-1a3d-3091-bf59-b269c7f342f7 | -19.94518 | -45.24449 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e374bbb-542f-3829-80d3-dd1b079f95a9 | -16.13005 | -47.48992 | 2025-06-28 04:04:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 631522ce-d897-3db7-b99f-750bd3de8bcd | -12.26378 | -46.76741 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f5deaa2-cc3d-33e2-a8fc-dcf12745ae5c | -12.10652 | -54.58623 | 2025-06-28 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README12.md)
