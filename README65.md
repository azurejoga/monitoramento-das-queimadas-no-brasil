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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cbcdbe1-dedd-3b93-a930-5c2bc22d7439 | -9.6293 | -54.3158 | 2026-09-03 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| a94b2c91-4283-3060-9c39-01f25d252dce | -3.3504 | -59.4465 | 2026-09-03 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ea1a90b2-6e98-343d-8ba9-5f2b8bb7fb4e | -3.9251 | -49.0539 | 2026-09-03 15:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3e8f7bc1-a468-3e5a-bd48-6625958bfdbf | -8.799 | -62.4905 | 2026-09-03 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b4d668d9-90f5-32bd-9803-d2c22a95c920 | -5.4553 | -60.0626 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a1fb5969-df8c-39bc-8d8e-c108d53b79bc | -11.0752 | -51.4731 | 2026-09-03 15:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9e39af6c-ed48-3dc1-af12-c9e8993a8ce3 | -17.0875 | -56.874 | 2026-09-03 15:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| f6c43f1c-bf50-3695-961d-3f621af5d0f7 | -10.7827 | -50.7198 | 2026-09-03 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 46ae47a3-5c67-3735-b7ff-c9d668b63aa7 | -8.7785 | -62.8324 | 2026-09-03 15:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8102f32d-2540-37f3-8023-25855ace8bef | -6.8172 | -59.9578 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 35b1fc96-3b1d-312b-8180-8955db005f21 | -10.7274 | -50.6192 | 2026-09-03 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| cf1320a7-f31f-331e-b113-0f213ce58a25 | -11.6773 | -50.4724 | 2026-09-03 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| dd5b6054-56d1-368e-8238-9e8b0c7108c7 | -7.5137 | -60.7919 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 9a0e3882-39c3-3063-8251-213c93c04946 | -1.4752 | -54.8157 | 2026-09-03 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| d9edb66d-b71a-3003-8585-600e4b04db6e | -3.6215 | -60.585 | 2026-09-03 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 92e93340-1ceb-3dca-8536-8092849b5894 | -9.4813 | -60.4516 | 2026-09-03 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9f95330c-fd9b-384b-892e-6593bf19093b | -9.4814 | -60.4324 | 2026-09-03 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 27516d52-4cf3-3804-a989-3d32d6e7ac3d | -7.5326 | -60.7147 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| bc4ba80a-a6b1-3b83-ae1f-b040cc252a4e | -11.5089 | -50.2989 | 2026-09-03 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 4687d600-cf24-3f33-9d00-ed326cccb5bf | -3.2179 | -61.2174 | 2026-09-03 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f394849e-8d83-3d61-b234-ef931215cd1f | -7.7337 | -61.0886 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1b4eadd8-954e-3e72-ba5f-27e98f4c19ac | -8.7967 | -62.8885 | 2026-09-03 15:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5c75d438-1f5c-3c14-bdcb-3d9066e35376 | -17.123 | -55.9194 | 2026-09-03 15:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 126.4 |
| 190387bb-ec01-36a5-a585-e6ff26db4261 | -7.7521 | -61.1069 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f317cf33-2810-3515-9313-d237a0830c3d | -7.4954 | -60.7736 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 59d5c405-e16f-3384-b819-45b0021e54de | -11.4895 | -50.3225 | 2026-09-03 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2e0cc78c-818b-3b3c-8868-3de4eccfdad9 | -9.1523 | -49.9853 | 2026-09-03 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| fef6450b-d354-30fc-9692-52d2ab3bfe10 | -10.8017 | -50.7178 | 2026-09-03 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| dd8c431b-a0b5-343d-857a-56e7843d6a3d | -3.3503 | -59.4657 | 2026-09-03 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2e5ea596-a822-3954-bbea-8713e7ed1b3b | -7.5139 | -60.7537 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 62355b45-835b-341f-a46b-773705f29f24 | -13.4194 | -51.3945 | 2026-09-03 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| eddeaa21-6658-32e4-901d-3992de08c4e3 | -7.507 | -44.4583 | 2026-09-03 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 579bbe4e-d883-30e4-a734-390be76b612a | -17.0878 | -56.8534 | 2026-09-03 15:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.6 |
| 326e50c1-7e4e-3aaa-9883-134631037e9f | -6.7463 | -59.4416 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 1103a5b7-5225-3904-9d9d-34f74d74c804 | -6.7692 | -58.6679 | 2026-09-03 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 06c0e443-8387-3607-9fc4-87dad97f87ca | -17.1227 | -55.9402 | 2026-09-03 15:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 3c44ab4b-3911-31cb-a77e-5057f2358170 | -5.3264 | -60.143 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 7c409eda-af0b-30e0-b3d0-d9de5ad9d1e3 | -10.8218 | -50.6306 | 2026-09-03 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 06c1af37-d8e8-3dbc-8702-aff994a5ef5c | -11.7725 | -50.4614 | 2026-09-03 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c1103714-29e4-3f1c-81e3-1225596060d5 | -10.3583 | -49.9528 | 2026-09-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 9f3cb7a4-2e5a-3f6b-8467-301b8de1f8f2 | -3.1815 | -61.1424 | 2026-09-03 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2b998c2d-4de2-34bd-8f52-520f6549db2e | -10.8396 | -50.7139 | 2026-09-03 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0c5c0872-dad5-3828-85b0-492fb185dac0 | -7.0786 | -56.5213 | 2026-09-03 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| ac974f3f-4c4c-3638-9688-24a5b7580c90 | -8.4677 | -54.6429 | 2026-09-03 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 3e9fa4c4-45dc-3fb2-b6bc-5a1f4dee8346 | -14.3818 | -52.5039 | 2026-09-03 15:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| fbaa6e84-89d3-3e3e-9826-7b88cc39e88d | -3.0347 | -61.4846 | 2026-09-03 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ee825698-4c72-3941-9949-129c66b91ba8 | -7.5325 | -60.7338 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c2c95ea7-85e6-3d4f-93fc-3a820d51cda9 | -14.5627 | -52.077 | 2026-09-03 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| ca8df5be-4142-3a93-bd93-071c778be5bd | -3.0164 | -61.4848 | 2026-09-03 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 8143e809-7a6c-3349-82c9-f878b484b8ac | -3.3321 | -59.4469 | 2026-09-03 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 5a412c82-cef8-3460-a674-6e7a06445ca4 | -7.2006 | -60.6706 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| c58b3f97-b0a6-3c10-be5c-01fda4048244 | -11.696 | -50.4917 | 2026-09-03 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 33891050-fd1e-3aa6-b901-f8ba7cf623c9 | -6.695 | -58.7291 | 2026-09-03 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 86769cd9-df03-37c7-832d-a8d8304a9b2f | -13.263 | -51.5845 | 2026-09-03 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| bb171f65-eefd-32d2-b079-a3730cfa2a4c | -3.6216 | -60.547 | 2026-09-03 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ea74b1ff-ae65-3752-9fdf-055d9b391c47 | -8.7615 | -62.5679 | 2026-09-03 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 6de79945-fe9d-37c2-b1bf-0fee1bf753de | -7.7522 | -61.0878 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 44de5392-8de0-3d32-99f5-8707eaa93433 | -6.7451 | -59.6533 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| bba2caef-cbd9-3ab5-974d-71bf1842b369 | -10.8215 | -50.6519 | 2026-09-03 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 22e48fa6-c2f6-3db7-a337-0bf4cde3bed0 | -3.1815 | -61.1613 | 2026-09-03 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 781c6dae-03a7-3609-93d2-f82136b95c39 | -13.8371 | -54.0989 | 2026-09-03 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| afdfb824-e09e-3f6c-8f49-485c319adc1d | -11.0933 | -51.5345 | 2026-09-03 15:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2ca5dfca-522e-38d4-a00f-612f17dcffc2 | -7.2251 | -56.7508 | 2026-09-03 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 57be77c4-0137-36ca-b7cc-79d0672d1fd2 | -17.0881 | -56.8328 | 2026-09-03 15:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 0299f3da-6102-3a10-803a-ceaafa29884e | -7.1123 | -42.7727 | 2026-09-03 15:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| ed0cd205-1dbc-3dc8-83e9-f4e25e57404c | -11.6583 | -50.4746 | 2026-09-03 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 76b721ea-de31-3031-af94-f9540e61232b | -6.8018 | -59.4201 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| aed3e23c-794c-3b68-a8a4-cfaa9beaaaee | -7.7336 | -61.1076 | 2026-09-03 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b94d4ede-c9de-3517-b951-1ff07b6388cc | -7.3118 | -60.5897 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 49e0ea86-b680-3da8-9e80-a8336a564775 | -15.2866 | -53.8617 | 2026-09-03 15:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| fd5af159-b887-379b-bf46-62e5ed120712 | -8.911 | -62.372 | 2026-09-03 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 274eff35-7512-33f5-a467-20d85f151d7a | -10.4636 | -45.317 | 2026-09-03 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a62dadca-4f6b-3578-8e58-e61e6420adad | -10.8398 | -50.6926 | 2026-09-03 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 22e8ce54-077a-3184-a6ca-04a29fc23e8e | -11.7722 | -50.4829 | 2026-09-03 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c0f9bac1-bd93-37fc-92b0-c6835f20447d | -10.3208 | -49.9352 | 2026-09-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 59244b6f-cde6-3374-8bed-dc30bbae518e | -6.8202 | -59.4194 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 95a93b39-3fc9-33f5-be51-61cec3004fc5 | -11.5086 | -50.3204 | 2026-09-03 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 4944a91c-1e47-3e18-9638-4527dfd0986e | -7.3117 | -60.6089 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 213e4e04-7ef5-326f-a33d-65a7ce482b4c | -7.3487 | -60.5883 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ebcbbe06-15fc-3d68-ba14-61a4a2c08322 | -10.5254 | -50.1709 | 2026-09-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 0f398d07-9249-3af6-a786-b9bda95250bf | -10.8404 | -50.6499 | 2026-09-03 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 582eb392-2d80-302e-88ec-ce830c0fcd18 | -10.547 | -49.9758 | 2026-09-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b7cddbd8-ba0a-345f-b9a4-3db0c90672da | -12.1269 | -44.1755 | 2026-09-03 15:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| edcae07c-0233-3576-b665-1c274f0b7b92 | -8.6853 | -62.9307 | 2026-09-03 15:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 133f2277-063b-32ac-98ff-9fc6ea1df1ab | -8.4488 | -54.6644 | 2026-09-03 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c6f48d39-4af9-3842-b7b4-682bd30133e9 | -8.6317 | -62.5732 | 2026-09-03 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 6f1a197d-87e9-37a5-a865-c73b57791ed0 | -11.7151 | -50.4895 | 2026-09-03 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 3fc01036-f55e-34cc-bd41-a16d7dfa790e | -7.3301 | -60.6081 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8703a2d0-abcf-3629-8f22-571f4e9a6c93 | -10.3772 | -49.9508 | 2026-09-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5483af81-9129-3051-ad59-e48d36f28d12 | -7.2255 | -42.7616 | 2026-09-03 15:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| a3227ecb-158c-3a5a-9284-bff92657c5ee | -3.7533 | -59.3231 | 2026-09-03 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| d0a929fb-6720-362e-b8df-6c8e20c999ca | -4.1515 | -60.7068 | 2026-09-03 15:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a52bfc66-82b8-3d4f-9ad5-9403a17b6f2e | -14.2927 | -52.0701 | 2026-09-03 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f315f5c5-da79-3245-834b-bb12840d9777 | -11.2295 | -51.2667 | 2026-09-03 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ab357523-a441-33c5-995b-9afbd66b5fb2 | -13.8563 | -54.0967 | 2026-09-03 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5c2780e8-305f-3b6f-b82e-021773d63398 | -8.1345 | -45.4923 | 2026-09-03 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| fd9653df-76b2-3826-852f-025886089ecd | -6.9872 | -59.2582 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0215baf4-6749-3a2f-805b-cfeaae76cc0f | -15.2866 | -53.8617 | 2026-09-03 15:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0de5d941-56c0-3905-ae9b-80c749090174 | -7.0058 | -59.2382 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f7d3ac83-8926-345c-ab52-70c35ee2b665 | -3.2178 | -61.2362 | 2026-09-03 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |


[Clique aqui para ver as próximas entradas](README66.md)
