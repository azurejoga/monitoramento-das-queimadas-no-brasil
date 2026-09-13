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
| c71fa6c5-1c08-3d1d-863f-2bc7d478ce72 | -9.36934 | -50.09273 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7de77c9b-27fb-3fd9-8174-fcfe6151bea4 | -6.31125 | -59.95944 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e5c4d12-5df8-361f-925a-687ec0ad3a6d | -9.55464 | -51.36351 | 2026-09-13 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27bfc58d-cf61-35d3-92ba-db2d0e1a83ea | -6.06954 | -57.86198 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdde5a20-f5d0-3d07-a434-c6091446880b | -6.59067 | -58.84547 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 87377cf9-110d-3409-bb01-91fd603d2a9c | -6.20207 | -57.77785 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fcd8b7a-89e1-3db5-94f9-d59d89d74b04 | -11.56812 | -46.99177 | 2026-09-13 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c004cb82-ad23-3ca2-9f25-d9869a7f046f | -10.92325 | -48.33768 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a82f7069-f399-3ff4-867f-13cc273e3a63 | -10.6214 | -46.10617 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d34256ba-25a3-3802-b5a0-69f7c5e1fb0d | -13.79448 | -48.79638 | 2026-09-13 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30e9266c-372c-3c1e-a75b-0c8055197190 | -11.33117 | -48.5433 | 2026-09-13 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c6fbc92-f02d-39fd-aa78-a80a0c33486c | -10.56311 | -51.34443 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f55153e-66ed-3d2f-9f54-96d3eb5099c8 | -10.56971 | -51.36754 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38e963bb-297d-3f82-bff0-04d8f8be836b | -13.45535 | -48.49133 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e7df667-a327-3f29-9221-d6a46e6e1881 | -10.31017 | -45.29064 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f69f02e3-edbf-32dc-9d05-e3efb31371ef | -6.74513 | -59.43368 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a1fcf9b-f091-3033-a340-502d71ed17f0 | -12.8511 | -44.38791 | 2026-09-13 04:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f260e3cd-75a6-3b8d-8897-c95119d657de | -10.94226 | -48.35275 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 459beff6-de34-3f71-a264-49db3af7c137 | -12.66193 | -54.72253 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd3be731-7154-3e5f-b583-dee4a78e5020 | -10.7302 | -54.00326 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52eb5ab8-240e-3820-b5d2-d1d20f137af1 | -14.27267 | -45.64941 | 2026-09-13 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 488499e8-edce-3807-8605-a7b1acbc36fa | -13.31136 | -51.72102 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b696533-55c9-376c-9c84-6df09c694fe6 | -6.10928 | -57.66459 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 807b9bec-411b-309b-945e-80416e575d56 | -12.66234 | -54.67598 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5baeeec5-0325-34bd-a182-3011154c2a06 | -6.95548 | -59.74787 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0274ad22-54d1-39cd-9a12-0b729605c6d7 | -8.12213 | -54.81037 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8b67b38-edc5-329c-8e0d-916c8773799a | -8.59912 | -44.42945 | 2026-09-13 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26b1cb02-fc15-3a5b-94a1-b8530a511a08 | -11.81496 | -46.40138 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 473782d0-6dce-3511-b39b-5c07c7313304 | -8.05399 | -54.8456 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b6970de-5db0-3e73-bbb5-65f21ea0aec0 | -10.69555 | -54.16116 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dfa5ead-9c03-3409-89a8-020d433823b3 | -9.71035 | -53.96779 | 2026-09-13 04:51:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bb10cb1-2712-309e-afe7-daa12f4fa3a3 | -8.0529 | -54.84816 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f70df86-5aca-3fcd-a541-cb0da392d245 | -10.55814 | -51.3326 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4078bd0-2d0d-390c-a93d-9bfe282223bb | -6.31385 | -59.97297 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12b9b75e-6b5e-3216-a966-9c3a31a01f58 | -10.8906 | -47.83986 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b6c8aa8-6695-3988-aa8b-ce7350425ba3 | -7.33917 | -49.55769 | 2026-09-13 04:51:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad1f01f7-ebbb-3f62-9180-a6e47bb64e71 | -8.21427 | -47.86633 | 2026-09-13 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca2a81c2-52a1-307f-8c38-bf82f6205f6f | -10.29034 | -49.99573 | 2026-09-13 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84f8e737-82fd-3084-9b72-3a32322cbea5 | -6.28655 | -59.92908 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 236f9d8f-f0d3-3668-874c-d2f43d50fb0d | -13.45008 | -48.50258 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9a6699b-38d1-373e-bdf0-be0a334127e9 | -6.20156 | -57.78078 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de1a8624-62da-3710-bbe5-321cf976d418 | -10.58662 | -51.35982 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e06c065-e53e-3115-b683-b56fbf61cdfc | -10.55202 | -51.32788 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 757beac8-ab55-3904-8be9-9d5da5d299a5 | -6.13029 | -57.57365 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82d1a69b-1ffa-3ce3-b3f3-7721aca82aa1 | -6.31027 | -59.95966 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24b07f98-4b18-3563-bb53-92931de16ab9 | -13.34492 | -51.78158 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1eadda98-1cf5-3761-a2ba-70a2de10d314 | -12.85497 | -44.39299 | 2026-09-13 04:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 16041ccb-d688-308f-98bd-153863c0c23d | -10.92726 | -48.35799 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| add74aae-dc1e-33c7-929a-09863fb15eca | -6.30615 | -59.95425 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd992c11-544b-3ff6-aa4a-6b098139153b | -8.0183 | -54.85669 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e92539c-486a-381c-81f8-8fc258c06f89 | -6.5991 | -58.86807 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1883ddb-dc77-3f33-b37f-a21c68fb0021 | -6.37958 | -58.29939 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f12fa41b-4507-3f7c-988b-19f8678da8bb | -9.36823 | -50.09972 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| da8fdb09-15e8-37b6-898e-d9c00c61f587 | -6.3755 | -58.29215 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b97dfaba-dac1-3ba6-a0f7-8845bf68ae0a | -7.87467 | -54.72686 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a633e2f4-76be-3fdc-9e41-1d9d42ca3dc8 | -8.02695 | -54.85457 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e601a5f9-f9ff-3b5d-9072-004558d3a5e4 | -11.83107 | -46.39911 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e368143b-8c70-3036-bacf-ef03b57e3897 | -9.8785 | -47.58495 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec3129d3-3ae7-3757-bbe2-502d0c95bbc6 | -13.55733 | -49.48616 | 2026-09-13 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a28eb61-9eca-3353-af4c-f97eeab0bcda | -13.55392 | -49.48561 | 2026-09-13 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 706c1fa6-f245-3acf-acd7-6230aa6142d1 | -12.47867 | -57.65295 | 2026-09-13 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d73ee76-1991-3ac7-8d21-ebe38263e058 | -6.78246 | -59.85241 | 2026-09-13 04:51:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f68f8491-65cb-3fa4-9ad1-7e6bdb47ac87 | -10.45695 | -48.65175 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1155e6d6-042a-354a-ad0b-9e8808283f01 | -10.97197 | -48.35225 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1ddc275-385b-3120-ad1e-590768418060 | -11.57251 | -46.98784 | 2026-09-13 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd6521d7-8ced-3c2d-9e0b-f6cc56c3c4cd | -11.18545 | -42.79666 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a31ee68d-b643-3313-9b71-42b4e638966d | -10.486 | -48.6401 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a34f323-cf23-3a45-a9b2-e9f451f4e3c0 | -10.46614 | -48.63765 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbb9f133-7c55-3ff3-b192-8d0293187b2d | -13.45066 | -48.49868 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04fea4c7-feeb-35ff-b2b5-61abb52dc8c1 | -7.86488 | -54.70462 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e576ae4-b3ac-3716-bad9-c08692f12a02 | -6.67726 | -58.71111 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a3295a2-14ed-38ad-b907-85b9162fe68d | -6.1694 | -57.72689 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45a2cd23-2e13-3ed6-b285-d7f08d96b8f7 | -9.94872 | -48.50972 | 2026-09-13 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e21e0491-6a22-3091-b783-4615397db9b3 | -10.9192 | -48.34097 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7be1e2d2-081d-3e16-93d0-387ae5691492 | -13.44834 | -48.48993 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a598caae-d93d-3232-821a-1a04686e82d2 | -6.671 | -50.91745 | 2026-09-13 04:51:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e748e651-9821-38b4-ac54-c1ef579bc642 | -9.59211 | -46.72132 | 2026-09-13 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac4ac06b-20ee-32a4-8381-fae4f6f09dfe | -10.30918 | -45.29745 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 498739a5-9525-30d7-a471-6efe59ffe537 | -10.62556 | -46.10862 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bf7ca69-7084-389f-8794-ee7e44a794e8 | -11.19724 | -42.78198 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 7792dafd-03b6-362e-89ab-738d39996e75 | -11.24954 | -54.15776 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bc328c7-f408-3e56-af72-399c36f322e7 | -10.47297 | -48.6388 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0221636-8327-3247-a51d-e2bd4f9a9e5a | -10.6844 | -54.15921 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2eebf951-7cce-366b-b4a9-0d6d558ddff8 | -7.8697 | -54.7004 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ae5c481-151c-3fb7-9d38-99d5a1c4a6e4 | -14.27686 | -45.65 | 2026-09-13 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1694274e-52c7-3576-9f28-6ea0a33d5beb | -6.09749 | -55.67325 | 2026-09-13 04:51:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d205912e-8a94-3603-af8d-e759993f1d87 | -6.73412 | -55.63695 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f93bd5a-e404-3e4c-b18f-db5c238a1869 | -6.38015 | -58.29623 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 500d15bc-c89d-3e0b-b3da-6d812f916093 | -6.65789 | -58.88225 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a2df095-68bc-3e5e-8b46-a5e30bb4c8e6 | -10.93477 | -48.35529 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8523145-b955-3fe6-bcf4-0bbece07600a | -10.35755 | -46.66889 | 2026-09-13 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 938484ac-89d9-34a9-8510-bf59f10ac580 | -7.53713 | -44.898 | 2026-09-13 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33614fbb-3ba7-37e4-a990-004f724f7dbf | -15.2641 | -42.80157 | 2026-09-13 04:51:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cb3a955-822c-3e1f-92ff-26b7c09370eb | -10.89601 | -47.80399 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23668993-a1ea-3250-98da-122d7b4e29f4 | -13.60833 | -47.87523 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13f3d48e-84ce-36c4-b0f6-b3ca482f1018 | -7.85869 | -54.7002 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22c9ab26-24e5-368f-a699-e421e2e66ec7 | -10.58426 | -51.36263 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34fc8c06-a4ce-331a-aa4d-2a8db6ebf757 | -9.5958 | -46.72185 | 2026-09-13 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 276675fe-2c08-3927-a9f6-d48a01ec1935 | -6.07925 | -57.86654 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7cea3c1c-0501-38e3-b285-c487d695b975 | -5.9787 | -57.76493 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README37.md)
