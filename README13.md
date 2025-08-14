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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e573268c-e20a-35fa-879f-e73e7b570ad0 | -3.82225 | -41.57674 | 2025-08-14 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4153fc90-7e69-3301-9f0b-32e2d5b878e8 | -4.24366 | -47.33878 | 2025-08-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1fa98ee-d57d-36eb-9155-649df355b958 | -2.90843 | -48.25037 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 683ba426-00c4-32f9-95be-239b960b657e | -8.52479 | -43.2958 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 18a47dae-3381-3db7-b1bc-7e76c775c538 | -8.52422 | -43.29958 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e136e202-5b18-3a93-9a9d-3f4fe99ae036 | -8.73992 | -44.0203 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 914e7a86-ce19-31c8-9281-f0b4f1e8a009 | -6.43922 | -45.90722 | 2025-08-14 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 426e4be7-0142-3686-a0a8-d49d96288967 | -6.36729 | -43.75802 | 2025-08-14 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7fd7c59-6693-3dbd-bf1c-1d9d3c4a3bd3 | -2.90919 | -48.24567 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2a92ade-5bec-336c-b219-f634e9dd82f1 | -5.47282 | -36.7892 | 2025-08-14 04:19:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 84716d75-96e4-3482-addc-2ef149f62e5f | -7.95247 | -46.83245 | 2025-08-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baea8af7-b993-3b42-96b2-a7c2d8ab9624 | -6.95107 | -44.55433 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 69e77e4b-82f5-3e45-882e-b8691c700d56 | -3.48251 | -39.16138 | 2025-08-14 04:19:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5bd7e6ed-fac2-39be-b2e7-b5a39adbec08 | -2.90778 | -48.30334 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bf3ab708-2c8c-353e-99b3-d7cec00ee356 | -8.74494 | -44.01004 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0c1c244-19d3-3b8e-933c-20f0734d1a0d | -8.73094 | -44.01153 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee2d4f27-977e-30de-bfc9-7f567903522d | -5.88898 | -57.74203 | 2025-08-14 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 835d7b7f-5872-311d-9fa5-d50529150971 | -2.4928 | -47.56918 | 2025-08-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 61b2ef53-49cc-316e-85aa-b8909254e6aa | -4.93647 | -37.39063 | 2025-08-14 04:19:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2caf1dac-40b8-370b-914c-4dc8d5ee4145 | -6.95161 | -44.55085 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| aa29168d-ae85-3893-98f8-bc8585fb58a5 | -6.90632 | -45.20977 | 2025-08-14 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c50c6d27-6d88-30a1-b8f3-6753c92c891c | -4.17617 | -42.45271 | 2025-08-14 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49a51b4a-68e9-377a-b95e-3896782cdc4d | -5.37643 | -36.85179 | 2025-08-14 04:19:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4d66237c-6298-340a-9749-0004d9a3df38 | -8.52135 | -43.3184 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40163d62-1df3-3022-a288-df13a5e6288c | -7.94851 | -46.83553 | 2025-08-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36977ea5-efa8-3d60-af86-7429b45e5508 | -8.52307 | -43.30711 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 02696003-3e8a-3396-bb44-98deec2a6804 | -8.52364 | -43.30334 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 54eff88e-5251-3b47-a0bc-7407c4669423 | -7.25521 | -46.05892 | 2025-08-14 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da0a4d7-dc9b-3719-9589-3d0ffade88c0 | -8.74273 | -44.02443 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 981e8b83-4cbd-3c81-b881-7e1cc0939ae8 | -8.73039 | -44.01512 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f192f1c0-75b1-3496-8055-dd1f708a55a4 | -6.94338 | -44.56023 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d74c769e-cede-3aa4-a18c-dfbb7455d75a | -8.52478 | -43.31893 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0008b04a-28f2-3a47-8003-a170879f6090 | -4.22351 | -47.21512 | 2025-08-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7efec92b-9d4a-3026-b2af-216354d7afb9 | -6.45291 | -44.56441 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8934cc9-4332-3a06-9118-bd76cf33d6dd | -5.37927 | -36.8445 | 2025-08-14 04:19:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b44b04bc-023e-33da-a712-6adcbac27199 | -2.90427 | -40.44197 | 2025-08-14 04:19:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eef50edd-0990-3b9e-ade4-c81aed6f1a3b | -3.99884 | -47.07961 | 2025-08-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 245dd485-9843-3432-9250-3d9f8f64adfa | -4.77813 | -45.33139 | 2025-08-14 04:19:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e07114a6-870e-31ef-bed1-f2ff2d392376 | -2.90461 | -48.24979 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e79a300-3cc7-34ed-bd62-fbdae756f095 | -7.94734 | -46.84286 | 2025-08-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d1c7b0d-19db-3c94-b464-30670c50c2da | -8.52079 | -43.29905 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| afc3d7e4-561f-38e7-86d1-2332f9c62b52 | -0.74931 | -47.75103 | 2025-08-14 04:19:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abe59934-3bfa-322b-aa3f-ef05faaf8286 | -4.17275 | -42.45218 | 2025-08-14 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ce207ec-b029-3df1-95c7-55b0eb39670e | -5.68645 | -43.6525 | 2025-08-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b4259e4-a838-3f5e-877b-aeb50b733203 | -6.61678 | -43.87941 | 2025-08-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3615b9b-572c-39b5-bf58-4c26f0e9ea0e | -6.82295 | -44.48061 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 547fd9e1-9e64-3dbc-bc33-def320497768 | -6.94723 | -44.55728 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cd1df322-e46b-3016-aa0f-501035180aef | -8.68698 | -45.80357 | 2025-08-14 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d934bb3e-a560-3198-901b-0b710c717cfb | -4.48348 | -47.66929 | 2025-08-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23afda9a-81ae-38aa-993e-7b99cce3dba3 | -5.15946 | -39.50566 | 2025-08-14 04:19:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 17cbae86-bb4c-3b08-9d86-aee60c44d391 | -6.54257 | -43.96505 | 2025-08-14 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7dd6e95-2294-37a7-baa8-133f24266643 | -8.52136 | -43.29528 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| e8989bbb-d9ed-3d2b-abb1-9bcf7d6cef5a | -7.13494 | -44.22243 | 2025-08-14 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c12af2ba-7b6e-3f7f-b50f-6785766d7315 | -8.74665 | -44.02137 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d248afb6-a32d-33bb-bb78-a4827ca607af | -3.91504 | -46.45251 | 2025-08-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d36814b8-6a3e-3e9d-8fc3-848689f1b719 | -6.61624 | -43.88294 | 2025-08-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4bf355c6-1b79-3728-990a-157c89f94720 | -5.7976 | -43.61516 | 2025-08-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1ce2893-80b3-3b26-a483-804ad2ce6f77 | -5.98356 | -44.15006 | 2025-08-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47312381-9047-36e0-b972-a49af19410fb | -2.90767 | -48.25509 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94ae5c86-f334-317a-a8b4-7c04c879d470 | -6.1845 | -43.30894 | 2025-08-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55463c2a-371e-32cb-b0f7-175c09822cd8 | -6.82626 | -44.48112 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dfc9926-ed95-3db1-a560-b25066a2aa10 | -4.61091 | -45.61393 | 2025-08-14 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ef68427-07f0-37a5-95f9-8511d45248e8 | -6.09781 | -44.61804 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72b25251-26e2-33cf-ae68-0d4bf0d5db69 | -3.885 | -41.03202 | 2025-08-14 04:19:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c7784c1-2f01-345d-8ecf-da921ca20d46 | -6.18732 | -43.3131 | 2025-08-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb6e0801-9ecd-3ed5-add4-b06742d3b672 | -5.47501 | -36.78928 | 2025-08-14 04:19:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 78931414-786a-3835-b5c7-8331fdf7cd12 | -6.94776 | -44.5538 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 45cab376-024c-3e01-be4d-f2fa05529346 | -5.37719 | -36.84639 | 2025-08-14 04:19:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0572a01e-7a14-319c-8a01-796ee51dd19c | -2.90385 | -48.25451 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| beb8180a-741d-313a-a859-2f330a1e48b1 | -2.36801 | -51.91101 | 2025-08-14 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 58857b6c-ca8b-3e42-add4-665fcf0e590f | -5.98302 | -44.15353 | 2025-08-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b10f0da1-5701-3f7b-b8da-859f38cc4e81 | -6.88129 | -40.96275 | 2025-08-14 04:19:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b39ecbd3-e903-3087-838e-643e15648def | -5.78197 | -43.6055 | 2025-08-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 770ca029-56d6-383e-9e4f-1bdbea83e578 | -5.47772 | -36.78983 | 2025-08-14 04:19:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 91dbc5da-c159-3ee5-ab72-f14da1c976b0 | -6.95215 | -44.54737 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 05eb8435-7a40-3f30-8617-b34d34e627db | -5.86631 | -42.84271 | 2025-08-14 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 660165d9-ad95-3f68-bbc5-532571a3ec11 | -8.52077 | -43.32216 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b806c8f-4453-39ca-8240-bc1c4a81e457 | -6.0807 | -59.9465 | 2025-08-14 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| ab5ab22a-ab11-37b1-b0a0-5b57c86ceecf | -6.8956 | -59.1462 | 2025-08-14 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.5 |
| d590e73f-fdf2-3cc6-8410-b4865dbfeee2 | -6.8955 | -59.1655 | 2025-08-14 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 9ba77679-31ec-3c56-bec3-d4f5e1c32fc1 | -6.8771 | -59.147 | 2025-08-14 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 51e7119e-3b12-3c0f-ab55-6210dcf71819 | -6.877 | -59.1663 | 2025-08-14 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e44fee33-c0a7-39c6-a810-50de9350b1e0 | -6.914 | -59.1455 | 2025-08-14 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 65e2aa61-63d6-3493-bc54-40f52e6a4526 | -13.07714 | -49.33055 | 2025-08-14 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c74c045-3f22-301c-bb7f-72b9268183b8 | -14.24074 | -44.58661 | 2025-08-14 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 994c5cae-9ac8-3e83-9c10-06d9df2572bc | -7.24653 | -57.64731 | 2025-08-14 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8eb20d75-82a7-3210-a7fe-d4defc042e09 | -15.92545 | -43.51541 | 2025-08-14 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d21f8815-2631-343a-8dec-4bb545ca7432 | -13.11412 | -57.14646 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6e891d5-f162-3aa9-a087-d2bd1bceabe1 | -12.15787 | -44.62956 | 2025-08-14 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1656a4d6-1000-3d15-affa-7af7f4f53e86 | -14.36247 | -53.37245 | 2025-08-14 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a0656e7-d478-335f-9c0e-58bafd2abfac | -10.53587 | -42.54902 | 2025-08-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b0af0214-79de-316c-bfa2-e6c373044199 | -12.17051 | -49.08588 | 2025-08-14 04:21:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6506faa0-ba31-3d25-a24e-0bc161666598 | -12.3326 | -43.44007 | 2025-08-14 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48788492-c1be-3ad2-8e5d-2a5119cfb6b7 | -9.2058 | -59.65149 | 2025-08-14 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b52a92d5-5f37-33f6-8f2b-d4707e755d5c | -10.34609 | -57.59969 | 2025-08-14 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54c69318-50ad-38c8-ade9-503ca55566d9 | -10.00576 | -59.22417 | 2025-08-14 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fd35f078-1f7e-3fb8-9d92-0ab2ba79da8b | -12.58665 | -46.979 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cdb3cdd-f383-3490-8ecb-3a80a7bd7e17 | -12.58007 | -46.95607 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d07d93a6-150c-3408-9f0a-07412c6e71f4 | -13.78879 | -44.33083 | 2025-08-14 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76776e53-6ade-3b48-a50a-9b46ca2e2f43 | -11.6894 | -51.62407 | 2025-08-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README14.md)
