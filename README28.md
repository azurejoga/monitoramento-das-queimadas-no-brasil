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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 702adf32-1394-3f43-b7cb-2f732af5620d | -10.85136 | -54.03796 | 2025-07-26 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baac6514-b48b-3005-8b73-14aa38dfb8bc | -6.63159 | -58.84605 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| a70b6c8b-1fce-3a16-9868-5b7ee0f0f4c4 | -9.60833 | -63.4649 | 2025-07-26 05:44:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bebc0e94-3278-37c5-b597-7b6854eca431 | -6.68193 | -58.84425 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a971ff11-8db7-3b4d-9d9f-6809028421c0 | -6.66983 | -58.83355 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8b604452-11e2-3536-8e7c-6090120d6085 | -8.61113 | -64.06888 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b124628-d8c7-32c0-9120-97c4a12ea60c | -10.22579 | -59.40929 | 2025-07-26 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfdb20bd-e8f7-320d-8171-8f1a211e5392 | -6.63928 | -58.85588 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| bc7591b1-ff41-347f-a105-4943d893b3ac | -6.63482 | -58.85526 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| a7e55122-d3a4-3eea-8d28-2e08955d1949 | -7.29044 | -60.18123 | 2025-07-26 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f21bab92-a3e6-3484-8b5e-604510653faf | -6.66155 | -58.85914 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 3794f2fc-fa85-3508-ba83-2e5a8afe19b2 | -6.66028 | -58.83659 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 85a99f6c-dde5-376d-99ea-5c69e4984ff3 | -6.53697 | -56.26581 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cede46c6-aa3d-398b-a576-ce64b6e81881 | -6.68386 | -58.83116 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 80ef0fd1-5a7d-33d2-8a88-8eed2dfed04e | -8.49955 | -64.04456 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b35dd7dd-9593-3360-b7c2-f3265c59bcfc | -6.62146 | -58.85332 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 09700054-9493-3d32-842d-fc6c2f323520 | -6.53471 | -56.26649 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 995cf333-555b-3f36-a4cb-b6fdec7ff078 | -10.85159 | -54.04343 | 2025-07-26 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eff18ea0-6852-3076-b585-78986bf98b44 | -6.66537 | -58.83287 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| d68956d4-30bb-3bb3-b683-89a9980fa081 | -6.55388 | -56.24536 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49f20f99-5de4-3df0-99c3-bbe86ce40c77 | -6.62591 | -58.854 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| b1ceef9d-714c-36c5-9444-52c0b271a5cf | -6.68703 | -58.84058 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 585c640c-9b3f-3044-a7ef-679b707530ef | -6.67173 | -58.85173 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 2692b6ae-1806-371f-8691-703ee0853231 | -9.01733 | -63.92064 | 2025-07-26 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d3ee10a3-a67d-373f-95bc-9c038417a006 | -6.54718 | -56.25463 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64997c81-af6a-360f-a0c1-e69b12346dc0 | -6.67555 | -58.85673 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9bf127f3-a210-3e34-af2f-a11b2379051b | -6.61824 | -58.84396 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97941fc6-649a-3f94-b01f-f9b0e8de11f2 | -6.65072 | -58.83967 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1d2a0aac-3a5b-3e0e-b8aa-07bb53cdb72a | -6.65008 | -58.84408 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d1f17ee7-5d3a-3418-865e-9798911e3bb5 | -7.56635 | -61.40628 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd98cc86-8e9f-3ec1-bf4a-a4efd74cf485 | -6.53562 | -56.25982 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c313dcd2-a22b-3ffe-8f98-e1112f8498ba | -6.65518 | -58.84034 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3751a3d2-15ac-319f-9fa8-63cca898761f | -6.64373 | -58.85654 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d49a2595-fcfc-3cc6-8aac-cb417745fac5 | -6.65773 | -58.82272 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9be2b2bd-8fab-3f63-8728-f3402fc7c217 | -6.6418 | -58.8384 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ffd1168a-c5a6-344e-b3ee-ae6f327f828c | -6.67939 | -58.83051 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9e75f656-881b-38ae-a07a-e62277e0c7b4 | -9.13199 | -63.92222 | 2025-07-26 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be6b701b-2c8b-321b-9a51-ac0faebdd6c0 | -6.68575 | -58.84927 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3eee5af9-403d-3edf-a02d-fae3f2878203 | -6.61504 | -58.8345 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 123d402c-16ce-3477-a98b-b41855ce3359 | -6.63605 | -58.84667 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ff985e48-40fc-366e-b18a-0e6ed645776c | -6.67619 | -58.85235 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 5475fd89-dc82-3081-8a3d-06b1c4ab7aef | -8.9764 | -61.50807 | 2025-07-26 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a61b8d69-303d-33b6-9e4f-8b4f37c4bc7c | -7.90132 | -63.53225 | 2025-07-26 05:44:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa6230aa-9ebd-3367-8689-debc7f42f12c | -6.53262 | -56.25832 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9ddae1a-b205-3e1e-8e6a-da9a7c33ffb0 | -7.56184 | -61.41039 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a705db20-832b-377a-9ab9-ca6a280091c1 | -6.62903 | -58.83213 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fa4a0906-2336-3107-a0ae-f5419fd3650e | -6.54278 | -56.24715 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9de8a52d-4842-3135-b229-ad1cf09185ab | -6.66409 | -58.84167 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 80b6cf41-22bd-3af1-b109-7124be03507c | -6.67493 | -58.82983 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5e7571fe-9f78-3f1e-9dc1-ad5b3b2c10b4 | -8.53841 | -63.88376 | 2025-07-26 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09087e9d-d6fa-3a7f-bd2d-b98084a9bc9f | -7.29508 | -60.17822 | 2025-07-26 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db40956e-eecf-3ff0-b7b1-8a62e9e0bc2b | -6.62332 | -58.8403 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 63259b0d-832d-3faa-8f61-0ffb6b9651bb | -9.22614 | -59.49966 | 2025-07-26 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e15db631-8424-3dec-9d45-5806b9f2945d | -6.54186 | -56.25387 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31fc9278-a148-3b2f-be5a-ec40262d8d57 | -6.64882 | -58.85283 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| a1381e10-faca-3117-a4a2-1bf68464b971 | -6.66791 | -58.84672 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 172.0 |
| df35a9de-2c41-3900-a070-0aaa99eca960 | -6.67559 | -58.82537 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d0082bc-75d1-31ea-a93d-8669974478d5 | -6.54094 | -56.2606 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e049a637-87a7-3bde-9fdf-ca1fa2d73f05 | -6.54323 | -56.24383 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e005d22-8d66-3b16-aea5-708999017b15 | -5.91797 | -61.30334 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3031114-09d0-3a88-96c8-c99deabc6c6e | -6.62394 | -58.83591 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 127a0756-2f31-30d0-887a-7b151ee19519 | -6.53166 | -56.265 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d56a467-59d5-3ca6-af99-1a291277a280 | -6.66155 | -58.8278 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| f39cbf12-eab9-3011-9a77-af3849086bfa | -9.2054 | -59.68075 | 2025-07-26 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70fb94f0-e26e-3a6c-90f8-304d1699afd3 | -6.64819 | -58.85719 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8672a28d-fc0e-36c1-b546-3269917eb20f | -6.63797 | -58.83333 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| fc8d77b3-130b-3376-9d3d-bc58d9da019e | -6.63098 | -58.85035 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 091cb452-0bd4-3a59-b898-4b9f88143efc | -8.49785 | -64.03298 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e066f0c3-31bd-3f2f-96f0-03a73f81791d | -6.55783 | -56.25611 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8c130cb-7f9d-3de3-879e-5f9461ef7a2d | -6.67875 | -58.83492 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f898c85b-4857-3d12-96d8-b2b0ece84d8f | -3.84125 | -62.06968 | 2025-07-26 05:44:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ded700c-90bf-3b35-bf64-5dac115180ee | -6.54566 | -56.24319 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48386e2a-c38c-3dd6-a749-d920ae013560 | -6.53841 | -56.25579 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba07a345-5832-35c3-ba36-fa7490fbca42 | -7.49434 | -63.82145 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad0570b9-6c68-3e9f-8113-eb5dfc989059 | -6.62011 | -58.83084 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| ed362098-a314-37f2-b1f2-5847f3adc7c9 | -10.85076 | -54.04321 | 2025-07-26 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02339523-33d9-3576-89d3-3a084b501483 | -8.53498 | -63.88323 | 2025-07-26 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 18e5d1b5-a88a-3bf5-9a8a-d89b76a29e8d | -6.62457 | -58.83149 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b14eab82-9bb8-3413-a067-4bca1e5d12b4 | -6.67684 | -58.84797 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 83bc1a45-496f-3c56-89db-3285cfff52db | -6.66664 | -58.85545 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| c87734ae-54d9-34ec-acd0-b3c07c1da54f | -6.65709 | -58.85849 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| e59abe12-11ac-3e64-abf3-a79fe527b83f | -6.64371 | -58.82507 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 91a14134-87c1-38eb-8a2f-240592cdcd75 | -10.04898 | -59.10347 | 2025-07-26 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 671f79e2-5761-3e9a-a786-c47116d3c08b | -9.39333 | -63.50646 | 2025-07-26 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f73e682-e586-37d3-97b1-61f8e9c71651 | -6.68065 | -58.85298 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| d4f82937-141e-37a2-bb25-08b649124c5a | -6.53938 | -56.24905 | 2025-07-26 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c1d9de8-87b7-3773-a5e8-40f36cba489a | -7.50091 | -63.50739 | 2025-07-26 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11bb4fa2-435f-32e7-81e2-f848e126c6ff | -9.19984 | -59.68863 | 2025-07-26 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 492b0565-5338-37a5-976e-1189e196194e | -6.67112 | -58.82471 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8430c5db-e187-3d9f-9676-48003bde6049 | -6.65136 | -58.83525 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d0f0c4cb-c84c-312f-9dfd-8aa4ce461bbc | -6.65264 | -58.85785 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f910e122-0f7c-3933-93a8-abff990bf9d9 | -7.56253 | -61.40571 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6fc029bb-e83f-3b15-b445-e54bc9fcfb68 | -6.68452 | -58.82666 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2efc5f40-164c-3754-89b5-96af8f8c3004 | -6.62777 | -58.84099 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 335f1586-6662-3565-b49d-20182ed1cd20 | -6.62967 | -58.82766 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2938244-28d9-344d-80d5-4e24f73729b8 | -6.67301 | -58.84298 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 72ef860c-9b8e-3368-8f48-32f8558905d2 | -6.68257 | -58.83994 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5117ed22-5c10-3cae-a3dc-915342043433 | -6.6252 | -58.82706 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57a6a25a-9603-34c2-b622-fda8e0639243 | -6.63414 | -58.82825 | 2025-07-26 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4aff616b-722e-3364-b89f-14e231dbe1eb | -5.9173 | -61.30789 | 2025-07-26 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README29.md)
