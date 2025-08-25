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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54cc0d89-3238-3495-832e-848877ff59ac | -8.9761 | -65.398697 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1dd29ef4-0ba1-3f4c-8313-3b01c961efe7 | -8.5093 | -63.879398 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 70e78d59-fe28-3383-b125-7d745792dbe8 | -9.0429 | -65.734497 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea8be8f2-0672-35a8-b98f-a92f6a6758c3 | -9.1673 | -59.4617 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2a8c11d-405d-35b0-a9a3-f615ceca32fe | -7.6273 | -62.7257 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b45e717-89ec-3f71-8288-4539ddc6c947 | -8.1257 | -62.867802 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07e8d803-869d-3dc0-96d3-09306573b8f3 | -9.0055 | -65.391998 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4474b55c-7ec9-3fff-a9e5-503d9858f3fd | -8.9042 | -62.450298 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01244eb4-c061-3d0f-94ce-4beeaf5b1b42 | -9.1609 | -59.4776 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84dcff27-4229-3e56-83ac-3ee0489bcafb | -9.1612 | -59.520401 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecbeb40-11bf-3473-a486-d7adeed0eb02 | -8.9875 | -65.403503 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea1322d4-32ad-3e07-9ca9-7f3d9a787fe0 | -9.0138 | -65.697403 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb7be4da-1df6-39d8-adf6-54da81e738ba | -9.2172 | -60.922199 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8be75be-f33d-3189-873b-1a11095a5677 | -8.9909 | -63.643299 | 2025-08-25 01:53:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e0e6145-0cb6-33a7-bf45-4f412108d103 | -11.468 | -55.450401 | 2025-08-25 01:53:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| deccd271-f29a-33b1-af3f-d26bceb757dc | -7.5635 | -63.853401 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc057f94-d71c-32ed-86db-63ec0a28facb | -9.8258 | -64.2537 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c93522b8-ed1d-3876-8bd4-0bc0945c16c8 | -7.9236 | -63.060699 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb918e5e-d20a-3fe1-9bad-bfacf869c70b | -13.1324 | -53.717701 | 2025-08-25 01:53:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb8ff44b-9290-3ca4-a1d6-d1c8b8d3ff5c | -8.8902 | -64.183098 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69a5447c-79dc-3cb3-9e03-8f80d7c1f4f8 | -14.4368 | -56.464401 | 2025-08-25 01:53:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 117f8b32-7cd3-3245-b6c2-6bbf39a69b5b | -9.9634 | -60.173801 | 2025-08-25 01:53:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ab79f40-e669-3ae2-a380-d04822cb281e | -9.1868 | -59.456799 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60198a2c-2c06-3298-b5cd-eb76c2f9fe7c | -9.1713 | -59.602699 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98fdc930-01be-3e96-b1c2-09c9eb0f337f | -9.1477 | -60.7645 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7feb3d6-919b-3b0e-bb9e-d16743233a72 | -8.8902 | -62.4347 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5ebd635-4fc2-3994-b864-e648e34e48c6 | -7.5439 | -63.858002 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46402585-c4d6-36c3-bfaf-fc36a184079f | -8.1159 | -62.870098 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65253ef6-6eca-33b9-9798-13936f0887dc | -7.623 | -62.707802 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9f65492-e6ff-3b0a-96a8-a12f08d99de5 | -13.1419 | -53.715 | 2025-08-25 01:53:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6546e06b-7b86-33dc-845c-2c7d6a475bbb | -8.9793 | -65.412697 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 605df53b-4f9a-34a1-898c-67fba7d980ff | -8.877 | -62.466202 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c0a027f-7f7a-3cce-9128-df91782acb93 | -8.892 | -64.190598 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c324976e-c338-3c3f-9172-a068bb757a16 | -9.022 | -65.688202 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d889eef2-51d6-34c4-9919-d8ba233aefb6 | -9.1595 | -62.351299 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb2ccdcc-b675-31c1-86e0-fd5901ada499 | -9.1546 | -59.4935 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5df784cc-7034-3fe2-891e-a062810191ed | -7.6724 | -67.0952 | 2025-08-25 01:53:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce6fc402-67d2-363c-abb9-96d2b743a987 | -7.5346 | -63.818501 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 804e80cb-a2c3-35d6-a8f2-5e97f45b6e56 | -9.0169 | -65.396698 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc41a080-3dac-3999-88e6-fdeeb4f31eed | -9.0071 | -65.399002 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a4facb9-d46f-3379-97a6-dca04f17cf76 | -13.1403 | -53.745899 | 2025-08-25 01:53:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f19d5957-4174-394d-ab4a-947a6e6b16b3 | -8.9195 | -62.4277 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4e67b8a-dcfe-3356-99ad-cb3c44d2ce2e | -8.1082 | -62.881001 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3843b01-3784-3308-9fdc-7964934debfa | -8.9732 | -67.472504 | 2025-08-25 01:53:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 591de042-653c-34b6-b4c8-0ece4753f949 | -9.1639 | -60.830898 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf825a3-e9a5-32bb-b692-d43892a81e4d | -8.9748 | -67.479599 | 2025-08-25 01:53:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7c8164-52bb-3231-b5c3-a3e4ce1cd599 | -7.55 | -63.839901 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1612ecd6-8d9d-364d-b7f5-4c5ecf4bd360 | -8.9859 | -65.3965 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0200fa16-3b9d-3364-ac88-560607b5ec5c | -9.1002 | -65.714104 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4cd52f6-97ba-30f5-b152-5c042d57856a | -8.5191 | -63.877102 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e87d1c2a-45e6-3609-b1af-95f42b3854b7 | -9.2525 | -59.638302 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 314c5739-1fce-31bb-80ab-a3aaf1f9dfb8 | -8.9777 | -65.405701 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd423f5-aa61-3180-bee8-888648e1a2e9 | -9.0723 | -65.727699 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 737f632a-4eaf-3dd7-a877-950194ee20ac | -9.2366 | -60.9174 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c890fbf-4cf4-30b6-898f-8d8e13e553fa | -7.674 | -67.102097 | 2025-08-25 01:53:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1537479-ee82-3e4f-8c84-25967ca164a5 | -8.9809 | -65.419701 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba0d846-5038-3dcd-9c96-1a31cc5e016a | -9.1901 | -59.470299 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32734ec9-5bfc-3c8a-878f-6e62ec551171 | -8.2332 | -61.420601 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2336a3d7-4cae-33c9-9885-69db8b1f4c98 | -11.7009 | -60.175999 | 2025-08-25 01:53:00 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0217d8ea-7aa3-3f2b-a36d-b8ef0beaec58 | -8.1061 | -62.872398 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3cd8d4-1102-31b7-b152-180fd1be5ac9 | -8.8825 | -62.445999 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 33f3330b-348b-37b4-ac18-a58c29bf527f | -6.9171 | -62.996101 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5348c469-2d75-39d0-96a0-cf446913bcaa | -8.2183 | -61.4021 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9c248f3-4c8f-384f-ba67-0053e3cce269 | -7.4297 | -60.619801 | 2025-08-25 01:53:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99a12b45-dcad-3123-83fd-ed5db53ad919 | -9.1935 | -59.483799 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5cfc43f-3a0e-35f7-bf79-aa3618fb2128 | -9.5085 | -60.5084 | 2025-08-25 01:53:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e994b287-7f6e-372d-8b2e-e1b05eb88bb2 | -13.1594 | -53.740398 | 2025-08-25 01:53:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4f380cf-4c07-385a-9951-f5c085a72d9c | -7.6503 | -63.520302 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5845596c-1b36-3031-b54d-0d9085bdc1e9 | -9.2168 | -59.702702 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d113dd20-695c-3c3c-ba8a-b12bfd7aec80 | -9.521 | -60.517399 | 2025-08-25 01:53:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a45d207-7b3e-336a-aaf9-67ee4b846372 | -8.9076 | -62.421101 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de5e491f-af14-3b35-8023-88fb912999a1 | -9.8211 | -64.278 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b21d6b8f-99dd-3b4e-ad9f-1223ca38ef3c | -9.177 | -59.459202 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 184eca9d-337f-3080-ad20-6ae5dcafd723 | -9.6543 | -59.634602 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd57a7f-5993-3ee0-8fab-4d06703d9e7e | -9.195 | -60.9161 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4e8f2c5-b133-3057-be48-e18796f635b6 | -10.2578 | -59.1143 | 2025-08-25 01:53:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b33a839-309e-31ae-87c7-2007063afe9b | -7.5537 | -63.855701 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05b5a6c5-fa45-336c-a6ac-c0a87d3808e1 | -7.5519 | -63.847801 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f324cc35-5014-318a-ab18-a81ef97f14c2 | -8.2281 | -61.3997 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7739a609-f3a4-3722-8e20-abf6c5946b0d | -9.171 | -60.817501 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6ff1681-011e-3bce-8a0b-ae6095db3dbf | -8.6636 | -68.668198 | 2025-08-25 01:53:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71dfe60a-16a4-3495-a587-2c27be2380ea | -10.4139 | -64.385101 | 2025-08-25 01:53:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93e405d3-397f-3203-9c1d-c050d132ab2e | -9.2048 | -60.9137 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc15f35e-03d2-3c6e-98eb-e5617b36890f | -9.1683 | -60.806499 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3e072f8-e9d5-3205-b474-244b37d5b9ae | -9.816 | -64.255997 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1ef3935-57cf-398b-909e-4730be9e4fbd | -9.9664 | -60.1856 | 2025-08-25 01:53:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 061a666e-e8fc-33e7-9dbf-5bedf403b5e1 | -8.8999 | -62.4324 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50db0b19-449e-301f-af66-b0f0cca1ff37 | -7.9159 | -63.071499 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b6a21e1-8cc3-3bb2-a880-f781e3aeae25 | -8.4694 | -63.929298 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc2062e7-e43f-327d-af79-c67a4823247e | -9.1736 | -59.445702 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04b9583e-5355-38a8-9bb9-657a7f47c7e8 | -6.9269 | -62.993801 | 2025-08-25 01:53:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fdf915d3-82f4-3948-84ae-952ddc686f00 | -9.1639 | -59.448101 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb3ce92d-6b12-39c0-a88c-51a8cccd5dcd | -9.0121 | -65.375702 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbed9c95-f5c8-397e-a22f-3745e4024d47 | -8.9174 | -62.4188 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 296dc594-2652-376d-99bb-e0fa1d82137f | -8.5155 | -63.861599 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d247cce1-5cdf-35d1-bfbd-973ab4a0aa08 | -8.6864 | -62.8801 | 2025-08-25 01:53:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b56775ec-7b3e-33e4-840b-ed6221cb3682 | -8.9923 | -65.4244 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7555271-23cc-3882-b50a-a5308b425e64 | -8.2306 | -61.410198 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b1061ba-32da-33fb-bcc9-917d72bd0a26 | -8.2132 | -61.381199 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc10b0cb-4149-3487-a1ee-32d8955ad9c8 | -8.5173 | -63.8694 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
