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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 831fd12b-cb02-3160-9068-adf42ecccf34 | -12.1516 | -47.0608 | 2026-09-05 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 15398b20-4747-3d5e-ab36-f069cf47a080 | -3.5406 | -48.1889 | 2026-09-05 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 345.0 |
| fc6444b3-10ff-3d9b-ac20-767efb9ed3a4 | -11.8248 | -46.0448 | 2026-09-05 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e53ef340-96c0-31fb-aad7-cf8539605b05 | -3.7645 | -61.7548 | 2026-09-05 14:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 7959b05d-48db-3e80-baf3-42eb804f0dce | -10.3004 | -50.0445 | 2026-09-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1a572cc1-cb93-33b7-ba69-ff6f22aa0189 | -10.1462 | -50.2952 | 2026-09-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ca1e9b35-ede4-3104-9dff-e3a40a264438 | -12.4328 | -43.275 | 2026-09-05 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| f7a4d4c6-f0f3-3c8b-8ece-114d8d46cd78 | -10.3385 | -50.0191 | 2026-09-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e23587ae-1707-346d-b80e-f7d0250af6da | -3.7827 | -61.7733 | 2026-09-05 14:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 9e78292b-4289-3caa-9627-3dc61601d697 | -4.6669 | -55.635 | 2026-09-05 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| f1f5a2ea-be17-3b3d-9d8c-5bc699ac8c74 | -11.5479 | -45.4676 | 2026-09-05 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 3530b1f4-169c-32ae-8136-e68779fa92ca | -3.5592 | -48.1666 | 2026-09-05 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 8736525d-3171-360b-98e3-07eb79fa3b32 | -3.7645 | -61.7737 | 2026-09-05 14:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 23fa05a0-2cd0-36f6-a551-3cfcc9a91057 | -3.7828 | -61.7545 | 2026-09-05 14:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| cbc49ee2-6634-36bc-901b-4f2d17a928df | -10.3196 | -50.0211 | 2026-09-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5485e6c1-2ebc-382b-800f-257068f17957 | -10.3007 | -50.023 | 2026-09-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2e212e46-53e6-3d50-b62a-e56b42dbde6a | -12.4522 | -43.2717 | 2026-09-05 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3996a92c-7946-3c10-b957-94790fd0f4dc | -3.5407 | -48.1673 | 2026-09-05 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| a3210adc-241c-3973-beee-439af311c6b0 | -10.3004 | -50.0445 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 59775059-c030-318e-a831-b283a04afd9b | -10.3574 | -50.0171 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3219f665-847c-39df-9aaa-7e05551aa357 | -10.1462 | -50.2952 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 6763723a-7692-3817-a992-8a62840c596e | -10.1653 | -50.2719 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| dae36561-708d-32a5-810a-255749abb0f3 | -3.5592 | -48.1666 | 2026-09-05 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 13211f69-50a5-30bc-a457-d402d915e929 | -4.6669 | -55.635 | 2026-09-05 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| fea29fd1-3265-309f-a8b0-8a917d88673c | -3.7828 | -61.7545 | 2026-09-05 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 650a535a-bdf9-3e77-b5a6-83bdbad4b01a | -3.5407 | -48.1673 | 2026-09-05 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 175.0 |
| abc03da8-cc48-388a-8cfe-9e0ec837fc49 | -10.3007 | -50.023 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2b3cebca-0660-37b4-bcb8-2666a4292c68 | -3.7645 | -61.7737 | 2026-09-05 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 577d7df0-d090-3f89-8adc-1a29026b4ab0 | -12.1516 | -47.0608 | 2026-09-05 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| fc20eb18-ed07-349f-b56a-18cbc29af274 | -10.4145 | -49.9898 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 7bd31bab-6854-3a0c-a7f7-507fc34e9c28 | -10.3385 | -50.0191 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e6347dcc-c9f7-3438-805c-fd1766347ac7 | -3.7645 | -61.7548 | 2026-09-05 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 123.0 |
| ae6a0a35-6df9-3e2c-aa37-67ca2f208687 | -10.3196 | -50.0211 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 01a7eb1e-ae90-3705-a256-f7fedbdd9f95 | -3.5406 | -48.1889 | 2026-09-05 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 343.6 |
| 643296f6-c3ba-37da-a91a-1271014d4f76 | -10.165 | -50.2933 | 2026-09-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2b6102a7-9e6f-3835-b03d-1526d3521dcb | -3.7827 | -61.7733 | 2026-09-05 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 3243fab0-bb4f-3960-839c-0a2d435c0868 | -4.667 | -55.6152 | 2026-09-05 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| bc0e4fe2-568a-3b7d-b68a-c083ecd66855 | -5.32 | -56.04 | 2026-09-05 14:15:00 | MSG-03 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 958ebdc0-9cdf-32cf-a397-21d715d57a2c | -5.35 | -56.04 | 2026-09-05 14:15:00 | MSG-03 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb41d9e-946c-3b76-a579-c1ec36f50048 | -5.35 | -55.98 | 2026-09-05 14:15:00 | MSG-03 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebe791c4-4cc8-324e-87e7-4d50c02e09ad | -3.56 | -48.2 | 2026-09-05 14:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16ea8441-fe98-39b4-8696-d8d0ad1aa012 | -4.6669 | -55.635 | 2026-09-05 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 4c4cfdaa-bb00-341b-a3f5-8307e452545b | -3.5406 | -48.1889 | 2026-09-05 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 342.8 |
| 570a8225-9a67-39bc-ba50-8cdb977f6c7e | -3.7645 | -61.7548 | 2026-09-05 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 5250fa2c-7f61-3a05-8169-55488d4f3b7a | -4.6853 | -55.6343 | 2026-09-05 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 3e3c2329-981f-34d3-9204-4f5007b63e74 | -5.3277 | -56.0263 | 2026-09-05 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| ed54bad3-d12e-3488-81a7-ac4a26159c3a | -3.5407 | -48.1673 | 2026-09-05 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 44059d96-ac4d-3fd0-8960-42fdfe38236a | -12.4328 | -43.275 | 2026-09-05 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 32e18a50-515d-3759-994f-04a18f0e38c8 | -10.1842 | -50.27 | 2026-09-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| e05c5dcb-abf5-3826-b676-c6e97cadd844 | -3.5592 | -48.1666 | 2026-09-05 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 1675aca3-44b5-3039-9116-65381b3c6154 | -3.7828 | -61.7545 | 2026-09-05 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ee3c796e-ef94-34a9-b93c-587d6feb6ac9 | -3.7645 | -61.7737 | 2026-09-05 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 806f7c3f-471f-3373-85c5-75ce35d963b3 | -4.667 | -55.6152 | 2026-09-05 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 11ff806d-81ef-3dfc-a4d3-d25da6a9c7a4 | -5.3093 | -56.0271 | 2026-09-05 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 436761c4-4472-385e-b2a7-dd40d2a48de7 | -10.1462 | -50.2952 | 2026-09-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 585e7b90-f1e3-38eb-89c1-2bf0a7c871dc | -10.4145 | -49.9898 | 2026-09-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2f6b4f62-a751-3315-bc4b-39ab16e3df45 | -5.3094 | -56.0073 | 2026-09-05 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| bbf92978-9019-3f61-ac72-eb11a45dda0f | -3.7827 | -61.7733 | 2026-09-05 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 26cda591-7d32-394d-9530-e9c9364a7108 | -10.3956 | -49.9918 | 2026-09-05 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 19d3c55d-954e-3a8b-aec2-be0009a69bb9 | -10.4145 | -49.9898 | 2026-09-05 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3e90000b-29de-3231-9cb3-2a8cdb42a5fa | -3.3688 | -59.4079 | 2026-09-05 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6b57e057-c859-3832-a1f3-e68ad2bfd5a1 | -3.5407 | -48.1673 | 2026-09-05 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 649eab15-56c2-3308-9153-1ad4e21fcd41 | -4.667 | -55.6152 | 2026-09-05 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 24d6745e-2aaf-38d0-97ce-e539367eeb1f | -17.6202 | -44.2011 | 2026-09-05 14:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 119.9 |
| c727b1da-e61b-3a16-a4d3-bccfc7e4bca0 | -4.6669 | -55.635 | 2026-09-05 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 200.7 |
| f0de420b-0ea5-3bfc-be69-ec3bb83d5dcd | -12.0936 | -47.0913 | 2026-09-05 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 62a28c39-51ff-3dee-a5ec-145f03d4741f | -12.094 | -47.0688 | 2026-09-05 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2665fe6b-6439-3ea0-b88a-63373961ab41 | -3.5592 | -48.1666 | 2026-09-05 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 6684d5da-7401-3c27-9047-2767ed0bc960 | -3.7827 | -61.7733 | 2026-09-05 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 9649f314-273e-32a2-98a6-34652865964e | -3.7645 | -61.7737 | 2026-09-05 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 193.7 |
| bd9d7c15-fc11-38ed-98db-8025bb62ec97 | -3.7828 | -61.7545 | 2026-09-05 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| ef42de23-3bdc-387c-a372-bb04f4212baa | -3.7645 | -61.7548 | 2026-09-05 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 148.5 |
| bd0bcf6e-c288-372f-bdf3-69261dcd81e2 | -1.4944 | -54.2563 | 2026-09-05 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 473088f0-4664-328c-93bd-0e72fb148a4f | -3.5407 | -48.1673 | 2026-09-05 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 4b6fee9c-4623-3377-9b3c-03b1da12de06 | -1.476 | -54.2765 | 2026-09-05 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 699bcb84-4967-3172-bfaf-a669c232f313 | -17.6202 | -44.2011 | 2026-09-05 14:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| cb734293-adc2-3cfc-8de1-6bb7ad7006b2 | -5.291 | -56.008 | 2026-09-05 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8013578b-c3c6-374d-a914-c0014befd28f | -3.7827 | -61.7733 | 2026-09-05 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 2d9be1c6-5519-3a1e-a4f3-b12483e01c69 | -5.3462 | -56.0256 | 2026-09-05 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1338.9 |
| 15f3aea9-59e8-3d39-bcbe-1ed90eec5980 | -3.7645 | -61.7548 | 2026-09-05 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 09b4b8a5-2470-3227-962f-daa818529aed | -11.2764 | -45.7113 | 2026-09-05 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 96f86d65-54d1-3948-99f0-56e9d3f9aac4 | -8.7817 | -46.4623 | 2026-09-05 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 50afb57f-f8a3-3574-8110-52f630d2cc84 | -3.3688 | -59.4079 | 2026-09-05 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| a6e867b6-d04f-371b-a89b-5625f311ce49 | -4.667 | -55.6152 | 2026-09-05 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9e2f5c4a-bf0e-318c-83a3-076c0105bbe5 | -5.3276 | -56.0461 | 2026-09-05 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| c1b42dba-5b7d-3f05-88a5-3d6ca424ab4f | -7.2158 | -43.6069 | 2026-09-05 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 551a66d0-efb3-37dd-b38d-3ecc850fc882 | -3.7828 | -61.7545 | 2026-09-05 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 38aa7a7b-ae03-3aa9-9ce9-08079d286e26 | -5.3094 | -56.0073 | 2026-09-05 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ea9d5c10-fdcb-3617-91f6-f65f09befe24 | -3.7645 | -61.7737 | 2026-09-05 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 2db3af07-a334-31ce-9801-1cf3bb63aacb | -1.4761 | -54.2565 | 2026-09-05 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 1e2efa8a-1f9d-37b7-8f57-deab41799c6c | -3.3688 | -59.4079 | 2026-09-05 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9dbe28aa-46b9-3793-a4fc-3b5b4a465fc5 | -3.5407 | -48.1673 | 2026-09-05 14:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 542c8a63-00f5-3331-aabb-a0ed0ede06a2 | -1.4761 | -54.2565 | 2026-09-05 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| be71f52d-f221-3e33-a9f1-a02a6437890f | -10.2818 | -50.025 | 2026-09-05 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 6646544e-4daf-33c3-9637-80d0774b02b6 | -3.7828 | -61.7545 | 2026-09-05 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| fbecfd7c-475e-385b-a5c5-8034b358953f | -8.7817 | -46.4623 | 2026-09-05 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0991c8ad-7379-3235-b207-ee4d4f5be8e4 | -3.7645 | -61.7548 | 2026-09-05 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 9aee2bc8-a18f-3a7b-b021-9d4c7f1ba10b | -3.1816 | -61.1235 | 2026-09-05 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| b271767e-542e-3594-85af-831c45cbf508 | -3.5592 | -48.1666 | 2026-09-05 14:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 57f85b3e-43c3-3925-ad16-a10c25f7f3e1 | -6.0244 | -60.1781 | 2026-09-05 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |


[Clique aqui para ver as próximas entradas](README40.md)
