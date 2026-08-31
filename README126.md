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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9519cb0d-2ace-3b53-a13d-da3a8af46556 | -12.1736 | -50.52465 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a73a50fe-25ef-3a06-8fe8-cab1c46f8c93 | -9.65006 | -46.05656 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 016eca4b-4173-344f-8158-7d2c31c215c7 | -11.52341 | -46.94517 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48b45449-b771-39c1-8258-3fa0d471fb8e | -11.7131 | -47.64551 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d1b5d419-6753-30dc-90dc-9e4680c9123c | -9.216 | -51.58075 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1eab5457-0940-3247-8737-ff711a3f8211 | -11.22234 | -45.10702 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0cc90f1d-bf7f-312c-963f-60c704e73999 | -9.66117 | -48.2789 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b9940b80-7410-3e93-853c-1780c85facdc | -10.82251 | -50.68409 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 60f7b2bd-8895-33d3-b086-69b43925764a | -15.01713 | -52.75991 | 2026-08-31 16:30:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b36e89e5-1eff-36a7-ad7e-451ebebc86bf | -10.35552 | -49.97892 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| faa795b3-a89d-3253-b5f1-24965c417c24 | -11.91477 | -45.05777 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b4811b7-02c3-3274-a447-c55b4f6b333c | -11.25284 | -51.2581 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b2f35e40-0d8f-3a37-b241-d6fce743bfb5 | -11.26475 | -45.06081 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d34eb517-1a88-33cc-a58f-72c64d799255 | -8.38299 | -44.99931 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 6de0efdd-7323-3cf3-b482-aa49a90d1872 | -9.83128 | -46.35254 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| baa218f6-34af-3d67-b91b-33231910e16d | -11.06018 | -51.44683 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 10c1342f-b99e-365b-aa3b-7d7d8540d067 | -13.38623 | -41.35065 | 2026-08-31 16:30:00 | NPP-375 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cd6c2f30-2e5b-35ba-bbd9-0ce226658067 | -8.07731 | -43.61066 | 2026-08-31 16:30:00 | NPP-375 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eab121d2-fec3-3acb-8cec-f724842416fd | -10.12533 | -50.3134 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8bd61873-d5e3-3bd4-8912-2bad7b64457d | -15.25139 | -53.85493 | 2026-08-31 16:30:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cd4fa75f-47d0-34d4-b048-abf89b8cb275 | -10.34328 | -49.96289 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 13d3687b-747b-393b-a150-9eb2cd60126a | -11.34956 | -45.22139 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8a80dc9c-d63e-37e9-a993-1793def40018 | -8.86838 | -47.07994 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| e71c195e-b193-3067-a4be-ab01e10852a0 | -8.85174 | -47.0786 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ec38322a-111e-34f4-89f5-1ed476c04fca | -8.91994 | -45.0364 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7da01f45-a806-37b5-8087-181faf6dd4c7 | -10.73985 | -47.97299 | 2026-08-31 16:30:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0259a85a-7d3d-3af3-b543-24548b7635b0 | -8.39546 | -44.98501 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6486c5d4-5316-3858-a79e-3d644d8d0238 | -9.20953 | -51.57399 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1038307a-ad8a-3391-b0ea-d2e702fcf718 | -8.86537 | -47.08755 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3c3e362e-4203-3bc7-a966-df3b2cd965b8 | -13.26739 | -51.59662 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0d3c503c-58a4-33fb-8e09-77f98cc36dd8 | -8.76037 | -46.47198 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5dedaec4-a6a6-39dd-99bc-a4c3627436a5 | -9.21456 | -51.5697 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 41c93a86-7e40-3653-bafd-8065473a429e | -11.06932 | -51.51828 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b537d70a-0cf8-305a-abce-45973a9ea06c | -10.80521 | -50.63306 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 80d12876-f4d7-304d-aef0-d1cb364f2c68 | -11.2495 | -45.11223 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 47e6e0c1-d31e-3b21-8776-e78177179b39 | -11.71253 | -47.64124 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0df386c5-0d2f-3c40-a85c-d7217b6e0945 | -11.93324 | -45.0815 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| cac0a8b6-7945-3853-b1cf-e5d57bb14840 | -13.47279 | -40.25149 | 2026-08-31 16:30:00 | NPP-375 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4f39e872-e084-375d-bbb3-48688e72f0a3 | -11.20765 | -46.08453 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fb82ebe6-baae-35ab-aea6-6dd1b9ddb21a | -10.10959 | -50.31237 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c8107b2d-7727-3026-8a9a-4accbc8880d9 | -11.26677 | -45.06224 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55ae540f-6765-3e0f-8859-7db745b6ac15 | -9.42582 | -45.64277 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e9509628-8de2-3355-9b5e-2209e9e2bd4b | -11.07254 | -51.52102 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 618e280f-428b-3cfe-9f37-316338a7f43f | -11.20847 | -46.08724 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7868a167-28df-325e-9e9f-92cc70c97bd6 | -8.8689 | -47.08349 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3b6d569c-485c-3ab0-a5fc-e7f936022a0f | -9.59997 | -45.40419 | 2026-08-31 16:30:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9af018f9-3f86-3431-a5bf-3828270f421a | -8.76913 | -46.45058 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| ce711d72-f0ad-39ec-a1a3-2f086704a872 | -11.22493 | -45.15204 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| deae7619-aa42-3227-af51-cc3ecb4e5ad2 | -8.86607 | -47.08704 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8f2eb48a-a8cb-3f7f-a46f-fb8ee6dcea74 | -10.87536 | -40.73955 | 2026-08-31 16:30:00 | NPP-375 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 52d3d2fd-ec42-3065-90b1-d1a655412410 | -11.2477 | -45.126 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b6ea070b-ede2-3551-a192-fe0b25a76940 | -9.19111 | -51.56119 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 784713f8-9715-3f1c-baea-e8b5453d12cb | -11.20832 | -45.33231 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e9c0a5e9-fe40-36a1-b916-3e118eea6b52 | -9.19065 | -51.55762 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 4a2854ae-754b-3463-a362-6acea3138d2b | -8.76351 | -46.46637 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| af31f2e2-f298-3ced-b80d-8f801070b3cf | -7.34502 | -38.73044 | 2026-08-31 16:30:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4f37041b-6659-3d31-b8f3-ff917f5a7376 | -9.45333 | -48.19774 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b593b79d-54ea-34ab-9368-ae755af2489f | -11.636 | -50.18339 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db9b92a9-1a58-355a-aca4-20a5f13474f3 | -12.96177 | -45.93762 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 23b8f556-70d1-3cd7-9106-a5ce659f90c3 | -14.96065 | -54.56427 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 1d84f58c-9732-329f-9f67-d84c5d4154ce | -12.9051 | -45.84636 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 09d0507f-8dae-32ed-9369-1763a6fe2149 | -11.61849 | -49.42006 | 2026-08-31 16:30:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f0cc5887-bbac-3b27-88e3-b4a160f038ca | -11.46375 | -44.87062 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a33fd7a-c313-3309-9931-9ffef61b1548 | -5.58731 | -42.31906 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 776c4b19-7cab-3e30-b864-5ff3c88c153b | -4.95991 | -55.85725 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 418a1399-268e-3522-beda-f0595ffe447c | -3.4105 | -43.37428 | 2026-08-31 16:33:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 8ee7ccd4-639e-3011-9808-7805ec94cce6 | -7.42319 | -44.26825 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90cb6b4d-4e2e-3966-8312-36d62308b3f5 | -6.33813 | -44.93801 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 25d1b71c-42ba-33b5-9876-a4b6294421ff | -7.92651 | -44.23824 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f57b7bb4-6993-3d31-b899-73bf604a29c2 | -8.12599 | -45.48575 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| c4839025-2981-333d-b0f9-ea45f6b168ff | -5.80326 | -45.04056 | 2026-08-31 16:33:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 74dbf367-778e-355f-9b4f-234fa984aac1 | -7.59943 | -44.99726 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a3a14fa1-295e-31cd-b534-19b00d18f80f | -5.8742 | -52.16038 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 9c4f467a-4e07-349f-92ff-c4177e0b4fc3 | -8.1729 | -54.92915 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| d786cd71-e96d-39d6-9ff3-9d6a756263d6 | -7.8555 | -45.18113 | 2026-08-31 16:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2c7ab269-ea24-315b-a740-33388d8bbfc4 | -7.22479 | -42.7681 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 97416cdb-bf7c-35e3-b97c-98b53e137698 | -7.55785 | -44.33153 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| aea10f7a-018c-3380-ac30-3da2b134d3a8 | -6.97866 | -45.39611 | 2026-08-31 16:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 279fc49f-457c-3a36-9658-d2e41fcd32bf | -7.02485 | -56.54395 | 2026-08-31 16:33:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 87ad28dc-1a72-37eb-95f0-2cc74aa27056 | -8.12853 | -45.58121 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 2002e0be-6243-3325-af57-2ac2e39b7ec0 | -5.57999 | -42.338 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0b4cb7c7-2f4b-3c1c-a977-9104b1901323 | -6.25754 | -53.67899 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 98994a5c-8bb9-3bc2-8d7e-ca5496c4bfe4 | -8.1395 | -45.57956 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d57be9b1-a56c-3068-a273-75462dd91c17 | -1.30264 | -46.47051 | 2026-08-31 16:33:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ee708d5a-2af5-3988-b979-243646264391 | -3.94411 | -44.75025 | 2026-08-31 16:33:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 46cd42ef-afdc-3811-9b3a-48e48dd138b8 | -6.84086 | -41.72036 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| de670d2b-08b7-3b55-b1a7-31e9b9e49aa3 | -6.27777 | -53.3326 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a1f535cf-f403-30a1-8593-bd5c1dc43180 | -5.76492 | -44.13186 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| cdaeb8ba-82fd-30f7-bf72-9b83a06d5913 | -6.49633 | -41.85848 | 2026-08-31 16:33:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d982037a-26b3-311a-bd54-a75a1f570ab4 | -7.9908 | -44.33965 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| f32ae0cd-407b-32af-b4fb-49ecfc8e7e82 | -8.44275 | -46.89928 | 2026-08-31 16:33:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2ca01241-2ff2-37f0-8a41-1f973dbf1ab2 | -6.65963 | -43.87352 | 2026-08-31 16:33:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e64f918f-f8c4-3045-849a-43834224398f | -7.52282 | -44.4521 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04cdb0a7-7b14-34f7-92f4-670cfda849ce | -8.12365 | -45.57319 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 88679276-d712-395d-974e-2079f9f1f32a | -7.78753 | -44.07302 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 828ceab2-322d-3b1c-857b-7a3dd2bf13bf | -8.18039 | -54.93437 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 8f47b2aa-6060-3c36-984c-47650a3237a6 | -2.88947 | -41.79747 | 2026-08-31 16:33:00 | NPP-375 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5dde655-47db-3e58-b9cc-b243df0a812c | -7.9448 | -44.24305 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ad09f80e-5220-31c9-85b2-e177cc03f258 | -7.60231 | -44.99709 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a11e6434-ccf7-3f1e-8641-27842c44207a | -7.99623 | -44.28128 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.0 |


[Clique aqui para ver as próximas entradas](README127.md)
