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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7999a8d1-6971-33b7-82b9-b896decad8c1 | -8.2142 | -61.39476 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2ef3c41-559f-339f-a165-de314f7250a4 | -4.11223 | -56.34268 | 2025-08-27 05:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f586cade-d305-3e48-9fcc-1c21cf01b1e0 | -6.704 | -58.56458 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1efa438b-2231-3d22-a4c7-600ba48073d0 | -7.56273 | -63.85493 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 577f99ae-1e13-3666-933f-908dd86c4091 | -8.6545 | -67.26875 | 2025-08-27 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8a8f86f4-6de7-3b36-8f7c-85c99ca6505b | -7.1784 | -59.73909 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24073204-b57b-3e35-9a2a-90d76aad0e80 | -8.4609 | -64.04724 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e60887a-33fe-3f99-9eb3-8d06d106c59c | -8.85876 | -62.44742 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91bd69d6-27c6-322c-a585-c92af8cd446c | -9.15025 | -60.78383 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7de7dc9a-fa79-3ef1-ba38-2b3a8669cf0a | -9.40632 | -60.50126 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f28ced92-9354-3f90-8883-d1e4b331b0cf | -9.58357 | -55.38432 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c40239a-50d2-3e7f-9a0e-2f9bce09c6d8 | -3.39291 | -59.45912 | 2025-08-27 05:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae3e4112-5e8d-3c0f-a35e-d67425cd0cd0 | -7.91942 | -67.23357 | 2025-08-27 05:44:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9f91b3ff-b57b-36f0-bc19-554e63c765d6 | -7.48229 | -61.36325 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62128da6-4f55-3d35-939b-a680b53b7ca4 | -7.35305 | -57.62776 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7b7f20a-7a56-31fc-9b60-183279699c23 | -5.62067 | -60.24207 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6b63e3a-9c1a-37b5-8b9e-65ebff537dce | -9.40578 | -60.505 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 85d7dea8-4c09-33ed-abbf-b9196855ded5 | -9.16422 | -59.54131 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51970162-fd7d-3556-a09b-6b92d61af570 | -8.65169 | -67.26453 | 2025-08-27 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9d5d6a4-0667-30f1-9eb2-f0f47f449367 | -8.53599 | -62.66574 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03fabaad-79d0-31d7-8a86-f98a2b10b10b | -6.23857 | -60.0099 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a13309fb-0ab3-390e-b26e-864c35050949 | -9.40658 | -62.49185 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9b9ff29-9e78-3b44-ac6c-1b85ca35b9a2 | -9.52692 | -60.52945 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27179ebf-befd-3234-b2bc-19e03a4555d1 | -9.41736 | -60.52871 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 889a62f9-c1cb-3c93-9175-45db4f41908f | -8.88892 | -60.76114 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69a44c76-1bf6-393c-b465-096e2a7219dc | -9.41839 | -60.52127 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed6648f5-0110-3f26-afb5-882ec0a498ee | -7.47319 | -61.33114 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d7423ec-ff9e-3683-8d52-6aa942e8a21a | -7.71248 | -61.12226 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a974027a-1d1f-3392-a6a4-f0ef48c1ad1e | -7.47558 | -61.34113 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97926124-8c2f-3fe7-a8b5-309b824e1c09 | -8.59767 | -63.86367 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db43f85f-1643-310a-a43c-790eb37f6696 | -7.74605 | -61.08484 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ede3caf-3599-39f7-b814-ade72c31f20c | -4.96007 | -55.81843 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 303b768a-3302-3497-9ed1-792ec999ba9e | -9.18981 | -59.51873 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38a07a83-b03d-3c05-ba69-4b17e26aa1ee | -8.95297 | -64.13661 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dfb9562-dac1-3de7-a394-76f13ce2de78 | -9.52868 | -60.52876 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6597d2c2-56d2-3478-a1db-d46a39e62025 | -9.40937 | -60.50933 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 937d0b64-2627-3033-8212-22e38d8dddbe | -9.41994 | -60.54051 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac60386a-05eb-3d13-a6a4-25ae0befd46b | -7.39954 | -64.34679 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4f5c8eb-b431-3daa-a615-8ce4c198cdca | -6.68176 | -58.85864 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0f7fab4-d86c-370f-965c-0305a6cd916f | -7.36054 | -59.66816 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e03b798-a40a-34d6-b455-457c341c6329 | -8.86972 | -62.44907 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca7b9f19-f768-39e2-99b6-e84c27807699 | -9.17616 | -59.45512 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 187dc1f1-7f11-3519-8393-a6e798e629d2 | -9.16838 | -59.51127 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a54387a-72f2-380e-812c-7fc897823e00 | -9.40668 | -60.52789 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 632c67c7-a23b-33bf-aa4e-34150926a19c | -9.18839 | -60.80842 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9e10492f-9e1b-346c-864d-8f7f5b420c20 | -6.93727 | -59.56268 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 060a8787-ef33-3ee3-849c-58e07006b6bc | -8.90707 | -60.77817 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8421030-030f-3e19-b583-6992d0c35544 | -5.35758 | -60.40054 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0250af58-ac69-307c-a968-6c854b474632 | -5.79372 | -59.21195 | 2025-08-27 05:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6cfd6e9-b3c4-3d8f-8497-ab464a365be7 | -7.54683 | -63.84498 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53e3ece8-512b-318c-ba94-7b94fc75a9cd | -8.88387 | -60.7676 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1959dc-b51d-32fc-823f-9f48d254e8f6 | -9.41633 | -60.53617 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02513768-46e9-313a-bd4f-53e59c0e31a8 | -7.47303 | -61.40003 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f20ec72-ee48-30c3-8074-23f976c1e8ec | -8.57573 | -62.60219 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fec51a42-4f85-34fc-bc0c-080fa916fa60 | -6.8219 | -58.97345 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be2551ad-42d9-3224-ad9e-0466192b3d69 | -8.35087 | -62.93404 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cd7049b-52c9-374c-bdaa-d6f712086993 | -9.16561 | -59.5635 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4b59bb26-d09f-39d8-b8c3-f28b0665409c | -9.40595 | -62.49616 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b64aeac5-5bc5-3407-8f64-b20a65a4f328 | -8.96615 | -62.14249 | 2025-08-27 05:44:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49f1abfb-fd71-3dac-a519-1674766f7f7e | -8.89648 | -60.76587 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea810439-2e5d-39af-ab04-08853ef2ec4c | -9.39798 | -62.49932 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c0db3aa-b13f-3138-ab20-f9a9b84573a9 | -8.07566 | -61.54889 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5531f8d-1f02-3946-8603-14efeefe2c4b | -6.23449 | -60.00928 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a365877b-bf5d-3aa9-8dc9-3e397f579d7c | -9.17659 | -59.51691 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 256869d4-edcb-3d9f-b133-8200725c21bc | -7.34412 | -59.6618 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee972018-0df9-34cd-9fe2-042af610167f | -8.55428 | -63.94052 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83b8617d-7e81-319e-924f-45b838cb88b1 | -9.27917 | -56.91061 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c3e9951-c50c-31d4-98f0-ceeada59a288 | -7.6614 | -62.54371 | 2025-08-27 05:44:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a25e01b-3433-381e-aaca-24e1f04261b7 | -6.79314 | -59.63838 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8243be08-b7bf-3c47-b3a1-e017cb395010 | -9.17363 | -60.76537 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8beec9fb-787d-307e-9f29-70ce70156d36 | -9.22127 | -59.67469 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6417300-53de-34bc-ab5f-e32e1e025690 | -3.39345 | -59.45557 | 2025-08-27 05:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a3ccbec-6c7c-3c54-8c2a-4e20903f441d | -6.76816 | -59.66243 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8237cba-b6c8-30e8-95c1-0e051cc1f05e | -9.16061 | -59.56728 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66e9ee3f-3a09-3499-9635-7beea8586614 | -7.36799 | -70.1489 | 2025-08-27 05:44:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0f53df-ac11-3b7b-94e9-b70086aa9066 | -9.27899 | -56.90718 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5796c890-e7f4-35a4-851b-5878a05832a8 | -7.46637 | -61.40176 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a0aae81-041d-3150-bb7e-010b5f262af5 | -7.35004 | -57.62825 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b51096ec-ab06-3dda-b399-fc297c2c8c6e | -8.06805 | -61.54781 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe2c865e-712d-3953-8fd7-748caa9d49f7 | -9.15626 | -59.56641 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f70cfead-905b-3b3c-9cf6-0e5fd114c1fd | -5.7602 | -53.776 | 2025-08-27 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f1f2246-947c-30e7-8dd5-3af5ff14c42f | -9.41851 | -60.53345 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c325aaa8-9e34-33b3-80e1-48a15e10f931 | -8.95354 | -64.13293 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67856b60-3066-3f69-8854-a4eb281f06e6 | -7.62338 | -61.37696 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87faa127-2810-393f-a257-b52852acbc28 | -8.07635 | -61.54429 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e443547-b111-3fa6-b814-6609973e7d1b | -6.91794 | -59.36388 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc19d663-c365-3e8a-bd7a-6c819151b9d8 | -6.7022 | -58.55263 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5b1ca34-4bb1-30e6-ae79-1487085b9928 | -9.57376 | -55.38155 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e3d9427-5cd2-32f5-a6c1-ca1e0bff11a8 | -9.39896 | -60.52299 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38df3f4b-93ab-3d40-8bd9-c76b20d87ebd | -9.23134 | -60.82537 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f74a7de3-a0f5-37cf-aab6-ad3f004d1aab | -7.03715 | -59.8497 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62aec377-b81c-3998-9154-fe76e3c76303 | -6.78892 | -59.63778 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5794fad-c0f0-37fa-b8b3-98c9dfd6988c | -9.40918 | -60.53968 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b284d5fd-8e63-3d6a-aeaf-e2614616cc89 | -7.62514 | -61.03749 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 223274e0-1f49-3234-9e92-be6feb4880f4 | -8.90455 | -60.76705 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82c785e2-6415-37ef-b7c5-c9b82df070ad | -9.40829 | -60.51677 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3133507b-12aa-35e1-9132-1bf587b5c41b | -9.4196 | -60.526 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49fc8dea-5cab-39a5-be74-a971698ffecd | -8.33844 | -62.94442 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f48b7c81-264d-3b45-bb97-fd951f644e2c | -9.17278 | -59.51195 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9a786de-4846-3b89-933a-34833da7114c | -9.18621 | -59.44775 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README75.md)
