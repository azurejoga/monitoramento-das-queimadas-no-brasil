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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d13dcf2-c633-3458-85a7-34b4a098f68d | -8.5217 | -43.2593 | 2025-07-09 06:00:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 50964c38-051a-3219-b167-e5d1a6cb01c3 | -8.5025 | -43.285 | 2025-07-09 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 181.5 |
| 369ff0cc-dfeb-31ff-9973-e60dc40a17f6 | -6.1792 | -48.0494 | 2025-07-09 06:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a3c5b0ef-29f6-34ad-afe8-9d133d9a4d2b | -11.4393 | -45.1154 | 2025-07-09 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 180a529c-ce2a-37f2-be05-32739109ffca | -8.5028 | -43.2614 | 2025-07-09 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 9c786333-0759-3502-9622-0e2d64ecc7af | -10.5776 | -49.1316 | 2025-07-09 06:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| dc129ec7-7bc7-311a-be42-cceaeb948074 | -9.94605 | -66.8638 | 2025-07-09 06:03:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbab618d-48f7-3d80-88b5-1a208be7f7e8 | -10.29512 | -60.54383 | 2025-07-09 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af3e9c33-0afc-34e6-97d0-4460c4364ebe | -9.02279 | -61.23574 | 2025-07-09 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2971271-5ca9-372e-92f3-3c0df9c0ef08 | -10.29458 | -60.54797 | 2025-07-09 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e1e7ea7-416e-3f9f-84c3-1f2b43f61f4a | -9.02326 | -61.23226 | 2025-07-09 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6c263f5-9146-3c60-8f41-1b3d57697b11 | -9.9275 | -59.93605 | 2025-07-09 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df77e8d0-ecc2-36d4-ac1c-3391f7b11754 | -10.29397 | -60.54612 | 2025-07-09 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a6b8bf3-ee34-3e4a-8e9a-928d9e6f1c99 | -9.92803 | -59.93164 | 2025-07-09 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cffce668-db1a-3167-91a0-bbb31c9397a0 | -10.29978 | -60.54683 | 2025-07-09 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c2dbf2d-c668-3000-91dc-151c99f9ead7 | -9.46388 | -62.19205 | 2025-07-09 06:03:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3096c242-8560-3af2-9ac9-29bc009751ad | -7.92867 | -61.56007 | 2025-07-09 06:03:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 408ee611-f4d5-3b62-9f57-9eb91385067c | -9.46347 | -62.19513 | 2025-07-09 06:03:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cab5fe0-0ac5-311c-a784-90f25ac2fce7 | -9.92624 | -59.93452 | 2025-07-09 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4460516e-241c-37eb-9bdf-789b7241ce6f | -9.93225 | -59.93533 | 2025-07-09 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d499271-d395-3a6a-944b-86aa546ad24b | -9.50726 | -65.58801 | 2025-07-09 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 234af473-f082-36ae-9f55-f81299e75efd | -7.92912 | -61.55681 | 2025-07-09 06:03:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 837395b7-7908-321d-a18f-77aeee902035 | -7.92901 | -61.55684 | 2025-07-09 06:03:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65b7ffd-dd4f-3beb-bf55-a6f3539b40b8 | -8.5028 | -43.2614 | 2025-07-09 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| ff33b5c7-0a57-3a87-9596-1336b4b23dd5 | -8.5214 | -43.2828 | 2025-07-09 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 7aff076a-2c86-3e0c-809c-70ae06a5c270 | -11.4397 | -45.0923 | 2025-07-09 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a02f92b6-c87b-34b9-bdc6-2a73d3a3fe52 | -8.5025 | -43.285 | 2025-07-09 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.2 |
| ca1a7fa8-96bb-3ac4-9d2a-c7b7f509032a | -10.5779 | -49.1098 | 2025-07-09 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 7367778f-6c03-3b0a-9bb8-a04a68189f6f | -8.5217 | -43.2593 | 2025-07-09 06:10:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 600cfc16-f70a-3ba4-b265-f388c3e190ec | -11.4393 | -45.1154 | 2025-07-09 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d812d250-a2db-3f11-abd3-858f284e404f | -10.5776 | -49.1316 | 2025-07-09 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 62f3ec06-3a27-35a5-841d-488a8a8c6b94 | -11.4393 | -45.1154 | 2025-07-09 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ecd478ae-1b7d-3c7e-bd3f-16808503b145 | -8.5217 | -43.2593 | 2025-07-09 06:20:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| d30be5b5-a03a-3289-b66f-7b4e6d356e2b | -8.5214 | -43.2828 | 2025-07-09 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| ff7b268f-d4a9-3e0d-a3dc-d0a74b42893f | -10.5776 | -49.1316 | 2025-07-09 06:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| f85aacfd-8803-3b14-bf3d-b425d04adfb7 | -8.5028 | -43.2614 | 2025-07-09 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 1bb2c5e0-5d5e-37f4-b877-0472788d98b0 | -8.5025 | -43.285 | 2025-07-09 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 634bbbf5-2efb-3295-8b9a-f3a3b0b4e75d | -11.4397 | -45.0923 | 2025-07-09 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e20df0f6-7cde-3eee-b639-fc10765d7479 | -7.91386 | -70.92447 | 2025-07-09 06:25:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a525f73-ebdc-32f6-bd60-088930dd7bce | -8.5214 | -43.2828 | 2025-07-09 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| d6924305-b96a-3510-9f32-32d3ba16b889 | -11.4397 | -45.0923 | 2025-07-09 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 92405c9f-845c-3af3-a2ec-785943a4fdc2 | -8.5028 | -43.2614 | 2025-07-09 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 510c8b03-e580-3666-ab00-6ecaa95ea8b0 | -10.5776 | -49.1316 | 2025-07-09 06:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ac68b2fb-a258-3d5d-9455-d8a9db610e6a | -10.5779 | -49.1098 | 2025-07-09 06:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 99ad6f0c-bc0a-336f-8b82-2709e30c3531 | -11.4393 | -45.1154 | 2025-07-09 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| de08bf7d-0abd-3911-bbd1-c7df4d6faa43 | -8.5025 | -43.285 | 2025-07-09 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 154.8 |
| 1114bc70-44b7-3813-9a7d-35252b366ca8 | -8.5025 | -43.285 | 2025-07-09 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.2 |
| b4ade678-d9a7-39d4-9c08-9834267ac432 | -8.5028 | -43.2614 | 2025-07-09 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| e827dbef-ff27-3013-8908-1e2e9dc09072 | -8.5214 | -43.2828 | 2025-07-09 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 3a84ada8-156e-3bf4-87b9-5bffb6618637 | -11.4393 | -45.1154 | 2025-07-09 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 02185e79-9645-3dee-9b79-1b7bea6f3e66 | -10.5776 | -49.1316 | 2025-07-09 06:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c58ef219-35ff-33f8-bc34-bd63f88560f9 | -11.4397 | -45.0923 | 2025-07-09 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 0784bf5d-ddc6-3008-a7d2-ed6ce45cab4a | -9.92635 | -59.9308 | 2025-07-09 06:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f4982290-608f-3510-b6d1-cfed4dc1320f | -18.63776 | -55.72381 | 2025-07-09 06:44:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 37f3b0b0-2ff8-3985-9e7f-8e78cd4d3cc2 | -8.5025 | -43.285 | 2025-07-09 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| 10265580-142f-3686-a7b6-4baf4c989eb9 | -8.5214 | -43.2828 | 2025-07-09 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 7a62df45-d4af-317d-8024-bca45411beac | -11.4393 | -45.1154 | 2025-07-09 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 024fdc68-338a-31e6-9cfa-1c557267b996 | -11.4397 | -45.0923 | 2025-07-09 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ff9fcc63-f3b9-35d2-b5d8-6de1ee440b3f | -10.5776 | -49.1316 | 2025-07-09 06:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| b749b8be-0fb6-3a44-856d-e030447d199f | -8.5028 | -43.2614 | 2025-07-09 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 2238cdab-632c-3b09-b54f-b4e9589b70b3 | -8.5025 | -43.285 | 2025-07-09 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 5b3bb48f-8490-3434-a491-d4d6735dbdff | -8.5214 | -43.2828 | 2025-07-09 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 927a96df-851d-303c-a277-0efa75dfbf9a | -11.4393 | -45.1154 | 2025-07-09 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 65bfd470-b8f6-383a-92be-4bfbdf224672 | -8.5028 | -43.2614 | 2025-07-09 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| fbe95e12-a3b5-36c1-ae9d-6b2cd93e798a | -8.5217 | -43.2593 | 2025-07-09 07:00:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 4fe6ce9a-ae18-3af2-b3a9-c04bd2ef3f79 | -11.4397 | -45.0923 | 2025-07-09 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d8f492f0-f7f6-3a84-aec0-672025fe2fd0 | -10.5776 | -49.1316 | 2025-07-09 07:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| f02a3421-9229-3800-abc6-f46415fd438e | -10.5779 | -49.1098 | 2025-07-09 07:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 6cf68574-a8e6-34cc-8d38-628181ba5835 | -8.5028 | -43.2614 | 2025-07-09 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 21dde481-478b-30a9-af3f-a79dbc228b69 | -11.4397 | -45.0923 | 2025-07-09 07:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b5c0015f-92b1-33ef-b418-f39d241dbe11 | -8.5214 | -43.2828 | 2025-07-09 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| effd5146-5665-3db3-a294-c4622be363b4 | -10.5776 | -49.1316 | 2025-07-09 07:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 6b17860d-2013-397b-a644-3bdf6279b109 | -8.5025 | -43.285 | 2025-07-09 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| ef8e9083-5663-3ecb-b968-12f6a784c5d2 | -8.5217 | -43.2593 | 2025-07-09 07:10:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 238bebfd-f0c3-34e8-9418-5ca376006fe5 | -11.4393 | -45.1154 | 2025-07-09 07:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 81e4198c-d271-3d75-a69c-54629aa54bf1 | -11.4393 | -45.1154 | 2025-07-09 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f47a823c-fc2a-383e-b71b-9192f9bcf26b | -8.5028 | -43.2614 | 2025-07-09 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| fdf1d796-be0f-3a21-a35a-1cc85d964705 | -8.5025 | -43.285 | 2025-07-09 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| c92c2766-5194-3033-a4b6-4b9ca71c10a5 | -10.5779 | -49.1098 | 2025-07-09 07:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 031b25e1-7136-379a-9a03-2c71b6a691fa | -8.5214 | -43.2828 | 2025-07-09 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| e0deb4cb-b511-3423-ab31-a1eee751bef5 | -11.4397 | -45.0923 | 2025-07-09 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2dba3dd8-93a0-3cb9-91b2-cb09491c1eb1 | -10.5776 | -49.1316 | 2025-07-09 07:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| cb10ad7c-fd85-3128-bc82-f4c109ab4963 | -8.5028 | -43.2614 | 2025-07-09 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.9 |
| aafa0187-8fc2-3f6b-94cf-7ce1e09b695e | -8.5025 | -43.285 | 2025-07-09 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| f4b9777b-55e3-3f23-866b-be35a90d58f9 | -10.5776 | -49.1316 | 2025-07-09 07:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 68627c4c-6c21-3482-bf35-4a3bb3e67f83 | -8.5217 | -43.2593 | 2025-07-09 07:30:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 9914b100-ec62-35bf-83c5-970a82d134b0 | -8.5214 | -43.2828 | 2025-07-09 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 453e8cf9-fc55-3cfe-ab9c-4cb7f4eac4ff | -11.4393 | -45.1154 | 2025-07-09 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| acecdef8-f74c-3bde-b750-317d7f912fc1 | -11.4397 | -45.0923 | 2025-07-09 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 976fb337-4b32-39a3-9907-552a0768006e | -8.5025 | -43.285 | 2025-07-09 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 0be87f5e-51af-33e3-8d0f-07d94337e2ad | -11.4397 | -45.0923 | 2025-07-09 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 2cfaede0-a3db-3047-ad6b-de10adabeb32 | -8.5214 | -43.2828 | 2025-07-09 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| fa583663-57fa-3545-828e-5f1690140d42 | -11.4393 | -45.1154 | 2025-07-09 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f68068be-bbbb-3493-8872-a5ab772d7083 | -10.5776 | -49.1316 | 2025-07-09 07:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| d533ad9d-20a0-3072-8dad-144f133dd118 | -10.5776 | -49.1316 | 2025-07-09 07:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| c5958fa5-4530-3ec8-85f2-4a9618147566 | -11.4397 | -45.0923 | 2025-07-09 07:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 00efbac5-08e0-333c-9dd0-3371e9d6a14d | -11.4393 | -45.1154 | 2025-07-09 07:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 194d7483-d18c-3298-9b8d-5d6ddeb5e357 | -8.5025 | -43.285 | 2025-07-09 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| f1de6baa-9c5d-38b8-bf92-61310adfa2a6 | -8.5214 | -43.2828 | 2025-07-09 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| d3546f11-b5eb-31f1-bae8-ed974db5af97 | -11.4393 | -45.1154 | 2025-07-09 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |


[Clique aqui para ver as próximas entradas](README26.md)
