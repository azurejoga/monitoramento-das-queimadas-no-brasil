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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6543cfa5-b92b-3713-af8e-bc112e96ef16 | -21.9374 | -48.5688 | 2024-09-26 06:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 84f0a52e-d17f-350a-86c2-c134508aa1d1 | -8.97852 | -68.63943 | 2024-09-26 06:40:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 209767f6-d572-3f7f-8a9d-f176b4bd479a | -8.9779 | -68.64435 | 2024-09-26 06:40:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cb167d2-ef98-34fd-aa19-78aaddf2186d | -8.43328 | -70.78992 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7d1bc7d-c20d-3bfe-84cf-2f6a7fb80b1a | -8.43283 | -70.79324 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bc7e377-f502-353f-9e5e-1016f9f6c9ff | -8.43237 | -70.79655 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f7c793f-7f91-3898-bd53-c341f1673fa8 | -8.43138 | -70.79192 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7aaa8c6-ffc2-3374-a2be-66193e64b41a | -8.43095 | -70.79523 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab1d9cd7-fcd3-3b15-90a0-c7f96d42e1a7 | -8.41071 | -70.75571 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 66fed7e7-0908-31f6-8a98-9f88c72d5239 | -8.41026 | -70.75908 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4cdfb72a-9f6e-3a06-8ff2-7ae652176fe0 | -8.4098 | -70.76245 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fe2c360-9e6b-3341-a5b5-74a1a65fe027 | -8.40536 | -70.75498 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d991de32-02ad-3bab-9ed9-d661035cb082 | -8.4049 | -70.75835 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3abbccef-f986-3108-b235-538d8abb798d | -8.40445 | -70.76173 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 303fef88-fb04-336d-863d-da58d8ed6768 | -8.03138 | -71.02449 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eab88457-f95d-33ab-8290-c6bd77167541 | -8.02616 | -71.02376 | 2024-09-26 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf36813c-548f-37cc-8001-b7ede68f7942 | -10.39685 | -67.87412 | 2024-09-26 06:40:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58d97dd3-3dba-31f9-9708-99ba2a693c42 | -10.39519 | -67.8735 | 2024-09-26 06:40:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5d8737e-12d3-355c-bc9c-f7ccbd62df5e | -10.39027 | -67.87312 | 2024-09-26 06:40:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08e9fb34-400f-341c-ac93-4434647de6e1 | -8.4156 | -70.7535 | 2024-09-26 06:45:55 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 49486d8a-3b66-3509-b2dc-a52c411fb03e | -9.1217 | -61.3334 | 2024-09-26 06:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2703a97c-55f4-3c53-9dc6-0fb676857e75 | -9.1216 | -61.3526 | 2024-09-26 06:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 69ccaf6a-f02d-380a-a86a-a3ffd3ab7ec4 | -9.1032 | -61.3343 | 2024-09-26 06:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 27a58ccd-975f-3a9c-8a31-7e631b1a90fc | -9.086 | -61.1245 | 2024-09-26 06:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 76fe7006-4ae3-3a47-8cc5-bad32926cdd7 | -11.2788 | -65.2793 | 2024-09-26 06:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 1f05627d-08fd-31ba-a014-9b056b3fc9dc | -11.26 | -65.2801 | 2024-09-26 06:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bd45fa72-0d5d-375b-b8fb-edc96e2af062 | -11.2599 | -65.299 | 2024-09-26 06:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| d2c2db8e-846b-3809-950b-22bf0fe4f82a | -11.616 | -60.3463 | 2024-09-26 06:46:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 36.1 |
| c1fe7226-96b2-3ac7-aa25-dc658adae8bd | -11.5972 | -60.3475 | 2024-09-26 06:46:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 647d6baf-b1a9-395e-af8c-f6325cb06456 | -11.597 | -60.367 | 2024-09-26 06:46:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 10629bd7-169f-38b6-bf38-c9a4ebef1318 | -16.8234 | -57.4789 | 2024-09-26 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 839bdbb0-3d7f-3a8d-a37b-4b13f0132229 | -16.8231 | -57.4994 | 2024-09-26 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 597d0b2e-333a-3152-bcea-e58676400eee | -16.8039 | -57.4811 | 2024-09-26 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 6a1eaba2-3d10-31ce-967e-7f8092d31486 | -16.8036 | -57.5016 | 2024-09-26 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 2745a092-4b55-37e3-b982-da4520490ef0 | -21.9374 | -48.5688 | 2024-09-26 06:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 28fa3d61-56e1-384e-b44b-29f3f9d5b392 | -6.9306 | -63.1053 | 2024-09-26 06:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 16061a5a-6ca7-353e-94ec-e69d3c8d6fc6 | -7.2905 | -61.106 | 2024-09-26 06:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 80666418-ec48-303a-8ccc-a179aa805ad6 | -8.1394 | -61.2817 | 2024-09-26 06:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| e6814bcb-fbc5-3647-a5c4-af44417d5bc7 | -8.4156 | -70.7535 | 2024-09-26 06:55:55 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b31c7768-066d-31f9-849d-0b18d8c8e75d | -8.8293 | -63.699 | 2024-09-26 06:55:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 02983bb9-de49-3b86-8633-801a0f9b95d9 | -9.1032 | -61.3343 | 2024-09-26 06:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e21d7234-6d92-3520-b6e6-ab3f7fe78bc9 | -9.1046 | -61.1237 | 2024-09-26 06:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 0af42177-0630-334f-9ca8-60ad9c68828c | -9.1216 | -61.3526 | 2024-09-26 06:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2067ff33-911a-386d-8669-4fb21f292e4a | -9.1217 | -61.3334 | 2024-09-26 06:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 01899ff0-e96d-3122-9c55-793df1aed39c | -11.2599 | -65.299 | 2024-09-26 06:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6e3e376f-ee6b-33c9-af39-4814fdd97b21 | -11.26 | -65.2801 | 2024-09-26 06:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 476ae567-48d3-38b7-8988-9419c11f1d2d | -11.5972 | -60.3475 | 2024-09-26 06:56:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 83819f6c-8298-3bc8-ad49-bc5c3db4fa7e | -11.616 | -60.3463 | 2024-09-26 06:56:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 6c38820f-4f74-3a07-9414-29a9d7123f28 | -16.8036 | -57.5016 | 2024-09-26 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 67732b7e-9860-3cbb-8da3-bf1d06ed03c5 | -16.8039 | -57.4811 | 2024-09-26 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 9a198cda-7120-3edb-ba26-eac9bd5d7f34 | -16.8231 | -57.4994 | 2024-09-26 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 807b4066-a035-3d30-816c-8577f87dca79 | -16.8234 | -57.4789 | 2024-09-26 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 7ee7baa6-e3bf-3d5d-a3a0-1db28e441adf | -21.9374 | -48.5688 | 2024-09-26 06:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ec01eaeb-7764-3b68-a9eb-1e65d590e074 | -17.1 | -56.19 | 2024-09-26 07:03:48 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a9129ee8-c736-346c-ae41-0da9442108b8 | -16.85 | -57.76 | 2024-09-26 07:03:51 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 822ae79e-22d9-3634-88e6-1a3efb5000df | -12.86 | -51.27 | 2024-09-26 07:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9ea8f2-c530-331b-8ebd-8ca0ca43d781 | -12.89 | -51.28 | 2024-09-26 07:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fca7796-db94-383a-8498-9530c76e64ff | -10.04 | -53.48 | 2024-09-26 07:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2ef1045-ffa1-3c25-8833-72b59577961a | -10.01 | -53.54 | 2024-09-26 07:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 048f3d9c-557f-3a2a-9a26-ea222a4ad450 | -10.01 | -53.48 | 2024-09-26 07:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25f98d89-f063-3a1e-8fd1-2153fdb0e656 | -6.9306 | -63.1053 | 2024-09-26 07:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 1007f342-dbcc-339f-bb85-1e1c35b03e08 | -7.2906 | -61.0869 | 2024-09-26 07:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| c74f6b81-77cc-3aea-8b65-c3b046a4d706 | -7.2905 | -61.106 | 2024-09-26 07:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| bba2ed90-2c70-3bf9-a2b1-10b7d8f8c978 | -8.1394 | -61.2817 | 2024-09-26 07:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 3ee941ba-0b2d-3f6a-8604-5b114d42134f | -8.3971 | -70.7538 | 2024-09-26 07:05:55 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 44.2 |
| f7d724c9-e20a-3179-bb19-6f1a42e729c2 | -9.1032 | -61.3343 | 2024-09-26 07:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| e60bee63-babf-3e7c-86f1-30495e9d3101 | -9.1216 | -61.3526 | 2024-09-26 07:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1dcc42a2-b05c-3fbf-b928-94936d1c426a | -9.1217 | -61.3334 | 2024-09-26 07:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4d92486e-d236-3b29-84ba-ac7857742a5f | -9.1219 | -61.3143 | 2024-09-26 07:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| e177236d-8b6e-3b78-8f27-c44e054aceb4 | -11.1845 | -54.7769 | 2024-09-26 07:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 79e68b93-bc00-3a8b-a96c-29b963da4776 | -11.2031 | -54.7956 | 2024-09-26 07:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 29632dc7-42dd-3934-8cad-f1b614a3d96a | -11.2034 | -54.7752 | 2024-09-26 07:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 320.9 |
| b6f2a0d5-0b4b-3757-afa5-3a345b5e337e | -11.2036 | -54.7548 | 2024-09-26 07:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 476b2498-159c-3cd5-8f4b-3935770022ec | -11.2223 | -54.7735 | 2024-09-26 07:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 33649108-54b6-375a-95c9-c5b424d2538c | -11.2599 | -65.299 | 2024-09-26 07:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 91fdf9e3-1991-378e-b66a-76655bf0fca2 | -11.26 | -65.2801 | 2024-09-26 07:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3c02dd26-9dd7-3d6f-ac00-c430f2d5c2fd | -11.616 | -60.3463 | 2024-09-26 07:06:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| f00620d3-2f53-38ec-bb9a-37fdaf570237 | -16.7992 | -57.7876 | 2024-09-26 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 55996f5e-e794-3176-b391-f81e80e4d57a | -21.9374 | -48.5688 | 2024-09-26 07:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c9698ae7-c41c-3875-b3ac-2e105b0cbd47 | -7.2905 | -61.106 | 2024-09-26 07:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 9aa3c54a-0b1c-3d81-91a8-96b93422719a | -7.2906 | -61.0869 | 2024-09-26 07:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| f667afbf-3c14-374a-ac47-62785abe4e72 | -8.1394 | -61.2817 | 2024-09-26 07:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 6cdd5e5a-0d43-36e3-abb1-e1621c4b7419 | -8.3971 | -70.7538 | 2024-09-26 07:15:55 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d01c36d3-4509-3d01-929a-1580f3bd441f | -9.1032 | -61.3343 | 2024-09-26 07:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 80a0e9d9-37b1-3d15-878c-fc47febca0b5 | -9.1216 | -61.3526 | 2024-09-26 07:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 17e06b6d-2b82-3b3d-9367-d8445df45ae9 | -9.1217 | -61.3334 | 2024-09-26 07:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| edd15141-ae1c-31c5-93b0-0552bd701ce6 | -11.2034 | -54.7752 | 2024-09-26 07:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 292.1 |
| fa953e03-5427-3090-95c1-3d1725cfb773 | -11.2036 | -54.7548 | 2024-09-26 07:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| a14b1866-0709-341e-97b1-8643ed29ba95 | -11.2223 | -54.7735 | 2024-09-26 07:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f0e19f6b-3bde-31c8-b22e-70138bfdde53 | -11.2031 | -54.7956 | 2024-09-26 07:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 177693be-eef1-3750-a110-e704996cbe68 | -11.2599 | -65.299 | 2024-09-26 07:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ddd2dc45-830c-3187-a64a-ad26323edf95 | -11.26 | -65.2801 | 2024-09-26 07:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2fe7fe00-7c8d-336c-ac28-bcca749f763c | -16.7992 | -57.7876 | 2024-09-26 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| dfb96605-0a50-36a4-a60c-66f1d83937f9 | -21.9374 | -48.5688 | 2024-09-26 07:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 418c835b-4c49-319e-ab71-58c39ed3b7ea | -21.9381 | -48.5453 | 2024-09-26 07:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3ca3e51e-a3f3-3aaf-a5b9-727a65197ffa | -8.40282 | -70.75544 | 2024-09-26 07:20:00 | AQUA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 7790b5d7-fb0f-3adc-bb12-a992ca43ef7e | -7.2906 | -61.0869 | 2024-09-26 07:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| dc38a9b4-79c3-3dae-8418-77588dd815bd | -7.2905 | -61.106 | 2024-09-26 07:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| c09d7573-5bd5-3405-ae77-3c18f611a7d0 | -8.1394 | -61.2817 | 2024-09-26 07:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 4114ad44-d893-38be-a86c-155aada2c28a | -9.1217 | -61.3334 | 2024-09-26 07:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |


[Clique aqui para ver as próximas entradas](README173.md)
