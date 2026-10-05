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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9866f379-dc46-3059-8f23-a4c5a9cd9af1 | -3.12398 | -53.75625 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e01b0011-4904-379d-a524-975877b7b254 | -3.87469 | -55.81103 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ec09fe1-d528-3f75-94d1-2cd1e7e40f98 | -3.30952 | -53.85039 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28a7f1a7-ab50-3ee3-8447-fd0381847edc | -3.13049 | -53.71084 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e8b86389-bcf7-3fee-b05d-807007efd147 | -3.87363 | -55.80658 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1125b3ed-1aa6-357b-b146-fb343882d11b | -3.11128 | -53.75885 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d0d424be-7773-3d04-9a9f-d9a661388c5d | -6.21438 | -52.68943 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f7207ef9-2df1-3308-a5d2-48ca0630265d | -2.94465 | -54.1435 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1048f4e5-e928-38c1-85ec-f6c2eb085bbc | -2.94164 | -54.20321 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56a12911-5e5e-3695-8d6f-ba1f73a7d7c1 | -1.61755 | -55.14174 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5de946d-6819-3f0f-81ad-fec6335e6327 | -2.817 | -54.12202 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92409a90-fd15-35bd-b56b-67f77599c98c | -6.20731 | -52.79216 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c671eb7b-28ce-33b3-b5e2-db026f1fc216 | -3.46046 | -54.59603 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 67f0c067-e2fa-34d2-a4b2-e897ca7c596f | -3.8854 | -55.81227 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2cd51b4-bb61-3235-a96c-51fb022b2f65 | -3.61408 | -54.59919 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5722a0b8-278f-3664-b428-00a2b10df58e | -3.86206 | -55.82277 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9589e271-2f80-3aa8-93f9-d24356ce00c2 | -3.37282 | -54.10088 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d197cb9-692c-3aa1-9d06-9910eb84738f | -3.51646 | -54.62467 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d778e43c-10e2-31ec-9efa-6fa32fb728b6 | -3.05972 | -54.16179 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e0f3932-2829-36b2-9f8c-f650bd2c7bee | -4.05947 | -54.31563 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5451910c-f081-3ffe-8116-1c3aa00e4c62 | -3.11257 | -53.74979 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 951a304d-81aa-30fb-9742-41bb80d120ac | -3.11716 | -53.70753 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d35fea4a-0641-3afb-897d-787b3fe26cf0 | -3.07674 | -54.16858 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 509a6d46-2334-3b4b-a8f9-d9f86e7f6e47 | -3.12857 | -53.71393 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 66a81dad-2ba8-3604-b089-66477d57db87 | -3.10304 | -53.71922 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3a54ada5-ed90-36be-abf7-8973d156d713 | -3.10841 | -53.72469 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0892918c-79e4-3c04-be6b-e13432413cc4 | -3.98602 | -55.82066 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d66e1985-4a8f-389f-b56c-faff93b68e8b | -3.12584 | -53.73206 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d57934c0-66ff-3dce-acaf-ea6c1c61b819 | -2.5878 | -51.85469 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 043a7ea9-dbe8-3f3b-a711-e7947798d36d | -3.65595 | -55.50278 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 258fa3e3-b8af-3255-b5c3-0d7b7010f669 | -3.50783 | -54.60272 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dad10ee6-1c40-3e7c-830f-c6e00f8b85f9 | -3.50637 | -54.60318 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7653f6b4-e8b3-3a91-a5c5-c70638a92b00 | -2.97997 | -54.09996 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eff30dec-82e3-3cdb-87a2-3d406df66743 | -1.5198 | -54.82498 | 2026-10-05 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d3c75831-a017-39a4-a876-5149f2833f90 | -2.81826 | -54.11358 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec8fa587-43f5-3750-b90b-85b58e0a7872 | -3.97971 | -59.33942 | 2026-10-05 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21e258bc-b785-3ad0-b6c7-318a94199f94 | -2.99481 | -51.04622 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be59da9e-1385-3bfa-94a7-06325f42a2b8 | -2.98648 | -54.09658 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72dacf57-be17-3791-ba52-594a58b68694 | -2.90882 | -54.14238 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0de61ba6-0071-387c-a2f5-3de3d6efb31a | -2.77907 | -54.09441 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 763f3d73-a52d-3754-9d1c-d0b1208c8390 | -6.21752 | -52.68904 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4d3b0a88-2596-3ba0-a0af-f17c795fc71b | -3.1238 | -53.74559 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6824d9df-ee1f-3fa2-9a7a-d2f41c675990 | -4.46038 | -54.96167 | 2026-10-05 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa45ebbf-eaf2-3079-b398-d04513ab9d1f | -2.22384 | -53.71671 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8f033acb-b7ca-3fe2-ae6d-d826d679bbe3 | -2.8059 | -54.11602 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 201790fa-4332-3dbf-b99e-015f70925c2c | -2.78308 | -54.10796 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b7b22d2-4734-347f-8be7-4c875e1bcb7f | -3.10435 | -53.75185 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b56ad38b-9747-3ea0-8433-fd7c82e32536 | -3.11971 | -53.69974 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3f1a2818-5b6a-37fb-9397-0a45ee7cef8f | -3.0872 | -54.17924 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 15aa847d-c1c2-3fc5-b9c6-28b2567394a7 | -3.10654 | -53.74885 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 869089b5-b060-3a44-ac49-fc468cca75d7 | -3.0585 | -54.17025 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d3ce0cdc-5fd7-3896-bf69-5cf8a44d59ce | -2.99112 | -54.10608 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9a204331-d7f5-3396-8c3b-35e027625bbe | -3.05104 | -54.22775 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 313565b2-5196-3c19-8f13-49c54972e44d | -3.11301 | -53.70337 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 70ff202f-0edf-3ac0-a81d-775ff9ef77f4 | -2.81114 | -54.12113 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d2afdaa-7c02-349e-ba82-ec67f4bc4262 | -3.51185 | -54.61581 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6a4c85c-15f9-302f-814e-185669dec23e | -3.33365 | -53.39086 | 2026-10-05 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d6e3f48d-329f-34ab-b6bb-08b290594010 | -3.12448 | -53.74109 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a96c270-1d58-3630-b02a-e6e8419895b0 | -3.86689 | -55.82693 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5de81440-272c-3cfb-bef2-da0cebff9d50 | -3.48741 | -59.72918 | 2026-10-05 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 352beb9c-a487-3e0d-a849-efd35d56dc12 | -3.31486 | -53.8558 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 178223f5-a987-3c65-83a6-799a0f8be3e6 | -1.88124 | -56.28409 | 2026-10-05 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fd4b04ac-fde8-3381-96c0-8d1c6ae04209 | -1.74638 | -55.23728 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82c2d0d0-0513-34c3-bee4-afe8f6c80530 | -2.90057 | -54.07607 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37bf1764-8df9-309b-b591-8cd43ef8941f | -3.50577 | -54.60725 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92465cbe-d5b7-3128-b32a-60951d3d09dc | -3.04457 | -54.23099 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e208a23-724b-3678-923a-6900ebd56aee | -3.47256 | -54.59355 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 13f22550-7b81-37e2-91fd-4e6af697eb80 | -3.05526 | -54.23441 | 2026-10-05 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2603c62c-1988-3c93-9c62-59a3016db5bb | -2.90357 | -54.13726 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e24cb236-1ca5-3de0-87c0-a4b46c94066b | -2.99383 | -51.05309 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfff73e1-c26f-3ddf-b7c9-0d69519a477c | -3.87801 | -55.81416 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 595b2e4d-7706-3512-8b20-fe52d23492e0 | -3.30485 | -53.84047 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1796911b-9b78-3369-a653-ec75c1a53f06 | -2.90295 | -54.14147 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc31cc3f-eba4-3935-b1fd-8291fe0d1d0b | -3.05041 | -54.2319 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1086d67e-c5a1-3101-be8a-6609d68b4641 | -3.05183 | -54.21672 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 215b8974-6fa6-348e-b978-f9a05b5e89d6 | -2.94069 | -54.12994 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d91a875a-fcc8-37e3-a186-eda41882980e | -3.11037 | -53.75279 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 970f51b5-e7f0-3285-84e5-d084fc4d40cf | -3.98494 | -55.81739 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2099bb36-7250-355b-844a-64190b880645 | -3.05062 | -54.22515 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5773b8c9-50d6-3e79-9ca4-f427a2b66fa4 | -3.08134 | -54.17828 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| d1206a85-cf68-336e-89ba-193cc79f37b8 | -3.57738 | -55.41959 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12a35a83-d8cd-3b16-8a93-ee1c836a9c91 | -3.32679 | -53.39449 | 2026-10-05 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faf64cfc-023b-3e2d-97d9-f42b7c495b4a | -7.33258 | -55.03481 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93187692-90e6-32df-9d74-22d0dae9a1fd | -1.20637 | -55.86183 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47a4d134-6157-3130-af98-0163bf92ff29 | -3.46161 | -54.58808 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 43f11fec-e12a-3173-860a-18392ea09a17 | -3.46103 | -54.59207 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a347ed58-f0e4-3c98-a691-f8f5ee8e6748 | -2.85397 | -51.29808 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 07b8e7d6-1dd3-3f73-ae5a-253cdc7b9637 | -2.48709 | -56.10766 | 2026-10-05 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 36fbc780-f155-32eb-971a-0833d9fbf1b6 | -2.94976 | -54.14269 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 67d48ffe-825c-3a87-b56f-59359f06b6a4 | -3.31779 | -53.85041 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28d311c0-9e29-374e-834c-cd009fe3dbd1 | -2.93544 | -54.12487 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32ebc53f-e724-38d3-866e-960e2abab6fe | -3.12243 | -53.75467 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 36a9816a-e8fb-359d-9eac-558ddc5d3cfd | -2.82089 | -54.12842 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22b082b0-8b04-3ac8-bb02-47f545ec11d6 | -3.11648 | -53.71208 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 36fe9790-12e1-344d-8a11-3a3b81b2fe63 | -7.32615 | -55.03803 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74dd45fd-39f4-3289-a40e-f0ccff650189 | -7.3267 | -55.03384 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52f717c8-6cd9-3942-9a43-44c7fdf2ccee | -3.59614 | -54.31491 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fe7ca6c-1396-38fe-9adc-94118e6dc711 | -3.97495 | -59.34261 | 2026-10-05 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 790b5255-a549-34b5-8ce4-b17ee50f60f5 | -3.10373 | -53.72517 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8c8dda43-dfd7-3a75-8468-dc4fbe6b067c | -3.37615 | -54.10655 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README55.md)
