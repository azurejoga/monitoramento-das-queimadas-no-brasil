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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e0db1a2-9d77-3226-baea-d5ba41a0d431 | -20.98988 | -45.80325 | 2026-09-05 03:28:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99438698-a76c-3814-a9d2-60d23d784dd5 | -18.17194 | -42.93885 | 2026-09-05 03:28:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6f68c741-f59e-3ac9-88cd-b60a5f030c8b | -19.83646 | -42.70559 | 2026-09-05 03:28:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a153568b-e46f-3ffa-9a1f-93ce64cbfd14 | -21.55025 | -44.0585 | 2026-09-05 03:28:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1d50eade-9faf-39ec-9f8c-dfdf34cd16d9 | -17.3007 | -43.3449 | 2026-09-05 03:28:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ded5ff8d-6edc-31d4-820c-7a1a64b7e765 | -21.45609 | -45.77019 | 2026-09-05 03:28:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 19410d52-8c20-3ee9-9189-731475b5ffc3 | -6.6513 | -59.9642 | 2026-09-05 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 10736e94-4485-327f-85f4-12ff824ca812 | -6.6697 | -59.9635 | 2026-09-05 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 076ad266-8dc1-3395-836a-20532510fb84 | -5.6565 | -60.2475 | 2026-09-05 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f6a6c47d-543f-3a9d-b3d8-2f34a94b7837 | -14.905 | -44.6782 | 2026-09-05 03:30:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d9a15381-7c38-3e47-a237-0a89f912b523 | -6.6514 | -59.945 | 2026-09-05 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.0 |
| e413d9f8-d949-388d-a19b-7d57586233dd | -5.9197 | -47.8927 | 2026-09-05 03:30:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| d51cf335-73b8-3eba-ace9-fb859df38217 | -5.3462 | -56.0256 | 2026-09-05 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a5bcf21a-a4a0-378f-a9e1-0d8f027ab6c7 | -6.6698 | -59.9443 | 2026-09-05 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.4 |
| ae82e654-f0af-3acb-aa62-cb0f7f73978f | -5.3277 | -56.0263 | 2026-09-05 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| b2280e16-6377-3e8e-92f3-5861342c5fda | -6.6697 | -59.9635 | 2026-09-05 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c84f630f-2d0b-3288-b5fe-d9773c93bbe6 | -4.6669 | -55.635 | 2026-09-05 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c68f42dc-6fbe-328f-991b-e1329dd2c7d2 | -6.6514 | -59.945 | 2026-09-05 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 27d4a726-bd66-3809-9b74-3a835fde4816 | -6.6513 | -59.9642 | 2026-09-05 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| b54723c0-3ec6-314a-8e97-fcec7a4438f3 | -5.3462 | -56.0256 | 2026-09-05 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 459c1543-80c6-3837-86c6-a71fd9a53a04 | -5.9197 | -47.8927 | 2026-09-05 03:40:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c6080784-38d4-3da7-9f8a-214f327c02dc | -5.3277 | -56.0263 | 2026-09-05 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| e14f7313-2ffc-3c6d-9bd0-bf23edc1650f | -6.6698 | -59.9443 | 2026-09-05 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 99372fc0-2d94-3d8c-86f2-b59268bda7c3 | -6.6698 | -59.9443 | 2026-09-05 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 1efeb020-d48f-3bc2-ba50-5b944ff9d23d | -6.6697 | -59.9635 | 2026-09-05 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 40fd60af-8577-372a-8546-a666d9ab0dce | -5.346 | -56.0454 | 2026-09-05 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 080fe303-6c12-3e53-bcee-1e18d129e3f9 | -5.3277 | -56.0263 | 2026-09-05 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 0230f179-3b85-3f66-b236-adb770f9e9e0 | -5.6565 | -60.2475 | 2026-09-05 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3219e950-23ee-391f-90f9-cf33e4970d9f | -6.6513 | -59.9642 | 2026-09-05 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 207f3844-bb24-3ca6-8f29-b8523acbe60f | -6.6514 | -59.945 | 2026-09-05 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 55f636a3-dcae-34b3-a43e-8d28dbf712ed | -5.3462 | -56.0256 | 2026-09-05 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 8b7a6802-8bed-31bb-b7f3-d324e02008f3 | -3.7645 | -61.7737 | 2026-09-05 04:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| a437824c-b7dd-3309-b147-713d721676b7 | -6.6514 | -59.945 | 2026-09-05 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 08d1b00c-a8b6-3317-a89c-3fabca2fbc7b | -6.6697 | -59.9635 | 2026-09-05 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1b48677f-08eb-3086-8059-57dbfee68844 | -5.3462 | -56.0256 | 2026-09-05 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 7fe34087-ebf5-354a-a0be-c57bd83d338d | -6.6513 | -59.9642 | 2026-09-05 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ac879d6c-371d-3e21-9e58-cb8f92e1511d | -5.346 | -56.0454 | 2026-09-05 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b69dd180-56f2-358e-a9a8-3fd0f185caa2 | -6.6698 | -59.9443 | 2026-09-05 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 88b57b06-a1af-34f7-9011-749e2449e456 | -5.3277 | -56.0263 | 2026-09-05 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| df7f6a86-ab50-30c9-b46f-c422878233cd | -5.3646 | -56.0249 | 2026-09-05 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5353b5cb-aa5c-35ee-acf5-278a8f8b1656 | -4.2682 | -38.01772 | 2026-09-05 04:00:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7d279c03-627a-36f3-8fc3-64c4db916ebe | -5.9738 | -43.62452 | 2026-09-05 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 138579d2-7817-3f45-980d-050d5c5481df | -5.77139 | -45.06979 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 61b1e77b-3c6c-3a47-b3eb-056d05910f89 | -6.17401 | -47.08529 | 2026-09-05 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8e0dc0cf-ee9d-347c-8afb-e87c17dfb582 | -6.72074 | -38.23892 | 2026-09-05 04:00:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0badab61-7f8f-32cb-b4d8-9379eaf1588e | -6.17413 | -47.08519 | 2026-09-05 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 024ac816-26dd-3823-93cd-50127e93554b | -6.71754 | -43.47911 | 2026-09-05 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b37ad10d-b0fc-36dd-b7e5-6b44165ed3a5 | -7.20693 | -43.5992 | 2026-09-05 04:00:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| edc55f15-2886-3a9c-b63b-17a7f4ba2b5e | -4.18189 | -42.44673 | 2026-09-05 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4616c5ab-68bc-34fe-a7cc-26fd83150fb3 | -4.41435 | -43.95299 | 2026-09-05 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 572628d8-6060-3337-abb7-0ee736132fb3 | -6.12421 | -43.75678 | 2026-09-05 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c275a91-2cec-32c2-9577-2cc2d52df68a | -5.77088 | -45.07273 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6b52b809-ce09-39a1-93a9-6949a282915e | -6.12504 | -43.75199 | 2026-09-05 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47566dc3-d61d-3e06-80d2-edd3a5e523db | -5.32652 | -45.16889 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 079ad0f7-d741-3157-8507-ea59fd827d43 | -6.55955 | -44.77702 | 2026-09-05 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1303f6b-060b-3e4a-9dbf-5c12ddb736e4 | -2.76303 | -49.48308 | 2026-09-05 04:00:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41298173-70ee-3c25-a898-383d52d7fa71 | -2.81055 | -48.67269 | 2026-09-05 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb39883e-a9b0-39a6-892d-6da062436d3d | -6.67363 | -38.85192 | 2026-09-05 04:00:00 | NPP-375D | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e61281f3-fc2e-3f48-8f58-6c346b69a3b0 | -5.97996 | -43.61605 | 2026-09-05 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85687f20-0c4b-39f0-9013-1b0bbf5a7f92 | -3.71445 | -39.6269 | 2026-09-05 04:00:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d47a6c9-7981-3502-8c8c-976f82ef9c21 | -6.126 | -43.75513 | 2026-09-05 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 450f7070-c18c-3925-b044-c1cd6eb52a8c | -7.2077 | -43.59469 | 2026-09-05 04:00:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4c0c29c-c299-3282-8d1e-9d6bdc6080c9 | -7.69875 | -44.33673 | 2026-09-05 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59f06e87-89c6-302b-b3fe-4b99cfea6869 | -2.81337 | -48.67398 | 2026-09-05 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c57d9320-29ad-3278-8435-4efde715c979 | -5.97538 | -43.61533 | 2026-09-05 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e2bf322-7eeb-3b4e-af3e-2fdeb8ddf5d2 | -4.54062 | -38.45163 | 2026-09-05 04:00:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5089aa67-f96f-31c7-9b63-d23ca28ff18f | -5.67324 | -45.30222 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1326d85a-574c-3672-af16-d8abfd7bec17 | -6.1268 | -43.75036 | 2026-09-05 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34ddb4fd-42eb-362b-8bb3-a038c13d9e94 | -2.80565 | -48.6787 | 2026-09-05 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c6433c3b-fa8a-3bdb-9ce4-d8a88dfb298b | -5.92473 | -47.89462 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6cbe4119-9ce6-36d2-a283-849fc450f59a | -4.17761 | -42.44365 | 2026-09-05 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ef9e478-b809-3d67-8b3e-d795a6c1e8e3 | -8.64545 | -38.14911 | 2026-09-05 04:00:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6f146439-7f46-3fd5-806f-bb872ccaae56 | -5.77039 | -45.07564 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 67d4465e-2cac-30d9-a60c-0b4a9138fd0e | -2.82162 | -46.70773 | 2026-09-05 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69a5d91f-d50e-37bc-9b77-6c1d59a1f4c9 | -4.36788 | -47.77821 | 2026-09-05 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe863b39-0ce0-3558-a18c-76d9fbbdb458 | -3.46841 | -43.34517 | 2026-09-05 04:00:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda0c9f1-0369-32ab-b934-1814502caaed | -4.1746 | -42.43697 | 2026-09-05 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34265327-f4b1-3dc6-b01d-8d0216fd0213 | -5.92388 | -47.89925 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b542e0f5-5972-3962-bd17-adab81ac2ba1 | -3.44151 | -43.27536 | 2026-09-05 04:00:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20439cbd-c023-388c-bb16-76f1def503ea | -5.97301 | -43.62913 | 2026-09-05 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e3a759f-44cd-3abe-8774-7f1df99fc2c4 | -5.2085 | -39.40796 | 2026-09-05 04:00:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b5574e09-ae39-3f44-988b-88bf66c1b79c | -3.05106 | -39.92918 | 2026-09-05 04:00:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6da623ca-c5a0-3135-84a8-a378e97e9782 | -4.26879 | -38.01406 | 2026-09-05 04:00:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 820822cd-9cb9-32ce-87ec-ed8ec1732d10 | -5.42135 | -36.76347 | 2026-09-05 04:00:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b692592e-7fa0-3bdc-bf6f-a1793b1934d3 | -7.45979 | -46.14128 | 2026-09-05 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 923de1b6-e4ff-3cf9-a9cc-7d05a8892274 | -6.30372 | -37.70071 | 2026-09-05 04:00:00 | NPP-375D | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 85ab74f6-2cc7-3308-8d63-ead5ff8ad30f | -6.34645 | -46.10787 | 2026-09-05 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da6dd3e5-fa5f-3170-8d36-04d54828e5c0 | -4.26538 | -38.01352 | 2026-09-05 04:00:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 1b63105d-e49d-352b-acd9-6b54c297ebf3 | -4.17754 | -42.446 | 2026-09-05 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f19b9329-4e19-31ee-9e76-466f8612d1f8 | -7.72067 | -42.86083 | 2026-09-05 04:00:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 594bf938-25e0-316d-8b7e-439357037e80 | -3.83298 | -40.10849 | 2026-09-05 04:00:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f4a2901-b20b-3ef7-bfdc-17e117e2c14b | -4.36315 | -47.78127 | 2026-09-05 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d0083d09-c475-328f-8852-ed3d1cf1e75e | -2.88784 | -40.39537 | 2026-09-05 04:00:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1f6e29b5-1b27-3b3e-9c89-baf92d7266b7 | -5.8 | -43.6511 | 2026-09-05 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7e68f98-4f14-3b9a-b6a2-9457439a3fb4 | -4.36169 | -47.77713 | 2026-09-05 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94c91047-9794-3ef5-a650-8a772376db05 | -2.82089 | -46.71195 | 2026-09-05 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66cfbb6b-96a9-318d-8e96-122bbd7a64c6 | -2.89428 | -40.10905 | 2026-09-05 04:00:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b7509e5-c17d-3515-bff6-5a74bbe8e3e1 | -8.64211 | -38.14857 | 2026-09-05 04:00:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fd28bd49-6b7c-3a6d-a4c7-49726bc692a7 | -2.80956 | -48.67859 | 2026-09-05 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a902bcd-cadb-3fc8-bd59-2c31e04d5791 | -6.55565 | -44.77032 | 2026-09-05 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
