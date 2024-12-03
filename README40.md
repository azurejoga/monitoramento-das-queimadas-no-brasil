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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea2beed0-80c9-3986-afef-e755a0e381e8 | -2.40871 | -46.48032 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9daaabc2-2350-3169-91d8-da3392214e26 | -2.93263 | -49.84109 | 2024-12-03 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd311a8c-bc69-305f-bfd1-11f147aae540 | -3.86287 | -50.89662 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 949bc23d-1933-357b-baba-87d17fa26d85 | -3.2566 | -53.66619 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6fb918ba-1329-3479-a7b7-281810985b0a | -2.34174 | -53.80054 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb8ba1f4-bf00-3884-9924-33fa1a25214e | -3.32977 | -46.4328 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a785940e-59a4-33a9-a94a-63a87e494c73 | -3.264 | -53.64902 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a0ca219-3f3a-376a-a2a4-a0af89fd8472 | -4.14207 | -48.2209 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6164605-a88f-3e3c-8954-f9eabf4c4e07 | -1.89974 | -52.85577 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaba77a1-5435-3908-a8be-3f0ebf060478 | -2.57566 | -46.41096 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19e1873e-9d9b-3530-821f-3e13975f9bcf | -2.59933 | -47.03845 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5c856c9-6687-3c5b-bca0-fa1b279c5c14 | -6.02348 | -46.24615 | 2024-12-03 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fcfa916-c399-3c6e-b5cc-1502a36e3a1b | -3.34813 | -51.21096 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb7c597a-d1df-3f03-9a64-f03e57971fa6 | -2.6643 | -46.12721 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 797afe1c-4015-3b2d-8001-4e036be61306 | -5.44215 | -45.58381 | 2024-12-03 04:29:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1311b8b7-0e73-3f77-96f3-0a646f16b5f7 | -2.79752 | -53.05139 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cbaac9e-cbbb-36c0-aadb-2452fab0e9a9 | -1.10583 | -54.18759 | 2024-12-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04ce7726-e329-3915-97c7-72d1b5d6fe1a | -3.19088 | -46.58142 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8174f571-d371-3a37-8509-20d7ed20ccc8 | -3.19419 | -46.58193 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62763878-e6a3-3511-bcf4-e73d1178ed46 | -3.89834 | -45.01333 | 2024-12-03 04:29:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f9de795-42f2-3540-819b-094b645fd3e7 | -5.65112 | -44.32774 | 2024-12-03 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a4cd58c-5bf1-384d-b3ac-e038d0c57771 | -3.76746 | -46.69585 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 973e3242-864b-3864-9669-f46747da4ec1 | -4.07769 | -46.68786 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37264843-1d6f-36a4-86ed-901b35b21400 | -3.23538 | -53.38023 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 214fdabe-20d0-300c-a7d3-ee77993b25c1 | -2.6854 | -46.14471 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c18ea0-c236-34d8-b7d6-df2c80a75a95 | -2.72571 | -45.20945 | 2024-12-03 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49273635-fb80-3094-9c49-2c7064cb8394 | -3.07093 | -51.26768 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec5729e2-8f5f-3dc3-821c-cd35238e8f3c | -4.40342 | -49.77083 | 2024-12-03 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c73e678-346a-3f97-a8a8-d948c3fc674b | -3.79834 | -46.6936 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ddcf711-b9af-3c48-8cb4-00931e8c6bc3 | -2.60605 | -46.21743 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aad6139a-30ce-3e49-9527-f9e5f4f26944 | -3.18143 | -46.55521 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15187145-157d-35ef-951a-2c5dcd538206 | -3.11635 | -45.9931 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5afeaeb2-c179-3a72-8e1b-36a634b859e1 | -4.82536 | -43.43303 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3aff19de-7835-3faf-a3ec-ba9db3a3aba3 | -5.14248 | -45.9579 | 2024-12-03 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7f2a20c-dba2-3a6e-a07e-20efed8d71b8 | -3.29819 | -50.27729 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bd693fe-086a-3467-acd7-e3b1b2ef2327 | -3.39913 | -50.23233 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8160b143-fa8c-3042-88d0-c440bdffb9c8 | -2.65231 | -46.11791 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3fd4f76-8a6a-3b33-bbd2-9e69f2743edf | -4.00501 | -49.97219 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1da40320-bc48-3ebe-b669-5409553cb811 | -2.14822 | -50.69427 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6150f415-eaf6-3cbc-9539-e66ffb5194b8 | -3.82736 | -46.61663 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b010568-e462-3d6e-bc58-1bcaea029055 | -3.08283 | -53.37654 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 71b6658f-41c4-39fd-af20-b6c758a1d9b0 | -3.94779 | -49.96774 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d97b08d8-914e-31ef-931f-459bdffefdd1 | -6.02685 | -46.24669 | 2024-12-03 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd0ec292-0b67-3f25-a8c7-b58902508340 | -4.31029 | -48.22967 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b47785f-6664-3f6c-a905-1a6cf1deb388 | -3.77077 | -46.69638 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 922f835c-fde2-34dc-89cb-a7b29a4c1688 | -4.18936 | -51.18579 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9a2f2d55-b57f-3946-921f-220402946df9 | -3.85249 | -46.52119 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44ad174e-f90b-3f10-a200-cc2f73e9c064 | -3.55548 | -50.17469 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 34be15f7-bf88-3682-ae2c-3255c6855ea7 | -1.88317 | -53.29588 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4d7530b-ea69-3e1d-a6c2-5874629615dd | -5.53326 | -46.45944 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23475e54-e235-3de9-b7a2-f7f078248477 | -2.72042 | -46.20347 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7d48687-b5b9-36c3-81db-cc1e7108d595 | -3.01651 | -54.03888 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8ba039c-d0b6-3305-86d4-d6acd993b3bd | -2.72672 | -46.2932 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1c77d46-da43-3ad3-b6d4-b41561f5d642 | -4.07823 | -46.68439 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc4ed1c1-53be-3eec-8b94-06739020c55b | -3.12103 | -53.11409 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d529aefb-3c05-3ace-ab5f-6056acc0d0c7 | -3.1596 | -46.62954 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d55c93ab-9475-38ac-8f2a-619688205165 | -2.56161 | -46.3275 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 850e02d6-0c18-3df6-b735-b6f3311efb3c | -2.79318 | -53.05069 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1672f969-bd15-38a8-a4a3-35b20c6d4cc1 | -3.24836 | -53.66021 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| df82f606-ff56-3f3e-9991-0fc15aa5ab21 | -4.06369 | -46.82013 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 047cfe9c-0f33-3a39-8010-edebc49ef68e | -3.09549 | -54.29891 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bddaaf5-4255-3c14-9946-3d876e5590a0 | -2.82529 | -52.58918 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cfe861be-70f0-368f-b009-92af003078d0 | -7.62243 | -47.84372 | 2024-12-03 04:29:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b083ce95-bcc5-3d20-a24b-fc59b671dbd3 | -3.26431 | -45.37299 | 2024-12-03 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ace2e49-bb17-3e1d-9199-2a87401181d4 | -2.76408 | -54.12486 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc11292b-aaae-39de-819b-b2007149cd3f | -2.57999 | -51.92386 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ed94059-e319-391e-9c95-0e2a85cee772 | -2.20837 | -53.7812 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4a41a639-e0b5-3f52-a3f4-c4ba7949fb5d | -8.14046 | -44.46655 | 2024-12-03 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 746379e5-a7b7-3fd2-b90c-122538008988 | -4.31252 | -48.21564 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 859de29c-4368-314f-bc43-4a6a73bf509a | -2.565 | -53.40331 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 350722b3-f78e-3055-b1ce-d909e8f206aa | -2.9773 | -53.90913 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c67d4d3-db60-3bad-9f5d-c5109f11d809 | -5.19455 | -43.73451 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9392f73d-e3e8-3ded-a9d0-67873f8da053 | -3.2509 | -53.93205 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0079cee6-88ce-370e-8e57-cfee9b67c870 | -3.64557 | -52.63228 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e5dcf64-02ff-35be-a7c9-878db6867ecd | -3.32965 | -53.54515 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e408f1d6-4e6d-3615-8f93-e52d1a6f5816 | -7.28164 | -46.19154 | 2024-12-03 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ebfe4af-a6cf-3134-9b16-cd038a3f6fd5 | -4.89946 | -47.14559 | 2024-12-03 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ac8bd1ef-17a0-3bf6-9892-acfe0877bf11 | -3.92183 | -47.09788 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dec26d56-6918-36a9-9da8-051f7ef44adc | -3.03604 | -51.3604 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41bfc026-8bdd-3deb-aeee-ed9fe6fc0a20 | -3.17585 | -54.33909 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 95101ea5-d85e-34b7-b1ce-450027642b2c | -4.55871 | -45.72132 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 862d0dee-4cdc-3407-a706-71b432d96a70 | -2.50015 | -46.24353 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57b747ce-ac8a-365c-9432-7190f0ad219f | -4.11242 | -48.53876 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6cabc22-b27e-38e5-a57c-8d327b7afeef | -3.22892 | -51.72985 | 2024-12-03 04:29:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dd6f3a0c-f67b-35cd-abc6-bb731c9d7db3 | -4.00066 | -46.94097 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 275b744d-f221-3bb1-9b72-df2cf1020a8d | -3.70106 | -47.11934 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f87df8a-a0ef-3956-8c12-3eba49f9adaa | -2.7727 | -45.22043 | 2024-12-03 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9eb19eb-cee1-3baf-8f16-a8125949c48d | -3.2549 | -53.62024 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1646ff73-3632-3183-884e-a7168845c09f | -3.33493 | -53.37909 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b72d506-102a-3175-b361-b45e76640b66 | -1.94723 | -53.3414 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 215217ba-65a0-36b2-8be1-73aef6475220 | -1.7503 | -52.80706 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4c6f8e6-8f21-379b-a6ec-cfce0e074c56 | -2.75212 | -55.33784 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97d252ac-e86c-3074-bcae-23535e36f852 | -3.25186 | -54.21054 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c20f9747-2ac5-3b5d-be02-b50bf69ee1cf | -4.52881 | -45.73521 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8e74e54-5ad9-3f97-a6e6-3047f2fffa43 | -4.56583 | -46.62915 | 2024-12-03 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aeabeabc-f192-3432-a730-9b6e44e32929 | -4.03534 | -46.93579 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab15ec81-9758-3ec5-81d1-d8cc7b62a654 | -4.39461 | -46.0091 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 346f9f05-6ed0-3143-bfe1-ca89701ae81b | -3.05674 | -54.50086 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1968f483-de88-3f39-8ba2-83621db0eb53 | -3.52013 | -45.01076 | 2024-12-03 04:29:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fdf2ef3-9cc4-3f98-ac93-e49a2c787ab6 | -3.08677 | -47.95479 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README41.md)
