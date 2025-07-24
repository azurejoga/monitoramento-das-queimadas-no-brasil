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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c9f0702-7e00-325f-bb4d-4408b9371214 | -3.95518 | -52.20411 | 2025-07-24 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5b49b86-9747-3df1-b162-d3f56103a851 | -3.07613 | -52.43581 | 2025-07-24 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62c7f676-7277-3bbc-a633-3c82fe8008a9 | -4.05568 | -42.52645 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 68297ad4-53fa-3a20-93a9-360ceeab6d20 | -5.18741 | -44.95918 | 2025-07-24 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 824349ae-5e99-32cc-ad30-41cf79589b43 | -3.17519 | -49.44827 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 12936d59-af70-3143-88e5-5b330503d6b9 | -4.77861 | -45.33381 | 2025-07-24 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f8fd316-5255-33ee-a0e0-7b284e011c17 | -4.77804 | -45.33772 | 2025-07-24 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51711b90-f806-3ffb-954d-c11343d66357 | -4.05384 | -42.52556 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b58c55fb-5aa7-35b0-ab56-f52a1135e3ab | -3.58447 | -47.52271 | 2025-07-24 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec79cf8c-c7a8-32e2-b962-faff4cfcc871 | -5.67651 | -43.66747 | 2025-07-24 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fed6627-34c3-355a-bb00-c5bcd8534168 | -3.58366 | -47.52806 | 2025-07-24 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d99e0126-aa63-3272-a3b7-f2998bad51cc | -5.68294 | -43.66859 | 2025-07-24 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a494b83b-1647-376c-ad21-3ba3208d3289 | -2.65929 | -47.3973 | 2025-07-24 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 31dd7f0d-c4c8-3c55-9584-b881a98249a8 | -3.1863 | -50.39136 | 2025-07-24 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bef60bfd-0d0a-3e58-9ba3-4151b1b4a9c2 | -3.04266 | -49.43759 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a49ac0d0-9518-38dd-a0a9-72b9c9bc0e71 | -2.65784 | -47.39861 | 2025-07-24 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| edb4906e-2ce8-3fa0-8499-1284f161fa0e | -3.05786 | -47.38113 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 150b6bcd-73a8-3b82-a2c6-b057149242d9 | -4.77981 | -45.33555 | 2025-07-24 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebb6141d-36c2-3bfa-be08-ea365d332456 | -2.38785 | -47.63184 | 2025-07-24 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcb001ed-e481-3a67-8042-5b3f69c39144 | -3.05299 | -47.38041 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc7d8840-dc11-3b5e-a0ff-5794bd44327f | -3.17883 | -49.45279 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| c770df5e-0842-357c-a9b7-5d8b581c6782 | -3.17942 | -49.44888 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| bcf75408-1496-3ebe-a12f-4c0ddf2491ad | -5.188 | -44.95498 | 2025-07-24 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de23fd0c-4adb-34c7-a4e5-423805268c41 | -4.04885 | -42.51254 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 6f225a03-1c5f-303e-9271-908358323a61 | -3.18306 | -49.45339 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a734d13e-a565-3aba-afd2-c7acda7e43f3 | -3.22908 | -46.78585 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1b628b3d-60c0-33ea-9068-65b1e8801571 | -3.21152 | -54.96474 | 2025-07-24 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715e5415-b1fe-3588-801c-d84eaa592e79 | -3.35803 | -47.15947 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 812fb578-dae3-321b-9c30-1bfd886c4dc8 | -3.04811 | -47.37973 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75a06a3e-b752-3c92-b367-c81af915b662 | -3.17037 | -49.45153 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8e46a110-91e0-359a-9fd4-853bc0786a91 | -4.80627 | -43.21125 | 2025-07-24 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b06355d9-0b4d-393b-adc4-cf7d24ff7b6e | -3.35751 | -47.15812 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35f66728-1591-3af3-82d0-8fb4d15c89ca | -5.68217 | -43.67397 | 2025-07-24 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20ac0004-a10c-327e-b09d-67bf8a345595 | -4.30581 | -48.10155 | 2025-07-24 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 08416684-02ea-3c23-b983-260017e317b7 | -4.04299 | -42.51841 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dad11c9b-93e3-3030-b70d-07ef54e5c8f6 | -3.03598 | -49.42457 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68174e48-f403-33e1-bd69-b4fc5bbaa335 | -9.75936 | -65.09223 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31f518af-9f4f-3eee-bca3-88535baf99c4 | -7.25003 | -43.06638 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 0efae990-da56-3288-ac40-942a5cea54a9 | -8.48727 | -47.23309 | 2025-07-24 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 928f8fad-e6e1-3f72-a79d-6aff7874679e | -7.31026 | -49.57711 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1da1783-11f4-3660-aac1-004b452c8663 | -9.32914 | -63.52175 | 2025-07-24 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec52ce41-0c6f-3342-8ddf-e101f9136a17 | -12.42368 | -45.37607 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 661e4400-f21c-34fc-8371-abc03fe118b1 | -7.26954 | -60.1782 | 2025-07-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f665f4f-a9f5-38c6-b7e0-e9903a30cef9 | -6.44949 | -43.83007 | 2025-07-24 05:04:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f933f55-4a5f-3bf5-b7c2-7422a2ae440d | -11.77467 | -47.40488 | 2025-07-24 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fdb9dbe-7544-3b44-96ba-0cdc0588abd1 | -7.25686 | -43.0673 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 3f8a5932-fa13-3f6f-b913-19e97849ab0f | -7.24679 | -43.07984 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3d1d6386-2723-38e3-b8ea-1156794a3ae8 | -8.03399 | -47.65129 | 2025-07-24 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b35577c-8195-3d95-8241-c122f80fefdc | -6.55328 | -56.24728 | 2025-07-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ec84233-4ead-3d9f-bbb7-6adee80a37d9 | -7.45853 | -57.67033 | 2025-07-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb22e990-36a5-34c4-bb83-237d7ee5ae07 | -11.77518 | -47.4015 | 2025-07-24 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7256fe95-cf5c-332c-8759-f5658ce9242e | -10.96366 | -49.57583 | 2025-07-24 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41013259-ba06-36be-99ac-c6ef9823bf77 | -8.72119 | -51.13578 | 2025-07-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d9f6c3f-0dac-369a-9b0f-c06135df59df | -8.4907 | -47.2336 | 2025-07-24 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ecde8d6d-6be4-3fdd-82c4-3c0aea0ef52f | -8.92479 | -47.34751 | 2025-07-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2392e79-8f82-391b-8b8c-afea0863e29a | -9.66587 | -48.52514 | 2025-07-24 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 482b6187-ce46-3af1-9443-354dc45ee763 | -7.91399 | -61.55616 | 2025-07-24 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1751c4b-2f58-39be-a4ce-ea22f76992a6 | -7.1661 | -44.37678 | 2025-07-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2cc3ad6-8fbf-39a5-8f26-4f91ae8d4e9c | -9.52671 | -63.62968 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac09d610-2964-3ad5-9e95-bf8d197aaea3 | -7.46145 | -49.39808 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3d53041b-74eb-33d2-9929-1a22bee3ce3b | -7.25277 | -43.08699 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f565abfb-de1e-316c-813d-479cf8c4c26c | -8.09494 | -50.0892 | 2025-07-24 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff28ede1-e60f-3b81-9932-c8a2a74d4322 | -11.73282 | -48.18668 | 2025-07-24 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 76617fe8-88a0-3c63-958d-4279df3e23e7 | -5.5033 | -51.13905 | 2025-07-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d09a7a47-87f6-375a-8a26-6427305db010 | -7.4608 | -49.40268 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f3e993a-f3de-3ef3-a6a7-2fc1a353994f | -5.0066 | -56.29309 | 2025-07-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78c5f18a-7367-3719-9b69-b326212395e8 | -7.45295 | -57.6619 | 2025-07-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdafa642-ea81-3e8a-8ff9-0159e2a973b1 | -7.26202 | -43.08115 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| e5299de4-79f8-3d96-bdfa-44b13e3d291e | -6.54113 | -49.84194 | 2025-07-24 05:04:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c58c102-cdaf-3c5e-ac50-e0b6525f3fc4 | -10.62998 | -45.23408 | 2025-07-24 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a9b795d-f30e-3041-8ad0-e90e8a8c1581 | -7.89799 | -45.55891 | 2025-07-24 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd461fd5-9067-35b2-99e5-9e660a27dc15 | -9.32263 | -49.11358 | 2025-07-24 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1134c36-dbd1-3a7e-9292-8156af3c1da4 | -9.75882 | -65.09522 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8058ca36-d4b6-3e5d-9262-54f6a024aeae | -8.57859 | -63.87708 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af0f27cf-afb0-34b3-8fdd-44aacfaf811b | -10.12376 | -57.76923 | 2025-07-24 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6d13b29-2929-3b9c-9d5e-9e3bc481ed79 | -8.09558 | -50.08482 | 2025-07-24 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dba0b732-edc6-3c8d-83d2-532a48c06333 | -6.26379 | -45.26961 | 2025-07-24 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59d6a3a5-24cb-3479-af6b-51815273fc07 | -12.4294 | -45.38204 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afa97365-ca8d-3e4f-9b98-cbe7e7941688 | -12.42005 | -45.37835 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c09ab2f-c953-3e3e-892d-42777933bc83 | -9.20326 | -59.67602 | 2025-07-24 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7db49984-31e6-3a44-b8c4-048bde75cef6 | -7.2552 | -43.08018 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 3fcb0223-18cf-3d11-98f7-05b66bcb3b38 | -10.71372 | -48.85287 | 2025-07-24 05:04:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 476951dc-2689-3556-9999-44d9b217e80e | -10.62433 | -45.22841 | 2025-07-24 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3e43f1a2-f59e-369d-a86a-b3cfb85ab3ae | -10.62936 | -45.23913 | 2025-07-24 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddecb1cc-f66d-3efb-a695-5c87be074088 | -11.77513 | -47.40125 | 2025-07-24 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8252bad2-1c59-3dc6-b0c9-5d30b7e40b26 | -12.42638 | -45.37915 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f9ca5d9-4100-318f-b4c8-2c1f940ada02 | -10.04186 | -59.09334 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f6eb345-5fa1-3505-b4b6-ab987d63a951 | -7.24919 | -43.07286 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| eb343eca-9526-3b1c-966e-9d2677322fb7 | -10.66771 | -47.78512 | 2025-07-24 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ec5a999-448c-33c6-bc25-48d6ab968b29 | -12.4258 | -45.38437 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6528607c-46a1-31ea-948e-667b41ab94c4 | -8.4832 | -49.55325 | 2025-07-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd154abc-4d42-31a9-9860-73204892a4d6 | -8.49647 | -47.23104 | 2025-07-24 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6816b98-61cc-33d5-9fc1-4021e04adc2d | -10.94711 | -54.3711 | 2025-07-24 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a032df2f-d33c-31e9-a7d3-5f94159224ba | -8.03955 | -47.64896 | 2025-07-24 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c953fc8f-b059-33ab-a3c8-4e86302e8bc4 | -11.10824 | -50.48865 | 2025-07-24 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4f770dd-30f3-3a3f-ac2d-0d859bbe9e11 | -10.67348 | -56.55208 | 2025-07-24 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2a96c65f-7594-388f-a032-cec790787e3e | -10.06268 | -59.09681 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4f7a35d-1161-3994-9932-c3e63219c556 | -8.47866 | -49.55254 | 2025-07-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 74f80ddc-3e5b-32f6-bdc0-900a1aa8fd3c | -6.53611 | -44.65991 | 2025-07-24 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03de827d-116d-3179-9e16-e36dc9e972ad | -8.29845 | -55.10255 | 2025-07-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README22.md)
