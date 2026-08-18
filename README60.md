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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f0521a0-edf1-3605-bdb9-0242c23c5a57 | -9.42505 | -60.41883 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2834853-04ec-379b-a35c-737136755330 | -9.42512 | -60.41916 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 095ffc45-dd31-33e8-9194-60c7747ed5cb | -8.97126 | -60.52524 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 285c478a-fa4b-3d4b-9d65-2f6240b74d8e | -9.16377 | -59.67189 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 083357d9-9333-33ba-8f8a-e4d4b51459bd | -9.16919 | -59.709 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a82c5fc-3936-3b64-9f77-0e32abfd9a15 | -9.12725 | -61.60549 | 2026-08-18 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aecda96c-4188-373a-a5cc-665bea966e49 | -6.95623 | -59.0308 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ce73ac16-edfc-3315-b05a-12e6c83e5c06 | -6.96224 | -59.03783 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c7f9a82b-51fb-3d3c-82cc-20b72e0db354 | -9.16991 | -59.70297 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 559e1b3d-c0c0-320e-ad97-276ebe1ae93c | -7.9033 | -61.73296 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac78d899-6458-3f5a-a191-4530a7a3aec8 | -10.41476 | -61.20866 | 2026-08-18 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4150b9a-2c86-3b5f-b93f-3ab5c8630a7c | -8.94751 | -60.54786 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82c4c9ce-5101-33cd-8a61-cefcc2afe08e | -9.4281 | -60.44597 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9010ca1e-f5c4-32ea-aea5-f94b93da25f8 | -10.41415 | -61.21367 | 2026-08-18 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95b51b49-e309-3f25-b548-6159aaaf4468 | -7.91494 | -61.73454 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| feef3f86-fc50-3f8a-9972-3232b3780601 | -9.42255 | -60.44022 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27a4243a-e3af-3fb2-abff-87d14dd126d9 | -7.90385 | -61.72884 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8531750b-4fbc-32ba-a09f-6cc40edba620 | -6.84565 | -59.01629 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b8217ca-89cd-39b8-9f67-56d9ef5152ec | -6.84641 | -59.01039 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 92454847-0e3e-3834-b1b3-002e2ca076c9 | -11.22174 | -64.9809 | 2026-08-18 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30a2495d-d97f-34a0-8fa9-710c34472c00 | -6.95528 | -59.02443 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1cd7d1fa-0132-3126-beb6-44e26581af83 | -9.42191 | -60.44546 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 247dd567-b81c-36c5-8d65-61ab2c0e86f6 | -9.01143 | -60.50478 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9033cb8-0e62-39c8-bf5d-cee06a24a701 | -9.01212 | -60.49958 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dfceea4-2fa6-34db-b8e9-ce2509d4a1ac | -8.96285 | -60.52927 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 843be6ea-a9a2-3ea6-b1cf-3bf946d781fc | -9.42642 | -60.40825 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 235d78ce-0a17-3796-9011-fec8e0e66add | -6.91021 | -62.90516 | 2026-08-18 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32c38639-a677-3c1f-9f33-f827d2803b19 | -9.52989 | -63.66328 | 2026-08-18 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01611212-cade-3d2f-bdfa-915ed584140a | -8.96219 | -60.53437 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a907ffc-1a64-3613-9d66-d0db1f758610 | -8.73089 | -62.90979 | 2026-08-18 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25bada77-6d95-3940-bf32-5f145fdad6be | -7.55198 | -61.18421 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61818a41-7981-3e9c-a5c5-a57029b21889 | -8.95649 | -60.52833 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd54cbce-0080-3f8a-986a-5322e0f997cd | -7.90276 | -61.73706 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 969290f1-8830-3bc7-957e-2790e87a4316 | -9.42448 | -60.42446 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e4c64ed-53c9-32a4-ad8f-c8434f3abf17 | -7.60727 | -60.95361 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947f0cca-a66d-3bb1-9f59-16f1534852c8 | -8.72591 | -62.90554 | 2026-08-18 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a1aac59-8e3a-3cd0-b5a6-6a8d1c837b73 | -6.96041 | -59.03764 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb99a521-e7a6-3f2c-9ab3-8d8507575532 | -7.88311 | -61.79634 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0996a576-14c7-3ab0-a482-a43dbfbdad97 | -7.60502 | -60.82977 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22b48091-1740-35bb-aa8c-b401afc5dfe6 | -8.90158 | -60.6044 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7501e455-ff5a-3ba4-abb9-8691ce991421 | -8.89525 | -60.60354 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea4e5e0d-1336-331f-9a70-2886291f4932 | -7.60666 | -60.95814 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88381d2a-f9ee-3a2b-82f1-da256a030017 | -8.90223 | -60.59921 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1876b828-c0d1-3a25-838a-b22b434f7d63 | -9.42167 | -60.44508 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bda5501-ea55-3593-bb81-0c547db9ab55 | -8.72638 | -62.90203 | 2026-08-18 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42561c9c-a063-3752-978f-0e4ae7f1c790 | -7.90912 | -61.73375 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bb0878d-75b4-33cd-be4a-a8a47ca125b6 | -7.91548 | -61.73048 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7a8e76b-5645-332c-bbf1-41fc67b8a152 | -9.42769 | -60.45174 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aabd8cfe-52c0-375e-b5ec-8ccb11958f0b | -8.95386 | -60.54873 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c7650d0-86a9-37ff-a16d-6efd9e9a8202 | -9.42834 | -60.44638 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7aebed24-bc51-3912-9218-5b9bb909e0c8 | -9.42946 | -60.43547 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfb276bd-1d91-3670-b985-8590ec019bee | -7.60789 | -60.94897 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f90db49e-b36f-36e3-a4c2-fa1435b1590b | -8.96988 | -60.52496 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91cf7005-2294-3669-924f-7b2e1e84b69c | -9.83746 | -65.05862 | 2026-08-18 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1bf2400-acb3-3c8a-870c-fcc3a181871c | -9.16302 | -59.67787 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f924682-114e-363a-a63b-f0d32ed11d78 | -7.88972 | -63.76056 | 2026-08-18 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef242c5e-0e8f-3b80-b5f0-72c7b967d3de | -9.20068 | -60.89043 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24ff0ce5-f514-31e9-87e7-3fa8189236b6 | -7.9144 | -61.73859 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e359965-2bfa-388c-ae40-ef75142d0336 | -12.23732 | -61.95086 | 2026-08-18 06:20:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f382154c-9f0a-35b1-811e-74f407eaccaf | -8.10224 | -61.34731 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df9d6b37-8519-332e-921d-356ef0848c41 | -6.91598 | -62.90263 | 2026-08-18 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adca718d-362e-32de-9d51-3ff4190bb23a | -6.96208 | -59.02533 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cfd5b68-0057-3dde-bc4a-11deee7f776d | -7.8889 | -61.7972 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 671c95f7-aef7-3f06-b2b2-a59fb45d84eb | -8.7323 | -62.89927 | 2026-08-18 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4daad6d-33d1-3baf-b5d9-d7f6e14d2604 | -7.61461 | -60.9451 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51db8113-bd72-322a-97e8-7cfb7635f0bb | -6.85247 | -59.01702 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 82e018a5-3425-3ae3-bb4e-5265b5a79685 | -7.92021 | -61.73949 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff5bb9c9-5da0-3597-b0fc-85bfd8b03d33 | -7.90804 | -61.7419 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 695bee2f-6862-3476-be0b-e9fc93a7aa15 | -6.95444 | -59.03067 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ee47db7d-4a4b-345f-ab85-b6217ad9b207 | -8.09629 | -61.34629 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44075899-0c08-311f-896f-277e5f254944 | -8.89656 | -60.59307 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e170506f-d1dc-3b5e-9292-a294ca1d5283 | -8.89876 | -60.55541 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0f552b1e-6ee2-3039-a028-a4c10c41ecfc | -9.12129 | -61.60467 | 2026-08-18 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fb7de03-4238-30a2-b89f-fad48cef8f4a | -9.05535 | -70.9155 | 2026-08-18 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a28b4fa8-e0b7-37ba-9875-6e34031d7f00 | -7.61334 | -60.95457 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4341c257-4d72-33a7-b59d-83482d206b48 | -6.84885 | -58.99144 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| da8acbab-cfdb-3116-bc0f-22b5c3c83ecd | -9.16671 | -59.70272 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67e4b8aa-8d4e-3052-99e0-834e4d88eb32 | -9.42577 | -60.41385 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c6c91f8-a57b-31c5-a65e-c8794bd0fc80 | -7.55256 | -61.17985 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75643e87-8731-30b5-ade7-5589c1b61609 | -8.90173 | -60.552 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b095aae-fad3-33d4-9442-d5b7f10dfb54 | -8.85752 | -70.84071 | 2026-08-18 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95ebc33e-0368-3f5d-8ca5-90519fb9eff6 | -8.73182 | -62.90278 | 2026-08-18 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04e04f4c-f976-3170-a41b-d2ce23405649 | -8.90109 | -60.5571 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2abcc470-93ee-398a-9edb-24cad5cb073b | -7.59998 | -61.23568 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6bb551c-963b-30cc-bb6c-d82ef10ae476 | -9.01265 | -60.50516 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1fbfa30-4364-34c0-a457-ed1cc47308c4 | -8.72685 | -62.89851 | 2026-08-18 06:20:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dc82cf7-19f2-3a17-8933-c440194bac13 | -7.90966 | -61.72969 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f73ab51-3463-39e5-ad93-43307ff89ee5 | -9.42963 | -60.43586 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9fa4253-309c-3e3a-8fd3-b5e77b784b44 | -7.92076 | -61.73539 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb86791e-8518-3f0e-97c0-b95cd07581f6 | -9.16593 | -59.70891 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a997501-2771-3f8a-85ad-58c29b40c911 | -7.87916 | -63.76205 | 2026-08-18 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59510dcd-34d1-3459-91d3-f73a39c8325a | -8.89538 | -60.55112 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bf1d4e5-fd9c-3c01-bfbc-09b818f86a05 | -7.61275 | -60.95905 | 2026-08-18 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 798f75b0-2919-35c3-97b5-b98c83d97400 | -10.57793 | -63.5479 | 2026-08-18 06:20:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9dd447a-684c-38af-aa3e-46aa7901cd89 | -6.84722 | -59.00409 | 2026-08-18 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 424f2d00-8626-3ac0-8f37-31ba96772a9f | -9.42126 | -60.45081 | 2026-08-18 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cccff488-128e-3aed-a54a-b157b4538030 | -8.95716 | -60.52319 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 434b5ce3-fb1f-3318-8bf6-feebd11c74f1 | -9.16749 | -59.69659 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cdf0983-f71a-3761-a6b4-b10cc3e364d6 | -9.0133 | -60.49994 | 2026-08-18 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdfdcf3e-d80e-3a80-b209-05390c974991 | -8.09032 | -61.34538 | 2026-08-18 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README61.md)
