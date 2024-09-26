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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02bc5a1d-75a5-3d54-bacc-ad7b74464b95 | -14.5705 | -45.6973 | 2024-09-26 01:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| c19efa31-6e98-38b8-be93-10bb393b6b18 | -14.571 | -45.674 | 2024-09-26 01:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 38d395c9-edea-3bf2-ad58-c664c05ce790 | -14.863 | -51.5019 | 2024-09-26 01:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 871fc3b7-a78c-3bbf-b88c-d1883ea59790 | -14.8824 | -51.4992 | 2024-09-26 01:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| b92c7bcb-1bb1-3011-ae69-407835fa9908 | -14.9348 | -57.9634 | 2024-09-26 01:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 5e444a78-25cb-3764-8261-2b55c04a2875 | -16.098 | -52.0111 | 2024-09-26 01:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 05dbdd46-a307-3503-8be2-063fe99103b1 | -16.0985 | -51.9896 | 2024-09-26 01:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 04b85a8c-4579-37c3-a38f-597c02c96e47 | -17.0118 | -57.947 | 2024-09-26 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 771a81a3-3ce2-36f2-b594-af1ef7e0bbb3 | -17.0121 | -57.9266 | 2024-09-26 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.7 |
| 7070bf84-4b7f-3bca-988c-e7916573d40b | -17.0124 | -57.9062 | 2024-09-26 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| b7a8abc8-f787-3c61-bd9b-2d6af282dd96 | -17.0314 | -57.9448 | 2024-09-26 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 4ac1b2d8-6f98-3661-adb2-00b3db94de27 | -17.0317 | -57.9244 | 2024-09-26 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| f5058d43-6b99-36e9-afa8-56d98273c12a | -17.096 | -56.3576 | 2024-09-26 01:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| b53a67f5-32ca-38c3-af5a-41f066732d48 | -17.0963 | -56.3369 | 2024-09-26 01:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| f98fb284-0d8f-3dd6-b6c7-336caa3a9e8a | -17.1156 | -56.3552 | 2024-09-26 01:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| b8a6d54c-7479-34f5-abd3-2098e788e2be | -19.929 | -43.7959 | 2024-09-26 01:36:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.3 |
| f0ae9149-2b1f-39d5-8f1c-7079f1e302fd | -19.9298 | -43.7711 | 2024-09-26 01:36:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| 37939cfd-4d1b-376d-b913-ea1e1ead1dc8 | -19.9496 | -43.7904 | 2024-09-26 01:36:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.6 |
| 2054b0d6-68a8-3815-baa2-e6376a0a3af1 | -20.4197 | -41.8798 | 2024-09-26 01:36:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 086fcdf7-e5ee-3f7c-9475-dd3619624612 | -20.5876 | -51.5026 | 2024-09-26 01:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| 01e3135d-384f-3496-8c95-c347e24841a6 | -20.6074 | -51.5209 | 2024-09-26 01:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 122.6 |
| 10557a29-4730-3c48-babf-d1a1a5459c7c | -20.608 | -51.4986 | 2024-09-26 01:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 345.2 |
| 21e2e807-9c25-3d0e-a2af-be36e013ff4e | -20.6086 | -51.4762 | 2024-09-26 01:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.3 |
| 71cb01b1-56bb-3344-86df-8c26b6445f40 | -20.6284 | -51.4945 | 2024-09-26 01:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.5 |
| 11605612-d782-3924-a97d-176ae442f7e7 | -21.9374 | -48.5688 | 2024-09-26 01:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 47.5 |
| c7ef5b48-6a12-3759-80ae-6f3e99e01f0d | -21.9381 | -48.5453 | 2024-09-26 01:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 848626f9-fd89-338b-a40c-ce1756f2ec30 | -1.0553 | -53.3553 | 2024-09-26 01:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0a744cbb-29e2-3dcc-a1b7-01eba10f233f | -2.6785 | -57.531 | 2024-09-26 01:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4c3f8da3-0073-3247-bb12-05b281eae994 | -2.6968 | -57.5307 | 2024-09-26 01:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1b585516-02f1-3f07-996f-5e0a5b9ba12a | -3.3158 | -53.2122 | 2024-09-26 01:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3abbb721-fe41-3cce-8c75-949a2d715393 | -3.3342 | -53.2117 | 2024-09-26 01:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| b1697484-78e0-37ba-a357-2fefc040af23 | -3.5673 | -50.3794 | 2024-09-26 01:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 977bc8f8-b248-308f-9a05-8aaabcdb3927 | -3.7282 | -47.7266 | 2024-09-26 01:45:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| ba0133c2-944f-3a98-9b36-11e076285065 | -3.9208 | -46.4459 | 2024-09-26 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 2f6b0639-41e0-3026-a359-b19010a74402 | -6.7839 | -59.3245 | 2024-09-26 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3407fb73-50ec-3c63-be25-17bf15415477 | -6.784 | -59.3052 | 2024-09-26 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 046f942d-be23-38b9-94b6-625ea5d6934e | -6.8024 | -59.3044 | 2024-09-26 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 86e7e4b0-2a4c-3c3a-9c3a-008f860191f3 | -7.2905 | -61.106 | 2024-09-26 01:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 70f867d6-45ab-342a-a8ff-ba2b327f0d02 | -7.3636 | -55.5334 | 2024-09-26 01:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| f9c78ca2-3dca-3347-b6b6-f77f37c534e8 | -7.3637 | -55.5134 | 2024-09-26 01:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 314.0 |
| 794921e5-cdb8-315e-9040-15d9d4eb99d5 | -7.3639 | -55.4935 | 2024-09-26 01:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 216.9 |
| f576d53d-a2ad-3f5a-9e8e-f8f7a217386e | -7.3823 | -55.5124 | 2024-09-26 01:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| f1965269-a3ad-31f8-b0cc-c8e2a00bdc6a | -7.3824 | -55.4924 | 2024-09-26 01:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 4c428aa4-35aa-32eb-a2a4-43dd98f9ad40 | -7.7968 | -54.7464 | 2024-09-26 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 587ed23d-47e9-3cf7-8e8d-dc9cb69f2f64 | -7.797 | -54.7263 | 2024-09-26 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 18dbe0e6-5106-3078-a988-7962f06f407d | -7.8154 | -54.7453 | 2024-09-26 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| e472df37-5b82-3034-b588-221d5c8263e6 | -7.8156 | -54.7252 | 2024-09-26 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 8d379264-0582-388c-9d33-12d140438022 | -8.3155 | -54.9956 | 2024-09-26 01:45:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 4bbd12c8-3d5d-34d0-9b27-8a5325fba9fc | -8.7087 | -54.7881 | 2024-09-26 01:45:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| c12775cb-2b64-36f2-914e-dbdcfe83c2ce | -8.8096 | -58.2367 | 2024-09-26 01:45:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b3c82bf6-de41-3f1b-a47f-a8946b6d3881 | -8.8098 | -58.2172 | 2024-09-26 01:45:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 9a323686-e40e-3c8b-a56e-11b6c29ea92b | -8.9244 | -67.1889 | 2024-09-26 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 579335c9-052d-358a-809c-2936b6402009 | -8.968 | -62.1415 | 2024-09-26 01:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 90a1b58e-1440-311b-abbf-c00e536bb39e | -9.0468 | -61.4325 | 2024-09-26 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| bfd54bf2-0b72-3714-8c4b-cfc1fc2f8b36 | -9.0657 | -61.3743 | 2024-09-26 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 43fe4a0d-baa3-32be-b4f4-4b5dd1b2dab1 | -9.086 | -61.1245 | 2024-09-26 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 5c5ff37e-d3c8-360c-9c87-be07a1abe592 | -9.1035 | -61.2769 | 2024-09-26 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 41275de6-1967-3f48-8075-6098d0b6e18c | -9.1046 | -61.1237 | 2024-09-26 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d1c07288-0c0b-3ca3-941e-077e3f51a263 | -9.1349 | -65.564 | 2024-09-26 01:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 8bc42059-4355-3e55-a4ba-6e643554eda5 | -9.1535 | -65.5634 | 2024-09-26 01:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 04e9373c-03a3-35d3-9ccb-943c57aa2d18 | -9.3571 | -65.6315 | 2024-09-26 01:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7c9e423d-1d76-37ed-b966-7453f34ec4dc | -9.6015 | -50.1566 | 2024-09-26 01:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 3ed5bb49-6e3a-3490-924f-e80146141bf2 | -9.6018 | -50.1352 | 2024-09-26 01:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 216fa0a9-3b09-359d-814f-196f2692406d | -9.6149 | -57.7568 | 2024-09-26 01:46:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 69cea0fb-4f06-36bc-b4c9-820360ac4e47 | -10.4558 | -45.8195 | 2024-09-26 01:46:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 8619100d-3303-3705-8b46-9f7940cacf0d | -10.4562 | -45.7968 | 2024-09-26 01:46:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 59774330-3c29-317a-a392-11065ff2c60b | -10.4752 | -45.7943 | 2024-09-26 01:46:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| d4af7b71-8971-3976-a637-a9ff5864ae8a | -10.3882 | -67.8737 | 2024-09-26 01:46:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 9c65c3c2-5db3-395e-b98f-2f1d0598f29e | -10.8913 | -57.4719 | 2024-09-26 01:46:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ec535a6f-3e86-3063-9a1d-cb036f71d7a9 | -10.8915 | -57.4521 | 2024-09-26 01:46:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 688e2204-2b9e-3fe2-ab5a-f9168eee2ea9 | -10.9105 | -57.4308 | 2024-09-26 01:46:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3390ed9d-2ead-3f77-83d5-80cd979d8b80 | -11.286 | -46.278 | 2024-09-26 01:46:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| eaf492c2-833d-3a08-bc7d-d856ef416353 | -11.2034 | -54.7752 | 2024-09-26 01:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 7a425158-2bea-3576-93fb-214469b287b4 | -11.2599 | -65.299 | 2024-09-26 01:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 204b9b98-d74d-3b51-828f-6a5d48725828 | -11.26 | -65.2801 | 2024-09-26 01:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.1 |
| cf446b60-44e7-358c-8bce-c511aca77f8f | -11.5013 | -56.7677 | 2024-09-26 01:46:12 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 43c26da2-4cbd-3cac-8b66-650b27f3a895 | -11.7179 | -47.8551 | 2024-09-26 01:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 0b5c1010-39ff-3cf6-8fa1-30770d4791a9 | -11.955 | -60.363 | 2024-09-26 01:46:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 61f15182-8d97-3330-979f-176af20dd3f7 | -12.2367 | -45.5045 | 2024-09-26 01:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 789007d6-4ad1-3ae0-8017-4ea2225e75ef | -12.5085 | -53.498 | 2024-09-26 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 682fa8ef-8ea6-32ef-b01c-b69df10cb0f0 | -12.5276 | -53.496 | 2024-09-26 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 0f15ef22-5740-304a-a8d5-c6f3a3ffb1d2 | -12.8076 | -51.3423 | 2024-09-26 01:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d9f41e2e-44ed-3174-8b17-253e28c1ecdc | -12.8462 | -51.3164 | 2024-09-26 01:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 94beea44-1315-31d4-b04e-89395bd3648e | -12.822 | -62.7078 | 2024-09-26 01:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 389fbba9-c288-341c-84b2-5b52837ffe8b | -12.841 | -62.7067 | 2024-09-26 01:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 166.4 |
| c8c43b52-8b6f-31fd-afbd-1e58296563c3 | -12.8411 | -62.6874 | 2024-09-26 01:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 0fc343e0-c9f3-3d60-bff0-07ab813b99d1 | -13.2863 | -51.326 | 2024-09-26 01:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| d6a005b1-e364-385a-95c8-7f03b504f94b | -13.3052 | -51.3449 | 2024-09-26 01:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 71580156-e27b-364f-8858-de618edb116c | -13.3055 | -51.3235 | 2024-09-26 01:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 468cd85d-9f66-3c04-9e04-8f353ed07a81 | -20.6208 | -51.4865 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d30e63a3-3c1d-3adf-934d-8a0108dadff5 | -20.626301 | -51.506199 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ebe2285-e6f9-397d-995b-a6a3d5e8ca59 | -20.6057 | -51.469799 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22a2ef3e-ef32-351f-9f1a-660bb0bbc94f | -20.6112 | -51.489498 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de60f05d-c0f2-30e7-8881-c7cba99019d4 | -20.6168 | -51.509201 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2aba4471-fce7-3fe4-a894-cfd394a0d762 | -20.6222 | -51.528801 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f99969a7-77fc-3c61-a7e5-b2f6225f4fa2 | -20.590599 | -51.452999 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 417839a5-b3e8-3936-99a1-139bd17fb642 | -20.596201 | -51.472801 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d97310e-6ff7-396c-8ea2-a12235c01f3d | -20.6017 | -51.4925 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd8b23af-21b2-3766-9de6-829f83b50c31 | -20.607201 | -51.512199 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed0ea9b8-d228-39ea-890b-a8b3c3e5912a | -20.586599 | -51.475899 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README35.md)
