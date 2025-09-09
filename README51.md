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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 828a1d87-37af-3d3b-a7ed-aacaa8b77c6c | -18.82623 | -49.6803 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6287cc08-2807-3a20-8211-7ebe84d33e55 | -18.66143 | -49.09335 | 2025-09-09 04:36:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da33ac18-2fda-3c72-8abb-8022b5ea39aa | -16.29143 | -45.68741 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f731d8ac-c75a-3091-9a3d-1e7a6b914201 | -16.34835 | -52.94252 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 469e3e87-89ef-3d96-965b-eb266676a0a7 | -15.54923 | -48.36921 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fea6ab64-e227-345a-95f0-825ba6352403 | -16.2873 | -45.68039 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2409763-8cd5-3530-b67b-c407b438685a | -15.257 | -53.80109 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6966be8-451e-31f8-9f14-92a9ffeb6ed3 | -15.72022 | -53.53874 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc316209-5467-31cf-a9f7-c0ced067cbcd | -18.61102 | -48.20719 | 2025-09-09 04:36:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e67cd4a0-bdb3-3124-9d0a-cd719382677c | -14.36668 | -60.30487 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b9db31d-670d-381d-8bdd-8b806f8f1303 | -15.08522 | -50.093 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 163d8d11-ae98-3e73-b2e0-10868733323f | -14.55801 | -52.2242 | 2025-09-09 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fefa5bc4-36b1-37a7-a7a6-65f862e68ac6 | -15.58641 | -49.2038 | 2025-09-09 04:36:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3388c620-e005-3d13-9aed-be55ffd0f305 | -18.03753 | -47.13055 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7c08ee27-9f99-31a1-9bd2-195899508eaa | -16.32172 | -52.92958 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ed2e243-2735-3a9b-9cf2-b1e26d1f0ee1 | -19.58726 | -49.46571 | 2025-09-09 04:36:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74d39558-8029-353a-9b51-466d9472f548 | -21.00224 | -46.05922 | 2025-09-09 04:36:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 79bfd703-f5c3-35b6-a11e-050e070f941f | -15.77284 | -53.54201 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7df54226-6c00-3b2a-88ec-d2af574f6365 | -15.5919 | -52.9015 | 2025-09-09 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d8dcd11-3536-313f-bc13-10beb689ca06 | -16.34418 | -52.94589 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6da6d7c-1c51-33e5-b92e-8a66019a76c3 | -18.76177 | -47.09905 | 2025-09-09 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65d2e098-e384-35a9-a8b2-49c225f99f73 | -15.27125 | -52.36083 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a2bd177-3604-3fe3-94dc-c4319bee8c9f | -15.24422 | -53.77198 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ba2e11a-5b26-39c5-af48-a49cc2363be0 | -18.03328 | -47.13424 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ceb3c5e0-c04c-3821-bad1-029ad75ea1bf | -18.82288 | -49.67973 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 057c5f38-4371-3d20-ab45-6657c4e3cfbc | -15.87353 | -52.20525 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffe019b9-1d8a-38bb-865f-81bc977afe10 | -15.5289 | -48.36578 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c00d1899-11be-3a54-839a-959cfe43bb15 | -16.07328 | -50.49568 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aab87099-4221-3a2c-bf76-5315f26a9c72 | -15.53173 | -48.37015 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9c1da19-a3a2-3691-8ca6-2bfea9e78afc | -15.54083 | -48.40234 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7aa0943-1bfd-3615-b153-652c85062069 | -18.805 | -49.63872 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a377962c-d049-3621-8ca3-04a32e8f5c8e | -15.1798 | -47.95445 | 2025-09-09 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b7e1885-fdaf-3279-aece-05ce18de7bc3 | -14.79226 | -48.23 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ce1a21a-30b8-349d-a338-f9cac385561b | -16.50992 | -50.61744 | 2025-09-09 04:36:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef975a76-cca8-3a59-9a8d-cd462ef7a264 | -18.82791 | -49.69199 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f2b459ad-24ba-32e6-9e53-14dbc7022f3a | -14.54488 | -48.74929 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6131c79c-cdbb-313e-aa9a-e6c9d4f1934f | -15.2578 | -53.79656 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf84628f-e478-3c08-92e5-b13f488a5f8f | -15.26693 | -53.7948 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d10b09a-d4be-31a0-9c38-b894fca96694 | -16.89272 | -45.79116 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5531aa3-f307-35d5-bc93-e8c6ccecb65b | -15.78522 | -53.53511 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94d7117e-1fb2-3af8-86bf-109d92328ecd | -17.95431 | -46.92461 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f37513f-cd32-3b70-a58a-ccf22e93fe0f | -14.54991 | -48.76121 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48ab1768-b12c-35b2-9c84-3e5793919403 | -14.44414 | -53.2175 | 2025-09-09 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ed659ff-db25-319f-8e5a-cfb9371c8e96 | -19.9275 | -46.17468 | 2025-09-09 04:36:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cd225c1a-82fa-3875-b99b-d8502e251a89 | -14.91978 | -55.88912 | 2025-09-09 04:36:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 16eabeef-2cc5-3e00-b2af-3deaa70e4a29 | -15.26616 | -53.79934 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b618da4-be8a-34f9-a429-528c6eb894ae | -15.20479 | -46.24635 | 2025-09-09 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6f7fd96-6a60-39a8-a387-0ea2952e8d52 | -20.07347 | -47.35696 | 2025-09-09 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbc931ac-f157-32e9-a127-e66e19cae39c | -16.34622 | -52.93377 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2407284-82ca-3857-98de-655a77a4a413 | -17.68164 | -52.26366 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 348416fb-cb06-3b29-b010-1489e901108f | -13.9562 | -54.01589 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef0c24a2-e4d0-38cb-867d-08f03dfa8e88 | -15.10799 | -52.34523 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| feb948cf-2e6b-3e99-bf55-26611106f067 | -14.53546 | -48.76624 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9de518f2-e3cb-3ed9-8c08-1fdf32c8932a | -15.01789 | -49.25631 | 2025-09-09 04:36:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ef8dbc8-ef35-321d-98ea-6641b3056dbf | -16.96535 | -45.84893 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a6cb2b6d-9756-3232-a1f0-c3a63fc51a15 | -19.45703 | -43.94011 | 2025-09-09 04:36:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2dfaf496-7d0c-3332-9965-f232cdd6e67e | -15.72097 | -53.53437 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aff29f8e-95f7-382e-879f-ef2a297ca948 | -17.16276 | -44.44962 | 2025-09-09 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 264df84f-1b5e-37d1-a8bb-7e22dea82567 | -14.91016 | -50.10423 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 512c9cb4-64ba-39e4-83fa-8af5461fee04 | -14.73638 | -55.91394 | 2025-09-09 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d2bee935-a497-3c8e-8e4b-1c01507a520c | -18.03814 | -47.12621 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| eca09e03-7f5b-35ed-9b07-38a56db931f1 | -15.26597 | -53.7934 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aea2aaff-9c85-3c3b-9254-87f417142ce1 | -17.73037 | -44.48951 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff677b3a-8d94-3cc4-a7d3-09eb9096d734 | -17.58029 | -49.80998 | 2025-09-09 04:36:00 | NOAA-21 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea3d7fe7-4f4e-3272-8d61-afa21ae08a0a | -19.59008 | -49.47008 | 2025-09-09 04:36:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b34f0cc-d2f6-37cd-a5a7-f46619f31503 | -15.40727 | -53.95816 | 2025-09-09 04:36:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 522ad8b5-82f3-3aa0-9cc0-0a595ff6aaab | -14.5546 | -49.1745 | 2025-09-09 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1f5c0db-7bb7-3a12-b46b-1fc0de54bf25 | -18.1198 | -45.32737 | 2025-09-09 04:36:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4762d6f7-dd82-3851-b251-5af16fc257c3 | -18.83125 | -49.69255 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1791d686-0831-381b-b3e3-740f86364b53 | -15.52671 | -48.16761 | 2025-09-09 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d5883e8-dd9f-30f9-9ee5-d079049d5f1b | -12.87454 | -62.09123 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cec6faa-6bcd-3a6a-8b7c-51d7ebe4c2c7 | -15.9191 | -48.16523 | 2025-09-09 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea35ccc7-bd12-3fce-95bd-41b4a5226f52 | -14.35731 | -60.31004 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad33c1d1-9bf9-33ab-8f6d-f78dae54a583 | -20.00047 | -46.95729 | 2025-09-09 04:36:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff1d0916-83cf-37d1-a4a3-849f4b44c171 | -15.24208 | -53.76233 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cd12038-66c4-3209-8b14-07c98112e7d5 | -15.09071 | -50.1012 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a9254d4-c2ac-3c4e-8fee-554df52ef76a | -17.29727 | -46.70812 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7b13ce8-eaee-3b93-b856-63d5fbd1aae8 | -15.81916 | -52.25824 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96a62af9-4f2d-36bb-96df-14b6e2909efb | -16.33294 | -52.92717 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95f1c7b6-cd3f-3439-b01b-5e6ae5ce69ab | -19.41537 | -46.51519 | 2025-09-09 04:36:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 677a083f-f7a4-3214-9080-dafb800b441d | -17.94151 | -48.65117 | 2025-09-09 04:36:00 | NOAA-21 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac74084e-a13f-37ee-bf07-6ff3db07297e | -15.10091 | -48.08652 | 2025-09-09 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27d85ae5-6fa8-304b-89cf-265b1a87e9ea | -15.26779 | -52.36024 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 131bf136-1cff-314c-b6d5-025f29fb4aec | -15.52949 | -48.38525 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54966157-5abe-3abd-b2a0-c0676305991a | -15.5419 | -48.3718 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b96b3c7-5639-318e-9c11-416e3b27a36b | -18.04028 | -47.08409 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e42c4878-e678-3932-91ea-3d088f4eb305 | -14.52986 | -48.73561 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f1b47c0-1c3a-3f6c-ba19-bb244ecf271a | -18.8173 | -49.67118 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39e1a5f6-365c-3fb9-9b6f-c26f7761ff7d | -20.07596 | -47.35469 | 2025-09-09 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d744ceba-e1ed-31eb-ba42-50a5b4037c5b | -17.7195 | -44.47235 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 447e2e68-5158-3762-99c8-bece8940431e | -16.34971 | -52.93446 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d92ab580-5d17-3440-b9f1-c6efed19a87c | -18.83069 | -49.69626 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7bfcb8b2-e6e1-3ce8-ab33-fc5363751b99 | -17.27372 | -46.74204 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dba47d26-a8c7-35e1-b32a-c44dba3ca390 | -19.90477 | -43.85355 | 2025-09-09 04:36:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3626082f-4dba-308f-bab8-d652f3bf15de | -20.5339 | -43.97226 | 2025-09-09 04:36:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 731259fb-3e19-34be-822a-6d120372d954 | -18.76614 | -47.66652 | 2025-09-09 04:36:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bf2be08-8f69-3980-bf01-fbddcceaa923 | -15.20153 | -47.97349 | 2025-09-09 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7259d23b-8d3c-3131-b8fb-43bf406d75ad | -15.83134 | -48.95247 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d14eb44-7f14-3b5a-8fc8-47fd4636cd64 | -16.32733 | -52.91779 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0864184d-c68f-3032-a371-0ecf48536004 | -15.29363 | -43.3819 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
