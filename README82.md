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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f3fe267-f9ca-3c2f-9cd5-96b240d31b12 | -7.62179 | -60.85048 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 64c72fc0-539c-3697-9c4e-2d167e325828 | -9.4039 | -60.57075 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dee42bf8-82f4-37fd-8817-b64af4826244 | -9.21664 | -60.80771 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 083d8b58-2c22-38d3-923f-48219e91dee7 | -8.95323 | -65.96342 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f8045295-fd4e-3421-b28d-1115b0dddff8 | -10.47018 | -57.96101 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7f3ebe2b-2ecb-36f4-85d1-f8670ff234ba | -9.45866 | -60.30811 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b48b5360-2b9d-3b1e-8420-d8b2deacb1a3 | -9.82833 | -64.28781 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90984dbf-db7b-3155-82ba-65d29dacb849 | -9.40582 | -60.52179 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08ea3eef-b9cd-3939-83a2-b0c4a1bd7ce9 | -8.95207 | -65.94832 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3d993e5-add1-3f72-a3e5-6f0716799c2d | -11.23375 | -55.06399 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6c22dcb-0677-359b-9d57-e0294cfb678d | -8.93853 | -65.9462 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74c23f22-37e6-3dd4-b88f-67a26d81b461 | -7.27829 | -60.2938 | 2025-08-28 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0116645a-95ae-3b40-a1b7-ac2277694baf | -8.87316 | -60.75709 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b74c982b-6f68-3ef6-bab2-6e2aec2d674e | -8.6088 | -64.07732 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b42e0fa-1a1d-3637-950d-4b56516fb4da | -8.9258 | -62.42949 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dc71465-ebdb-3a4f-9e85-41be52eac501 | -9.54973 | -65.70146 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c2f52bd-712e-358e-b9d7-0f04e6fb0de0 | -5.99762 | -57.84969 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12f14804-12f7-3b11-9af8-b14f658f6660 | -7.40151 | -62.29036 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9d8bb30-8314-3518-bd85-e9956d3322ed | -8.8764 | -60.76687 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e19f6fb-50fc-3542-abbc-08c9fd04e317 | -7.63122 | -60.84741 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 917bcefb-afa7-3c7a-9ca3-8ab418409820 | -8.51424 | -69.79747 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce2085d9-7651-307a-8512-e493b83cddbe | -9.41312 | -60.53759 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13838457-5967-3652-a37e-6ddfd6bd8196 | -8.10067 | -71.24384 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35e887a3-0c4f-3395-8b06-72f192af133f | -9.41177 | -60.51278 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 349c4013-b5ff-3634-9a0f-9035d46c77ef | -9.1597 | -59.57176 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0c9b9ff-9746-3251-93a0-2452742b46d1 | -7.39937 | -62.2905 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe6c67a9-cc08-31e0-b616-033735be5e5c | -9.11404 | -65.78127 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 0080ede2-20e0-3f7e-b3f1-23db6babaeeb | -8.70401 | -70.54571 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 635775a7-9511-3edc-a8b3-39f4d4cc9922 | -9.4714 | -62.38538 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3270e715-ae16-3c74-b5ef-7e0913ee9a49 | -8.93059 | -65.93001 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53cb1c2b-27e7-3d4e-a766-4a04d6f76105 | -9.07071 | -66.06373 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bce7f7f-7050-35f0-ad1b-dfb75b59ec40 | -8.44342 | -70.14532 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc32c196-fda8-3e1f-9c7f-e0686abb1b7e | -8.3456 | -62.93027 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1345b397-8067-3ef7-b0a7-759a3d08f418 | -9.4098 | -60.52725 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30069cc2-a1c9-3014-bdc2-f01ef6413cba | -8.95546 | -65.94884 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21890a64-833c-3794-8a0a-cb4b51e7053c | -8.69979 | -69.66518 | 2025-08-28 05:48:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cd4664d-d7a7-31f0-a9a9-412aecdec537 | -10.47159 | -57.94956 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1afd35f4-5a47-34b0-894c-d4e3cc6c6166 | -9.26698 | -59.77411 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 003e7f6b-fd13-3a7b-94f3-1606126e76ae | -9.25422 | -65.89699 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4eae44b5-13d4-3635-8458-06fe69ebda00 | -9.19937 | -59.54934 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e8ec9ad-19dc-3a98-b461-943c5725d6fa | -7.59732 | -63.34113 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1281f25-51f8-3f03-ae76-caebba121e0f | -7.54155 | -63.84581 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f371165-b4cc-3303-b29e-21c744582dec | -9.12995 | -65.79129 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 732e00e4-3f4a-313e-b806-e1b46e6ba342 | -9.53166 | -62.4016 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f2f24c3-d876-34be-bf0e-63e7c149d7f9 | -8.87768 | -60.75775 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35783f81-7b12-349c-aeaa-1abc066d8c72 | -8.95888 | -65.97179 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f25c32e-8ec1-3583-b478-0540f6fdfb56 | -9.11319 | -67.70693 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d9a41b9-c515-36ff-a10a-83f8adc254f0 | -9.80043 | -64.2766 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d313fa4e-5a82-30d0-96c5-50906d28fb6e | -9.46875 | -60.30447 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b34e3fe-262c-388a-8af3-e26826599847 | -8.93114 | -65.92636 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84814453-2cd2-3537-b0b5-a9b9ad86d76e | -9.47653 | -62.37857 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1cfec82-7554-3c3c-b396-f9e7eb5427b7 | -8.37786 | -71.18463 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d590a808-97f6-3875-8fec-f532449d99bb | -8.95211 | -65.97073 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c86101a-feb1-3c99-8a82-71ea3934128d | -7.39538 | -62.28995 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06d9cf8e-27f0-3cee-8d6a-b083d5888388 | -9.15675 | -59.59322 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9be3d2d7-2872-371a-985b-9a2ef0004e29 | -9.48672 | -62.39505 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2287209a-c896-35df-b34e-61c2fd4002f8 | -9.03746 | -65.73169 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23b06fb0-ffa3-3330-be69-e42add655991 | -9.80921 | -63.07754 | 2025-08-28 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ebf1a71-aa5c-3888-82de-46158f2dd71e | -9.45198 | -65.41982 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9c0c899-cd5e-347e-b114-56550b18ea8b | -7.56516 | -63.86243 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| febc8230-d73b-30c5-8daf-c512e74db235 | -9.14751 | -62.35854 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1f82940-eabf-358f-905a-dafc7ded7ab8 | -9.12314 | -65.76746 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 689257e4-a40a-30ff-8d50-96c20ec8f79c | -9.11461 | -65.77757 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ed4922de-b172-35bf-8e80-c7d37134125f | -8.341 | -62.9346 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6f107f5-51b1-3286-8270-8e2a86ab4589 | -9.13936 | -62.35735 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1626e3c4-b310-3b92-9fb6-2ba5336b29d1 | -9.5503 | -65.69771 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5769a78e-b982-3de9-9b30-d5facc7ac8c9 | -7.37314 | -64.36776 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4e452877-56ca-3123-9749-3e30a6308dcd | -9.70961 | -61.2859 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14e4c508-b4ef-33b1-96e2-1247202a2ae6 | -9.16701 | -59.55519 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1dc04d44-3063-3ba0-821d-d445711e9e6a | -9.17554 | -59.49323 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba1e6bf3-083e-3bb5-aab7-461b4e8c2b8b | -9.02381 | -65.70683 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c38c8cb-5da5-3492-a648-d4609ed8fe5c | -9.40849 | -60.53692 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b52a5115-ba03-30a6-b73c-b71e2615ec4d | -9.02325 | -65.68768 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 317fb371-cc1a-3f12-addb-360235028dff | -8.34172 | -62.9297 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c70255b-6f63-39e2-b807-f9f4221bbba7 | -10.47486 | -57.93896 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 012e57f3-67ad-362b-b647-43f28d7744e0 | -9.14344 | -62.35794 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a8a395b-ba4a-3d19-9be0-9a37d4deab0e | -6.00775 | -57.85458 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2de2068e-41a6-3716-aac1-c702d9aae8f3 | -8.33957 | -62.94437 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00e3bf72-3c8c-3713-978d-4b9851d5d296 | -9.1946 | -60.80016 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e04ae4d-8f06-3b51-868b-92f83b107631 | -7.46768 | -61.39541 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7730d100-8cbe-3754-b01a-6e2ede440107 | -7.4457 | -63.16334 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0501bcd1-4935-31bd-992c-8c6c4584a110 | -9.17125 | -60.76844 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04354580-6216-3cdf-86d8-46cfe308167b | -9.02495 | -65.69939 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0740cf1-9e22-3b08-ae5b-d4d1df5942ee | -9.01301 | -65.70895 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cd6ae86-a073-3530-ae6f-2d5c433495f7 | -7.28285 | -60.29449 | 2025-08-28 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54c86f4b-61d5-3b11-a2bf-ce54d24fd19f | -9.22263 | -60.80599 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 154df437-0e2e-3237-996f-84012ce5dcb3 | -9.80864 | -64.2468 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d769104-c4ed-3cc3-b88d-c2c2a8c02423 | -9.41308 | -60.50309 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56a1ccc8-df89-39c4-ac4a-c12bdadceac2 | -9.53627 | -62.39853 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 284122f6-c9ae-303f-8c1e-11ae826523ec | -9.01129 | -65.6973 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19f93038-b99e-3c15-93b1-0fd96123845c | -6.00199 | -57.85717 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9a70ded-b99a-3fa8-8504-8b18be8abe8d | -9.17603 | -59.45287 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ea143a5-ceda-3e92-b82a-d6dcedb59b0e | -10.46875 | -57.9421 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d0d392f-905e-3048-85d0-a1074e07f44e | -9.13109 | -65.78387 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9647b020-cfc0-3f40-87d5-385f4c478a69 | -9.13961 | -65.77384 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd01a5d7-3d41-3d08-9575-6afb148a1327 | -5.99876 | -57.84961 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5f6db99-a9e4-39cc-8e43-9fb010381486 | -8.88221 | -60.75838 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09ac6dcc-b11e-379c-95c0-e3fec06b65fa | -8.90664 | -62.47748 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69cd314d-1b0d-3cb2-bb05-0830476dcebd | -9.01528 | -65.69409 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b68d3266-faf0-3b0b-a805-4cb94201d396 | -8.95885 | -65.94936 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README83.md)
