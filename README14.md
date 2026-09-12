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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c138febd-c225-35ee-ab5d-000d565df2ca | -11.41131 | -43.9441 | 2026-09-12 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 466ac52e-b524-36a0-946c-cbe986ffac48 | -12.12975 | -48.96247 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 78aca736-c80a-3e2d-955a-94bf2e377fd5 | -13.3781 | -48.01366 | 2026-09-12 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8636badb-1cad-3a70-9bd1-433f844799fd | -14.91181 | -44.67363 | 2026-09-12 03:49:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ddae1eda-ab85-3849-a83c-7c3974cd49cd | -14.11876 | -44.21462 | 2026-09-12 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63d98737-abc8-37ec-bb42-2ba2acff5cc5 | -12.13291 | -48.9711 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ef5b8ae6-23aa-3e59-9f62-7feb20648d47 | -10.55105 | -45.21486 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ade6414-0b6b-3201-9f2b-b7b2747670b1 | -10.46476 | -48.64612 | 2026-09-12 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d1aceb3-08a7-3457-9e37-b2814a65e4af | -14.3925 | -43.78654 | 2026-09-12 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5ba03a4-6225-32d6-a453-8ed27c674c1f | -10.63787 | -46.11687 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0ddaf85-3a6d-38e4-a043-09a70348e141 | -12.37325 | -39.59142 | 2026-09-12 03:49:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eda85dd9-828e-37e6-a0fe-5d887f0e3fc7 | -8.03568 | -43.85998 | 2026-09-12 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 66432e4d-f051-30e6-81f7-e8bd145acccb | -10.47252 | -48.64451 | 2026-09-12 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f62698c-419d-3b15-8e9e-007b67c43934 | -10.63103 | -46.12283 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e09c340a-628b-3a9f-b300-6e312f782ffe | -11.37334 | -46.82695 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2beb8084-d30a-3f4a-9cbb-b897fa73f373 | -10.55345 | -45.20196 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 123330e5-cbcb-3016-9925-f76b51dedde8 | -7.96238 | -44.01491 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6166a32f-de56-35f9-8822-458ce6896fb2 | -3.66236 | -41.15973 | 2026-09-12 03:49:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e066df0-7e72-33c9-8446-3b4e200b9734 | -10.22043 | -45.18934 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f660b8ab-fdbb-366b-8b7a-91cf245fa531 | -11.27754 | -44.18695 | 2026-09-12 03:49:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28f6331b-4516-39e5-afce-d035c1262e2f | -7.60232 | -46.12125 | 2026-09-12 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfce62ef-21cf-3fe1-b535-72e01575f2d6 | -12.1298 | -48.95365 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bdb29116-817b-3011-a2f8-179e7e1d7488 | -9.52531 | -40.33389 | 2026-09-12 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 70a5450c-d186-3db3-bdfa-0c596949eada | -13.37518 | -48.01798 | 2026-09-12 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 104d4402-c813-3f18-99c1-2a3d88b4c565 | -7.95844 | -44.00808 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bfa8fc4-8040-3723-91d9-2987e58f5602 | -11.83656 | -39.18104 | 2026-09-12 03:49:00 | NOAA-20 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dce6559b-462d-3168-9e20-b5f453cd53ce | -12.63904 | -47.08841 | 2026-09-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62e49695-2806-3697-aaae-066848af019e | -9.7815 | -41.99859 | 2026-09-12 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3915a1ea-b159-30ba-973e-5df69cfc9b8f | -9.70383 | -43.45999 | 2026-09-12 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fd2945fd-4216-3395-bbeb-f9b3637941f4 | -7.96554 | -43.99705 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a641a46b-a907-37e2-9dad-1e6756c36fe4 | -13.65311 | -43.92942 | 2026-09-12 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b6044fd-46a0-35fb-afd5-8de66cd45ecd | -10.04652 | -46.27031 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53212ffa-ea9f-3b09-b4a3-41f27e7c232d | -11.36653 | -46.80111 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0548e516-eadf-3bd9-a2b4-654513300547 | -12.63824 | -47.09236 | 2026-09-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c5b37ea-bbfc-37a7-a15f-d9959492543e | -9.67356 | -46.01317 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9131292a-67c1-301d-8a41-049bc7fae254 | -15.80039 | -43.28113 | 2026-09-12 03:49:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13dad0a4-0f59-3713-93f5-743ae70e4263 | -7.95949 | -44.0021 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86e7c9cf-1c4f-3e8d-9d3d-60a45b256daf | -10.04733 | -46.26595 | 2026-09-12 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef5fa91d-c1d5-3720-ba9a-e3316e6f22bf | -11.35157 | -46.28325 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f7bfd55-4852-3937-b430-294c28385044 | -10.2767 | -45.26554 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1abed87-4954-313a-876d-f00475370b0a | -2.46508 | -48.04399 | 2026-09-12 03:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 95135380-20c0-3f48-ac75-768c35c08e8b | -3.23315 | -46.94962 | 2026-09-12 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| e4d04ee9-e099-3d33-9169-12ed46e1ae7a | -14.67738 | -42.85177 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1e698cc-d362-3400-903d-628229e95347 | -3.15781 | -48.61265 | 2026-09-12 03:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d698861a-b38c-3cc5-9e4a-e6c8e5324d69 | -10.2262 | -45.18728 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d12597a-29e9-3fc5-b186-89c86641ef7d | -11.37564 | -46.82613 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1df84a76-98e0-3d35-b510-17f96fb30391 | -10.54528 | -45.21707 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d28161cd-2422-3057-9dfe-88c1f40c8286 | -11.36165 | -46.79598 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26321050-b3c6-3f00-b1df-b9a7b80c8b14 | -10.55683 | -45.2126 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c298af2-98fa-3f6b-90d0-e9fe708d2100 | -9.31676 | -45.6481 | 2026-09-12 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46af76ba-c2a2-3293-818b-a68f583b1724 | -12.12648 | -48.9701 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1fa48638-8048-3bce-963e-75d23fa97e06 | -10.55624 | -45.21577 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5003d8a7-5f7c-3e60-a649-43b5f665264f | -10.90751 | -47.83698 | 2026-09-12 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14026914-6652-3469-85b5-036e88e6eb35 | -15.44482 | -41.38472 | 2026-09-12 03:49:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8089261c-8966-3953-94a7-f66b67720eae | -11.80435 | -46.38454 | 2026-09-12 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caf420e5-78f8-3e61-bae2-2dabc5898860 | -9.51849 | -40.32779 | 2026-09-12 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 13c6e902-ac09-3eac-86bf-f8ec3145c632 | -12.44239 | -49.59029 | 2026-09-12 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d98154d-a9f7-39eb-a0fd-8cbd4fdabb1f | -9.32355 | -45.64199 | 2026-09-12 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c7721c4-1cad-303b-914a-fc5017eca560 | -14.91563 | -44.672 | 2026-09-12 03:49:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 050bc6b0-396e-37a4-b1cb-ebfbcb45d99a | -12.29333 | -40.56843 | 2026-09-12 03:49:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 401035e5-7503-39f0-b548-eb4adebc7190 | -9.93299 | -48.51875 | 2026-09-12 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c76ce3e0-8c84-3242-95ec-161d7617061d | -10.55741 | -45.69986 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ea77274-6dd8-3422-a274-1b3a77c4692d | -9.53942 | -45.45301 | 2026-09-12 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb5ada8a-f939-3479-a07a-29f8c2736221 | -11.36726 | -46.79731 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 622cdfa8-e642-3461-8529-63de909f7564 | -13.43653 | -43.81615 | 2026-09-12 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6950879c-3dc6-3e6c-ad03-9a674cc05a4b | -14.67465 | -42.84335 | 2026-09-12 03:49:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 742d8cdc-fb82-347b-81f8-a63a392e4b45 | -14.58236 | -48.83907 | 2026-09-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e96ca745-5a10-3651-bd56-f971cd2dfb70 | -9.54563 | -45.47951 | 2026-09-12 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd767474-f4a5-39e2-b4ea-8d1c46aa29be | -11.53374 | -44.89382 | 2026-09-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a95e3187-53cf-3c8f-b48e-d8c8b997b140 | -14.5814 | -48.84364 | 2026-09-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 732c04f8-dea2-381b-b165-57d7e331698e | -12.2 | -49.40067 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fa24c5b-3ba8-3bb0-9363-74a53cf46d39 | -10.55164 | -45.21169 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61a2af81-e85a-35e3-a5c3-b2591b1c30ca | -9.34814 | -40.63694 | 2026-09-12 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e28f4064-cc93-32a8-904a-591fdc86d192 | -9.69948 | -43.40312 | 2026-09-12 03:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8d77870-8f4d-3397-80f8-bb191a830762 | -10.46596 | -48.64391 | 2026-09-12 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4adcd3a3-a668-3435-963f-2eb57f17dcf2 | -14.91103 | -44.67104 | 2026-09-12 03:49:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e8dca32-c45d-3c2f-86f0-ebde4414e0e9 | -12.13311 | -48.97823 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 149f0072-e799-3014-a4e6-7414f377c0c7 | -12.43753 | -49.58955 | 2026-09-12 03:49:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3c8a443-20c9-3ff1-844c-8dbc94cd249d | -10.22564 | -45.19029 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d15d663-2f95-31c8-b389-8d92154a9979 | -13.37631 | -48.01255 | 2026-09-12 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92df613b-af93-354d-bee7-53bfd0d94b50 | -14.83547 | -48.17246 | 2026-09-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70d7687c-343b-3ab4-a034-082dc07ae099 | -9.52613 | -40.32913 | 2026-09-12 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 2a2a4bfd-028f-3ee8-a244-eeeb51e406db | -9.31285 | -44.35308 | 2026-09-12 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31b4c297-e16b-3ce6-856b-a3b57928ebf1 | -3.77453 | -38.47266 | 2026-09-12 03:49:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 421075a4-f726-36f1-a07b-5aade684e86f | -11.3135 | -37.90075 | 2026-09-12 03:49:00 | NOAA-20 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c4d92fc-ebc6-3319-93e9-257cccde3abc | -11.35061 | -46.2861 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edc5075b-f9a6-36c7-a1ed-ac55187c9a6a | -10.62958 | -46.13063 | 2026-09-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc6a3b5f-2a3a-3463-9a10-4110c6e1aff4 | -3.22666 | -46.94833 | 2026-09-12 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a3bc677e-ab28-3cf1-8536-a152f06fb511 | -13.37699 | -48.01919 | 2026-09-12 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f908af7a-d28e-335c-8009-9d677e98c342 | -10.47222 | -48.64209 | 2026-09-12 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c1bc52f-9c85-3624-9fcf-0bbfd8c6b9e0 | -11.37252 | -46.84193 | 2026-09-12 03:49:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 59e603ad-4a2a-3961-bab4-6a24078f0435 | -10.55285 | -45.2052 | 2026-09-12 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e57fae36-45ca-34da-a5d1-eef0caa800e7 | -10.22068 | -50.37461 | 2026-09-12 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 237a47ae-365f-3eb2-b1d3-f95cdb6c4086 | -8.38852 | -46.30161 | 2026-09-12 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 378d98d8-8f81-3b31-852f-479c28dabb5d | -12.12807 | -48.97052 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e80acd0-2e5d-3701-899b-014d01031520 | -13.48907 | -41.33627 | 2026-09-12 03:49:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62bd5352-1ee7-3468-ac80-a68033345c1e | -13.46273 | -48.50615 | 2026-09-12 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6f370d3-c5c5-35f8-ba8c-4407d0e18238 | -9.78573 | -41.99933 | 2026-09-12 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54dfddd0-b0c6-3388-afa7-4640ef4bc582 | -13.65653 | -43.92789 | 2026-09-12 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 150e0dc7-0d25-3c79-84c7-48610113a974 | -12.7388 | -44.73764 | 2026-09-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
