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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26aa652e-d273-329e-b86e-7eeb75b3add8 | -13.4413 | -44.0267 | 2024-09-27 00:46:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 7ab977d9-44ae-33d4-953d-bdf716a44b33 | -13.4418 | -44.003 | 2024-09-27 00:46:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| aec9b3cc-5af7-37f7-ac70-aecb4ec8844c | -14.7109 | -45.5096 | 2024-09-27 00:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0138d5df-7d43-3d5d-b2e7-8b8808ac1bb0 | -16.3749 | -49.9223 | 2024-09-27 00:46:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| b72a6762-87a9-3ec1-95d0-f24ed8b4e704 | -19.1077 | -43.4466 | 2024-09-27 00:46:51 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 701f03d4-2a78-3e75-b687-41f39e0b3e15 | -19.6136 | -42.8159 | 2024-09-27 00:46:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 014f4bfe-4c02-30ba-b8f8-6e4bb6427d3f | -19.5266 | -47.8952 | 2024-09-27 00:46:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 118.2 |
| d94d0ec8-d59c-3cb8-a84d-1dd861947afb | -19.5272 | -47.872 | 2024-09-27 00:46:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8195eabf-b1c8-3a06-8374-61040089002d | -19.5469 | -47.8907 | 2024-09-27 00:46:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 96ad3784-3db7-34aa-9458-9cd2fd1d0f8a | -19.5476 | -47.8675 | 2024-09-27 00:46:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 737821dc-8383-37ac-8fc4-6bec99e2de6c | -21.0986 | -49.1347 | 2024-09-27 00:47:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.1 |
| ca165426-5cfa-384e-8c27-b2b5579f5067 | -21.0993 | -49.1115 | 2024-09-27 00:47:03 | GOES-16 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| 9173abb8-586c-3613-b1c8-d909f0da2121 | -22.7433 | -44.8035 | 2024-09-27 00:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 197.6 |
| 82163eaf-4f80-31c1-99f4-ad578242a545 | -22.7442 | -44.7785 | 2024-09-27 00:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.4 |
| 3233e1a9-460a-347b-a886-4be4b1f2a9e9 | -23.5816 | -47.3408 | 2024-09-27 00:47:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.1 |
| 1b3509a6-b655-314e-ad15-aeceb5b1b46c | -2.6783 | -57.5893 | 2024-09-27 00:55:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2d54fda9-6fdf-3ca2-8672-87601c4784eb | -2.8611 | -51.6699 | 2024-09-27 00:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 72187238-5a10-3443-8cdd-d0e760ab25e7 | -2.8795 | -51.6695 | 2024-09-27 00:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 8b079752-aab4-39e0-ae97-6568f27a04bc | -4.5616 | -47.9925 | 2024-09-27 00:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cee88a5e-8654-3069-82c3-e22bb86d3153 | -6.1173 | -51.1185 | 2024-09-27 00:55:41 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| eb162f3a-f12b-3319-b372-9393c2b3d7ba | -6.8015 | -63.1656 | 2024-09-27 00:55:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fa71392b-afec-3965-8e7a-d93d1ad35969 | -6.8016 | -63.1468 | 2024-09-27 00:55:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| adfd06ca-4da1-3d28-8b04-82d71d8c2c60 | -6.8199 | -63.1651 | 2024-09-27 00:55:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 172.1 |
| f417b76f-abbf-30be-8f42-669f2450302f | -6.82 | -63.1463 | 2024-09-27 00:55:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 153.5 |
| bacbe818-38c1-3d27-b8ef-e24ea07a805e | -6.8383 | -63.1645 | 2024-09-27 00:55:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| b3e7fde8-a7eb-311f-bfcb-6536111362b7 | -6.8384 | -63.1457 | 2024-09-27 00:55:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| e15c9809-04b2-3870-949e-371a1cb6b66f | -7.0912 | -46.4412 | 2024-09-27 00:55:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a583ac7c-ef34-3c59-bf7c-6002e635a820 | -7.1099 | -46.4396 | 2024-09-27 00:55:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 22dbb696-2882-364f-8fc4-c3667573abf9 | -7.2905 | -61.106 | 2024-09-27 00:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f61e52bd-a091-3700-9c02-9e38116e67af | -7.4605 | -60.4114 | 2024-09-27 00:55:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9036717c-3e3a-35a2-9229-6dc004042a68 | -7.4606 | -60.3923 | 2024-09-27 00:55:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 8cbf9816-f1ea-3cf4-b2a8-0573e56170ab | -7.4791 | -60.3915 | 2024-09-27 00:55:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e401fbde-971e-32a6-a7ac-a6d34227597c | -7.5289 | -61.3825 | 2024-09-27 00:55:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 4c7f0a2f-adfc-3e95-832d-339603f6b819 | -7.529 | -61.3635 | 2024-09-27 00:55:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d41930e8-0597-333c-8eae-105c5777e530 | -7.5703 | -60.5984 | 2024-09-27 00:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 873e75e4-0482-31c2-b3ba-9814da94e6bb | -7.5887 | -60.5976 | 2024-09-27 00:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 35a54523-e05a-3b41-a20d-8402abd933d6 | -7.5888 | -60.5785 | 2024-09-27 00:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b6cd8e6f-2e36-3b52-9c8d-b12206309326 | -7.77 | -61.2015 | 2024-09-27 00:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 22f3e444-3f93-3760-a059-c496b9d8b58d | -7.7701 | -61.1825 | 2024-09-27 00:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 9e1b41a4-e564-3b8a-b1f5-d7b542593b3b | -7.8156 | -54.7252 | 2024-09-27 00:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 5dcf7d98-afd6-3db3-bcba-cec81a860fc5 | -7.7885 | -61.2008 | 2024-09-27 00:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| edab2679-74c2-3d88-ac45-a571fcd00752 | -7.7886 | -61.1817 | 2024-09-27 00:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 80c29109-7755-3c12-8599-2cc970c399e7 | -7.9081 | -62.9976 | 2024-09-27 00:55:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 82159901-cb34-38f8-accb-788657644fa5 | -7.9174 | -61.2909 | 2024-09-27 00:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f2cd6851-e5ba-3491-aa5e-f8b0799dc57c | -7.9175 | -61.2718 | 2024-09-27 00:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8ef2ed1b-591a-3959-a663-c343785499e6 | -7.9359 | -61.2901 | 2024-09-27 00:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 645802f8-81f3-3900-ae84-e495307755c2 | -7.936 | -61.271 | 2024-09-27 00:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f6029157-f938-30a8-a170-a730767b4283 | -8.556 | -49.6112 | 2024-09-27 00:55:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| a10fc5fc-7f95-33db-b565-9fe95904f669 | -8.5562 | -49.5897 | 2024-09-27 00:55:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| c5eddd64-db30-3ec4-8787-2e8aeb147daf | -8.5748 | -49.6095 | 2024-09-27 00:55:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 06879508-c2d4-3cb4-913b-bf98d756f940 | -8.6101 | -63.1226 | 2024-09-27 00:55:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| fe07f7a0-4703-3fc1-a4ac-d39e203e55ca | -8.6286 | -63.1219 | 2024-09-27 00:55:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 03c7276b-f7b5-37e5-8145-53aa28033a44 | -8.7032 | -66.9907 | 2024-09-27 00:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 89d1bc2f-d880-3f11-aeba-2c83406a8497 | -8.7033 | -66.9721 | 2024-09-27 00:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 88cd2886-e528-3a33-a0f1-5b25e8e15f68 | -8.7218 | -66.9716 | 2024-09-27 00:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 1f26f4c0-f3c2-3351-abb7-c6e6d29a119c | -8.7219 | -66.9531 | 2024-09-27 00:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a44dc762-6877-34da-aec9-a8d3c5452254 | -8.8116 | -67.6917 | 2024-09-27 00:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 891d2481-6ba7-3e50-9a10-bebcfc600077 | -8.8117 | -67.6732 | 2024-09-27 00:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 6ffe18dd-fff9-34b0-89b3-4e0e005f5ad2 | -8.9977 | -67.3909 | 2024-09-27 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 12c7ad7b-06a6-395c-a37d-929f4e6cee2d | -8.9978 | -67.3724 | 2024-09-27 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 231.7 |
| 6a69757a-0b4c-3db9-9037-3cc9ad38ce22 | -8.9978 | -67.3538 | 2024-09-27 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| f35a9c10-bfda-314f-904e-e7125e6a04f1 | -9.0162 | -67.3904 | 2024-09-27 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d5e49486-fe8e-3e77-b1ee-2c49b44505f6 | -9.0163 | -67.3719 | 2024-09-27 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 0fc8c11e-3c99-3669-b724-10b727e3e1b8 | -9.0163 | -67.3534 | 2024-09-27 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| df0d8434-602f-3cc9-99b4-13a89f87be40 | -9.047 | -61.3943 | 2024-09-27 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 130b03eb-ec8e-3a0e-b510-e34eba722f2d | -9.0472 | -61.3752 | 2024-09-27 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7f54b34e-3e59-34c9-8407-199ede573b04 | -9.0656 | -61.3934 | 2024-09-27 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2d5dcbb7-e1a4-3357-9c7c-fd586cf260e1 | -9.0657 | -61.3743 | 2024-09-27 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a39ded86-4619-38d4-be26-223d5870c755 | -9.086 | -61.1245 | 2024-09-27 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 407549a6-5b6a-3cbb-b7f3-4e0f9ab49f21 | -9.107 | -67.8881 | 2024-09-27 00:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d64e8111-dd21-3e46-ba7a-651a47ecb093 | -9.1982 | -68.2929 | 2024-09-27 00:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 28223c23-94a9-3158-bfb4-ce8b05133c27 | -9.3763 | -65.5 | 2024-09-27 00:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 94c004ed-044e-30fe-9abe-dd77f28a9fee | -9.5829 | -50.137 | 2024-09-27 00:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 26f2bab4-f5ed-3d60-a410-346699c40f87 | -9.6018 | -50.1352 | 2024-09-27 00:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 3c1ac472-16fa-3ed0-bb1e-d994e6465eb3 | -10.3672 | -53.7858 | 2024-09-27 00:56:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 635b5ca0-4987-3048-9737-bb814fefbbad | -11.1219 | -50.8328 | 2024-09-27 00:56:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b0600934-ee05-3834-93a6-6f26e13e1e90 | -11.1349 | -54.1892 | 2024-09-27 00:56:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 4c3b5546-ed69-38bb-9558-17dc98df5306 | -12.1672 | -50.8004 | 2024-09-27 00:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 6c977039-1178-3a99-a1ec-9bfda98b6153 | -12.1859 | -50.8195 | 2024-09-27 00:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 285.6 |
| f6679918-d022-3e45-b84d-98d45dda31c8 | -12.1863 | -50.7981 | 2024-09-27 00:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 448.0 |
| ac17d3b6-e4d7-3d98-bf06-58d5cf21a50d | -12.1866 | -50.7767 | 2024-09-27 00:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 4aa6029c-f0c3-334d-bb80-ceb56a2d9dca | -12.205 | -50.8173 | 2024-09-27 00:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| a7707540-187c-3750-8582-98f6993b8cca | -12.2053 | -50.7959 | 2024-09-27 00:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 87b0bb02-84ba-38e6-8878-76ad912c696e | -12.6633 | -54.6988 | 2024-09-27 00:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 33d8abd6-93d9-33f5-863f-56bbca6d687c | -12.6636 | -54.6782 | 2024-09-27 00:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 45239b2c-afda-37c8-945f-461b1f6f5c31 | -12.6639 | -54.6577 | 2024-09-27 00:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a7f7fe5d-66b4-39fb-b406-839622e3533f | -12.6824 | -54.6968 | 2024-09-27 00:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 724f8a6e-1a1e-3120-89b1-45b2be15726d | -12.6826 | -54.6763 | 2024-09-27 00:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 56d22c3e-1599-3d40-9048-e3c7b346197f | -12.6829 | -54.6558 | 2024-09-27 00:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ba44b669-2898-3aff-b5f6-ffbdbb71fa75 | -12.8437 | -54.0422 | 2024-09-27 00:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 05846936-ba4a-3105-9407-cbb33295ca7d | -12.844 | -54.0215 | 2024-09-27 00:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 43398ec8-7cac-3604-8c6f-0b2e54ed2afe | -12.8628 | -54.0402 | 2024-09-27 00:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 89d835e2-390b-30ad-bb3f-4f31488508a1 | -12.8631 | -54.0195 | 2024-09-27 00:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| d2207aa7-096f-3716-af22-cf37d36e1da3 | -13.2345 | -45.6476 | 2024-09-27 00:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 3c5bf3f5-f4b8-3b66-a327-3b75fdad65ce | -13.4413 | -44.0267 | 2024-09-27 00:56:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 64b6c41e-0e69-306f-b8a9-67fb657803c8 | -13.4418 | -44.003 | 2024-09-27 00:56:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c2c762e9-3af2-3fad-a7c2-b6c5136e78d3 | -14.7109 | -45.5096 | 2024-09-27 00:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 7acb2343-ba43-3beb-9823-a4f9cf73709b | -14.7114 | -45.4863 | 2024-09-27 00:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b177c9c4-67c1-3127-a398-777cacf428ba | -14.7305 | -45.5061 | 2024-09-27 00:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 70864351-886d-3b71-bda2-ccd18d88c4a0 | -14.731 | -45.4827 | 2024-09-27 00:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |


[Clique aqui para ver as próximas entradas](README20.md)
