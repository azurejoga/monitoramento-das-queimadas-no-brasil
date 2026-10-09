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

## Dados Diários - Página 257

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41115747-4eae-3268-90f9-bb3256e2744b | -15.69189 | -42.36428 | 2026-10-09 15:58:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7615a3d-c316-3f1a-9c39-21c22d8e37dd | -15.91812 | -38.96444 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c0dab2fb-e91d-34b8-a63a-3102776c933f | -11.59217 | -43.69647 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 20c3cedc-4a0f-3940-9278-2a7031e66e40 | -11.96998 | -43.46598 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 9fdf3847-6a5b-358f-9447-a417a1835b20 | -11.98827 | -43.47337 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9743c7f1-d4d6-3480-99a6-60a2af9575f8 | -14.89823 | -46.16508 | 2026-10-09 15:58:00 | NPP-375 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 34659d4b-2a6d-3696-bf03-43cd1f186fa4 | -11.76789 | -45.47894 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 08f3f128-0199-3e15-a9f0-6a64bbca2d4f | -18.47518 | -42.25265 | 2026-10-09 15:58:00 | NPP-375 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 971bf0d7-17f2-30ac-b41f-f63d5e9559e7 | -15.69018 | -41.76742 | 2026-10-09 15:58:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0d7b5c27-a401-3193-882b-acd38f3f9b6d | -11.47384 | -43.38987 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 50e2888b-8744-3b1d-83f7-9956205846fe | -15.55362 | -42.63548 | 2026-10-09 15:58:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 10e949ea-91a9-32ca-bf8b-a92601c9d1b4 | -13.00442 | -39.7342 | 2026-10-09 15:58:00 | NPP-375 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 95350844-fdc7-3a98-b70b-779fd67b21ad | -11.96956 | -38.39066 | 2026-10-09 15:58:00 | NPP-375 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 67424eb5-a8a9-38b7-91ae-b535925eb891 | -14.05762 | -44.81697 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 18592ebb-80a8-3acf-92ab-b54fc47350cb | -16.06572 | -45.25671 | 2026-10-09 15:58:00 | NPP-375 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b792e8ac-0872-3637-a401-c10ad9df7ced | -11.83745 | -43.5852 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| db1b2c01-ca56-3c22-865f-4112aa2acc27 | -15.75266 | -42.2189 | 2026-10-09 15:58:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b7f909dd-7f11-38ee-a054-a59ea48a3564 | -12.22769 | -44.69898 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74a1d691-d64f-367c-8ad0-077abbec6da1 | -14.93543 | -41.07076 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ffc84175-fc82-396e-92b5-390b0e261627 | -12.18435 | -44.80626 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 230.5 |
| b7de629b-6efa-3c8e-847c-988033d3cc25 | -15.78885 | -43.38583 | 2026-10-09 15:58:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5bd20a3b-168e-369f-a64a-b93a1f233378 | -11.97821 | -43.48593 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 5bb76aa0-a669-35d1-aa8a-ce60806e4d1a | -12.24658 | -44.75605 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 189a0016-8cb2-3d41-9072-8b3883e477a3 | -11.98936 | -43.47327 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 744969ec-370c-33dd-9fa8-e90d537b7b98 | -14.93507 | -41.06767 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 73395147-8079-3c8e-8e2f-dd54384001b2 | -11.46163 | -43.38356 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| cf909f97-b471-3ae4-a61a-6169004b8b62 | -14.65397 | -43.53042 | 2026-10-09 15:58:00 | NPP-375 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 862d3b05-6e95-3ea1-85e7-5159e59bc56a | -11.7779 | -46.81282 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 0605fe70-ea42-30ed-8cc5-60bf673d8920 | -12.90945 | -43.45617 | 2026-10-09 15:58:00 | NPP-375 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f86844a6-bf22-3cd6-9510-202cc6ccc685 | -18.08486 | -42.26218 | 2026-10-09 15:58:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 2c109593-edf1-33ef-83a6-bf98e1225fe3 | -13.49638 | -43.5607 | 2026-10-09 15:58:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dbe20fd9-720e-3bbe-84be-15b833581bb7 | -11.97864 | -43.48949 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 174a7acd-5ab5-3169-80db-53c10669648c | -18.32411 | -42.38464 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| a19e6c39-f1ac-3df8-b149-c927fed67be1 | -14.58776 | -41.20325 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 79f0c740-799c-3077-bf76-b4776591c0fc | -14.76791 | -40.895 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 2b6f4806-3624-3355-ab3c-6d5d7fb13511 | -12.00354 | -43.44575 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6e2ba388-5107-3345-84aa-4615d980a385 | -12.29757 | -47.05769 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e8e0b3aa-38b6-3846-bbd5-f4a12e190a4d | -11.65109 | -43.69889 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| fa26e002-465b-3799-9843-ec67d6bf9ee5 | -12.22524 | -44.83191 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8eea5b08-f539-33d9-853a-f93ab14302f5 | -15.38575 | -41.93057 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6c5035d6-1d52-3d1d-9e8e-3e79a04fbff6 | -12.36341 | -38.88455 | 2026-10-09 15:58:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fbbd1c91-0404-34f0-ac0a-8437c68f954c | -16.12117 | -43.40103 | 2026-10-09 15:58:00 | NPP-375 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 107c70c6-537d-3a9d-898d-64647ee56020 | -11.59648 | -43.63707 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| babd4f11-d794-361d-91d0-9fbc6e1fcb89 | -14.82773 | -42.31858 | 2026-10-09 15:58:00 | NPP-375 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ae030be5-c3b6-3f50-b351-2fb743f51c7e | -16.07598 | -45.98098 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d35c9f70-c9f4-3752-bbab-b9f167bfa241 | -12.36494 | -46.57413 | 2026-10-09 15:58:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| fed0c1c3-17e3-368b-8ec0-0c1a30a45f43 | -15.10712 | -43.84353 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4bc44c1e-3355-34ab-adde-7975a2938572 | -14.05912 | -44.8191 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8be6e46b-4dea-374b-928b-c173ca7a2521 | -16.82487 | -42.29617 | 2026-10-09 15:58:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e16eafe8-59aa-3be5-87d5-2b0529f48d1b | -14.58263 | -41.20354 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 77ff4a97-dae7-3d84-99e2-5ab49e50d586 | -11.78458 | -43.53128 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 417a92e3-c9fd-339c-a060-681244b25258 | -11.58744 | -43.65828 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 64570082-e553-3e8f-90c0-6935db051b49 | -11.87087 | -43.57239 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ad9c5df3-03e1-3586-90ee-2dc88dcb6c93 | -16.51268 | -43.14784 | 2026-10-09 15:58:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fb09d784-d2ab-3069-aeac-df629fc95912 | -15.26399 | -42.37523 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.5 |
| d20ecb4c-bca9-309d-81a2-e0e06faabbae | -15.16561 | -43.80544 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5fd2fe5b-eaa9-36c4-915b-389d3035acf5 | -14.27267 | -42.18459 | 2026-10-09 15:58:00 | NPP-375 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d803bbb1-3a02-38ca-a942-3a3f32a22cc3 | -14.44156 | -43.93181 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 1b9578b2-c646-30d3-9c7e-ce16aa241c2a | -11.58204 | -43.6589 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 377b5308-f1d3-363a-bddf-b176ed7ab0c0 | -12.3651 | -46.56285 | 2026-10-09 15:58:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| acd26b2b-4ad7-345c-aa2a-2063f981ad77 | -14.50881 | -40.60463 | 2026-10-09 15:58:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b30f78a6-e0c5-33aa-8822-bee68a993f84 | -15.11027 | -43.63063 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 1d6afe0a-9ddd-357b-9671-20092405ffbb | -12.00227 | -43.44596 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 22f7fa24-cdc3-3400-b3dd-623bfec3faa3 | -14.2517 | -43.73906 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fe143eab-2ce4-3ad7-a268-66561a39b9a3 | -11.31891 | -44.82764 | 2026-10-09 15:58:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 14fb11dc-3fdb-3af9-94d3-070f13b3fd7a | -11.31218 | -44.82355 | 2026-10-09 15:58:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a79bcd63-0fd5-3403-bc23-073094892f1c | -11.57631 | -42.81219 | 2026-10-09 15:58:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8d951b3b-85d8-3653-a716-3ffa18949dcb | -14.6485 | -43.53546 | 2026-10-09 15:58:00 | NPP-375 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3a432afa-6a65-3296-8566-c63bba011729 | -12.24833 | -42.32203 | 2026-10-09 15:58:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7e443f28-c0bf-3192-9a97-744047690006 | -15.9729 | -45.02855 | 2026-10-09 15:58:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a6ad4c7-7fcb-346d-82e2-d5d4a04ba69a | -14.18122 | -39.25798 | 2026-10-09 15:58:00 | NPP-375 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 420f4957-d3a0-307e-87fa-a3e0bd0a2abb | -12.19017 | -44.63744 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 289.2 |
| d6c291da-c199-31c7-88fc-00f042a739c1 | -11.69125 | -46.77855 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bd82f43d-7b3d-3baf-94ac-8016398c8ad5 | -11.89174 | -41.62101 | 2026-10-09 15:58:00 | NPP-375 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| ea5694bb-9906-377f-9173-f085332200e8 | -17.52309 | -42.44906 | 2026-10-09 15:58:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 56ad939f-ff54-3089-88c4-e1bda38b1c5f | -14.0501 | -44.80735 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 555b11e5-5656-3a61-9d83-4f3973e4740a | -11.78024 | -46.81461 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| f792708e-9299-3b41-8802-f26a13c03720 | -14.04761 | -43.85294 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8917c297-aa2d-3f3a-9116-91e0ea8be079 | -11.99197 | -43.4563 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 335530e1-8a99-3a13-8e3c-10e89ac238ad | -11.5807 | -43.65094 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 392.2 |
| 72d23cd0-4e19-35b2-8672-e2df22221b49 | -11.7665 | -43.53403 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1fb606b4-f654-3926-9d93-4f437befac71 | -11.58695 | -43.6543 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| f7bbc90f-26bf-3adc-8fb5-6f7827c506dd | -12.81811 | -44.65546 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a5dc5f4b-76cd-30ba-9433-874ab5795fe1 | -12.68275 | -39.87104 | 2026-10-09 15:58:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3c70f5ef-3c8c-3d6a-b65c-72bac64c0831 | -14.06356 | -43.83294 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bf733ceb-e9b6-3b9f-bbee-404753708768 | -12.25343 | -44.74883 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 66dca565-03c9-324a-adb2-558c0ba91992 | -15.24708 | -40.52795 | 2026-10-09 15:58:00 | NPP-375 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 73c23585-d264-31a7-935f-2579351a9e30 | -11.27866 | -41.13021 | 2026-10-09 15:58:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 30.0 |
| a9717f99-7fd7-39f8-aef7-8b66dbecbdf3 | -11.96752 | -43.49348 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d90daf91-e548-3d92-bd4b-ac04744bf3f1 | -12.22168 | -43.94774 | 2026-10-09 15:58:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 677640c3-1a83-3c00-97d9-43b4528fdbeb | -12.20815 | -44.73866 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 3237f41a-259b-3b7f-8a36-9200f345e528 | -11.58737 | -43.70474 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 67ade0a1-a25a-3f51-a0b6-a229f417cca3 | -11.76868 | -44.96505 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1cba4fd5-7356-3256-8441-8b1098aebeb7 | -13.25866 | -42.25373 | 2026-10-09 15:58:00 | NPP-375 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 043d4811-5d20-3fcc-b85c-bb00cfd12e90 | -14.66885 | -41.79181 | 2026-10-09 15:58:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ce5934b3-7df2-398c-9ac9-72e32af20815 | -11.58594 | -43.64221 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| b13478a3-d657-31b9-9533-9f288f68d2a9 | -14.60279 | -41.28377 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| de214deb-4ad0-3ddd-97f9-354d82e87c89 | -15.54592 | -41.01532 | 2026-10-09 15:58:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5eb2a8cd-ad8a-3dd0-8e86-2706b9b5db31 | -15.10824 | -43.84486 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| de50e58a-1c74-38d0-a3d7-37773919185f | -15.17168 | -43.80476 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README258.md)
