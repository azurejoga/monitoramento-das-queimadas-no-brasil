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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fad9b28-12e7-33d7-9214-93a1ac93c5f7 | -7.2471 | -45.8685 | 2026-08-28 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3aca43ba-4558-3262-b86a-1603573b9636 | -6.1472 | -57.7995 | 2026-08-28 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| fa05abd1-c122-3ff0-a00b-e33fd283a86c | -14.8825 | -52.5868 | 2026-08-28 03:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| fbd9b73b-2e01-36b2-a4fb-b18f8dfa1dac | -16.1641 | -58.5851 | 2026-08-28 04:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 271.6 |
| 6dca0d51-27bb-34f3-8fda-9aabb2da6ee4 | -7.2474 | -45.846 | 2026-08-28 04:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 89b21844-b262-3e18-822e-9f5674a09ec1 | -16.1644 | -58.565 | 2026-08-28 04:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 79b2c125-826c-3c32-a2ae-bd12c21a5418 | -16.1444 | -58.6073 | 2026-08-28 04:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| d337bc06-9d4b-38cb-a5ff-ceacf23e78bc | -7.2659 | -45.8668 | 2026-08-28 04:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 6f54aa72-3284-3002-b47e-59ab9b6ba552 | -16.1638 | -58.6053 | 2026-08-28 04:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 89d578ce-e20c-327b-8837-453e5e2e2864 | -16.1447 | -58.5871 | 2026-08-28 04:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.2 |
| 27d3a499-a8b1-3a69-be90-c1a43ed28430 | -6.1656 | -57.7988 | 2026-08-28 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 09ee44cc-6128-35a4-a6a1-16e399ac7061 | -4.8583 | -45.3915 | 2026-08-28 04:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0433fef8-5beb-3065-bd09-cc7d0b0e0f54 | -7.2471 | -45.8685 | 2026-08-28 04:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 52e9eb56-c808-355f-a6a5-af6700ca7590 | -6.1656 | -57.7988 | 2026-08-28 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| b541fa87-2841-351e-bdf3-3a9565c3ff57 | -7.2661 | -45.8443 | 2026-08-28 04:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 22a9da82-5f77-3fe8-8418-b33983c39c3b | -16.1444 | -58.6073 | 2026-08-28 04:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 6de0c228-57b2-3f12-8837-c533e4720b7b | -11.1919 | -51.2496 | 2026-08-28 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a8eb816e-0773-32c8-b6c6-30414204ea8e | -16.1641 | -58.5851 | 2026-08-28 04:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 226.7 |
| 9b211e49-a52e-36e3-a51c-5cd7d1805c85 | -7.2474 | -45.846 | 2026-08-28 04:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 837ecd68-1255-35a1-9b70-b44714385144 | -4.8583 | -45.3915 | 2026-08-28 04:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| b9b259f7-2731-3a2c-bd50-3e52f96dd3f1 | -16.1644 | -58.565 | 2026-08-28 04:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| c01df69f-63b6-320f-8df3-6c70eb2ccc38 | -7.2659 | -45.8668 | 2026-08-28 04:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 647ceea4-2cc7-38e8-90f5-f04576f449ce | -4.8397 | -45.3926 | 2026-08-28 04:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 453c6dbe-fb08-3ef8-943b-044c10c9959c | -11.2109 | -51.2476 | 2026-08-28 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 94e75567-4ec2-388d-8fbf-b0a7ac0d26b6 | -11.2111 | -51.2264 | 2026-08-28 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| f1941fec-7926-3a34-b7f8-54eb4963e113 | -16.1447 | -58.5871 | 2026-08-28 04:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 18f1337d-8d1b-34f1-a627-5df6afb74a3d | -7.2471 | -45.8685 | 2026-08-28 04:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| abc6d08d-abd9-39cb-a6b8-bd2afa3074c3 | -16.1638 | -58.6053 | 2026-08-28 04:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 4369f0eb-121a-3421-9748-3e0e58cb5124 | -11.1922 | -51.2284 | 2026-08-28 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 199.6 |
| cf26dcf0-7965-35b8-adaf-b9e9034a62f8 | 2.52172 | -50.85356 | 2026-08-28 04:12:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 014c9ddc-bc74-3fbd-bec0-04946cbd2b87 | 2.5162 | -50.85437 | 2026-08-28 04:12:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4a4b109-8b51-3422-b53c-90ae8b38f7e3 | -7.20952 | -42.75889 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22e9dca4-b007-3abb-9602-a482276a20ba | -7.25583 | -45.85601 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b8457e59-df92-300d-9b1f-b40139059790 | -6.84202 | -45.02694 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a07e36-84b3-3107-98a6-e097941cddd5 | -2.53984 | -43.2627 | 2026-08-28 04:14:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b98208e3-888b-31e8-b09c-5d45d1864d9e | -6.90281 | -44.66933 | 2026-08-28 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0b32764-0de9-3613-918d-842d59db345c | -6.23433 | -53.48277 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f5a1262-d43e-3bd6-90e6-6b19935cf5ad | -1.959 | -48.37846 | 2026-08-28 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28a06fb6-c852-34e3-84a6-fb07e5553c37 | -6.2775 | -53.13868 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8d33e4ba-fd27-33dd-953e-9b841cfb2ccc | -7.44485 | -41.49032 | 2026-08-28 04:14:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f147a6e2-063d-3138-b7c0-ab7f38e5ca2a | -6.75218 | -55.68447 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d3e65ed-9239-34f9-8944-5422aeb68c95 | -5.98919 | -52.19654 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21927ecb-f557-3407-893d-8af33ba37508 | -5.26419 | -50.96819 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 964cbe53-8de9-338d-ac5c-31a07eb103b7 | -8.11367 | -45.82924 | 2026-08-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd817061-dd03-38d9-bf08-b9f1b0eb5e99 | -5.24948 | -38.50634 | 2026-08-28 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e0a3d55b-4a5a-3141-b167-b117dfd0899c | -6.3212 | -54.73718 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8e68736-77d3-36e8-b4a8-e63b2bed1f57 | -4.84372 | -45.39949 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b072e8e9-82ed-3e4e-a655-30d13b706c46 | -7.09981 | -42.19091 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f802199-5cf9-3804-902e-3d9da88c1016 | -7.08381 | -42.82505 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3dfde5ab-583f-3990-91c5-783021a31534 | -2.72147 | -48.79974 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef9d8ba2-1e06-3d87-ac10-e2cdb423b747 | -6.6315 | -53.18582 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e52de92f-3856-3323-a42c-1d8a6143fdfe | -6.14246 | -53.52686 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d3cc367-2627-3042-8a9b-30b6ec6b5986 | -6.89884 | -43.64042 | 2026-08-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 142e2773-3117-3cc0-833b-d41267408985 | -7.27066 | -45.35276 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0a35641-7201-3e61-a058-29e40064cc55 | -9.01808 | -40.99365 | 2026-08-28 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 758f51ac-8fae-308d-9f26-8411b6932f8b | -6.2729 | -53.36328 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4591ad06-6189-3861-8401-9e6ee8369586 | -8.75609 | -44.24592 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56389d90-fd40-3684-9aed-2de14387799e | -6.78717 | -42.76444 | 2026-08-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1d1707c-9f09-36e8-9f86-787f432651e5 | -7.26154 | -45.86491 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2b1cbac5-b9d0-3f91-aeb7-5afb3001fc46 | -6.83773 | -55.62048 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c25a5342-9d6f-321e-98c6-95dca392e859 | -7.24823 | -45.85875 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d8d58ee8-9835-3344-91ae-17e7a9db952b | -6.52348 | -55.25239 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d000230-b1b2-38ac-940e-900656a36316 | -6.53081 | -55.2482 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2006a87a-28c0-30e8-a89e-c9f018333642 | -4.84722 | -45.40005 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 991f58e0-0d2f-3cae-8fc0-8bace08c2974 | -7.15436 | -46.54275 | 2026-08-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf79eb46-e648-31cc-a6fb-a1f7ad136f5e | -5.16465 | -42.74733 | 2026-08-28 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efd64eee-d222-3049-af14-3bb44d07ec8a | -8.08207 | -45.8555 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2ef0e49-d7c1-3527-b191-c2e0ed716e3d | -2.81562 | -48.63487 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 693955bf-b5c5-345d-b287-7ea07f9d85e1 | -5.94283 | -52.36668 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c85f8c73-f409-3b5d-99f1-b608635668ca | -4.93153 | -47.464 | 2026-08-28 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5f81e1f-5cc8-3644-8150-fbada192fcb6 | -7.27126 | -45.34902 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f3a9801-e732-3691-9495-b3f13f134ee1 | -4.8536 | -45.40507 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba0489bd-7bbe-3aa6-bbd9-30a77cb459f1 | -3.46212 | -39.58217 | 2026-08-28 04:14:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0af5910e-426f-30f1-b41e-3ab056c4ccb8 | -4.84497 | -45.3917 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b8d7dd7-acff-3c12-aa96-3dfccc103917 | -7.15168 | -43.198 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9fcd2a38-854f-35b8-a044-678b3d24eb57 | -7.43953 | -43.07308 | 2026-08-28 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 180c9b29-81f9-3474-86e1-c2d880c16f51 | -4.85135 | -45.39669 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| b71325be-9007-385c-8645-695f8ad8eadb | -7.10316 | -42.83162 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d74e5f9-3999-320a-b11e-73dc13390167 | -7.74963 | -44.73494 | 2026-08-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4b0900a-8fa0-32a2-aaec-5f57bf0cd836 | -7.74236 | -44.73745 | 2026-08-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15b7266b-f46a-3ff5-8d06-50676e217654 | -6.28286 | -53.37326 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a63c39dc-d3f3-3731-9480-baebeb371895 | -7.43899 | -43.07655 | 2026-08-28 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1998e95-bb5d-323a-919c-4152b04cffd7 | -8.07844 | -45.81183 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 78f74b2e-9c10-3f95-94c9-3cab6ba15937 | -2.09787 | -48.21843 | 2026-08-28 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4fe3a0c-e5ac-3bc0-8a2f-2cf89ed05d63 | -8.20509 | -42.84975 | 2026-08-28 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4e000d1b-0f64-38ab-a89b-6b234a47a032 | -8.00904 | -48.40644 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc6c6bb8-3e8d-35af-a6cd-8e91f9bae4b0 | -7.0527 | -44.88938 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f104123e-99cd-3fb7-a90b-be1d19814bb6 | -3.53936 | -48.18286 | 2026-08-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb2c2020-ef5d-3ab2-9339-87dfe87f949c | -8.08146 | -45.85932 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08a5c068-67d5-3208-9b01-c31d64214523 | -6.26893 | -53.12196 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d327d44-4b19-3fec-813e-0d760a39f680 | -5.82115 | -46.22294 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b4d71aa-d0ba-33fa-81c1-b9721a90baaa | -5.58268 | -49.03407 | 2026-08-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f717804-edd7-3e39-8d34-c57c07467106 | -2.98405 | -39.89249 | 2026-08-28 04:14:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4c2c03b8-727a-3032-bb79-5feb0677c6e7 | -7.09755 | -42.18327 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 20c0166e-2e42-3c77-bfbe-2e1aad4071b0 | -7.21006 | -42.7554 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 52ce07cf-809b-317a-8018-99acf43fd7c6 | -6.83973 | -55.60991 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3440d0e0-d665-3cbe-9610-c88e3967fb4b | -7.16314 | -43.16788 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d4eebe49-3afb-3326-8341-21643bdb6036 | -6.12311 | -53.53588 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdb82324-6477-3a5f-9361-778a49079074 | -7.35102 | -46.69348 | 2026-08-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40f010fa-1c2c-305a-a0f8-26c9fce0be5c | -1.59391 | -47.35958 | 2026-08-28 04:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README16.md)
