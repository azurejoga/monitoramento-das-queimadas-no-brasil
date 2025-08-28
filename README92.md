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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f08dcf26-744f-31eb-962d-441ec9048385 | -10.7021 | -47.09235 | 2025-08-28 12:34:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 4ea3e2d2-943f-3704-98bf-234e00a84f1c | -7.24938 | -45.4305 | 2025-08-28 12:34:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2c4cbc51-1160-341e-858e-6fed31eed57b | -11.56239 | -47.621 | 2025-08-28 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ee287fe2-b7e6-3d81-bbd8-4e42df4cbc51 | -6.39296 | -45.58542 | 2025-08-28 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| e2e29a24-2865-3901-846d-18c5c3b076bf | -5.3085 | -48.186 | 2025-08-28 12:34:00 | TERRA_M-T | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d91a6b91-5627-3bc5-a187-f2d729d1e6b4 | -7.23986 | -45.43963 | 2025-08-28 12:34:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f9b02a2e-231c-3474-9775-bf46b2ba0f9a | -8.19389 | -45.07044 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 81dca561-9d19-3313-9164-236859367964 | -9.68354 | -47.08574 | 2025-08-28 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 32d4238e-8792-32f0-907e-0d9ddffd0fa7 | -5.91336 | -46.16278 | 2025-08-28 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c2d6be8a-3a4a-3005-87e5-daf71e66fb78 | -6.86892 | -43.60705 | 2025-08-28 12:34:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 88da419b-c9c2-3771-a231-0cbfb3d536b0 | -8.73628 | -47.39463 | 2025-08-28 12:34:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4d469b55-cb8c-3794-81da-9f147b7da430 | -9.44749 | -48.26698 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 580c7dd7-b5cc-3bf6-b8b0-01051c79ea79 | -6.15829 | -44.05496 | 2025-08-28 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 465.0 |
| 65e71dca-6724-32e0-9162-f27731f22948 | -7.72994 | -44.92655 | 2025-08-28 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 44d4573e-561d-3c4e-be45-2d3d94f2f92c | -10.47999 | -57.96236 | 2025-08-28 12:34:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 61b3f895-8526-3297-b316-49a86baef77d | -6.39095 | -45.60086 | 2025-08-28 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| dd61193b-9cf6-3b44-9ee3-e247ce1356b4 | -5.56396 | -52.0728 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c6bbbc77-0a8a-3ed4-896c-0bdf3ff17265 | -6.4454 | -44.56573 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 17bdbd0b-fa5f-35f7-aacb-04b96ea32320 | -7.18743 | -44.87434 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 4d761d13-15d4-3833-8d92-ae46cc1e165f | -8.27502 | -45.1841 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a242532b-5f42-3b05-bc0d-6c59659479db | -9.75732 | -47.93254 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 3dc47915-5ca5-3930-9650-5c2b5747d050 | -11.57894 | -46.40903 | 2025-08-28 12:34:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 1ca1c59d-e066-397b-bf93-2fd079d4f74b | -9.96305 | -46.50711 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 94156dcc-c260-34a0-b8b9-988090f04da1 | -11.35592 | -43.53329 | 2025-08-28 12:34:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 0d030569-3106-35d9-aa4a-16d54c94a68e | -3.35048 | -44.19727 | 2025-08-28 12:34:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| bc273ca9-7f7e-3475-b3e1-a7dc87703514 | -9.9724 | -46.52316 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 4dfc3172-a033-3503-9794-de91e7df9ef3 | -7.31817 | -46.12769 | 2025-08-28 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 70a5d608-fc26-3121-a32d-353c1760b6e7 | -9.43917 | -48.25461 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d1867ea3-acdb-340e-b8e6-feb83ee90dc0 | -9.72643 | -47.17217 | 2025-08-28 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 00a7c359-0582-3cc5-b851-ef5f11563370 | -6.57341 | -47.38074 | 2025-08-28 12:34:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d378cd72-2bad-3aed-b587-d9dc2adfd21f | -9.67391 | -48.3211 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6c00fb81-8cc3-3a56-b150-891511e2905c | -10.30195 | -46.81123 | 2025-08-28 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| bd151939-87bb-3b89-91c2-32cae810263a | -3.23717 | -50.10955 | 2025-08-28 12:34:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8c855ec7-ec47-3f3d-9af9-38757ee21a32 | -9.18558 | -46.76472 | 2025-08-28 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cc2b4c2c-13f6-3c50-9ca4-8eb826570a2a | -6.42838 | -44.57487 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9a2cf7cf-42b6-3602-ab65-6f31a797737c | -6.23776 | -44.72059 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a9a2a4ac-b081-3d62-8f37-4984fe04ffc0 | -3.42781 | -49.0447 | 2025-08-28 12:34:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8b6fb5e1-74f7-36c5-89e4-0ce22de494c7 | -8.92441 | -46.65588 | 2025-08-28 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 3a2beca1-1c84-3dd4-9611-6071a22dda33 | -7.32015 | -46.11319 | 2025-08-28 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 0f652d9e-8acd-3cc4-ad45-5ab9a23c4a18 | -10.4685 | -57.95374 | 2025-08-28 12:34:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 8153b5ed-b2af-31a3-9608-e6f85caafefe | -6.94799 | -45.72433 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 3abda031-eefe-38bf-a89d-551ab2c57471 | -3.35292 | -44.17982 | 2025-08-28 12:34:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e70eb6a0-566e-359e-aadd-3a130234d1d0 | -6.28668 | -44.47622 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bd8121aa-952a-3f49-9958-80aa4428d910 | -7.20171 | -44.06905 | 2025-08-28 12:34:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 88fe6c59-19ab-3ebc-91df-6b9b31a603cc | -10.4706 | -57.93972 | 2025-08-28 12:34:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 0867dbfa-3b0f-3103-8390-cae9836bb0c9 | -6.08971 | -44.67744 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 9478dd12-54b3-3bcc-a3e2-8432d5699da1 | -6.27255 | -43.69276 | 2025-08-28 12:34:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| f036e6fb-a476-3866-93ba-14d9b9c34967 | -9.68525 | -47.07241 | 2025-08-28 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 5a6b7f01-23da-3a74-8bec-6b4bd6d89fcf | -6.44305 | -44.58396 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| b3331d7b-89ca-37fd-8f94-aa803e743c69 | -10.49632 | -53.66056 | 2025-08-28 12:34:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d08415d0-8c12-3e05-9caa-c7ba68457141 | -8.73789 | -47.38242 | 2025-08-28 12:34:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 69003439-e230-32a2-a946-385d97d51467 | -6.2716 | -43.67591 | 2025-08-28 12:34:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 2594b14b-c80e-33bd-a4d4-ee44bbdc3398 | -6.2755 | -43.6708 | 2025-08-28 12:34:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 41450ffc-eb3a-3362-82e4-06ad1f9874c2 | -6.8661 | -43.6291 | 2025-08-28 12:34:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 145cf180-81b8-304b-a95a-bd6f2a9a9dad | -6.24541 | -46.62569 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d154f14b-9c68-3559-92d1-fa3bf7d29786 | -11.3382 | -43.55873 | 2025-08-28 12:34:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 231635be-5fcc-3fc3-a38c-0c21bafbfe2d | -7.32254 | -46.10528 | 2025-08-28 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8a8ecf74-405b-3cf5-858d-9ca42972eb56 | -11.92952 | -46.70553 | 2025-08-28 12:34:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f75b49a5-4456-3fd0-b5e2-232208e2d21f | -10.97211 | -46.8521 | 2025-08-28 12:34:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| cd807ef5-4cb3-39c2-a56d-4b8bf48f3a36 | -6.28484 | -43.67814 | 2025-08-28 12:34:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2ed9ddc6-b3f1-3024-b191-a5b2c45e5df1 | -10.49218 | -51.61347 | 2025-08-28 12:34:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2ad8ecfb-6b9a-306c-b283-da5bd3b2dd15 | -9.43185 | -48.30968 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2d9b2379-8df1-3752-8ee3-c39424d8eaf6 | -8.27122 | -45.1779 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 639919f2-03a0-3a66-bd3a-a1ef6fe2b1a5 | -8.26274 | -47.20698 | 2025-08-28 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f5fc11d8-716e-3d6a-a821-ed33dedf2b1b | -9.51501 | -45.5611 | 2025-08-28 12:34:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 5177b40e-befe-3e20-a552-3790abccdb46 | -8.55531 | -45.79856 | 2025-08-28 12:34:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 10c94dd3-cfdb-39d9-a1de-5b48d5b5f419 | -10.97022 | -46.86664 | 2025-08-28 12:34:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| b31846dd-dced-363e-99f6-62b84425b6a9 | -11.26824 | -52.74321 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 881f3ca0-9aa8-3ea3-ad22-5767f084450d | -8.27726 | -45.1661 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 5e84f847-aa74-3176-a234-e571a76ec598 | -3.357 | -44.18691 | 2025-08-28 12:34:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 7f65bdee-7e94-3875-a4d9-825a1af74b1a | -9.78728 | -45.72422 | 2025-08-28 12:34:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 35f2d2eb-b353-3fbb-ba33-e1dea0a36937 | -10.30024 | -46.82456 | 2025-08-28 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 05ce1b9f-e801-35c4-9a0d-39ae28672308 | -10.37786 | -45.17699 | 2025-08-28 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| cb7488ad-dfd9-3393-9ae1-3f439737255e | -2.44706 | -47.32399 | 2025-08-28 12:34:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b365f5a0-8126-35ad-90a7-0c5c863747ca | -9.6851 | -48.3121 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| eaa379bc-f3af-3c02-a030-17b636327fe5 | -7.18863 | -44.06738 | 2025-08-28 12:34:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 54f5b0f5-cc18-312f-8e23-ce5d52519766 | -11.56725 | -46.40817 | 2025-08-28 12:34:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 308.7 |
| e90fb7b5-9c8d-35db-818c-838af0c94710 | -6.25025 | -46.62064 | 2025-08-28 12:34:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 32c8a148-969f-3eb0-ab1f-e0a1d0603d78 | -9.16639 | -56.98803 | 2025-08-28 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| cdb5f08d-752f-38d7-b0d2-f7a86c3e51d4 | -9.50828 | -45.56593 | 2025-08-28 12:34:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f6069087-8e50-310d-a6c4-287d3b251112 | -10.46726 | -57.95958 | 2025-08-28 12:34:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 757b70bc-625c-38e4-8ac2-b9ac704bcc9e | -10.37673 | -45.17045 | 2025-08-28 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| a9d94b12-88a4-33e6-ad4f-3282633c07fc | -7.64217 | -46.55557 | 2025-08-28 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 27abd06e-0e86-3a28-8f3c-ffd834b78066 | -10.52367 | -46.68914 | 2025-08-28 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0b7cef16-c77f-33b7-a4d3-0ac267ec6e42 | -8.89032 | -60.76871 | 2025-08-28 12:34:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 3936c326-d8fb-3500-b9ae-c860d635db72 | -6.18378 | -44.15886 | 2025-08-28 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| cf33f1eb-aaac-32f1-a822-84ee43d67244 | -6.95 | -45.70904 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 184d12ab-c3e4-346e-9f5d-120c84285dc6 | -8.19954 | -45.0598 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c32ce4e8-1151-347f-867c-b757cd749e13 | -9.74172 | -50.60545 | 2025-08-28 12:34:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| db8c443c-f5f3-3b7e-bba4-5610bd7f0690 | -9.64787 | -45.57229 | 2025-08-28 12:34:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| aff46428-7ecd-3012-8d32-b5798d56fe7b | -9.16347 | -57.00594 | 2025-08-28 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5097d371-8829-3ead-90a3-7773f7758c18 | -8.52985 | -47.4234 | 2025-08-28 12:34:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9c0dfebb-d7f1-330d-8e0b-111bc0b8df8b | -3.42512 | -43.27963 | 2025-08-28 12:34:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 3dfff8cf-7f4c-3dd3-a9bf-91c8b228ff82 | -7.23762 | -45.42942 | 2025-08-28 12:34:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ac479e42-c598-38af-974e-8b41f9f61827 | -6.13562 | -44.42506 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b99533bb-0256-3491-a621-771c98f48438 | -7.32066 | -46.11986 | 2025-08-28 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| d28b941f-b7e4-3630-bc06-39393b0c7697 | -10.70385 | -47.07858 | 2025-08-28 12:34:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 2fe0009a-c98d-38a3-a4e1-7783f6f498ca | -8.08945 | -44.97865 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4aa34507-128b-3459-a666-e8ec7e628440 | -10.3241 | -46.81323 | 2025-08-28 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e20db2c4-52d5-3ab5-af92-7916edd5dda5 | -6.43071 | -44.58196 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |


[Clique aqui para ver as próximas entradas](README93.md)
