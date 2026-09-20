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
| b7702cc9-cc11-39a8-8306-a1d6d2ccc7e6 | -8.4376 | -46.8757 | 2026-09-20 12:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 68a66804-c647-3fe6-b3ec-eccb022cea26 | -14.6661 | -46.6919 | 2026-09-20 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 508.7 |
| a4c5d61a-7ef6-3bcb-bfe2-01c1dbc4f0e5 | -11.379 | -51.42 | 2026-09-20 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 13c8a3fc-8b0e-35c5-9698-48ffba1ff5b1 | -11.118 | -54.0268 | 2026-09-20 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 538fc364-1459-3fc4-89ca-81878463e858 | -12.642 | -50.9359 | 2026-09-20 12:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 205.2 |
| e5ece4c0-20bd-3164-95f2-f33bb5ed1511 | -7.5334 | -45.4367 | 2026-09-20 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 218.4 |
| beba7160-3249-399e-8e0a-695dc9ac2c74 | 1.26111 | -50.73507 | 2026-09-20 12:02:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 26.6 |
| cf901028-dfce-3e98-85be-75f23605dbd9 | 1.99429 | -50.82486 | 2026-09-20 12:02:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 342c0a06-2701-3255-97b9-15ea97b076e6 | -7.58736 | -47.0214 | 2026-09-20 12:04:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 7c5a8cec-b815-3d13-88c0-ad32326df4a6 | -8.76865 | -48.6662 | 2026-09-20 12:04:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 204eea4f-e168-3c79-9c90-6235cd644d80 | -7.17243 | -47.47571 | 2026-09-20 12:04:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| a0c747d6-88af-3656-b9fb-3342c4a8700d | 1.20638 | -50.99816 | 2026-09-20 12:04:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4bd6ffd3-2eac-36d1-9263-fe6aa63e532c | -6.9388 | -55.03572 | 2026-09-20 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| acb12438-e285-379c-a2f1-d5ea99293f5f | -8.44528 | -46.88785 | 2026-09-20 12:04:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f932bdcb-866c-3f6b-a9e5-36eeeecfe209 | 1.20513 | -50.98942 | 2026-09-20 12:04:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ddc5eaf-5ac6-3cf1-8d8e-fa115200da45 | -8.38928 | -47.19559 | 2026-09-20 12:04:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 938e2e4c-7866-3d50-9bf6-9a6dd6cc67b8 | -7.53551 | -45.40697 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| d0818b1a-547b-31f9-9147-91c7d33c77dc | -9.26535 | -45.94753 | 2026-09-20 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| abed01a8-4992-3533-bbb9-575bf291f943 | -8.93122 | -50.91222 | 2026-09-20 12:04:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8be3f71e-32b7-3ff8-ae7e-495574ff0e1c | -3.73787 | -54.64893 | 2026-09-20 12:04:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 87de082a-2c55-3f50-9427-d6872449264a | -7.17447 | -47.46043 | 2026-09-20 12:04:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 9c7e203a-02ab-3272-ba60-d4eeb2fbb136 | -7.58961 | -47.00416 | 2026-09-20 12:04:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 66d5e819-8f7c-3687-be90-f7003a63c2f4 | -7.42476 | -44.73351 | 2026-09-20 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| a5f2681a-e7e0-3d93-8362-73a8086d4ebb | -7.31583 | -55.60673 | 2026-09-20 12:04:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 10caa524-eda9-3a86-9e96-5128c882d842 | -7.53257 | -45.42976 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 308.4 |
| b7accc51-41a5-3b6c-8e18-ed5ddf15ed5a | -2.45726 | -49.22105 | 2026-09-20 12:04:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c0f596e4-96c8-30ce-b573-a5d60d0f3b58 | -8.3935 | -45.62097 | 2026-09-20 12:04:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 6d38f3d5-4560-3b2e-bba3-15903f100c6c | -7.54226 | -45.41438 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| dd5540e8-5fd5-34d6-a80d-29896c42dbeb | -5.81405 | -52.09038 | 2026-09-20 12:04:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b3885926-ca03-3daf-a64a-a6ef2facd948 | -7.75769 | -46.70669 | 2026-09-20 12:04:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| b641a0e7-605e-31a6-8ada-1de7bb40384a | -3.8502 | -44.26708 | 2026-09-20 12:04:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 0f31e5e7-36c7-3523-8cea-fb12cf68a289 | -6.93358 | -42.90315 | 2026-09-20 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.9 |
| a67f2cde-5af2-3d99-847a-4b542344e9bf | -8.61696 | -54.59742 | 2026-09-20 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3e474557-dad5-399c-8cd3-d45549e4b832 | -8.13971 | -46.8059 | 2026-09-20 12:04:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| d73008d3-9cfa-3d61-8de7-d7e014ad62a5 | -7.42685 | -44.74057 | 2026-09-20 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 77eac0c0-b8b6-3e58-ab70-e20446cee084 | -7.56837 | -46.36503 | 2026-09-20 12:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 7b6fa2cd-f2c5-364f-bf1e-7d0489e191b3 | -8.491 | -47.01983 | 2026-09-20 12:04:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e343d69b-ed67-378d-bea0-a95bfb164677 | -5.84787 | -53.53048 | 2026-09-20 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b5310876-1c19-36bc-8180-c69f70c5ed9e | -7.2774 | -45.5677 | 2026-09-20 12:04:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 5148adfd-19f2-3859-afca-d4a93c0bd6f5 | -9.26678 | -48.20036 | 2026-09-20 12:04:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0f6258c3-3375-3fce-92bb-5d61b0f637bc | -7.56587 | -46.38449 | 2026-09-20 12:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 7f24ea82-5457-39e0-8f0a-213cc46a8577 | -7.52249 | -47.3345 | 2026-09-20 12:04:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 609d6aa6-c6ab-3964-b110-a1064acc4908 | -6.9849 | -45.82045 | 2026-09-20 12:04:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6f50494b-2823-358f-8e4a-12eb9c70f0d2 | -9.21725 | -46.22864 | 2026-09-20 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 3d5e5390-5920-327c-a26c-c6b58ddacbc8 | -7.11732 | -48.40698 | 2026-09-20 12:04:00 | TERRA_M-T | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 26cff228-4d6e-3c4a-8ed5-d82b532f70bd | -7.1855 | -47.89503 | 2026-09-20 12:04:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9df66394-4f51-3d21-b5a2-038ddb2e76e8 | 1.15357 | -51.00542 | 2026-09-20 12:04:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f068268b-8f60-350b-96f7-16f0a6a1b90a | -2.45867 | -49.21087 | 2026-09-20 12:04:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 66665c26-0d3a-3674-b2fb-830fc1064bd0 | -9.76196 | -46.06292 | 2026-09-20 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 12394db9-a89a-3a79-92e4-701871b20cb6 | -9.69872 | -48.31763 | 2026-09-20 12:04:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b2913258-8d83-34f3-afe7-2a2d815ddd8c | -7.17654 | -47.44495 | 2026-09-20 12:04:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 02f8880d-591f-3f4c-9512-686fafbd4db6 | -9.04772 | -48.72019 | 2026-09-20 12:04:00 | TERRA_M-T | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3f9a1f2b-d8fc-3654-8afe-73457cac92fc | -8.63311 | -47.61598 | 2026-09-20 12:04:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| e7496aa8-0b54-3b6c-9ec4-efde1a8e5232 | -3.8542 | -44.27422 | 2026-09-20 12:04:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 541c664b-6e42-33dc-a5d8-d37e5f121ffb | -9.27166 | -46.20005 | 2026-09-20 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4d166689-c234-32ae-bb61-00dd75fc2455 | -6.56281 | -44.83168 | 2026-09-20 12:04:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| d7c99fd4-c8e4-39a7-920e-f5d64c48fc6b | -2.92079 | -54.12709 | 2026-09-20 12:04:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2c8a37ca-fd88-3340-86a6-0bf81c1a1f41 | -7.11551 | -48.42047 | 2026-09-20 12:04:00 | TERRA_M-T | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 59b460d9-5fc9-3410-b546-dffb4865d599 | -8.75971 | -48.65145 | 2026-09-20 12:04:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c96fdaee-5070-3614-b232-5402c2163507 | -8.76692 | -48.67912 | 2026-09-20 12:04:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 02768b3f-860c-3a26-b14f-8045270ee734 | -3.35255 | -42.76114 | 2026-09-20 12:04:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 287f9371-56fe-368a-8f90-f15634d91f2e | -7.51961 | -46.23428 | 2026-09-20 12:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 78766b04-a0fc-3186-a9cb-5cfa2187785c | -7.76036 | -46.71352 | 2026-09-20 12:04:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d8cbd677-836c-3cce-b7f9-6e6c2435f007 | -2.89027 | -57.80915 | 2026-09-20 12:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5df6cc68-0df1-3216-9b80-8e0edab716ef | -7.59922 | -55.70817 | 2026-09-20 12:04:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d2b8da48-ee8d-3e1e-9140-0f7f4642c3f7 | -7.52859 | -45.41241 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 2835c846-5296-3287-b89a-85a251d7229e | -7.75285 | -46.74307 | 2026-09-20 12:04:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2c38cc6f-0e9b-3e83-95e1-ab2558b0ad95 | -9.26811 | -45.92509 | 2026-09-20 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4d4202fc-bb31-3bf9-b498-00f3e6088085 | -6.76822 | -55.84491 | 2026-09-20 12:04:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2a0f849e-3fa4-3d1b-84c9-8ce3272643aa | -9.72141 | -47.22287 | 2026-09-20 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 4d898578-caa7-3317-a8af-2941c872b3f9 | -6.76496 | -48.04641 | 2026-09-20 12:04:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b1111ee1-05a3-3e6d-9262-2a4c56efc5bb | -7.32569 | -55.60792 | 2026-09-20 12:04:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| bc14c26c-7bc1-36e4-bf76-ffa03682c3d4 | -8.05865 | -48.48188 | 2026-09-20 12:04:00 | TERRA_M-T | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 21c5b14f-9239-3f4f-bc34-bb89944dba77 | -7.55991 | -45.43317 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 85d11f67-cfe3-383d-8fe5-5f48a61c5e07 | -7.2568 | -55.59837 | 2026-09-20 12:04:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a87a565b-79b3-3370-a6dc-f0e02479f5ec | -8.77612 | -48.7276 | 2026-09-20 12:04:00 | TERRA_M-T | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f6a26109-6ecf-323d-8091-8053491258a1 | -8.35126 | -50.83664 | 2026-09-20 12:04:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 554fa481-f0a5-374c-88e8-c76473308c29 | -6.66723 | -50.88744 | 2026-09-20 12:04:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3dea73d5-f96f-37ee-8452-d6f44c1d00a4 | -8.37467 | -47.58032 | 2026-09-20 12:04:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 42508066-b53e-3e88-935f-9eae8b2716e8 | -8.61554 | -54.60698 | 2026-09-20 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cad8baae-ddd6-30c4-9f6d-44411bc119b1 | -7.52583 | -45.43533 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 203.9 |
| dd13f9dd-8d7d-30db-b7df-55d1a0c7f98e | -7.17041 | -47.49084 | 2026-09-20 12:04:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| c80e587a-1d76-38af-ae5e-089de49047fb | -5.75202 | -57.58558 | 2026-09-20 12:04:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 441bf821-56e2-39d7-ad93-dc5e62e6b58f | -7.88321 | -44.85375 | 2026-09-20 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2a24eb63-7d1d-350c-bdcb-80d40ca5b9c3 | -7.69307 | -46.10485 | 2026-09-20 12:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5dc6ace9-c0d1-374c-b2a5-7ca4f7ec2f4c | -7.63404 | -46.75936 | 2026-09-20 12:04:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 2c9019fa-b07e-30a1-82cf-60e09ac2dc20 | -9.72363 | -47.20484 | 2026-09-20 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 486ec3b6-d17a-3128-ab11-af04f06fab74 | -9.27798 | -48.20189 | 2026-09-20 12:04:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2103b684-8285-3cf3-9581-8ed2ad6510c2 | -7.51893 | -45.42783 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a4de3d83-04ab-3443-901f-a630cd8a670d | -8.15258 | -54.80718 | 2026-09-20 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6d1156a0-2ed3-3157-9c98-8d262f544ed7 | -8.45441 | -47.65113 | 2026-09-20 12:04:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 251dcf5d-a6b6-302c-88f3-01b49ac6a65a | -8.44241 | -46.88105 | 2026-09-20 12:04:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| affc405b-ed70-315a-a238-201f41878f5e | -0.52253 | -49.15079 | 2026-09-20 12:04:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 11aca5fb-3796-388e-aa63-0cee1e0bda74 | -7.88053 | -44.84788 | 2026-09-20 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 5833d076-6f24-3a0c-b5e7-e813673271c3 | -7.52185 | -45.40498 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 8567030f-0515-3207-9a1f-6f8ea7c373bd | -8.43009 | -46.87951 | 2026-09-20 12:04:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 539cc52a-172c-3e4f-b4a2-922139aa139c | -7.75526 | -46.72495 | 2026-09-20 12:04:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 008f83d6-00d9-3ae1-90b2-743900477764 | -8.7704 | -48.734 | 2026-09-20 12:04:00 | TERRA_M-T | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 723bfdff-6d71-3c54-a71d-4475e988a938 | -8.77224 | -48.67282 | 2026-09-20 12:04:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 46089b23-245b-39de-b163-5740c269c467 | -4.49697 | -55.48322 | 2026-09-20 12:04:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README110.md)
