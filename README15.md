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
| 10f12895-2d8b-3f95-8aa0-d928f25ae0bd | -3.3341 | -53.232 | 2024-10-10 00:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 63f5d94b-ab08-3762-8a66-321995b59fd7 | -3.3342 | -53.2117 | 2024-10-10 00:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e84099d3-2db1-3249-b5f8-1a95d7dd53f3 | -3.7061 | -44.9555 | 2024-10-10 00:25:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8c98bf6e-8b57-3cc8-8416-dfba5e04377e | -3.7246 | -44.9773 | 2024-10-10 00:25:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 46a5ba5a-3cd2-334e-a107-41d96dda80a7 | -3.7247 | -44.9547 | 2024-10-10 00:25:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 158.6 |
| d930d67a-ff2b-369a-9e87-9785426b9799 | -3.8146 | -45.5143 | 2024-10-10 00:25:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| bbcd5c06-55b9-3761-b3a8-036b406ba0ce | -3.8147 | -45.4918 | 2024-10-10 00:25:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 087cfac6-59b3-35b9-a5e9-938e41bbdc57 | -4.0814 | -51.0292 | 2024-10-10 00:25:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 45f63bac-7b4c-36a6-9226-00462d756cf0 | -4.0961 | -48.2739 | 2024-10-10 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 2374c358-3d3f-33b1-aa0c-c0a4fbb1107e | -4.0962 | -48.2523 | 2024-10-10 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 5116d5ee-dbf5-342c-a085-e0ae4194ba5b | -4.0998 | -51.0285 | 2024-10-10 00:25:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 0644994a-c9ca-37c3-85b4-5d5e26c026f0 | -4.1146 | -48.2731 | 2024-10-10 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 204.5 |
| 5a006448-8185-3c2a-81a6-e74f198be246 | -4.1148 | -48.2515 | 2024-10-10 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| a20095f2-a1a9-3915-a31b-5e845103eb47 | -4.4776 | -46.5956 | 2024-10-10 00:25:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 180.8 |
| f69a0339-ad1e-3975-ab98-e5815ea505e8 | -4.4778 | -46.5735 | 2024-10-10 00:25:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 30d44f20-408c-359b-a893-16a090fe43cd | -4.9513 | -42.9973 | 2024-10-10 00:25:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 36916205-bf65-336b-8b20-69d8bb0fb800 | -4.9515 | -42.9739 | 2024-10-10 00:25:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5dfa8796-271d-3659-bcd9-4c77817e2df6 | -5.1904 | -41.2923 | 2024-10-10 00:25:35 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 6967c8f9-218b-3a49-a9df-4fe39e56a0b9 | -5.2361 | -44.8018 | 2024-10-10 00:25:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8bfe75bb-cc8f-39c8-909f-88ba311a9832 | -5.3524 | -46.612 | 2024-10-10 00:25:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 663ac3a2-6375-3687-b817-09abe406e7f5 | -5.3946 | -45.9865 | 2024-10-10 00:25:37 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| fc5c09c4-9ffd-3511-9a59-2572a5ce0a3c | -5.4833 | -44.2822 | 2024-10-10 00:25:37 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9daa987d-e725-399d-984e-68fd7d7815ce | -5.9034 | -45.4353 | 2024-10-10 00:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| b64cd603-12dc-3a4a-803a-af0bb23686a2 | -5.9036 | -45.4127 | 2024-10-10 00:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| e861d7f5-f1e3-31bb-b219-d46b25d5464f | -5.9221 | -45.434 | 2024-10-10 00:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 54599b76-907c-3fc5-9886-20b29d8b5026 | -5.9223 | -45.4114 | 2024-10-10 00:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e2a92cee-9eea-36d3-ae29-3a823224c905 | -6.5218 | -60.0649 | 2024-10-10 00:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a3c776e2-aee0-35c9-a09b-2b70b975e329 | -6.5219 | -60.0457 | 2024-10-10 00:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2dda8a16-0173-33ac-9958-fd92c308ec26 | -6.747 | -59.3259 | 2024-10-10 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5f8ba1b1-de5f-3753-b73d-a61285a6caa2 | -6.7654 | -59.3252 | 2024-10-10 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 6b319ee1-6664-303d-bd80-810aaec92732 | -6.7655 | -59.3059 | 2024-10-10 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| a44b3aa1-219b-3f58-b8bf-e70570385ad8 | -6.7798 | -60.0552 | 2024-10-10 00:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 050bdd65-ef47-35c3-8c83-c7e41b047935 | -6.7799 | -60.036 | 2024-10-10 00:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 2a326dee-aa59-3889-a081-992c04486dd4 | -6.7839 | -59.3245 | 2024-10-10 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 83806758-2def-332f-b0dc-722773fe2a0a | -6.784 | -59.3052 | 2024-10-10 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 48b2add6-661c-3fb2-a5fb-07d3f8d27b16 | -7.0416 | -59.4296 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| f75109b9-ff0d-3b3f-8b2a-5104433d0679 | -7.0417 | -59.4103 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| d9e207d9-8f28-3f29-85ff-3a723ff2022d | -7.0419 | -59.3717 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 13244d09-a22a-3c30-a9db-0b98379aa2bd | -7.06 | -59.4288 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 75e75de6-f6f0-3638-877d-b595ace326fe | -7.0601 | -59.4095 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 9f492577-4ad2-36f6-a533-ec994cb09a9e | -7.0786 | -59.4087 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e3b2a1eb-b8c8-3493-bb1e-5da8fcd7cbf7 | -7.1341 | -59.3871 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a41ffc0f-0f49-3af3-b404-c45ff8b55cd2 | -7.1342 | -59.3678 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| ba6622c7-3eba-3c24-a01d-d20294f6c033 | -7.1346 | -59.3099 | 2024-10-10 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9ef070d1-98e3-3353-b932-267523afe744 | -7.3942 | -46.1472 | 2024-10-10 00:25:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7fceaa0d-a16a-3194-b14b-5ecfbc2dbd40 | -7.5746 | -46.8 | 2024-10-10 00:25:49 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 87aebcd7-cb8a-3adc-904e-136596ab174f | -8.2325 | -61.1823 | 2024-10-10 00:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7030efeb-d545-30dd-9fc2-62a2f1aad4c2 | -8.6173 | -54.5924 | 2024-10-10 00:25:55 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 15064a1d-032d-34a2-a521-184c2aa3b4e9 | -8.6843 | -63.1009 | 2024-10-10 00:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9f84df03-286b-3479-883d-5de2d5dda958 | -8.6844 | -63.082 | 2024-10-10 00:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 35bca378-667d-3599-a3d1-0080e674ff3a | -8.7029 | -63.0813 | 2024-10-10 00:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 29bd76ac-ac8b-3bb4-bcb3-29c56fa5cfc1 | -8.7762 | -63.2295 | 2024-10-10 00:25:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 5eed511f-5636-33a2-9d5a-ca90a36ca789 | -8.9898 | -61.6261 | 2024-10-10 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a8a2482e-7028-358b-8282-df92d13718e8 | -8.9899 | -61.607 | 2024-10-10 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 84b3e3b7-f8d8-3f67-bbf2-4234af9c3c25 | -9.0084 | -61.6253 | 2024-10-10 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 084491c5-6dac-3d38-8dc2-37ddd79a60ff | -9.0085 | -61.6062 | 2024-10-10 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2c6bbb27-f7e6-3e5e-9089-90a6a2c02784 | -9.027 | -61.6244 | 2024-10-10 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| bfcf3ad9-6da0-3bcb-a30f-6108004f81ac | -9.0271 | -61.6053 | 2024-10-10 00:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| c2d2ed41-c916-3f87-ab6d-f0ff1e804779 | -9.0841 | -61.4117 | 2024-10-10 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d19fb9bf-c343-317a-981c-1927805d5b5f | -9.0842 | -61.3925 | 2024-10-10 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 3a22b9f3-8b39-38e5-994a-921672d77dc3 | -9.0857 | -61.1629 | 2024-10-10 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| bd1efcb8-5f23-3a02-8576-268920f1b1bc | -9.0859 | -61.1437 | 2024-10-10 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0ccb2064-8898-36b6-b19e-ad5aee2243af | -9.1035 | -61.2769 | 2024-10-10 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 97ea44a4-02de-3cd0-8363-7d46ed595566 | -9.122 | -61.2951 | 2024-10-10 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 905b21fa-0fef-38a0-98ad-d0353ae6837d | -9.1221 | -61.276 | 2024-10-10 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 047f10b5-69c0-3404-88da-f0c72f834982 | -9.1843 | -60.3514 | 2024-10-10 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b0ad1013-5b1b-386c-b4bb-a6d5d91230fe | -9.8551 | -60.3159 | 2024-10-10 00:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 26723204-1e2b-3022-b24d-26c4538fdceb | -10.4287 | -60.9979 | 2024-10-10 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 100c1958-6913-3056-b5ef-2e715beb6257 | -10.5746 | -48.0178 | 2024-10-10 00:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7ea451f2-9998-324b-bc03-a8eb99930d11 | -11.0252 | -57.2436 | 2024-10-10 00:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 836054fd-09b9-3c64-beab-733f7264f51f | -11.0254 | -57.2237 | 2024-10-10 00:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 258.2 |
| 5c86411c-edee-31ec-9a56-2b61f98e6c8a | -11.0256 | -57.2038 | 2024-10-10 00:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 235.7 |
| cea044f5-acc0-3664-9455-cfb9c20ca1a8 | -11.0443 | -57.2222 | 2024-10-10 00:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 309.7 |
| 9efb8d23-2591-3c41-b975-6d38265b6f5c | -11.0445 | -57.2023 | 2024-10-10 00:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 282.5 |
| 79a4d461-5962-329f-803e-809ceb977a8a | -11.5349 | -44.0324 | 2024-10-10 00:26:11 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6b75a7c2-1e83-3bae-9387-678e9dbac0ed | -11.2575 | -60.4855 | 2024-10-10 00:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6f5e07e9-f101-3153-a278-43d575d817c3 | -11.2582 | -60.4079 | 2024-10-10 00:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0d8cd103-4050-32ae-bbd9-5d01c3e6373d | -11.2583 | -60.3885 | 2024-10-10 00:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7411558e-6234-3b22-aed0-301a5d858824 | -11.277 | -60.4067 | 2024-10-10 00:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ecee1432-152b-3b70-ac07-180526c39a0e | -12.1955 | -46.7396 | 2024-10-10 00:26:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| c0ebf8d9-a5df-3bac-87d2-160e4449dbf9 | -12.1958 | -46.717 | 2024-10-10 00:26:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 4da1e4ff-613c-31bf-a951-97d4fd9ae608 | -12.2147 | -46.7369 | 2024-10-10 00:26:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 9dc0ab86-baf2-373c-abee-7f6e4958072d | -12.215 | -46.7143 | 2024-10-10 00:26:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4cfdb9fa-c5f9-3630-9aae-22b1961e042b | -12.663 | -54.7193 | 2024-10-10 00:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 408c36e5-cd36-37c2-a9d5-32c181190352 | -12.6633 | -54.6988 | 2024-10-10 00:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2dd648a4-e551-3a95-b048-a0566502f43b | -12.973 | -46.216 | 2024-10-10 00:26:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 54394bb0-a4c6-38be-9c34-57191ce0d3fb | -13.1842 | -51.7217 | 2024-10-10 00:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 56fbcdbf-5f27-3d2b-b92c-775bc2298488 | -13.1845 | -51.7004 | 2024-10-10 00:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 66e51ecb-35a0-3a30-bd22-41721090ead0 | -13.5326 | -44.2937 | 2024-10-10 00:26:22 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9beb120f-3e52-3ec0-b2b0-4a2395c4e8ec | -14.079 | -44.1483 | 2024-10-10 00:26:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b55b807a-d1c0-322a-83c8-cd4c88d72e61 | -14.0985 | -44.1447 | 2024-10-10 00:26:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 950de258-defe-34b7-9431-bfddf9d2076d | -3.2571 | -54.1824 | 2024-10-10 00:35:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d045b402-3161-302e-9900-30e4e23275ea | -3.3341 | -53.232 | 2024-10-10 00:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 148906d9-2b17-30c2-a6b3-1d66211fd18f | -3.3342 | -53.2117 | 2024-10-10 00:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2c338eed-f153-3cbe-8db7-6a95f7cca516 | -3.6793 | -50.1232 | 2024-10-10 00:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 114caa61-aabe-3ade-b6e9-cf71e798f6df | -3.706 | -44.9782 | 2024-10-10 00:35:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 139.9 |
| d2dc444e-5a88-3fa4-8be7-a34dd400458a | -3.7061 | -44.9555 | 2024-10-10 00:35:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 223.9 |
| 818f1f21-5d46-3aec-9049-c95ace21702a | -3.7246 | -44.9773 | 2024-10-10 00:35:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 413c633a-4fbe-31b8-881b-5490ac3117a0 | -3.7247 | -44.9547 | 2024-10-10 00:35:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 305.6 |
| 8dd78a29-4ff0-306e-994a-f1581e1aa41e | -3.7431 | -52.3223 | 2024-10-10 00:35:27 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |


[Clique aqui para ver as próximas entradas](README16.md)
