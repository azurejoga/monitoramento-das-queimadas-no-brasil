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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a11295a2-6ca8-3db1-9740-ddaf0dca09a3 | -2.54255 | -47.10424 | 2024-11-19 00:45:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 11ff455a-be83-34e6-8472-899d149421a1 | -2.98638 | -45.34057 | 2024-11-19 00:45:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0475e46a-b288-313d-91fc-fa8504f7a4b2 | -3.18043 | -44.30733 | 2024-11-19 00:45:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d6b34923-03fd-34d9-b609-e5b89379aa33 | -2.32083 | -45.65357 | 2024-11-19 00:45:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7ab42e1d-f6dd-36f6-89d0-f29ec944f897 | -2.99746 | -45.16096 | 2024-11-19 00:45:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f3075f8e-01e3-3d09-b270-2fd49f364065 | -4.37731 | -50.49975 | 2024-11-19 00:45:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7f21cb27-f477-356c-b447-60a2977ef19e | -3.57661 | -50.25857 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9e79ac5a-2264-3f2b-8bb6-1bc1254145ca | -2.96578 | -49.16506 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9889f9c8-0ce4-38de-98f7-0c748245e8de | -3.54479 | -50.41434 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 4f2b5939-06d1-39e5-af87-f616554e21e5 | -2.94343 | -48.07502 | 2024-11-19 00:45:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6d8cee6e-8e8f-396a-946f-98bd16281534 | -4.88248 | -42.98004 | 2024-11-19 00:45:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2fb69523-6631-3f49-bc81-ebef27c1d02c | -3.56853 | -51.45319 | 2024-11-19 00:45:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 95a56207-08c8-3c0d-b9d4-e8d56ed783dd | -2.48739 | -49.0337 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 078f47c8-02c3-3bc9-ba51-c9ebc0bfee28 | -3.20881 | -52.44028 | 2024-11-19 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 56f560ce-7efc-310e-95ce-7516e6c0d9d7 | -5.5092 | -46.44836 | 2024-11-19 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 99cf10ca-1286-3c70-861d-a84538abb686 | -2.68154 | -46.18483 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 775a02de-3028-3d0c-958b-3a474ee67b44 | -3.05032 | -49.46892 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1afe2b46-14ef-3663-8359-e44b89fbbbc2 | -2.68652 | -46.22036 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5c3b972d-057f-33e3-ab1d-f5e9a81f6458 | -3.36805 | -50.82618 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 080d9c8e-9d3f-31db-9376-563784553a2d | -3.48304 | -48.24594 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| f4b09b42-bad8-3021-aa09-36626d675cc6 | -4.48679 | -46.72017 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8dcd29dd-3f7b-33ef-9c8e-794088e52ff9 | -2.66557 | -51.72961 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9f8757cf-5393-3654-9f2a-e55f88dd3370 | -2.84279 | -46.67837 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 419e00f2-ab67-3c19-b085-b5955bc25500 | -3.34461 | -50.49874 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b34a9b24-e12f-3f91-a326-a7b63c050e97 | -4.37551 | -50.48675 | 2024-11-19 00:45:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2a0bb2d8-e50a-3178-9ce1-61c8d05fae13 | -2.677 | -46.2276 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 36f2f568-c5dc-30a1-b06d-633971f13797 | -2.49541 | -49.02237 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 93004d18-d4fc-37b7-a0cc-2ac69d3325fa | -3.29772 | -45.3284 | 2024-11-19 00:45:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ba8a3df8-a601-30f2-98f8-0465f12b30df | -3.08108 | -45.42456 | 2024-11-19 00:45:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c9ffa61b-194c-3a17-acae-722e1b098c18 | -1.99442 | -45.5583 | 2024-11-19 00:45:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 84658256-d7e9-38a5-87f5-def836ed2ad7 | -3.38829 | -52.79447 | 2024-11-19 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 7ffdb0c1-d9fa-3d59-a840-a9dd8d0db3c8 | -2.8304 | -46.66843 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a1002b99-bf57-3793-85d5-ef56a4cb2081 | -2.88037 | -46.75385 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 72057cb3-aef1-3961-aa82-0bc59c2650f1 | -3.03865 | -49.4768 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0d7969ff-fb8a-3b37-a41d-8a23ff0fc1b6 | -3.24996 | -50.40283 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| eda3543a-592d-3f56-a1e0-46d4ac856ac8 | -3.03915 | -49.45952 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| bb10469d-11ce-3f4f-bd74-9c0cd053d277 | -2.72143 | -51.80966 | 2024-11-19 00:45:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 988692bf-e30b-34b4-be2e-1134894944e3 | -3.47388 | -48.24721 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3370f383-a6a3-3be5-bcbd-e758d834a3ff | -2.31701 | -45.62606 | 2024-11-19 00:45:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 49643b10-1d73-3f8f-8a32-112dc1fad77b | -2.33308 | -45.67359 | 2024-11-19 00:45:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b2f4a6c3-1681-3ff1-bbb6-5109477bda17 | -3.27794 | -50.52677 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c36aa997-01b7-342c-8b8c-7a7c7cb24a72 | -5.58643 | -46.34082 | 2024-11-19 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f3535ba-f0d4-3408-8a8d-2c21a1744869 | -3.85193 | -46.6485 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e33b6c8-1ba7-3941-a87f-494ace106510 | -2.72119 | -46.07928 | 2024-11-19 00:45:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| baaafa11-51e3-374e-9fee-0c8e0bf7c027 | -3.48435 | -48.25541 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 75d6dbd9-3957-3570-a33d-5912e19aafe2 | 2.58708 | -50.85084 | 2024-11-19 00:47:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e155f663-c8ef-3b29-a2f1-dc0defb9b791 | -1.30499 | -52.25161 | 2024-11-19 00:47:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2f407953-f402-3322-b581-d8902ae0d7c5 | -2.58562 | -51.73154 | 2024-11-19 00:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 069e6a3e-3082-3656-87a8-25bd82c98bbc | -1.70019 | -52.13448 | 2024-11-19 00:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2a91591a-f383-3758-80f8-a10b4aae4076 | -2.59491 | -51.71486 | 2024-11-19 00:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0cce3987-74d0-39de-a4c2-3e3b2c7c5b01 | -1.76831 | -46.31749 | 2024-11-19 00:47:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| da5466f7-cc2d-389d-ba32-681f71fe3ff4 | -0.28524 | -51.54778 | 2024-11-19 00:47:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f051250c-6eab-3f5a-8f69-5603eb476e5a | -1.24192 | -52.05446 | 2024-11-19 00:47:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a6072a53-7b3e-390a-a6e8-42743ddb5439 | -1.70991 | -47.07916 | 2024-11-19 00:47:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d0ae2db-08ed-3c1c-91d3-d73bab83a7c3 | -2.14215 | -48.94818 | 2024-11-19 00:47:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b41e5f2c-6d50-3d02-8c45-71108d528280 | -0.25319 | -48.53181 | 2024-11-19 00:47:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 082d2817-b2e9-3025-8617-e390c802a185 | 0.33734 | -50.41302 | 2024-11-19 00:47:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2067844b-ef6a-3645-82fb-6d36cbeeeed6 | -2.7462 | -54.06911 | 2024-11-19 00:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 896474e3-8f2d-3016-9d79-5b29e4469daf | -2.76039 | -52.60355 | 2024-11-19 00:47:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fa3d7e5d-a26f-3ded-b74f-96c2406005ea | -1.41853 | -52.43752 | 2024-11-19 00:47:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 2a18ae9e-ae67-31d5-a427-195f886c5f4d | -2.15304 | -50.91133 | 2024-11-19 00:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8deeee8a-b233-34e4-97ee-18614fdaacfb | -2.77273 | -52.60233 | 2024-11-19 00:47:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 257.4 |
| 2665433e-cb05-3cb3-8c13-4f9b05104397 | -0.99976 | -48.00174 | 2024-11-19 00:47:00 | TERRA_M-M | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bcb1b7f5-97ef-345d-9c19-de4f6bf37963 | -1.69954 | -45.82176 | 2024-11-19 00:47:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 36244918-6aad-3e8f-ac99-d689ccc0103c | -1.38334 | -47.44593 | 2024-11-19 00:47:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5ab773ed-1205-3cd6-bfdd-e877f764d686 | -0.84558 | -48.75321 | 2024-11-19 00:47:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db841002-704c-3678-b92a-d9a441ff382c | -1.3012 | -52.24655 | 2024-11-19 00:47:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7ac48f6e-a6a7-3f50-bbbf-0cdde1379c3d | -2.75426 | -54.07459 | 2024-11-19 00:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d64ca7f5-9db5-3207-b5ed-cf8a8e5172bc | -2.2869 | -53.64182 | 2024-11-19 00:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 8fb84340-0157-32c8-af30-445b6ac0f112 | -0.25192 | -48.52263 | 2024-11-19 00:47:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 69036348-bd7c-39b8-8199-87c42eca6176 | -1.36771 | -47.26837 | 2024-11-19 00:47:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a906a95d-4089-3bb1-a76d-181e0ad31cbc | -1.70237 | -52.15035 | 2024-11-19 00:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 73d42cf3-a106-3c0c-8aba-722c9630f08c | -2.6055 | -51.79087 | 2024-11-19 00:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 49a02847-3858-3262-9602-b091d56e54de | -0.28998 | -51.55515 | 2024-11-19 00:47:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3ce4a943-0093-317f-839f-376417194f02 | -2.8504 | -54.00754 | 2024-11-19 00:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 62e5c57a-d4a3-361b-bc13-31c6178cbc58 | -0.88918 | -47.86858 | 2024-11-19 00:47:00 | TERRA_M-M | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3daac55a-efe4-3167-9e95-5c1ce5395b85 | -1.15693 | -46.75398 | 2024-11-19 00:47:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6345fbdc-f5cb-3e92-b609-3b5f2e7db9c2 | -0.12157 | -51.42772 | 2024-11-19 00:47:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 054ecb51-1eb5-3e0c-8a59-631e8fbb9a63 | -2.02433 | -52.08154 | 2024-11-19 00:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| fd8d260f-cb7b-3c5d-9108-6939e1ca3c59 | -1.83751 | -46.28362 | 2024-11-19 00:47:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d8915cea-28bc-3bdc-b92c-c956b765345e | -1.21183 | -47.61436 | 2024-11-19 00:47:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 039a7f8b-a765-3428-8b69-b7e551aef8fa | -1.76708 | -46.30858 | 2024-11-19 00:47:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 620b209c-87f3-326b-ac40-d60cd9010492 | -1.74431 | -46.27543 | 2024-11-19 00:47:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1e396ab8-d646-3880-976c-a8ffb2cb4233 | -1.30274 | -52.23583 | 2024-11-19 00:47:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b0abc0bc-be94-3aaa-a856-1831a58845d7 | -2.58352 | -51.7164 | 2024-11-19 00:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 765bfbce-f888-3186-b699-312c6672c045 | -2.77513 | -52.62002 | 2024-11-19 00:47:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a22ff446-f8d9-330c-8d31-c893180b8200 | -0.85472 | -48.75193 | 2024-11-19 00:47:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97dfc7e9-772e-3848-87a2-c52739469dc9 | -0.1196 | -51.4393 | 2024-11-19 00:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 3d2be839-2391-3784-b0ba-c965a2b92970 | -23.9294 | -54.1011 | 2024-11-19 00:50:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| b56eb400-474f-38bd-9463-18b6870db5b2 | -5.9788 | -45.3621 | 2024-11-19 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 0a4c5d6b-a131-3b0b-bb6d-a02e7dbb948e | -23.9083 | -54.1053 | 2024-11-19 00:50:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 17ec9fac-0757-3662-a36d-05d9b568a87b | -9.2546 | -44.9845 | 2024-11-19 00:50:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 8f1ea341-91c3-3133-920d-e538c6c3b16b | -3.5126 | -50.2133 | 2024-11-19 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 23aa4d02-755e-33ed-91b8-b12614d4e9ed | -5.979 | -45.3395 | 2024-11-19 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3a1be52e-826f-3769-a2cc-d2135c4665d0 | -2.7659 | -52.6163 | 2024-11-19 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 0a1876a3-cfef-3a0d-894e-b7e251002dfa | -5.9601 | -45.3635 | 2024-11-19 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 2ea0c633-d737-3c58-8b14-21d3b8e2ebf9 | -0.1196 | -51.4186 | 2024-11-19 00:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 5c24958a-a76a-3e85-95db-1145da35695a | -2.4827 | -49.0167 | 2024-11-19 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 27dcd248-47e8-3f61-8164-aaaa5bdd9460 | -2.7843 | -52.6158 | 2024-11-19 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| abc318a5-24aa-38ac-a082-630349cc7103 | -2.7844 | -52.5954 | 2024-11-19 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |


[Clique aqui para ver as próximas entradas](README10.md)
