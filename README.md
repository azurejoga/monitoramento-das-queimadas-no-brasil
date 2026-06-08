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
| 06bdeaf1-f65c-32b3-b27d-6375e7c37aad | -14.3327 | -58.4614 | 2026-06-08 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 11b57252-06f2-3e32-9e75-5117580e7707 | -14.3519 | -58.4597 | 2026-06-08 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 5b8a4470-8633-35c4-9ba3-c440e52e6e99 | -14.3327 | -58.4614 | 2026-06-08 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 1eae8dda-d806-30e3-b709-0576659757ae | -14.3519 | -58.4597 | 2026-06-08 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6828c143-2c4d-35c9-beb1-c69b63666420 | -14.3519 | -58.4597 | 2026-06-08 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 7fa9a65e-f49b-3d9e-a337-7272cdc16ad3 | -14.3327 | -58.4614 | 2026-06-08 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 6f01614c-52ba-329e-8973-2114db6a501f | -14.3327 | -58.4614 | 2026-06-08 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 8b3bc828-0af0-303e-86ac-4b2e5dcfc776 | -21.99227 | -57.61787 | 2026-06-08 00:43:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a8fa6cb4-2faf-3468-b1dc-5b29a5cec597 | -21.99098 | -57.60741 | 2026-06-08 00:43:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 27.1 |
| f856d8c4-5a6c-3e40-a613-e4a5ec19bf71 | -21.3105 | -50.37573 | 2026-06-08 00:43:00 | TERRA_M-M | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 476da8de-7d24-31fb-b087-792d7afaa30d | -20.09642 | -57.21672 | 2026-06-08 00:43:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38831fe5-0c96-36fb-99b3-137eda674c3b | -14.34 | -58.470901 | 2026-06-08 00:45:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 726c2344-97d5-3bce-afc0-ca8f3cbebb8a | -14.3465 | -58.453499 | 2026-06-08 00:45:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad1e5f0-6f60-3a60-8710-01d1566102d0 | -14.3351 | -58.448101 | 2026-06-08 00:45:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa7c799f-3f45-3637-a501-ec4e99a27089 | -9.3014 | -48.958599 | 2026-06-08 00:45:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37e3a61f-937d-355f-948a-fd4feebd9f0f | -11.7423 | -57.8218 | 2026-06-08 00:45:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91342d33-34e4-358a-bd95-fe0e152deacf | -14.3498 | -58.4687 | 2026-06-08 00:45:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 715fa3a2-bd8f-3b80-9e25-452a31f75fc3 | -21.9965 | -57.603802 | 2026-06-08 00:45:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 29f61ce8-3443-31cc-ad11-03b39ebb2cbd | -14.3482 | -58.461102 | 2026-06-08 00:45:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3fdc5b6-817d-397e-b5bb-3ee961b5a872 | -14.7341 | -52.677101 | 2026-06-08 00:45:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f40e3bd7-d023-30bb-a758-e5038c8813fd | -21.994801 | -57.5952 | 2026-06-08 00:45:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d9437063-17be-33ef-9988-64c29c1f8292 | -14.732 | -52.668201 | 2026-06-08 00:45:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff98c122-8e5f-3403-ac97-273035faa6b8 | -14.3384 | -58.463299 | 2026-06-08 00:45:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c73a209-db82-33fc-9cf3-e007dd244fc4 | -11.5926 | -58.499199 | 2026-06-08 00:45:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8eb083f6-c491-39ba-b0ac-4a48c5719330 | -14.3367 | -58.4557 | 2026-06-08 00:45:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 16c0023a-30fa-3ed8-921c-465b3ce6bfc5 | -10.8504 | -53.7355 | 2026-06-08 00:45:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76e4488c-5e0d-3066-b9d5-df2baf49cfdf | -14.73724 | -52.67455 | 2026-06-08 00:45:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 425516ef-e62a-39b5-84b5-22705fcf9890 | -14.34042 | -58.4712 | 2026-06-08 00:45:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1b14a297-a9e7-39b2-b56c-5da60ce814ae | -14.33914 | -58.46153 | 2026-06-08 00:45:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5bd90152-8102-3ee7-bc1d-10ba9dc25aa2 | -14.73936 | -52.68789 | 2026-06-08 00:45:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a3934dc6-94f8-3e32-99e6-561349a23714 | -14.33785 | -58.4519 | 2026-06-08 00:45:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 37bc432b-2dcf-358d-9162-92ec0fa15a2f | -11.5846 | -58.50923 | 2026-06-08 00:48:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f6a64611-6913-3215-871f-1e1bff5bde0b | -10.85527 | -53.74439 | 2026-06-08 00:48:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e1bb6a0a-840a-3847-959a-1cdc9e5dde74 | -11.51183 | -56.12137 | 2026-06-08 00:48:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3dc3aafd-ad79-334a-9a5b-8691c24ac21f | -11.89917 | -57.76888 | 2026-06-08 00:48:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d02e0c1d-5806-369c-9300-c169fc23c8f4 | -9.30729 | -48.97686 | 2026-06-08 00:48:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 80f0c979-e46f-3693-8508-39ed1abc8261 | -11.73266 | -57.83266 | 2026-06-08 00:48:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a65e1bce-0c3d-3b9d-8a4b-bfa37e27e0d9 | -11.74149 | -57.83138 | 2026-06-08 00:48:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9cbe7b1b-0d56-3c00-90ce-94eaa05c338b | -10.84481 | -53.74605 | 2026-06-08 00:48:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 55ade9c4-f04c-3e52-b1c9-81cc46df6215 | -6.57387 | -51.1164 | 2026-06-08 00:48:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e6361ef7-e19e-3c29-a69c-b70f72a92b77 | -14.3327 | -58.4614 | 2026-06-08 01:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 1701af7d-19bc-37e3-b924-49637bc3d55b | -14.3327 | -58.4614 | 2026-06-08 01:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0d5bb293-54ed-3fd0-aae6-37cfa2bb4af8 | -14.3325 | -58.4814 | 2026-06-08 01:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 35b5d814-5bd7-35b1-8060-17c7dc0d70eb | -14.3327 | -58.4614 | 2026-06-08 01:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 9f7ca103-d732-3c7e-8979-d671114743a5 | -6.97889 | -42.88566 | 2026-06-08 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5a572699-7e83-322b-8d87-90507c1c5d86 | -5.51961 | -37.48548 | 2026-06-08 03:25:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9ad89ec-bde2-3689-891f-ba478d3515de | -5.51907 | -37.48854 | 2026-06-08 03:25:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2d6bb31-7fc1-3163-ae3f-4eac8eefc9a1 | -6.98186 | -42.88663 | 2026-06-08 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b3532690-8742-329c-a9a3-1f5f228d8c34 | -6.98017 | -42.87912 | 2026-06-08 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2b9692a5-7f0d-3f49-8034-283353a9bf2e | -6.98311 | -42.88001 | 2026-06-08 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c9d644e0-8d9d-3009-a900-88bb56f71a77 | -9.49206 | -40.38823 | 2026-06-08 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9554004c-f0d5-3ce7-af16-adba9463b3a9 | -11.0266 | -44.3236 | 2026-06-08 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90ceb82d-fa55-3141-b28c-60578d556d4b | -6.98595 | -42.88698 | 2026-06-08 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 66052d01-68b8-3e5c-873a-12b0c606eddc | -11.02813 | -44.32326 | 2026-06-08 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2a60168-f640-360e-a78a-2ac88e3d9151 | -11.0281 | -44.31644 | 2026-06-08 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9c0e512-8973-3a16-9a69-92ef0235ba16 | -9.49679 | -40.3863 | 2026-06-08 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 168c5800-080a-3400-9dfc-904383c9fe69 | -9.49285 | -40.38401 | 2026-06-08 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b55d8cc0-5d9c-34a7-b549-2e08942c54f3 | -9.49866 | -40.38525 | 2026-06-08 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b64ebad-3fc1-3f75-a9ef-a002a255ad16 | -3.49109 | -48.03848 | 2026-06-08 03:45:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a388b32d-7f36-32e7-89e7-27a47921e5f7 | -4.5232 | -37.72738 | 2026-06-08 03:45:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ffd4d343-0a12-32bb-bc8b-3fce62a21230 | -3.49228 | -48.03163 | 2026-06-08 03:45:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5813342e-17a6-302c-a237-d551a7162025 | -3.49818 | -48.03914 | 2026-06-08 03:45:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 444d7cf9-e151-3839-aea3-bce04d363192 | -14.29618 | -49.24466 | 2026-06-08 03:47:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a1521e4-43b9-3c5a-a82d-7b314979728e | -15.52582 | -42.63787 | 2026-06-08 03:47:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3c6ef863-3ae2-3e62-917d-4749bea9e60e | -10.14031 | -47.64096 | 2026-06-08 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47e8da30-38be-3abe-81cc-bcda4ef4dc55 | -11.03437 | -44.31907 | 2026-06-08 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 259a8ef2-1ae8-3aa0-8e20-12425d0cf276 | -11.02948 | -44.31811 | 2026-06-08 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86f425a9-0cf8-3e1f-9652-3eddb9f60280 | -17.16215 | -45.06192 | 2026-06-08 03:47:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb2509d2-845f-3724-91de-747f73e3e775 | -10.14647 | -47.6421 | 2026-06-08 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 93e46dd9-029c-3830-a387-b7a5a71a2cfe | -7.22407 | -46.43362 | 2026-06-08 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7f49398-f326-3b94-b377-088604d1b6a2 | -5.51925 | -37.4852 | 2026-06-08 03:47:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 46b30c74-d58a-3f16-b2f5-d19d7a177b10 | -7.89767 | -47.09548 | 2026-06-08 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8594c998-8f10-3fb1-904c-c4341f03f8be | -16.72314 | -41.49693 | 2026-06-08 03:47:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8f2d027-7a9b-358a-ad24-f3fd2d990722 | -10.14606 | -47.6389 | 2026-06-08 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3e58d1bd-6e4c-35f8-9542-db11f0043de6 | -7.22636 | -46.43324 | 2026-06-08 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7e5f3f4-fefe-32d7-a93c-ecacdacb167e | -11.02459 | -44.31717 | 2026-06-08 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 945290f5-9d49-3e5c-af7f-c251ccf79605 | -18.24316 | -42.75373 | 2026-06-08 03:47:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9b64c742-c8d7-396d-ad88-d8810bae8c7e | -7.2255 | -46.43783 | 2026-06-08 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 400eaecc-3a6e-3ed9-9003-3427749e3028 | -9.30555 | -48.96965 | 2026-06-08 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58bc729b-e007-3a5e-829b-83ce1e7b7a35 | -7.84656 | -46.19243 | 2026-06-08 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e241894e-4849-304d-9e10-7cf02ae9b95a | -5.49403 | -37.24382 | 2026-06-08 03:47:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7eb459df-fcf4-3336-afb4-93fa2cf6c1d0 | -14.30358 | -49.24078 | 2026-06-08 03:47:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8eebe1fd-2782-342f-9751-52671852c8bb | -7.90478 | -47.09173 | 2026-06-08 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c10830ca-00c4-3c5d-ac8a-007ca2b6b4ea | -10.14559 | -47.6467 | 2026-06-08 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3f77706-94e2-3e98-aaa3-bb5afd948cab | -17.7263 | -42.68778 | 2026-06-08 03:47:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ff9e4781-1fbb-38f6-9770-0c67bcbd1300 | -10.14516 | -47.6434 | 2026-06-08 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 30b9b9c4-d6f6-3811-afe0-eb17a9b5002a | -7.39787 | -45.24831 | 2026-06-08 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d523dd47-d0df-32f6-ada4-b4d22f493b76 | -7.84731 | -46.18842 | 2026-06-08 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a3b6b62-cf04-34dd-8149-9bbf64475159 | -11.43954 | -46.6769 | 2026-06-08 03:47:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80e565fe-6869-3efd-b25c-9a0c1f3b8624 | -16.72112 | -41.49328 | 2026-06-08 03:47:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb0fff64-65e8-3e37-9059-0564b7afdbe2 | -14.30253 | -49.24573 | 2026-06-08 03:47:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62edb367-24db-3453-a6b8-2c0fcbfb190c | -12.82153 | -38.41906 | 2026-06-08 03:47:00 | NOAA-20 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c51907e3-6287-38ed-ae18-e4de41626892 | -12.04972 | -45.57113 | 2026-06-08 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a80bf56f-5b1d-33ef-bb49-97dfa1569871 | -12.49182 | -46.27747 | 2026-06-08 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5984f5c2-0887-30f5-ad4e-0cc97b679897 | -12.04401 | -45.57311 | 2026-06-08 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87267261-ccf5-3d88-9f12-efcfa79c5dac | -20.32324 | -47.7353 | 2026-06-08 03:49:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29ef349d-b808-3cff-ac40-f2ef947717bf | -12.06733 | -48.42472 | 2026-06-08 03:49:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e057736b-6325-335e-8770-673fcacdbf30 | -12.04387 | -45.57332 | 2026-06-08 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91b2ddc9-b909-3654-8d0f-4de8c837d627 | -12.32015 | -46.07661 | 2026-06-08 03:49:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87ba16dc-dbc4-3628-bff5-33c041a03de2 | -18.90968 | -47.43162 | 2026-06-08 03:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README2.md)
