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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c575eee7-3480-3361-b622-4f0abe8cbcd9 | -19.8929 | -47.8138 | 2026-05-09 00:00:00 | GOES-19 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 56.6 |
| fe8a5197-e776-3e29-9b40-e9b97ac88721 | -11.2978 | -54.7668 | 2026-05-09 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ca24d18d-5c0c-3e87-b495-295402644c91 | -16.4163 | -54.9079 | 2026-05-09 00:00:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a4df94ad-ac58-3b4a-a5a1-0019710bff7d | -16.4163 | -54.9079 | 2026-05-09 00:10:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9ae16c8f-60b0-38cc-bd1a-445f98b079ec | -11.2978 | -54.7668 | 2026-05-09 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 476913ca-322a-32e9-94b9-da05a709594d | -11.2978 | -54.7668 | 2026-05-09 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6d5b4aeb-f267-353d-a222-d490f43273b6 | -14.0118 | -56.6215 | 2026-05-09 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 03a16d37-d9a6-300c-87af-df4bb8051e54 | -14.0115 | -56.6418 | 2026-05-09 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 75f06bb6-8f12-31e0-93f5-d59b830115fb | -11.2978 | -54.7668 | 2026-05-09 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 36028622-f4af-3b5a-82f5-ba06ee3d21da | -11.822 | -47.3298 | 2026-05-09 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d2b33fd9-beb7-3539-a41b-52414f88d647 | -14.0115 | -56.6418 | 2026-05-09 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| e90996d1-53f9-3193-9ec3-f47da725e0fc | -14.0118 | -56.6215 | 2026-05-09 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 59b842fa-ddca-30ef-b42c-4268efab16b4 | -11.822 | -47.3298 | 2026-05-09 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| df1e17b6-6841-3755-85ef-d025a044185c | -14.0115 | -56.6418 | 2026-05-09 00:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| a35d6f1e-38e4-3b6b-9a85-36c0b9d10a03 | -16.28026 | -49.95989 | 2026-05-09 00:52:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 1b965229-7b4d-3f1b-8905-6329457d337a | -11.51076 | -58.66277 | 2026-05-09 00:52:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 362976eb-ebbd-3661-a865-fc2563d34f7b | -10.66329 | -49.71254 | 2026-05-09 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 5a5a5187-17a8-377b-9201-34ef6d99ea7c | -10.55868 | -56.34259 | 2026-05-09 00:52:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1b30edb3-cf7b-3e05-acb2-c1455ef08605 | -11.29242 | -54.76975 | 2026-05-09 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 7e2a64ab-e720-32bc-a3c6-f805d460d37c | -11.60498 | -54.18635 | 2026-05-09 00:52:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 62aaf849-6860-3854-82bc-9f685020b910 | -11.50953 | -58.65382 | 2026-05-09 00:52:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b30e7c6a-ea48-3556-aa0d-e995a85de735 | -11.91904 | -54.11084 | 2026-05-09 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| cc1cc094-0f43-35e1-8fec-918c09d9274a | -14.32316 | -57.73557 | 2026-05-09 00:52:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb0e41da-fcf8-39e4-888e-78a2e5a1fd3f | -10.54933 | -56.34394 | 2026-05-09 00:52:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5222392f-cd8a-3e67-9556-16cd54b273ea | -16.28611 | -49.96535 | 2026-05-09 00:52:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 439b0790-3961-3075-b091-d910a4d89467 | -14.00333 | -56.63864 | 2026-05-09 00:52:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 3f76983b-87ef-3f33-86be-42c327524511 | -14.32191 | -57.72654 | 2026-05-09 00:52:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e30cc119-0575-3516-adf0-a25db944ddff | -14.00201 | -56.62933 | 2026-05-09 00:52:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| c8cad786-aaa8-356e-a604-a2162252ad58 | -14.01096 | -56.62791 | 2026-05-09 00:52:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e8c5bf7-d68c-3046-ab7e-d5995dbf5655 | -11.29058 | -54.75759 | 2026-05-09 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 52bf7c75-d51d-31c0-a912-543d8c211ccb | -9.25067 | -60.33648 | 2026-05-09 00:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d78286d8-1779-37b3-99d4-3938a2780c7a | -10.5542 | -56.331402 | 2026-05-09 01:04:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3e8f8e1-ef81-31e7-a87f-62ec1ed5d911 | -9.8323 | -63.2369 | 2026-05-09 01:04:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8cec29b-7cc2-347b-b481-d338abe669bd | -16.2722 | -49.935799 | 2026-05-09 01:04:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a7da8ce-6ba4-3bc8-9956-4bebf4ce61fd | -11.2931 | -54.762501 | 2026-05-09 01:04:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e354b12-2164-37a5-a9a0-2c2bc2850d3b | -11.2993 | -54.746101 | 2026-05-09 01:04:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 631817cf-2eca-3a9b-9b01-f0239181d133 | -14.0033 | -56.619999 | 2026-05-09 01:04:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c15b8037-679f-343f-9e9c-806306c8fb39 | -14.0057 | -56.629799 | 2026-05-09 01:04:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b8fc8a0-1674-31d5-8985-0b370aa04a28 | -11.2896 | -54.7486 | 2026-05-09 01:04:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 031845c3-76d3-3576-a928-522c1066638b | -16.2765 | -49.9387 | 2026-05-09 01:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 10af1a99-e581-391d-817b-9baa5e01ec68 | -16.2761 | -49.9608 | 2026-05-09 01:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 141.3 |
| f1335de8-d88c-3ac1-a580-43929b58f022 | -14.0115 | -56.6418 | 2026-05-09 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 77427d61-f7dc-3a3d-88e7-79708ebf9eeb | -16.2958 | -49.9575 | 2026-05-09 01:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 147.6 |
| e285176f-754f-3bde-ad75-faa0c4fcf188 | -16.2962 | -49.9354 | 2026-05-09 01:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cc0845bb-e2f4-39ef-8f31-4dc4b519ea1f | -14.0118 | -56.6215 | 2026-05-09 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 62940d61-e6a0-3b5c-bc8f-1af7b5a6e38f | -11.822 | -47.3298 | 2026-05-09 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 3eb693e7-8463-3f5e-aa2b-025486f55d4c | -11.822 | -47.3298 | 2026-05-09 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 45244905-ae2d-38ad-aee8-a18ffd6aa5d1 | -10.5606 | -56.342701 | 2026-05-09 01:34:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7c65c4-b723-3d93-b9b6-13f5b383b9eb | -11.3051 | -54.756401 | 2026-05-09 01:34:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4812b8be-c97d-37a1-bdd0-f52259650eaa | -14.011 | -56.623402 | 2026-05-09 01:34:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd20f241-47cd-306b-a1f7-bb56b196f3e6 | -14.0133 | -56.632702 | 2026-05-09 01:34:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0aabdbba-624f-3b56-a50e-5b23315aca3f | -11.2954 | -54.758801 | 2026-05-09 01:34:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d83fcec7-161d-34d4-a44d-db2583ce8512 | -14.0035 | -56.635201 | 2026-05-09 01:34:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51dd0f00-e460-3bb9-9aca-408d8735b833 | -11.822 | -47.3298 | 2026-05-09 01:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f4aaf46d-dfc9-320b-94bb-72f348708477 | -21.3445 | -47.0236 | 2026-05-09 02:40:00 | GOES-19 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 48b9d820-f21d-336f-8ce3-016623c9096d | -21.3445 | -47.0236 | 2026-05-09 02:50:00 | GOES-19 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ce5f47cd-d383-3c18-b786-0eec68c1c29a | -20.2457 | -46.8204 | 2026-05-09 02:50:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 70.0 |
| d5a2273c-275a-387c-896b-e74fb3a56b12 | -20.2457 | -46.8204 | 2026-05-09 03:10:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 610cc7e6-78dd-3fb0-aeed-6005dd322b9a | -21.09019 | -41.24693 | 2026-05-09 03:10:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 985c49af-954d-3e4f-bf7a-19cbd93621b5 | -21.08911 | -41.25149 | 2026-05-09 03:10:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 94e5d900-05be-3c33-b02d-3ab6faeaa90f | -3.1437 | -40.63886 | 2026-05-09 03:53:00 | NOAA-21 | MARTINÓPOLE | CEARÁ | Brasil | 2307908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad285a6a-573a-36a0-936b-eb48369979c9 | -9.30571 | -48.58484 | 2026-05-09 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5817800-069c-3016-ae9c-10c41a18d398 | -8.73145 | -47.98414 | 2026-05-09 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13e40c41-9e52-3749-921c-1213af0cac30 | -6.19372 | -44.86988 | 2026-05-09 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71e25a2a-f3df-3a6c-94dd-dccc9b86df2a | -8.72772 | -48.32451 | 2026-05-09 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df4385f4-32df-30ec-831c-4614d65ccae9 | -8.69105 | -49.0709 | 2026-05-09 03:55:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d61c6b0e-d323-3561-9066-a64d4fa1d0a9 | -10.63713 | -48.01388 | 2026-05-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2de8ef02-c4c8-35ce-999e-ff2988548fe2 | -10.55317 | -42.43547 | 2026-05-09 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 52e531f0-d6c0-3b4b-9b35-7a791646f90d | -10.6409 | -48.02219 | 2026-05-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca701f31-b261-3ef1-b70b-8f2a8386a241 | -10.55679 | -42.43608 | 2026-05-09 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 39598507-f0b5-36ad-9da6-9c185ccab224 | -9.64425 | -42.96827 | 2026-05-09 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c51ff9fe-9294-3490-83f3-4622028609ff | -8.6903 | -49.07491 | 2026-05-09 03:55:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b6a33a0-4ab2-327e-8a05-1c0465d2b3c7 | -10.64028 | -48.02552 | 2026-05-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18a5a237-ea19-31d5-8397-d8e37d04f34c | -6.32424 | -44.63552 | 2026-05-09 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 337e29d6-62a4-31b6-9989-8efc2d18dec1 | -8.70591 | -49.08599 | 2026-05-09 03:55:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 930fb024-e8ca-3e10-bad1-dec343bb36ba | -9.64483 | -42.96103 | 2026-05-09 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b2b42e8d-2c82-33c0-9ca7-c4eb892396c6 | -8.70291 | -49.1021 | 2026-05-09 03:55:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccc971b4-14f4-3d8c-b26a-de8285125f36 | -8.72677 | -47.97975 | 2026-05-09 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a97b72f9-e8e2-3faf-8330-f68ab7dd21c2 | -8.72578 | -48.33501 | 2026-05-09 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f3d6ccc-9116-38b0-acd7-80310a075b43 | -9.01505 | -40.99317 | 2026-05-09 03:55:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a588c27-1bb3-3c33-a9d7-9806a02bab20 | -9.30504 | -48.58841 | 2026-05-09 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a3138c8-60e0-3197-b47c-026b0832d767 | -10.63776 | -48.01052 | 2026-05-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dffe3d32-5ebf-3b0d-8a22-1b0d119e9e6b | -9.30026 | -48.58379 | 2026-05-09 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b93e3de2-8b6d-310b-9ff6-a34e1e44399e | -10.63193 | -48.01326 | 2026-05-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb43a9c7-970d-3dd8-8b41-995f6f4493b6 | -10.63076 | -48.01949 | 2026-05-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a9c373f-79a8-3566-8331-7ff48422e0cd | -9.3045 | -48.58664 | 2026-05-09 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a187d5bf-df03-3e66-a9e9-ca9608538e95 | -10.63133 | -48.01643 | 2026-05-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b1ff36e-1e5a-3d61-ac0d-abed60e0163c | -8.70516 | -49.09001 | 2026-05-09 03:55:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3fd7576-b83a-37a1-9d9d-61a3ff46e5c0 | -8.72615 | -47.98318 | 2026-05-09 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d2c402e-3d05-37f9-abd8-1f0dcfc817cd | -6.32942 | -44.63178 | 2026-05-09 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 098f5dce-8292-3078-aa95-0de191651da3 | -10.63648 | -48.01738 | 2026-05-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8662260c-0178-374b-b0b4-027ae8d26fc0 | -8.72643 | -48.33146 | 2026-05-09 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f55e3509-784e-359e-88b5-e63bef22011f | -6.18921 | -44.86922 | 2026-05-09 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75c34bf8-5da4-3d1b-bd1a-1ddec71d8b75 | -8.72738 | -47.97638 | 2026-05-09 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d4e8a55-f983-3797-8477-3b815bfa6281 | -9.38762 | -37.80995 | 2026-05-09 03:55:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 542685e6-da00-3b39-8749-c5a02210296e | -9.64332 | -42.97024 | 2026-05-09 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 40737815-8f5a-3bb8-83e4-1894b539f325 | -10.55247 | -42.43969 | 2026-05-09 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| db3c1401-cd31-30bb-96b7-1572f6a0b865 | -8.70097 | -49.08084 | 2026-05-09 03:55:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bfcdd10-83cf-3feb-a341-b7208cf914da | -10.73187 | -43.98434 | 2026-05-09 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5af541b-30af-3c7e-843e-b67a6182ecd6 | -9.64346 | -42.97287 | 2026-05-09 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README2.md)
