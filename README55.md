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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 794ef1c2-a635-3e61-9cab-19fad39ad3a5 | -8.63325 | -67.26766 | 2025-08-20 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99066b38-7b97-3c4e-a928-77aeaaf26d8e | -9.896 | -64.26105 | 2025-08-20 05:50:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40cedbe0-0fa3-37ff-a347-9cc63fbc38ba | -8.30175 | -70.74708 | 2025-08-20 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e3b2c4c-13bd-34cd-a5c6-aaec9e00fb14 | -13.1547 | -54.91877 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 194696ed-0042-3c5f-8d0a-6df77da9ffd4 | -10.91444 | -57.506 | 2025-08-20 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e1b0155-69a3-32d2-8561-d21811597b7d | -10.24938 | -68.26488 | 2025-08-20 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aeee93b-ba45-3830-a1f8-37ec67486030 | -9.20996 | -59.69286 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12eab0e3-d8ea-3a3a-b7b8-0dcccde98db7 | -8.56607 | -66.95686 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 137ca82d-5db9-36f3-826f-04af4e4a2ae4 | -8.97122 | -60.49617 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e931467-656d-3ccf-9322-958b2130b9ed | -8.55829 | -66.94132 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f234798-c1fe-368e-9adf-6611b773377b | -9.51317 | -60.52326 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff16be3a-e759-329b-b3ee-ae3040c6f2db | -8.96989 | -60.49711 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d15ed7b-8170-3f3e-829f-912917372e59 | -9.17478 | -71.9424 | 2025-08-20 05:50:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d83c8cc5-7554-387d-bbd8-904fcb1be361 | -9.1888 | -59.62721 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c292f8d3-5ab6-3a38-a657-0fc9849d0e82 | -9.22767 | -60.33804 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 04c3c3af-5343-3c40-a14f-8b76fc415b20 | -12.96727 | -56.85174 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6e897bc-6706-396e-b5de-5f8fbaf8f20a | -13.1597 | -54.93968 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 878842e7-84a8-3c76-b571-3b3437c3c673 | -8.76192 | -64.19566 | 2025-08-20 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d293dc2-13f3-3170-b7bb-9e7c5e9665fc | -9.22848 | -59.60444 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63595ead-d33b-36cc-8248-c0370930c09b | -12.97809 | -56.86848 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32ccb5f8-537f-3812-aea8-a9af5934752a | -7.78653 | -66.96276 | 2025-08-20 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e6c007b-7c8f-38d1-9318-0efb7d660662 | -12.98271 | -56.88394 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0420e7ed-04e1-3d9d-8662-f6b210cfc359 | -10.55175 | -62.74039 | 2025-08-20 05:50:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1723cab1-ec2a-3d4d-bd6e-fe1164bde475 | -12.97916 | -56.85861 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62879509-ddc8-32e2-9e61-2dbccf353e77 | -9.19018 | -59.62771 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 19d9491d-1147-39e0-9363-b89811cd66d3 | -9.21747 | -59.68859 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b3e7196-fe1f-3060-b6d2-9e7a40d0422f | -9.18945 | -59.63336 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1b74cc38-e3bf-3736-b4c6-499958e0024e | -12.97239 | -56.8628 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c493ec7-4391-3508-886f-0ca316bd51b0 | -7.90185 | -61.52213 | 2025-08-20 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6423665b-ff17-360b-b41b-2ccc95e108a4 | -7.96892 | -55.30764 | 2025-08-20 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6d56592-abfe-379c-8465-447b7c0b9fde | -7.4472 | -63.02924 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12b6568a-a3c8-334f-9e23-ab4c97c9cec4 | -9.19437 | -59.63424 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b4ff1594-8fca-3b33-b05c-a14e28d83a3b | -9.24189 | -59.61763 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fea2ea35-ffc5-39a1-a329-daceff6bcb35 | -12.97361 | -56.86744 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f82ca7f0-b5d0-3d70-8622-fd235457672f | -12.96672 | -56.8568 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7399619-1d25-315f-8e7e-0f7886007735 | -8.88301 | -62.40362 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aff7870b-c02b-3d09-9efa-2c1949b347de | -8.88353 | -62.4 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3971d435-b869-37b0-a4d5-0bd00ad15ef6 | -10.45066 | -64.4066 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b549df9-c668-3673-80db-66da9656b9aa | -9.23766 | -59.61139 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7dc946c-9a03-36fc-b1a1-45a1de302ff5 | -13.15403 | -54.92543 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b4edc4ba-885e-3c2a-9968-ee670b3f50a9 | -9.52588 | -60.53518 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f3854c1-6f08-3c01-8d50-642e3d3ca76c | -8.97054 | -60.50102 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0fc0d2d-6fd0-3318-acd4-f015917404f6 | -9.23345 | -59.60508 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4354c11b-5e00-3215-bc93-bc4fe28006e7 | -9.22997 | -60.33552 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 7ff91c2e-b79c-3e0e-abd5-2fed6c20c6ef | -8.75827 | -64.19511 | 2025-08-20 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 236da2cc-cd66-3718-beee-663ac4a8ec85 | -8.96925 | -60.50196 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a70b7a00-db04-3ce4-9e82-be8c40b730f6 | -7.79038 | -66.9598 | 2025-08-20 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1894d50c-4208-3823-a9d2-2d62bb1fd3ae | -9.1808 | -59.64903 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b50f6de8-4662-381f-ac3e-0d1587461a01 | -8.63433 | -67.26071 | 2025-08-20 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12455d4a-14e3-37b0-b2f7-c3c438d5fadb | -12.97403 | -56.84767 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f5ad815-58a0-3dda-bdef-d41c6f64b8f1 | -10.46439 | -64.46681 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afad7cf5-356d-3128-8c8b-2ceb004c3ea9 | -14.61709 | -54.9121 | 2025-08-20 05:50:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 16d4961a-eeee-3784-8d28-b9525c388294 | -10.24994 | -68.2614 | 2025-08-20 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7924e93-a37a-30ca-960d-98a2823a19bb | -9.20934 | -59.62442 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f68cdd3e-fa7b-3fed-af7b-f2c4d47606e4 | -9.22836 | -60.33306 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 18db4339-221e-31b1-8d1f-4fdbdcbf837e | -8.69751 | -62.09838 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 300eddd5-1171-3c3f-aa1f-b03e615ad72d | -9.21142 | -59.61927 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b583c1c8-0e62-39eb-9e88-7790c9799fdd | -8.96252 | -67.72955 | 2025-08-20 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f82ba183-08e5-3638-9853-71d6c202137f | -15.00113 | -54.81773 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 13c8af9c-99c3-3769-a932-1dca1651cb52 | -15.0018 | -54.81062 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1f50b9fb-c3aa-3d50-ae68-7b07afcd3bae | -14.62098 | -54.91029 | 2025-08-20 05:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0408a1c6-fb3a-30f3-9f5d-69ec5c70d6e5 | -15.05733 | -54.83749 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e50fd6f1-e915-319b-b34a-3b59a6e8ec4a | -15.05998 | -54.83893 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cabc6cf-bb7f-3865-bdec-4eea6cb3a4bd | -20.52098 | -57.40419 | 2025-08-20 05:53:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 91e2a85c-8c02-3e60-aba9-988478da5469 | -15.01471 | -54.82771 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d6264fd-5290-3944-8f0e-b3d81d3f078b | -15.00046 | -54.82483 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aed22f03-4073-3ff7-8c30-83a1fa7d6e4b | -15.02181 | -54.8294 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df48ad2c-fa40-338f-b23b-6ccca86698d3 | -14.62292 | -54.88935 | 2025-08-20 05:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8e13b48-6c5e-371e-a82f-25cffc6d45ae | -15.06378 | -54.8458 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 718d0e0f-567b-3ed8-8506-80c1af4e36f1 | -14.99979 | -54.83195 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51178299-1bfd-33fa-99a3-8fa054a84215 | -14.63075 | -54.88263 | 2025-08-20 05:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea954244-3f63-3700-a24c-6ceeab0214f8 | -15.06449 | -54.83844 | 2025-08-20 05:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76ec171f-4fe6-3864-9339-9cd031276ef4 | -15.0502 | -54.83621 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 823d5292-2537-3742-bfa3-48db55706632 | -15.05283 | -54.83777 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7f10f84-23c9-3362-aa08-779c5fa23e19 | -15.05347 | -54.83078 | 2025-08-20 05:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f5bf059-1187-3091-ad44-fcb371756001 | -20.528 | -57.399 | 2025-08-20 05:53:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdffacca-3416-3691-a792-ec8cced90050 | -4.90953 | -43.22957 | 2025-08-20 05:59:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| ef23b145-6c04-3644-8406-ce4ad82b52bc | -4.29499 | -48.06644 | 2025-08-20 05:59:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 70efcdef-fbef-3d6f-8a8a-aed137dd508f | -3.98046 | -42.50531 | 2025-08-20 05:59:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c5991a71-fe90-39d8-9c5d-9abeca0b7a60 | -6.0701 | -44.11779 | 2025-08-20 05:59:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3980177c-0194-384f-bfe6-94c9501820a3 | -3.2271 | -46.79603 | 2025-08-20 05:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 83674779-5dad-361a-9c3a-d133a11f32db | -6.9505 | -42.8536 | 2025-08-20 05:59:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 7a9dd428-5a4f-35b0-a389-e6049f3727c6 | -6.06358 | -44.10967 | 2025-08-20 05:59:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e0012de5-645f-31f6-9532-0ad21049b11a | -6.94804 | -42.8713 | 2025-08-20 05:59:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 3ed5512c-8e77-3e92-8992-0231f810a4c3 | -6.85632 | -43.61116 | 2025-08-20 05:59:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2be98501-f6a7-3f46-aa0b-d05674def5cd | -4.3086 | -48.09521 | 2025-08-20 05:59:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f0e9afb6-7040-3bf8-956f-4bb9b435d3d0 | -5.97995 | -44.1328 | 2025-08-20 05:59:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b5bcc45a-23fc-300f-9ae1-6d4dfd393a0d | -4.4226 | -47.75444 | 2025-08-20 05:59:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e173d893-4d7e-3bdf-8ded-ddc2ac25c2a1 | -7.58932 | -44.38342 | 2025-08-20 05:59:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e5069263-40d8-388f-9b78-8234197955ab | -5.75724 | -43.98537 | 2025-08-20 05:59:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 39783ce8-629d-3bf8-b7cd-695a432b5e29 | -5.97429 | -44.13992 | 2025-08-20 05:59:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5c13cbe5-ee57-3f4a-ad5e-0936545f58a5 | -6.613 | -43.87053 | 2025-08-20 05:59:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fb649471-5dc2-3344-b796-6b634d52ca9c | -5.98818 | -42.82145 | 2025-08-20 05:59:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6490a996-2745-35e9-a1f5-c9a74ea083ee | -4.91188 | -43.22284 | 2025-08-20 05:59:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d0a6f24e-43a9-348a-84ac-ce411a55eb80 | -3.236 | -46.79732 | 2025-08-20 05:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 1ef88314-5d10-32d2-9040-7052e52cf93c | -2.90122 | -48.28808 | 2025-08-20 05:59:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7f65eae-2405-3023-846c-c7aea85ac2b9 | -2.89989 | -48.29687 | 2025-08-20 05:59:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3b9c499-dc20-36d5-bfb1-233ca5d2284c | -7.65538 | -45.25151 | 2025-08-20 05:59:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aeb49e54-3c09-3fb5-a3b7-fa0a0882f17f | -4.90965 | -43.23805 | 2025-08-20 05:59:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| fd70513c-b378-34ec-851c-3306c4d5fed9 | -2.38526 | -47.65931 | 2025-08-20 05:59:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README56.md)
