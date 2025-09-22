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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 779df273-6523-398a-bf09-5e31cbcd6cb0 | -11.28516 | -47.51941 | 2025-09-22 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5e42faa-a5a5-376e-b652-6280e35de063 | -12.71402 | -47.69889 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b9e23b22-5fab-3dfd-8438-1156c747d098 | -15.95459 | -59.41259 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4823bc4-896a-3977-8b1f-ccddfc98d665 | -15.99131 | -59.4785 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2572ba11-060f-32c3-b738-e944a33aa981 | -11.04363 | -54.17604 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7353b36-9536-362d-a9d2-b73ba2276757 | -11.33069 | -54.35182 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b93e9d6b-38d9-3732-8d43-26f49c819ef1 | -12.97785 | -46.38234 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9f23009-b140-3b0a-ac19-3d8707502896 | -12.08525 | -44.79378 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 496e2789-644c-3b18-814c-933c1c6d2df1 | -18.37864 | -46.46463 | 2025-09-22 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a21b4fa-827c-3b73-84cd-1585ca7c976d | -11.64407 | -52.86235 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb393596-d9e6-32ff-a768-77f3336790ad | -14.62101 | -49.74807 | 2025-09-22 04:40:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40b742dd-a9ee-3449-89d7-da219607fdb7 | -12.97328 | -46.38662 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da9c2097-9a5b-31f2-bdb2-c77cc2feb2eb | -12.75166 | -47.75484 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae05be97-7486-3ae6-9738-0b52999a14e6 | -11.63907 | -52.84959 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a952b0a5-ef47-3204-8f42-f12c1deb1434 | -15.35556 | -59.18682 | 2025-09-22 04:40:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9b838bf-1231-3c2b-8f58-29c8877905dd | -15.8356 | -59.51389 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b50c6af-e67d-3b6a-b819-3d301582617b | -14.97402 | -44.40971 | 2025-09-22 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73a5bfc5-c7d3-356c-9eaf-3c4796448728 | -11.63497 | -52.85283 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b2169210-f1a8-359b-b8cb-2c0118d8985b | -10.43416 | -61.34298 | 2025-09-22 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 695259d9-f557-3d01-8d33-88fad79f57a8 | -14.44878 | -46.52426 | 2025-09-22 04:40:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 98af158c-c162-3834-b076-68335d5026cd | -14.58939 | -56.03656 | 2025-09-22 04:40:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acadbab0-5c7e-3c79-a13d-33230013d23c | -16.73741 | -43.02509 | 2025-09-22 04:40:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b2037838-ab42-32a0-8690-2ff64b99e525 | -15.00553 | -55.31101 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e88abfa-9ff8-307a-8a54-5755aa2ed17c | -14.77485 | -48.60707 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7feda91a-3228-3c62-90dd-aba7404d8186 | -15.9676 | -59.37373 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9236e84-d834-37a2-966a-eaa76d738a99 | -15.83567 | -59.58871 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d53eb79-2027-3631-bc23-d15241cc8a39 | -15.83438 | -59.52 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f6625719-974a-3239-9e01-024ba84d5dfb | -15.83783 | -59.5069 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| acea0c1b-4dd7-32d4-9906-040101006997 | -11.26376 | -49.24302 | 2025-09-22 04:40:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e92dfc81-f1d8-3988-9b83-e71236992a7d | -11.3099 | -54.33862 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45291979-b00b-39b5-a83a-d0febe1541ba | -15.83086 | -59.58776 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38e0d6f0-153f-3d16-9705-86593d1a1571 | -11.73389 | -47.80772 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd6c67a5-0c1b-3ee1-a5f0-5a584960b452 | -12.71576 | -47.71202 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31e738e2-801a-3044-b716-341f25730201 | -12.13537 | -44.7762 | 2025-09-22 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f59a2d36-c101-3a45-a1a9-7bd48e97d923 | -11.66477 | -47.49596 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de7a8ce4-00d7-306a-aafe-02a1e66645ed | -14.07516 | -50.1534 | 2025-09-22 04:40:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fbd327b-08a2-33da-aafe-b69eb2df1840 | -15.25677 | -43.08501 | 2025-09-22 04:40:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c0398f4d-8b93-3abd-8699-fb35f8dfb515 | -17.06071 | -44.90369 | 2025-09-22 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35256e71-3026-315b-872d-c9ccdcc539ef | -11.64753 | -52.86295 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16f5012c-211f-31ee-8f17-90d07f810068 | -17.1049 | -45.90648 | 2025-09-22 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c54ac58d-9d27-3c0b-80d2-f37c26d96738 | -18.40008 | -42.86322 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9a21692-e687-3ce0-b329-92cb4fd066ea | -15.83675 | -59.58328 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d81e6294-f99e-36ad-8da2-616b5259f25b | -11.87248 | -64.93614 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 730fa90f-738d-3ab6-9ddd-00770f7f453c | -14.44807 | -46.52946 | 2025-09-22 04:40:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c230395b-6cb4-33e9-a80a-785dfad276a4 | -15.76385 | -59.42868 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d147be11-a9b3-33de-87f6-cf1a5c2138cb | -13.41158 | -46.69035 | 2025-09-22 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b73b4ab-d61d-3b37-93b0-57b3c26321af | -11.65099 | -52.86354 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf25a4b1-7eee-33b7-87f2-e2af85927c7e | -15.34982 | -59.19115 | 2025-09-22 04:40:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34135f35-f8f3-3149-9e26-2840f61061ab | -15.94611 | -59.40542 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4f37f08-d81d-3074-856e-db9c3c741d71 | -14.39586 | -48.55764 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43b94eb4-805c-3a01-833f-90c6eb94d025 | -15.28597 | -59.42125 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc7a7570-f2f9-33d3-9ba0-06554229bac3 | -18.37812 | -46.46865 | 2025-09-22 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 34516124-d9d8-3320-a469-031b354593fd | -15.96172 | -59.37546 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3bb36582-f7a8-3116-886d-eb1031278741 | -16.01957 | -59.46054 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49ce019d-6eae-3c93-916d-b285891b5ab9 | -11.22288 | -49.59649 | 2025-09-22 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 404c6813-f566-3bcd-8c52-f17ce7497aa0 | -12.27408 | -47.84207 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba99688e-8016-3e28-8113-ea01302f366d | -15.2749 | -56.85568 | 2025-09-22 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e280e64-2075-31eb-8ce8-6b4120b0985e | -14.62016 | -48.27858 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d23d0bf8-b522-3473-bc6c-7a2348dd98b2 | -15.03653 | -55.28814 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 278c69f6-f7ad-3e5f-82ba-77a45cc8a03d | -14.39938 | -48.55818 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fd23c1c-7bc2-3d1a-978b-dea5adfef0f1 | -15.04025 | -55.28887 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e69b2a8-35eb-3dc8-8b8c-0780f3c38f0d | -14.61659 | -48.27795 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49dadbe5-337f-35a5-a749-a89f5fe2d3f7 | -15.99727 | -59.47336 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad2dc552-1949-3655-9de7-51af50c01381 | -14.44012 | -46.52895 | 2025-09-22 04:40:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1812501f-c9ad-3fbe-940e-38eab292df5c | -15.8403 | -59.52001 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d57215c5-954c-3800-9ed5-4c3f9f8eac9a | -18.101 | -44.26992 | 2025-09-22 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d31eef48-550c-30f8-9173-9dbfdcc36447 | -11.04215 | -54.17286 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f359147-3642-38f2-a105-b397bcb15e6f | -11.31953 | -54.34974 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67bdbd21-da84-3fe4-8c94-fd66aa5adc64 | -15.95033 | -59.38347 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12dbfecd-b23a-3749-8c2a-7baa8be6c0f5 | -16.00898 | -59.46415 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 946b2b71-cb06-3575-b9d2-58f759da70c5 | -11.42461 | -55.01095 | 2025-09-22 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 332d5522-5d0c-3fac-8e75-3ed145188f76 | -15.02699 | -55.27672 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfa05cb3-b2b4-3bfc-84ac-00134841f877 | -12.71278 | -47.7073 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3fbff2fc-aee2-3656-974b-c227169d3857 | -11.87095 | -64.94337 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1979290-6aa8-3d69-99e6-7a5e5c62f181 | -11.55599 | -48.5887 | 2025-09-22 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3408859-1851-3e96-b3e4-9635c0bf4a92 | -14.44153 | -46.51862 | 2025-09-22 04:40:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9d1db82-8a7d-3302-9488-65216b2ecb3d | -11.66181 | -47.4912 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f52233d9-7061-3098-a4c8-629255e37a49 | -15.76523 | -59.4206 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5df2c34f-ccad-3629-914e-3b4f4a0efa84 | -15.02617 | -55.2814 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3db885a2-8c74-3863-bb33-e7bc9de90b3d | -18.55198 | -43.84953 | 2025-09-22 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e02f6bc7-014f-3217-808d-b9a8cfa2cdaf | -14.22967 | -44.32082 | 2025-09-22 04:40:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bee687db-c23f-339d-84b6-dc9ecb4880dd | -11.22198 | -46.16284 | 2025-09-22 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94fd0fa4-9b23-342f-ad76-f96ae3dbf766 | -12.09003 | -44.7905 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0639dff2-d29a-3427-9cc9-73bc0ce7f3bc | -11.22128 | -46.16781 | 2025-09-22 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afa90a94-b3be-3ecd-81b0-77debaf2ce39 | -12.36336 | -44.21738 | 2025-09-22 04:40:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b9cb24f-3383-3208-8a75-24892e0a2efc | -12.7134 | -47.7031 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf79ae6c-dc8b-3ae1-bc54-aad679405acf | -11.63151 | -52.85225 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1d5b9283-524a-3545-92c9-25e5fa25f039 | -18.54694 | -43.84963 | 2025-09-22 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74716f2c-486b-350a-a3ad-289f64ba5b72 | -14.44409 | -46.52921 | 2025-09-22 04:40:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d066eb9-34e9-3797-a2fc-ed1cbc91a030 | -11.73419 | -47.80173 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75ce26d8-b693-357e-b1fd-eef6bc5eb809 | -12.06783 | -44.82682 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80d82b49-2700-3337-af26-229fa99dafa2 | -15.96644 | -59.3765 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d9a43c0-26f7-3b79-9fe6-26e7f3e69137 | -18.39637 | -42.8564 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e78d2a3-4c6c-3c03-a2c7-7753e570c452 | -12.06731 | -44.83072 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de85fdd5-2329-35f9-ac43-746043c1d02b | -18.84328 | -42.19514 | 2025-09-22 04:40:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 913eee45-7da2-3fe5-8f59-7ff1a48be7d1 | -11.65757 | -47.49496 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7a6bbbb-9664-3caf-ba59-fea1a9e42cdf | -14.2696 | -44.38095 | 2025-09-22 04:40:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56c428c5-841e-3af9-b8a0-987de13ac9db | -17.34136 | -46.83006 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6915145b-7e87-39f9-9461-bd88a159af12 | -17.16609 | -46.8348 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01cdc527-0079-36f0-983e-cee92ff7c832 | -15.41305 | -58.78127 | 2025-09-22 04:40:00 | NOAA-20 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README30.md)
