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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5983fe0-c3ec-3e91-987e-68a37d066a5f | -13.3055 | -51.3235 | 2026-09-14 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| aab68118-d9e5-3c70-8c55-7ada217218f7 | -14.1856 | -47.407 | 2026-09-14 12:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f468025d-37fb-3136-93e9-6769eb1fbd5d | -9.3763 | -50.1139 | 2026-09-14 12:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| f9e43416-81ed-309b-9f9e-4af0caf6f9fc | -5.1439 | -55.9543 | 2026-09-14 12:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| af9c541b-b860-3b1f-9ece-c2d11b0be483 | -10.6641 | -54.1491 | 2026-09-14 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| ec274d17-7642-3a76-a55f-10ae292d36e6 | -8.8081 | -45.8753 | 2026-09-14 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 480.7 |
| df8c99e8-c4a9-3a68-9673-47ba083074c6 | -5.1255 | -55.955 | 2026-09-14 12:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 68e5049e-740d-3e4e-a6fb-cc360c203d54 | -13.2863 | -51.326 | 2026-09-14 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e3fc5587-6efe-350d-8e5f-61f621f62afb | -8.6001 | -44.4609 | 2026-09-14 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 59e285e0-1291-3812-8c5d-d93f0bd34172 | -13.2867 | -51.3046 | 2026-09-14 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9500334a-6064-37fa-a642-9096513a47e7 | -8.7445 | -46.4213 | 2026-09-14 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 62dd2312-ae44-3672-a51c-8c5901fd11a5 | -15.5572 | -48.7953 | 2026-09-14 12:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| db145861-a5f2-31e1-8a40-b104a25741a6 | -13.6349 | -47.8969 | 2026-09-14 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 6ae32174-6762-3f2a-a928-acb6c6b4c0e1 | -8.5812 | -44.4629 | 2026-09-14 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 965909d7-347a-3ca2-b1a8-ef65e08d3156 | -13.4458 | -43.8128 | 2026-09-14 12:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 07591bbe-2f6d-3b04-9973-eda21560c5bf | -14.205 | -47.4039 | 2026-09-14 12:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 5fe95735-a625-37dd-879d-0ca0416c96e4 | -10.6829 | -54.1475 | 2026-09-14 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 80341273-19de-3082-a62b-6d684f26978a | -6.6767 | -58.7105 | 2026-09-14 12:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 2ea5aa33-65b1-393c-93eb-bd7931434c12 | -9.4325 | -50.1299 | 2026-09-14 12:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e604a266-12ae-3804-a6ca-ea2192f28041 | -13.4264 | -43.8163 | 2026-09-14 12:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 904f96a9-06da-37ea-8da0-42be96ae2b48 | -13.3059 | -51.3022 | 2026-09-14 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 729ab07b-b551-30cb-8ad6-20818cf9c766 | -8.6194 | -44.4357 | 2026-09-14 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e15acdf5-cac9-3d4e-8557-2b0520cda732 | -10.6827 | -54.1679 | 2026-09-14 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 7a1daeea-866a-3f40-8ddd-f81c87e6c34b | -3.8042 | -44.1072 | 2026-09-14 12:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| fc3485a4-ffce-3f0d-b60a-26c2da971a45 | -13.2867 | -51.3046 | 2026-09-14 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 8adf02a3-19f9-39d0-8375-a215e0410e06 | -13.2863 | -51.326 | 2026-09-14 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0b45c739-7df0-3fb3-89d0-f01dce012424 | -9.4328 | -50.1086 | 2026-09-14 12:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 57581c07-4d05-31c3-8054-27e14512ca71 | -13.3055 | -51.3235 | 2026-09-14 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.9 |
| af974b68-a5bf-392f-bc14-aaf9a9815b1b | -9.4325 | -50.1299 | 2026-09-14 12:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| e039d6d3-3514-34a4-bfcb-bb64999db1bd | -8.7634 | -46.4194 | 2026-09-14 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 305.7 |
| bbed8d38-76b5-39c9-b3cd-bccc90b6f851 | -13.47 | -48.4772 | 2026-09-14 12:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f57e2452-7317-302f-b93d-35168bcc86a6 | -6.6767 | -58.7105 | 2026-09-14 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 6b9fd80a-ca68-3991-86e0-9441191f716f | -5.1255 | -55.955 | 2026-09-14 12:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 0585223b-c0db-3d4b-8fa4-6f74cf2cc723 | -13.4458 | -43.8128 | 2026-09-14 12:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| dcbd9b3a-0054-304e-a15e-69ff313ef534 | -14.205 | -47.4039 | 2026-09-14 12:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 22577a27-eb8f-3ced-90b0-ae25eda30fb0 | -8.8081 | -45.8753 | 2026-09-14 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 837f08b3-d71d-3415-bf8c-3ba0b57cb798 | -10.6829 | -54.1475 | 2026-09-14 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 982b2174-938b-34d4-a254-8ec6c7986ff2 | -13.3059 | -51.3022 | 2026-09-14 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 98e2824d-0bb3-3f59-8aa3-be3c4436e969 | -14.1856 | -47.407 | 2026-09-14 12:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 56e3a95c-d007-3782-ad62-3cd48e109a85 | -8.6001 | -44.4609 | 2026-09-14 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 47322c55-b761-3d2d-b4c1-3d654b68de19 | -8.7445 | -46.4213 | 2026-09-14 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 167.0 |
| b134b325-b400-30ae-b1bb-f6a374192f51 | -5.1439 | -55.9543 | 2026-09-14 12:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 72a22b27-ee3d-33ed-ab7e-a161c10c23d3 | -13.4704 | -48.455 | 2026-09-14 12:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| fdd4f4d1-8b04-35c4-8023-87d001d5d3ec | -13.4264 | -43.8163 | 2026-09-14 12:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| fcde8ece-7407-3f35-9eeb-e7831afbcde0 | -10.6827 | -54.1679 | 2026-09-14 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 2ef15588-82d8-3393-a24c-a39dcb10ce6c | -10.6641 | -54.1491 | 2026-09-14 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| fc69f496-f87d-3fb2-b190-12a6498140d1 | -13.4458 | -43.8128 | 2026-09-14 12:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 54cb5dbe-448f-36a0-93b2-104a45041392 | -13.2867 | -51.3046 | 2026-09-14 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 359.0 |
| b19bc046-a8fc-332d-8fb0-412cf8ea65dc | -13.3059 | -51.3022 | 2026-09-14 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 4dcd0753-a9f9-3d03-ac79-96e85cd5ae3d | -3.7855 | -44.1081 | 2026-09-14 12:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f15b12a4-f552-3d71-a8fc-c08c4affd18b | -5.1439 | -55.9543 | 2026-09-14 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 174e5e99-3ec0-3cf9-af5f-710c2eec87de | -10.6638 | -54.1696 | 2026-09-14 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| bdf54907-d21c-3be9-94c3-724d9bc4bb74 | -8.6001 | -44.4609 | 2026-09-14 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 3d40ce96-e412-36bd-b468-6ad84f28b690 | -14.1856 | -47.407 | 2026-09-14 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9f9ba466-49d0-39ea-b829-be1eb19a8544 | -8.6005 | -44.4378 | 2026-09-14 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a48c287b-5caf-3e36-bd83-7873435d679c | -9.4325 | -50.1299 | 2026-09-14 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 3a46230e-7785-3dfd-a4c2-3bc05ab9efc4 | -10.6827 | -54.1679 | 2026-09-14 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 621c5431-c9e1-3ea9-b56f-5c96a3a19df3 | -3.8042 | -44.1072 | 2026-09-14 12:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 1c432693-00b6-30b5-a9e2-cc0b22348e83 | -15.5572 | -48.7953 | 2026-09-14 12:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c26fdaa7-2dd5-33ee-924f-7fba4258d750 | -9.3763 | -50.1139 | 2026-09-14 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 80190d74-106e-301d-93e0-33e2d677b172 | -14.205 | -47.4039 | 2026-09-14 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 291.1 |
| d212c7cc-245e-3556-808d-d4663c410969 | -8.8081 | -45.8753 | 2026-09-14 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 8ace02a7-ecc4-36a1-886a-7a6e40419f84 | -13.2863 | -51.326 | 2026-09-14 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 4d62243c-4541-3d2b-bd6e-ec71ce3a3b77 | -5.1255 | -55.955 | 2026-09-14 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| bddba79b-e7c0-30b4-a2f7-ef45dbd5a717 | -13.3055 | -51.3235 | 2026-09-14 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 13287795-50bc-3a06-b89d-d1cad710feaf | -10.6829 | -54.1475 | 2026-09-14 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| b685da93-32e7-388d-9289-47f28be0506a | -10.6641 | -54.1491 | 2026-09-14 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 92be079c-9de3-38c9-8237-55bc755c98d9 | -8.6194 | -44.4357 | 2026-09-14 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 6ddbc067-0844-3221-adaf-7ddcc9fbbc45 | -14.2046 | -47.4265 | 2026-09-14 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5151f442-f8c2-3f31-a49e-a74904c7bcd3 | -9.4328 | -50.1086 | 2026-09-14 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| e043559a-0eb9-3087-ab0d-59c2231acabb | -6.6767 | -58.7105 | 2026-09-14 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 4b23fb66-d95f-3cab-9a74-789737cc030f | -9.4325 | -50.1299 | 2026-09-14 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| bf80dfc2-136b-3a6d-90b9-314e0f765437 | -10.6827 | -54.1679 | 2026-09-14 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 0f130390-0918-3dab-ad07-d150b11e4a9a | -10.6829 | -54.1475 | 2026-09-14 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 4da3cf7a-f411-3ef0-af48-271ddac1cadd | -14.205 | -47.4039 | 2026-09-14 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d38f4a9d-fb21-3389-a859-fe8f82bb13ee | -8.6194 | -44.4357 | 2026-09-14 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 341.6 |
| cf6b3124-d2b3-3d4a-9fe6-7bbc0dd15e80 | -6.6767 | -58.7105 | 2026-09-14 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 356a10df-b465-31f2-8f8c-f41c46e71f5c | -8.8081 | -45.8753 | 2026-09-14 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.8 |
| a568b24a-4ddd-3483-9c00-d0ebbf07d61d | -15.5768 | -48.792 | 2026-09-14 12:50:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 527cd260-e417-3b2e-aff8-ad33d9db2a5c | -9.4328 | -50.1086 | 2026-09-14 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 8bdfbae1-5196-314c-a718-31c4ff87354b | -15.5763 | -48.8144 | 2026-09-14 12:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 419c46f6-049a-3b41-8417-ceba0ec4ac1d | -9.4936 | -45.4818 | 2026-09-14 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| fb6db97b-a801-3459-b60f-dc3920740e37 | -10.7145 | -47.5374 | 2026-09-14 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| b3ae7e1c-751d-3cd9-bfc4-571e30f52350 | -8.6001 | -44.4609 | 2026-09-14 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5e353d12-2c8b-3491-ba89-a552730366ca | -10.6638 | -54.1696 | 2026-09-14 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| fbf64bc8-d506-3263-b891-2333d3dd59c1 | -13.2867 | -51.3046 | 2026-09-14 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 194.5 |
| e241a9b5-7408-3f26-892b-e0c4983a8fef | -10.6955 | -47.5397 | 2026-09-14 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 1d83299d-02ec-35a8-b2a3-d68cb0559f55 | -10.6958 | -47.5175 | 2026-09-14 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| fd3697b2-5403-3ac8-af68-def95d6aacd5 | -2.9024 | -50.4423 | 2026-09-14 12:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| b12c1747-432b-36ce-9acc-f4c2eb782456 | -9.4513 | -50.1282 | 2026-09-14 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 37d85a16-1114-38e1-8c7c-aed6b15203f1 | -2.921 | -50.3999 | 2026-09-14 12:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| b149569f-d73e-3445-84fa-352d489c5000 | -7.0164 | -44.6413 | 2026-09-14 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| eda95aba-5579-39f0-9197-ea02807c3668 | -8.7445 | -46.4213 | 2026-09-14 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| aa017f7f-5d83-3f77-bfab-4861a62f8045 | -2.9025 | -50.4214 | 2026-09-14 12:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 266.8 |
| f5f82c65-15ea-308c-9d9d-8a35d8226285 | -5.1439 | -55.9543 | 2026-09-14 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 5578efdf-e20a-3d06-8765-70d64ea87215 | -15.5572 | -48.7953 | 2026-09-14 12:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 27ff1408-2c90-3687-b6da-42e9196535a7 | -7.2295 | -47.5569 | 2026-09-14 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 4ef0da44-c44b-3d9c-894d-2ead7f6a67f9 | -8.7634 | -46.4194 | 2026-09-14 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 068bbc17-3fa3-3649-a666-5b7a46c8aa17 | -13.3059 | -51.3022 | 2026-09-14 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 178.0 |
| faa4f18b-4382-3f06-bbdc-56e1ebde5101 | -9.4139 | -50.1103 | 2026-09-14 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |


[Clique aqui para ver as próximas entradas](README68.md)
