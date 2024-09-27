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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75960275-5e21-3c38-8269-d6b67a905731 | -8.6286 | -63.1219 | 2024-09-27 03:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 0e264b1b-317e-32c8-94ec-52412d09bf0c | -8.6285 | -63.1408 | 2024-09-27 03:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bc2d1c67-725a-35ad-8677-df95e61fe25f | -8.6101 | -63.1226 | 2024-09-27 03:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f7dd0bcb-a2f7-37e0-a1da-2b02e0b7a170 | -8.8117 | -67.6732 | 2024-09-27 03:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3406e4bd-5fd6-3ae8-a86d-7a5fbf5e9774 | -8.8116 | -67.6917 | 2024-09-27 03:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 217f93e3-b115-356e-a899-934bc9e0ef8c | -9.1032 | -61.3343 | 2024-09-27 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2b5d7f4c-d56b-3510-8e78-5ec47577cb51 | -9.103 | -61.3534 | 2024-09-27 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 420efd05-200b-375d-bbf3-6c70d56e13c0 | -9.1029 | -61.3726 | 2024-09-27 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9f3d9922-b073-36cb-b9b1-f3dbc910d5f7 | -9.0656 | -61.3934 | 2024-09-27 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d51e4d11-f315-3129-afc6-86e5106e4a02 | -9.1217 | -61.3334 | 2024-09-27 03:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3956e046-af1b-3b9f-aafd-0444efb80ab2 | -9.1216 | -61.3526 | 2024-09-27 03:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4b54f01e-f493-36f8-a0e4-afd9fc820f7e | -9.1215 | -61.3717 | 2024-09-27 03:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2003c1ba-c757-329c-8395-a340373a4dac | -9.3214 | -65.3522 | 2024-09-27 03:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b03c44d4-4e3f-3a22-bc79-dca4df7a735f | -9.3029 | -65.3341 | 2024-09-27 03:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f0dd3cf3-9bac-3545-91e9-d616d88c0705 | -9.3028 | -65.3528 | 2024-09-27 03:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 5c0a72d4-2595-3470-9b05-c7cc6cd0608a | -9.602 | -50.1139 | 2024-09-27 03:06:01 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 8ade09bc-b932-3e3a-8b01-2d7b8e1e425a | -9.6018 | -50.1352 | 2024-09-27 03:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 296.2 |
| 0b87c6e5-e98c-3cd8-a038-1135e63847fa | -9.5832 | -50.1157 | 2024-09-27 03:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 84a9b5b1-bb87-3d59-8b5d-6c6089806911 | -9.5829 | -50.137 | 2024-09-27 03:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 204.4 |
| 7a3ffd84-aae4-3fe3-911d-3024967f55a5 | -10.1312 | -49.9976 | 2024-09-27 03:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3e94ee0e-af46-3bdf-a01c-31bc51045933 | -10.1309 | -50.019 | 2024-09-27 03:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 42a9d23a-9b01-3d88-8713-ad1453f57b59 | -10.3672 | -53.7858 | 2024-09-27 03:06:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| ab2c2201-38c7-3142-93bd-ee0274a77f9f | -10.7036 | -50.9828 | 2024-09-27 03:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9cf16441-8c24-3758-93ea-561fed19d71d | -10.6846 | -50.9847 | 2024-09-27 03:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c4153cb5-6984-3530-b8ff-6bfe745b2b97 | -10.9267 | -54.2488 | 2024-09-27 03:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 9f2d635f-f70f-3d1a-99ea-25d8fda2e114 | -10.9264 | -54.2692 | 2024-09-27 03:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 8225e98f-8c60-3fd2-b5d9-5aa8f63d2d54 | -10.9453 | -54.2676 | 2024-09-27 03:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 1ef80c88-71d2-3654-86bb-4fde97af94ad | -10.9456 | -54.2471 | 2024-09-27 03:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 96c6de99-85b9-3659-8b1f-59d5758ab51a | -11.2538 | -47.0918 | 2024-09-27 03:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 91044b19-147b-3b28-8a08-d86a76068a2d | -11.2534 | -47.1142 | 2024-09-27 03:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 364.5 |
| 454b2b8e-5e68-39f8-b937-ed42a798250e | -11.2531 | -47.1366 | 2024-09-27 03:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 89a4102a-2f51-36b5-bb47-3dd902b57dd2 | -11.2343 | -47.1166 | 2024-09-27 03:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 155.6 |
| e049fc77-140b-3270-870d-6bf9a502cae3 | -11.2223 | -54.7735 | 2024-09-27 03:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3a63232e-d1e5-39a4-8b08-50a32cb8a2c3 | -11.2725 | -47.1117 | 2024-09-27 03:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 4da6fc79-3405-3b28-95a0-731bee8fe57b | -11.234 | -47.139 | 2024-09-27 03:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 6268b116-1aed-35b4-a5e7-e0ee6e636765 | -12.1668 | -50.8218 | 2024-09-27 03:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 0f069d26-e110-3585-916a-0dd9d8b367f9 | -12.1672 | -50.8004 | 2024-09-27 03:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| c8c2eb71-66e4-3c5b-9f01-eed99f938d44 | -12.1856 | -50.8409 | 2024-09-27 03:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 43726704-a810-32be-9507-929ec0c8b5bc | -12.1859 | -50.8195 | 2024-09-27 03:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 295.4 |
| f54c3de9-3279-3678-bdcb-3f5e65444c4d | -12.1863 | -50.7981 | 2024-09-27 03:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 216.2 |
| b7329cf5-908c-34c4-8d50-261b926f7afd | -12.6824 | -54.6968 | 2024-09-27 03:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d95d323c-b200-3b59-8564-ce6c833a71e0 | -12.7014 | -54.6949 | 2024-09-27 03:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 571fd734-cdc8-3346-ab86-1c6fd69d0312 | -14.941 | -51.4695 | 2024-09-27 03:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 795d2eb4-c538-3cab-8a44-44a7963fc25d | -14.9414 | -51.448 | 2024-09-27 03:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 313600d9-5863-3702-aafa-48ca93f7281d | -16.893 | -58.0417 | 2024-09-27 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 8baeeabf-634c-3ee6-8b99-5195c7037b26 | -16.8933 | -58.0213 | 2024-09-27 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 20620782-f084-3a46-b460-31bb4aff7fa3 | -19.2991 | -49.6765 | 2024-09-27 03:06:53 | GOES-16 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f2f544b4-18bb-3c07-8211-250ed08fbd7d | -19.3977 | -42.5753 | 2024-09-27 03:06:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.0 |
| be2a1516-7205-35c6-8e43-4f1963bc4438 | -19.378 | -42.5556 | 2024-09-27 03:06:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 0a3bcd74-2a63-320a-aff2-a794c391f894 | -19.3773 | -42.5809 | 2024-09-27 03:06:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| 199bddef-bf96-31ec-9877-3b741ca80353 | -19.6342 | -42.8103 | 2024-09-27 03:06:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| f1ed95f5-ac79-33b0-9dbe-c4101e703811 | -19.6136 | -42.8159 | 2024-09-27 03:06:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.6 |
| 83b2b470-66a1-3762-9036-93ba994bf6bd | -21.0665 | -48.8196 | 2024-09-27 03:07:02 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.7 |
| ed05d312-6eed-31a7-84aa-01b2c927a193 | -21.0658 | -48.8428 | 2024-09-27 03:07:02 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| 51206cba-200d-389c-bd5c-38276c1fca5f | -21.0871 | -48.8149 | 2024-09-27 03:07:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| ecd0512f-3240-3649-8ca2-a221856ed26b | -21.0865 | -48.8381 | 2024-09-27 03:07:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.9 |
| 59f0baba-3fe7-3e6c-b1eb-3c11fcc945c5 | -22.7433 | -44.8035 | 2024-09-27 03:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.8 |
| a5599ed8-4c57-33dc-9ddc-991b0aa97d99 | -22.7442 | -44.7785 | 2024-09-27 03:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.1 |
| 29582f23-8b7a-3060-aba0-eec5cdd6d856 | -2.358 | -47.5989 | 2024-09-27 03:15:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| b102d36c-4752-3829-b43e-1bfd6d1b0ace | -2.3579 | -47.6206 | 2024-09-27 03:15:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 15976a4a-82b8-3700-95fc-b282920ee56f | -2.8611 | -51.6699 | 2024-09-27 03:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ef61c5ef-748d-3d0b-8cb0-7cd749e9fe1f | -3.0107 | -51.0652 | 2024-09-27 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 1bc2629f-6e26-3c00-a6dd-1677878fd0a6 | -2.8795 | -51.6695 | 2024-09-27 03:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 43e4728f-a6a6-39f7-966f-aa67b816fb4c | -3.2321 | -46.7836 | 2024-09-27 03:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f5543d15-4778-399c-a2d4-a724df6a006c | -3.2136 | -46.7843 | 2024-09-27 03:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 748e8805-cae2-3ac6-8cd2-bc4ebde251cf | -5.397 | -43.4332 | 2024-09-27 03:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 37e9ff8a-7b88-34cb-b4d7-1703a8c87946 | -7.5887 | -60.5976 | 2024-09-27 03:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 007a1f9a-cfbc-3ed6-917d-574a0ab8c594 | -7.8156 | -54.7252 | 2024-09-27 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ac2f353b-bce7-3bb0-b916-670d6c949972 | -8.4831 | -62.6549 | 2024-09-27 03:15:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| d95a9e15-5ca8-3cab-83ec-02130f99aedb | -8.6286 | -63.1219 | 2024-09-27 03:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| a65e150d-2ada-345a-881b-b51e00b6ed89 | -8.6101 | -63.1226 | 2024-09-27 03:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f9aaf334-dafe-39dd-93a9-ac25ceff1266 | -9.1032 | -61.3343 | 2024-09-27 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| be1b825e-a116-3c13-8f58-645506760d69 | -9.103 | -61.3534 | 2024-09-27 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 71354aa3-6c05-3830-87e3-742163a7be01 | -9.1029 | -61.3726 | 2024-09-27 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 00986d45-73a9-3d7b-a4c9-ce46474c1bcb | -9.1216 | -61.3526 | 2024-09-27 03:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 41139a64-23f8-3903-9107-c4b243dc5440 | -9.1215 | -61.3717 | 2024-09-27 03:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b5b8f82e-1347-34c5-9498-73879f613da6 | -9.3672 | -63.6972 | 2024-09-27 03:16:00 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f3cd615a-c204-32af-80bf-03eb1327cc49 | -9.417 | -51.4426 | 2024-09-27 03:16:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6e6a4e0c-4fee-3b48-be25-228dc3d3f80d | -9.3029 | -65.3341 | 2024-09-27 03:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b8ff49e6-c4fb-327e-ae79-5c88ed514627 | -9.3028 | -65.3528 | 2024-09-27 03:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 74450e26-f7c3-306f-8298-39301ddbe41e | -9.602 | -50.1139 | 2024-09-27 03:16:01 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| eefe4cd6-c20c-3329-8654-ae61606e964a | -9.6018 | -50.1352 | 2024-09-27 03:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 245.0 |
| 48eab4f7-8702-35a3-a6da-ab1c34145682 | -9.5832 | -50.1157 | 2024-09-27 03:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| fb5440f2-47ed-3dba-8989-f5853fa7ec5e | -9.5829 | -50.137 | 2024-09-27 03:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 07e54ba3-d4ec-33bd-8951-d5ceac9b9879 | -10.1312 | -49.9976 | 2024-09-27 03:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 83b68616-71ee-3943-a7e3-9ef5046cd12c | -10.3672 | -53.7858 | 2024-09-27 03:16:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| b57d4da9-ee14-3f01-974e-9e8848063128 | -10.9267 | -54.2488 | 2024-09-27 03:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 51ce4355-657a-34ad-8ac4-e60c963ca7fd | -10.9264 | -54.2692 | 2024-09-27 03:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 158.4 |
| bfda6a3c-b471-3867-adce-400137f18541 | -11.2534 | -47.1142 | 2024-09-27 03:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 296b03c1-79c4-3909-b717-13c0a20dc888 | -11.2725 | -47.1117 | 2024-09-27 03:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cf9d85c7-aa8f-3862-ab31-6a0539c1e3b3 | -11.2538 | -47.0918 | 2024-09-27 03:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 65c245eb-04ee-3f83-a62b-feba38ee7a88 | -11.2531 | -47.1366 | 2024-09-27 03:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| be922386-65c1-3a4d-a386-8f704c13d57b | -11.2343 | -47.1166 | 2024-09-27 03:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 332138f0-ff4d-3f21-837e-612c36c64735 | -12.6824 | -54.6968 | 2024-09-27 03:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9c22ce6b-71f2-3006-ad5e-37feca22099f | -14.9414 | -51.448 | 2024-09-27 03:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| a1388ae8-fc89-3552-8352-4e3a2b8dd8d5 | -14.941 | -51.4695 | 2024-09-27 03:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| f8ee4772-ec2e-348f-ae09-fb25dd492cd5 | -14.922 | -51.4507 | 2024-09-27 03:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 9dbc136f-84b8-397d-887d-bd916532276d | -14.9216 | -51.4722 | 2024-09-27 03:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 05859232-6b3d-3735-b267-8e0da6c7761b | -16.3749 | -49.9223 | 2024-09-27 03:16:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 66273c8f-db02-3367-9398-d3fe61e32316 | -16.3552 | -49.9256 | 2024-09-27 03:16:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 149.2 |


[Clique aqui para ver as próximas entradas](README47.md)
