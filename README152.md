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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e30dcdd-d066-37fd-bf65-64c382eafefd | -6.57882 | -55.43969 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0ec2ebf9-26c1-370b-97d1-1c2d2b5272e1 | -9.04137 | -70.58278 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9c4674ac-3e4a-3b4a-8586-e23a8bc85c6e | -8.88173 | -71.46706 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cdd4f8ed-7576-32b4-8108-7d20023be2bc | -8.1538 | -63.99854 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1e18d3fa-b97a-3da9-a9fc-5ad2e8eb269f | -7.59612 | -61.33912 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 99829537-82b7-3f17-9bc3-cd7cc4ba8dc8 | -6.0152 | -57.6652 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9a86dcf3-d20c-3e3d-945e-edc28c6891cd | -4.05654 | -60.64097 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2546c5e5-ec92-3723-8d21-77270b67a1fe | -3.40497 | -61.32126 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 35afcad3-97d0-30c5-abee-ec86c0f8f022 | -4.90171 | -56.26427 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ecc17bbe-9ad8-303d-b7a9-49077c77f43a | -8.89715 | -71.42425 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 201e7f2b-20bd-3590-a2b9-3ec6fb5feb08 | -9.04209 | -70.58815 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 3a5ef348-0ef2-3c99-9b66-0a812aeb833f | -7.58466 | -61.3106 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eaeed273-7d2e-33a5-a681-cc6b4cca891d | -8.19685 | -71.47697 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c1af77e9-8c0e-3c42-9778-87a739674e23 | -7.92382 | -56.63355 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9e3155dc-5afc-3594-a641-72de4b299626 | -3.23251 | -61.23648 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7ee57303-9c89-33c8-849c-12a0ad6c2044 | -5.94795 | -57.72928 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 39100238-b2de-3741-abbc-f74760877c51 | -8.86211 | -71.26159 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9aa98c55-3ac4-3ee9-b03e-cf92750c3c2b | -8.27254 | -70.7788 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 168c9ec8-70e6-3c3f-ab53-bc81d53d7a68 | -5.91472 | -61.30164 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7f1ca279-8b97-3c67-a7f8-c41818653714 | -4.33649 | -54.89855 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c1ac037d-3985-3b27-9bb1-fc4a04e3626c | -6.16048 | -57.78328 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 96663301-3412-31fb-8e26-48bc5991a766 | -8.1371 | -64.00107 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19c108a9-c742-331f-b2ba-e2b85eae6baf | -6.9169 | -59.48498 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3cb08274-2fad-3c62-8ec1-e8f1d0bb40a7 | -6.62811 | -59.08086 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2e0b0c80-df00-3474-9894-132009704cb0 | -9.42487 | -70.57819 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9e2dce8c-64b3-3c57-80ed-dfc771b7dfec | -8.60255 | -70.21144 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 37061d4a-b928-3906-a530-42c8bb448921 | -8.79443 | -70.82666 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 109.9 |
| c3f7c853-94ad-3daa-a5a6-307acbbf1973 | -7.8242 | -73.4058 | 2026-08-28 17:47:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 25.2 |
| b0ed2407-0fc0-3218-82ec-dc9523c1246b | -7.98014 | -71.49651 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 10ed16cb-1f3d-3281-9fe2-b74201d05ae6 | -5.93237 | -55.67245 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a96bd42d-288f-3af7-97f3-7cd9a17f1a61 | -8.89889 | -71.53185 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a8d9821c-7f49-3fb1-b4ba-e61f43b6a53c | -7.74139 | -61.05998 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0fe1b6f-8031-39d0-b53e-1599f610879d | -7.98299 | -71.44098 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 884598ae-08cf-3366-af77-c528e7f411eb | -4.92687 | -55.77179 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 75f4462b-d2d5-36a0-98ba-b2c6a280111a | -6.86423 | -60.07565 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e86cc3d1-f514-3838-a3da-fce8680a3c36 | -8.19645 | -71.47398 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 082a8b0a-d5cb-3883-bdeb-04ddbc0fea4b | -6.75272 | -58.72898 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e1b9c123-df73-3d6b-a403-8e0860a176b9 | -8.8814 | -70.80305 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9181d544-bc48-3c5f-95f3-b650ac293957 | -3.51609 | -61.59465 | 2026-08-28 17:47:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f7a1732-a6f2-3141-a639-184d8cb5cb03 | -8.86529 | -69.05616 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0cb5c937-6e35-398e-9b0b-16556da79026 | -5.45969 | -60.23613 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51327f0e-5943-36d5-acf1-2e7f3a87db58 | -8.87632 | -66.90749 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 842c578f-3568-3f5a-bf97-fd189d227e5e | -9.05037 | -69.61211 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 795f3d98-2b6e-3e37-a081-b17a295bc80d | -6.23384 | -55.46722 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 488aa6b8-6ade-394b-a7e1-4865cac21317 | -8.08849 | -70.63941 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f05ce40b-547a-3b08-be89-2abbc46e00dc | -6.82086 | -59.70843 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da7d6b16-0ef1-34ff-88d6-3a28bf1d778d | -8.68302 | -70.75377 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 911a3bcf-159c-36ac-9b2f-a6e469c78a77 | -8.4373 | -70.33071 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 981dd295-26e2-320c-b2c2-ddbbc701b6ef | -9.48341 | -71.29744 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8609026e-2aec-31a0-8117-095950a4f250 | -6.13401 | -57.72766 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 29eb8710-3429-3204-b2a9-cd6b45fb17fa | -7.62454 | -61.34226 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 07c83968-b43a-362d-964f-5d7c6f2bbb58 | -7.62512 | -61.34594 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 254c1c2a-f900-3814-a575-0be2d14a9417 | -8.15099 | -64.00259 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| b4642e8a-de77-338d-a497-16efad83919d | -7.52592 | -61.36215 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 21bffb09-be42-3a25-aeb0-0733cbcb7ec4 | -9.19196 | -65.77971 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f25c477-aed6-3e1f-a8de-b5380151e158 | -6.15244 | -57.94254 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7bf82e9-68d1-3133-9153-90a15a1abd9b | -7.21966 | -60.62584 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f7d9ebcb-8973-39de-b7e3-fb43dc3eac38 | -8.85022 | -70.64619 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9762f526-27f6-3383-93a9-c0deaaf79341 | -7.94726 | -72.38174 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6ac82ea9-304a-398c-b1e2-c36226f1d10d | -6.08159 | -57.38481 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4fffc09-dba3-351f-9529-9e26fd0d65ec | -8.76754 | -71.13067 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bf1e847c-1a4b-3e14-95df-0dfb4621576b | -8.56689 | -64.17822 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c99a5b38-2a94-33dd-8c35-7bf8a2f7796b | -9.0317 | -69.57716 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 2d452f83-058d-37e5-ba66-63b23c586022 | -6.95062 | -58.95256 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b708746c-34f2-3a56-9549-24291ecd5e06 | -8.60726 | -70.21084 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0ea29ab1-0b3e-3f58-ae27-2ed2c5bb3ad2 | -4.15172 | -59.39286 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1336c327-2e85-3b72-95cc-76e34d5598f6 | -6.70472 | -58.93131 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 30c24b36-a390-38e8-971c-e6c73feebb8c | -6.32696 | -57.7401 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e280df8a-f2cb-3f6c-8b00-bd3c6c26999d | -8.35506 | -71.05987 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f85cc12d-1371-3034-928d-fb98e5bb2b9f | -7.43719 | -59.77116 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a78619e-0445-3cca-ba5d-9b7df175b2b3 | -7.46126 | -61.39499 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 699eb4b0-8043-3e16-b3b7-1a216b309ae9 | -8.49808 | -70.31734 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 8322a602-f3b2-397f-b271-703ae94a8c5c | -8.63598 | -66.53168 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1ce8589f-8e95-37da-a344-f8b96517f262 | -8.63473 | -66.53328 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d9119169-291b-385c-9f6d-14480c274633 | -6.01726 | -57.78228 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d409657-44df-3e06-afe4-eacb9f5f6614 | -6.72871 | -59.65512 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa555f04-c800-3269-a095-b710bc0f4e11 | -6.93956 | -59.30984 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 408d6237-7c07-3026-ad4d-210f093133a0 | -6.00664 | -57.8479 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4db51038-381a-36b8-8b95-54b2e0d05fe6 | -5.88057 | -57.76826 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4627e0ee-398f-3d9d-92f9-32a407b8336e | -3.34618 | -58.19802 | 2026-08-28 17:47:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3597c1fa-9b6b-34ce-b91c-f25e43174f39 | -6.21471 | -55.4842 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2881a9d6-1dd8-38b0-8363-b751adf8addb | -6.21481 | -53.48014 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5ae9830a-0e56-3879-9863-8b1025dccec5 | -7.34751 | -72.94543 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 7b03e515-1612-3946-95c0-6bd365a2b0e9 | -3.88855 | -60.92572 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b2f0961a-c396-3987-80f1-09fcee4918c6 | -8.27474 | -71.14726 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 80e2d32b-36af-3e98-9731-cacfb1cfc84e | -8.5443 | -70.91039 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 232ea190-1a70-319d-a4d6-790e731be31f | -7.0049 | -59.57266 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2b9db11e-0cb3-33af-9969-3b45e986073f | -4.46203 | -55.66794 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e1b91a07-c658-3479-876b-f2cea7b27731 | -9.12332 | -70.17749 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32c96152-bde3-33c5-a916-e7b872d553a8 | -8.95579 | -68.90066 | 2026-08-28 17:47:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 38eb08ef-fd55-3b14-8e48-b94f00279032 | -4.32691 | -63.33399 | 2026-08-28 17:47:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a1cae0f5-21d8-3405-8107-ba270c8ada93 | -7.92407 | -72.28714 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 2cc686b5-42ee-3a22-853d-af5f20f3d9e8 | -8.0241 | -69.89655 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 69755fa7-93ec-3c1e-993b-1d04c96ab333 | -6.77444 | -59.44098 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ec8843fe-2364-37db-bb0e-14cbf2cd316e | -7.88045 | -73.02794 | 2026-08-28 17:47:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 7cd951f4-211a-3f3a-bb79-245e0ba520bd | -5.99103 | -57.67719 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 7e1e79ef-99e3-3925-8e1e-08222683015c | -8.02754 | -71.01731 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c55c84a5-cdad-3f63-a6ff-7730287d2278 | -8.63663 | -66.53609 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3f128779-6de1-3778-9cc3-7cf0f3875ba9 | -6.37241 | -54.95754 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f83a2fb4-0d15-3a72-b523-c57b62c6482e | -6.54303 | -56.26203 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README153.md)
