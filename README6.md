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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f880e63-6713-375d-8751-755433768470 | -7.86466 | -41.93361 | 2025-12-16 03:55:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f64a4c9-879f-33ee-bbb9-2835f5647544 | -5.27651 | -43.64196 | 2025-12-16 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb96d607-5f57-3110-a8b8-42d8f4ba23b9 | -11.04913 | -45.39274 | 2025-12-16 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 920ba090-e42d-3c93-a906-dd7c0c640cc5 | -8.08773 | -35.24479 | 2025-12-16 03:55:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6a249411-60bf-34dd-a326-3cf88dbf5210 | -5.95355 | -42.53273 | 2025-12-16 03:55:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5783534b-7652-3fc8-b308-f8fefff93c49 | -11.16556 | -38.00159 | 2025-12-16 03:55:00 | NOAA-21 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e23e4d0c-16ef-3f40-88cc-ed9d8447cd4b | -6.55246 | -35.27954 | 2025-12-16 03:55:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f06a9885-90c1-3c25-82f6-d859148181d6 | -8.42664 | -44.02876 | 2025-12-16 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fcbe769-a663-314d-99ff-d8becc11d81a | -7.61392 | -47.05395 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88b7136f-a1bd-38b4-9bd5-ac28b1200216 | -7.41193 | -39.4649 | 2025-12-16 03:55:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f07c5895-2579-3e06-ab6a-2cdee8db5c5c | -8.06717 | -43.14418 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a31f8ba3-4883-3f24-b45b-6fad294482bd | -5.75992 | -40.50573 | 2025-12-16 03:55:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| acdb7c40-6252-38bc-acb0-0ffa3f88f3cf | -8.06958 | -43.14192 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d49c5099-658c-34bb-9893-1f4a63bac632 | -11.7598 | -44.03239 | 2025-12-16 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b9c9889-be21-3a50-b4b9-e3ebe7ac4886 | -10.52119 | -44.93124 | 2025-12-16 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1dda851-65cb-321b-bd5c-ebb63d1a1f38 | -4.63466 | -47.93913 | 2025-12-16 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0807ab7f-bfe8-34fe-a500-d8e67af61d1d | -6.42188 | -39.83102 | 2025-12-16 03:55:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ec8752e-5352-38f7-bc37-c73f753455fe | -5.72124 | -40.50353 | 2025-12-16 03:55:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bf5a28b7-bedf-346b-bcc1-53e10eadb66f | -4.65584 | -47.81457 | 2025-12-16 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76e9a6e2-1c6a-3aea-9593-4210803bcdb3 | -8.41675 | -44.03797 | 2025-12-16 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37a5e22e-de72-354c-ae62-b90d9698daad | -7.30906 | -39.23361 | 2025-12-16 03:55:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20d28065-62c0-3ba5-bf64-b6ec2ebcb4bd | -11.88925 | -43.71172 | 2025-12-16 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2889be7b-c849-3e20-8a8e-ea6d8329dbd3 | -11.1497 | -43.32713 | 2025-12-16 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bcb80174-ec3c-393d-b935-3f6b7706fd54 | -5.19236 | -44.29354 | 2025-12-16 03:55:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d77848ee-ceae-3058-9a76-6d7259d4ead0 | -7.52086 | -37.35091 | 2025-12-16 03:55:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0acf529f-651d-3dca-b402-028e1eb2ab10 | -8.07102 | -43.14481 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 74139e07-f2f2-3883-865d-5df550f5a298 | -7.61514 | -47.04988 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a8a379b-c069-3f42-bcb0-abb7b417204f | -11.04704 | -45.40474 | 2025-12-16 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0099ca52-9f89-354e-ac62-b138689f6900 | -9.45726 | -35.87403 | 2025-12-16 03:55:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 00cff48d-9540-32cd-8a05-2763fb8c2e14 | -5.39777 | -44.6853 | 2025-12-16 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a8958b0-f6e3-36f6-a73f-4787fdc1dd48 | -8.07181 | -43.13996 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| aa178738-1e97-37d4-8c89-daf628c54a4f | -7.86397 | -41.93774 | 2025-12-16 03:55:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| edd3ab50-879c-3434-bf46-2bd58f45ee96 | -6.73709 | -35.04614 | 2025-12-16 03:55:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8e4fe613-bf0c-3ebb-8cd9-bd6bc8430efa | -7.61565 | -47.04696 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0999b2ed-c220-3584-964c-87aacc189f53 | -12.82007 | -43.82019 | 2025-12-16 03:55:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43ed46a5-bf09-3eef-b137-106327f68b98 | -10.77889 | -44.46057 | 2025-12-16 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 169f83d7-4bc9-3318-abe2-9e31a0fb9052 | -11.56114 | -44.94874 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb1e49a5-301c-39d5-a019-fb7b0448f519 | -8.07487 | -43.1454 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 99c6d22c-40a1-3157-8bc2-b20c1e8af2ff | -11.1452 | -43.33101 | 2025-12-16 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d8d36cf5-c967-360f-bceb-ff1d687c329a | -8.4214 | -44.03512 | 2025-12-16 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01d3e838-356f-3c11-80f0-1451fc1cd7aa | -10.6223 | -40.51886 | 2025-12-16 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8fc3f041-df58-30be-9fcb-5d0f1242e012 | -9.55852 | -44.93614 | 2025-12-16 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb6a837d-d7cc-3cb6-a200-9003f36ef642 | -10.80547 | -44.50571 | 2025-12-16 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da18a458-17bd-3a85-800f-6fc00ac3343b | -9.8243 | -40.56959 | 2025-12-16 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 45c563b6-2ba0-36bb-ba0d-4747311849f1 | -8.07343 | -43.14254 | 2025-12-16 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8c340c92-dce7-3ca0-8981-7db8602ec4c5 | -7.61412 | -47.05577 | 2025-12-16 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b164ac0d-b07d-3f94-9862-c67478cac4a8 | -6.66787 | -38.96359 | 2025-12-16 03:55:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4f85d05-2be5-3bcd-a58e-6d7251a7cba4 | -11.14598 | -43.32648 | 2025-12-16 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 104fe223-dced-35c5-b8ad-5dd3513a36bc | -7.7832 | -37.14754 | 2025-12-16 03:55:00 | NOAA-21 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c239e8b-2cb0-30a9-9268-f81615397326 | -17.70702 | -40.15894 | 2025-12-16 03:57:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0b0f6f3f-f5c0-3902-a3e5-794a0c148377 | -15.46603 | -39.15659 | 2025-12-16 03:57:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d00790bc-83c4-3ac3-a118-c579eb56118d | -14.43829 | -44.86942 | 2025-12-16 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1819f553-32be-3222-9f99-ceaa108941c9 | -17.7098 | -40.16313 | 2025-12-16 03:57:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9ae02d94-630b-375f-a98e-99eb388f68ff | -17.71314 | -40.16367 | 2025-12-16 03:57:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 05e38d61-4ad0-3f96-8ba4-f1e3ff715b24 | -15.4621 | -39.15974 | 2025-12-16 03:57:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 172f9c4b-5bf3-3881-9096-f650d093b82f | -17.94277 | -40.02018 | 2025-12-16 03:57:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c6d981b7-60db-3de4-88af-390f5346a4cc | -15.14083 | -41.83611 | 2025-12-16 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6df525a-49a3-3ebc-9c7a-68352c2d790c | -14.44606 | -44.87074 | 2025-12-16 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52a39338-28f6-3647-ba21-92b7d9760364 | -13.43005 | -41.32057 | 2025-12-16 03:57:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ebce8e9-d53b-366b-894a-9eaacf73e37a | -17.71036 | -40.15947 | 2025-12-16 03:57:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 29cfc37a-27c3-33ed-afbb-0a7e239c227a | -14.44218 | -44.87008 | 2025-12-16 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72c7a96f-75f4-3d0c-aaeb-06038f89401c | -15.46266 | -39.15605 | 2025-12-16 03:57:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 690f7606-937f-3c97-9fb7-17638f415d9a | -16.64986 | -40.62681 | 2025-12-16 03:57:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 47a28077-1445-35c9-a2bd-57aae6a656d2 | -15.13747 | -41.83552 | 2025-12-16 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 94206475-03b5-3327-86c4-31b44f6c17b4 | -17.71369 | -40.16001 | 2025-12-16 03:57:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 065c60df-a488-3c59-8104-7e183eebf38f | -13.37971 | -41.88544 | 2025-12-16 03:57:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 45de15a8-7b9a-3892-9bc9-140a67e3b116 | -22.89854 | -43.65713 | 2025-12-16 03:59:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0115cd9-59f1-3060-8e07-7e39d574cd86 | -23.61006 | -48.347 | 2025-12-16 03:59:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c770c5c3-8cb8-3699-b0a1-2892e6cc81c9 | -12.3074 | -57.3608 | 2025-12-16 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 1960ce05-b049-33f7-a556-478ee4423b1b | -3.65514 | -47.56084 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef25286d-8dfa-3436-a750-4eda4bcb56c1 | -5.11546 | -43.29417 | 2025-12-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 011489e2-3fc2-3981-9a22-8098cba6afbc | -5.84875 | -44.78529 | 2025-12-16 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 550cb676-25c1-3a75-8751-19c83d7e00ab | -4.40572 | -42.33381 | 2025-12-16 04:23:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6797f193-9d1b-366e-8c1f-3baf007ce542 | -3.65879 | -47.5615 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87791a40-3d8b-3f67-b415-7aced91c3493 | -4.63559 | -47.93956 | 2025-12-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbb457fb-8fe7-3453-b581-ddbd72cbbb81 | -2.80929 | -49.1259 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e920072-e410-3d18-af5a-85301cb9862d | -3.56845 | -47.17524 | 2025-12-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 972487cd-fc99-3419-b40e-afd2eacf4c6f | -5.72195 | -40.50278 | 2025-12-16 04:23:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2a3a7ff7-72c3-3a5e-962b-f61de07a35bb | -4.54589 | -47.91771 | 2025-12-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 242352da-7324-3d6c-a65a-73e1b59b4166 | -5.58144 | -43.75329 | 2025-12-16 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd8c261b-36a3-35c5-aba0-23e24ebfab2c | -3.72614 | -44.48879 | 2025-12-16 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91481a31-dda2-3ae3-a01f-63e8e54a4848 | -5.93781 | -44.45872 | 2025-12-16 04:23:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 714e2d19-b7a6-33a7-b3eb-c2b206f76fce | -4.65237 | -47.8129 | 2025-12-16 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62afda11-1e9e-3d78-9b0c-97f05b88254f | -4.40228 | -42.33328 | 2025-12-16 04:23:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c226730b-18b0-3016-bf5b-3482a2c827be | -3.0264 | -47.09078 | 2025-12-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ccd0dd-6e04-330d-b676-15cd0d6fb786 | -2.7949 | -51.40648 | 2025-12-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94576699-4fe2-3650-8054-5eaed555145e | -3.66094 | -47.55491 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d54f6210-bb06-392c-91b2-8e9f9f802a78 | -3.8357 | -44.82579 | 2025-12-16 04:23:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd8a5f20-f2ba-3050-bff6-ab5ec4489d6f | -3.93881 | -47.00646 | 2025-12-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33c700f2-2e88-393e-b136-ad5da106fee6 | -5.8493 | -44.78183 | 2025-12-16 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4bb9ae2-edba-3450-b5ef-10feb4b3cbbb | -4.6349 | -47.94384 | 2025-12-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89e0d449-16d1-3e03-b64b-4bc7ed500830 | -3.46141 | -48.97505 | 2025-12-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87d96e3b-4f38-3a19-ba0b-2dec586e02ec | -5.75922 | -40.50589 | 2025-12-16 04:23:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 976e650a-1d42-3cc5-a448-a13827616b68 | -3.65217 | -47.55597 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e942378-ff6d-3ed2-a237-bc138e43e629 | -5.18493 | -35.86738 | 2025-12-16 04:23:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d37a2dec-f282-36df-86f0-892817500c3e | -3.65293 | -47.55796 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5561d271-e18e-3872-ae0a-19ba0409f1e3 | -4.66145 | -42.39858 | 2025-12-16 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 010def3a-6283-319e-98ae-0b2bc396ed37 | -3.15331 | -48.14304 | 2025-12-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 399b67be-c03a-32c7-ba5d-bffbb1f8ccc8 | -3.40181 | -49.21043 | 2025-12-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9caac5a-4f1c-36d1-8f3f-10af016d144d | -2.81135 | -48.6485 | 2025-12-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README7.md)
