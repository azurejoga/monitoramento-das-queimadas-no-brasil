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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7ddcd92-6df2-3622-b3b8-60c9b27605e3 | -14.50443 | -48.32213 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a20fff3e-2359-30ab-bfaa-14e607aadf94 | -12.86725 | -44.81382 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 212f52b3-b32b-3d32-80db-12cf2a54c8d3 | -17.57619 | -46.90174 | 2026-09-28 17:07:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ac73d53a-c608-3df2-b3f9-f074d9e2e022 | -12.05976 | -45.74361 | 2026-09-28 17:07:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 2d67a606-16ce-3ebb-9e0a-5133e477201c | -12.91208 | -52.07076 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 397409e6-3b90-30fa-8a75-3789d65df69a | -12.86536 | -44.80389 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e6419bd7-94b2-3a5b-abcf-4b5a0bffe465 | -14.12141 | -46.28979 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5ead860c-4af4-362e-ac6e-68a440b74752 | -11.27923 | -43.55578 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2f5bf8e5-fc9e-33cc-b7e1-d0f678018790 | -14.15885 | -40.73177 | 2026-09-28 17:07:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| df0b12e7-cd1a-35fa-9c22-9db600501503 | -12.75699 | -50.98272 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ed0f9154-5a50-3e8d-8f7e-164984c2ba84 | -12.68905 | -45.01805 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| be13278b-7dbb-33d1-9e3f-62de286a002c | -15.06957 | -54.60006 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| cf30766c-265b-3455-82d4-66baaa64314c | -12.75538 | -47.30166 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 70b75a9c-6573-393e-b211-c6c47604a36e | -18.87313 | -46.67115 | 2026-09-28 17:07:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9c435f24-425b-3a29-890c-0a54ea126f62 | -15.06288 | -54.60107 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 1e77c8ae-5b7b-37f7-be8a-b82592bc9566 | -16.06427 | -47.9247 | 2026-09-28 17:07:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 23bc89a7-ac68-353b-84c4-9ee42da4aae2 | -18.00656 | -43.48219 | 2026-09-28 17:07:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 462074a8-5ac0-330e-80e2-fb56bddb651a | -19.30539 | -47.44371 | 2026-09-28 17:07:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1bfa823-60c3-3d09-8058-8831d4921157 | -14.32714 | -44.80669 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7f8f1d90-0282-379d-8782-e04c987dd077 | -17.57356 | -46.91104 | 2026-09-28 17:07:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37a39354-c179-3293-943d-f3c08c7c4476 | -11.6796 | -44.53332 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 7d3cddcd-0f1e-3b6e-a16a-d5f1a0317ae7 | -15.16764 | -43.5726 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 522a1757-c39f-3685-8955-325117639178 | -12.98333 | -44.797 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83be081b-efed-3138-a1e7-49689f9b3824 | -17.33681 | -53.95795 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 85d07ed3-625e-3d93-acf3-190dde77d952 | -11.39293 | -42.55806 | 2026-09-28 17:07:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 5ae43510-2c4f-3593-994a-a1d38814e206 | -12.96126 | -51.05634 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8efe3c76-1440-35d8-9760-b789a621f3cc | -17.23909 | -42.52342 | 2026-09-28 17:07:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c7e9526a-981e-31ed-9b7b-0359aeac68a0 | -14.4564 | -40.32839 | 2026-09-28 17:07:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 5a847667-d90a-37a3-b7e3-2255da23870c | -14.24397 | -40.94695 | 2026-09-28 17:07:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f475e80d-eb89-3638-8408-8291a20566f6 | -12.24519 | -42.03468 | 2026-09-28 17:07:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| f407f075-d161-36b3-aa9c-60c1a061580d | -11.20442 | -40.58678 | 2026-09-28 17:07:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c2ca7ebb-d1e7-336c-ac9c-a4ca4f482e01 | -15.51905 | -41.65031 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| fc5e92ba-b0dc-3f58-a210-b17f7c1f9b3c | -14.96343 | -41.06308 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 77f60620-0ce2-3e2c-ac93-ebf3d984965a | -18.02214 | -47.63588 | 2026-09-28 17:07:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 86ef3358-7048-3089-b045-1b7422cdb4c9 | -11.66473 | -43.52958 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| abf6fddc-ffeb-3060-a773-8102ab43ccd1 | -17.25353 | -44.81217 | 2026-09-28 17:07:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 451177a0-d887-30fc-b32c-cb462fa79b3a | -18.12152 | -44.38467 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 91613bff-a459-30f4-9603-7274955f9c2a | -14.51335 | -52.49047 | 2026-09-28 17:07:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3362e746-a6a1-37cd-a7bd-e189a2d31a9f | -11.37456 | -43.39747 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 56b8df6c-01fc-3d7c-8c3d-95f6c36998c5 | -11.70485 | -43.48999 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 721ec94b-a8e8-392c-9e6f-9cb915520fdb | -15.04529 | -48.04089 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 586b2033-6d3c-32eb-8a54-895c00440698 | -11.38043 | -43.39624 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5cf93c77-6ef7-343f-88d1-7c733d773483 | -12.43716 | -48.22403 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d7e23772-ab29-300b-80b9-ee1902430e07 | -18.72155 | -49.13031 | 2026-09-28 17:07:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1507767e-a5e9-3ed1-946f-fe0f3ab33017 | -12.67671 | -47.36657 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| db2a915d-ba2a-3ed0-bcbd-1964109ff41c | -17.57217 | -44.38673 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 326dc4c9-3cc7-3cd3-a6c3-518592f57651 | -14.51062 | -48.30968 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 06211c6a-f515-3151-9474-5dce35c088b2 | -14.51188 | -48.31691 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3b74682a-36ba-36dd-ac28-1b72f94f937a | -11.28506 | -43.55463 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 309daa49-f576-3b19-abda-137e36c6c4ea | -18.09566 | -43.25349 | 2026-09-28 17:07:00 | NOAA-21 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4cc4e4f8-7b52-350d-a7c4-d488e5e5a1dd | -13.94515 | -49.07568 | 2026-09-28 17:07:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 59a07e17-7628-32d7-9efc-2e9c0d7dae95 | -15.20533 | -50.24918 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91157859-135f-379b-8794-d4e6f2ce2114 | -14.452 | -40.74924 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a1b4c646-bf0f-3137-a05c-11d552abc6c8 | -15.07733 | -54.60632 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| bea00eaf-3a95-3a77-8530-c334f8236938 | -17.32788 | -53.96687 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c7cb2e14-6ba3-3cae-9ad0-89a55c093db3 | -11.71225 | -44.5268 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f5cf9936-3fcc-3aa5-996b-215841d4f8e2 | -15.74293 | -46.02659 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a9c80e8f-5301-33a7-b1fc-f0c1b02ca9ab | -13.08378 | -47.43746 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4f7e1f47-a55c-3896-8304-a53c6c2c6f15 | -17.30317 | -44.52376 | 2026-09-28 17:07:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| e5b8fb68-7dda-3c0f-89f8-5aa01fca9010 | -17.32347 | -53.96006 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7ddf2b6b-9161-31ca-a40a-c4d2bb542cf3 | -17.79244 | -47.1577 | 2026-09-28 17:07:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8f85b38f-e9a0-3ca2-ac35-458b614b20de | -11.65067 | -43.27687 | 2026-09-28 17:07:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9a5fb28-8d97-3221-8271-ce61a63a33a8 | -12.96481 | -51.05573 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 181fc2f1-641a-3435-a30b-1e72c1e1104e | -12.74851 | -47.28917 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7b58f039-40ef-3152-a1b3-a29ed67e2ff4 | -12.59901 | -45.08798 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5bcbbe5a-4514-3ab2-bebe-686790becfa1 | -15.07679 | -54.60268 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 36b24569-01d4-33a4-9efe-43a7c3e15ae6 | -11.90761 | -47.00337 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 49ecb4f5-4e90-3a78-b2b8-72b26adbaf9d | -12.49244 | -44.72706 | 2026-09-28 17:07:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| d35cad1b-5e32-3063-8296-b8c66d5a283e | -17.10428 | -39.5187 | 2026-09-28 17:07:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0ec9dd32-a306-3771-9f7d-cc14e03b3aee | -11.71495 | -44.51125 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| bc674775-1d57-3b82-8bd9-2f1097ca5c1e | -12.74911 | -50.68084 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 1e946911-4bfe-3347-ad61-0b42e4ce154e | -15.40912 | -47.94005 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1fe37d40-c269-31c3-beab-9e07634f9173 | -14.58693 | -41.23417 | 2026-09-28 17:07:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 97109df5-caa5-3793-9cc2-878b91295f2c | -11.71294 | -44.5304 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 302ad147-39d4-3e82-a86f-56d67bfbb393 | -17.58979 | -46.66704 | 2026-09-28 17:07:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d3ae165c-8bc5-39ce-8d8b-3da6e376cd6c | -12.10427 | -45.22041 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ebf230fe-0169-35ec-910c-141e59e20e55 | -18.05372 | -43.63368 | 2026-09-28 17:07:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 91e151b3-e713-3602-84ab-a8c2c559cf41 | -15.14906 | -44.03873 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 49.4 |
| d547a68a-ce7c-33e9-9bfa-34084dcfe435 | -15.08629 | -54.59752 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 0836e619-5163-3dc0-b3a2-1abe4261b50f | -13.49059 | -48.60553 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0c608e7b-79c3-37a9-a1f0-c066f216d75b | -16.2912 | -40.20065 | 2026-09-28 17:07:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 4d8808b8-dafd-382d-a797-e4b32935e5b1 | -13.37825 | -44.0284 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d583d2fb-be4f-3e79-a6da-8d8c70b63273 | -15.75703 | -42.28419 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4338c5dc-4ca3-3eae-bdb4-69fc7b8134a6 | -17.33348 | -53.95848 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 81e14f22-a4d2-3fdf-873d-5f11147922b0 | -15.4113 | -47.92859 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf1891a6-64e0-3709-835c-273285fc4bf2 | -15.19924 | -46.15788 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fb858418-2f15-39bd-aaa7-d555e7a5da82 | -12.74513 | -50.68419 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| a3b1fb07-ffb5-3b96-ac72-116417054db8 | -15.68459 | -47.60411 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9485ff85-a90a-3fde-8b2b-445a84c0da5e | -11.26499 | -43.54503 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| a2986e7f-4d22-3aea-b130-efedf06dd809 | -13.37551 | -44.01426 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| a8f20f69-4fee-308c-95ab-03612c22c377 | -13.17412 | -48.54668 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 486d52b6-1b42-3b97-8fa6-67ca563fe89c | -15.15452 | -43.59787 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 9652c9ca-1543-30cc-b562-d82e30ee4095 | -19.24528 | -46.6253 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3ad44910-f369-37c2-ace3-0e845e163005 | -13.1637 | -48.55907 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 776c3b93-55fc-3364-9cd4-e78708618bde | -18.87239 | -46.66717 | 2026-09-28 17:07:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 34593d17-d2fd-3ad9-9956-d8bcefbbf409 | -24.70889 | -51.32502 | 2026-09-28 17:07:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| a8dfe7bc-a3eb-3925-8a16-90ed5e2e64e5 | -18.06091 | -41.43134 | 2026-09-28 17:07:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 47ca686c-fc76-3d5f-a5bc-5b7adddf085e | -12.24411 | -42.02942 | 2026-09-28 17:07:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 09a2e1d9-2382-332f-be85-f879da87fa20 | -17.20033 | -46.64251 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 03b4d5e6-6213-3782-aa08-3f0afe047f76 | -13.08459 | -48.56073 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README130.md)
