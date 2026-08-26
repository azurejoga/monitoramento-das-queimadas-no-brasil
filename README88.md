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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a2336ee-2230-38c0-8155-2682cd9d8201 | -6.7691 | -58.6873 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| cde96cef-cdf5-312d-bcd3-92eefef37838 | -9.6022 | -55.128 | 2026-08-26 15:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f92ce3f1-636a-3719-b07d-90f252193d0e | -8.1482 | -47.5218 | 2026-08-26 15:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 45b72f4b-88f4-3f74-991d-d2d6f876c017 | -7.4768 | -55.2872 | 2026-08-26 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6e36bb2f-6d4b-36b8-a693-0f36182af4e4 | -12.757 | -46.4538 | 2026-08-26 15:10:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 15f3cf70-e758-3ba5-ace5-3d49a45686b6 | -3.2179 | -61.2174 | 2026-08-26 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 32c25351-c7fe-3a01-ab94-5734e8f287e3 | -6.4047 | -54.9642 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 084a9831-05df-3f13-960b-f58b4b4f7489 | -9.1315 | -57.5703 | 2026-08-26 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| c3163ef9-b06a-3be5-b547-c36c68aebda1 | -10.95 | -49.5877 | 2026-08-26 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| bc14c85e-2ed3-3641-9b4b-6d9fc2c2d16b | -6.5829 | -58.9851 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 147df413-2020-396d-8999-18c3d5fb5330 | -9.1317 | -57.5506 | 2026-08-26 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| de2b1ce3-cc08-3ae6-9743-e8b877f1d52c | -6.4232 | -54.9632 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 90b69660-1ecc-3ee8-a695-856f4f175852 | -10.9405 | -50.255 | 2026-08-26 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 422.9 |
| 87d4a4eb-1ede-3550-90df-7fea2e286b0f | -6.1544 | -53.6874 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| fa2254bc-c6a6-3dad-93e9-0c1722e120c4 | -6.3323 | -54.7272 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6c94ac4e-2d05-3077-b198-59a9dee42158 | -11.6025 | -46.7542 | 2026-08-26 15:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 35f6ee71-00b5-30b0-9140-2dd1395f2158 | -6.7833 | -59.4208 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 57c183d1-c152-34f1-b63f-10b88cf89ee0 | -8.1669 | -54.9648 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e3ac3d9a-7336-3602-b176-3fa06a81f8e7 | -6.1477 | -57.702 | 2026-08-26 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 44ff7fbc-f7ec-3335-8a45-5a2fd451b7b9 | -5.6035 | -45.5465 | 2026-08-26 15:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 55a79da3-8e5d-3af1-ae22-145757a6af9b | -11.7733 | -54.5396 | 2026-08-26 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 240.9 |
| 0575f5b4-bba9-3a4d-a8ca-c790db8cfb20 | -11.1561 | -54.0028 | 2026-08-26 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 75aeff53-2f3d-3c23-ba15-f235ee4237c5 | -9.1711 | -49.9835 | 2026-08-26 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 188.7 |
| 4d893e79-f360-3923-906a-5ed0b7b3c8ab | -10.9664 | -51.1251 | 2026-08-26 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e5662fc2-3c95-3908-b5dc-45d5900b3c5f | -8.5962 | -54.8563 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 2096ad84-2382-3a66-960a-647b1c88f223 | -13.5848 | -51.8419 | 2026-08-26 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 858fdd9e-36fc-3272-883b-539f526cdbf1 | -7.4947 | -55.3662 | 2026-08-26 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b2417baa-a53e-3f00-853f-978393088bf4 | -9.1713 | -49.9622 | 2026-08-26 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| aba7777b-6df6-3e38-bc5d-4b31e1be4061 | -13.6817 | -51.7872 | 2026-08-26 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5e259c36-ad3d-3302-b541-e3c4b88b28fa | -6.0807 | -59.9465 | 2026-08-26 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| f58516e3-51c5-355e-b422-816815ef878c | -6.6227 | -58.4801 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5597dde6-bb82-35e2-8feb-a9db6afc05a3 | -6.6915 | -45.2159 | 2026-08-26 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 66cd1c22-2414-36fe-998c-a61bd7a95399 | -13.6337 | -49.0051 | 2026-08-26 15:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| cc96615e-c3b4-3212-9040-b8eb189fc616 | -9.1896 | -50.0032 | 2026-08-26 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 849d56d1-f77d-3c3a-8023-0ef7e1835123 | -6.7815 | -59.748 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1abeb299-2504-340d-b19b-adf070ee6052 | -6.0353 | -58.0376 | 2026-08-26 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 253b7196-bf22-362b-81c6-d4a00a306556 | -6.3504 | -54.7865 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 601b2ddb-d5aa-3a9b-a655-37a687467dd4 | -7.0242 | -59.2374 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e2404278-792e-301a-a529-eb65cad28e90 | -8.616 | -54.7339 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 322e5dfc-ec55-3ca4-8566-6228e86434ee | -8.9418 | -45.748 | 2026-08-26 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 175.9 |
| bb30459a-1d78-31e2-9536-72ee5e928ff2 | -6.6917 | -45.1932 | 2026-08-26 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 278.3 |
| 90d80323-1df3-3eb6-92a9-3d0976e35ef1 | -11.7736 | -54.5191 | 2026-08-26 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 375.9 |
| 4f3e36a1-7ed6-35ee-95e3-06ae58eaa88f | -9.4435 | -60.5307 | 2026-08-26 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0216c785-ae3d-337a-bb40-c7f89ac99db0 | -10.7793 | -50.975 | 2026-08-26 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 78d7059b-bbeb-397f-9849-0987141cf963 | -8.7769 | -49.9763 | 2026-08-26 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 269.2 |
| 255b8acb-f5c7-3ef4-886e-f048319b496d | -7.0058 | -59.2382 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 757552d0-5a9e-3a83-9396-2b6796ca7dca | -3.2178 | -61.2551 | 2026-08-26 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 1cd0b731-7b68-352a-a711-072f89949afa | -11.7357 | -54.5227 | 2026-08-26 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 263f1c9f-4092-3212-944f-3453c3701f0f | -4.8002 | -43.1709 | 2026-08-26 15:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 242.7 |
| fb63a99d-b102-3418-ada4-a36b1808ec6f | -9.1708 | -50.0049 | 2026-08-26 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 8e9e3326-d5d3-3f91-903d-c07995317793 | -7.5015 | -44.9397 | 2026-08-26 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 4c8d0b59-39db-3c2c-b3a1-54df21d57b50 | -7.6649 | -47.1242 | 2026-08-26 15:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 283.5 |
| 6e4a87ea-be2a-3c52-bc66-48d616ee0c1b | -11.8165 | -47.6647 | 2026-08-26 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 196.1 |
| a06e5ed7-2136-399a-ae2a-c500368d4486 | -12.5968 | -47.892 | 2026-08-26 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d4ec3b9f-010f-3690-9070-c7a4af03e54b | -8.0733 | -47.5066 | 2026-08-26 15:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 14f0b128-7caf-3f34-9b0c-4dbc2fba86cb | -6.8008 | -59.5934 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 59138829-ab5d-3d54-a7df-03abcb22fa9d | -7.385 | -55.1523 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 166.3 |
| a40a0a07-ff25-3413-8645-4c2b58931d0e | -9.7249 | -49.3296 | 2026-08-26 15:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 3c749c15-0378-31e5-aa16-288a871d2655 | -6.8019 | -59.4008 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 52b8624f-644d-3890-8f79-8ebd7859f861 | -10.9216 | -50.2571 | 2026-08-26 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 555e4ed3-4c7c-3887-a089-79a839f211c3 | -8.5975 | -54.715 | 2026-08-26 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 6952e6e2-f671-3327-af19-f75b72feef2f | -11.7546 | -54.5209 | 2026-08-26 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 389.6 |
| d7072714-2c8e-31d1-8a91-a1665bf0c463 | -10.779 | -50.9962 | 2026-08-26 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 3490e054-3ac1-3f35-81ce-9062e5f64be2 | -7.52 | -44.9608 | 2026-08-26 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 464d2931-fcde-341b-8f6d-87538d6781a3 | -8.7584 | -49.9566 | 2026-08-26 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 164.3 |
| d3e63d2d-4835-39c6-afd4-009eb2f98643 | -9.7246 | -49.3512 | 2026-08-26 15:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 67222913-3219-3a16-a999-bcc6ac10d8f9 | -11.1165 | -49.8707 | 2026-08-26 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 1f5bc677-f67e-3129-963b-56bf8991bc50 | -6.6226 | -58.4995 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 2c058f7e-7d12-39ae-a9da-9356eef45c46 | -6.7647 | -59.4601 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d1fe88bb-c54c-3e07-82b1-bb2147fc69fa | -6.7103 | -45.2144 | 2026-08-26 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 15b48e32-667a-38ae-b0d2-de8609ff2649 | -11.1939 | -53.9993 | 2026-08-26 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| f025e738-0291-3e23-9ba7-a1228a75b219 | -6.7296 | -59.1337 | 2026-08-26 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3207352a-998a-3637-af4b-93727d6d4957 | -12.616 | -47.8893 | 2026-08-26 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f5d0e1be-c919-32df-9069-42f1e285c337 | -6.8062 | -58.6469 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 23b0c38b-f2b1-39eb-82da-54825cc0a83e | -5.9794 | -52.2252 | 2026-08-26 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 271f352d-7e34-3773-9352-1dc9ac5a271e | -9.6776 | -55.082 | 2026-08-26 15:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 5a2effb9-9139-33d1-910f-45a42347540b | -8.5175 | -55.324 | 2026-08-26 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 96d148ec-62eb-3683-9b08-4681a97c9e73 | -8.7582 | -49.978 | 2026-08-26 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 237.3 |
| 2b05d312-9d83-3cd2-8ebe-2983134c0a61 | -10.3145 | -50.4061 | 2026-08-26 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1a37afb2-6de5-3f13-9ba1-8e1f3068fe32 | -6.695 | -58.7291 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 47ecae24-df7d-35de-9e44-c58ecf82eede | -10.7982 | -50.973 | 2026-08-26 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.9 |
| a383450b-27fa-3567-a250-b1463f2dfe17 | -8.5177 | -55.3039 | 2026-08-26 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 57f4c805-d27a-3fb3-b3d4-a8abb2fa1e70 | -6.6225 | -58.5189 | 2026-08-26 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e58fc113-f8bd-3a23-b795-07f5743b2ebb | -7.65 | -47.11 | 2026-08-26 15:15:00 | MSG-03 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08297973-7f48-3c7d-bf6c-dbfcd91e73e4 | -13.26 | -51.37 | 2026-08-26 15:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0546d38d-a8b4-344c-83f3-10596c2fd559 | -9.36 | -48.69 | 2026-08-26 15:15:00 | MSG-03 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 614a9c41-f55f-3207-bb00-f4628b449985 | -8.77 | -49.98 | 2026-08-26 15:15:00 | MSG-03 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57582a5d-0637-3c59-b979-68b84554e5a5 | -7.66 | -47.16 | 2026-08-26 15:15:00 | MSG-03 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 146b000a-9c7e-3a2c-bb4e-f3ff4dd0cc81 | -11.78 | -54.54 | 2026-08-26 15:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b3784ff-029e-3b5a-983e-d6863994d27e | -8.5365 | -55.2826 | 2026-08-26 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 80ea88c3-5da9-3b69-8fce-08a656eb84b5 | -13.3402 | -48.2079 | 2026-08-26 15:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ed53541d-f596-3563-949a-d44efc293fad | -6.0807 | -59.9465 | 2026-08-26 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 171050ba-b9bf-3290-9443-f5c0b2a5e273 | -11.1939 | -53.9993 | 2026-08-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 258.6 |
| fa7e66c2-e612-385e-b77c-51b364321646 | -3.79 | -59.284 | 2026-08-26 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 157d94d6-d290-3ad1-99d2-c62c1480a12f | -8.7769 | -49.9763 | 2026-08-26 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 333.2 |
| 22ea788b-ce6f-3c90-a742-603533e523ae | -8.7584 | -49.9566 | 2026-08-26 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 685307d0-8ad8-34ba-a837-1d5b52b0a3d4 | -8.5175 | -55.324 | 2026-08-26 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 2ef0f3c9-5268-3966-810c-e0f07bf197b0 | -7.52 | -44.9608 | 2026-08-26 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| fb2b084c-8a47-36a8-9fd6-f692f01efd41 | -8.5973 | -54.7352 | 2026-08-26 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 708c67a9-519a-3068-9815-94dae54c6443 | -7.1309 | -42.7945 | 2026-08-26 15:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 245.5 |


[Clique aqui para ver as próximas entradas](README89.md)
