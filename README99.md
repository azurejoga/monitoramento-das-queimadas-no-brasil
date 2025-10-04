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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79d13797-1776-3019-ae37-154cbb6f5fdc | -2.68152 | -48.38802 | 2025-10-04 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec69bb4a-96f7-3306-a56d-a275e5967e15 | 1.91911 | -50.85855 | 2025-10-04 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3bf3672-5a9b-352b-8fc0-dd7b061529f0 | 0.4613 | -60.43801 | 2025-10-04 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a63ab95c-22cf-305e-b75f-1dc9c61fd120 | -3.4462 | -43.33483 | 2025-10-04 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a2c488d-4328-30db-9709-ca2ac87351f5 | -2.68532 | -48.39323 | 2025-10-04 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5128298f-ee5f-3507-8929-41967edc4c78 | 0.50324 | -50.77684 | 2025-10-04 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d2bb0363-0e5e-371a-9263-ef1ca998bf66 | 0.465 | -60.43321 | 2025-10-04 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7839cc6-84d7-3c28-9369-8ae6e28e4978 | -2.69047 | -48.38942 | 2025-10-04 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 702b8118-c4b3-3d59-a184-43894092f52b | -1.88692 | -48.39837 | 2025-10-04 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f67832f-2140-3151-8445-1565fbfee18b | -2.55509 | -47.65854 | 2025-10-04 05:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17a45372-b976-36f7-946c-68136f4c7f00 | -2.25909 | -47.85317 | 2025-10-04 05:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 863019b2-2c5e-32b4-aab5-1590fe08bfd8 | -3.39787 | -50.275 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44816990-2eba-3a87-815f-b9914a5ab4c5 | -8.21942 | -46.79682 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86514c9e-d184-3420-bb5d-87d95fd3739a | -3.70321 | -50.96808 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9051adeb-0982-3c17-9d94-da6c761575de | -10.00205 | -48.27404 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fa4d303-3f26-341e-aadb-a0e34506ec69 | -8.62961 | -54.99844 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 019ddc53-85b1-3dc7-9a6b-e507a15006e0 | -6.74657 | -44.58518 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86f27e6a-5a10-3814-bf6f-d31f8e743cd5 | -6.65045 | -42.80916 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| da60c198-708c-3545-ada9-bf02d0f387c7 | -8.85038 | -46.79464 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2f3cbc66-f4bd-36dd-b020-abf6d70c4de6 | -9.34732 | -45.7864 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60e4da79-c4c8-36c9-86b4-1202322a8be9 | -8.35417 | -46.83845 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8371c0db-89e9-3dbd-bf17-d46f9a90d04a | -4.89738 | -49.96396 | 2025-10-04 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 492591d8-529d-30be-a916-ea236c793bdf | -5.226 | -50.82599 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64f2d550-6001-3d6e-af2a-bf916da3f600 | -9.94337 | -50.89314 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b0262d4-4408-3894-bf07-fb948e2d176e | -10.02369 | -50.19399 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2122ad9e-eedb-3028-a80f-199971fd47ad | -8.84326 | -46.84886 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5a19399-f0cc-314d-995e-3d4044266685 | -4.82903 | -42.76485 | 2025-10-04 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3059fbe8-427c-3e11-843d-87ccb4920145 | -6.2304 | -44.65414 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 141be663-c697-3304-b268-a2f8cee1f3c2 | -9.99125 | -48.27822 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a4dca19-2794-3a26-a027-9982f45ae94d | -9.63484 | -54.30971 | 2025-10-04 05:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a03a428f-30d7-3870-a4b3-03f0df858bd8 | -6.87351 | -47.23387 | 2025-10-04 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 906affce-8a84-3272-a2ce-700d2875c7c6 | -5.70267 | -49.30238 | 2025-10-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae1a6f3e-46b0-309b-8395-1593a4b8e5b5 | -4.82575 | -42.76331 | 2025-10-04 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b3884ed8-4e4b-3671-ac64-6f5d874749c7 | -6.71395 | -42.81377 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 77b20ee1-94b4-3c7a-8b65-b24f923684fa | -6.43894 | -44.45468 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7f3f328e-1e4c-3a2b-a95b-829bd28ebf61 | -9.90254 | -43.73364 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 014c7f0c-dfaf-3c86-b0fd-d62bcfc32ed1 | -6.37313 | -43.89424 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 08ab5a40-c781-31c8-a7eb-81ccac3fa448 | -6.20405 | -44.33979 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa6aec83-8264-318b-9da4-ce197375c27e | -5.4288 | -47.09735 | 2025-10-04 05:04:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bc04b42-3cb8-3704-8d67-e4cff84128a4 | -8.10961 | -55.02075 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a63a6400-7f77-3838-83d8-c9a5a5be1482 | -9.94601 | -50.23624 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76c83229-eec2-30be-a290-a846e4677a33 | -5.79122 | -45.77702 | 2025-10-04 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d5f71b9-9d9d-3952-ab2e-0b8fc0c62510 | -3.06959 | -49.38136 | 2025-10-04 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 203c1eb7-209b-317b-b91e-a8109cdd0a20 | -8.12616 | -50.23483 | 2025-10-04 05:04:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d810a65-bae5-316f-a730-4eed9ec4feda | -7.91593 | -49.64607 | 2025-10-04 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb9a062a-d966-3346-9a74-e19c45fc288a | -9.94161 | -50.2356 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41e062fe-4bda-3842-ab08-0bb64ca2c355 | -9.2665 | -45.77398 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4a22fb1-b480-3ba2-8d7a-7bb38f39ddbf | -4.4446 | -43.23358 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ac34e7a1-f6ef-3244-8e8f-00e79b24daa9 | -7.04362 | -42.77348 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 75f138fd-a91e-3e4e-adf2-72c2b42f476a | -5.4339 | -47.09819 | 2025-10-04 05:04:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bb6da31-9987-3772-82e1-244fe2753db3 | -6.24461 | -45.33636 | 2025-10-04 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 460804fe-dce7-38d3-b6ac-1c67abbd17dc | -9.31733 | -54.5336 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f343d955-679a-3cc1-be89-c4833bf03a55 | -6.74658 | -44.58651 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 98efe9a8-fc35-3999-8e69-660cd34cdba0 | -7.55381 | -42.39993 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9d41733a-380a-3a1a-8e34-8177c903ec87 | -9.94543 | -50.2406 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3959c2f4-ce28-3be0-a82a-920d1a6b0773 | -5.7993 | -43.608 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e973865a-e9da-3a5f-90b1-7cbe005c4408 | -8.61721 | -54.96715 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7068add8-4eb2-3c81-baea-2b743008e995 | -8.52703 | -47.21254 | 2025-10-04 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83c5216e-aa4f-38c4-bcb8-4ebef951cdcc | -3.39441 | -50.27093 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa60d9b5-6af4-3158-a884-3026f184701c | -8.64148 | -54.59196 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dc6359e-8028-3a90-a520-4f9230bf290d | -2.78462 | -51.79559 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bebb8f2-9d6c-3846-b040-a2124a3a7a75 | -7.72928 | -49.85612 | 2025-10-04 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e20337ce-132b-38a3-8fb4-21b76d5a94aa | -9.90531 | -43.74166 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b07be48e-49e2-3ba8-9cee-390c9fda675e | -9.91074 | -43.80901 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dbd0b88a-a0fa-3369-be9c-a321186cc872 | -10.34228 | -48.16621 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa36ab9f-6734-374e-a5c0-72ff93dac362 | -8.20426 | -46.99075 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 126a348b-cdd0-3203-ad92-684667c010c5 | -6.34999 | -43.45765 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 494b9857-5d07-3e45-a814-f09b0de231fb | -7.70949 | -42.5694 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c2b88ab2-b224-3d8d-adf8-695e67b6b32c | -4.44238 | -43.24998 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 8ab815fc-aed9-30a0-b77b-10816b82f628 | -5.96171 | -43.49008 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 182d5e39-d01d-3f69-ae6a-f18fed92d5d3 | -6.6565 | -42.81596 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fd0cb6bc-b8ed-38ee-b4bd-c7809209856b | -7.16133 | -44.99687 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7e4d3661-055c-3a4c-933e-2ed8f3ccd6f1 | -8.62509 | -54.98307 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e4b2324-720d-33b0-865e-3f5da3078b8b | -3.53279 | -52.9924 | 2025-10-04 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7bf9214-ea3a-3323-805a-5ebb78b007a2 | -4.05297 | -49.3164 | 2025-10-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e0d6743-1705-34e7-872e-c5f5b3673fb9 | -5.20207 | -45.06696 | 2025-10-04 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e43c270a-a363-39f6-a3b0-7d1b8a629395 | -6.87662 | -44.50163 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 79871e45-4b84-38e3-9bd9-d3787907f5fd | -6.46028 | -44.57444 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1963a30d-8d95-3a1a-b5d1-ca7f597f464e | -9.32187 | -54.52658 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c16197d-f284-3145-9bdc-7e9ec693f7d3 | -6.07772 | -42.51181 | 2025-10-04 05:04:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a7b71475-e011-3fab-9745-1bd929d7f9fe | -5.82348 | -42.88791 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1c8ce3f8-18d7-3d5f-b770-022ac10106a2 | -7.52972 | -61.47997 | 2025-10-04 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76346a3d-17fb-3a52-a677-68a931d022b6 | -4.89612 | -49.96007 | 2025-10-04 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58700563-5777-3bc2-bce0-6b869d22bf2c | -9.32529 | -54.5271 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 505f501c-5697-3609-9eaa-698883694541 | -6.66156 | -42.83005 | 2025-10-04 05:04:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c989b6d4-6b14-3061-8780-a738419d41cc | -8.5319 | -47.21662 | 2025-10-04 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ae2fc24-17e6-31d9-86f0-4dfe69934f49 | -8.12447 | -50.24699 | 2025-10-04 05:04:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04a1d9d5-95b9-334c-a995-d044bbf0bde8 | -8.21402 | -46.79587 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 561e0382-5be2-32b6-b652-52f6e9ee13b1 | -10.34683 | -48.17124 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 283c3271-550a-30f5-8b32-c8ae007f3eab | -3.3984 | -50.27155 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a19fd461-e9a6-3760-b2fa-64886742c734 | -9.3361 | -54.52491 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 098fb473-80e0-3058-8d78-c94d3f96bd94 | -9.63772 | -54.3141 | 2025-10-04 05:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36431cbf-0f26-3be4-a7f9-1d4edfcde1fa | -6.60366 | -44.29672 | 2025-10-04 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a84ea60-7e72-36b7-a5d6-174f3d955e0f | -9.94983 | -50.24123 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0e6f034-805f-31e7-ba46-b0aeb50ce8ed | -7.34694 | -44.34913 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f0d46dd3-bb3f-35f8-b952-867a16c0cdbb | -9.93335 | -50.19701 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3116fedf-310d-33b1-904d-3d2562647a88 | -6.22554 | -44.27548 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56f9b354-f59c-3666-a6a2-70b1803129a4 | -9.33613 | -45.77979 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e85231df-07c5-362f-b769-63819edddc28 | -5.79018 | -45.78438 | 2025-10-04 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 616e830f-c6e6-3811-82e3-1b0a79755e94 | -9.34898 | -45.78549 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README100.md)
