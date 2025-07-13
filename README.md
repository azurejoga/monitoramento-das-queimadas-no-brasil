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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e294494d-70dc-3e81-a67e-7d03bac4177a | -13.8482 | -45.8916 | 2025-07-13 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| b36fd775-b35e-3332-9e2f-af4e56aa1496 | -3.6179 | -47.557 | 2025-07-13 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 4dc37811-8236-38f9-bdaf-cbf6738028e0 | -7.991 | -43.3884 | 2025-07-13 00:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 349.8 |
| ee52ab58-960c-3b2b-aad6-15adf810eab2 | -7.9913 | -43.3649 | 2025-07-13 00:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 158.1 |
| bb0b37d8-2cce-3222-a1b2-f1b263c5f4d1 | -7.9721 | -43.3904 | 2025-07-13 00:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 132e43d5-1ddf-3d0f-afe5-f9b21182df35 | -5.739 | -44.9945 | 2025-07-13 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| bee5bfd3-63f9-3aa5-9082-dcf7a6a8af81 | -3.618 | -47.5352 | 2025-07-13 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 9346787f-b804-3e65-aece-dfc3898d873a | -7.9907 | -43.4118 | 2025-07-13 00:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d919d0dd-2b6a-3829-9306-2824aa8f3206 | -5.7392 | -44.9718 | 2025-07-13 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f298b18c-477e-3f6b-bde4-73a5f1d518ab | -7.9897 | -43.381901 | 2025-07-13 00:05:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c1a1e8b-8828-3423-9da7-5a678c71221c | -5.7397 | -44.984402 | 2025-07-13 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 983c5bd2-8599-35f3-8a42-1a064eff7dc6 | -13.8321 | -45.892399 | 2025-07-13 00:05:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37d27d5e-16d1-317f-bb6c-4f3144dbf403 | -6.3061 | -43.6465 | 2025-07-13 00:05:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e6a73e5-57fa-3eeb-ad5c-b04fe6365f00 | -7.0332 | -44.349899 | 2025-07-13 00:05:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 548130ef-87d4-3c86-800e-2464a4d5ac50 | -7.992 | -43.3922 | 2025-07-13 00:05:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 56afd64e-7829-3faf-98c4-0540540ffcec | -6.273 | -43.402901 | 2025-07-13 00:05:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 128594a5-b5e2-34e3-8cbe-0ef4e0d0e386 | -7.9822 | -43.394299 | 2025-07-13 00:05:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99dda2c5-b275-3981-afe4-02e5c8265cfa | -6.2632 | -43.404999 | 2025-07-13 00:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53dc3400-b990-3e48-87cd-27c05fb1f1d8 | -5.2626 | -44.862099 | 2025-07-13 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e70607a3-03bd-3f43-89b5-c90f811ddeab | -7.9799 | -43.383999 | 2025-07-13 00:05:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 357a4e56-c0e1-3a12-a2a4-12c417a90b65 | -10.5591 | -49.1036 | 2025-07-13 00:05:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc4d110f-3b0f-3ea3-827e-64c51bb4d68d | -7.9777 | -43.373699 | 2025-07-13 00:05:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 41927e19-95d6-3d52-add2-a22136341d08 | -4.2782 | -48.043301 | 2025-07-13 00:05:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26280475-a9a1-3ddf-8bb1-c8ce713f1a41 | -4.2879 | -48.041199 | 2025-07-13 00:05:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7119629e-e428-37f8-b963-62f534fcb4a2 | -7.9875 | -43.371601 | 2025-07-13 00:05:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e7e8bac6-6e8a-3c56-b3fe-177bfde9db49 | -8.5008 | -43.283699 | 2025-07-13 00:05:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 537c65e7-7ad1-39ea-867c-6367c9f466b4 | -3.6063 | -47.537399 | 2025-07-13 00:05:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43b6318c-194b-37d5-93f0-5c03498039cb | -5.7273 | -44.9744 | 2025-07-13 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b813210-f7d4-3e80-b1e3-a198c1f6d803 | -3.3992 | -43.362598 | 2025-07-13 00:05:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 691e0e69-4557-3df0-b51a-5a9e85c000b3 | -6.3083 | -43.6567 | 2025-07-13 00:05:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0377b3e3-ae8a-39cc-aa5f-40c38a0af892 | -3.6123 | -47.518501 | 2025-07-13 00:05:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9754467d-d0c9-3dfb-b6e5-a0de4077f067 | -5.26 | -44.850399 | 2025-07-13 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21a9a811-3844-38a8-a8e1-6008c51a1be4 | -3.616 | -47.535301 | 2025-07-13 00:05:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29491c9c-0ac2-3692-a91d-84cf86d97484 | -4.5253 | -48.010399 | 2025-07-13 00:05:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a28bcaa2-6a30-31e3-84ec-7fd2901b8195 | -5.0196 | -38.5294 | 2025-07-13 00:05:00 | METOP-C | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 45d4db52-71ad-3a24-89d8-93895634bde5 | -3.4012 | -43.371601 | 2025-07-13 00:05:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01ed2852-6d66-3cd8-9c81-421353d4f550 | -5.73 | -44.9865 | 2025-07-13 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 690e2cb8-e81d-349b-9120-d0b789154d3f | -5.1997 | -44.3456 | 2025-07-13 00:05:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 470d1676-943d-30e6-8a83-6ad49781a631 | -16.070101 | -43.6451 | 2025-07-13 00:05:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 34a10daa-7faf-3c42-9ba3-5f61395211d9 | -7.0307 | -44.338402 | 2025-07-13 00:05:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7f8d28d-24cc-382c-b82f-325b1bd56bbb | -5.2021 | -44.3564 | 2025-07-13 00:05:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e66d0d91-edfa-3c64-b835-947026e2866f | -3.6026 | -47.520599 | 2025-07-13 00:05:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a87f88-3fac-350a-864c-a52c22bab977 | -5.2652 | -44.873798 | 2025-07-13 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2ad33fb-5eaf-3003-8414-355085aa6f01 | -6.3105 | -43.666801 | 2025-07-13 00:05:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c17b7b87-064d-31aa-bcb9-f85f78b9a73c | -5.7371 | -44.972301 | 2025-07-13 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 419379c6-770b-3ea9-a0de-93102a0f38a2 | -18.0393 | -50.5399 | 2025-07-13 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 43f5ede4-8273-309a-8d20-1c260fd99550 | -18.0398 | -50.5177 | 2025-07-13 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 7d912007-ec7f-31af-b2ff-db05a93e5ae1 | -7.991 | -43.3884 | 2025-07-13 00:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 292.4 |
| 243c0c99-4758-379f-bbf2-cabd1c22007f | -7.9913 | -43.3649 | 2025-07-13 00:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 27cdad86-d382-31d4-9f49-ff2b47513249 | -3.6179 | -47.557 | 2025-07-13 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 5bcb81c4-0476-3d74-89f7-6bd18880b669 | -7.9724 | -43.3669 | 2025-07-13 00:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 4314ff9b-02c2-3b54-9bab-c3cfbe53e6eb | -5.739 | -44.9945 | 2025-07-13 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| a465d727-d850-381a-b5b0-aa030607bac2 | -3.618 | -47.5352 | 2025-07-13 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a7529383-7f34-3e2e-840c-2354e447ac22 | -8.0099 | -43.3864 | 2025-07-13 00:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 43e33311-45d8-35a4-a033-abf9617dd0ad | -7.9721 | -43.3904 | 2025-07-13 00:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| bd1be14a-aa67-31fa-8f7c-c69cd3c94224 | -3.6179 | -47.557 | 2025-07-13 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b77983d4-ea0f-3c72-a796-2c54a4d4edb8 | -7.9913 | -43.3649 | 2025-07-13 00:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 3bd1deea-8af4-3fdb-acbe-410be9c4d05c | -7.991 | -43.3884 | 2025-07-13 00:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 360.0 |
| 5a314fbc-680a-358a-a15f-96cebc8b35fa | -7.9721 | -43.3904 | 2025-07-13 00:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 0937c338-9ab5-36cd-88a5-48d10e1cf013 | -5.739 | -44.9945 | 2025-07-13 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 27275317-6880-3a9e-8df2-ca7a186c2e08 | -7.9724 | -43.3669 | 2025-07-13 00:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| c20193d7-494b-3a8d-acb8-4f0dd32132ca | -3.618 | -47.5352 | 2025-07-13 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 4f259b6d-232e-353e-9be3-1d62d1f9ecf2 | -3.6179 | -47.557 | 2025-07-13 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b8924180-6ad8-32de-8ec7-2c7b4ba25135 | -13.8482 | -45.8916 | 2025-07-13 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 36422c74-b634-3f6c-a377-96b68f364381 | -7.9907 | -43.4118 | 2025-07-13 00:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| ca41b9c1-a361-33d0-8188-646ad6912289 | -13.8477 | -45.9146 | 2025-07-13 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 63573ccb-cee5-3a3b-b1e4-bc488d56dfd0 | -7.9724 | -43.3669 | 2025-07-13 00:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 4fed27d2-cc4e-3493-96bd-c1707be4405b | -3.618 | -47.5352 | 2025-07-13 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a6cc771c-128e-3528-bd04-2be9cbbc0b44 | -7.9721 | -43.3904 | 2025-07-13 00:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b2da9343-e6c8-398f-88be-9436daa1269e | -7.991 | -43.3884 | 2025-07-13 00:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 325.0 |
| e03a2ff0-b8cc-356e-819e-47291e6d25d2 | -13.8288 | -45.8948 | 2025-07-13 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f8455816-a1e0-3a08-b6f3-6a2bf3c19da2 | -7.9913 | -43.3649 | 2025-07-13 00:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 166.5 |
| 3cf93324-8b63-375d-bea6-1ca6f410093c | -7.9721 | -43.3904 | 2025-07-13 00:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c904b6d9-cf10-3dd0-9bae-e8ef68cd2901 | -3.6179 | -47.557 | 2025-07-13 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| d1bde9ac-dc33-3197-9f15-9e7a1f4367d6 | -7.991 | -43.3884 | 2025-07-13 00:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 396.4 |
| 8acdd577-51f6-3e48-83b5-c34c57afd9b1 | -7.9907 | -43.4118 | 2025-07-13 00:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b92874b1-bc15-317a-80e0-e388e2e103fe | -13.8482 | -45.8916 | 2025-07-13 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 14aee236-ae85-3a50-9a13-2f5fa08a1683 | -7.9913 | -43.3649 | 2025-07-13 00:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 179.1 |
| 3afe71a6-f35c-3d53-96c2-cc05887bdec4 | -8.0099 | -43.3864 | 2025-07-13 00:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 49e2e3cf-d1e5-37a4-a9f3-3ec7eb4714db | -8.0099 | -43.3864 | 2025-07-13 00:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 94aae872-5e9c-3f0a-84c1-c652817f69ad | -7.9907 | -43.4118 | 2025-07-13 00:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c93de526-af6d-3f11-a34d-8d31e6ca8ae9 | -7.9721 | -43.3904 | 2025-07-13 00:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 141.4 |
| d5c7f7f7-b4db-3797-8d78-90cd9f03dfb6 | -7.991 | -43.3884 | 2025-07-13 00:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 372.9 |
| 8f7733ec-eedd-3367-a8f0-faf10567ff53 | -7.9913 | -43.3649 | 2025-07-13 00:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 159.5 |
| cdf306a5-4751-3504-95f4-1b358008120c | -7.9724 | -43.3669 | 2025-07-13 00:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 4f0f2b47-c81d-32e7-8e93-5208ed5246f2 | -9.3458 | -58.8284 | 2025-07-13 00:51:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc4fa81b-cee4-3de6-9e7b-b52c106df9bc | -6.6319 | -56.274899 | 2025-07-13 00:51:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53e58eec-4854-3425-8027-f5b1a832506a | -10.0527 | -59.100899 | 2025-07-13 00:51:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b085fbe2-6b32-3b51-b4c2-64050ca6ecea | -9.0276 | -59.535999 | 2025-07-13 00:51:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46f8285f-6bc6-3269-ab32-0a4479f5fbe3 | -9.0303 | -61.214802 | 2025-07-13 00:51:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c898cea6-1ef7-3b6f-92b9-e5e061453442 | -19.090599 | -56.035702 | 2025-07-13 00:51:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72681ddf-c952-338a-bcd3-ed879e0eece7 | -19.0891 | -56.0284 | 2025-07-13 00:51:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 703bafda-d16b-3052-b4cb-6ae92df008bd | -9.026 | -59.5285 | 2025-07-13 00:51:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8c54f8e-9447-3975-bd01-4d07789c3fd3 | -7.991 | -43.3884 | 2025-07-13 01:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 305.0 |
| a1fd6a06-cda5-3918-88f4-c2b76b4a6c07 | -7.9724 | -43.3669 | 2025-07-13 01:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| 7954d7be-04ac-38e4-b0fb-aa067061643a | -7.9721 | -43.3904 | 2025-07-13 01:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 1c752fff-8820-3d1d-b632-39306e75aa26 | -7.9913 | -43.3649 | 2025-07-13 01:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| 6e3d760e-27dd-3e93-8d33-45474c04500e | -8.0099 | -43.3864 | 2025-07-13 01:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| f6237c4c-215c-355a-91eb-a35a76631cd7 | -5.739 | -44.9945 | 2025-07-13 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 7ac9b604-fe00-32c8-9894-d9f254b71bbb | -21.10847 | -49.21164 | 2025-07-13 01:00:00 | TERRA_M-M | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |


[Clique aqui para ver as próximas entradas](README2.md)
