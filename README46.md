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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 900c005c-4cab-3737-87a1-e769efc2d92b | -23.24836 | -45.97219 | 2025-09-10 04:17:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cd0a513b-6d19-3507-9cba-c463980db392 | -14.75438 | -45.33172 | 2025-09-10 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11d5550c-f178-3410-bf0c-1406a88b217f | -15.96099 | -49.62415 | 2025-09-10 04:17:00 | NOAA-21 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf086603-1ff9-3f83-b2ef-3811df77e095 | -10.75451 | -48.91888 | 2025-09-10 04:17:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 412f8ddd-0a1f-3d8a-a0bc-884ddd0d246b | -20.11804 | -47.80332 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1016503f-4999-37ad-91a4-b3d20040d319 | -16.09238 | -49.22173 | 2025-09-10 04:17:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 602742ee-311f-3d66-9738-87ef5b6c5503 | -14.75108 | -45.33117 | 2025-09-10 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f428dd4c-f75d-3088-bf69-2a3ed995e674 | -11.49527 | -50.41925 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14cf8114-35d8-3598-8c79-3f036701679a | -16.30333 | -45.69302 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 213d2a07-d308-3036-890b-bcaa6fee4d34 | -15.69782 | -49.90044 | 2025-09-10 04:17:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb58266d-f1e5-33a2-82df-25861ade48f2 | -12.93377 | -54.79588 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20200754-9a7d-3fa3-ae80-b7acaff459ab | -12.04794 | -51.03625 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 294dfb9a-ce82-309a-bba9-9e5cecd15ed9 | -10.19443 | -46.80479 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac131570-0ddf-3fb9-96c2-0f1f964c66ff | -12.06164 | -51.05994 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a193296-c770-304f-88cc-92dc1c4897e4 | -11.81757 | -46.75409 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d3b6ade-6d96-3cf5-8364-8b5a0b81aa43 | -14.55201 | -48.75108 | 2025-09-10 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42cdc1fa-7109-3335-a792-bcab098d6f92 | -11.81348 | -46.75744 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba9929e3-ca97-37eb-a60a-e2d456cf5cf7 | -15.21813 | -44.04176 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2112a102-e1bf-372f-a752-184283998f6f | -13.95571 | -48.25608 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf03bcd4-5141-3003-b992-885ac6c78c66 | -15.83463 | -48.96943 | 2025-09-10 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b6f1a5a-d726-3613-b5e4-4c682758d03e | -22.1563 | -47.6659 | 2025-09-10 04:17:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4bf3fbec-db7e-3313-b5a1-034fe7672b1c | -13.97552 | -48.23568 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77c9b78b-21ec-329d-9e8a-46a6c7ad45ee | -20.288 | -46.24721 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99314f5c-f18d-31be-afff-faea72be4423 | -23.2646 | -45.79318 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b5250a45-c8a8-3ce0-ba94-7bca8960bf83 | -17.72203 | -44.4458 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db00ce5c-fb94-37fa-bab9-a42dbc730c8d | -21.00386 | -46.05629 | 2025-09-10 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 74ab3fdd-d27e-3b32-b787-82818061e35c | -9.77223 | -48.33865 | 2025-09-10 04:17:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff8650cf-095c-32dc-8733-31f57b52ad25 | -20.10761 | -47.82478 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a403e56-ba0d-3848-b797-ecdbe3ea84d7 | -13.91367 | -44.1756 | 2025-09-10 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d150207-ed06-3819-80bb-e8233df017b0 | -11.67739 | -46.90277 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34b1ec08-5c15-3663-97b8-e6b8266485ae | -12.94184 | -54.81336 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12e360e4-4986-3b6c-9fe5-cae85a36ea17 | -12.18715 | -53.86836 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fe67ec93-b53a-3628-a692-d1da1de402c4 | -14.29616 | -49.14321 | 2025-09-10 04:17:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a483072-a459-33ad-a6a6-c37f72a9e765 | -23.39063 | -45.96747 | 2025-09-10 04:17:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9a9be620-a43f-3172-b576-0ffb247862ce | -15.48974 | -49.48893 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe3cacc6-322e-3e9f-a77e-daf4dd85df27 | -15.13532 | -52.40068 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0ae794bf-b88b-3ad9-a73b-87df50b4f566 | -11.11383 | -48.40914 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 247e3d60-4c22-3993-8be5-60434013d2c0 | -11.03823 | -46.05504 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6531337-f455-3b0c-97cf-ac8d62b9a8e2 | -15.11251 | -48.03127 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 482c8cf7-1560-3894-a881-e6205caaebc0 | -14.46553 | -53.33626 | 2025-09-10 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 672c8b89-8a0d-3b62-aa07-6fd464435190 | -15.5262 | -48.37795 | 2025-09-10 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a26f05e5-ffb9-3e9c-a3f9-d3e6792d0942 | -12.02983 | -45.85728 | 2025-09-10 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9aa2ecd5-428a-34e4-a0e6-54db07daa888 | -11.68249 | -46.90374 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28c50795-940c-3c1a-ac21-b2a89d2fff37 | -20.54432 | -47.69426 | 2025-09-10 04:17:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3146f1f9-b721-3bf6-a802-e04e7a2aa515 | -14.90218 | -50.12648 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d6b2194-d786-342b-b4a6-5da58fa7ee14 | -14.44036 | -52.95887 | 2025-09-10 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4f137a7-72f4-3a5d-8363-1059d07f31a1 | -20.70344 | -46.0658 | 2025-09-10 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e528f20-7fcb-3239-b946-5af31ee9f7fe | -12.18404 | -50.63224 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdaf6709-fda8-30fa-bb92-7e3aabd68f80 | -11.16127 | -45.28707 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3e1c16f-6b7c-301e-9f54-b829a12f5519 | -10.01888 | -51.70473 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2624b06f-5ff3-3eea-8e36-92bbf6a7d8cd | -17.56054 | -44.54556 | 2025-09-10 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92e9fb95-2578-3fb1-b8dc-b919d9a1b057 | -11.21192 | -54.99004 | 2025-09-10 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a455448a-e013-3176-bfb0-fac97d02323c | -12.92644 | -54.77477 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5b43d867-0d8d-3ee7-9353-5442f4cf1996 | -17.2965 | -46.68017 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 324c1ff4-1509-31fe-86de-e08d84192a69 | -20.16555 | -47.69547 | 2025-09-10 04:17:00 | NOAA-21 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbe43eba-f9a0-388f-a56c-11a28c2682f2 | -10.72286 | -48.28293 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| ce0a60e3-ec5e-3395-8891-970e08b65877 | -13.97057 | -48.22142 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f2a4f3cd-1ab5-3364-ab8e-717747c54333 | -17.30605 | -46.72688 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bff969aa-61a1-3f41-8289-c3b19466ea77 | -11.44276 | -43.64362 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40bfc566-7a65-331f-abfb-465e197d6040 | -17.5572 | -44.54499 | 2025-09-10 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e3c5c02-b56f-347f-90bf-7c9373291117 | -16.88256 | -45.75372 | 2025-09-10 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27437e79-aaf3-3d22-b188-b3457cdc5ca6 | -13.79412 | -46.2935 | 2025-09-10 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 32e3f1d0-7342-37df-9b9e-8ac58203eaaa | -15.25319 | -53.78597 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74bb52df-380f-35dc-8cc9-f4782eea2255 | -11.15794 | -45.28654 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2e312c3-2c06-368d-800a-367c397ec259 | -9.76512 | -51.12349 | 2025-09-10 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cc8fe69-2acb-3109-a488-3c018331659a | -16.62416 | -49.77441 | 2025-09-10 04:17:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 905d5032-14b1-34dc-afa7-cffcf5f68070 | -17.55999 | -44.54922 | 2025-09-10 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68ef357e-a01c-3952-b743-ffb1483b5c1d | -15.1415 | -52.39289 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f0e50ef2-dd4d-326f-854c-bb991b920472 | -17.28202 | -46.68514 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 868c383b-42d1-3ad3-9abc-039dedb365e5 | -17.30974 | -46.74634 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f33bbc56-ec87-3b2b-b92d-793c50585cab | -12.93856 | -54.80075 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82cfa9e2-8de7-301c-a272-4481ba8a15a1 | -12.15337 | -43.70889 | 2025-09-10 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 453f6d15-ed5d-3bd5-83fe-f401c04d6d33 | -16.45861 | -51.97904 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f89d4691-85c7-31b8-96b1-632e951bb4e6 | -12.18647 | -53.86544 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e19d0c65-dd4a-3bb8-bbfa-f13efcd43a4b | -20.86761 | -43.70855 | 2025-09-10 04:17:00 | NOAA-21 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4227b1d7-af6b-3111-baa1-c24d30e24eb4 | -14.3817 | -47.3188 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| decea9d4-2f16-3ae8-a275-242cbecead5d | -16.05887 | -49.96763 | 2025-09-10 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55f1adbd-f85d-3a50-8abc-ccd83de076b2 | -10.96508 | -46.80205 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0fd1632-21d3-35d9-97c1-8c442c044d58 | -15.60386 | -52.75241 | 2025-09-10 04:17:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be16af91-4180-3bcd-8be2-9d42737edf26 | -12.93781 | -54.80457 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08c499ef-b17d-300a-9829-dde03b3db6ee | -16.84705 | -41.14655 | 2025-09-10 04:17:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cde0b37c-6cea-385b-8548-e2ee3d7d4e2c | -10.30642 | -48.8038 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6cfad70b-f92f-34e7-89c7-04161030e69c | -15.1455 | -44.03048 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6f36bce-ee83-3b13-90a4-c5b331a8caf1 | -15.14227 | -52.3888 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3646cea-a17c-3df9-874b-0ea078a2e644 | -15.01073 | -48.03072 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f94f4850-9190-3eb7-883f-9093b300990a | -17.77781 | -46.13772 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68cd228c-976d-3df8-ad92-6d46621912ec | -12.06962 | -51.06594 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f7804a6-f06c-3e80-80dc-a98a738ad448 | -11.8284 | -46.74738 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5686120-5179-3f5e-9132-9ffe08afae47 | -10.27673 | -48.81234 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b08c6ec2-a06e-3ece-b980-d4f582ff3f1c | -22.8294 | -46.4305 | 2025-09-10 04:17:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e86c2279-8127-39ba-b495-9921965e921b | -11.48323 | -50.41288 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39220e06-66d0-3390-9cfa-78920ff066b0 | -10.96923 | -46.79862 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e7b785f-4b11-3d20-982d-38989109a71f | -14.35817 | -47.31112 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40cad50f-ee26-3061-b771-f1ccceaaaaa0 | -10.00517 | -48.08705 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 80c46ac4-ce51-3463-9dfa-8c5474de0b2f | -10.57924 | -52.04115 | 2025-09-10 04:17:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d90ce09-88a9-3559-8404-63b94b1c8d3d | -10.01499 | -51.67217 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 71294b4f-0259-32d4-b78e-033162258bac | -15.15331 | -44.02424 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc4f1891-f5be-34c4-ae2e-4cdf4da03ee3 | -15.16212 | -47.95203 | 2025-09-10 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7422d6c-8d30-38bf-b09b-72a5db8c592b | -20.13317 | -47.68964 | 2025-09-10 04:17:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd0fe955-dc14-3493-8842-7753a3d7ba83 | -11.56033 | -49.04314 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README47.md)
