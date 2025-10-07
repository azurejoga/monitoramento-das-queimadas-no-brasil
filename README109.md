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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 117cca99-5361-39eb-ad53-ef24df439f26 | -9.14727 | -60.63051 | 2025-10-07 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1e7867e-2b09-3cf3-9c87-15fba80d1f82 | -8.06862 | -72.34457 | 2025-10-07 06:18:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9347f049-844b-30a4-ac93-cda0d6cc1fc2 | -8.22459 | -72.82188 | 2025-10-07 06:18:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab9402e4-b046-351f-a79a-e1c39afcc484 | -10.84095 | -69.14519 | 2025-10-07 06:18:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06621f9d-9e03-330f-b41f-8ed4f5daa382 | -7.49381 | -63.67385 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de186769-bbb5-3d2b-8af1-38c3332bf907 | -8.9053 | -71.37279 | 2025-10-07 06:18:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e417c6e-9843-316f-a22c-d74477d70735 | -7.43227 | -63.74917 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e4e194f-5331-3bf3-82c0-37eeeeede83b | -7.43276 | -63.74546 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 744f2590-36a2-304d-91cd-e563e6a13e47 | -7.48041 | -63.55971 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cc8a06f-7061-3c1b-bd36-58e09aa697ce | -9.56164 | -63.50714 | 2025-10-07 06:18:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec964c5f-3e14-3493-9d15-d02dd0137616 | -9.75382 | -62.27417 | 2025-10-07 06:18:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a67b728-d059-32df-947e-da7067731443 | -8.23253 | -61.17688 | 2025-10-07 06:18:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa3d3ce1-7a55-393c-bbc8-524c57060c07 | -7.42926 | -63.74655 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0407b103-f794-3f05-a1ed-3ebce27a2b8e | -6.95705 | -71.4976 | 2025-10-07 06:18:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 558d0771-7e3c-392e-b39e-420e25584def | -9.20012 | -62.59407 | 2025-10-07 06:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c0ede93-9b58-3de4-9333-71a59da1ed84 | -8.22587 | -61.17602 | 2025-10-07 06:18:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9669fa2a-1a4f-33e9-8bcc-1a5452bd90be | -8.90307 | -71.34032 | 2025-10-07 06:18:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 022e806e-864a-37bd-a49c-80d84d6cb2ed | -8.93079 | -62.21555 | 2025-10-07 06:18:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a34c9a81-8e6b-3e6e-8c3e-b522147ec3df | -9.55578 | -63.50644 | 2025-10-07 06:18:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a6b3629-b952-353b-8055-dc740bb1b4d3 | -9.39972 | -61.44403 | 2025-10-07 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db8c7394-1ce2-3418-b076-64bbb8b64447 | -7.46097 | -63.61917 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8e1134d-16ce-39df-a92d-e6ed4633d603 | -8.84156 | -71.24592 | 2025-10-07 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0d1a29c-7b11-3bfc-bdce-65ce7b2b7f54 | -7.49432 | -63.67011 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15352e71-9624-3d72-8368-2fd7f07de89e | -9.14806 | -60.62402 | 2025-10-07 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40e82266-36d3-3d50-a862-16aa10f2d0f5 | -6.95486 | -71.49739 | 2025-10-07 06:18:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cef93fbe-de8e-3be1-87cb-e299f6dba28d | -10.89686 | -69.56194 | 2025-10-07 06:18:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c099ae7e-50cb-3e3f-9f8d-d4c37f832f7e | -7.82512 | -73.1021 | 2025-10-07 06:18:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 24f23f8d-bf41-362e-85f1-432d507561ca | -8.93142 | -62.21054 | 2025-10-07 06:18:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adc17d6c-564a-3740-befd-96664b2434f1 | -8.9245 | -62.2147 | 2025-10-07 06:18:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e98842a-e8b9-3939-9741-f520fb2ac33b | -8.22403 | -72.82543 | 2025-10-07 06:18:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1648590-6484-395e-a26e-94f8a58286ab | -9.74751 | -62.27303 | 2025-10-07 06:18:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04221ef7-6710-37f0-9726-7add2e4b6ce6 | -7.464 | -63.62138 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c735de5-e027-3db3-815f-c6498e970e63 | -7.46454 | -63.61753 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4178ec1-54f8-3d54-8752-fe4a476d2be6 | -9.40299 | -61.44455 | 2025-10-07 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a041485-6707-3b05-8abc-6aa5da040c47 | -7.46661 | -63.61993 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c636e799-e4c7-37f5-ba3c-8151dbbd75e7 | -8.85758 | -62.3654 | 2025-10-07 06:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b641fbc-9919-3894-933f-c791be5af079 | -7.43485 | -63.74735 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14272d0b-9dcc-38f2-acaf-b6ac250ef39d | -6.95362 | -71.49706 | 2025-10-07 06:18:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2944228c-606f-33f0-8bf9-f81816d79f10 | -7.83284 | -73.0746 | 2025-10-07 06:18:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21c9f293-7ddc-3fb6-a6ef-e1253cd4f6b1 | -8.85695 | -62.37023 | 2025-10-07 06:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26737184-8016-3806-9c32-3f30f097af12 | -9.39633 | -61.44387 | 2025-10-07 06:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79648e35-d25e-3581-b129-286273355930 | -7.4799 | -63.56356 | 2025-10-07 06:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6c1cceb-ad6f-3cf8-b225-19bbb671c6e7 | -7.75751 | -70.73178 | 2025-10-07 06:37:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59556c77-09c0-38e8-bded-eb5396e4aef7 | -7.75706 | -70.73499 | 2025-10-07 06:37:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a381bb22-4f2a-3c3f-90cc-8173f7c6e684 | -6.95533 | -71.49963 | 2025-10-07 06:37:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e83460b6-b01c-3204-8974-279c8cbb6a55 | -20.0701 | -49.5184 | 2025-10-07 06:50:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 10dc1f25-ae17-32b6-86a9-262893975b78 | -18.157 | -53.37 | 2025-10-07 06:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 809aa430-11f9-37a7-a4c4-f00c10ebf35b | -20.0491 | -49.5455 | 2025-10-07 06:50:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.1 |
| ab6de7f3-6306-371a-9241-1844fbc319ff | -20.0695 | -49.5412 | 2025-10-07 06:50:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.3 |
| aefbbe2d-1ef1-3299-8da4-7883271ac16f | -18.1176 | -53.3548 | 2025-10-07 06:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 72.7 |
| f292cb19-4cca-3b31-9e67-40b58cef09df | -18.1181 | -53.3333 | 2025-10-07 06:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f8293f03-085c-305b-a00a-5195a29d95f4 | -20.0497 | -49.5227 | 2025-10-07 06:50:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 0d3003fb-9ace-39d1-b718-0fdde2ac998e | -20.0695 | -49.5412 | 2025-10-07 07:00:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| 56e9aeb3-9679-34bf-a051-5e1bb0a6cd37 | -18.157 | -53.37 | 2025-10-07 07:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 9e2d8461-0cfc-3ffd-a15e-3d6f41270ddc | -20.0491 | -49.5455 | 2025-10-07 07:00:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 21d31752-d47f-33bc-bb5f-27ea0d936b4e | -18.1176 | -53.3548 | 2025-10-07 07:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2d779205-9bd0-3fb6-b679-2b2dd295aaaf | -18.1176 | -53.3548 | 2025-10-07 07:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0a8ab7f9-e3b3-3cf7-b1e2-dc611607d0f7 | -20.0491 | -49.5455 | 2025-10-07 07:10:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| b9aa8612-745e-396e-a7c5-fbf5dd67fd98 | -15.6198 | -52.5715 | 2025-10-07 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 72ad4c2b-7702-3e2f-ae33-6e0b4abfc008 | -15.6003 | -52.5742 | 2025-10-07 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 7f734ce6-a299-3682-825b-1e0457dbfbea | -20.0695 | -49.5412 | 2025-10-07 07:10:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.6 |
| 51cfd8ff-aaac-3072-8d25-51e3ecfcba69 | -15.6397 | -52.5474 | 2025-10-07 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 609eb8a9-2c09-3f86-b910-4cf047a53269 | -18.1769 | -53.3669 | 2025-10-07 07:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 248ef339-842e-3b2b-9f2d-66191300baeb | -15.6202 | -52.5501 | 2025-10-07 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 5f930999-f8a1-33b2-8f1d-5b94e3db85c5 | -15.6007 | -52.5529 | 2025-10-07 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b61ff963-ad16-32e6-b02e-88ee2fef16a6 | -18.157 | -53.37 | 2025-10-07 07:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 036df0ca-7cd0-305b-ad98-8b6c8ac5ea65 | -16.275 | -50.9681 | 2025-10-07 07:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 5766d576-ab67-33c5-899a-d919eee3fe1f | -16.2946 | -50.965 | 2025-10-07 07:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 40ff5e3c-2429-3f23-8805-be9cb09bd1ee | -15.6202 | -52.5501 | 2025-10-07 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 99517177-1759-35b6-8f48-31b302cca520 | -20.0491 | -49.5455 | 2025-10-07 07:20:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 399b520b-1417-39dd-bb83-b38ef3c1473e | -16.2942 | -50.9868 | 2025-10-07 07:20:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 16b04079-3e57-3b30-8b9c-86b481484a0f | -18.157 | -53.37 | 2025-10-07 07:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d3a2d327-ca57-38ea-9f9e-624ac89a0946 | -18.1176 | -53.3548 | 2025-10-07 07:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6d05abcc-a059-32eb-8e62-90f73f6e80d9 | -20.0695 | -49.5412 | 2025-10-07 07:20:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| a6122947-e93f-38ad-af88-71d8ff622d75 | -18.1181 | -53.3333 | 2025-10-07 07:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 137c9083-4759-3b30-b2bc-82aae3bbe211 | -16.2946 | -50.965 | 2025-10-07 07:30:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e1f532f9-285f-3850-a714-85bc5c011457 | -20.0491 | -49.5455 | 2025-10-07 07:30:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 89fe41ba-da97-3aaa-9340-72b258031c48 | -18.157 | -53.37 | 2025-10-07 07:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 6dff8f92-eb8f-3a53-ab21-6068c5645b40 | -16.275 | -50.9681 | 2025-10-07 07:30:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 84a0b1f2-e75c-3ccf-9c2c-029d1536aded | -15.6202 | -52.5501 | 2025-10-07 07:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 010868c5-88cb-3c03-9d38-3f93e2a4cacd | -16.2942 | -50.9868 | 2025-10-07 07:30:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c3d10011-869d-3595-aa18-a1ff6b230919 | -18.1176 | -53.3548 | 2025-10-07 07:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e86d386c-31a7-332a-becb-7740cff9965d | -15.6198 | -52.5715 | 2025-10-07 07:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 18fa4794-d7fc-32d3-a7a6-82ab11c813fd | -15.6007 | -52.5529 | 2025-10-07 07:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c7c33348-bcbf-3f0c-b68a-b754b0779604 | -16.275 | -50.9681 | 2025-10-07 07:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7acd6853-14c8-366c-a1e9-26118fc67cec | -15.6007 | -52.5529 | 2025-10-07 07:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 516f2f5f-705a-36b9-b943-b2d8e76d6f74 | -15.6202 | -52.5501 | 2025-10-07 07:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 29c34587-6e8c-39e3-8172-10d109aa8758 | -15.6003 | -52.5742 | 2025-10-07 07:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| daa740ee-b42d-3391-932b-39c8420ece7d | -18.1176 | -53.3548 | 2025-10-07 07:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 8bc41c77-0363-36a9-8019-104ce19713a8 | -16.2946 | -50.965 | 2025-10-07 07:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 188bc094-b333-377c-8549-c8b9b825c1c3 | -15.6202 | -52.5501 | 2025-10-07 07:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 32ac8542-9bdd-3559-b551-f7f6586967ee | -13.2232 | -51.6744 | 2025-10-07 07:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6b050eb0-ed3a-37e2-9345-b25f56f0ecef | -18.1176 | -53.3548 | 2025-10-07 07:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 449a1177-7d7e-33cd-8b16-d42b8542aee1 | -15.6198 | -52.5715 | 2025-10-07 08:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 702296a7-042a-394f-a016-850217b6dd62 | -15.6397 | -52.5474 | 2025-10-07 08:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5e624d90-4990-3ffc-b7b7-a4adc44012b4 | -15.6007 | -52.5529 | 2025-10-07 08:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b66429c5-113f-3ae7-aa67-21bfdd1a9e60 | -15.6003 | -52.5742 | 2025-10-07 08:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| cdf27db2-644d-3829-a1b5-487f241a80e4 | -18.157 | -53.37 | 2025-10-07 08:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b07f9e92-5ac9-340a-b32e-fa1a14dab913 | -18.1176 | -53.3548 | 2025-10-07 08:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c2542f9f-bd74-3e4d-80f8-35f025e95c30 | -15.6202 | -52.5501 | 2025-10-07 08:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 137.1 |


[Clique aqui para ver as próximas entradas](README110.md)
