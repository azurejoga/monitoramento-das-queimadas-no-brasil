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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d10a6192-4bc9-3642-8c41-566d78a5c75c | -10.56836 | -45.26869 | 2025-08-04 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d152f0f5-13fc-3e37-ab33-b76439bfa9c6 | -7.01457 | -59.83138 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9a1b240-5c29-38a1-bdeb-1216dde65d02 | -8.01385 | -43.18988 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0132af1d-3dab-3f1b-9a65-79b406a23bbe | -8.35641 | -46.90791 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48bf9922-ac7a-3bcb-ba6a-995ce2fbd5ba | -12.69862 | -48.08504 | 2025-08-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17ff89bc-c6cb-3ef4-8a6c-e5b91907285f | -10.23135 | -54.26847 | 2025-08-04 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b6d765c-b11b-3a41-aec4-d917c469424f | -8.25958 | -47.3339 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1bcd942-40aa-337c-b987-c26883c29e23 | -7.99214 | -43.162 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 74fba676-c370-3e43-b8c1-3b07a8f6eace | -11.22624 | -48.43786 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9894f037-561d-36d9-8f3b-562b26cb72f3 | -8.38752 | -46.93486 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9e9b28b6-b95c-304b-b5b6-94a9d845e2fa | -8.73467 | -46.40908 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 132ec06b-bc4d-379b-8879-462544af4906 | -6.64873 | -59.09639 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5779be8e-a71e-39f1-a6ce-1447aaaf92fe | -8.01453 | -43.13587 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cdeb33d2-fd2e-333e-847a-bb99dfa2b47c | -7.6489 | -49.84182 | 2025-08-04 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 084ee918-60e5-3bf2-a953-e19f797497b2 | -6.62623 | -59.96537 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4d39c0dd-abdd-3a14-9b66-6a90031bc904 | -7.26868 | -46.16111 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6732c53a-3362-30fb-ad8e-ad71ecdbf8bb | -9.46433 | -57.83504 | 2025-08-04 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c0b7bb3f-bbd6-3f30-a135-de01fbccd3d8 | -12.4339 | -44.8549 | 2025-08-04 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6f56d14-8710-3d69-8414-0bde32bcb241 | -9.45658 | -57.83792 | 2025-08-04 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ac1a6ea-131d-3fde-aac4-7f4ddeeb4b5f | -9.98129 | -67.57471 | 2025-08-04 04:57:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7bf70aa-ecec-3dc3-a35b-5482bff7d6b4 | -6.67035 | -59.16267 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bac94d95-d074-32aa-8238-a717cdda9d3c | -11.22262 | -51.52766 | 2025-08-04 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2191e8f-670e-3720-9955-1c08e5b3ea25 | -7.03194 | -59.85368 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ff526fa-125e-34d4-9056-f24488dfdca3 | -7.99032 | -43.17623 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 155e892c-a59c-3a61-b512-effe02ea8e2f | -11.75871 | -44.97107 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b916343-8a79-3fae-91aa-ebcef2ed8c69 | -6.15285 | -57.91356 | 2025-08-04 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5030089-dae4-3c2a-8889-60ac8e37f335 | -8.5484 | -47.46083 | 2025-08-04 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65003d51-46ef-3173-92d5-b6cd59062e89 | -7.00633 | -59.83008 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32f48faa-8011-3f8c-93ef-7a902e9d25c4 | -7.7718 | -45.22302 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5b37ba7-3d73-320b-8552-090901d13735 | -10.2927 | -45.17617 | 2025-08-04 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0e4f901-8bb2-390d-bbf0-9736b5794d4d | -7.6432 | -45.29982 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d824026d-a19a-3f94-bf4a-d03f40a08d3f | -7.02689 | -59.8335 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4d66499-f6f3-3963-a2ba-f73aa4093635 | -6.15212 | -57.91795 | 2025-08-04 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0b8900e4-4854-36f1-bd01-475e2683f967 | -7.03606 | -59.85436 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fd9b8ef-374e-3593-bcd0-7b35c9d0101b | -9.39911 | -45.49949 | 2025-08-04 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d102639-07be-3624-8eab-289b7770fc13 | -8.04268 | -43.11473 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| cbd3ba93-e653-3170-83c9-8166635c977f | -6.62143 | -59.96841 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c77c25d2-f7ed-326e-9e75-299957654fef | -8.73548 | -46.40303 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e83f69ee-cb19-38e2-b462-7df52b8fd87e | -6.64744 | -45.88979 | 2025-08-04 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad1ac890-5735-3d36-95d1-3a28d79f4b66 | -7.01868 | -59.83205 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d330c088-8b52-3045-833e-da07db034672 | -8.73002 | -46.40518 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 118694de-bd34-3d15-a83e-ff95fc1782c7 | -8.00576 | -43.20356 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 164f1a72-8d99-3279-ab06-b7701a83f43e | -6.64791 | -59.10139 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 350e53d0-0e14-3bd2-88d6-a57fcbabc1aa | -7.02753 | -59.82975 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8005cb22-55df-3eb0-b92b-a060ccfd9078 | -8.00702 | -43.14484 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 888cbe77-f7c7-3dbc-8c12-fe829954a915 | -6.6227 | -59.96075 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30351ecd-74c0-38ee-80ea-acd06b168a5b | -7.01109 | -59.82699 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf45c2ab-8ca4-3a3b-a7ef-5c258154fc68 | -6.61499 | -59.9555 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c0c24b5-6050-33a8-a37a-9ed71f60382e | -8.73895 | -46.41582 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2b0dd30-7392-3025-8ea3-f85dea947af2 | -7.44335 | -48.94399 | 2025-08-04 04:57:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd393d79-e918-3647-b112-13e22d4d7dff | -9.3982 | -45.50652 | 2025-08-04 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c42b557-a27a-3301-b63c-d2c55cd0f59a | -9.46367 | -57.83907 | 2025-08-04 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ad6bfaa-1ff0-3e45-8383-fb39c0cd81fc | -7.99388 | -43.15953 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 2a0d92cb-23dd-3b60-99e9-e98cd31d3086 | -7.37338 | -44.19037 | 2025-08-04 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b30112a7-29d1-33bd-a3a7-df10d614eca5 | -8.2624 | -47.33816 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b8009ffc-b79d-38f2-bc89-f65c2516bb14 | -7.41189 | -45.26729 | 2025-08-04 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 482e3f1c-62f1-36b2-af14-8b77e8c7c1f0 | -7.99647 | -43.17753 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1b55fe9a-f3d9-3270-9ca9-38275b54de96 | -8.74176 | -46.39476 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99018642-c6d8-32f0-afcf-dbf0acd6cef8 | -12.69792 | -48.09061 | 2025-08-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e82b334-0b2a-3284-a5c9-c62e27c313e2 | -10.24572 | -50.16461 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 278dd3e6-2778-3449-8718-3e65116c585b | -8.51664 | -44.75035 | 2025-08-04 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea46e3ab-04da-3e0a-a1d2-ba2fdc0d35ae | -8.00638 | -43.19878 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d13cba9d-dbd6-3849-b79c-7ee4030233ba | -11.93291 | -44.94374 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5554fb56-662e-3a01-8bc2-c62bde72d39a | -12.70213 | -48.09581 | 2025-08-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baf0521a-7f79-36da-a11e-4cdd54c97eb9 | -6.61917 | -59.95618 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a167b2bf-297f-3bda-87fa-32e94830b149 | -9.44119 | -46.31805 | 2025-08-04 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1a3381c-0230-38d6-a13f-d3714f818409 | -7.99154 | -43.16669 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 77f0a726-3a07-3481-afbd-ad85c229ca0a | -6.66953 | -59.16769 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a870e2c9-e1cc-3e23-adac-0bdea3d3cac3 | -8.05023 | -43.10564 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f3c17c39-8fa2-3c01-8e2a-817289fb6d17 | -10.68124 | -56.55333 | 2025-08-04 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cda4966-d171-3e2d-841c-eee2dd2f9bbf | -6.67756 | -59.161 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32a77c2f-0349-38ba-bb24-e2cd5f7fad0b | -7.08043 | -44.3758 | 2025-08-04 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7e612e3-9615-362f-abe3-c131659ddb25 | -9.39865 | -45.503 | 2025-08-04 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f538fa9-fe7b-3925-ab9e-068445c3060c | -7.37973 | -48.07503 | 2025-08-04 04:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48563fc3-f547-3ee5-a832-976e5e94ad69 | -11.22197 | -48.43448 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 377d82c3-98b6-333e-bbda-489a5f70b9c0 | -8.36128 | -46.90867 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3ac7e33-01c1-3455-bd80-3d0158fbf305 | -7.99131 | -43.17847 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6c613a75-9a81-3370-b975-f601259c5b6d | -11.78509 | -44.9969 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4033e82f-76ed-3472-a4ae-5dbfc2fb2ddb | -9.39318 | -45.50241 | 2025-08-04 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 847c8470-d243-343f-a550-c5ae8278cdd8 | -15.49086 | -47.10349 | 2025-08-04 04:59:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c41ce357-3734-3527-bfd1-2d899b98b10f | -15.56827 | -47.08824 | 2025-08-04 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4c0f43a-c4bd-38c1-9b9d-ce2e5fa89d57 | -13.05954 | -56.9202 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d245f87f-4596-3592-816e-65fac01d0177 | -15.56288 | -47.08801 | 2025-08-04 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a372ac87-b8c6-36a5-9f45-28651514c954 | -13.06957 | -56.92188 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56be75b8-dd69-3d2b-b04a-4406513956a9 | -13.04693 | -56.89219 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| bae438bc-10b2-394f-bb51-363cb8002f5d | -17.36357 | -46.08371 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 999ff43f-7ad8-3e90-abb0-25cbe2f1b463 | -13.07349 | -56.91884 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fc1a86f-f0fb-3178-a165-36e77d88d6f2 | -13.05478 | -56.88609 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0f5cf10-fa3a-3b53-bf9a-1e8b4a230298 | -15.76194 | -49.94164 | 2025-08-04 04:59:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0eceacd1-588a-397c-a299-6af8afa7790c | -13.05971 | -56.898 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc4aeb30-9da3-3a43-88ff-1e2f54dd7e2b | -19.52452 | -46.90593 | 2025-08-04 04:59:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc627a57-6b0f-3b3a-b051-70d75007b01e | -17.36936 | -46.08471 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb8db034-38c1-3b7d-af51-78de0057e118 | -14.84512 | -48.39308 | 2025-08-04 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 985306c4-7c4b-3754-8ed1-e8a999c65da1 | -17.36331 | -46.0862 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d665ed7c-c7e6-34e2-af7e-bf5530976068 | -17.37449 | -46.0923 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9161ce3-84cf-311c-92be-96b189b3c2fc | -19.52152 | -46.90409 | 2025-08-04 04:59:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f978632c-8616-360a-9606-36c646cf76ff | -13.06305 | -56.89856 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa248bc6-8401-388f-9dcf-d94522c61ef3 | -16.42654 | -43.72094 | 2025-08-04 04:59:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03ab15cc-f920-3b95-8252-d8a5b9063a14 | -17.36322 | -46.0872 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0189e1c7-d8bf-303e-a159-7cee91017c44 | -13.04751 | -56.88858 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |


[Clique aqui para ver as próximas entradas](README24.md)
