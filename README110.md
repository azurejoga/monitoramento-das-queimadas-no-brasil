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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c03d592-d5c5-34c3-b243-a1aa80c2eb74 | -21.36341 | -55.69836 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65052787-2f28-3d98-875f-8f7ee36e9c70 | -21.36215 | -55.69266 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d46905b8-09d3-3b93-9185-58d4533fbc7d | -21.35518 | -55.69638 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bed35c3-8ee2-3a25-812f-38949acb0b9d | -21.349 | -55.66119 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 787c107c-abaf-3b6e-8115-ad821c96e9d2 | -21.34822 | -55.66527 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edfd7bce-70fd-35a3-97fc-a33b3ca71c4a | -21.34442 | -55.68519 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ade19b15-9cc3-3c6f-aaa1-efc96fd08a43 | -21.3441 | -55.66437 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7730ddd-a505-3d2f-971e-dff0b4a8ea63 | -21.34364 | -55.68923 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f65f8bd-3943-3a74-88f8-a74a9efb5f0d | -21.34333 | -55.6684 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b958eead-f666-3998-b0f6-44eb8ae8d47c | -21.34257 | -55.67239 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44c1cfc9-4d95-3e8b-a8bb-3937b1ba0589 | -21.34181 | -55.67632 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d2c8c88-6624-3ae4-959d-dff1442c3b04 | -21.34105 | -55.68028 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 779e31cf-b8cb-3554-a7f0-e0766ac2c69c | -21.34028 | -55.68433 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c99b748-293f-333a-8674-7f60df169281 | -21.33949 | -55.68845 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6a991ae-d84a-3b23-99ae-12044daeeb08 | -21.33922 | -55.66742 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 630657b5-e1f9-3d70-838d-8b7cc4f38524 | -21.33869 | -55.69263 | 2024-10-03 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e6b5449-1122-3795-b555-1c3f8d30143e | -21.33846 | -55.67137 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f2e3507c-172d-3bd3-8cc3-ace806bf4f91 | -21.33771 | -55.67532 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f4c3425c-204a-361b-89fa-b4945d1b2442 | -21.33695 | -55.67929 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a6546ee-d002-3170-ba3b-853f4b8858ee | -21.33436 | -55.67039 | 2024-10-03 04:32:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52f00baa-cbf6-3506-9557-1990babb132a | -20.03736 | -55.95166 | 2024-10-03 04:32:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0be27675-364d-3895-829a-f09b3a91c7e0 | -9.0149 | -67.7423 | 2024-10-03 04:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d92a5d79-29aa-3d6f-88e9-ce4ae66282fa | -9.0515 | -67.871 | 2024-10-03 04:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3df3620f-ec03-33c9-8a37-3fa26e04b627 | -10.8942 | -63.8971 | 2024-10-03 04:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 832ff147-60ba-33c8-8529-f8b5bfd16a79 | -11.6931 | -64.9974 | 2024-10-03 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ca91b8aa-c0c4-3174-b951-c9343833d9c6 | -11.6932 | -64.9785 | 2024-10-03 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| d09cfc28-f57e-39c8-bb08-615627877e82 | -12.4038 | -63.0009 | 2024-10-03 04:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 177.5 |
| 29a4a16c-d654-35b2-aa85-f18c5e4c1d1f | -12.404 | -62.9817 | 2024-10-03 04:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 8571353d-8e0e-3f58-bbbb-7ebee71df84e | -12.4227 | -62.9999 | 2024-10-03 04:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 53ff0bc9-6dec-348a-9d06-8a1aaddbe15b | -12.4228 | -62.9807 | 2024-10-03 04:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| fbb29eb1-7974-3776-8e4a-156d09febbdc | -12.881 | -62.4538 | 2024-10-03 04:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b60de8e4-2ac0-3eec-9c8a-50858b1c5a6d | -13.0406 | -51.1218 | 2024-10-03 04:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2064e763-bf73-3279-b83e-fb94896a9ea1 | -13.0402 | -51.1432 | 2024-10-03 04:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 74e14f9c-670c-3ad8-8c86-c1223ccf6239 | -12.8999 | -62.4527 | 2024-10-03 04:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ec1f9036-0a0c-306c-b3c2-c8cfb8721ebc | -12.8998 | -62.472 | 2024-10-03 04:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 110.6 |
| cb9b3eee-9721-35cd-ad47-2999b8aa775c | -12.8996 | -62.4913 | 2024-10-03 04:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 3463857d-b8bc-3aac-9216-410521cf0659 | -13.0594 | -51.1409 | 2024-10-03 04:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 27e6ce00-e311-3e62-afff-f9d9ab464afc | -12.9741 | -62.6409 | 2024-10-03 04:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 0833ac73-801f-32d9-9a2e-9a520c35f9f6 | -13.5198 | -51.1252 | 2024-10-03 04:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| f79dce99-a2bf-31c0-9516-61c72bbde6bd | -13.5387 | -51.1442 | 2024-10-03 04:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 817868d8-4134-3456-a033-16a89652ff4f | -13.5391 | -51.1228 | 2024-10-03 04:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 15c1acdc-55e7-3ff6-9561-c2595bc67e09 | -13.5195 | -51.1467 | 2024-10-03 04:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 145a2d90-2de7-38c3-a578-257ffef60bf5 | -16.6688 | -57.374 | 2024-10-03 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| cfb88558-f521-37c5-8e40-f054f87fea68 | -9.0515 | -67.871 | 2024-10-03 04:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0c48bd2c-6fa6-3ecc-801d-4d07ca2ce061 | 2.11955 | -50.66982 | 2024-10-03 04:46:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ca8953a-4c84-3f4d-88a2-d00ff77b8e89 | 0.82454 | -51.86536 | 2024-10-03 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fbbaec1-f5f7-348f-96b0-aa8b28a26a4c | 0.82119 | -51.86589 | 2024-10-03 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6b71862-e214-3013-9ef8-fe20dc2ef6a9 | 0.81785 | -51.86644 | 2024-10-03 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dc4acd1-0127-3a20-b38e-19facdf8e648 | 0.81176 | -51.84943 | 2024-10-03 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b3de5b99-a292-38a7-815d-dcd05843cf71 | -10.8942 | -63.8971 | 2024-10-03 04:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d316859a-43f9-325f-b52a-d7afeb43da6d | -11.6744 | -64.9793 | 2024-10-03 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d6eb1ca8-fb91-3f2f-8e60-cf8a5bfbfe42 | -11.6743 | -64.9983 | 2024-10-03 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 595bca7a-6378-328b-ac2e-c3f1b41c2b06 | -12.404 | -62.9817 | 2024-10-03 04:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 2469997d-0702-3f36-999c-bdb178bbdd97 | -12.4038 | -63.0009 | 2024-10-03 04:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 198.8 |
| b2cede14-4845-3c0a-a0fe-308d984016b6 | -12.4228 | -62.9807 | 2024-10-03 04:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| dbb9a6c8-d3de-3196-8323-6f341add25cc | -12.4227 | -62.9999 | 2024-10-03 04:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 8127d594-231d-3c42-b49a-3afdbb0ee7a3 | -12.6484 | -63.1214 | 2024-10-03 04:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8e1c883e-4eeb-3e01-94b5-03244a44ff2f | -12.8999 | -62.4527 | 2024-10-03 04:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2867adab-6e3b-38c0-8231-bddf1ef1dd48 | -12.881 | -62.4538 | 2024-10-03 04:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d646732d-5f90-3434-b159-a5270f1a1726 | -12.8996 | -62.4913 | 2024-10-03 04:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1e235bd8-2e2f-3264-a6d9-f731744a13f7 | -12.8998 | -62.472 | 2024-10-03 04:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b9e99c4d-8264-3d54-b71f-cd5551db9a04 | -12.9741 | -62.6409 | 2024-10-03 04:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 6b059a58-31a6-3248-8ba0-f4f9a70c4133 | -8.433 | -41.93853 | 2024-10-03 04:49:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6ff532e2-6c18-33d0-a40a-10ef1796f983 | -8.43284 | -41.93738 | 2024-10-03 04:49:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5117998e-7481-37bb-9f7c-c66f5ef0f9fb | -8.43225 | -41.94179 | 2024-10-03 04:49:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5b584121-a1a6-35f9-8f16-12001799e1a7 | -3.10445 | -42.62839 | 2024-10-03 04:49:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c981635-c30d-3a00-84eb-a158a5901536 | -3.10393 | -42.63177 | 2024-10-03 04:49:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 556b483e-4907-3463-b344-5bafef3c57c8 | -3.41702 | -42.27034 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0cc26a2-1cee-3581-ba70-7d89acbe3764 | -3.41648 | -42.27403 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c9b6a24-79df-36c5-a2be-5148cbc15e8c | -3.41592 | -42.27783 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b03f87c8-f8a1-3f6d-bc44-e075326106f9 | -3.41539 | -42.28148 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e103d32c-419e-34a0-86a2-a4aa495ec25f | -3.41486 | -42.28507 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cb77ed4-2f12-3af5-97e4-c8abe14e94b4 | -3.41433 | -42.2887 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4cd0d55-c8c5-3fd9-ae40-1ac465830726 | -3.41305 | -42.25877 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fa53c36-431d-3cd3-af9d-10973ee59caf | -3.41252 | -42.2624 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06c16f3f-f6e3-3ec1-9663-280389643751 | -3.41199 | -42.26599 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff81b5ad-5d7b-35a0-83dc-093a00eac1fd | -3.41147 | -42.26953 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 222d9684-358f-3015-b81f-beb51ebfeaaf | -3.41093 | -42.27325 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f192ebde-0094-32fa-bafe-ca0ea94c59ad | -3.41038 | -42.27702 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d71da2c7-ec69-36ad-9651-2b79cd6f9b8d | -3.40984 | -42.28072 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 143e1d9b-ade0-3a49-aa0a-77d6f1210300 | -3.40931 | -42.28435 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| bce718d9-e877-3c22-870b-6d74b42f0b28 | -3.40878 | -42.28798 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| c08f9de4-6752-3bf3-8030-1e25c71e4866 | -3.40825 | -42.29161 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 554b76fb-a6af-32d5-8c01-444aac72b403 | -3.40803 | -42.25434 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3277f43a-34b1-3d03-933d-4da0688916dd | -3.4075 | -42.25796 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 010dc976-b801-393a-b65e-45670bb22416 | -3.40697 | -42.26156 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4873d9c1-8de3-3a2d-a838-066f36698711 | -3.40645 | -42.26517 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b817ce4b-7a41-36e2-ab97-87b949bfbd65 | -3.40592 | -42.2688 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 72285f40-77f3-3c09-84ce-0ee3ae5ff8eb | -3.40483 | -42.27628 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 08fb0d16-4b98-3d6f-b4ba-b94c875911e5 | -3.40429 | -42.28001 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c79ad64d-98ee-35c8-952d-3cbf1d7fb5c6 | -3.40376 | -42.28361 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| f6a4ab8e-52b0-32ab-a844-6c296c934782 | -3.40324 | -42.28722 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| a8ca3759-e742-3443-abd5-b9ae3299434d | -3.40271 | -42.29083 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74578261-f787-3799-8784-2e74db92c379 | -3.40218 | -42.29445 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e2c7e0-2b65-3033-941c-1fd40248dbfc | -3.40195 | -42.25716 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f8c0957-0c28-3e8b-98ab-862178b0060a | -3.40143 | -42.26075 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffb581e5-516a-33b2-b5cc-22579f9ab3a5 | -3.4009 | -42.26438 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc3546c0-8c7d-3e16-a2d1-85e462507162 | -3.40037 | -42.26806 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 31dfdafa-618a-3a9f-9ad0-a6fa1e761ba7 | -3.39983 | -42.27175 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fe87ca68-2beb-37ec-aff2-49e9df2a2428 | -3.39928 | -42.27557 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README111.md)
