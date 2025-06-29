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
| fbf5907a-6ce6-3dad-969c-384c2110d2ab | -7.1936 | -43.70691 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e129fb0-b946-394c-83eb-96478362d6f5 | -6.62121 | -47.28428 | 2025-06-29 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5da88aa9-a799-3cc7-a8a1-81647f761dbc | -9.71424 | -56.18728 | 2025-06-29 04:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4d8f76f-0007-3aaf-8e3f-5bdea16d50f5 | -10.92991 | -44.15483 | 2025-06-29 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5895f741-3a28-3ed3-8cb2-53dcfd7d337a | -11.55661 | -52.80532 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47ed5d19-b525-3f46-9451-1db2db500673 | -10.55138 | -52.04797 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 74627a42-94a0-3ae8-80b1-34d67e0884c9 | -11.88279 | -46.50414 | 2025-06-29 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20af46c7-7b0c-316c-a997-8885a71cbb2f | -11.25779 | -52.73925 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7128931a-588c-3a9b-9759-9f59aa6a696d | -11.73108 | -47.62101 | 2025-06-29 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e208e4d-c150-3eef-8cc0-0928b7878310 | -7.25933 | -43.12875 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 76ffff0c-c3d8-3f9b-86c9-e9770bd6be0c | -11.02784 | -56.28334 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7a44034-621b-3dbf-bd41-f21cc6d3fe2b | -11.58041 | -44.83535 | 2025-06-29 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dc7068d-44fa-30d9-8c9a-5ce10786e637 | -7.09721 | -44.36495 | 2025-06-29 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e038bf12-6938-31cb-b1ef-7c989873509e | -7.19178 | -43.71814 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 718081e9-d0ee-3e65-b749-af762daff07e | -11.55692 | -52.77367 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0d991b0b-20b0-3f3f-b7a5-59b7c9087d15 | -7.18957 | -43.43225 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4bc594af-e37a-309d-beb8-8cbfaa63ec17 | -10.56154 | -52.05367 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8dc7b788-86b4-3eae-9c85-df0f64b86abe | -12.93327 | -51.56683 | 2025-06-29 04:10:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18d1b0fb-8fd2-3d3f-aed8-c3a2fd5e5233 | -9.70327 | -56.18561 | 2025-06-29 04:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a14c631e-b15a-318a-bbc8-05ef818a64d1 | -11.27386 | -52.74648 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 178734e0-6b10-3f85-b51c-1109a67c2739 | -11.26972 | -52.73773 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 675f161d-3f71-36e6-abe3-e3ab91364153 | -10.53977 | -42.53537 | 2025-06-29 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3602140-cb68-3672-a82e-b95948c802a9 | -11.01447 | -56.23556 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9f7cec9-01ca-3905-bbd8-2d37cf7c943c | -10.56021 | -52.03142 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26eb2744-831d-3f0a-b1cb-9052d74b7a03 | -12.04937 | -48.08223 | 2025-06-29 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c92562f-cf3f-3e83-b9f5-f31af297025b | -7.64228 | -44.71281 | 2025-06-29 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53264fbc-9451-32bd-8eee-89e0aae3d876 | -9.72126 | -56.18889 | 2025-06-29 04:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8c77822-2997-300c-ac03-ae4cd7c29de9 | -6.62966 | -47.28566 | 2025-06-29 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| afb99dc6-d20c-39ab-ba18-895ebe2a3513 | -11.0353 | -56.27436 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e237b83a-2783-3e3f-b163-a6f59484b294 | -10.85277 | -53.75683 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a61242-30ab-3106-9e84-2061f1d07290 | -7.26434 | -43.14067 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 76d6364f-babf-3f3b-a74d-f41c52e300fa | -11.54278 | -52.7867 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f8cdc784-6a67-32dd-ace4-9a3a75caa35d | -7.18833 | -43.71759 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d76d2ae-af37-3a86-9dce-2258c030a9d1 | -11.56439 | -52.79512 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b180d651-c9a2-355e-bbf3-dd8aceb00035 | -13.46126 | -47.38548 | 2025-06-29 04:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50e43b57-0ea7-3fda-96c0-81e79c41c8bd | -10.56789 | -52.04435 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3edf4d4e-9943-3f9b-832b-eed254585ac4 | -10.79868 | -47.99428 | 2025-06-29 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28247ce6-0e3a-30f0-a901-ff3befd0a8a6 | -10.94894 | -45.59997 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e08f475-640e-3520-87f6-d761bad97ee0 | -7.55564 | -45.82719 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92553b83-1a2e-33f7-9c9e-1333b7531250 | -11.54614 | -52.79933 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dde855a3-b220-304a-937c-7fad9402151a | -11.55206 | -52.7688 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0ec06fb3-3b52-362e-8af5-63cc502c691b | -7.19421 | -43.70317 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb6f2a04-7de0-3e4c-818c-d36e88db90e7 | -7.25758 | -43.13959 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 770c2c02-a116-3081-ad70-fa1c6a4ae455 | -10.8683 | -53.74903 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72118781-8273-31ef-a445-156dbf163265 | -10.55507 | -52.05287 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 64d5dab0-4328-306c-98e6-f2eac579d52e | -11.551 | -52.80424 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c27b803f-7646-3cf5-98ed-b2494d1cf207 | -11.56365 | -52.79893 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a710e9d-f21a-3bcd-a1f6-44beefad72c6 | -11.03112 | -56.25969 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d04c5878-c257-3435-abcb-4dc50770288b | -8.01727 | -47.41291 | 2025-06-29 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4109f76b-3a3e-3292-b6f9-ffcc4b7e2aa8 | -7.40287 | -44.57279 | 2025-06-29 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cd1b5c9-aee9-3107-bffd-9e2b844bfa61 | -11.54353 | -52.78286 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b6cd9a36-3e5a-33ec-ace2-ffae9afddfb6 | -10.55162 | -52.04111 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a1250168-1593-32ab-8a6d-fdf54bf4ab90 | -11.55249 | -52.79654 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fa67b937-3c4d-3bff-a5a9-cfe5354c311c | -10.83207 | -53.76683 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b74fecf5-b4a2-31de-aab9-9e3aa5ecbdaf | -8.075 | -34.97845 | 2025-06-29 04:10:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fee8b421-9034-38e0-8204-be21504a9e71 | -7.16173 | -49.51006 | 2025-06-29 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b52d3e43-4f4a-3cfb-8112-c420b5f95a54 | -10.85876 | -53.75816 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93d7be7f-9296-3f51-b37b-896cce874b1c | -10.85189 | -53.76139 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c329c6e-3aa9-391c-bacf-417681749cef | -10.86142 | -53.75217 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bac8a54d-bec5-35f6-a437-d14a3185be55 | -12.0208 | -47.77604 | 2025-06-29 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dde69620-0d08-3ab2-8723-8471f0483920 | -9.43029 | -47.94974 | 2025-06-29 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 889d60ee-936f-3ff6-a4eb-e2f70341d333 | -12.11132 | -54.5804 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cab334e6-a294-383a-883c-322a4e6fb63c | -6.62478 | -47.28887 | 2025-06-29 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0819975f-fea2-3f60-99ae-6fe6d808d1fb | -12.05996 | -48.47759 | 2025-06-29 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7a76aec-0ac9-3883-9a8c-e3d2c2900a59 | -10.56116 | -52.05037 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19d4de9a-b230-39be-8df4-62a3634dc9d1 | -11.88152 | -46.5055 | 2025-06-29 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f130ede-0429-3377-8a2c-f9be19c2cd4d | -12.0248 | -47.77676 | 2025-06-29 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2e9cc7e-8b66-37b5-a9da-14d7202fa78f | -11.57571 | -52.11391 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed7fffe4-366e-367b-a1b0-3f4a8948aeb4 | -10.55749 | -52.04549 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5b08634a-c623-30c7-b34a-39982bbb0375 | -10.56901 | -52.0441 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 371c31af-912f-3e50-8eb0-725df880c17e | -12.10515 | -54.57904 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e5de640-19e7-3711-b769-05e242ea0fdc | -12.18255 | -44.34054 | 2025-06-29 04:10:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 863241ed-2014-3ecc-b10f-4c0790cc9e2f | -8.84933 | -50.1754 | 2025-06-29 04:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ca4f8ff-e292-3e3a-bb90-89e1ab5d1ed8 | -11.27217 | -52.74163 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 405b606e-f99e-3f07-b336-605746c3f1bc | -11.54203 | -52.79057 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7c3a2664-30b7-377b-8889-102f17a0db42 | -11.55133 | -52.77257 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0f95884a-f216-3c09-a5be-f5dc74e4d854 | -7.55527 | -45.83431 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae1da84e-3b0e-3ab7-a3de-64e2dd754ebf | -10.55836 | -52.03512 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ec509fe8-d4d8-3980-b5ba-1a480211f56e | -11.03949 | -56.28904 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bec4c56-0f82-3f61-b7a9-4b9c3ea24c0b | -9.79073 | -48.57122 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47f105dc-ed12-39ae-b63c-5dfd7f3931b0 | -12.05578 | -48.47683 | 2025-06-29 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1fb607c-bb0d-318b-8bc0-2257b676016e | -9.14808 | -46.38522 | 2025-06-29 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9690cf27-f4bf-3ad9-8b49-769062260511 | -10.97431 | -45.11635 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5340349-b3d3-3c3b-a107-f7284b0caead | -6.62609 | -47.28107 | 2025-06-29 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b540f4b1-c1a3-35e8-a0c4-c6149e8d9c7f | -7.19765 | -43.70374 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fff18b9-311c-3e26-860c-14e71a85370b | -8.09014 | -46.85841 | 2025-06-29 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17325b7c-01a4-380b-bce7-babb3be292de | -10.55206 | -52.04443 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 442b7c3c-085e-30ae-bdb8-5ccbe7ee381e | -10.9578 | -48.14997 | 2025-06-29 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 367e378e-f8aa-3ebb-bb6d-dcbc7d206a83 | -6.63031 | -47.28176 | 2025-06-29 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2c04a0db-9e5d-3e7e-a049-e5960a356821 | -11.49516 | -48.0812 | 2025-06-29 04:10:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ef1fbc3-23bb-34fc-85cf-ded8ea7f2b2c | -10.79454 | -47.99364 | 2025-06-29 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 814501ef-b430-3c26-bb63-09a5cac26237 | -11.83619 | -47.52456 | 2025-06-29 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36990889-6d96-387e-b668-548984cdb644 | -7.26154 | -43.13651 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6194ca9b-0c9e-32f0-9cbe-0b5d832b5677 | -9.64302 | -48.79131 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c702d53-cd34-3fec-baf0-daa5fa044fc4 | -11.01373 | -56.24584 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1231e7f-5281-3166-8d0c-2970d4255900 | -10.83807 | -53.76812 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd199fc3-8657-3b76-afd0-73b09c46c320 | -6.89692 | -43.97936 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eed62bd0-8d12-382c-b0a4-0bfc1180f64a | -11.03344 | -56.29144 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9da7affe-fa5d-3b0a-a895-b1b956df9a34 | -7.54948 | -45.84044 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44a5c616-bfac-30be-a3ef-d29df0cfdd81 | -10.98199 | -45.11355 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README12.md)
