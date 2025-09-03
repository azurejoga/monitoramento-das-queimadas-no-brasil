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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 212082c5-674a-3acd-bd21-2b0a3bd4b22c | -6.84681 | -45.55071 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91e9cbd8-f053-3c73-b53d-889f3663458c | -5.89513 | -46.16389 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0ced4af-e9ed-3446-a380-8d8cb606f7d0 | -11.59347 | -52.11814 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c0ab509f-5e48-3c67-9d7d-c7786e0a9fee | -7.93269 | -46.47075 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57f56e89-707e-3bdd-92c8-c094413499dd | -9.95245 | -51.62631 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a9275c7-7afa-3c39-8ffa-404236fbdfdc | -7.69763 | -48.73645 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 23.9 |
| d4e47d20-f554-3857-ad41-4aace45af41c | -6.84844 | -52.82423 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65036d73-886e-3acc-a297-db7a82ee7c14 | -6.84449 | -52.82734 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c51636b7-8bba-37e7-89e0-a8c0329dfb8c | -5.81326 | -43.2291 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 85e9f3fe-fed3-39bd-adb4-26d0777d8124 | -8.46298 | -45.06211 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee616622-be94-35e3-a1b4-bea433bcabb5 | -6.05958 | -57.99512 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6639cb19-c392-3c28-a48c-f42dc91b130c | -10.75963 | -45.27477 | 2025-09-03 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19456b7b-2e10-35ea-a37e-426a53092ce0 | -9.42396 | -48.35629 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b4b4ed3-3be8-3e20-a607-98e9dac259f0 | -6.2737 | -44.5113 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7307991-2e79-31c3-aa4b-cab0cda332c8 | -6.26049 | -57.89873 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c450859-96a0-3cbb-8976-91cc4cdabb14 | -6.28657 | -43.58784 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4880f89e-ccb0-350d-844b-4fa46fbb5178 | -10.14567 | -46.26542 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f67c07dc-feed-352d-9bac-d5957b8d9c0d | -6.27242 | -43.30613 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| efac346a-9961-3649-801a-41378b6266a4 | -9.80857 | -45.98851 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ea14efc-17d3-3a21-b14c-d5018534bed7 | -8.54822 | -47.47658 | 2025-09-03 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa76d844-e723-3b4f-b59c-eecb1fdc6a10 | -5.91796 | -57.71362 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc5aafec-3680-3d91-9bd5-9b9c0fe0e98b | -7.69742 | -44.98676 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d23789a9-602c-3fa8-add2-c4727ea4a6d3 | -6.95298 | -42.97327 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e39dc59f-1e56-3657-97cc-096d6181a3a8 | -6.64774 | -45.91436 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6822697-0b87-3b92-ba8c-96e4e72cc9da | -10.14513 | -46.26935 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 526c9e65-e359-3085-adae-61a561aa3485 | -6.27752 | -44.51649 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 865e614e-daae-31cf-baf6-d0c157d1f289 | -5.80858 | -43.23924 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83c6fcf9-8204-3289-b508-7868b1f46e98 | -7.70651 | -48.72551 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 29133d57-98e9-320b-b634-156500b90627 | -3.7255 | -58.84504 | 2025-09-03 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ae8844-5d5d-3bd1-b08a-33f97499b782 | -11.80232 | -48.35874 | 2025-09-03 04:46:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50245f15-b710-3138-b7b8-2f4889fcf3ed | -5.89429 | -43.35648 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc3f9fb2-ee99-3c2e-aec1-51700a0af1f1 | -8.04795 | -52.35985 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05da76a7-c623-3789-b531-06c7ff260668 | -10.48367 | -50.33564 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9f29342-d083-3c7f-8c73-642f588352d7 | -11.60331 | -52.07658 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 490c9a10-0186-3375-8ce8-9d4e1aa31fc9 | -7.91656 | -46.43201 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fbd89de-8e64-344c-9c79-7881dc69f91f | -11.43566 | -46.90981 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1783fba5-a804-322e-bb91-6d7024767b6b | -7.00575 | -43.22322 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 895fca2f-d429-35d7-9678-d3a2c665de8e | -6.54133 | -42.95603 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6324342f-9ab1-39d2-b02a-386b154232aa | -8.15144 | -54.93392 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5944a3ec-91cc-3274-8a72-06a0192e4adc | -11.59459 | -52.13268 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 16783afe-562b-324a-8472-7795ce68b40b | -11.62256 | -52.0617 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b31b5e-d67a-3bd0-b22f-e9ef95af39f0 | -7.0026 | -43.23803 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 864aba06-e7f1-3e4c-a439-9aed11703884 | -7.43724 | -46.00958 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b00b69da-d8b7-311c-9878-53bd51dde62f | -11.12238 | -44.64181 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4196532-f1dc-3768-ab98-687631669e64 | -11.60495 | -52.06606 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e90fbdce-4d0d-3c19-b757-003744fdda69 | -8.857 | -52.02134 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3950d19c-4acf-30a7-8e76-9dbb5bc02183 | -6.50334 | -43.083 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f244ed85-aea3-33f2-b537-773cf75471c2 | -6.81914 | -52.83444 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bef99bd-d533-3a3b-a061-569e11370674 | -11.58468 | -52.1311 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 89ab1778-5add-3478-8bda-f43b3bc841b4 | -9.63529 | -46.11527 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1452e25a-ba1a-39c7-9284-df4a72c076ad | -11.59016 | -52.11761 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| da11d756-274e-3e4d-8faf-d7449e72974d | -8.36201 | -52.52566 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e23081c-c1a9-3fc7-8d71-50ebce6b506f | -9.1351 | -49.6552 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 17d1b0dc-a9f3-387e-b2c9-81ebcdb3a2f8 | -8.83685 | -45.77243 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ad9bf1a-8b42-3c44-bf36-1a0b7fb080d0 | -5.62667 | -51.29368 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5cd7585-4f16-30ae-b879-415d6a1e23df | -8.05128 | -52.36037 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5a7043f-407a-3bcb-980b-7d256a650c41 | -10.49607 | -53.654 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbc22fb1-1c5c-308f-b843-939afe26d791 | -6.27426 | -42.59764 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a33ec36-a395-3f7b-879e-190193de7889 | -7.89931 | -46.46566 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71c656b4-a075-339c-b877-67b816485b78 | -9.80036 | -49.98568 | 2025-09-03 04:46:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93118789-1908-3f77-96cb-03ae6496f3b2 | -11.19301 | -55.01616 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 211ed1ee-ea6c-3c78-9b7f-fd8597bdba4b | -6.26367 | -42.63609 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26adb3b7-64d1-342c-aa17-fc1b9f04afcb | -10.30013 | -46.36282 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a692f8e-1158-3ef2-b0d3-59152e20978a | -6.97721 | -43.27423 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c033c2d5-3869-31c5-a65b-9f984386178b | -6.78433 | -52.81403 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d39196f7-8659-3a4a-bdb8-84c05b81f567 | -11.39735 | -46.86206 | 2025-09-03 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61c0ca05-612e-3cb5-b943-4fa981ccfcbb | -11.06764 | -52.0661 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14b6c10e-ccdf-3d98-899e-c0eb1b7b9eb7 | -5.92021 | -57.72772 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 54971e97-d993-3b43-9f10-df2c43110d30 | -6.1737 | -43.31335 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1cf17d6f-ae1e-37e4-94a2-936fcbcf58f4 | -11.67499 | -52.22857 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da49fb71-e9e0-387a-8df0-48bd50be1b4a | -7.9685 | -46.50825 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 23973aa8-e947-37c5-8297-a166f8f4e618 | -11.44512 | -47.29725 | 2025-09-03 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed827c8b-bc3b-3996-84b8-efe7f3818b36 | -6.35284 | -45.65155 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53e90cf9-1a1f-32d4-bee1-96f137603fd8 | -6.21674 | -41.80462 | 2025-09-03 04:46:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0f419423-97f5-3ace-ab7a-f721f9984cb0 | -8.0704 | -45.36584 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d890ec6-e5e3-38da-a697-4f2dff2f5a7c | -9.14486 | -49.66061 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6f5d387-d374-3390-aa40-0603e0fcd7e1 | -6.82588 | -52.83554 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3aad47a-10b9-37e1-b91a-42592388d5ce | -6.77874 | -52.80572 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c81bbb0-5fd5-373f-bd20-3b2fd367137a | -7.90082 | -46.45522 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b800c33-01b8-36c1-80f3-ccc3e1a3f9c1 | -10.46251 | -53.62605 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c55b9b0-fb02-356d-b510-68b15e305c6c | -11.60171 | -52.10868 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 514a5312-3691-32e6-be78-8c77ab9bcd7d | -10.08519 | -48.06367 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2db8de5f-c363-3eed-b23e-16cd0ab7b720 | -6.79282 | -52.80421 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb945fd7-da12-3873-b159-5f9cbffa7533 | -9.14082 | -49.64055 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e715e78d-9ff5-3072-936b-4202b7d869e6 | -6.64375 | -44.09789 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c74bef7c-f6ef-3ec5-a317-3b8baba128e1 | -10.45635 | -53.62132 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42cb30ac-f25f-3e5c-ba64-5ef22dc75c96 | -8.86637 | -52.02639 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d74c8d80-78e9-3f57-9169-90e48b43e0ee | -10.67728 | -50.62889 | 2025-09-03 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a914dc9-9483-384f-8520-44a35b7dfdd6 | -11.40613 | -46.85942 | 2025-09-03 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6208276c-b370-3d57-b1de-eb8efa85f217 | -11.21312 | -55.06922 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f52dc3b-2f42-31c2-bb3e-e2d50b1c585d | -7.93687 | -46.52872 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01b464ee-d656-3c0d-bca2-06ca6d43872b | -6.58312 | -44.35564 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 980f6e07-480a-3ac1-b835-ac22b5e68e9a | -6.32914 | -43.56293 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebac712f-8f7b-37ae-872b-d57517e51efc | -10.27072 | -51.12936 | 2025-09-03 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc242bea-40f2-3189-80ee-7c8e0639bcdf | -7.48162 | -44.8274 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a4d725a-ce39-3965-ac6d-6b4c1b9fba12 | -11.63081 | -52.05223 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a348d8ef-8c23-306d-8661-d1c9a607fc74 | -7.70682 | -48.74869 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc95da77-ac71-313b-abd9-caf35938775f | -6.26418 | -43.29374 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1d84f4f-b343-3224-a2f9-5074778d4243 | -8.05232 | -45.3682 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51fc2803-4ab0-30cb-819d-5c649e98fdb5 | -10.476 | -53.62823 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README63.md)
