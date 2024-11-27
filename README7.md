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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2458e60d-4009-35c6-bf6b-16ba8baeb9b7 | -5.7803 | -43.009201 | 2024-11-27 00:21:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e76f9d23-983f-3a11-b6dd-65cd7894c961 | -3.889 | -42.413601 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| edcf0915-f9aa-38c3-9009-b71f5b3ace10 | -1.6532 | -46.925499 | 2024-11-27 00:21:00 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb078ec-5aa0-398c-9fa2-3eba1cd29435 | -4.2469 | -42.444302 | 2024-11-27 00:21:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e45b7be-8cd2-3bb9-8d29-e3eda40d9d0f | -5.8948 | -42.968899 | 2024-11-27 00:21:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e489bb3b-b728-3c83-aa77-86675fe7a1fc | -3.9755 | -50.345402 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88c40d8c-e74c-3de2-b4de-3b9a36e091cb | -3.0688 | -50.364101 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a52034a9-a90b-3d58-9240-575934d01d98 | -3.2054 | -45.733002 | 2024-11-27 00:21:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff00eba5-7b16-3c89-9144-b8a0b2f0d42b | -1.6011 | -52.427799 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf2aea6-a00a-3e66-bbe7-5557fc931e94 | -3.3448 | -46.3013 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb49b3c7-6512-354b-bee6-3e588eb3ffde | -2.8746 | -45.231201 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8aff9aa-d46c-3bba-8d82-da261d755044 | -2.9815 | -45.4739 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51e85be2-5f86-331b-864f-2db9f9479c19 | -5.0062 | -43.592499 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c9aaf0b-0bc4-3363-8f87-51cc1b6fcd55 | -4.147 | -48.447601 | 2024-11-27 00:21:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eac5b625-f503-3595-adfe-f0def33332e9 | -1.2559 | -51.719601 | 2024-11-27 00:21:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 139aea07-0a82-3bad-9940-3ec2db062c15 | -5.2525 | -35.4725 | 2024-11-27 00:21:00 | METOP-C | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c6ef520-21a0-3f1a-b40f-d8c56907720d | -3.4999 | -52.158798 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02c94d31-b2ba-3da3-b65e-9fce6cb84aa0 | -1.49 | -46.0755 | 2024-11-27 00:21:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b0f36e2-9521-34d6-8a0d-7c9001f590de | -3.7819 | -46.595001 | 2024-11-27 00:21:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19c77341-1d6b-3459-85ff-6eb469396717 | -5.2565 | -35.489201 | 2024-11-27 00:21:00 | METOP-C | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc8900a6-bc38-3774-bc11-32f533e3715a | -9.3726 | -35.926102 | 2024-11-27 00:21:00 | METOP-C | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72440c0a-4f6d-3592-9b11-4177419e6b9f | -3.1877 | -48.4172 | 2024-11-27 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 28da6fd1-5aa1-3e94-b42b-465e5e8feee3 | -1.6813 | -52.4537 | 2024-11-27 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e2b7ef10-14ef-30f3-9faf-4a3e16230a9e | -1.9376 | -45.7141 | 2024-11-27 00:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 11af4411-e089-34b9-b7ce-097c0118df05 | -4.2114 | -50.899 | 2024-11-27 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 02fbf773-5a7d-32c3-8f27-6f44b8e87f01 | -2.5963 | -53.9771 | 2024-11-27 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e6a3b0b9-bfe9-3a1a-9b45-41b2438f842b | -3.1876 | -48.4387 | 2024-11-27 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 250.1 |
| 963e9040-345e-39fd-9790-1a8bce91e9c7 | -2.8611 | -46.8186 | 2024-11-27 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 4eb6d3e8-95ce-30de-9f56-5f7191e7cc9e | -1.6624 | -52.7192 | 2024-11-27 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 303e036f-793b-3a4c-8019-27acc5e77c44 | -3.0154 | -45.4577 | 2024-11-27 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 7012e218-9a85-3984-a02f-36391eae96a8 | -1.9562 | -45.7137 | 2024-11-27 00:30:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7bdb215e-c209-31fe-8593-c9dedf1b5824 | -3.0153 | -45.4802 | 2024-11-27 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 6b64768f-dba2-3094-b2c4-11f23109c2dd | 1.3535 | -50.6207 | 2024-11-27 00:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a04eb091-9cb4-3dd9-b66a-604b53582e7b | -3.5226 | -52.1653 | 2024-11-27 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 1948d42f-e238-332f-8a51-0ce1677928b9 | -2.8239 | -46.8419 | 2024-11-27 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| af094cf6-cf55-3386-a3d5-b065b040fdf1 | -3.5411 | -52.1442 | 2024-11-27 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 52d6f92b-88d6-3543-9081-8db462a05ad7 | -3.1692 | -48.4179 | 2024-11-27 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 206.3 |
| b77244f4-de1e-32ef-9b92-dd4f38d2156c | -2.9967 | -45.4809 | 2024-11-27 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 5d9ea179-93be-3f09-af0b-b86278916b73 | -2.8346 | -54.1326 | 2024-11-27 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 91af0ce9-6e45-380f-a048-5e7493a159d2 | -3.541 | -52.1647 | 2024-11-27 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| a87e5c1d-7b0a-31a7-8f3d-f9ed11296c65 | -1.6813 | -52.4333 | 2024-11-27 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9cc57f18-8be1-363f-a1e9-ee11aac23a1c | -3.5226 | -52.1448 | 2024-11-27 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 50515fce-e6a8-35e6-81f8-21c734b585bd | -3.169 | -48.4609 | 2024-11-27 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a20c7d2c-3008-33ab-aa5d-5d58b71d5168 | -3.3201 | -44.0147 | 2024-11-27 00:30:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4e109587-c22d-3bd4-b267-1de3a3e91bdd | -11.7715 | -54.6828 | 2024-11-27 00:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2de80862-a9ea-3382-9fa9-ad9a6f189cc3 | -3.9675 | -48.0634 | 2024-11-27 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| bc75a51e-b834-3adf-bed0-0b27a919e49c | -4.2115 | -50.8782 | 2024-11-27 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7929e0ad-cc62-3247-aae5-36c9d3f1e17c | -2.824 | -46.8199 | 2024-11-27 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 1c9625cd-26b0-37d2-9f3c-67c16258cc57 | -3.1691 | -48.4394 | 2024-11-27 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 577.9 |
| 94243f12-f1d4-3d3f-bc0d-6407325928cb | -4.1417 | -43.8135 | 2024-11-27 00:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 99b2ec33-fdfc-3927-af31-d582daae402e | -3.1506 | -48.44 | 2024-11-27 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e0f79b13-b074-3e48-876b-5e9ec8659fef | -2.8347 | -54.1125 | 2024-11-27 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 21afd9af-026b-3720-8d24-876e911f81a2 | -2.8425 | -46.8193 | 2024-11-27 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 93bbcdeb-6823-3168-b91d-fd032e7ee5dd | -3.9674 | -48.0851 | 2024-11-27 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 85c97854-8a1e-32cd-a090-fbccb848b805 | -4.7195 | -46.5827 | 2024-11-27 00:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 969dea16-84ed-34de-bcd8-88a5ed0cac47 | -4.2299 | -50.8983 | 2024-11-27 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 75a608c2-d29c-3bdc-80b2-4daa79153ed7 | -2.1928 | -53.7839 | 2024-11-27 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 650f16c1-589d-3468-bc83-f0e230d2d0a5 | -2.9968 | -45.4584 | 2024-11-27 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 281.5 |
| c4265415-971b-30a4-b446-a0bdfdae54d5 | -5.9975 | -45.3607 | 2024-11-27 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e4119e16-dde6-3673-8748-6734335bffc5 | -4.7197 | -46.5605 | 2024-11-27 00:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a4dbca55-4b85-3735-8d7c-80ef158be20c | -3.3015 | -44.0155 | 2024-11-27 00:30:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 208f10f9-dd20-3dab-9833-064aa78f68b2 | -3.0393 | -48.5082 | 2024-11-27 00:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 28b2500b-4906-3f06-9d43-5f4b9862c3e3 | -11.7713 | -54.7033 | 2024-11-27 00:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5938fcc0-7e06-3979-890f-75a26a959266 | -1.9376 | -45.7365 | 2024-11-27 00:30:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| efb88b9a-2bc9-32ab-bc8d-3644aba72e83 | -1.6444 | -52.4951 | 2024-11-27 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a022d614-264c-381d-89a4-0be1f8d9d6f5 | -2.6987 | -45.6705 | 2024-11-27 00:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 022d4edf-9fa6-3d48-b7a8-91bf6489a371 | -2.6988 | -45.6481 | 2024-11-27 00:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 99c745a5-f05f-34fc-96d1-06e0a212ca52 | -2.8424 | -46.8413 | 2024-11-27 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| fea9f94b-f0e6-3ac7-ae0f-2f5393893a10 | -1.6808 | -52.7189 | 2024-11-27 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 77bdc2aa-d7af-3897-b55b-668dae2fe7b5 | -5.9788 | -45.3621 | 2024-11-27 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 1084ce74-b490-3f85-9237-14e1e16bac70 | -1.9561 | -45.7361 | 2024-11-27 00:30:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b796b73f-de4d-32b9-b5c4-b7fba1f255df | -4.1419 | -43.7905 | 2024-11-27 00:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7f26e663-463d-38d4-84a6-8b46d1019d59 | -2.8347 | -54.1125 | 2024-11-27 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| fbda2dc9-4c98-3e7a-9f4b-e72a1abd2aaf | -5.0401 | -43.5973 | 2024-11-27 00:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c2af4ea4-ef10-360e-85da-3e6b7bcefe8b | -4.1417 | -43.8135 | 2024-11-27 00:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e55d6359-d189-30c2-96fa-368f4007b97d | -2.8425 | -46.8193 | 2024-11-27 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 171eceb9-b019-3774-a7a7-70fdd0e5d4da | -2.6988 | -45.6481 | 2024-11-27 00:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 113.6 |
| e1140330-df6f-3208-81f1-ac671c715147 | -2.8239 | -46.8419 | 2024-11-27 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 31f4d193-fe37-3f99-a092-2a721fbce6ae | -4.7197 | -46.5605 | 2024-11-27 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 0fbc367b-40fe-3727-9d2c-6a3c91bc8cee | -4.2114 | -50.899 | 2024-11-27 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 262d43a8-c2f8-3ff4-83e7-68c945ed65f9 | -1.9561 | -45.7361 | 2024-11-27 00:40:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 1fe9c02a-4ab4-3442-99f8-6603338daa63 | -3.9674 | -48.0851 | 2024-11-27 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 2fd155e5-a50e-338a-80ea-a6d4a5d773e5 | -1.6629 | -52.454 | 2024-11-27 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e474164a-fd3a-3f60-9bfd-68d9c35260cc | -5.9788 | -45.3621 | 2024-11-27 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f21553ff-2d6e-30b9-a842-58ad1e7cb01f | -2.8424 | -46.8413 | 2024-11-27 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| ecf9565c-c579-318c-97ab-c4a1a3a5b386 | -1.6629 | -52.4336 | 2024-11-27 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6e04199a-b1ae-3f1d-8e37-3c154255754c | -1.6813 | -52.4537 | 2024-11-27 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ec2a12cf-5b90-3ea7-8cd4-6a7659c7211f | -3.541 | -52.1647 | 2024-11-27 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 08606b44-f2f1-358a-8023-84c055d15e54 | 1.3535 | -50.6207 | 2024-11-27 00:40:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b5e31eb8-04be-3d77-a440-56156eb69dac | -3.9675 | -48.0634 | 2024-11-27 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 12a88218-e08a-37b7-a41b-5231d68511f9 | -2.9968 | -45.4584 | 2024-11-27 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 216.8 |
| 36a53641-6a80-3930-bd10-3bceac143c40 | -2.8611 | -46.8186 | 2024-11-27 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c601c1d3-8df3-3d1e-9247-68301a3b9f61 | -3.9859 | -48.0843 | 2024-11-27 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 510f10cf-c3a1-3dee-8094-4983e32ac8bd | -1.6813 | -52.4333 | 2024-11-27 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 589efff5-5395-39d6-b3a7-caea2fbfeb33 | -2.6987 | -45.6705 | 2024-11-27 00:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 8123d41a-7a05-3b04-804f-11ba33e1310f | -2.5963 | -53.9771 | 2024-11-27 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5bdee05e-1b67-3073-8864-bef4b89b1fce | -1.6624 | -52.7192 | 2024-11-27 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 1d54af90-bd42-37b6-acc5-89fac29920f4 | -3.5226 | -52.1653 | 2024-11-27 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 0f87aa1c-cefb-3e4f-b780-d87541fde6cf | -3.5411 | -52.1442 | 2024-11-27 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| ebb71538-751d-30e0-8971-b7f86b152420 | -1.9376 | -45.7365 | 2024-11-27 00:40:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README8.md)
