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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39d172f6-6d23-34b2-a3b5-98572c8431d5 | -5.48262 | -45.62174 | 2026-08-28 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f8e7fff-3b85-3292-9cbb-a7db79625c9d | -8.03188 | -48.02533 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bbb3c62-744a-375d-bd32-a23a3375e762 | -7.88124 | -46.0935 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5dea22ae-55a6-326e-acda-d9f034c32170 | -7.0634 | -42.15974 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4b68de3-d87b-36ee-9587-4e4f3dc8829c | -7.38642 | -49.54565 | 2026-08-28 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047742d9-8941-3de8-9c74-e8dfe124e282 | -7.1063 | -42.78934 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 755646e9-a892-3fcc-88e6-f35b9a0fd020 | -7.31649 | -42.96854 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2476810b-9c7b-3be8-b5ab-110c5dcff844 | -6.64449 | -53.18487 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8fb79c6-30b0-32f9-8731-b23b37998d46 | -8.08961 | -45.85275 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62fde152-a360-3640-970d-11b450d15797 | -2.81193 | -48.62997 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05d88975-2d94-38dc-b2ca-8b8940e0cc6c | -8.08189 | -45.81242 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b835a7d-16be-3f45-871b-727d893130d2 | -6.75148 | -55.68627 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f7c9edb-8e09-3b48-894e-e0c46367cb59 | -6.27683 | -53.14246 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8dbfbe40-eb54-30ad-9b48-8ef9c7918c24 | -7.26727 | -49.8531 | 2026-08-28 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a329ee7-7d98-33c1-89cc-506397bb216f | -7.89234 | -46.09143 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92132220-275f-37c7-a9a8-faa4b4e14830 | -6.64263 | -53.1879 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7724a361-d9af-3487-b988-e955b16676a9 | -6.48924 | -53.50233 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a53dc5e-555f-369d-a66f-74f05db32765 | -7.12836 | -42.77849 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4d51a88-56a4-3c60-9ecf-15b68b812e7d | -6.18276 | -45.91531 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4019eb6-f4ba-35d3-8d18-088f0ec30548 | -6.63774 | -53.18313 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20a7e664-c750-3c69-92a7-53f723be9bd3 | -4.84848 | -45.39225 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea436ddf-0ef8-3d34-a071-3855d564231d | -7.3811 | -46.51034 | 2026-08-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71491390-d095-376e-aa60-09dfed41dbc2 | -6.50086 | -53.25848 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92a16a86-54df-3449-917c-498bbd49fb96 | -6.64319 | -53.19233 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5c9e002a-085f-3f2c-9170-2dbf0c1aac0a | -8.05944 | -45.86377 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ddc0400-26f9-37ba-816a-e4592899a93f | -7.31703 | -42.96507 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df2fc3d6-d68c-3624-b065-cf93647d7816 | -2.80757 | -48.6293 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7dea50b-fd41-38d9-8f16-7ea63d008445 | -9.01749 | -40.9977 | 2026-08-28 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2cdcb809-0e7b-3a12-9702-78b427f039d7 | -6.32031 | -54.74213 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47086971-e788-30a6-82a1-bdbd92457758 | -6.06948 | -53.77258 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e92e4d90-3301-382a-a92c-2d490d24cef7 | -6.32206 | -54.73242 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a30a7453-39d6-33d4-a231-fd485cff96f3 | -6.83875 | -55.61507 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f286dc61-b0f5-3204-af02-923816bccbc4 | -7.25868 | -45.86046 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 1936fed6-469e-324a-8494-6a0499035f42 | -1.36 | -54.63467 | 2026-08-28 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a53adf8f-519c-30d8-b8ea-0dcaf17e6be5 | -4.85422 | -45.40116 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1be6096b-1d1c-3e0d-b8d2-d052e0583aab | -6.06366 | -53.77142 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aab5efe-3a5b-3176-8c9b-5a6299eb556c | -6.83808 | -55.61623 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 88217585-b0d7-3b3a-82f3-7cdf30d79456 | -7.26091 | -45.86877 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4c1b0bfa-a07f-3c51-8ec5-5cdcc932287e | -6.28354 | -53.36933 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d81cf240-ba5c-33c7-8263-5c835c28927f | -8.06315 | -45.84077 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b0185a5-eb3b-3208-bd14-f80515a94d2c | -2.50144 | -48.13715 | 2026-08-28 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 65e35095-b19b-3406-9ddd-a2f1cd9f3198 | -5.29203 | -50.93618 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2f911ea-f726-38f7-9f79-9e6a41cb2dd0 | -1.74407 | -47.1248 | 2026-08-28 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bf0f48a-094f-3c7a-a98b-a4ac4c4164c7 | -6.53618 | -55.25471 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f90fa33-fea2-33e7-b8d5-02c01731e997 | -6.12887 | -53.53682 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e0b915-246b-3c91-a107-6585b6325ef1 | -7.3886 | -49.545 | 2026-08-28 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4603418-e800-355a-b30a-7469672a3299 | -7.27164 | -49.85407 | 2026-08-28 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0abf2030-726d-3e94-966e-afbd80dce22e | -6.14343 | -53.52816 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df52f933-945e-399c-bf54-a05c8731585f | -6.9016 | -43.64439 | 2026-08-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21b4a6a5-6e61-3265-a63d-21c83a3fc401 | -5.47503 | -45.12114 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4713576-2dd4-3a11-8baa-b381aaf091a3 | -6.43265 | -41.78093 | 2026-08-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ce8ae1b7-7abd-3246-bd01-1fad542a2159 | -5.86938 | -43.52693 | 2026-08-28 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c472d26-5614-37ce-9fc9-f259f7fec7a7 | -6.22879 | -55.61994 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc02ddab-5eb5-3560-8589-2ec6aa411506 | -5.47564 | -45.11735 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e54e86d-6c67-3644-b8be-e9ddcf8194ad | -7.07119 | -42.15363 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 054e9039-950a-3e38-9bc8-65168dfebe27 | -7.26439 | -45.86934 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| acbe7933-67ca-31ae-826c-51ad10a134a5 | -7.24696 | -45.8665 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 313315a6-6c9e-3445-8895-1511fcb84cd5 | -6.64751 | -53.1927 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fff13891-a5e8-3b47-a294-cd494d4a4800 | -7.2628 | -45.85716 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d4398d58-1c0f-3f73-80e7-417fbc06165f | -6.62227 | -43.73488 | 2026-08-28 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed3bd5a7-8193-351a-8baf-361efba4d4ef | -6.64874 | -53.19344 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f3ccf11-215c-39cb-a5ea-7894a1fb57ba | -5.7746 | -46.16895 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b67157e-6ed1-3107-b39b-c215ec459c6e | -7.2045 | -42.74738 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dfe879ad-2c81-3058-b6b4-2cfbef3fde4f | -6.185 | -45.92384 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1860292e-369f-3c00-b6f3-c1d43c6714a8 | -7.05983 | -43.59114 | 2026-08-28 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58372b1b-3222-3828-97ca-f0518f1a64ee | -8.75664 | -44.24244 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35139eb4-64ce-300e-abed-d440662cdca3 | -7.07261 | -46.26571 | 2026-08-28 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e397b808-dd08-319a-aaa5-ece1580db165 | -6.90214 | -43.64093 | 2026-08-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc42db40-b1ef-3963-b414-fa256b663c99 | -5.34253 | -45.15869 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| eb716ff2-c1a5-3827-a672-2f9d3eaa840d | -7.3481 | -46.68861 | 2026-08-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2dc2943-da51-3919-b044-91c96064d0b0 | -5.81394 | -46.22182 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96669b4f-6618-3ab6-9e17-2694c86030e6 | -6.22785 | -55.62109 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33bc7f9e-9c34-3ba0-bbf3-b1b6ccd96955 | -2.57929 | -44.18652 | 2026-08-28 04:14:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 248c92c6-ff1a-329d-95e1-c034c3fbc3c1 | -3.0638 | -48.74913 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 801b8ecf-aea9-3bbd-94c0-f7ba5afe87ce | -6.59573 | -55.44174 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2abfff0b-be10-31e3-9560-a91ec83a2ffa | -6.49531 | -53.25714 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ada11b92-0903-37ae-9b82-e1de9704c933 | -9.01394 | -40.99717 | 2026-08-28 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| b570c30a-ad4b-3d77-a0ea-0c8afde994a3 | -6.63271 | -53.18648 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93ede1f0-183f-3e04-8107-65b802a0643c | -7.08197 | -42.19543 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 03c7dbe0-142f-306a-88d1-13feadf30d31 | -8.06377 | -45.83691 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43796cbe-75a6-308a-8889-1e04f972feb0 | -2.72078 | -48.80405 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b091e0f5-53ec-3f27-a9fc-2cce61861a67 | -6.18853 | -45.92443 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5550bef5-2844-3b6c-8e44-6a28f594b65b | -8.08553 | -45.85603 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8541cd9e-9a9c-33aa-a72b-50fbd7b9a37f | -7.74839 | -46.12951 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23c16658-2e03-3e76-b81e-fe8560c81d37 | -9.06965 | -42.81831 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 608380f8-0ef8-3260-bacf-f5fba18b4a04 | -5.34313 | -45.15492 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b18ce908-5490-3f51-839e-1e1d7a3e2b42 | -8.08899 | -45.85656 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89125e93-f276-38af-8b8a-2fbfda11afce | -6.13677 | -53.52554 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5637dc32-1485-3825-9e5f-c5ca49713e8a | -6.27188 | -53.13786 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 453a2ddc-fbf6-33d2-a4b3-f4e35690d582 | -2.73516 | -47.03817 | 2026-08-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 373229bd-6d26-359c-a3b1-3aa446b598b8 | -8.09005 | -45.8057 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a88ed0ad-5629-3446-8443-0d2c1f129c26 | -8.27266 | -44.82618 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc3fa9ec-bbc7-3ee4-9791-991fc94d16b4 | -2.88363 | -48.08086 | 2026-08-28 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b276dde-1b66-3d39-9d72-505e908a326c | -7.09375 | -42.82659 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04758d16-5fc8-3868-aa9b-9f94447eb829 | -4.8466 | -45.40395 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6b93131a-51bc-39a2-a9d4-4011bf7c2c1f | -4.85072 | -45.4006 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 3ee2917a-77cf-36ff-a978-09bd75b32ec6 | -6.13777 | -53.5267 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 644d3def-8747-3ca4-b0be-134dfeb062ad | -3.70295 | -45.25122 | 2026-08-28 04:14:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8f7a5bc-06a6-35b6-b53b-d3dbf425b58f | -6.13612 | -53.52927 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd863426-7351-39da-a6c2-aa0bceb6d70f | -5.76191 | -50.223 | 2026-08-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
