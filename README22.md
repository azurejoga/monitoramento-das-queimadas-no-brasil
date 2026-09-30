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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3625e2f-b471-3791-a933-480f43c2176f | -7.08301 | -41.73558 | 2026-09-30 04:32:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| abb55231-712b-3bf4-adc5-01440b962c90 | -5.73553 | -45.16391 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d950dd25-d61a-3cf9-a310-c697d65d79b2 | -9.16173 | -45.59809 | 2026-09-30 04:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9bbfce6-fb7d-3f26-87b5-999d302dd02a | -4.29005 | -48.60523 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9233d8a6-2977-35dd-ba9a-ef6055222904 | -5.7261 | -43.27908 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03ba7693-e698-36af-bb39-d9950e22cb76 | -2.38464 | -47.60393 | 2026-09-30 04:32:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61d38739-faf2-3a6c-842a-e4d81ff3a67c | -7.82418 | -45.81543 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bcf9f946-17f0-3c7f-9047-77a0f76ac194 | -4.31349 | -46.77543 | 2026-09-30 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb3cbe17-124e-3d5f-9765-74f6512e0e45 | -6.21035 | -42.51626 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f936776f-a23f-3620-a260-3107b2ea8558 | -4.80772 | -49.46445 | 2026-09-30 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8949043a-1729-3210-90ea-10efb1d6819f | -8.39069 | -45.44168 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23d53f78-43f2-3d02-9351-8e397b966f8c | -3.01472 | -53.88195 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0157801-15ba-3dc0-a221-f1b5490dfb9f | -7.82026 | -45.81844 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dae7ed9-760d-30d2-94a8-7361b496cccd | -3.23812 | -46.94336 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| f40f327c-f9e1-3b97-a64c-1c7ddde6f364 | -2.98028 | -51.03922 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ead52e76-7e72-37b7-9992-5acc621d0bf5 | -4.11973 | -48.81912 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 627342dc-d5c1-3d0b-ac7f-a5daba983604 | -6.37994 | -45.80606 | 2026-09-30 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8323bfda-3bed-3117-85c2-e8e5af906edd | -8.05212 | -45.46618 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 899f49bf-7179-3bcf-88be-71a8f3623f36 | -6.1128 | -55.69938 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2287e9a5-764c-375d-8cfd-c80a6a478eb5 | -5.74562 | -45.05802 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7846799d-21d1-35f8-8c67-5cb197e5bf18 | -5.73506 | -45.0599 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91d565d7-0430-3e4b-886c-8064c93c8221 | -5.81363 | -46.22104 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3c3ab23-60aa-3707-be65-ab29fefed411 | -4.54114 | -50.77603 | 2026-09-30 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78e7c591-2b59-3b29-b759-cc2ac557f8bc | -2.73839 | -49.41489 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f83570-bba9-38b2-aa4d-26a60d7044cd | -3.15412 | -54.07797 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e264bee-9acd-364f-83d9-554ef5f619cc | -2.97868 | -51.04908 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 412ae4fd-c33c-3495-ab24-ccf7ce4a54c4 | -6.13259 | -53.29948 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| adac0e7a-6cbb-3062-9b7a-89f068442549 | -7.83086 | -47.93152 | 2026-09-30 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35df88f6-2f42-3cba-9238-a8418d42c1d4 | -2.64071 | -49.27132 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27981451-ea3b-3057-b10e-fcd80124aaed | -6.20922 | -42.51314 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 93c26566-efd0-3709-b76d-5f6081efbf9e | -7.67892 | -45.95892 | 2026-09-30 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20ace237-7827-3bc7-bbab-fd3f30766877 | -7.45871 | -45.78916 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d83cfc5d-3793-3495-85f9-f332bcdade8b | -7.08235 | -41.74668 | 2026-09-30 04:32:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c48d289-e81f-36c2-bf50-409a9f831ab8 | -3.23942 | -46.93516 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 21a158d4-8a31-3f48-814d-67bfa55b70cb | -7.50445 | -45.82559 | 2026-09-30 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f977ecf-8b67-3e03-9138-4a5d35374385 | -3.82919 | -55.79354 | 2026-09-30 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6274292e-c65c-3bfd-bccf-335b038de6fe | -7.84927 | -45.83035 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b0d13f60-3f8b-3a54-b16e-32e7d32b8d10 | -4.2692 | -48.55986 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2d0a3a5-3d5a-3e29-b0bb-04b2e3465982 | -6.79394 | -55.82286 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dc8b0e5-48c3-3410-95d3-b73cb15049bd | -4.02468 | -54.19824 | 2026-09-30 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 469efdcf-3022-392e-886f-b5a311d5a8d7 | -7.49502 | -45.79856 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc01df0f-1de5-3835-954b-d7e453cab0dd | -5.69918 | -44.73311 | 2026-09-30 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8e8e9996-5b48-3fb1-be0d-5ec85fb514de | -8.38573 | -45.40864 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8af31488-596f-3fa5-80c0-5b66f987d7c6 | -7.17136 | -55.40387 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1dec4b2b-f956-3ee4-bc31-e6872722017b | -5.36282 | -47.91511 | 2026-09-30 04:32:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c77aa455-d609-39c7-92e3-aadef40a0d2e | -4.11495 | -48.82352 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 652cfb93-a8e1-3d9f-8a01-cc71e98e763a | -3.15227 | -51.03788 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 053b1eec-91c1-3a4d-aeab-de4d3dcde686 | -3.22076 | -46.93624 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e905f85-30a6-3f36-9633-c64cc64bc34b | -7.4615 | -45.79323 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0cb2e64-7b0b-3cf0-92e9-31610c360e04 | -7.38562 | -47.01441 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8792a7d6-6aae-3e8d-a540-5f977107d970 | -8.37131 | -45.392 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c643541-4125-34dc-8bcf-e7701e0a47d6 | -7.50769 | -55.03172 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e0a4fab-860a-3db9-842a-b4cdc728a8fc | -7.81634 | -45.82145 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fbd99183-b5d2-36e5-a8fa-6fa8a4df9ca6 | -7.07391 | -44.36293 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7717505-0e8f-3f71-9646-bc3540061bcc | -2.37727 | -47.60514 | 2026-09-30 04:32:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b70cc99-6820-3738-bd94-fe0ec714cb51 | -2.99354 | -51.04652 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87aefcdc-c3a7-3ad0-b66b-1d301aa3850c | -7.02817 | -44.63055 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4acb8bf2-3540-33b8-9667-6d7dcf4a7339 | -7.49781 | -45.80266 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27b99358-0152-3efb-9069-f27463a328e3 | -2.98107 | -51.03432 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a253816e-5295-3d86-985d-ad21513b1817 | -6.71338 | -45.62595 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 922c370a-3433-3664-b4f8-44521facf83f | -5.73895 | -45.05694 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fffb37e5-9f83-3da9-a2ae-79a8e7410e66 | -3.42117 | -48.33883 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 880708f4-ffb2-3d09-9477-ccab6950a076 | -8.9802 | -44.17819 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36ee5fbc-a8f0-37eb-b5da-a23342e4181d | -5.32741 | -46.2015 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a99293e4-aa92-38ea-a872-bb19c33d8642 | -7.47448 | -47.41787 | 2026-09-30 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 554812af-c371-3b16-bd38-e3c1f091d2a9 | -2.98645 | -51.04238 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0213cd11-77c1-3b33-a14a-61fa7322e907 | -6.30106 | -45.94757 | 2026-09-30 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d223b097-7519-3c03-aee1-7131380eabe1 | -6.11361 | -55.69492 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b143849-de49-335f-9b56-5a0367e74ab7 | -7.06691 | -46.57086 | 2026-09-30 04:32:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b92267b0-43b2-3a69-9625-c1dc94aeb1f9 | -5.73181 | -43.50555 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ea91c55-7fe1-3a78-80fe-dc9c488576cf | -6.33393 | -51.15186 | 2026-09-30 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58bbb576-1846-3255-bde7-932045fa7821 | -5.73284 | -45.05238 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fe0902b-8e9a-3e7c-92d3-55922bdbf8e2 | -2.89988 | -40.39165 | 2026-09-30 04:32:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fc1f0b99-3769-3af5-8334-e43302fb87a8 | -9.30942 | -46.2517 | 2026-09-30 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc6d3070-e8bf-385d-9607-aad978bf6ba7 | -9.09978 | -47.17254 | 2026-09-30 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12cfba91-8316-3ec5-b5eb-f6ab1a1033ce | -2.44748 | -49.21757 | 2026-09-30 04:32:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85634058-33ab-3f61-8586-ef45cae21036 | -5.81481 | -46.21368 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e651645b-c8c2-386d-8a93-ab5151a25660 | -6.7879 | -55.82175 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68cbcbf0-4ab9-317b-8811-b6b284b1f78d | -3.56847 | -50.25926 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84a31e4f-28a0-3e70-b424-6e71c8c97b3f | -8.59267 | -50.41627 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f666712f-6efa-3380-b267-b365f70d7428 | -7.53223 | -44.54327 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92895294-1ee8-3580-a31d-2e4029e04b2b | -3.97218 | -48.00552 | 2026-09-30 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ecb2852-e6da-3580-83a9-d414657f29eb | -5.74277 | -45.16148 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84f984ed-5bec-3529-96b2-c684966df191 | -7.84592 | -45.82981 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 819d1782-ae0b-399c-897f-6b028dfdb8f7 | -2.98729 | -51.03746 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a3d84c5c-0553-3b2a-a5eb-78c3e9f7561f | -5.76113 | -45.17521 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7436faeb-3ba5-3594-ba72-b76e4d3d5db7 | -5.81823 | -46.21422 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3792649-fbfa-3f1b-af17-f66c0b7ead84 | -6.10034 | -53.09029 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17f27424-4ccd-3a9a-bb00-ac8bb70b730b | -6.33317 | -51.15622 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e77bdc79-438c-3b5b-87e5-a9503fe9df4f | -4.02259 | -54.21041 | 2026-09-30 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e272460-4e40-30ac-861b-22bf54d6b8f4 | -2.36773 | -50.34624 | 2026-09-30 04:32:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ef234a-cff0-3083-9217-db82b9af8d07 | -7.83422 | -45.81702 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4a4314a9-5a5c-3ced-8b6c-7f0bcd731105 | -8.75324 | -44.9087 | 2026-09-30 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3a0ae98-3c87-3453-8582-e26bb250684c | -3.10744 | -50.28394 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 60d58d41-7790-31a1-8c5a-6208e5f7d376 | -7.84705 | -45.82271 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 08114909-593e-3b96-ae2b-acd0ee9e41b4 | -2.99045 | -51.03588 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03f11963-6e01-370a-a0ca-842263036fc1 | -3.9684 | -48.00488 | 2026-09-30 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76d8e2cb-c537-39f7-aae8-18a662e9c568 | -6.11114 | -55.70856 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c39fc88-19bf-3223-b9ee-d94db953d6c0 | -8.83649 | -49.70607 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d0c22d9d-e22a-3006-a3a2-740263f6bd38 | -2.9701 | -51.04259 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README23.md)
