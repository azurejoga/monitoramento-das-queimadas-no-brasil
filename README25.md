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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8229b8bc-2f60-3b5b-82d7-3a2b9359a851 | -10.16602 | -44.90392 | 2025-11-14 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3b3b252-2ac9-3b47-9bf8-4bc2786cd3f1 | -10.05869 | -44.7677 | 2025-11-14 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff3a5abf-e641-330e-83e4-9bc13a4abf7a | -7.46511 | -42.57042 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31141450-8cc0-3961-9b4f-be8e40dc9bfa | -8.72946 | -48.31833 | 2025-11-14 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dc1b8d6-0cd7-38d3-aebe-c76099e52848 | -8.45849 | -45.13503 | 2025-11-14 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5809434c-5d4b-39c0-9568-b8a7b898dbd6 | -10.11009 | -40.8974 | 2025-11-14 04:23:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 3f68340a-41ab-377c-affd-b4e5373d545b | -3.47669 | -45.64935 | 2025-11-14 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6b90239-a9c7-3341-bd17-c07253a7441a | -7.35987 | -43.35242 | 2025-11-14 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c4f2372-6259-3e83-94f3-b633cfbfe438 | -3.99259 | -47.19098 | 2025-11-14 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48cd068e-8551-3d82-b311-cf1fc4bb0db1 | -7.88174 | -48.40856 | 2025-11-14 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e4c23cf-83b5-3f45-895c-d163dbfe14f8 | -3.98285 | -48.00211 | 2025-11-14 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef8f6271-c3a2-3479-9e2f-3ca27375ef8a | -2.8833 | -45.29424 | 2025-11-14 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d74b6c2-aa0d-328e-b505-f8108e1e1d8b | -3.47387 | -45.64518 | 2025-11-14 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b27c1e4-ceba-310b-87c3-fe8ef4885e7a | -10.45157 | -47.3375 | 2025-11-14 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea8214f2-aabe-3314-ad94-d52f85f27fc8 | -7.84984 | -44.2909 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cc46477-7537-344e-bdcf-612c31baa2c0 | -9.31622 | -47.83445 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b64b19c-4de3-3fd7-855f-ed66ade8f58b | -7.63331 | -46.15443 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f245077a-27ce-3774-84ab-bcfed52f6880 | -6.56745 | -48.73222 | 2025-11-14 04:23:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12123ab8-68db-3077-8f91-338219abc50a | -4.46542 | -45.82622 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| feb2a74b-d22f-3812-bec8-7f2822b7c9f1 | -7.93135 | -44.33241 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57f6c0d1-1411-32b9-a8db-612fd9d556bc | -3.01712 | -49.43288 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec60bab5-40ea-3e95-bb90-fb87c3179ab7 | -7.9288 | -44.33211 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86523edb-71af-3565-b39c-42681324c382 | -1.3396 | -54.61277 | 2025-11-14 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e72db4e7-f446-3f58-9174-82f0f5d6f354 | -2.83601 | -45.48285 | 2025-11-14 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a0d1d0f8-af18-3b45-aa13-9629a451c28c | -7.93698 | -44.36205 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2426fd4-6826-3b8b-bce3-3ac45311cae4 | 0.62194 | -50.76259 | 2025-11-14 04:23:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74df4acd-96c1-38a1-b455-1571c1ba70d0 | -3.31307 | -49.46787 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78969b50-2327-3021-9a68-8311a1c2ac26 | -8.74365 | -45.36231 | 2025-11-14 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dcb5401-da78-3892-a375-00bd2d34422d | -2.47007 | -48.22854 | 2025-11-14 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d696637-252a-3a15-8662-651824bc42e7 | -2.52326 | -47.8047 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31918283-179a-3273-b2ae-36630ae17ba5 | -7.7886 | -49.61848 | 2025-11-14 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 056bf009-4e1f-332a-8e0f-06b01c029dea | -3.70859 | -41.64273 | 2025-11-14 04:23:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c711e5c2-ebbf-3b5c-a8c0-9ee95106201f | -3.53185 | -44.84837 | 2025-11-14 04:23:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57065209-616d-3b23-b0fc-86ecfce0d7bf | -4.29169 | -41.64885 | 2025-11-14 04:23:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2c41689-5cc9-3529-91c0-e077cdd00a31 | -7.93354 | -44.31837 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96405920-dc2e-37fb-a042-c399751326bf | -7.49774 | -47.03571 | 2025-11-14 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18b5c25e-5bb8-3ec5-9da5-d8ee88e17698 | -4.46126 | -43.62135 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dafdd6a-5eb7-3c70-a231-21b346848db4 | -3.42572 | -50.16844 | 2025-11-14 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d041b456-6017-3bb0-bbce-36b9dda9f0aa | -1.34636 | -54.60958 | 2025-11-14 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ce73db7-8c91-3a58-9273-274a6e7c16ee | -3.10747 | -45.40282 | 2025-11-14 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b866853-27eb-3b5c-a133-03633afd67af | -9.85464 | -47.61149 | 2025-11-14 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b9d630e-82cd-311d-b164-a6bfb47534c0 | -7.54257 | -45.85231 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c6fa6957-8be4-3421-b4c6-94e28203646f | -7.9277 | -44.33912 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e0c036f-bd6f-3509-b0fe-37e14fd17bb0 | -7.85263 | -44.29494 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3611e7d8-17c8-35e9-9b6c-a73985656820 | -4.7163 | -42.9379 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 55c0c76f-b459-3245-af17-f8ce50f17b77 | -6.72361 | -47.43553 | 2025-11-14 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 545bde46-2a4b-31f9-940d-9efd5f522a40 | -8.53565 | -49.58309 | 2025-11-14 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fce55c2-5f5b-3e79-bd49-004580a8bbf4 | -3.47784 | -45.64209 | 2025-11-14 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 393f6dad-7bae-3156-8650-9311f08dc161 | -9.9143 | -47.86292 | 2025-11-14 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6509c24f-df3b-39e5-b644-0f67b606b106 | -7.85487 | -44.30249 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c825cfa6-8369-315c-8665-0c93d5ca6380 | -7.8365 | -44.2888 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cd94d29-2380-3850-9024-32d96024f0bf | -10.17529 | -44.77858 | 2025-11-14 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78e86cab-5d1f-3393-8cb9-688c5200f536 | -3.01231 | -49.43601 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41fd0fb2-6514-3d01-b803-caf3d27b3d11 | -2.75066 | -49.52931 | 2025-11-14 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23d45b1c-4431-341d-a0aa-440cd7b0530b | -2.45293 | -48.82098 | 2025-11-14 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a39c5fdd-5735-374e-8d80-9a9fdfc136ef | -7.01516 | -46.39579 | 2025-11-14 04:23:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e843e3a8-a080-315d-ac25-b7ea0b4e775c | -7.72836 | -47.18963 | 2025-11-14 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cc6364e-8093-343c-ad7c-d04e357674ab | -7.77956 | -43.79371 | 2025-11-14 04:23:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bd6331fb-23c3-3eba-b6f5-0eba02c73f17 | -2.96043 | -48.58768 | 2025-11-14 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86d49fa3-bb4d-3d12-aaac-002b730e4fce | -7.7249 | -47.18906 | 2025-11-14 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c3bebaf-cf5c-31b1-af32-d6d7869791dd | -7.46044 | -42.57764 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 568c59b2-73a4-32fe-a028-d194c4158983 | -2.84281 | -45.48392 | 2025-11-14 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf9a554-9c30-3292-ba2d-d6a564ca774f | -3.48009 | -45.64988 | 2025-11-14 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fa391fe-cd31-3fdd-9a92-fd044a46a589 | -3.36615 | -48.4056 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77a992b7-5deb-38a0-ad2e-a0d2ecaa4249 | -7.88313 | -44.87916 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db524e29-fb1b-3567-a30a-494fb3ff81f4 | -4.6098 | -43.38659 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12fbd781-f1d2-3f0e-bf0a-23f6f9acb9b9 | -3.80781 | -45.03585 | 2025-11-14 04:23:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce560dfc-47e6-3f93-87e5-ae166939d1e6 | -4.60809 | -43.35393 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e779ffa-f09c-36f1-a941-a57b28cd2985 | -9.91366 | -47.86679 | 2025-11-14 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f7a53f3-dff3-329b-9e1e-012f398b9d01 | -9.31556 | -47.83835 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7be1cc73-e417-393f-820e-1688c8bb7080 | -3.82039 | -45.2909 | 2025-11-14 04:23:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae3338c8-df4c-3121-8684-54f422aa7fac | -7.8198 | -41.79295 | 2025-11-14 04:23:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4de239a6-3577-3950-8c0d-d69b180bc416 | -4.02592 | -43.1125 | 2025-11-14 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0767f612-a1c3-37df-b3ee-679b1a6e2bd7 | -7.08348 | -46.12146 | 2025-11-14 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b055e229-3d90-3c3a-a196-c5cc5bd596a0 | -8.90133 | -47.89508 | 2025-11-14 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45fb3174-5b0c-3b5d-9f5b-796ec871bcb0 | -7.88657 | -44.31826 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12b98a5a-6271-3239-a97f-d66d359cb592 | -4.09362 | -45.94445 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca49bd07-9f48-3d4b-8d51-1c441b5836f9 | -3.98305 | -47.99961 | 2025-11-14 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6d54770-2b55-348f-999d-9a0d26eb47cd | -3.31239 | -49.15705 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85273387-6b05-31fc-b251-3b10a94f9a89 | -9.44061 | -44.87261 | 2025-11-14 04:23:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77c9321a-2ba9-3bea-8fd5-3eda2acf3a47 | -8.90828 | -41.07562 | 2025-11-14 04:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1aaa1e6b-e719-3e13-9864-c7f878dde6ef | -4.12815 | -43.0088 | 2025-11-14 04:23:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f2c7d37-47c4-32ec-9e30-747e51ea3305 | -9.8182 | -48.35468 | 2025-11-14 04:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec947e20-fa69-3d4d-9fa4-bcfdced459c6 | -3.57438 | -41.72136 | 2025-11-14 04:23:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f4eada13-29fc-3022-a41a-f7f2e901ebf3 | -3.31404 | -42.39189 | 2025-11-14 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 815ec783-3573-3c84-8a1e-6153fa758cec | -7.09473 | -45.45641 | 2025-11-14 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4d2da2b-cb8f-3d2a-acbb-bd69e6514069 | -7.70909 | -42.33701 | 2025-11-14 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c2b905e-20cc-33b0-a287-d4b613deda61 | -3.86716 | -42.76388 | 2025-11-14 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62905527-c99a-34eb-b0cc-b58758fdd04f | -10.32251 | -44.28141 | 2025-11-14 04:23:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d398d5b3-632f-372b-b799-83ef7d204180 | -7.46337 | -42.55824 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c6e97adc-2b59-3085-9dda-143f825b90da | -2.52251 | -47.80927 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc9ac6a0-bf68-3ff5-b221-25cfe008c01e | -7.83984 | -44.28933 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b46cb522-47cf-3fa5-8518-883037bb8353 | -2.11784 | -45.36364 | 2025-11-14 04:23:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 914443d6-59df-33dd-82c9-f65d48499322 | -3.24493 | -48.88089 | 2025-11-14 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0e21b6c-42cd-3fe9-ace5-d59243fb7e63 | -7.49499 | -47.33438 | 2025-11-14 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0a8bb01-0103-307d-b3fc-58f439bd2289 | -10.80231 | -44.8555 | 2025-11-14 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdf599cb-c369-3457-8f89-3e12442cdf1b | -7.28938 | -45.46585 | 2025-11-14 04:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36bb6b2a-429b-3584-b841-3df9cb71fed4 | -7.45928 | -42.58532 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bce68bd8-ffcc-3782-a927-e79ca9be2920 | -7.44823 | -42.56386 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63aed256-4ba3-3871-a7b7-b3f0f304c5cd | -8.96642 | -45.11262 | 2025-11-14 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README26.md)
