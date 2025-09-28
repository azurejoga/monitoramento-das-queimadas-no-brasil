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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57b71747-bf2d-376b-8e3d-5b588df5d8c3 | -12.00008 | -46.61929 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7aba2b05-5af6-385c-a48f-6f99391a71a7 | -10.11458 | -45.35014 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ffb2eb3-283e-3c49-867c-88d016cdb66e | -5.82109 | -44.44156 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba93fa00-bb91-38e7-89a5-f6f117e0a199 | -7.8089 | -47.01561 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d38f7b3d-684a-3f3a-8ccc-ed8e0140be49 | -5.94324 | -42.90038 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0eb1e754-f892-3fa8-ac93-047263da74a5 | -5.8768 | -43.19709 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| be653ef6-7295-3bf9-bcb7-0da2f2c7a118 | -10.96912 | -49.56612 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4debfea1-2c57-35d2-b6d8-912c3502d7ec | -6.48306 | -44.50808 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52d33bfb-3c9f-3a4f-89c7-eb3eab9dae69 | -7.22528 | -44.75901 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 309a6b0a-d417-391b-8284-c8451d427062 | -7.63201 | -43.80367 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9cd9c794-a4ad-3da1-82f6-b7bc7f569cce | -7.25528 | -42.99427 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8b824f28-0fb8-3f73-9557-21a4f1729855 | -9.40732 | -54.69989 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63da0f9a-46a4-35c8-9e85-a678d57974f1 | -12.84981 | -46.89663 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c8479cf-6fc7-3be6-971d-e57af0722c77 | -6.95312 | -45.39418 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bafcf2f4-7683-3745-ac58-576e4507933a | -5.89593 | -42.81428 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3c00715b-58e9-3856-b64b-d574697724d2 | -9.12105 | -45.88372 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb2dc172-2761-3e8e-8a94-5a693fccdd5c | -11.99164 | -47.04622 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1ff249f-38d5-33e9-b307-7ae537d8a901 | -7.23093 | -44.76735 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a114fc9e-f52b-3118-981d-7f5e13af1354 | -6.49646 | -44.12755 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 630cb798-9d38-3b1e-b709-995e2085234a | -12.89335 | -45.17367 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f2e996ea-26c2-3081-8acb-45943b9af8d2 | -11.09806 | -54.27874 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4012c11-e458-351b-9e58-5f5eeb16fd8e | -8.1678 | -46.42118 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f6d98686-27f8-3f97-b878-53203649cbe5 | -10.13263 | -45.32277 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce32b642-4e51-36d1-b04f-36230aa8d686 | -7.04134 | -44.76829 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23564431-3b43-3e49-a363-30fc29a4360c | -6.40501 | -42.90918 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9b9d091d-c796-390d-816d-5eaf19620ba9 | -11.36475 | -44.9636 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27542a39-270a-3ed8-844f-3329d0b00e19 | -5.82954 | -44.43174 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62deaec5-2097-354b-a57a-9f4ade61a036 | -5.90996 | -42.93999 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec873cb7-cce7-3a9b-a1f1-9644a38ea670 | -10.01198 | -46.7009 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19ef87f3-3744-3bf9-bf52-145c568acf8c | -11.70489 | -44.41784 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a76a809-6085-31cf-9106-20939bbe490d | -12.00624 | -47.94338 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0a0f96d-30b8-3f36-a9b2-dea08464addc | -11.94958 | -47.91617 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4319f90b-98b0-33cb-8ee1-c1352fc8831a | -9.10259 | -45.82648 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9452bae-3eac-3705-a032-dee18eb013e8 | -6.27437 | -43.62866 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ee9eb6d-5528-3eb3-87d4-c50fd57ab3a2 | -6.14999 | -47.2984 | 2025-09-28 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 475efc4b-cc81-3d3a-805f-6fbdc63176cd | -7.75877 | -45.73917 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 116b3ce0-a6d4-39da-a586-71caf411fda7 | -7.23489 | -44.76422 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01512a55-a5a6-31ed-9a38-846fe6ed8613 | -10.17 | -49.37343 | 2025-09-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff87438f-ff72-38bd-81b3-5b7fa8fb0ad1 | -10.96782 | -49.5739 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29768488-71fe-3b6f-923d-b68717c24570 | -8.17275 | -46.4113 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fc87f017-1718-33e7-879e-198d8f26e51b | -6.30919 | -41.9201 | 2025-09-28 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e2f1a09b-c05b-303a-bf96-054bf7b1e90f | -9.07599 | -47.59268 | 2025-09-28 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92abf310-c473-3b99-bd94-5866ffea6f45 | -10.58184 | -46.26857 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03d5548e-2dc1-36e9-b0e6-5ff49cfa7e68 | -12.10587 | -44.20124 | 2025-09-28 04:25:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13289a37-59f0-3132-b8f4-9fb2cfca4a4d | -6.55 | -43.81492 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf88a973-f864-3137-b7ff-850fbbb933eb | -6.15194 | -42.80154 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4cb75171-c67e-32fa-bd73-f6f77ebbbd31 | -12.01737 | -47.91626 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36d9006f-4006-3e3b-8e0b-a2acaa49e724 | -8.43668 | -46.87017 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af15460b-dd14-388e-9834-050b168d60c6 | -11.68938 | -44.42394 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fa2b210-ce05-3905-ab0e-a22afa8ccae9 | -5.62816 | -44.92136 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07d8cc5a-99a4-38f8-b385-5d2a65728d2c | -7.3737 | -47.03905 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e3c368b-3353-3f47-8d8d-d239de406a28 | -7.71419 | -41.28813 | 2025-09-28 04:25:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d660bb63-b26b-3356-b614-204b7008b5d6 | -6.23807 | -44.48595 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf8ebb78-4af1-3e82-b83f-6eda745bb257 | -7.25958 | -42.9905 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0474061b-47f2-3981-9bac-d2f7d78805e3 | -6.6817 | -44.60557 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8442c827-05b3-3313-b14c-fa0d4cbf808a | -7.74275 | -47.00507 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad2b2202-c29d-34c8-aad6-4eb975908ea9 | -8.83707 | -46.2026 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 935381fe-8007-3fa6-9861-834966e36d04 | -7.58341 | -42.32112 | 2025-09-28 04:25:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 327d4512-1062-34ce-92d6-6bf7072ebdb7 | -8.82109 | -45.97731 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab09cff8-8ab7-371b-9323-422fdb3039c9 | -12.14342 | -47.29105 | 2025-09-28 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 055fe666-a3fe-3123-b9e6-77adb443e3da | -7.86678 | -44.57198 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68a75c8e-e40a-3bd7-a74e-45715dcbaac0 | -11.26143 | -48.3754 | 2025-09-28 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7187e9f8-0f2d-3bc2-802d-f3362d088fae | -9.1205 | -45.88724 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e733ae5b-d12c-3ed4-8918-baddc63609de | -11.9607 | -47.88904 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f06ceb8-2828-36ef-a2ad-d714deefca21 | -6.27025 | -43.6322 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98b542f4-9f24-38f6-a3b6-03c558ea12f9 | -7.82375 | -45.14635 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27b048f0-4015-3a0b-852e-468ca293a081 | -10.92181 | -45.7283 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14268b7d-e062-3ae7-bab4-33a7163da865 | -11.36128 | -44.96304 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01f35b59-418a-366e-bbc8-267b34f741b6 | -10.04668 | -49.20285 | 2025-09-28 04:25:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 731cd7ca-63c6-3b89-b557-93a58d2ab232 | -8.08086 | -47.8702 | 2025-09-28 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e402a600-b5a0-342c-8236-2c9e3f08f7d3 | -9.08989 | -45.86433 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2656e5b3-cf19-3d00-b2c5-507e02b2a050 | -11.81039 | -48.2346 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b08750d-f595-33e9-8180-ea7388d06c68 | -11.10459 | -49.23896 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7428403f-8d7b-35b5-bfc7-55b23e930eda | -6.15128 | -42.80578 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e51d63e7-2ac7-348d-9dcf-26f92ed03759 | -8.48961 | -47.81819 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1fb4ccc-1b9d-36d0-8bad-fba095346502 | -7.79455 | -46.99902 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9b3a9e2a-a08c-3d30-a09b-dd1434c6895a | -7.86564 | -44.57946 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ede1074b-eaf2-39c7-a64a-896460086c6c | -12.9419 | -45.11198 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3dee1198-dbc6-379f-a795-8d15d7c14a90 | -11.43767 | -44.99913 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd6d23d2-78eb-3490-b250-da399cbfc65d | -8.64864 | -44.86048 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fbc5625a-313c-3248-9bcf-ca304b0d75c2 | -8.21697 | -47.03446 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27e96e48-e524-33d5-a5d6-48f473702292 | -10.90869 | -44.8181 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7db56f97-7eed-3660-8da4-a5e6c30c035b | -11.95458 | -47.90613 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1d29b5f-6f4f-33f0-8139-2f3fc3b67dd4 | -5.63764 | -44.92648 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f573ec9b-1557-34e6-8a70-bfeca0b35c9e | -8.17442 | -46.42223 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 468706ea-9a8b-3e5c-bb23-de7b17d7ea13 | -6.55234 | -43.8231 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92cd1f66-86a4-396f-97c8-1462d877845e | -11.37806 | -44.96984 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79784b25-62fb-35f9-9093-f1fbabc70bb7 | -7.6323 | -43.80273 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d3753af-4594-30e6-ab4b-9d425aa8fffc | -7.38145 | -47.03313 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d8957bf5-6deb-329f-86fc-76608fba636b | -11.97617 | -48.00367 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaafa133-3833-3815-8897-4b3aa4fdd8ee | -6.28856 | -39.82621 | 2025-09-28 04:25:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9b07c3f-36db-3897-bfa0-d87b65cb8ba2 | -7.79123 | -46.99849 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8839e757-04c1-34c7-a18e-8e1d2cb02cbc | -5.99561 | -45.80824 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d090aa9c-d845-3d7a-9ad0-0a9ad5342849 | -6.48363 | -44.50439 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7abfccc9-7c61-38dd-89f2-fc7d9378a421 | -5.79624 | -43.41891 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ea5a39d-5cd0-341d-b453-c59e2d762fdb | -11.36193 | -44.94828 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 314b0271-ac55-3c92-9712-e9c516dc4fe5 | -11.38671 | -46.98533 | 2025-09-28 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ed8a8cb-3c51-3d02-a036-b3b539e9f94d | -12.95116 | -45.14597 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbe8da38-5c66-3636-a90b-6ba326580143 | -12.00601 | -47.0413 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de41361c-a5ce-3382-9f93-4b4f39e4f9c1 | -7.74274 | -47.02653 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README58.md)
