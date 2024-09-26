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
| 11923f58-a056-3791-91e0-11561f092f3c | -21.91 | -48.57 | 2024-09-26 00:03:20 | MSG-03 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0d93d7cf-ce11-3dfc-bab6-9c305664181e | -20.6 | -51.49 | 2024-09-26 00:03:28 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a08f7ed-a4a4-3fed-aa76-fa9e2705b5f3 | -16.82 | -57.73 | 2024-09-26 00:03:49 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05d74c38-5377-393c-a6da-243f2c77a964 | -10.04 | -53.48 | 2024-09-26 00:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2935af25-d5e3-3719-b60e-b171ada17a5c | -1.0369 | -53.3555 | 2024-09-26 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 1a0d2fbb-2d8c-3f9d-86d2-3bacbd3eb7bf | -1.0553 | -53.3553 | 2024-09-26 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| e02c3748-7731-3ca8-acbd-a6a1e2593892 | -2.6496 | -54.6172 | 2024-09-26 00:05:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 84fd5da0-bb97-3e32-abb2-44f4e8f7f218 | -2.6601 | -57.5507 | 2024-09-26 00:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5c4f9f24-64e5-36d4-8ab8-3505d036653b | -2.6602 | -57.5313 | 2024-09-26 00:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7fe4ffee-f5af-307a-a090-6bf0c71b2880 | -2.6679 | -54.6168 | 2024-09-26 00:05:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 29dc536c-caa7-3183-a868-98531a524366 | -2.6785 | -57.531 | 2024-09-26 00:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4bc45534-306b-351c-a777-cdd15d562c5c | -2.6968 | -57.5307 | 2024-09-26 00:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9a871d3e-2b22-3385-87da-43380ad4e3b0 | -2.7315 | -46.7568 | 2024-09-26 00:05:22 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| d18b8d23-d7c7-367b-aed2-7ce2e94818a1 | -3.3505 | -53.7775 | 2024-09-26 00:05:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 5dab8382-3873-3763-a638-5b583d7511e6 | -3.9023 | -46.4467 | 2024-09-26 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d9782e69-444d-344f-9369-71a3f7b22746 | -3.9208 | -46.4459 | 2024-09-26 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 2bae43a8-3c9d-398b-aae5-8fc0c396f203 | -5.212 | -47.9577 | 2024-09-26 00:05:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fb60282f-290f-356c-84ba-dfb8089a6903 | -5.2306 | -47.9566 | 2024-09-26 00:05:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0707284e-14ee-37e3-8b18-d465fccecf5d | -6.5772 | -60.0437 | 2024-09-26 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e6ce059f-89ba-3ef1-a1eb-b82a07c3271b | -6.7902 | -44.7296 | 2024-09-26 00:05:44 | GOES-16 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2187591a-93ad-3345-bfbe-5e445b54ee66 | -6.784 | -59.3052 | 2024-09-26 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 62b3774e-ec0c-33f8-bf35-4b27faeca2f9 | -6.8023 | -59.3237 | 2024-09-26 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 07d0ce1e-73c8-3933-b87f-21e896723858 | -6.8024 | -59.3044 | 2024-09-26 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 20563eaa-450b-3681-9643-93bcd19cbf22 | -6.8384 | -63.1457 | 2024-09-26 00:05:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 9055512d-e020-3a79-a172-45d94bed7048 | -6.8385 | -63.1269 | 2024-09-26 00:05:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 96a1c445-d696-3424-9748-49d49a7c80f8 | -6.9305 | -63.1241 | 2024-09-26 00:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 75d64fc8-a307-3e16-85ab-8f706141421c | -6.9306 | -63.1053 | 2024-09-26 00:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ee49ed35-094b-336b-a7cb-a7d189e8c951 | -6.949 | -63.1048 | 2024-09-26 00:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 141cc028-e96c-37f9-a9bb-5e5819621bb4 | -6.9681 | -62.9349 | 2024-09-26 00:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 2841d643-6fa4-3ffd-994a-a711c74ae0ef | -6.9682 | -62.916 | 2024-09-26 00:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| edca1375-75cc-30bd-bc27-8117335240b4 | -7.0912 | -46.4412 | 2024-09-26 00:05:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 65598eb9-f585-329e-ba0f-ad6ad2cd9dd1 | -7.2905 | -61.106 | 2024-09-26 00:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| fe4e8ef7-b095-3dd9-8706-b31ae78fa1fe | -7.3637 | -55.5134 | 2024-09-26 00:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 9b263eef-46a9-3806-82e9-b4832a3d1108 | -7.3639 | -55.4935 | 2024-09-26 00:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 0aacd11e-a2d0-3ad9-877b-c4a05e7c2f14 | -7.3823 | -55.5124 | 2024-09-26 00:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 76db169f-95eb-3202-acb8-015255de413b | -7.3824 | -55.4924 | 2024-09-26 00:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| b56a990d-9296-37b9-8bc3-837595dd7b65 | -7.5705 | -55.1617 | 2024-09-26 00:05:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4303734c-dd07-3a33-97e6-22f147c4323c | -7.6075 | -55.1796 | 2024-09-26 00:05:50 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 13c3177a-9864-35b3-adb7-cbda9824c971 | -22.6117 | -42.1437 | 2024-09-26 00:05:50 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5091aec-276f-3be3-ac5c-51c4c9a4a2ad | -22.6143 | -42.158199 | 2024-09-26 00:05:50 | METOP-C | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24231586-696a-3134-8695-bb7d66d35533 | -22.601999 | -42.145699 | 2024-09-26 00:05:50 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 29bcd1ac-5459-3503-99bb-0d12b9722838 | -22.6045 | -42.160099 | 2024-09-26 00:05:50 | METOP-C | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae0fb4c2-f343-3352-a6f7-ca871b973a27 | -7.797 | -54.7263 | 2024-09-26 00:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 0f4cf9ae-e10a-3776-9d53-a6320d78a579 | -7.8154 | -54.7453 | 2024-09-26 00:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| a5590c26-e529-3644-92bc-2e408c2af001 | -7.8156 | -54.7252 | 2024-09-26 00:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 647a1601-521f-3f70-9cd1-03a400e6c35b | -8.1572 | -61.3953 | 2024-09-26 00:05:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 22e0b9a0-bfea-348b-9897-274ea4a3c19a | -8.1757 | -61.3946 | 2024-09-26 00:05:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7846b1b5-d80d-3451-9622-9d52024c643f | -8.3153 | -55.0157 | 2024-09-26 00:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| f1d70e45-9f4f-3447-990c-26f9483386f8 | -8.3155 | -54.9956 | 2024-09-26 00:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 0f1d334f-53bd-3485-8499-5c2f23a77faa | -8.5187 | -55.1834 | 2024-09-26 00:05:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| fab2be1d-e584-346c-bc97-2b005f4a1151 | -8.5735 | -51.4506 | 2024-09-26 00:05:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a2b019de-3634-32e5-8dba-05e8592e93c1 | -8.5737 | -51.4296 | 2024-09-26 00:05:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 967ec1ee-6965-30aa-bc81-47e9bccf7cdc | -8.592 | -51.47 | 2024-09-26 00:05:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6affb37b-f41b-3671-b1d7-027f8bb66e44 | -8.5922 | -51.4491 | 2024-09-26 00:05:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 179.8 |
| fe884a78-0c89-33b8-b806-afdbf6096cf2 | -8.5925 | -51.4281 | 2024-09-26 00:05:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| bfe6822e-9266-3a41-a00e-9830156920e6 | -8.611 | -51.4476 | 2024-09-26 00:05:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b2f34a4c-c96c-3e37-920b-7071e09899a9 | -8.5542 | -63.1814 | 2024-09-26 00:05:55 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 43b8b38d-5939-3623-96ed-0801e1afa0ad | -8.7085 | -54.8083 | 2024-09-26 00:05:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| b8321a51-3f65-313b-87e7-21b7a83ed668 | -8.7087 | -54.7881 | 2024-09-26 00:05:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 71253343-19c0-3f47-8b5d-f8dffe5dbe6d | -8.7272 | -54.807 | 2024-09-26 00:05:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| f0b4b50e-d528-3664-b03d-ab86736743d6 | -8.7274 | -54.7868 | 2024-09-26 00:05:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 0f626b44-4efa-35bf-aaa3-8ca775de896b | -8.8098 | -58.2172 | 2024-09-26 00:05:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 98729a7d-a499-347e-b0a8-f7db2d14d930 | -8.8292 | -63.7179 | 2024-09-26 00:05:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 873931de-f79e-3fab-864c-cd45373ea01d | -8.8293 | -63.699 | 2024-09-26 00:05:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| f67a53f4-39f8-3533-afdf-85ac87e5ab58 | -8.968 | -62.1415 | 2024-09-26 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c6d1f185-bdab-3d67-8c14-4a90392ac928 | -9.0536 | -60.435 | 2024-09-26 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 04ab2527-e874-3e51-891f-89d1137de072 | -9.0657 | -61.3743 | 2024-09-26 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f72ae60b-1646-3031-9285-bee3f7086d0b | -9.086 | -61.1245 | 2024-09-26 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 87a5c948-da68-3836-8de2-7b48d964f6fe | -9.1046 | -61.1237 | 2024-09-26 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| a8299c91-29ec-356f-85ce-f7681c8ecb80 | -9.6117 | -35.8287 | 2024-09-26 00:05:59 | GOES-16 | SANTA LUZIA DO NORTE | ALAGOAS | Brasil | 2707909 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| 61825ffb-76e5-3d49-b133-9fb3764c202c | -9.2888 | -64.4534 | 2024-09-26 00:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f7d32b87-471d-3847-951e-06562b36786b | -9.3801 | -56.8631 | 2024-09-26 00:06:00 | GOES-16 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a867b969-6ded-31e5-97f1-45b3b211980f | -22.8659 | -47.801601 | 2024-09-26 00:06:00 | METOP-C | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79eb8001-030c-394b-acc9-5f7b4d881fad | -9.5827 | -50.1584 | 2024-09-26 00:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 67f66960-a12c-3e68-a29d-6c2b85b6be46 | -9.6015 | -50.1566 | 2024-09-26 00:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 180.3 |
| 65e53e5b-1423-3b49-aaa1-cb5b0adb5989 | -9.6018 | -50.1352 | 2024-09-26 00:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| df6aaf6b-25c7-31c9-bfd8-0bce0df1d2f8 | -9.5594 | -66.0359 | 2024-09-26 00:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 64e4cbdb-53e9-3698-b17d-17f51d98a2ed | -9.5595 | -66.0172 | 2024-09-26 00:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| b9858631-def7-351f-bcfe-9c4506bcfdc0 | -22.8563 | -47.803001 | 2024-09-26 00:06:01 | METOP-C | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d1e69ba-ed24-3720-a546-b7ff837b6084 | -9.806 | -53.5664 | 2024-09-26 00:06:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 4b9229d8-6108-3bd8-a80e-83fb48b9f790 | -9.8083 | -68.8152 | 2024-09-26 00:06:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2ef9381c-f5f4-3f31-875e-6d85ab74205b | -9.8269 | -68.8148 | 2024-09-26 00:06:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 17eee12d-d804-3ad0-b472-69f6713a1327 | -10.0506 | -68.5875 | 2024-09-26 00:06:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3cd4ab5b-77ab-3285-b2cb-e72ee08a3bfd | -10.0692 | -68.5871 | 2024-09-26 00:06:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 73c929bb-9664-38e6-ae54-f6736af87b1b | -10.3526 | -58.9068 | 2024-09-26 00:06:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| ac1a65ab-40a1-3146-8bcb-c44d84ad8924 | -10.3713 | -58.9056 | 2024-09-26 00:06:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 6cbb504d-0f44-38bc-8022-d511f7126c95 | -10.6265 | -45.8432 | 2024-09-26 00:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 8ec791d6-1127-36ca-8407-ccfa634a0f60 | -10.39 | -58.9044 | 2024-09-26 00:06:06 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9ea253f7-7d38-30f9-9b49-e934b776303d | -10.3902 | -58.8848 | 2024-09-26 00:06:06 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 27e4ae02-b125-3e31-a683-552d433b5576 | -10.3882 | -67.8737 | 2024-09-26 00:06:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 95.5 |
| f4b3421c-ef49-3aaf-aeb2-655f783c883b | -10.4068 | -67.8732 | 2024-09-26 00:06:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 42f450a2-0e61-3e71-8060-e6f8ad6c40a7 | -10.8352 | -45.8843 | 2024-09-26 00:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 0f411179-9003-3fc4-98d7-52dbf1407654 | -10.9924 | -44.4383 | 2024-09-26 00:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 366e010f-3963-3ae5-bd1d-dc8d29d10652 | -10.9928 | -44.415 | 2024-09-26 00:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 2b5a163a-6b41-3492-b0ff-6f43439024c0 | -10.9264 | -54.2692 | 2024-09-26 00:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 8c974805-7322-3961-9c6a-0f544dbefbd7 | -11.0569 | -51.4328 | 2024-09-26 00:06:09 | GOES-16 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 0632470a-c543-362c-8b50-448415afff5f | -11.0758 | -51.4308 | 2024-09-26 00:06:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 8a1bea48-dc9d-368b-89b4-0e8c22ce659c | -11.2034 | -54.7752 | 2024-09-26 00:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 8fac6ba1-fd0d-3d64-81dd-fe6cfd311334 | -11.2412 | -65.2997 | 2024-09-26 00:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 61001aa9-0568-34f3-a8e6-6de7e6ef107e | -11.2413 | -65.2809 | 2024-09-26 00:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |


[Clique aqui para ver as próximas entradas](README2.md)
