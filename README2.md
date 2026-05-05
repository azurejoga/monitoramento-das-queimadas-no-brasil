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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6de1e0da-467c-3af4-98a4-857fdb08309f | -13.92746 | -47.28089 | 2026-05-05 03:32:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f9db3de-0b04-384a-a4fb-0cdb7515e5f2 | -14.07272 | -47.6338 | 2026-05-05 03:32:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f79b7293-efa1-3f2d-ae67-86b37e2bda71 | -13.43514 | -43.84321 | 2026-05-05 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9d371c1d-8e14-323a-a255-6bfbf9917147 | -13.92777 | -47.28157 | 2026-05-05 03:32:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 637ea288-297d-3517-a65f-8ed784219d19 | -11.13027 | -45.12103 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5060098f-c48a-3710-a58e-f4b9839cce0e | -11.12635 | -45.12874 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5c9e5292-1460-3e3a-8738-087be3180ec3 | -11.12967 | -45.1453 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c9ecd1b6-fa68-34f1-9748-8c309385416c | -11.78771 | -43.61732 | 2026-05-05 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22688b8e-911f-329d-825b-02794842ecf0 | -11.12925 | -45.12601 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d689defe-6c9e-3f36-9988-d2f62db4272f | -11.12733 | -45.12375 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e35bdea-5a15-34ee-b1b7-4dd314450521 | -13.43764 | -43.84454 | 2026-05-05 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7afd488c-74ac-3596-8dcf-7891441c655a | -14.03494 | -47.6469 | 2026-05-05 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7214f0c3-af3a-3884-b661-b16c120a278b | -11.96945 | -43.9754 | 2026-05-05 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e804f21-feb6-3037-a107-d6bccbf0b6ca | -17.80236 | -46.70896 | 2026-05-05 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15b90a01-a432-3d87-9e89-e3befb660346 | -21.53846 | -47.13717 | 2026-05-05 03:34:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a291994b-e4af-3caa-b088-8cc0b4d6f40d | -21.5374 | -47.14168 | 2026-05-05 03:34:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7555f2-b65a-3c33-bb5c-6e458c640239 | -21.70133 | -48.42093 | 2026-05-05 03:34:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0fe02016-67d8-313f-83fb-243d813d7ef3 | -21.53256 | -47.13585 | 2026-05-05 03:34:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e510d12-a859-3ba0-ab3a-f1b103697d9f | -21.53149 | -47.14038 | 2026-05-05 03:34:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2644ee3e-dadf-3467-a72d-510eea02ba28 | -22.48692 | -41.9642 | 2026-05-05 03:34:00 | NOAA-21 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2b20916-11d7-33ec-be6c-aea244e8edda | -22.70022 | -43.36386 | 2026-05-05 03:34:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 44aac556-5726-3673-89fc-72f7fbaa1829 | -21.85743 | -48.071 | 2026-05-05 03:34:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 123e3b10-2423-3b6f-a905-9a8286eaa43f | -21.53398 | -47.1405 | 2026-05-05 03:34:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27ed6f2a-02ce-316d-9e10-885e993f4dfb | -21.7058 | -48.42037 | 2026-05-05 03:34:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 730ae0d1-9867-378f-a4fc-45c365d09429 | -22.48774 | -41.95999 | 2026-05-05 03:34:00 | NOAA-21 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b0db2a8-fe38-37d2-8588-be5ad6e16b2d | -22.03903 | -48.36514 | 2026-05-05 03:34:00 | NOAA-21 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 678e8af3-f938-3ca6-a673-3f9dcc7bc206 | -22.7015 | -43.36074 | 2026-05-05 03:34:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ec2e3ac0-f001-3295-b33b-729ea6a73d8a | -17.80131 | -46.71371 | 2026-05-05 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3f0b1c2b-e051-38c4-bf41-d6dcfc9e6cd6 | -21.70754 | -48.42281 | 2026-05-05 03:34:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f92a565-cf36-32b1-8789-0f09ecc3e913 | -22.74516 | -42.25191 | 2026-05-05 03:34:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7265e0bd-0ec1-3e03-8857-90a01dda8bec | -21.70458 | -48.42556 | 2026-05-05 03:34:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3dbf76b-4b2d-3bdd-af91-38dfbba9f1e7 | -21.8564 | -46.97486 | 2026-05-05 03:34:00 | NOAA-21 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b21a9484-f313-329c-a5b1-c2cf1baaaf80 | -22.80078 | -49.3366 | 2026-05-05 03:36:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23d25bd8-9e34-3f26-95ef-1e894f500a49 | -22.67601 | -47.47778 | 2026-05-05 03:36:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df662bcc-414f-38c2-b342-fab953e8237e | -22.79936 | -49.34228 | 2026-05-05 03:36:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 053f71c5-a2df-332e-b181-3454bd0f31e8 | -22.67714 | -47.47285 | 2026-05-05 03:36:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8650f266-ecad-3705-81d2-fc831bc6d25b | -23.03957 | -47.7413 | 2026-05-05 03:36:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 844f5a49-491f-3e61-952f-d35e3efc29a9 | -10.20978 | -44.76351 | 2026-05-05 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b916040-42a4-3da6-976b-71bdaa828236 | -8.78328 | -44.82452 | 2026-05-05 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fa048e7-a50d-3f63-b4d0-2d3e991f303a | -11.79387 | -43.61682 | 2026-05-05 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88fb7867-106c-385d-bfe8-33349bf0968f | -7.51358 | -49.42651 | 2026-05-05 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af8600b1-90d7-3892-b3e6-4adce530294b | -8.20739 | -47.99135 | 2026-05-05 04:04:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88ae46b9-9986-3338-98be-06ad0850b3a0 | -8.2068 | -47.99465 | 2026-05-05 04:04:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 412f77b1-2b2e-345d-9672-77e75551b0ff | -12.27055 | -43.50581 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 838d3ae3-a508-3302-84b2-18ed857d5001 | -12.27348 | -43.51094 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3f9cb8f6-e9e1-328f-886e-d04a7a132c5d | -11.7909 | -43.61158 | 2026-05-05 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9565b6bc-c100-3878-a300-6fae4bfe883f | -11.96515 | -43.97557 | 2026-05-05 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4812284d-353b-31f7-b1fc-87fa6ce23db1 | -11.79012 | -43.61615 | 2026-05-05 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b17b041-ec46-3834-b9e6-950be82ebcc5 | -11.78637 | -43.61549 | 2026-05-05 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82ae1584-cd98-330f-a4ed-728d0a6e0b6f | -12.27425 | -43.50647 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c6038a62-be57-33c5-adf2-5bc0196ba1e4 | -11.78183 | -43.6194 | 2026-05-05 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 705fd463-bff4-391f-a059-4ef829224564 | -12.27503 | -43.50201 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3f50413-71d8-321f-9019-840ac569503d | -11.96688 | -43.97818 | 2026-05-05 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71d9ae26-1696-31c0-add5-9bd119bae0a1 | -8.89196 | -36.63879 | 2026-05-05 04:04:00 | NPP-375D | PARANATAMA | PERNAMBUCO | Brasil | 2610301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 192e2957-9625-3ec4-bbf1-77fe2fc6a11c | -11.29594 | -40.41388 | 2026-05-05 04:04:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e4182090-4ab9-3179-b2bd-66ca6df2107d | -9.46955 | -47.80032 | 2026-05-05 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d03ba0d6-5fb8-34dd-b2e1-fa544736f028 | -11.13401 | -45.14366 | 2026-05-05 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1b318205-5a45-33ca-ab3f-d2481ab1ce26 | -9.68187 | -47.0282 | 2026-05-05 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59101d8c-470f-3385-aa04-914341b881a5 | -7.51284 | -49.43058 | 2026-05-05 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1a99d0f-1749-3b00-917d-41696828e762 | -11.78934 | -43.62073 | 2026-05-05 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ca9a3ca-2051-3798-88ab-18ff8912eea1 | -7.51787 | -49.42578 | 2026-05-05 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4cecee9-2989-3c7d-a692-65851f989f84 | -12.26574 | -43.50154 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9256ac11-29fe-32d6-af80-dc83709bf01c | -11.61212 | -47.10451 | 2026-05-05 04:04:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db5012e2-17e8-3997-9009-e6d1778ed864 | -8.78375 | -44.8257 | 2026-05-05 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e986c4b-52e6-3ef1-81e2-f631192457fc | -11.61016 | -48.06089 | 2026-05-05 04:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f998cd79-1b70-3360-a45b-954d40f286d0 | -13.28964 | -43.96727 | 2026-05-05 04:04:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04c66489-d20d-33b1-a20f-567fdfe05b9d | -12.26763 | -43.50067 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32b1f2ef-eed2-3b34-b239-ad4ea7269a90 | -9.76478 | -43.90211 | 2026-05-05 04:04:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dd827f0-553b-3b46-a532-914dfcc733aa | -11.84277 | -43.9668 | 2026-05-05 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 441371ec-f62c-36a2-a333-766ea3aaa80e | -11.88397 | -43.81011 | 2026-05-05 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4c0caac-8f49-3168-9f79-5df8cd60f9eb | -11.12973 | -45.11965 | 2026-05-05 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9ed4565-7a06-3162-8004-913a706ef54e | -13.29045 | -43.96267 | 2026-05-05 04:04:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53eb827f-18c3-38b6-8f39-6dfd1f46a8af | -11.12984 | -45.14295 | 2026-05-05 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 64f33664-6d5a-3635-9c4f-fe1d812c3196 | -9.4701 | -47.79733 | 2026-05-05 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e84a25d-2b9f-3096-8008-8d2d73c663c4 | -11.12906 | -45.12338 | 2026-05-05 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61e94de7-11de-3a78-bf52-1ab33a7ce14a | -11.1284 | -45.1271 | 2026-05-05 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46f0adae-6d65-390d-bb7e-7bd6c5ce61ce | -11.94661 | -43.37798 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d874598-c7bd-337a-9273-a628a9c7fa43 | -7.87485 | -42.6883 | 2026-05-05 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2bbf4829-7fe5-3e90-aba0-dcb0d18d862b | -11.93746 | -40.00294 | 2026-05-05 04:04:00 | NPP-375D | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d1857df-7ad6-3007-b669-0be81e189309 | -9.68092 | -47.03353 | 2026-05-05 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fad251e-ac6b-392e-8f77-dc94c57db262 | -11.88539 | -43.80843 | 2026-05-05 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51fcf1be-2803-389b-b065-a03338cef3ff | -9.56714 | -44.57064 | 2026-05-05 04:04:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09180f51-34db-3922-b8c0-34b88012abbf | -9.67976 | -47.02952 | 2026-05-05 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e3cfda8-7621-3b08-a0e9-b587db9daeeb | -11.78559 | -43.62007 | 2026-05-05 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b0ee1f2-416e-3a18-840f-01a6c9fc7807 | -11.94955 | -43.38316 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e3809df-6fad-35e2-ba8d-dfb93c5b610b | -7.51124 | -49.42868 | 2026-05-05 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 007f5c08-ec97-3feb-9b7b-e95582606638 | -7.52595 | -47.17579 | 2026-05-05 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac0f058e-8dae-38bf-a7ef-dd4163f5a50c | -7.52089 | -47.17482 | 2026-05-05 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c00dc12-484a-34c6-9d84-09c8064948d8 | -9.57062 | -44.57507 | 2026-05-05 04:04:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2af5da27-86ec-32bd-9a35-17b0780ebcbf | -11.95031 | -43.37866 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fb4fea0-1a4b-3e4b-a681-a423f3c1b251 | -9.56302 | -44.56997 | 2026-05-05 04:04:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ef9068-4618-3278-9bb3-167f70709ff4 | -12.27133 | -43.50135 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f928732-c4e1-38be-9ead-cfe7b8024c8c | -11.61518 | -48.0618 | 2026-05-05 04:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a62a07c-ae15-3f20-987c-918cd31434e4 | -12.26685 | -43.50513 | 2026-05-05 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd48ac92-b53b-310f-a204-b096804cb424 | -11.13468 | -45.13992 | 2026-05-05 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6b20f2ff-09ce-3fd9-85ab-839e72c9af9d | -7.52142 | -47.17186 | 2026-05-05 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb287251-c78c-3401-affb-174ad9023149 | -11.61129 | -47.10113 | 2026-05-05 04:04:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cabc607-b5b7-39e6-9ada-46450647c2d5 | -11.96897 | -43.97623 | 2026-05-05 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b97feea2-c34d-3139-88fa-45f7fe21ff97 | -7.62243 | -44.11368 | 2026-05-05 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52b68d4b-aafe-3b50-995d-0e9e445fdb49 | -14.08271 | -47.79187 | 2026-05-05 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README3.md)
