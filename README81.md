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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70e69d7f-4796-3ff1-b265-4d11f538dbd3 | -9.52244 | -60.52261 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d17bbf18-af34-3d2a-893e-c84b4a5abe0c | -9.09486 | -65.72659 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea2198ef-bdb8-3eab-9498-1c86429e3fe9 | -6.69108 | -58.8594 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b6bb857-a3be-3b8b-954a-30e1402a0575 | -5.80113 | -59.22293 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76356c14-5110-32f4-8c2d-9b562bd51bb2 | -11.70224 | -60.18044 | 2025-08-25 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7318d63f-911c-31bd-a66f-acfdf921a1d9 | -8.68696 | -62.8746 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3449400a-fd49-3211-b760-af28f6d3de25 | -9.12923 | -60.73007 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf768ac5-2ef8-3547-9e6c-3cf3bb4fa005 | -5.74847 | -63.17249 | 2025-08-25 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df873179-cb7b-3424-a072-de94bbd6d3fc | -9.19511 | -59.48651 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99892c70-a048-3f33-8400-19f06933be4e | -6.68648 | -58.86086 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a191a8f9-47a0-3b7e-a4a8-eac72d5bc4e9 | -9.19297 | -59.45401 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 084b7554-7bc9-331a-b96d-be3c2088a5a2 | -9.01891 | -65.395 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72459a04-8e1d-3893-8e79-388d39b0835a | -7.89598 | -63.06551 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 1f7e1f0f-d4d3-377f-b109-5487654a4d5e | -6.80064 | -58.6416 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab67a827-72be-32f8-ad58-3cc22e6ef426 | -9.31143 | -63.43791 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c2bcbed-830d-34e8-b294-29049ecb8bab | -9.24804 | -60.48759 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9eef4769-60a1-3de0-a928-bd57446c2b9c | -8.91007 | -62.41163 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5835b8a7-31d0-334b-86f7-533c2e72c38a | -9.01986 | -65.70419 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7f8eec5-74c7-3d4f-bfed-61a91d905cb8 | -9.49409 | -58.93411 | 2025-08-25 05:55:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf49d9fb-7745-3f08-85e5-27edfe393b23 | -8.12986 | -62.87519 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ec27af3-4106-3e6e-a531-226e2617a12a | -9.23893 | -60.4765 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f790016-22da-3c0d-9b90-4d9fea6650a1 | -9.09244 | -65.71737 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3c948338-721d-317d-b2e9-6c382e19c9c8 | -9.2353 | -60.92247 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a168825-28d5-3cc8-8e62-f53c5daba8d9 | -9.20006 | -59.44941 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ebb77c8c-5738-366d-9c25-ac1816feb6d1 | -9.24327 | -60.48367 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 576a260e-2701-3481-b290-0098c8504ad9 | -8.12002 | -62.88226 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7f42172-7c4c-3eaf-8143-cbd4de038a0b | -7.65265 | -63.52284 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a4d4a4f-2e9b-3659-8157-554875abb36d | -9.15965 | -59.45507 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cc1e825-b91d-3956-ac4c-73072799c371 | -9.2031 | -59.50828 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1274b4ce-6d79-3e55-8f2d-305240c37f60 | -5.80652 | -59.22372 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63c66c5-1de6-38ad-952f-e711d19fdd3c | -11.69676 | -60.17964 | 2025-08-25 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 157f9ea2-32b0-3e6e-adac-386fcd2ba0ce | -8.47104 | -63.9304 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14ed0fcc-9fe8-3ee8-9335-afdba7cff4ee | -7.54575 | -63.85947 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59c645d6-4be4-3b23-9e81-47c7b7af3c2b | -9.00524 | -65.40016 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d1c92dba-5e3e-3ab4-8ee3-296a8dad58df | -9.15262 | -59.46556 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aacd12d0-3658-3f07-b7f6-d969d7c08e4d | -8.90034 | -62.44766 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52feea86-c623-3c87-a8be-8c6f32cd61e3 | -8.10326 | -62.87552 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b05a97f-5d76-34ff-a21c-a554e2ecce5b | -8.90557 | -62.45491 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef571419-02f0-3527-9e7a-344c48dfa2bc | -9.15625 | -59.48109 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92bfa4ec-2ff1-3217-b392-596b1b18d433 | -8.91611 | -60.7198 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 96d1b6a4-724a-3475-95d3-45d18032ed63 | -9.64786 | -59.63388 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bcbc0674-2e92-3da2-a2c3-e3fe1a7b6aa3 | -8.91955 | -62.41953 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efec88b3-fc17-3073-8f3c-9003ef6bd79a | -9.01031 | -65.39169 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2084ed5a-c277-3ab7-bd89-0bcbb85010ec | -8.92159 | -62.43863 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7524aef3-8f03-3262-84bc-52d4bd0bfd8f | -9.15118 | -59.47665 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0a2b669-7ac9-3e2f-94a7-ecfc9f94eefd | -9.02153 | -65.39335 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8193b8a-e7e8-3653-8b2c-9803e1111ff9 | -8.23296 | -61.38268 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12676615-c52d-37f9-831b-07c023a619b7 | -11.99447 | -61.02243 | 2025-08-25 05:55:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f63355fd-7ec2-30b9-9364-9496b48ff52f | -8.89469 | -62.46736 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36a84737-8c2f-343e-9859-29b7c714ba7e | -9.21101 | -59.70929 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edb70142-4e0f-3881-bd58-258ff150f966 | -9.09611 | -65.71792 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ab164e14-bdf5-3186-8803-c68590bb8f27 | -9.20667 | -60.79598 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0288373f-d97b-3613-8965-b08f7311a53f | -9.25883 | -59.6427 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb6f9d27-c7b3-332b-829a-22071c2ec255 | -9.04735 | -65.72161 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5288e2fb-b45d-3e86-949b-22a33071e128 | -8.26058 | -70.82532 | 2025-08-25 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11b080ad-968e-36e8-acaf-3e94571d2054 | -9.2104 | -60.9208 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 309a1ae9-b7b9-3e39-be1b-843bc32602de | -6.78924 | -58.64025 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d93ebb6-94c3-3d2e-9180-a6999f696545 | -8.22048 | -61.40231 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f56daf49-5899-3e22-ac7f-b44b0f47a686 | -10.42383 | -64.43633 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 756177a1-a1fa-3967-a37d-f0d3fafd7567 | -8.89001 | -62.45553 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c33e0b9-4615-3c53-b90b-75adee34d330 | -8.91769 | -62.43338 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e62dd289-dd9d-3cc1-8d2e-1f78056c8a0a | -7.33185 | -59.6122 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51673c53-d651-3c8f-81be-f7c1c9efc422 | -9.01442 | -65.68991 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5c24fee-c6a4-3442-9f86-66989575bccd | -9.24243 | -60.49004 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d50d6a5b-8cb3-3220-b3e6-4bee45741634 | -8.58604 | -62.63123 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb6becaa-1dac-346b-a7a0-786cb403b8c6 | -8.88419 | -62.43131 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e55a8e3f-5447-3a0c-b6f5-ec026242afc4 | -8.61639 | -62.60863 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d566773b-05ff-322a-bba6-52de745ffcdd | -8.90876 | -62.42081 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cf5516a-1421-304e-8d44-e02d12591800 | -9.18365 | -59.61748 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00cd9425-8b57-342b-8ed6-98dd7076eb20 | -9.15287 | -59.50697 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc11bace-9f8a-3209-ad36-bc16b2a30a23 | -9.15987 | -59.49663 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e085abb-86c3-3b01-8615-a13f84df418c | -8.86203 | -68.84875 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 151dcc1a-fc74-3204-8e23-b3d96cdb43be | -9.17388 | -60.7697 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4eeafd6-e064-3345-922f-8c6d3dda0af7 | -9.09181 | -65.72172 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f9f90e9b-1988-328c-98cd-1ddd478a62d0 | -9.65343 | -59.63435 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f8c03cab-2ae4-33b2-b4fc-7e8427058b1f | -9.19758 | -59.46801 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25ede5b1-9b54-3978-8dae-2ecc13309030 | -8.22312 | -61.41894 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76221c49-1427-375f-a333-d8a892f016d5 | -9.20043 | -59.43975 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 315924be-8c20-3103-b9a9-e65ea5273528 | -9.18165 | -60.78935 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 68251571-b852-32f0-b48b-36f451757ef5 | -9.19573 | -59.47709 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77779f94-a0e9-3fb8-83b2-e7db8dda1bfd | -8.22384 | -61.4136 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ce52319-0b1f-3032-9b62-9b0e779b5bb0 | -7.57187 | -63.43812 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72bc78a4-9714-3f21-8355-48750ab35242 | -9.05772 | -65.72767 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68865d8a-83cc-383b-9ea5-daea7c5fe63c | -8.88743 | -62.44113 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3090ecbe-c88d-30e0-9ad1-69760beb5596 | -9.16749 | -60.81805 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc11c855-5006-322b-8006-0bc14dacf35f | -8.89774 | -62.46597 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59febaa0-bc40-3710-bce1-28e737d37cf8 | -8.77874 | -63.95952 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0856afa5-24e1-39fc-b651-07d007784d02 | -9.19391 | -59.44654 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 558d3a37-2f1f-3e31-9f4b-aed58588d93a | -8.90226 | -62.46662 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3e8d7a1-d746-38a4-9983-152d0c3db63a | -9.19731 | -60.78851 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89f8df99-9347-377d-a3e4-a7d7fbaef009 | -9.20498 | -59.49342 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 867d8b52-ae31-3cf9-9453-7092c4fff352 | -10.2579 | -59.11456 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db875e72-e5e8-3145-8028-d188b798f5de | -9.26932 | -59.78313 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 357df812-ccd6-3eab-a468-f4dcd00d7676 | -9.09119 | -65.72604 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| df10136a-d62c-3e43-b5ac-c71a931c1fc5 | -9.01233 | -65.37805 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd12e71f-8e99-3eda-9c08-2ca6d8301f9f | -9.20155 | -59.43818 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7237ae9-ba78-3489-8405-f2cd24e91ada | -9.01682 | -65.69926 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe269baa-9623-367b-82f3-a1adafe214c6 | -6.92535 | -62.9952 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73ccd26c-6a04-34aa-9431-298a1f36bd24 | -7.64798 | -63.52596 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd9fc040-7626-35b3-bc4f-30a70838aa75 | -8.86604 | -62.39585 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README82.md)
