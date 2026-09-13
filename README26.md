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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f619a6e-a1ab-3265-9928-6dedf8fb724c | -7.87494 | -54.71538 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8baf7207-95e0-394b-a505-5b5e7df77138 | -10.22221 | -45.19165 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a604b3e9-2826-3db1-a098-8bc3a0a7ab5a | -11.51781 | -54.62894 | 2026-09-13 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 340e0962-eec9-3e24-aa14-094ea9db7857 | -11.31356 | -48.5452 | 2026-09-13 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab1f7e2a-3337-3467-8298-2aa308cb1ca5 | -11.57053 | -46.98859 | 2026-09-13 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 67cac6e6-16c5-379d-b372-ea70f6c7fe15 | -9.54755 | -45.44701 | 2026-09-13 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 337ae90f-4bfc-34f1-9d64-bc9ba07ffac1 | -9.80184 | -46.55654 | 2026-09-13 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db1b90ab-9106-3776-bf20-b0fc2356443f | -14.12763 | -42.1179 | 2026-09-13 04:17:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0c0cf6c-6669-3054-948d-97a78afff388 | -10.5135 | -57.45673 | 2026-09-13 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de7e3c86-4a2d-30eb-a665-14f2cd3c76eb | -8.12469 | -54.80942 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34842a1d-1c1c-3db7-8863-2f33de9cc6c2 | -10.73077 | -54.0015 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 810798af-d656-33f5-ac4e-1f0c10f05397 | -10.53562 | -51.38495 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03a4d1d8-9f25-34a5-bcda-59b15068565a | -8.12279 | -54.80879 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4861393f-cc64-3917-96d6-d81a963e5fb6 | -11.72233 | -46.73946 | 2026-09-13 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ad6582c-11bc-3199-8396-bb061abd4a6c | -7.87577 | -54.7109 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d194bdd5-920e-353f-98eb-212faedd3fef | -13.38659 | -48.01223 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29266a01-bc8b-3c29-b9d9-7dc755d005dd | -9.58528 | -55.16219 | 2026-09-13 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45512082-5760-3750-a8c7-c290195e1d45 | -13.45052 | -48.49635 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cc67c74a-f745-3a5c-9a5a-043af7259cdc | -15.26529 | -42.79667 | 2026-09-13 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d99cd72-a7f0-365f-9489-126c92626f75 | -9.94742 | -48.50701 | 2026-09-13 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaee07f0-f87d-367f-aec0-9a4bab79b371 | -13.37341 | -51.70986 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d18d8e4f-72f4-3ebc-928f-c969e0943059 | -13.46089 | -48.4798 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ffe3b49c-39ee-3bb9-85a1-e8c068a02ad5 | -8.0343 | -54.84927 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9aeaa1eb-dda6-3536-b71c-4e5792addcff | -15.28394 | -46.58336 | 2026-09-13 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b7727a0e-16fe-32b9-a941-6cc2b274bdda | -10.90489 | -47.81952 | 2026-09-13 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b38e27a5-91c0-32fb-baed-5a5f59c15de6 | -10.54413 | -45.20012 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69885516-a520-3980-b424-1d57b8e5da25 | -13.43384 | -43.82697 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49560346-3930-339f-8656-a3f19aa9060e | -11.63588 | -41.43174 | 2026-09-13 04:17:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1cf8e7c8-1daa-394d-ae41-fe330add9f56 | -9.70868 | -54.3576 | 2026-09-13 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7cbdb86-834e-3b9d-8b15-f269f21c0d7c | -10.62833 | -46.10528 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 168c35f3-dc99-38e6-acdc-9ad39c494124 | -8.0593 | -54.84908 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c0e5349-e00c-3f97-9450-f866a7dea3f6 | -10.90857 | -47.82007 | 2026-09-13 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7813c80d-67a8-3d62-8192-4bc55b87e3ae | -13.48576 | -48.48905 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0d37438c-a748-3684-82ad-f317fe9f5b14 | -8.04636 | -54.85153 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33241ee8-7928-3ac3-9989-bef2afd12374 | -10.63081 | -50.57079 | 2026-09-13 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0356ebe7-aa17-3121-b7b2-27500cc53e2f | -10.63234 | -46.10213 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8660679-27b4-31ae-9f5b-80c8a46b92d1 | -13.61439 | -47.89018 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bdaea4f-3406-3863-a83c-9c24719595be | -13.60091 | -47.8834 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b06158ad-c8e5-3247-8ea7-163ad6eb0d0e | -8.01951 | -54.8536 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28ba5a8d-abc0-395b-82cf-107aca93a8ad | -11.43343 | -45.1483 | 2026-09-13 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ee73069-30c6-3034-b81e-2d7687c330de | -7.86289 | -54.71341 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f950bcab-ae5d-357e-8a11-d0f2b4d25754 | -7.8672 | -54.7236 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e318f452-8025-393c-8bac-613793f29281 | -13.61659 | -47.8773 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9846ede9-9935-3f49-bf4c-c53248fca6ec | -10.62758 | -50.56882 | 2026-09-13 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5525e383-a819-305f-b6b6-67d183e11e66 | -11.18457 | -42.79858 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b56810e0-299f-3a60-b1f1-aac0b3aae157 | -13.46014 | -48.48423 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 576b12f7-3080-32ea-9820-69fd10e60efb | -14.91192 | -44.67274 | 2026-09-13 04:17:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39426277-07b6-3950-892a-083bbe2f25ea | -9.59245 | -46.72337 | 2026-09-13 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf654004-2819-33a4-a862-2f42aafdf5a4 | -11.57402 | -46.98919 | 2026-09-13 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 31a33f50-ccd4-355e-a22c-790e104f0e44 | -13.991 | -54.07179 | 2026-09-13 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5ddaaf0-647c-3ae0-818a-04a9b2f9fbd1 | -10.28188 | -45.32932 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a09aeeb8-393e-37f5-8469-cf8c2a424efd | -8.03945 | -54.85508 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69390443-8601-3b84-b137-15c4fdbd89da | -15.23528 | -49.4575 | 2026-09-13 04:17:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b4e35a7-2aed-3417-81cd-7e795a460fee | -7.86698 | -54.69147 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fc61923-10a4-35d5-b1c5-cf164c3b2293 | -8.11869 | -54.80825 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1d8f9e3-0d1d-33e1-9dbf-75b885d46935 | -10.74049 | -49.58988 | 2026-09-13 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b65a7c0-5f5c-3592-ade1-6c21a5a4861f | -13.4638 | -48.48492 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 534b521a-ae3d-328d-9349-9351ef735465 | -13.60449 | -47.88384 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb35903c-72d7-3dea-aa8b-954191d9dba7 | -13.39454 | -48.00893 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d504a115-9401-3eae-a279-a1d02f4bfe2a | -13.36811 | -51.71354 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 845b6885-bb77-301c-9e8b-0e1d1462ac0d | -9.13384 | -51.60603 | 2026-09-13 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 464323a9-8fe8-30a1-9098-ecc82c31d92f | -15.79248 | -42.3188 | 2026-09-13 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0227e8d8-2f77-3f58-aeab-4f9095203994 | -15.28335 | -46.58699 | 2026-09-13 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79f5b598-cb07-3640-b9a5-a9fa14332aa2 | -12.14518 | -48.9583 | 2026-09-13 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 903e24fb-9d2b-3c6a-a997-001285eddb18 | -10.68822 | -54.16669 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6cc25a74-8781-34ac-bd11-e84a8d3b6132 | -13.45554 | -48.51128 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afa5caec-bcb9-3113-a77e-d11016b393a7 | -13.38303 | -48.01148 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9e376ee-d1a0-3323-af72-c5083746b892 | -8.11611 | -54.78918 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c7eac2a-2764-3579-9bf9-1b38d1940f2b | -7.86892 | -54.71436 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29b0a750-7b23-3aa5-9589-273850f5601b | -10.64478 | -46.00483 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 163f933c-5ff9-33bc-924e-51321cbed638 | -13.59731 | -47.88831 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8366ff0e-2632-324b-aaef-eeef88c49fdf | -7.87408 | -54.72001 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37a2edeb-cc2f-3b34-9f40-37d06422f0da | -13.30002 | -43.67644 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b562ad5-e5c0-3ead-a47b-b1fbf289f7ab | -13.60877 | -47.88026 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| abfaf908-d3bb-39cf-b57f-8ff987081d11 | -11.51564 | -46.82161 | 2026-09-13 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b32d73db-a51a-380d-966f-8f4d8abb38d8 | -10.63614 | -46.01064 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38fa9673-3358-353f-9a3a-ef794e26e8d5 | -10.94559 | -48.35442 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da2e411b-4806-3d2c-aa5b-8e2efebc4032 | -10.93797 | -48.35353 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c61d0e10-fbf9-36e4-8f30-355688e945c9 | -11.5212 | -54.62922 | 2026-09-13 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efe107b3-184b-383c-889a-7e8be97fcadd | -10.63274 | -46.01009 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a370b3da-9e65-3127-8b51-6e53372f9b66 | -13.75727 | -42.59967 | 2026-09-13 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c004f0fa-e70e-3bb2-8960-01210cf2cd8b | -8.1193 | -54.79396 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6db0550b-9125-3a0a-9a94-ba64cbcdfc65 | -11.80603 | -46.382 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddfdc440-0528-3c21-9f38-413dfecfa33e | -9.59132 | -55.15103 | 2026-09-13 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2953e637-b5a3-33c1-b6ab-87c601bf92bb | -9.71655 | -54.35809 | 2026-09-13 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad2d1796-e910-3708-9d92-7be8763c47d3 | -13.6002 | -47.88753 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddcd7995-e8ea-351b-91d6-7495e6a7008c | -10.75646 | -46.2455 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 464d9d6e-834f-35c0-a5cd-1ba182db3dfe | -10.536 | -51.30394 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78ccf62a-6a0d-32aa-98ff-f27d37b9e6f4 | -10.63215 | -46.01379 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d4884c3-2511-320c-a805-84aa0c98959e | -10.57499 | -51.35079 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff638e09-cf9d-3897-85fc-75e06d19ce42 | -13.74974 | -42.60258 | 2026-09-13 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f5953b7a-75d9-379b-93fa-501a7645c6f6 | -11.43929 | -45.15342 | 2026-09-13 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5580e8f-d1fa-37c7-ad4d-4a0283f1315b | -7.87215 | -54.69697 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec32fa4c-d536-38d6-8b5a-f52eee93b8cd | -12.17798 | -44.0188 | 2026-09-13 04:17:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6cf7dd1-8028-31dd-bfdc-826d8732bbfb | -10.47005 | -48.63408 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87ffaf2c-7a6f-32eb-aaf7-0769d045b270 | -10.69373 | -54.16784 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f96be76-2498-321a-9a8a-618959c36924 | -11.20084 | -42.78239 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2c3e675d-c94e-3450-a283-a43f98e8f3fb | -12.15586 | -48.96513 | 2026-09-13 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a1391124-99cd-3f03-847e-838acc862662 | -14.71118 | -46.64942 | 2026-09-13 04:17:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b0a76a17-9724-3d94-8b3d-edcd4fd511f5 | -8.05239 | -54.85267 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README27.md)
