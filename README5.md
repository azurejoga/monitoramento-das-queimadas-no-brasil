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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4db64f7-4497-3a8a-a8ef-2141868e8366 | 3.31921 | -61.23526 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41429cfc-e7d5-3a0e-802c-15a06fcd022a | 2.57575 | -60.5461 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7db00545-e4b1-39c3-acc6-23d318155846 | 2.08151 | -60.5338 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12e0b823-f606-39a8-9f97-1bc3342ff416 | 3.32658 | -61.23401 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbff7d3c-968c-3b7c-9ddd-fc14767b9d43 | 2.20065 | -60.80667 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c797b9c3-4c28-3215-98f4-3676ca14fd40 | 3.23084 | -61.20468 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc3591a7-e008-340c-b95b-2289f9c319ce | 3.88576 | -61.84378 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 180c1e7b-3665-3d33-b2f0-cfee681de670 | 3.33046 | -61.21093 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8d1cfa8-f295-3fbe-b6d6-8570a6495a48 | 2.57652 | -60.55092 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01346056-3056-3fb8-ba20-3f32642b00d2 | 3.878 | -61.84095 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fc6c258-15f9-31ad-b6dc-a187fef36f08 | 2.37587 | -60.96606 | 2026-04-13 05:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40c892e6-bf62-3e38-8c13-71f2e5ef60fd | 2.19755 | -60.81198 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 528c02ec-52a4-36a4-bc71-68791e08c947 | 3.88221 | -61.84436 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22def55a-fdea-310c-bb2f-47edec75c6e7 | 3.31182 | -61.23639 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d12930c3-ed67-38f8-b3d3-492b00a0b612 | 3.23382 | -61.19974 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddf50d4e-04ec-39f1-a9de-047f71095013 | 3.33325 | -61.2284 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88889d20-2999-3762-b75b-980ab817ef33 | 3.23258 | -61.20222 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b243cd4c-2dd2-3383-b770-8feea3abdeec | 2.52383 | -61.67379 | 2026-04-13 05:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf50b861-941f-3d4a-a8dd-5908d23d730b | 3.24145 | -60.17813 | 2026-04-13 05:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e7942cd-ad4d-3724-a246-00941f5cf7ce | 3.31482 | -61.23149 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3268e007-b719-3dd2-b9da-10ff4b03c610 | 3.27309 | -61.18447 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe5e6af3-61c3-3e4c-b1fe-3520593abf43 | 3.87735 | -61.83698 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a08a322-7ed4-3fb1-b873-71dfc6cfff37 | 2.38683 | -61.77161 | 2026-04-13 05:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0338a351-7b3d-35a9-bb66-7876ac57f5e2 | 2.17361 | -60.70156 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b369c0-c365-3ad4-bc50-5fc825f27e7b | 2.1744 | -60.70633 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67b34593-9ebf-3875-bd49-bf9f4c97b0c9 | 1.83436 | -60.73961 | 2026-04-13 05:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c796b2b-d2b8-390b-81ac-33235a2cc971 | 1.95353 | -60.65619 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e9d9415-bd81-3681-a341-fafb5652d5eb | 3.33026 | -61.23338 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e0541c9-9cfb-3653-b29a-7b07db2bb451 | 3.88155 | -61.84038 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 493204ce-0a38-3687-a876-569b8d946bb8 | 2.37892 | -60.96084 | 2026-04-13 05:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5643b29c-e927-363e-8a1a-8db281021f2d | 2.35511 | -60.44079 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5cf9e35-3d03-3d99-a7f3-86fcab40c206 | 3.2738 | -61.18884 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d3c0ece-283c-335d-abe1-53766742e9f8 | 3.32589 | -61.2297 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adb13800-0b93-33f9-ae36-ae20533c8ed4 | 2.02558 | -61.09429 | 2026-04-13 05:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c2898c3-2221-3f1d-8f0c-a32777ea1a06 | 3.32957 | -61.22906 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f641fd8-d38c-336f-b99c-1cca12391d0d | 3.23628 | -61.20162 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2acd1a6-bb64-31b8-a189-4c592678487c | 2.19934 | -60.80972 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4101ad8d-8f0b-3d1c-949f-01bb7cef2f8e | 2.01802 | -61.0939 | 2026-04-13 05:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdafeb0c-a466-3498-ba13-25ccbf6d05e1 | 3.31551 | -61.23582 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a162dc7-def2-38d4-a1f2-b2240e1600ee | 2.20011 | -60.81439 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3ba79b5-d693-398b-b4fc-19b739035e67 | 2.37512 | -60.96144 | 2026-04-13 05:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09f73ed8-d5b3-34ef-85c9-939b4e99d60d | 3.23752 | -61.19914 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef494867-8e65-33e3-8022-064bd4a2268a | 2.37914 | -60.19243 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5e41e9a-502b-33d4-b2be-b3e354b75fa5 | 2.20139 | -60.81136 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53b68b90-9bf9-3b04-83d2-b455b325a38c | 3.88265 | -61.84302 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75f7ee57-3dfe-368f-8e5d-bdb4ed7f6e9c | 1.95257 | -60.65422 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ca5b212-a17f-3b02-886a-31b5c88257ee | 1.65201 | -60.14397 | 2026-04-13 05:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7f79ce5-bf5d-3196-9009-2ac5dc8af3cc | 2.38345 | -60.96483 | 2026-04-13 05:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce9b615e-dcef-3b80-9018-ece57eac8b44 | 3.87866 | -61.84492 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d06b405-982a-3835-961d-29e154dc3b4a | 3.23328 | -61.20657 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2569a527-977b-328e-9f2d-1855b526485c | 3.23824 | -61.20351 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36b00e70-34de-384c-8ad7-3a5dccdb3163 | 2.0218 | -61.09489 | 2026-04-13 05:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a5f3bee-de75-3b48-a1ec-e18b568db932 | 3.8791 | -61.84359 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a92c925-497d-3a4e-a902-cc56245c7d69 | 3.32289 | -61.23465 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b47ea81-ef9f-38bb-95fd-228d19dac77b | 3.88201 | -61.83904 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce70f6c2-2c4c-3258-9cf4-8b70b1a64464 | 2.17253 | -60.70361 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45f12d98-01cd-34ec-a26f-a98337580177 | 3.31112 | -61.23206 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 032b3e79-8344-3064-9919-00b9861b3129 | 2.52747 | -61.67321 | 2026-04-13 05:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd3e071d-83d0-3d47-b58c-179a5e748910 | 1.1028 | -60.5414 | 2026-04-13 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 3ee727db-c8c5-3b51-863d-3a619873d48a | 1.1028 | -60.5225 | 2026-04-13 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 436cc6ba-cd7b-3890-90f0-b5fc299c6c28 | 1.10273 | -60.54509 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8995252-9234-3347-ae78-b2a0afa8904a | 1.10726 | -60.53508 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e31370ce-cf11-3ac0-b87b-48996cab0210 | 1.11255 | -60.5296 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 28f43282-b42c-33ef-b419-a70648e5bda8 | 1.1003 | -60.53851 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf0c905e-d416-32be-84f1-283f12d9bf7c | 1.10562 | -60.533 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bdbc0815-3c10-327e-a3f9-11ce49b7a448 | 1.10802 | -60.53959 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e73f2065-c75f-3956-b493-2150fb41544f | 3.31852 | -61.23769 | 2026-04-13 06:14:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 788fada2-d80d-38ef-b548-8689de300052 | 1.10417 | -60.52393 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 344c541a-66f8-31a2-bac0-93d18d6ca949 | 1.10948 | -60.51832 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbc7af06-4b5c-3614-bb80-21e25bfa6d16 | 1.10197 | -60.54056 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95913f81-79ff-321d-a7ab-fd19e5cfde1a | 1.09957 | -60.53397 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 961e79cd-b34b-393d-be83-53a1edb1e0b7 | 2.37737 | -60.9633 | 2026-04-13 06:14:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98ce2f8b-713a-3f4e-8907-da463afd33b1 | 1.11311 | -60.54105 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 276165ea-0ccb-3680-bc98-eae23ba06ea3 | 1.11771 | -60.53099 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 324111e8-fdf8-3d16-80e9-e6f5a40ec72e | 2.37654 | -60.96306 | 2026-04-13 06:14:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8fce4801-24f3-3b37-a5ba-b8a207029e68 | 1.11021 | -60.52288 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b875e120-e8a5-3a2f-96f0-3cd0009671de | 1.11026 | -60.51588 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 61ce6090-0ddf-31f9-a46c-813fb29452a4 | 1.1133 | -60.5341 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e4ac4d83-66c0-3a14-a6ed-0900955c1e7f | 2.1736 | -60.70626 | 2026-04-13 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4664952f-b7b1-3b0d-9078-9b15ac971092 | 3.3179 | -61.23402 | 2026-04-13 06:14:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbdcbf8e-fdab-3bc4-a3cd-5932332dee33 | 1.11094 | -60.52748 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8d811be2-7e7b-3b3f-b86d-d0345345d6a1 | 1.10045 | -60.5315 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c5e65a7-32a5-37e2-9486-f4b8cfaabc6c | 1.09969 | -60.52697 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c28cffe6-e462-37e0-9e0f-8bd83b47f9b5 | 1.09368 | -60.4973 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 31b9ab2f-57ef-3cfe-bfb7-74b9b9ec8401 | 1.10121 | -60.53603 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a3a8238-fe78-3ef5-8c5b-5400209a7dd6 | 3.31229 | -61.23483 | 2026-04-13 06:14:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f29af91-1b7e-344e-96fa-686e5f21b5ed | 3.23917 | -61.20091 | 2026-04-13 06:14:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c20efcb1-ab05-35c0-8db9-b6a71e8a2c1b | 1.10123 | -60.50558 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc1c1960-85fb-31fa-9ddd-604bbfa4d2ac | 3.31166 | -61.23112 | 2026-04-13 06:14:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4aa4e0b2-6bd1-38cb-ab4e-f8a64c1d7bc5 | 2.1729 | -60.70205 | 2026-04-13 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54198b69-32f6-3679-b73e-ff2fdee0da50 | 1.11179 | -60.52501 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4290bcac-f2fa-3650-bb6f-bcee8d09bc9d | 1.10344 | -60.51937 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d6d83df-5b9d-362b-af09-6f24dd272214 | 1.10498 | -60.52149 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| df15fa34-bc19-31f9-b725-17b90c6f95d5 | 1.09892 | -60.52241 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 98bf1f6e-b115-31c2-9c18-28dbbc9f7a42 | 1.1049 | -60.52846 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 45d51060-500f-3ec7-9c6f-8d19863f1043 | 1.10574 | -60.52602 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d303b0ef-4241-3550-83ce-10e8b5294bf1 | 1.10422 | -60.51694 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4258f89a-df62-37f8-9d91-43ddf46de9ef | 1.10271 | -60.51479 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ebb65886-d9a4-357d-bf0d-071e3845ff8a | 1.11405 | -60.53858 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3b7cce80-19ea-3c9b-a0f8-fe208e9df2df | 1.10103 | -60.54305 | 2026-04-13 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README6.md)
