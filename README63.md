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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bed444e-5cc9-327b-acad-a97666400edf | -8.5934 | -66.81702 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8216887-bab9-3d6f-9171-72e7e590a200 | -10.99468 | -59.14977 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 548d609a-827c-3fba-95c1-0404daf1b370 | -9.40508 | -65.90831 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4222a203-393f-363b-b9a7-7a3c7b429358 | -9.14785 | -68.23924 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1973474d-079f-3f98-a62c-ef371ab46f8e | -9.15308 | -65.40105 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0f47269-50ec-3c54-9b72-1858829661fa | -6.07565 | -57.80183 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 023f04ea-092a-3ed8-8027-578421574f91 | -8.58885 | -66.81286 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3ad9f73-d221-3662-bb68-b05509c42010 | -9.48579 | -64.69085 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53b1c8a0-5ee8-3913-a747-27e610913bbb | -9.15396 | -65.39619 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3d3d5a1-f3d9-3bfc-8e49-23131fa20b18 | -6.49395 | -58.52635 | 2026-10-04 05:18:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a887af23-3ab2-3cee-848b-bc4d070b8f7f | -8.55298 | -67.06535 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72c8e897-6760-3ca6-a288-8ee1ee3206aa | -8.73591 | -66.5744 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b596a3-1e3c-3a5d-a1c8-a8d75e15af57 | -8.58313 | -66.81501 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 796485a0-5896-39a3-8bac-d6436e035702 | -8.51185 | -67.11139 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 536628ae-8b15-3a8b-84b7-1a878e026574 | -8.61801 | -64.22738 | 2026-10-04 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 385328ca-ab00-32ff-bdf0-5a20590c4991 | -9.94839 | -59.60967 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b1172c-1744-385c-938c-c84c3237ef3f | -6.06941 | -57.60603 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8eeb8ace-0c35-3a88-b28c-0b431d58373f | -8.85652 | -66.79337 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37742b92-56a1-38a7-9686-f2a2e7473312 | -8.34747 | -62.8323 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e5b9f01-a97e-37c0-b5cf-f7b3cb57b5f2 | -7.32942 | -55.02762 | 2026-10-04 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 795352af-a61b-3ae0-b1ca-96f6e14c54fc | -9.92644 | -65.03571 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50e77a69-1d2b-3977-b97d-197d9ca5d66e | -6.06501 | -57.61241 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4c618f4-4fcd-39e7-a407-0a638da36529 | -9.47563 | -64.34058 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73225437-3906-370d-8929-750917fb6955 | -6.09758 | -57.66361 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cd2686a-2efb-3dc6-85f6-a578c4b70865 | -9.13207 | -65.95002 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cfecc9a-bd97-38f4-8d18-37a0830eedee | -10.22321 | -59.08844 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3852fa38-3c5a-374c-8dde-dfee4d0354a6 | -6.02429 | -57.69804 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18aa5acc-8f24-33f5-b638-09a6d8dd36cb | -5.93712 | -57.73371 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3989e0a-2c0b-3f4f-a5c7-4669174515c1 | -10.26762 | -63.83748 | 2026-10-04 05:18:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d04fe56-b06f-37b9-a87e-11db9c43bb56 | -8.58008 | -66.82373 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37bc738a-bfd3-3686-a454-41a3760902b0 | -8.89361 | -66.73419 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaf9286e-0202-3121-ad70-a7948f229e77 | -10.99525 | -59.14625 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5224487-5251-3299-9a1f-023ef65c4b82 | -8.57413 | -67.00925 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34655e72-9e44-37d0-9da6-f45adfb42ba7 | -9.70105 | -57.45042 | 2026-10-04 05:18:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5b5b5dc-51b6-3c3a-9b32-fa8d5843ab4d | -9.69717 | -57.45343 | 2026-10-04 05:18:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce00cb7d-9f86-3e01-9f02-0bc56b52a40f | -5.87756 | -57.72428 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 908f2587-ee77-39ff-b00d-36f64235c999 | -9.15899 | -68.27314 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbd47c9c-a7f5-36f8-9980-12de5ca9efa2 | -9.65415 | -63.44684 | 2026-10-04 05:18:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5748c60-7595-3f2c-ac2d-587c9b7d3edf | -9.08669 | -61.16047 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8e5f3a14-37f8-30ed-96fe-4f6305de05cb | -10.21933 | -59.09142 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a2f4b08-3f1b-342e-8114-30de25136aae | -9.01638 | -65.68867 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1e74913-6098-3a4e-b74b-4cd244b157d8 | -10.95606 | -60.90756 | 2026-10-04 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd5df4e2-f008-33ac-b60c-b15ba3de2d8f | -6.51393 | -55.39376 | 2026-10-04 05:18:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cb76a17-118f-36ff-8127-815384e95c4c | -8.60028 | -66.80862 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05bb3e48-bc78-3005-b8a9-d8d364751b9a | -9.92483 | -65.04475 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ede86c5e-315d-3e91-8759-af30992ebf9a | -9.13611 | -67.93406 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db598de9-f7ce-323f-8d68-8079350d91b9 | -8.51711 | -67.11237 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f63177fc-a1a2-37cb-bb59-41e87a5c0470 | -8.34086 | -62.84708 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4770d62d-cf36-3044-8a50-19b564c8d916 | -9.08959 | -61.16518 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d19bb9cd-ef30-3911-b5b5-2215512fc9b8 | -8.54347 | -67.02995 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f294090-86e2-3bb4-8828-f4f18bbf93f6 | -8.54404 | -67.02672 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b4655df-97d5-3b6a-8445-ae9ff6850c2e | -10.58838 | -57.50227 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc121859-9ab0-30d0-8f5f-f96646ec77f3 | -6.10089 | -57.66414 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea60c65e-2888-344b-93d9-03f58f74f4bf | -8.96214 | -62.34479 | 2026-10-04 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 206dc7e8-e955-3451-b5fe-a3aac28fed98 | -10.60182 | -53.97009 | 2026-10-04 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c42d026e-f177-30dd-a3e3-61772eaeb46a | -8.57166 | -66.81937 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c39c1c75-578d-3b42-a847-8c7101138f56 | -9.89398 | -65.01114 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c2e6aaf-584d-345c-8943-5bb1c1cb2045 | -8.57068 | -66.99864 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0128e125-2d5c-3449-b846-9d1f086548f0 | -8.34835 | -62.82715 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96735da0-16a5-34d7-9828-4e8378b161a9 | -9.90778 | -65.03689 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98de9435-6ad2-39d6-a81c-e7ba15d3b816 | -8.70993 | -61.39721 | 2026-10-04 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3829d9e4-57ba-3de0-99a0-72c1c63e5fbf | -8.5997 | -66.81177 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 440e10e1-3323-3259-bdf6-a7d54871aac7 | -8.71356 | -61.39783 | 2026-10-04 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7af38836-c038-3fc9-aac1-801a36033909 | -8.88799 | -66.73617 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 953d6d28-8839-3522-89e1-f394c3f7f6a5 | -7.32588 | -55.02707 | 2026-10-04 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f66c8a1-a3a3-3f78-b760-04e60e6457ca | -8.57009 | -67.00185 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cd78fbc-6300-37bb-8438-ead7617bdceb | -8.89283 | -66.88658 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8882ab4e-afbc-3765-aada-3d269fbddd28 | -9.69105 | -66.39805 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a83ab431-2be2-3024-ad3b-197543ae4ec3 | -8.54327 | -67.03008 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 821fdaff-5b94-3deb-9376-df9426a7020c | -9.89845 | -65.01196 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f333173-88d8-33f1-a12d-df9f3148ab5e | -9.47207 | -64.33568 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 088e2e3e-9f12-3b4f-b1a3-fa43138886e4 | -6.43812 | -52.70759 | 2026-10-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6adda39-7fa6-3b2c-8079-c2a34b9e9e88 | -10.5397 | -57.96944 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f4d0280-fa52-3b7f-9070-d057b703d98a | -9.17234 | -49.9472 | 2026-10-04 05:18:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75ae1f9e-16f1-335a-b358-8f44118370e4 | -9.79141 | -60.13863 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e446fe30-4d74-3606-8c67-78cd543c1e88 | -9.01546 | -65.6937 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1c9177-ac30-3d17-ac48-1cc100730380 | -6.09703 | -57.66707 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4aad190-5d4c-322d-8695-bcc377f67171 | -9.79482 | -60.13919 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 225717ae-db20-314e-becb-efa21f1c9abd | -10.83159 | -57.20927 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dd578cb-4305-30db-8f40-3d56b995ad34 | -8.58064 | -66.82057 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 821f9803-c5d5-3598-9a5e-29cbc8e04209 | -9.01361 | -65.7039 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f317fd6f-846a-3d18-af23-b45607c7fbbd | -9.12619 | -65.89967 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68c3ee2b-7b79-37db-8ff8-e98c47ee8320 | -9.13118 | -65.46819 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab5a9228-de74-3969-88c0-8d8afe1b80b9 | -6.05792 | -57.69983 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e4bf955-0f72-31ad-b438-c77a763be958 | -8.55358 | -67.0621 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50a9e963-348d-3ca0-963d-f458fe0b0e54 | -8.96133 | -62.34951 | 2026-10-04 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c88338f-9a15-30a2-bd9f-959ef4467ead | -9.69995 | -57.45749 | 2026-10-04 05:18:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16c8e714-fb40-334b-ae6b-c0faecc5863a | -9.91182 | -65.01443 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eec6ce81-56e9-3011-a856-7123577c319b | -8.88085 | -66.89405 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd204a03-77e9-30c8-9e8f-b8bb407bb0da | -8.60772 | -66.97281 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1997068-1135-3d40-855e-49b641ad51d0 | -8.65281 | -66.93652 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2be4eb7b-a914-3266-bd0c-d65d42dde797 | -6.45405 | -55.46191 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ead68ef8-6542-39a9-92d0-caaf6a19ba1f | -10.83832 | -57.21033 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f79d9a-b08a-3c87-b490-43216150081d | -8.56286 | -67.07056 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1476a4a4-4e59-3be0-9902-c257f624c439 | -10.0128 | -65.23757 | 2026-10-04 05:18:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e4c1987-bfe6-3082-8a62-e8b7444396c5 | -8.57492 | -66.82278 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56fb3b81-a174-3d19-96b1-807ffcf4685e | -9.02889 | -67.47352 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fd7bd44-3d09-39c4-8211-d226e585c486 | -10.99137 | -59.14922 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be83f527-33ec-35c4-a91f-4394ee7a0e25 | -9.69939 | -57.46102 | 2026-10-04 05:18:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67a9c27f-c3db-3871-8248-acb8f20bdff8 | -9.13092 | -67.93157 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README64.md)
