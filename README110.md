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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9137e8a6-643c-36c1-93da-647e49e71d21 | -9.88297 | -45.84521 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b037b97-739d-3c48-a9f1-7f24554909d8 | -10.83248 | -50.51328 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4b75b37c-2e71-3780-aced-f2b36c8138a7 | -9.68661 | -46.56528 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e6cfcded-f6c9-328e-b420-3c2d38391172 | -14.18617 | -52.85479 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1646353d-bdaa-3171-aea4-8ba958b6aa25 | -11.21993 | -45.0463 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 34fa5a33-702e-37bb-b382-f820ac34236a | -9.94745 | -45.99792 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 032e2542-9309-3863-b452-4dfb14b27bfe | -10.86116 | -44.8004 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| a8c48b45-aed9-3c6e-ac8c-a2f86db979e0 | -11.83815 | -47.20469 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a44da441-1a51-3b67-ab5b-c49ab8582394 | -9.86508 | -45.84462 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 6f0f293e-f6ab-3c47-9181-3606225ed9d8 | -15.81916 | -56.42553 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 194f2176-fc82-3212-86cb-c6bab4d8a21e | -10.7884 | -53.97314 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e8d164b6-4f58-340c-8a66-de39c0d4cc21 | -12.38891 | -48.20057 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| b9981fb3-e1cd-373d-ab90-e3c9eea698fe | -10.17715 | -46.85214 | 2026-08-28 17:26:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad04b76a-7f38-3bcc-aa57-8b176a391dde | -14.89602 | -56.32463 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f0e13e3a-c963-31f0-8a1d-3a0a944a06a8 | -10.85393 | -50.21692 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0b834ee3-a5ce-30a5-892f-9c118c86570d | -14.36727 | -53.01624 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f9d42cbe-ce4a-3c55-a268-8bffe6f7353e | -10.33213 | -45.35665 | 2026-08-28 17:26:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c7cacdf-ad55-314d-8fc7-3f889b9c1137 | -11.24105 | -45.06056 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9244706f-46c9-3fa0-987e-be44b3fd91a6 | -14.80977 | -43.56387 | 2026-08-28 17:26:00 | NPP-375 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 585d1dcf-3f5f-3a3e-8659-2e71917589e1 | -15.34559 | -52.83364 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77a9cfc8-029e-3c8f-8aa9-8c3973261ed4 | -12.19725 | -50.5541 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 969d1dcc-5162-38d2-be6b-33955143e07c | -14.11017 | -42.62224 | 2026-08-28 17:26:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 5dd9639d-3a1e-37e5-8392-568709eaf0e1 | -10.88622 | -50.50394 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e5b25fdb-3a68-3612-bd25-9cf997c4577d | -13.65217 | -49.01349 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c4752f05-d970-3e94-a21a-a218b5512de6 | -11.83312 | -47.20578 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dbf9f1b5-0cbc-36e4-8c75-1b5c3fcd409e | -14.41238 | -52.58317 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 401dcdc1-a91a-3e97-9b94-f109c2e035e7 | -14.17589 | -48.7686 | 2026-08-28 17:26:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2fa8fe9f-b0eb-3010-8144-8be9b8fc9e10 | -14.92374 | -41.26482 | 2026-08-28 17:26:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| a26ecb13-52f4-3d44-870d-35ce6775babe | -14.41435 | -41.21772 | 2026-08-28 17:26:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| c1cb50ec-b89a-30b2-a6b3-8d2c2e29c203 | -13.42016 | -51.76936 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1927f3c7-f159-3a67-ab49-257a208bf7c1 | -16.50476 | -54.44101 | 2026-08-28 17:26:00 | NPP-375 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 02fbde6e-d88d-3687-a276-d2399b5ad9cb | -13.88609 | -53.244 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 8dde1004-0941-3fe1-a6f8-1b27b29dbac0 | -14.59857 | -40.59169 | 2026-08-28 17:26:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 9e7429bc-17b2-321b-b243-a6b294691fe5 | -10.86623 | -44.80341 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| fb810e30-6ddf-3f80-9acc-909afd3c328e | -11.83271 | -46.76989 | 2026-08-28 17:26:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4e67c5f-2d25-34a2-8c68-5fd975002f3e | -11.19408 | -55.08265 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c550e6ce-c0ad-3a1f-b4cb-a357da89665e | -11.37217 | -45.14243 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 33395baf-3abc-3d1b-9522-93d68a245a13 | -13.31192 | -46.92521 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| abb63b90-726f-36d2-8459-7ce9265b0aa3 | -11.24518 | -45.05064 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e2efb2cc-40a1-3a49-a2a7-f652275f0544 | -14.88598 | -52.62994 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 39184ad3-37fc-3c36-bb08-f026d7132a3f | -11.37288 | -45.14618 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3050c091-32f2-3509-8285-323d670bf8ac | -13.4636 | -57.04543 | 2026-08-28 17:26:00 | NPP-375 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 5bfebc19-745e-3e19-a17b-f8b82f892fce | -10.69314 | -48.21676 | 2026-08-28 17:26:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd36fb16-4a58-367a-9557-9dadb4f52510 | -15.90308 | -56.23542 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e5671e63-541a-350d-a14f-e29a4fde1c84 | -10.33435 | -45.36046 | 2026-08-28 17:26:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c9ca535-e190-3e27-b1e1-5a46adb01656 | -14.22594 | -53.3743 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 01151e76-a4df-3869-abe4-ef15b9e9741d | -12.06042 | -47.15473 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9b2edf9-3f1e-3fb2-b1e7-96bd19782ee6 | -11.58269 | -45.52261 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| dbe79196-8e2c-36c9-a369-d06b9d24235f | -13.42621 | -51.77032 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8a4a68bf-e059-3124-a7b4-cb4a65ee6fd3 | -10.46011 | -46.19132 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 179.4 |
| cf3b6b67-7742-34d9-90d2-309d82ddcd7f | -14.20751 | -45.28677 | 2026-08-28 17:26:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dcdd6f52-20ff-3f2f-b2c6-a75578868354 | -16.583 | -49.78606 | 2026-08-28 17:26:00 | NPP-375 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9eaa6d86-aeae-34f7-ae68-f241b36f453a | -14.88273 | -52.61028 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 081836d0-9cbe-3eaf-b325-462d4fc51114 | -10.85935 | -44.79999 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 30bc5b68-cb8d-3d6a-b98d-76dfd8debe49 | -13.65479 | -47.74206 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9351cfc5-a716-3464-bf5e-833296708621 | -11.24957 | -45.07286 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e20849b2-b883-3634-9c28-ffde6691a42c | -9.86472 | -45.8458 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d559b419-7b00-3953-af61-76161d93fd55 | -14.61287 | -53.15261 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c6009934-5ff7-3439-9de9-ec51b0ce34d3 | -12.57345 | -48.48719 | 2026-08-28 17:26:00 | NPP-375 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e5964ea3-974e-3af3-8f7d-225948092a79 | -10.4608 | -46.19505 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 406905ca-535a-3140-8caf-26ae6ddeabbf | -11.77154 | -54.51513 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dfbc5eec-8ee7-3f5e-a25b-3188318f12f2 | -10.92792 | -46.63061 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5b531d2-5952-365b-8820-bab0e8f74968 | -9.99937 | -45.57883 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 991f491c-158a-3505-83eb-37280e3d27ff | -11.9633 | -45.50709 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d523843a-b126-3138-92ee-a54a9c714fb1 | -13.55162 | -52.61536 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0529b42c-89e2-3007-abd0-c4bf7425c676 | -11.70921 | -54.54431 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b107bb1e-99eb-3195-8d90-d7ccdee340c9 | -11.28048 | -54.03584 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 9dab15c6-7f32-3396-8d3e-2bf59b93e783 | -10.33304 | -45.36128 | 2026-08-28 17:26:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3bf0988-0565-3e57-9595-9b33f0cbe7d6 | -14.18901 | -52.85026 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 56e2caee-4a92-3813-90b7-2b41535de492 | -11.34423 | -48.39649 | 2026-08-28 17:26:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0a6b2eee-e492-3155-829e-f048d993e61a | -11.21315 | -53.98893 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 69467d1a-b3bb-3197-9c5a-032d098e2d73 | -14.43121 | -52.58794 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97d80cf0-0e5f-3000-ad33-b6485885cb1b | -15.47126 | -53.96613 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69558378-0a68-3add-ad55-f04048905b84 | -13.32917 | -46.93413 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f0ef1e32-9ee2-3fef-b848-38e97e53b53e | -14.5493 | -53.30418 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 154cb679-4ba1-3463-bba1-761990d2c723 | -9.65649 | -45.71906 | 2026-08-28 17:26:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1777ccc9-f0f5-3a12-871f-7d51285987d4 | -14.90881 | -56.31465 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| d62929af-e892-3e65-ae1a-17d8b54e3eea | -9.84057 | -45.87489 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 61fefe71-dbe0-3a10-9b69-b3d8d1cf8e93 | -14.19818 | -52.8406 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ee43603e-f0c8-3585-b086-c3d5a8d6581c | -11.02421 | -49.66661 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f6f69f7e-1f27-370a-a42c-0c6ec4a7d48f | -11.01379 | -49.63354 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| da67f5fc-5336-3e65-b20c-b98573ecf3f5 | -14.23238 | -51.7629 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4ba50afe-9729-347f-b139-4e567ea47f9c | -10.99725 | -49.64066 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d44db51d-3112-3071-b50b-b5d768d76902 | -11.22406 | -53.99105 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9ad91137-ed6f-38ed-9d72-97e396620e76 | -11.57623 | -45.51963 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 55dea206-0336-3832-9cee-3842582989ac | -9.88382 | -46.35081 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c351cedf-88e6-3a2d-8f9a-a1847c88bc0c | -11.37228 | -45.1482 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a15a31b9-2f6f-3494-85b6-600257029186 | -15.02354 | -48.15262 | 2026-08-28 17:26:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 582bb26d-8acc-3caf-b86f-556fefab584f | -14.22294 | -45.24986 | 2026-08-28 17:26:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5258d76d-1d28-32a7-a80b-054b9c59c1b5 | -11.31914 | -50.69874 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f5ef16e5-e30f-3ff4-a9a1-a6e9a11a3f94 | -15.72331 | -48.25707 | 2026-08-28 17:26:00 | NPP-375 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 48ea17f5-1064-39d1-8529-3136fad1bca2 | -12.57801 | -48.48619 | 2026-08-28 17:26:00 | NPP-375 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 065a4986-dbcc-3ba2-b481-ff05caad9a29 | -11.61008 | -46.73257 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d550c1e4-5048-3124-887f-4b1cbcd229db | -14.89995 | -56.32782 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd0e7436-6f9e-3767-b558-0b47aa639338 | -13.42754 | -51.76807 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| db0a8509-a353-3500-b145-94522493d45b | -11.22241 | -45.04625 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| de084a99-bf17-35c1-9146-e7727a04c733 | -14.48969 | -52.13736 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c3543b8-b591-3147-9dc1-afd9a9026521 | -11.25097 | -45.06834 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 251049ae-e555-376a-b2cb-eaea7d35b79a | -15.34966 | -52.83688 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8b2e302-623a-3d50-81d9-dc9bf65f45f4 | -11.22629 | -53.98292 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |


[Clique aqui para ver as próximas entradas](README111.md)
