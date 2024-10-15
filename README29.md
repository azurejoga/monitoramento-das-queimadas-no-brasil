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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6c3ad67-6c87-3e2f-a2be-5701136f1f1a | -6.07722 | -47.0569 | 2024-10-15 04:02:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28590f0e-7907-331d-9256-3c2532eff73e | -6.05172 | -46.60075 | 2024-10-15 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7413ec07-5635-37e4-8a6e-7485d3de19a0 | -6.05024 | -46.59785 | 2024-10-15 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1b06663-4555-3b0f-aadb-c5160adbf8d8 | -6.04498 | -46.6016 | 2024-10-15 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d555e0f-2a8e-35c0-9491-ce8efcc3fb23 | -6.0397 | -46.60546 | 2024-10-15 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79c50475-d4bc-3ec7-a21d-b9579d8996fe | -5.60601 | -47.96034 | 2024-10-15 04:02:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca156c7a-1b6c-361d-96e0-6fa714d512dd | -5.60594 | -47.95749 | 2024-10-15 04:02:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dac36ff-bf8c-3cd9-b1c2-78179b76b880 | -5.60545 | -47.96038 | 2024-10-15 04:02:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54482f0c-a9e4-34f7-aa0f-9778747e77f5 | -5.60046 | -47.95956 | 2024-10-15 04:02:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46c6c673-1ac8-3295-8588-44f0edcb7959 | -8.00801 | -47.21143 | 2024-10-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36f5f1a6-2a7c-3ff7-b0fe-2dd5f0135f8d | -8.00712 | -47.21226 | 2024-10-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b46ff35-d70a-38f4-8b81-f56e2b14b44b | -7.91011 | -47.83723 | 2024-10-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cd6db1f-edf6-33bd-b220-728633e168fb | -7.87607 | -47.74841 | 2024-10-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a95bb5be-a5aa-3e08-af57-d779f8376438 | -7.87133 | -47.74765 | 2024-10-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32f04510-d9ad-39da-ac02-5c02392dcca9 | -7.09758 | -48.33398 | 2024-10-15 04:02:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee2a2243-ec64-3821-9727-038db383b632 | -7.0931 | -48.33025 | 2024-10-15 04:02:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf669000-2c66-3013-951f-7ddac405b234 | -9.20731 | -48.66039 | 2024-10-15 04:02:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 054cb22c-c825-3abd-855f-fa5e36ca65fa | -9.20623 | -48.66632 | 2024-10-15 04:02:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c165900-110f-353d-97fc-0eae9d4fd484 | -9.2024 | -48.65946 | 2024-10-15 04:02:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ea181d2-68e4-3759-8873-974bc1634ad8 | -9.20135 | -48.66526 | 2024-10-15 04:02:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9982b46-8c90-3480-8109-8e85a3ba8da6 | -8.1243 | -47.56998 | 2024-10-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba3443bc-83a6-35de-a2a5-eec8c3e7089b | -8.12343 | -47.57497 | 2024-10-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a5348151-817a-3150-9418-245a3a67d903 | -9.33079 | -47.36989 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9a12d34-e6a9-3059-be43-5d37b2cc36ee | -9.32629 | -47.36911 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 874b0e02-04c6-3765-b672-28fc57988df2 | -9.28478 | -47.89666 | 2024-10-15 04:02:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07ef46fa-6aff-3dc9-aefd-7eaab68c7095 | -9.2016 | -47.56461 | 2024-10-15 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d2c5174b-c252-3ead-974e-f07346e1d72e | -9.16659 | -47.60229 | 2024-10-15 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88dfc91a-4d30-3431-9807-0a4ad6a16214 | -9.11192 | -47.69884 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 774b746e-0d63-3295-a2ff-b3b6e49b590a | -9.10948 | -47.65844 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89c67b6e-f07a-38f9-b5a3-6704190e321c | -9.10488 | -47.65764 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 534bf4f2-0659-3889-bbef-ac5e54aacc80 | -9.09201 | -47.78547 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9c1839be-06a6-3129-af57-15e7fdce115e | -9.08737 | -47.78464 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c7957d47-7b58-34ce-9b4d-3f8fe06c4085 | -9.08651 | -47.78957 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5c52a0e5-a31e-3ef5-ae36-b64f362c67da | -9.08273 | -47.78379 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4ec5b30-69c3-3547-bd3f-4eec73dab657 | -9.08187 | -47.7887 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e8ffbeb-d0e6-3792-8097-141af675d22e | -8.92761 | -47.91174 | 2024-10-15 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38ed19a6-6c27-3e6b-9dfb-ddaeaa95bdca | -8.92198 | -47.91618 | 2024-10-15 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e738352f-7c80-35ac-910e-2e054f08c429 | -8.70538 | -47.54031 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b7276cb-5f8d-3943-b5ea-1eb2ec5fbab4 | -8.69163 | -47.53762 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d533a849-c534-3b89-a04e-f240ed68e002 | -8.55878 | -47.81581 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8794f6d-4e8c-31ff-aec6-be7e13e51a0a | -8.55237 | -47.82491 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 505bbdc0-d6c8-3da9-88ce-5e5015b6cbdd | -8.46687 | -47.8151 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3ae97f2a-b1b1-345e-b33f-b1561e5f1f28 | -8.46619 | -47.80779 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 802c8a37-7631-3907-8f3f-c410a841546e | -8.46597 | -47.82014 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e48649a-a569-353f-b3e4-5deba92ca2ee | -8.46447 | -47.8178 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 55ba5660-f991-3fe7-82e2-e839e52a4de4 | -8.46306 | -47.80936 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f3ea51e5-e75c-32c2-b8c3-0ea9fd56ba1e | -8.46216 | -47.81435 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7af5a6fb-2083-30a3-a128-a0afbd6d7f8a | -8.46149 | -47.807 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b409872a-8ec1-324b-8b2d-d6c475afc1bc | -8.45924 | -47.80363 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f7e8aba1-5492-34a7-92ae-aebb912b1036 | -8.45835 | -47.80858 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ed2087ac-4d13-33fa-9ad6-e22858bee9e8 | -8.45764 | -47.80121 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 88bcaac7-c9aa-3c79-b007-33ad8552d15c | -8.45678 | -47.8062 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a582a5a3-f2e5-34cc-ab60-eed5144acac1 | -8.45454 | -47.80283 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7ad1af65-5db5-315d-9e3f-0cb34f7c421e | -8.45294 | -47.80041 | 2024-10-15 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c60f5060-20c9-36e1-9470-c90359fc9b71 | -8.44722 | -48.03353 | 2024-10-15 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b5f99cf-48aa-3574-b0ef-a0dbfe421d59 | -9.99825 | -48.86154 | 2024-10-15 04:02:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1436219-8ecc-333e-ae18-5571930a2038 | -9.99654 | -48.85964 | 2024-10-15 04:02:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19fb830b-f2c8-36e0-bd04-c1e71ea600b6 | -9.89821 | -48.7606 | 2024-10-15 04:02:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da305daf-6f8c-3157-ac6d-8db107a366c9 | -10.14357 | -48.82714 | 2024-10-15 04:02:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b145ff95-d19f-3e68-ab36-b6a5b70836db | -10.13869 | -48.82624 | 2024-10-15 04:02:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bba64ebe-cf5b-384a-8f1e-4ccf5606054c | -9.93989 | -48.13418 | 2024-10-15 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a5fa03ef-c149-31f3-bfd2-b5186610713a | -9.93897 | -48.13921 | 2024-10-15 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1e53af29-4733-36b1-9fbd-890f6af8a853 | -9.93608 | -48.12858 | 2024-10-15 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e018cca8-aa15-3590-afcc-da7b509a655b | -9.60454 | -47.71593 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de5160a6-38c1-3c00-bc31-6cc39cc3d2da | -9.60115 | -47.73489 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9cafbd34-f373-359d-85c5-a4d15b32b3dc | -9.59997 | -47.71505 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a063b3fb-6e14-33b7-84fb-2befdd56c442 | -9.59912 | -47.71982 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0e1c6b8-d2cc-3f38-a61e-fcdbd8202350 | -9.53024 | -47.78925 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ebfb60cb-b034-36ee-80d3-b61c17b25fa0 | -9.5265 | -47.78348 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2c4fa46-5ade-33ce-a144-9fa0edcdb5f4 | -9.52565 | -47.78832 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d89517ef-f4ef-3a85-9660-6b8e4f317986 | -9.52477 | -47.79332 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 902e7297-713d-3da3-87d9-f22b5cf73d4f | -9.52389 | -47.79829 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 612a9683-78d0-306c-8c00-648a599a9d0a | -9.51928 | -47.79747 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b94a3c3b-e4e1-3e65-baaa-354e2ac3a7d0 | -9.51427 | -47.63871 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19f7b1d5-a67a-36a4-847e-c959a4c9b859 | -9.51379 | -47.80165 | 2024-10-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c1fe02b8-27d1-3b81-9223-9d39817ef29c | -2.85899 | -48.24311 | 2024-10-15 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 036a28c0-2547-3e7a-96fa-046fa6df83e2 | -2.78811 | -48.09138 | 2024-10-15 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36b54cbd-e51e-31ea-8567-6d39a1e00283 | -2.78765 | -48.09198 | 2024-10-15 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ac24880-4617-38d2-a9c7-3fcb7173c105 | -2.78389 | -48.084 | 2024-10-15 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5efa2a18-8e1e-3494-97e9-cd2abed013a1 | -2.78348 | -48.08463 | 2024-10-15 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ed2be21-a430-3fd1-acf5-cf09c07e4175 | -3.46677 | -47.67055 | 2024-10-15 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b27ec7f3-bafe-30e9-b394-1b0851c08cbc | -3.46628 | -47.67351 | 2024-10-15 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c967f559-2332-3c93-bf67-00aca8a6854f | -4.57649 | -48.01643 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41981b6e-1cda-3648-bf00-50711712e41d | -4.57598 | -48.01945 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f89c4b66-639a-3224-88e1-864e6538f977 | -4.5714 | -48.01559 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf0b30b8-da7c-340e-887a-37fcb2c71793 | -4.57088 | -48.01862 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f0609e8-95bd-30b1-a76a-a5db76ca2bbf | -4.56578 | -48.01783 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c15ac624-c3f4-3d21-93ff-33f4c4a3a730 | -4.56526 | -48.02089 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 335413eb-15ab-3705-b7f6-b9c5475db7d9 | -4.38803 | -47.76065 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 16774706-fd58-3b25-8e0c-6363bfb5680e | -4.38753 | -47.76358 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 3b43dbfa-1b0c-3180-a3cc-4181197cd6c9 | -4.383 | -47.75989 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2bab0234-8777-303e-8025-86f82a4a5d3a | -4.32619 | -48.62751 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d25ce60a-e2ad-3d45-a61e-0f6e28ee5848 | -4.3256 | -48.63092 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd8e27fc-05ac-3aa2-87ca-4c60411654db | -4.325 | -48.63438 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50861d7f-c2c5-367c-bee7-b5987f3cda71 | -4.32026 | -48.63008 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c82baa2-f165-31bf-9413-01837f70260b | -4.31967 | -48.63351 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ce1c14a-5116-3fde-9bc9-10527e737209 | -4.28032 | -48.06883 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 108de4e7-ab55-3bd7-96ef-442c948034b8 | -4.27624 | -48.22148 | 2024-10-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36aa7ffd-ea9e-35cb-8f21-f1f7a3a0afc3 | -4.2757 | -48.0649 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97d5e5c4-8c3e-34ef-884a-d63197946786 | -4.27519 | -48.06796 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README30.md)
