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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c92816a7-f897-3259-9492-debbd10b7119 | -3.70115 | -47.59944 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c0bb7a0-3525-3fce-be1d-6e42b022ef37 | -6.47986 | -46.70875 | 2024-10-11 04:00:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01768d6f-74bd-3ffd-881a-9d5d09c2bcc1 | -6.13142 | -47.27397 | 2024-10-11 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8dca7ab0-6054-3866-9267-da3c4966603e | -6.13053 | -47.27919 | 2024-10-11 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7554a095-22dd-3dd9-af41-81cbac638229 | -6.12662 | -47.27318 | 2024-10-11 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c93bf74-07ae-394e-9103-7719d6692f90 | -6.12573 | -47.27839 | 2024-10-11 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 50047b7b-b36a-3d44-9e2a-127fc9ae60dd | -6.12182 | -47.2724 | 2024-10-11 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4b215dbf-92c1-353a-a2fd-b07462683560 | -6.10832 | -47.26476 | 2024-10-11 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 961c5966-5522-3c9f-aa77-1f522e01799e | -5.83906 | -47.43293 | 2024-10-11 04:00:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3d4547ba-c896-349a-b44f-55499800e2b9 | -5.30354 | -47.56203 | 2024-10-11 04:00:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e9a396b-8774-3d91-bd04-c3d884af231d | -5.65037 | -47.92714 | 2024-10-11 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb8d5847-b93e-38a0-a432-1f5da9d17307 | -5.64531 | -47.92633 | 2024-10-11 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f53de6b-a70b-3277-977b-eae198683d8f | -5.5527 | -47.75478 | 2024-10-11 04:00:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a152d019-8a78-3776-8e8c-12655b56498a | -5.55214 | -47.7561 | 2024-10-11 04:00:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83083af0-22a9-3c34-b6d1-bf8534e392a7 | -6.84603 | -46.93128 | 2024-10-11 04:00:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6eb88d6e-6ae4-3371-8bba-8d05f963cc80 | -9.09679 | -47.93841 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a6a569e-0366-3c66-926c-f26441cf2406 | -9.09585 | -47.94361 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d386e047-aab9-3400-a89b-5d20fc54ab12 | -9.09203 | -47.93749 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b57e068-7345-3573-b2e5-f71c8e608100 | -9.09109 | -47.94272 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d2ffd05-3165-3021-a53e-fb144e7860d3 | -9.08038 | -48.48132 | 2024-10-11 04:00:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5150d1c3-6474-3aa7-9373-a9d72a93b1d7 | -9.05811 | -47.85414 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5531dedf-b054-30f5-822b-dcc2113547e4 | -9.05339 | -47.85319 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13c2a9cf-f649-3618-b9a9-02c615a34623 | -9.04428 | -47.68497 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f52398e3-52c9-3367-abbb-d2955fa0310e | -8.46693 | -48.27321 | 2024-10-11 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0b5fef1-c3d1-385d-bf7f-aee78b48e1d7 | -8.46599 | -48.27163 | 2024-10-11 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa68f971-f74b-39ab-a3ca-a13983f94751 | -8.46201 | -48.27226 | 2024-10-11 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e89d7c36-11b0-3382-aafb-92830fd12e0f | -8.46108 | -48.27067 | 2024-10-11 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8435e582-4539-30de-888f-331ef61a68f9 | -2.97429 | -48.00253 | 2024-10-11 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4718b13d-a7ee-3a2f-89c4-1f182340926e | -2.96952 | -47.99841 | 2024-10-11 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67cf0ee8-e4d0-3083-bf1d-3954709996a5 | -2.96899 | -48.00162 | 2024-10-11 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1345d710-5ac4-328f-a890-8cf7252b069b | -2.96845 | -48.00484 | 2024-10-11 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dcde7132-e09a-39bd-9499-5b56fe4fe4a5 | -2.87831 | -48.9059 | 2024-10-11 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d27a099-6964-3139-a031-ba748835dffb | -2.87766 | -48.90972 | 2024-10-11 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aef8a7a1-645b-3787-bde8-fb1c8734abaa | -3.45978 | -47.66354 | 2024-10-11 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d1f55eb-6e33-3a01-b8a5-5489051827ff | -4.83607 | -48.93538 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b0e027c-e3ce-359f-9754-1c961c533dbb | -4.78618 | -48.89844 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3724df12-dc31-362c-ba6a-859cce1fbb14 | -4.78557 | -48.90203 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b390cc5-f761-3d47-95cd-0e608b72b8fe | -4.69784 | -48.62206 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fd40afe-fc67-3a27-ac73-cd7bf5b4a156 | -4.69246 | -48.62109 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 062cba45-e204-36cf-b2c4-c64a92b11e66 | -4.38239 | -48.61967 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fac68851-595b-354f-8ee9-77e141f06dcd | -4.38178 | -48.62325 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 303c2faa-64a3-3030-aa2f-ce68b5937374 | -4.31811 | -48.63715 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efeb8596-f3d1-3ea2-819b-6394b4c5fb58 | -4.31751 | -48.64061 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b99bd4a6-de03-3200-87a2-17baca2c283e | -4.31726 | -48.63354 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 838cf721-8351-3bb9-add6-7ceb3578eb0a | -4.31667 | -48.63704 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc0d07ea-e29c-356f-896d-c83df2fa39db | -4.31609 | -48.64051 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bbed5c0e-7169-3c1e-b91a-007188106af7 | -4.3133 | -48.63278 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 462b83cc-a3a9-3a2e-83a9-bc985d0b61d3 | -4.31269 | -48.63623 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 161bf337-6783-3673-8103-4d82bc86d1e4 | -4.29558 | -48.62984 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f798cd72-aa10-3727-a807-6b90d1744028 | -4.29017 | -48.62888 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1516ee71-873f-387d-b6fc-26399f40f6c0 | -4.28958 | -48.63236 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb077bc5-5574-34b9-b787-77b9feed5907 | -4.28899 | -48.63588 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00fe1a40-6ce9-3e5d-b372-2b2cf2de8595 | -4.28358 | -48.63493 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6e60d94-ce13-384b-be4d-c740ca2db581 | -4.25346 | -48.64795 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d650ddb-2eae-3c97-9662-b95416d97e70 | -4.25287 | -48.6514 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0101c9dd-1301-3509-8c46-9c6ae6409969 | -4.10971 | -49.06572 | 2024-10-11 04:00:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0c4abc1-d8d9-37f3-b349-a8e2a1fe5918 | -4.10907 | -49.06949 | 2024-10-11 04:00:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0777f393-f6da-304f-a869-24c20fdc3b83 | -4.10347 | -49.06859 | 2024-10-11 04:00:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e39e69a-9a70-3604-98f7-e5200cc66fac | -3.95186 | -47.9609 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ba90038-592a-3eb9-8c0d-ecab98e8f679 | -3.92022 | -48.34497 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07bb402f-4002-3b6b-9355-d43dc2c98dfd | -3.91547 | -48.34047 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f7b9a6c-e1a1-3f96-89f6-48078cd84c51 | -3.91489 | -48.34396 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8def250-b67f-3618-aa10-c587bc793adf | -3.91431 | -48.3474 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 694517cb-3355-3ecc-b67b-c84717056063 | -3.91375 | -48.3508 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea2e27d3-c56d-3096-b1ac-e12bf2e29865 | -3.91318 | -48.3542 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a94fb719-1a2d-377a-85be-6447d4f37039 | -3.91014 | -48.33944 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa36789d-f807-3020-8587-41a767615b13 | -3.90957 | -48.34286 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c69fde3-b8be-3b55-8fee-6e5710f532c7 | -3.89601 | -48.35807 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 510675c0-76cf-366d-b42f-b349f5918357 | -3.89543 | -48.36157 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f8c7c6f-613b-33eb-a380-1337a8837f6e | -3.80942 | -47.79219 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca675501-76d8-3d72-8c19-373153460559 | -3.80889 | -47.79523 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2de387e2-d4d0-3f3d-8034-2ca903285e83 | -3.80777 | -47.79293 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97093c03-88af-3a51-bd21-582fa31e5740 | -3.80727 | -47.79597 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 274b47b4-ba31-32e2-8297-bd5aebced503 | -3.80261 | -47.79204 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15b5471f-512c-37af-b0db-7956dbde6866 | -3.76669 | -48.10296 | 2024-10-11 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6060a13-1f24-39b9-a6ec-83158ed81e2b | -3.76614 | -48.10617 | 2024-10-11 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07585ffd-5883-3bbf-8cd8-3053bd6c04fd | -5.07033 | -48.08041 | 2024-10-11 04:00:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c58e8806-7bff-3edc-b13c-a6b48a32f325 | -4.97613 | -47.93052 | 2024-10-11 04:00:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ebf4f96-15d4-3f05-83e2-04b5b7115c9e | -4.97351 | -47.92708 | 2024-10-11 04:00:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88b9f038-9c1d-318f-bfbc-96593a070f92 | -4.97296 | -47.93021 | 2024-10-11 04:00:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f08f2e72-6690-39c6-92db-c75ed95c9bda | -4.97103 | -47.9296 | 2024-10-11 04:00:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 468fccaf-0e0a-3805-bec6-09b449e04465 | -4.82528 | -48.22229 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb53444f-67a9-350b-926e-1645a98b9cc0 | -4.82005 | -48.22141 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5eeebe52-304a-330b-8ef7-d7bd5bfec51e | -4.77983 | -48.07916 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba476963-6d26-3f5e-82e3-99fe959dacdc | -4.77929 | -48.08229 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8aba7504-6b7a-37d1-b10c-0dfe32aefb7b | -4.48464 | -48.11143 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9b8b92a3-18e6-30f2-94c0-3cfa859d235e | -4.47942 | -48.11059 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f3be002-2980-3f35-9df0-c979a864c4d6 | -4.27748 | -48.06736 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19103772-e51f-31da-a57f-6d4403cd447f | -4.27226 | -48.22806 | 2024-10-11 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7290b56d-d29a-3c74-b3c4-2b561b21db59 | -4.20176 | -48.13283 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 343d296b-6d6d-3349-ad9f-6ec4ee77c9fb | -4.20121 | -48.13601 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6c93843-eec3-3c29-b862-62fe0e68729f | -4.11986 | -48.26917 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba53c50b-e156-30e7-810a-0d4bd9a723e4 | -4.11929 | -48.27253 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91302e9f-2dd7-3ca7-89ff-35ffea31c97f | -4.11874 | -48.27584 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ea25ac9-29b5-3426-9398-43d80b2b7bba | -4.11798 | -48.24802 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e89f5afc-61b4-3a3b-9e60-8f55951b5280 | -4.11742 | -48.2513 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2137c019-a16c-3a60-be60-06105975aa66 | -4.11687 | -48.2546 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c5f75ae1-7ec0-3618-868e-a7f45ba68f86 | -4.1163 | -48.25796 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d5e0a453-0bdf-39b6-b463-87deab4adc2f | -4.11573 | -48.26132 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c36a29d2-d1eb-31d9-b668-44e76bc4d03b | -4.11515 | -48.26474 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README40.md)
