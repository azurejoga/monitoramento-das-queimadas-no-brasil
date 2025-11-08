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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2416739c-f7d1-3a73-a4ec-e6e41a434ea6 | -7.05036 | -49.29271 | 2025-11-08 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a5fbf53-0f8b-3666-b9c8-75db53da117b | -6.26236 | -44.17209 | 2025-11-08 04:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff116733-ff67-358b-946b-9978c09c7f6e | -6.25923 | -44.17262 | 2025-11-08 04:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36f5bc70-6cf9-30c1-a825-3ff9af2c3009 | -8.15333 | -54.84542 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b5f621e2-bd84-3c5d-8f16-8bda06bb4c79 | -9.86513 | -64.88708 | 2025-11-08 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7ebfd52-656d-36a4-9bbd-2d44d97b2bff | -6.11999 | -57.71289 | 2025-11-08 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 303f8159-d7e2-3bad-9bce-623be7c3ee23 | -10.9887 | -53.9824 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c2cce57-0fdb-3ae9-8253-7d9fb4884acb | -8.20494 | -46.97989 | 2025-11-08 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f34351b5-9533-3819-8f80-653e8e30e327 | -7.53046 | -47.38683 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe37b2f0-5c33-3233-ba3c-2bc120f0a5cf | -7.54339 | -41.66552 | 2025-11-08 04:57:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1478164c-4655-3c10-a90f-a65d91f54eb4 | -10.88481 | -53.7737 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2fd7fb5a-e009-3cfa-8ad7-eecc7406361f | -8.60794 | -63.52687 | 2025-11-08 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b95aab1-df8f-3853-9e4a-390a5621ee8f | -8.01553 | -61.52486 | 2025-11-08 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff8c2883-3879-3bab-bdc8-4de35d8b938b | -9.16202 | -50.56511 | 2025-11-08 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b929c22-055f-3cd0-86b9-550db08bbfa8 | -11.05877 | -60.88532 | 2025-11-08 04:57:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5531881-1f84-3366-9207-6e042814f0d6 | -9.08007 | -61.69249 | 2025-11-08 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b95099c-a190-3fe2-867f-89425ee2ce87 | -4.41701 | -59.95094 | 2025-11-08 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33439fb6-25b7-357c-9768-889bdffdd786 | -8.01595 | -61.52205 | 2025-11-08 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37ab05d4-6dcb-3f5c-a307-524733043a3f | -10.36133 | -47.33427 | 2025-11-08 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93904436-e993-3c21-974a-84d41732535d | -9.95006 | -63.19776 | 2025-11-08 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0618447-514b-3dc6-9720-f8082a2723c5 | -8.637 | -54.55997 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c387b3e5-210b-33c6-a75b-525c66df3690 | -9.93809 | -55.54789 | 2025-11-08 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ba45da6-6977-304d-8cb6-0d17f7bb6cee | -8.74196 | -48.32011 | 2025-11-08 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1293ef9-07db-39b0-922b-dfd03607bc49 | -7.03579 | -46.98677 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| de15536a-6072-3050-a3a5-17f2759125af | -10.99764 | -53.99118 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86c71830-e329-34cb-b0b8-9aa180fb464c | -10.06359 | -63.0576 | 2025-11-08 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a77d50e-8096-3a81-a682-e1b7d33ec5d8 | -7.78632 | -48.52967 | 2025-11-08 04:57:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ed4580b-460b-3ebe-a3cd-cf24cdd4598a | -8.43965 | -43.8681 | 2025-11-08 04:57:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 100a70bd-954e-3fb0-b41b-cf200c81a015 | -7.90877 | -54.8238 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5064684d-2f12-35de-bf92-a6c37e1f9149 | -7.55321 | -47.2488 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c77cbc0-9670-3cb2-80d0-3fcfef493446 | -7.55474 | -47.25199 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6952f9f-92c6-3d24-97b1-280d490c8c72 | -7.46168 | -46.63577 | 2025-11-08 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4964a360-f438-3247-ac40-63209965b230 | -9.55088 | -66.7477 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e1efefd-ca0e-3da7-8222-82817ec61f82 | -9.32495 | -47.82668 | 2025-11-08 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc645c5b-079a-38fb-9ac7-2a58ef4f26f4 | -10.51203 | -58.58344 | 2025-11-08 04:57:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecc2610f-8327-3e12-a9b5-7071a4af97d6 | -6.52267 | -55.03426 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63cfb73c-b40a-382e-8f5f-196978241aad | -10.71438 | -48.54836 | 2025-11-08 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff780932-700d-3e72-b673-56aa3f9c2f75 | -7.79195 | -46.64884 | 2025-11-08 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f67904f2-19a4-383a-a787-70aeef389759 | -8.49063 | -44.73074 | 2025-11-08 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 526c50f3-5d0f-35c8-86ec-a85a769c86f4 | -9.7984 | -64.14204 | 2025-11-08 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82972f0b-ec05-3f41-a04c-c823b9e0c33a | -11.19784 | -53.83322 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0819aa9-05b1-3382-854c-438162dd98ee | -5.7822 | -46.56141 | 2025-11-08 04:57:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d9ddbeb-7a34-34ef-aafa-847f6cb47740 | -6.4841 | -48.37025 | 2025-11-08 04:57:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78585bcd-503a-3ef3-9b32-7a2b816db1a0 | -9.0465 | -46.99907 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cee6ca4b-d343-3767-bcc7-a76c0b68ca48 | -7.05089 | -49.28918 | 2025-11-08 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ccfba9f-2827-3fc2-a791-174958beff01 | -8.80624 | -49.84513 | 2025-11-08 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6239f1be-0ed1-35f2-a59b-b181dc8fb227 | -7.57233 | -45.86965 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61d8de69-1f19-3f1d-be0e-d7c1f7cc603a | -9.07553 | -61.69167 | 2025-11-08 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e6b50d3-5c4e-36da-88f8-b7159e7c4c44 | -8.49114 | -44.72693 | 2025-11-08 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4f8ccf0-78bf-306e-b277-bd0fa563f439 | -8.52135 | -55.03265 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 876305a4-b19b-322d-83e2-9ee797eab69c | -7.75698 | -49.26645 | 2025-11-08 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f29fbffe-8f1d-3959-955a-7bf5a4039a48 | -8.3811 | -54.8247 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46890bb9-ec6f-31c3-9f72-8be353f42a86 | -10.57316 | -49.25071 | 2025-11-08 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb76e021-07b8-3e1e-9b5d-23d2a4d06b6b | -6.15537 | -55.96396 | 2025-11-08 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c7107d2-b44b-3989-b241-e0f431fadf4a | -11.86868 | -62.89206 | 2025-11-08 04:59:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c280ec37-de6f-3c18-8194-8dc9d3208027 | -17.62247 | -49.33804 | 2025-11-08 04:59:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b71b46c-e99f-370e-9ccb-c2bb9b106a45 | -18.5105 | -53.49291 | 2025-11-08 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa5eca44-4d64-350c-bbe1-697763973752 | -15.10747 | -48.77267 | 2025-11-08 04:59:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce115692-f5d2-3d0c-ae60-4cc6f30f98a0 | -18.20539 | -56.73911 | 2025-11-08 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 727d6a45-2868-3585-86d7-57a7d34d3abc | -11.7552 | -61.07951 | 2025-11-08 04:59:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4aa4d22-bd22-3943-ba7f-2d80c3426d87 | -11.72283 | -59.31895 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19f04fc4-777c-306a-b97a-29dfbf8b9ea5 | -15.18549 | -49.51955 | 2025-11-08 04:59:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87c48a29-ac49-3fb9-a153-ca39a8496b25 | -12.43667 | -63.15843 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a67dd107-4c7a-3db4-bfad-c308c213e2ee | -11.73485 | -59.31633 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2de76f8a-1fe2-3afe-a4ed-fac03481a2a6 | -16.09129 | -59.11215 | 2025-11-08 04:59:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea3d10b8-39fc-3419-a392-a9a446f07667 | -12.43098 | -63.16267 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44aa9bfe-1c01-314a-8c2a-8c86790a3e20 | -12.42625 | -63.16174 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2862c690-7b75-398a-986c-6fabb5dc556e | -11.72814 | -59.31048 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85de10f2-7eef-3ced-9c7c-be8d83dcab13 | -14.97706 | -52.98328 | 2025-11-08 04:59:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47bc6f1d-6fc4-3803-a7b1-ba61aac0712c | -12.25834 | -60.55042 | 2025-11-08 04:59:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c47174b-df3b-343d-8d82-e51c9222ff29 | -17.87738 | -52.39835 | 2025-11-08 04:59:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30abb2e9-a850-3c77-a741-f290a94a7eb1 | -15.63671 | -56.01128 | 2025-11-08 04:59:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1d87ae86-fc3c-3b9a-9e0b-3df5d858a55f | -12.45179 | -63.15606 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59626f5a-b674-3f03-9e42-15edf9379b13 | -10.28326 | -67.27685 | 2025-11-08 04:59:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b8fd450-7205-3aa9-84cb-95f5926e66b7 | -12.4357 | -63.1636 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b03e51c-d2b3-3849-8769-defddccb719c | -18.33473 | -54.27725 | 2025-11-08 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c3f0945-08d2-3c09-890f-b236c4527f9e | -16.17826 | -52.17052 | 2025-11-08 04:59:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cec40439-7560-3377-b173-002403c66c55 | -11.72579 | -59.32422 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9748ba8-be72-3241-abcc-bc4f7c5b4216 | -17.62714 | -49.33866 | 2025-11-08 04:59:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37273fcd-7919-3746-a3f5-3a5018eba75b | -18.33282 | -54.28636 | 2025-11-08 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5993ae2-78e4-3786-8433-e597f966fe0c | -12.44707 | -63.15512 | 2025-11-08 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2d33358-1d2e-3624-b000-7c5b1bc2d6b5 | -13.93954 | -50.05628 | 2025-11-08 04:59:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed0bfa5c-03ef-33b9-ae9c-8ada90df2612 | -15.18491 | -49.52404 | 2025-11-08 04:59:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d25d58b6-59e6-3a2d-922d-f8dcb9689edd | -14.85738 | -59.42687 | 2025-11-08 04:59:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5839b75c-7bbb-3d1b-bffa-3351df19b616 | -11.72658 | -59.31961 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31865704-3dd7-3551-9ebd-7fdf950de42b | -11.864 | -62.89112 | 2025-11-08 04:59:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65d37dc6-5b1f-34b0-b533-b66b25076a41 | -11.26152 | -60.89457 | 2025-11-08 04:59:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a905d26-e604-3cd3-a77c-65813df162e1 | -11.71167 | -61.42489 | 2025-11-08 04:59:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66ec9c8c-eb3f-3bf6-b052-c99f87c602c0 | -16.28835 | -52.93843 | 2025-11-08 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 934b5b34-6173-3520-9896-5fb07d9f06db | -11.71593 | -61.42572 | 2025-11-08 04:59:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38008b7f-13e9-3232-93ef-2e142b868453 | -18.2087 | -56.73967 | 2025-11-08 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| a0edf43e-424e-3916-941e-6892d7bdc341 | -18.47714 | -53.40998 | 2025-11-08 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3eaf7905-b571-3025-85c3-83fa7e4b4870 | -13.93531 | -50.05574 | 2025-11-08 04:59:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c718dfe9-da56-39d0-bd5e-34c30d9def6c | -10.2822 | -67.27536 | 2025-11-08 04:59:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 308a99db-a490-3d28-9cc9-9cafad606de1 | -11.90833 | -58.93505 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb176f82-7711-3cb8-869f-9c29f9bea902 | -18.20813 | -56.74329 | 2025-11-08 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| f5bdefd1-9cd5-3a6a-9cb6-e9a21ba4ef84 | -11.71909 | -59.31829 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1769cdfb-eb12-37dc-9e52-437bd24af82b | -11.75588 | -61.07562 | 2025-11-08 04:59:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| be6b238b-2d60-3383-a1a5-7094f4d79bc9 | -11.72892 | -59.30592 | 2025-11-08 04:59:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab663606-613b-3536-b855-e0748fe45ea3 | -15.46467 | -57.97226 | 2025-11-08 04:59:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README37.md)
