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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a27d7e7e-30c7-3a10-898d-4da46b2718cb | -11.81519 | -55.07724 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 18a88bab-d557-3cd5-ba67-83eabefce1ae | -10.2431 | -52.23542 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5d1890ec-a1cb-316e-abaf-2bd04f893e5d | -11.81579 | -55.07266 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d0ff4159-7c05-3fb8-9459-d48cec169a7b | -11.29839 | -54.01266 | 2025-05-28 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f622c411-0b95-3bec-b661-7027c4e387f8 | -10.6598 | -49.44746 | 2025-05-28 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6aed098a-9ccf-3a70-824c-87f0ff8ed373 | -2.5352 | -53.95718 | 2025-05-28 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8587b5b-a70c-3619-9251-01d8e4f083ed | -11.1399 | -53.91885 | 2025-05-28 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a4d22a0-32ef-3229-845f-c0ab919ea2d1 | -12.4081 | -49.99806 | 2025-05-28 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8effbf92-20d1-33fa-80bd-f658c798a76a | -12.40474 | -50.00303 | 2025-05-28 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7e198d9-7dd5-3c10-a209-358c040f3825 | -12.41106 | -50.00401 | 2025-05-28 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 032f824e-98ae-3ac5-a965-3aba5059effa | -10.23818 | -52.2313 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6204c484-02a0-38bb-9fed-492b51485d02 | -11.39898 | -52.94685 | 2025-05-28 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5407ae5-3a6c-3a90-b7a3-53d535267152 | -2.95592 | -60.01396 | 2025-05-28 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe6fa5a6-b1b4-320c-ae22-845c947f3a6d | -10.73666 | -49.29228 | 2025-05-28 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e86d068-db55-3dc0-856c-e48a81d18ac7 | -11.97835 | -52.46691 | 2025-05-28 05:23:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8f59ef6-f03b-3a30-8536-e0864c8ef734 | -10.23244 | -52.23384 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19677743-04a4-32e7-af78-4b27068eaf89 | -10.53912 | -59.22469 | 2025-05-28 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b0a8780-8a61-3778-945a-243b76334b55 | -12.40755 | -50.00317 | 2025-05-28 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 643dba98-08ad-321d-8703-8021dd514a47 | -9.18352 | -62.45644 | 2025-05-28 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0929d8b8-6e2c-36e2-9597-9f05f268d9fe | -10.66487 | -49.44577 | 2025-05-28 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2f4639e-e31c-3b4c-9b3f-8f2afb2f9318 | -12.40533 | -49.99796 | 2025-05-28 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c4d21bb-d747-3491-926b-298bb73d17e4 | -11.82028 | -55.07332 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8dda5907-1e0c-313e-a6ab-a19480e42a49 | -11.97748 | -52.47387 | 2025-05-28 05:23:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96b79918-bfe8-311a-b7d2-aa1390d55bc0 | -9.19657 | -49.47362 | 2025-05-28 05:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fcb2911e-c706-38ad-ac6e-126125b2d103 | -9.15358 | -49.64998 | 2025-05-28 05:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1cd48b80-ed2c-3c76-999b-cc3016dab2b7 | -9.04041 | -47.75063 | 2025-05-28 05:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ffbec65-c234-3d0c-a579-233662cee434 | -9.042 | -47.74517 | 2025-05-28 05:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 04a27600-d15c-335d-8344-e7d9b8c62327 | -9.04119 | -47.7438 | 2025-05-28 05:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e00fee54-c3e3-3814-a126-c0a468c840c9 | -13.48794 | -52.95824 | 2025-05-28 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d44805dc-8d94-343b-acab-5d8f052270dd | -9.04118 | -47.75198 | 2025-05-28 05:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ae9bf6a6-0166-3377-87b9-3938267080fc | -8.73129 | -47.99231 | 2025-05-28 05:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59175ae4-e3e2-3f8b-ac47-f0f764292e7f | -13.49325 | -52.959 | 2025-05-28 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0780a3d-28d2-3a6f-91aa-5a130cb00ae1 | -9.20033 | -49.47428 | 2025-05-28 05:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aedabcae-f78d-3d75-8ac7-fd468cd05807 | -18.85739 | -53.62457 | 2025-05-28 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6241e80b-ca90-3023-8bf5-c84f8aded5ed | -9.15485 | -49.64998 | 2025-05-28 05:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a34e648-8125-3eb3-b478-9399d9a8a195 | -18.85775 | -53.62111 | 2025-05-28 05:25:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbc09669-2dda-38d1-96a1-a17481dd247b | -8.01862 | -49.6873 | 2025-05-28 05:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9d3019a1-971d-3a50-bbb6-1f6dff502cf2 | -21.5228 | -49.86205 | 2025-05-28 05:27:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d205fbca-4f83-3058-9a6b-26998834b212 | -11.818 | -44.2703 | 2025-05-28 05:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2139eb9b-2a08-3e23-96ed-e3bdf9e9bc94 | -7.6762 | -46.0995 | 2025-05-28 05:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b273a87b-8681-3a36-bc3d-0018b1bd4e70 | -7.6762 | -46.0995 | 2025-05-28 05:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| faeceb1f-63a5-3a20-a343-8085dece8ac3 | -11.818 | -44.2703 | 2025-05-28 05:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 63a97a0c-da00-344e-bcee-55f2ffacf8a4 | -6.11871 | -43.94187 | 2025-05-28 05:40:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5167e121-2254-3ef4-a52f-631dd74c075d | -6.32129 | -43.37558 | 2025-05-28 05:40:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3fb50cca-af1c-359e-8836-1d9f3fb11d62 | -6.21487 | -43.34338 | 2025-05-28 05:40:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 220f00f8-b434-3925-a45e-2a408b098f1e | -6.11729 | -43.95162 | 2025-05-28 05:40:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dc335890-fa52-397f-8628-d42290ba3f6e | -6.20537 | -43.34195 | 2025-05-28 05:40:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 28d929f1-b888-3f85-97cd-0039975da9a9 | -6.21337 | -43.35379 | 2025-05-28 05:40:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 10479606-c011-3c8e-8b6f-bbda5ab3b742 | -6.20388 | -43.35235 | 2025-05-28 05:40:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b6480a35-9699-354d-8da2-59042c8f7bd4 | -7.62325 | -45.75711 | 2025-05-28 05:42:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0c549b58-3eaa-32e7-bb5e-249cc9bb57eb | -7.67592 | -46.08619 | 2025-05-28 05:42:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 53f089e4-1072-3252-9707-11eca9b5b4cd | -7.68339 | -46.09631 | 2025-05-28 05:42:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| ad09892e-0856-3f21-a4a7-5670554c6ba4 | -7.19027 | -43.10774 | 2025-05-28 05:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 264ec31e-bb24-3001-a573-e8820a5975ac | -7.67327 | -46.10381 | 2025-05-28 05:42:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a9e11cfd-a0ef-3dae-bc68-f948d561a945 | -7.6746 | -46.095 | 2025-05-28 05:42:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9d19d0dc-cb81-350f-972a-c39cf6a88daf | -11.81545 | -44.27213 | 2025-05-28 05:42:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| b2b6f891-0a63-34ab-a64d-3615664fe87f | -7.66448 | -46.10251 | 2025-05-28 05:42:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a638a963-cc8b-3b44-a3f7-bef8ec1b5909 | -7.6104 | -43.38752 | 2025-05-28 05:42:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3d03d50e-aeb3-34fa-b5b9-4a6bbf74d4fa | -11.81698 | -44.26123 | 2025-05-28 05:42:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e6aa3945-9dfd-369b-86d7-08be37104e9c | -10.45298 | -47.93855 | 2025-05-28 05:42:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a3c40989-30a2-3e48-bd26-d79ec70d1bae | -10.23034 | -52.23211 | 2025-05-28 05:42:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 15be7f18-dbbf-3701-9723-b4616fc55800 | -9.19797 | -49.47283 | 2025-05-28 05:42:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ff4f56b0-9cdd-31bb-b75a-a170a497b14f | -10.45156 | -47.94776 | 2025-05-28 05:42:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 99b40274-433e-3a60-b61a-f0ebe2ca02b8 | -7.08186 | -46.05091 | 2025-05-28 05:42:00 | AQUA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ff203ed3-bff4-396c-95cd-be14eef655e7 | -9.04084 | -47.75032 | 2025-05-28 05:42:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 189aef02-277c-3ffa-b765-2cd6f24797a2 | -11.39682 | -44.82785 | 2025-05-28 05:42:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b5c4a9b0-b652-3621-8d5f-47f4b7336c9e | -7.6658 | -46.0937 | 2025-05-28 05:42:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 23e8f98f-22f4-3432-bef1-6d0586503980 | -10.47088 | -47.94127 | 2025-05-28 05:42:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9705b350-3390-300f-8c62-0b96f70b3a88 | -23.26225 | -49.4916 | 2025-05-28 05:44:00 | AQUA_M-M | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| ef7ea50e-9c11-3807-b905-2d1f7dcf8c60 | -11.818 | -44.2703 | 2025-05-28 05:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 50039d73-bd68-381d-8fa1-a054c5742482 | -7.6762 | -46.0995 | 2025-05-28 05:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 24122971-a86a-3227-a300-23d990dddc88 | -11.81343 | -55.0742 | 2025-05-28 05:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4512d94-7a50-34f1-b431-5f11d273d040 | -11.81283 | -55.07817 | 2025-05-28 05:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 620adfdc-75eb-3a50-9710-e99c503eb80e | -11.81276 | -55.0804 | 2025-05-28 05:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53da4427-70b4-31eb-98b0-140daf0aec16 | -11.80602 | -55.07709 | 2025-05-28 05:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3d40790-29a8-396b-a4df-b02155fd70ed | -12.10889 | -54.66584 | 2025-05-28 05:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aae7aae3-dcd1-3afe-9353-966b2995ecfd | -11.81355 | -55.07198 | 2025-05-28 05:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30b10f3a-0eae-3605-98e3-bc84f111b3b9 | -11.82026 | -55.07517 | 2025-05-28 05:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d7adaf0-2fbd-3347-82cc-9258fb2c1e54 | -12.11593 | -54.66664 | 2025-05-28 05:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 819e2fb1-bd59-3452-9658-7954890f6a72 | -7.6762 | -46.0995 | 2025-05-28 06:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4ae6207d-9eee-36a5-8d77-f3996525ed3b | -11.818 | -44.2703 | 2025-05-28 06:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| eefc28e1-9059-3d6f-a66f-f9f0e850acb2 | -11.818 | -44.2703 | 2025-05-28 06:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| ace7f7e1-bad5-3241-a534-ebf22b9959e8 | -7.6762 | -46.0995 | 2025-05-28 06:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9c316e7f-6643-38b2-b60f-301d3afdda1f | -7.6762 | -46.0995 | 2025-05-28 06:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 839b0c2a-2b0b-3ddd-9ab1-e44122e42c46 | -11.818 | -44.2703 | 2025-05-28 06:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3ebee09d-9290-3b29-9399-2572bf398a2d | -11.818 | -44.2703 | 2025-05-28 06:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d1fd8c1c-5c0c-3909-8cf3-5b02505f1d15 | -7.6762 | -46.0995 | 2025-05-28 06:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 7d8b916e-7109-3e97-9df6-45669206c498 | -7.6762 | -46.0995 | 2025-05-28 06:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e99ae7d8-d696-3f7e-b5f5-e1814d36b501 | -11.818 | -44.2703 | 2025-05-28 06:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| dc7ba8cc-e930-3dae-aeb6-b6ab9a5e2a45 | -11.818 | -44.2703 | 2025-05-28 06:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 88f0269d-dcc5-31bd-81c7-6ebc0b994303 | -7.6762 | -46.0995 | 2025-05-28 06:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3aec66c3-1e15-3f62-ab9d-253c31119121 | -7.6762 | -46.0995 | 2025-05-28 07:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 4676322f-40f4-35ad-bb91-1aee4116c77a | -11.818 | -44.2703 | 2025-05-28 07:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 29da08e2-7272-37ba-812c-55b3f842f4ad | -7.6762 | -46.0995 | 2025-05-28 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 5459de69-4e80-333d-9ece-8525a64c5477 | -7.6762 | -46.0995 | 2025-05-28 07:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 47c00f97-7add-3300-b3d3-5f16cf66681a | -7.6762 | -46.0995 | 2025-05-28 07:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0509d888-da15-3a38-98de-48af5d1c9572 | -11.818 | -44.2703 | 2025-05-28 07:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e4ead7ac-a44f-350d-92c8-c345900bfcac | -7.6762 | -46.0995 | 2025-05-28 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| a8df8a2f-9c95-3915-a29a-1760cabf3643 | -7.6762 | -46.0995 | 2025-05-28 07:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 81c68b47-3fc1-3333-ba85-dda7dd1a3913 | -11.818 | -44.2703 | 2025-05-28 07:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |


[Clique aqui para ver as próximas entradas](README16.md)
