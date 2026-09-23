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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3964b808-a545-3193-a971-c43e955eb02c | -11.29924 | -51.36452 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e6cab86-c6ac-3cb3-bd74-541569640268 | -6.46545 | -59.98737 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90eaada6-bd4b-3326-bb56-3229f60a0fd9 | -6.67724 | -55.06751 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74d0dd3d-c13b-311c-b10e-26979eaa17b4 | -8.28215 | -54.77342 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f3ffb1d-e9fc-32b4-9664-6dc398f0ead7 | -14.62938 | -45.65417 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00809bf9-4303-3948-8b8b-51271ec22448 | -11.5718 | -47.7317 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 082ff502-fbbc-36e6-9ded-7c856b7598ff | -14.61745 | -45.63246 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 06333896-6ca5-3bdb-8360-cddd3238aefb | -11.43817 | -47.39131 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f092bfd-9cee-33ae-89a0-c6151b5a50df | -13.87043 | -48.56288 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbb6f6c3-800a-360e-a260-ab302d198c36 | -11.35124 | -43.37958 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48bcc3fd-5a12-35ed-848c-d3b111cf4025 | -12.66435 | -45.04055 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e48de15-29c2-3d7c-a04a-3d9db8bbebe1 | -8.80512 | -44.27824 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d21f703-7125-395c-86b0-a89b19fd5d4d | -10.36293 | -50.44584 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 573cfd7c-cfc7-34e4-8be4-e254448acc04 | -12.90682 | -50.89393 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 798f1023-91a9-3596-a496-5a14eac87ba8 | -12.06368 | -50.35226 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b1c3412-be22-3eb8-8dfc-fef15e316331 | -8.80983 | -44.27077 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 46e7c4e8-23eb-3368-97aa-2d3053c6854f | -9.56598 | -47.96021 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5712268-06c4-341a-9596-4ad60e9adbf8 | -14.61508 | -45.64873 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93a23285-fe9d-3093-b863-726972f7c27a | -5.6007 | -60.20557 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f16d8b6-316c-3c7c-bb0f-5a803138ca18 | -6.39006 | -54.88477 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42e4a7cc-c79a-3836-b125-08c88c3d2f78 | -7.1352 | -48.42758 | 2026-09-23 04:27:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c46a6fa4-a006-30c6-818f-89cff4dc84b1 | -9.57433 | -46.53561 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c89bd376-7768-38e4-b06c-b7c34d57c6c3 | -14.38133 | -47.23868 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91aa5afd-2629-3df8-bb26-fa368bc48bd5 | -6.37856 | -55.28191 | 2026-09-23 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36d73ea4-f84c-3bf2-864f-1a286003a363 | -10.00736 | -45.1909 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64398394-56c8-3d65-bd46-33200c2ee4fa | -6.68735 | -55.06965 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de3128db-2d34-36c6-a895-10cfb084d8cc | -14.62801 | -45.63406 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d2b4080-8ab4-3e35-aa20-69103748a48d | -11.10956 | -48.31218 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9444bca2-8192-34a3-adbf-2e6ce0dcd735 | -14.6063 | -45.63494 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4382ddc1-ad23-3282-adf2-63edc6f051fd | -6.61986 | -59.92433 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 23f14b5f-945c-39a6-85cb-9cd32c247912 | -8.77442 | -45.63056 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9f778de-4a8f-382e-976c-15315f070eb3 | -10.26214 | -49.97946 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 351e8d09-129f-399c-81be-2612ef37dc96 | -8.17451 | -54.79769 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fe6151a-36bd-34c7-bbaf-140684fdddbe | -12.75909 | -50.9071 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4e26bcc-2204-3b07-a36f-9a9c446445df | -14.63111 | -45.64195 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 68493476-9e31-3dd3-bdf4-0e99150729ca | -8.59947 | -44.53544 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba2c13c0-d613-3a38-b439-8024a7fce6d0 | -12.78046 | -50.91079 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c0b4834-cfb6-3b6d-8a91-be8457b958fb | -9.84651 | -46.37998 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4bafe615-aa26-32c1-a991-1af600677a71 | -14.70387 | -45.5863 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1696a8dd-523b-380a-a97d-00137757faaf | -12.0445 | -50.35382 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d554732c-27ab-34bd-96ff-9e899201206e | -8.48605 | -46.86604 | 2026-09-23 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cdddf37-edf1-3e95-aafc-dd722950d0dd | -6.72061 | -47.79071 | 2026-09-23 04:27:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 633b0883-7579-3a79-80fc-53eb1a08b01a | -6.34632 | -52.74688 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 121dea8a-c4c3-36a5-8f1d-92732944406e | -10.87895 | -54.09259 | 2026-09-23 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15fa2096-1cb5-39d6-9af4-58be010d3f86 | -7.87365 | -44.97284 | 2026-09-23 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ffdcf5c-a56e-39b8-bf02-e9b1018bc70c | -6.46904 | -59.96823 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeacb44f-e81d-3fe6-aed4-e6102eed27c1 | -11.12927 | -49.45518 | 2026-09-23 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8a28e19-b5eb-35fb-b34c-fb8f28d29459 | -5.9237 | -59.92253 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 88c0e5b4-5e43-37d2-a8d6-e3e5d841a9b5 | -6.46257 | -49.8731 | 2026-09-23 04:27:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a2f33a7-3690-3ebb-aff4-57747baea01d | -8.09957 | -44.42571 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11a18acd-01f3-3b4d-b537-fa0780fdc549 | -11.6661 | -43.47604 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c860b174-450e-39ac-b5ba-111510944e08 | -5.65767 | -60.21581 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 77edc390-c976-32fb-a97e-57acd113229c | -13.01379 | -50.60244 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 994d19cd-e72b-3f4d-81b5-7c9f40dfe149 | -9.16274 | -51.53336 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4dd4ce58-3c2e-3b38-834b-6b5529d3546a | -12.41353 | -46.97214 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b08552d7-5310-388e-97e1-f28ed1335af6 | -14.59399 | -45.62063 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 757d5dd3-97ee-367b-bc0e-ac5436b623c9 | -13.70888 | -48.78717 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d7d4b5c-af57-39d9-b27f-28896b1657cc | -8.37808 | -45.60321 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 646b0af9-bc2b-3a5a-898c-e0d1d251f48e | -8.48882 | -46.87003 | 2026-09-23 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fde368b7-c5a1-34ea-b095-2bb6afdfbbef | -8.33436 | -45.33419 | 2026-09-23 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a43f61f-db06-3472-b086-3e54d7e98f5b | -12.18053 | -50.12147 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 066fec99-b5c1-38c5-be36-c5389a33dd15 | -14.63232 | -45.65877 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68382d18-1625-30cf-91cb-3980f50a2ae3 | -6.08014 | -57.62707 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a9d1c6c3-99c5-3177-b588-493cb7ad7f2b | -13.92996 | -47.83253 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b6f1944-342f-3c3a-8423-17381afb4a5c | -12.87544 | -50.86311 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59460d63-66ad-3882-b995-6491820543fb | -11.29401 | -51.37291 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 226a0c30-624a-3242-92d6-ab7fd29ccae5 | -8.2773 | -54.77257 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 440ecf70-3e79-3511-8ac9-af0d8460c91e | -14.61513 | -45.62373 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26822ff1-496b-39c7-94b3-775f4ffc7980 | -10.20654 | -44.13917 | 2026-09-23 04:27:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68f3da65-1a34-3107-a164-7bae071a4e02 | -12.78184 | -50.90251 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd4e1cd0-68b8-3999-932f-db7e967f6e31 | -9.93696 | -48.47575 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 440b7831-3584-3275-b7e5-6978e33a17a6 | -10.50334 | -44.87689 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efefaa11-5646-39d8-b7f3-df79c86516b0 | -10.3241 | -50.41377 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cd0559b-52a5-3990-8359-0316b7862dc2 | -14.61978 | -45.64116 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0e392ac1-86cb-3f2c-b76e-f324abd2e9fb | -10.26531 | -50.24453 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b2ced64-feb1-3a5c-abe0-82ec1e16c63f | -12.18975 | -47.01334 | 2026-09-23 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ea623a15-7184-3f3a-a4f4-769d9df6b401 | -11.68832 | -43.45209 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a92a069-1d6d-3361-b769-bb7d27ee9fac | -14.01496 | -43.25825 | 2026-09-23 04:27:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3b0f861b-19e9-3bd6-a6b9-7aef4741b426 | -12.41631 | -46.97623 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f411e942-855d-323d-be25-548b01ea05fe | -13.01446 | -50.59844 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 023ff06b-9cea-3880-9a01-c800f5013acf | -12.72488 | -50.8927 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdb71ab0-5db3-3452-8343-3413be295b13 | -9.96873 | -50.26072 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb2bf311-957e-3c14-9422-64538706bed1 | -7.5499 | -48.6877 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff20ba3-b1f3-31b1-8a04-f4c45cd2ba5c | -11.6553 | -47.80669 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d004e8e-e178-3bd5-a381-70ef8b49b0d0 | -11.75587 | -47.62168 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5999f5e2-c3d7-3d45-bf4d-b1c9204113eb | -6.06652 | -57.80935 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8979bcc-cc55-35cf-a3be-a731965f0771 | -7.55757 | -55.01833 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87590418-e8d6-3a42-a479-b1916f7f061c | -8.09187 | -44.34661 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b22b733-8a52-3791-80e3-35c3185d1311 | -11.75612 | -50.05212 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf80128d-2769-3d84-9a1f-7b11d06f658f | -13.30258 | -47.88639 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d3e8eac-a83f-34ee-a992-48189d692831 | -12.47115 | -46.974 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67904530-a97f-3e64-9216-ebd9e4ce5ab7 | -12.76335 | -50.90358 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e6de1e0-6dcc-3134-b524-1f0d51731e35 | -9.0376 | -45.02002 | 2026-09-23 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e92b5b7a-033a-331a-b373-a235fb19859f | -7.3118 | -44.16972 | 2026-09-23 04:27:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9ff411d-45cd-308f-8ed1-0ef9c4db41b4 | -14.63169 | -45.63786 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 50ad96f4-3e49-33de-ad9e-c36856ea21ed | -10.70035 | -48.721 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26950370-a0ad-3fce-8c50-86b71eb722d7 | -11.77995 | -50.07136 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d48d0f1-1b27-3f5e-9f0d-9f30bafb9fd2 | -12.85631 | -50.86827 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2179fb29-3d07-39d9-9175-141a3f7d1714 | -14.59811 | -45.61707 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00ee15ed-e6b1-38df-b1af-8978d972534f | -12.12719 | -47.37587 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README69.md)
