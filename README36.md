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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d10a62a5-4dfd-356b-ba13-583a22b506e2 | -7.12873 | -59.64432 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 189a520e-2deb-3388-98b4-67dea114c340 | -9.15486 | -59.65792 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f53586af-778c-3a01-892a-4afc76db5fde | -7.08329 | -60.02267 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67d923a8-7ba4-3a05-b1f7-d4ceb437fcfc | -6.9016 | -59.14479 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9852afe3-297f-3fcb-8691-909ac56c7c6b | -6.11241 | -59.92389 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de18c7fa-a6de-32b4-a2d4-3395047f849c | -6.89485 | -59.1487 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e6577bf8-8e95-3a91-8c37-a527593a0308 | -6.88801 | -59.15984 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 12f76594-664b-3feb-a7d9-c56cbf9cfbad | -8.11596 | -61.2091 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98e81921-da9b-39ef-a638-0c0198d4dc79 | -7.33222 | -60.62014 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4e3b650-6777-3c56-a14f-a0b05bb7e58f | -6.09089 | -59.95273 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e9073578-ebed-3baf-a683-dc75ee916713 | -5.74692 | -59.87069 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba959a3d-c86f-3660-b480-48b07861a2e7 | -8.1155 | -61.21266 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2285754-5017-33eb-ab08-5c01096664b0 | -9.69445 | -65.69163 | 2025-08-14 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f701c3c3-76da-338b-83dc-b41cd2f4b34e | -6.92092 | -59.14568 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b57a3330-2beb-3ed7-bab5-d4896e8e63d4 | -6.88265 | -59.14701 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 414e599e-716a-3c36-8f86-1a1e504b5ea5 | -6.91545 | -59.13997 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 854a8add-6852-3e9e-b9c5-d36b2eb9e376 | -5.7567 | -59.88472 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b87ed2c-67fd-35bf-8bc8-bbe5d73ae7c9 | -7.33223 | -60.62804 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1723751d-ecfb-3028-b2f6-c18926801f41 | -7.87971 | -61.82656 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6197968f-fed7-3418-810e-c0cbba93642c | -6.64803 | -59.07799 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 20a82094-6a62-387e-b3c7-27da2eb931de | -7.13409 | -59.64937 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3335b659-71a2-30fc-95bd-f7491fc8ae55 | -6.87782 | -59.13675 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 388f50d6-ed36-3c39-bec4-1ed4fe1b1b04 | -7.88186 | -61.8107 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d820f42-7521-33a1-b094-4f2582a9559d | -9.15428 | -59.66245 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e77fea7c-16bc-3116-8720-9477d5b221f6 | -9.5093 | -60.53872 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2842d77a-9c3b-3b78-817b-0ac6924f59a3 | -7.07481 | -59.20789 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 449f587b-dc0b-3f45-81e1-5fbe4995f261 | -9.20662 | -59.6487 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbb5c68f-c594-3f78-92d7-83e6521b02ac | -6.91378 | -59.14666 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4e08d28a-7ef5-3dee-8633-3ccc4413fec4 | -7.09534 | -60.02428 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cf8e41e-4247-3488-a3bb-520554667e8e | -9.16611 | -59.67613 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54088d19-ad04-36ac-a2b2-20bfd32f6709 | -7.26337 | -60.63313 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a284bf2f-6d37-36d6-82e9-caf807f4f1ec | -6.88862 | -59.15516 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 1e88efcd-4a75-33f6-beff-57b48c3e0125 | -6.87846 | -59.13202 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04ea9832-5244-3d5c-8232-2844c3026ad2 | -5.75208 | -59.87572 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 737bc6b7-261b-3234-8543-900130ad469b | -6.09988 | -59.92982 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77d6d1e1-9368-3c87-8873-6862d2c13d8d | -5.74543 | -59.86929 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b454d8-2c9c-34bb-94c4-567513a22132 | -5.74936 | -59.89574 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a283a49f-c6c8-3e1d-a145-3e2f1f287e15 | -7.33273 | -60.62438 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b047e4b4-2737-3d25-8dd7-3543035e40ca | -6.88313 | -59.14957 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e32e1d1a-c6bc-350b-bc03-b44d4a3c978c | -6.09253 | -59.94078 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 07182938-64ed-37ec-a572-6b1bcd70101d | -7.3378 | -60.62882 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1723a6a-bbcf-337b-85c3-c84ff68ded5a | -5.74011 | -59.87777 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a58d084-887b-389b-8928-56c3c6cdc6db | -6.77792 | -59.46967 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa2739c1-21bc-3a54-af9b-dc5d64a253b7 | -7.87495 | -61.82264 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 252c0b43-a37f-3a4c-907d-2e1760cfd80e | -9.16036 | -59.66329 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 453e1e3c-a612-3427-bea8-d19ed88147d4 | -10.02569 | -67.6422 | 2025-08-14 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2b58d6a-bff5-3b04-a65b-d449e3198d9b | -9.19268 | -59.66125 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1727250d-2626-370e-acd9-f0870e2c6eaa | -6.09823 | -59.94187 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eae05a60-17e0-31a7-81b9-96e169324a7d | -7.87538 | -61.81949 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 331f1cde-fd9a-3e88-af37-d3711dc3c1f7 | -6.91316 | -59.15121 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2a724071-efff-3ccc-8df3-18a8cc3b9035 | -7.26486 | -59.99586 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71001c9b-9a1b-3101-abc5-611d68d21fde | -9.93028 | -65.23418 | 2025-08-14 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 836ee12e-00a3-3ee5-96cc-1f48dc58ef55 | -8.10826 | -61.18292 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ee91b11-b013-30ad-9a66-a2539032eabe | -6.88434 | -59.14009 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f8efee1-c710-39d0-a696-ae8c7bbe42c0 | -10.33584 | -64.45448 | 2025-08-14 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3901853-4552-337c-a3fe-dca459f077f8 | -9.16172 | -59.66133 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4efb9d21-22e6-322c-ac18-15cb8e23bd65 | -7.26896 | -60.63383 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6df1493-47de-3e73-b14a-54067530db03 | -6.88137 | -59.15641 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a028f338-3aa4-36da-89b8-ca5af7ff1ec3 | -7.13446 | -60.12863 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e946d3f5-3bb4-345c-bc3a-b01e8b5d4186 | -7.53259 | -61.38609 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7177f920-1e0c-3ac2-9655-1a08f86aea8d | -6.89105 | -59.13623 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbcbb12e-3fbf-3eea-a92f-1236bd9bec4a | -7.60406 | -63.52134 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a927f50-68d9-35fd-857e-6222a31b0523 | -7.87148 | -61.80918 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2c2bc6f-3d19-32e2-a579-008a8973b093 | -9.40284 | -68.61362 | 2025-08-14 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12e3b985-9400-3423-a4f6-51e5a80cec4e | -7.87928 | -61.82969 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08c1c0de-9248-3986-bab5-7bfced250392 | -7.13844 | -59.64451 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37e217ad-9ca4-3990-9208-4ace2f09d283 | -8.10557 | -61.20395 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ca9cc18d-bae0-3bf2-84c8-937f62e98775 | -6.88923 | -59.15041 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 77edca32-49eb-38a2-9f4b-a6a617419ddd | -6.11186 | -59.92786 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04805c7f-03ca-3d27-879b-439de9e48405 | -6.08572 | -59.94783 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ea40e631-d697-359a-b057-ac44b157bbe6 | -6.87823 | -59.13927 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ac2aeab-fd85-3d92-8e10-001ddf805b6b | -7.12511 | -59.62636 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b14612b5-cc0e-3ff8-a7b3-e6099f7ab66d | -6.94069 | -59.6371 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c62f50fb-5014-3cc4-b82b-13bcdd663333 | -7.88056 | -61.82026 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c373a0a0-41eb-375d-a468-149bc6efae3c | -9.50351 | -60.53795 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3547a62f-f5ee-35ba-a4f2-6e323ca32fc0 | -6.90288 | -59.13548 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 443da6cb-5db2-31fc-9d3b-e07537ba63a8 | -7.5578 | -63.48421 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14c6963a-d6d8-39aa-95d1-fdcf3d2098f4 | -7.87019 | -61.81872 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea42640e-6b56-36be-a4a4-e0a3857b3752 | -9.16525 | -59.6734 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38133fcc-af84-3239-9885-03dbbc4b0c41 | -6.88888 | -59.8838 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9577bfe-3a4b-3ba3-b7f8-1b671873108e | -7.12453 | -59.63068 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| db0e5763-f546-3759-9f98-5df2260aaee3 | -6.09878 | -59.93784 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30f3070a-61bc-3756-b219-31fcf9f7db77 | -9.82941 | -60.766 | 2025-08-14 06:01:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a901baa4-2a67-32b9-8fec-859e13f90d60 | -5.76242 | -59.88557 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e53b4c9-4bf2-38b3-a2d0-f4189f8e9bb0 | -5.76025 | -59.9015 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aed8cc90-71e6-369e-bbcc-7dff204e99d4 | -5.76133 | -59.8936 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fa158ff-a0c3-3dae-8eff-79604c8461f2 | -6.09198 | -59.94481 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ada6fcd6-6d35-3c96-988a-a067e9a752e5 | -8.10668 | -61.18082 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2789a034-b69b-351c-ba6b-fb611655df2a | -7.09481 | -60.02841 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24a5e487-84a6-3dd4-9615-80f5903eb3f4 | -6.90031 | -59.1542 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c07e683a-db1b-3ed8-9621-ab5ec69b12a5 | -8.11099 | -61.20474 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf2d6a82-4b4a-3fdb-ab11-c8550556efe4 | -8.1043 | -61.1983 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20b583d1-bf45-3d58-9131-d298cb71c402 | -7.55848 | -63.47943 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8205243e-40c1-3bfd-b656-759d42bedf99 | -6.10669 | -59.92293 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98591836-d398-3032-9ad3-fb569369d5fb | -7.87453 | -61.82574 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8046323-038c-3094-aeff-44d75ca7afc0 | -7.13945 | -59.65439 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98d9ceb8-8248-358b-9d5b-89762dda0fed | -6.07421 | -59.94654 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12d76e10-e332-3e8f-a622-673b406baef3 | -9.19098 | -59.67501 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f096d440-d44a-3230-afc5-d021de94532a | -6.88984 | -59.14563 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7e012de3-7a8d-348d-9066-d8b8e1c2d214 | -7.07542 | -59.20331 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README37.md)
