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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1c353ed-8db6-3ba3-8a65-dca368119e08 | -12.9732 | -45.2051 | 2025-08-20 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 359.8 |
| 478ce103-efb5-36a8-810a-b90b4c9617f3 | -8.7942 | -45.492 | 2025-08-20 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 495682ee-479c-3f11-9efb-c00772664006 | -12.9925 | -45.202 | 2025-08-20 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 454.8 |
| 6a6c7a83-3a2c-30b2-a230-f3fb02d50bac | -11.3087 | -44.9264 | 2025-08-20 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| e68c3d82-d46f-31ff-a30c-f139d1732b16 | -13.1367 | -54.9171 | 2025-08-20 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 5dad2646-fb87-3715-aa51-d7001747176b | -6.9605 | -42.8816 | 2025-08-20 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 7ec601df-9eee-3a99-8adf-9585d5d1761e | -8.7945 | -45.4693 | 2025-08-20 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 55eeaf5a-d2ab-36ba-8d61-11a63cf591f1 | -15.0196 | -54.8112 | 2025-08-20 13:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3e1814e9-96f6-379f-8e46-2d33dcdaae8b | -5.9713 | -44.1312 | 2025-08-20 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 36e5b636-3081-3cbe-bfcc-42e25344dc89 | -13.8748 | -45.5411 | 2025-08-20 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 06423299-30f0-3022-a1f7-e543a7052acb | -8.297 | -47.64 | 2025-08-20 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| ef66bc5e-b8ef-36aa-bc86-ee22ad93527b | -12.9921 | -45.2252 | 2025-08-20 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 583b61ff-86a6-3273-98aa-b0c4c9a75a94 | -13.1558 | -54.9151 | 2025-08-20 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e66a743d-0325-3e18-9ce6-f6d927ee857c | -12.6698 | -44.9525 | 2025-08-20 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 26ffe3f7-b0e0-3f0a-8f18-6dbb4da0c377 | -12.9736 | -45.1819 | 2025-08-20 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 0ca3e380-6870-3dd2-bb5c-7f6beb8ae22f | -15.0002 | -54.8135 | 2025-08-20 13:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| dbe3995f-ecf0-3039-a486-f437a31c30d9 | -13.1555 | -54.9357 | 2025-08-20 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| eb3b7fad-a19f-334a-998f-69c9882fdb76 | -8.7948 | -45.4465 | 2025-08-20 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4627be2c-8b27-398c-822d-f5c7c5cdccb2 | -11.6739 | -60.1869 | 2025-08-20 13:10:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 55af088c-d5c2-3ea0-bfce-693163515ece | -13.1364 | -54.9376 | 2025-08-20 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 2e249d19-5524-3026-9779-dde1046d91ec | -5.9711 | -44.1542 | 2025-08-20 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 255.5 |
| f6350ce8-8297-3414-8810-4d1fea03bf24 | -5.9713 | -44.1312 | 2025-08-20 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 216c6bad-2f6a-30e2-b8fa-94727ac14542 | -12.9921 | -45.2252 | 2025-08-20 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| d0330740-77fb-3844-8817-054f8995a3c2 | -12.9736 | -45.1819 | 2025-08-20 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 8f0727ec-b4f9-3ae8-90a6-0746bffb7383 | -13.1364 | -54.9376 | 2025-08-20 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 80a4b3d8-c86c-33d9-8933-66b84720774e | -13.3349 | -54.4027 | 2025-08-20 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 248.5 |
| 69f3d80e-c82a-3c7c-a0ca-9f2ee42809d5 | -12.955 | -46.1504 | 2025-08-20 13:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 8432e042-4b3e-30f4-9f5d-7f127196b246 | -12.6698 | -44.9525 | 2025-08-20 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 1b48f808-8322-3d25-8880-f1c3c1888cf5 | -15.0002 | -54.8135 | 2025-08-20 13:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 0961a379-a45a-36b7-85e7-ae115cfe5ffd | -13.8748 | -45.5411 | 2025-08-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 563875d6-3b5c-3e9e-a8cd-5f87bb49c2c8 | -17.594 | -42.2745 | 2025-08-20 13:20:00 | GOES-19 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.2 |
| bb0512d6-58df-3cf4-9550-4feec290b298 | -13.8743 | -45.5643 | 2025-08-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 4bb662da-01c3-3b13-a39e-e7ed024bff06 | -12.9732 | -45.2051 | 2025-08-20 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 46898508-22ad-3dc2-bef7-3160c97f317a | -13.1367 | -54.9171 | 2025-08-20 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 09d5fbc1-a256-383f-a12a-b120be19cc2f | -13.354 | -54.4006 | 2025-08-20 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| d0ca38b9-2ccc-3791-a25b-7ddf1e765607 | -13.3537 | -54.4213 | 2025-08-20 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1eae375b-0691-37d7-af04-41c2968345b4 | -15.0193 | -54.832 | 2025-08-20 13:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d1d28bc0-74bc-32a7-b98f-c3dea44c92bf | -15.0196 | -54.8112 | 2025-08-20 13:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e67166fa-434e-3262-9e45-682832c5c501 | -10.8214 | -43.2665 | 2025-08-20 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 78.8 |
| f2716b75-9614-3d2c-bf7c-985e900fd0d9 | -13.8553 | -45.5444 | 2025-08-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 56d463a5-61c7-309c-9d3e-f3825fe2e4c4 | -5.9711 | -44.1542 | 2025-08-20 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 200.4 |
| d4b4fb42-26f3-3ccc-92f7-7d480387ee41 | -12.9546 | -46.1732 | 2025-08-20 13:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 6e57a60f-6aeb-3f01-8de1-73ff8d5005f2 | -8.7945 | -45.4693 | 2025-08-20 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 4d1c0528-1163-3dfb-923d-9948512b645b | -13.1558 | -54.9151 | 2025-08-20 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 5c04d9ea-ec31-362a-8b60-4cf47dcdba68 | -6.9607 | -42.858 | 2025-08-20 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 0f3b0af2-e478-3847-a832-86dce101e7d2 | -13.1555 | -54.9357 | 2025-08-20 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| a31bce69-faa2-3792-8c8b-d9f5bf10d780 | -3.982 | -42.516 | 2025-08-20 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| c84aee53-9292-3936-a388-4ce397220f98 | -12.9925 | -45.202 | 2025-08-20 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 516.7 |
| ceaab916-248f-3571-a323-5942560ab043 | -12.6147 | -46.8821 | 2025-08-20 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| a66791ec-86f7-3142-84a7-e336247a16bf | -13.3346 | -54.4233 | 2025-08-20 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 301.0 |
| ed2dae52-f8d9-3def-aa71-b9f3f4ebbd40 | -11.3087 | -44.9264 | 2025-08-20 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4a452885-bd35-3171-bd08-ea7dcc21b9c9 | -5.9713 | -44.1312 | 2025-08-20 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 50303251-6d2f-35e1-9dec-ebda126e9509 | -13.1364 | -54.9376 | 2025-08-20 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 6ef2f379-35d8-3b70-896a-5f294d1e90f4 | -13.1558 | -54.9151 | 2025-08-20 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| f81f8ac2-7c3e-3300-be89-585f8be340bf | -8.7948 | -45.4465 | 2025-08-20 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 21df1018-0684-3436-813e-c020d81faaf4 | -8.7945 | -45.4693 | 2025-08-20 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1f8e8797-679b-3d1e-a1d1-b3bd9ddb8557 | -12.9732 | -45.2051 | 2025-08-20 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.4 |
| e07f001b-56da-3b54-8588-2aea210d2e21 | -13.1367 | -54.9171 | 2025-08-20 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| bc312536-55c0-3144-9f4b-8df9413c4172 | -17.594 | -42.2745 | 2025-08-20 13:30:00 | GOES-19 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.5 |
| 33b8c254-68de-3c15-93f4-b043e8ba9433 | -13.354 | -54.4006 | 2025-08-20 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 1fc3984a-b68e-3ee3-a04c-9a7eb400c0d9 | -13.3346 | -54.4233 | 2025-08-20 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 297.0 |
| 70e2db1c-ab80-3095-b056-b1476f41dd05 | -13.8748 | -45.5411 | 2025-08-20 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f93222f1-4083-34d8-8c29-578b8c948ec9 | -15.0196 | -54.8112 | 2025-08-20 13:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| ce07b081-8799-36e8-b3f7-ab089c8f86ea | -11.3087 | -44.9264 | 2025-08-20 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 93026ecc-25c2-3537-9f17-f527d1a1dbfe | -15.0193 | -54.832 | 2025-08-20 13:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 70f1e31b-9bfc-397d-88c7-c359917faaa0 | -5.9711 | -44.1542 | 2025-08-20 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 249.1 |
| bf95997f-fa29-34a4-8efd-4ec3e229f66a | -6.9605 | -42.8816 | 2025-08-20 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 7ab64874-ea57-3c29-81a0-6ad46c249dc9 | -10.7043 | -48.2226 | 2025-08-20 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 63fe7218-dc0d-3f6b-8d64-0f62d7b594cc | -13.8743 | -45.5643 | 2025-08-20 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| bff0d2df-4bd6-3e1a-897f-479cdf3b8482 | -6.8497 | -44.4267 | 2025-08-20 13:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2bdd357d-65e2-3594-852d-0878a64f2eb4 | -12.9925 | -45.202 | 2025-08-20 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 405.0 |
| 9eaba264-cd57-37a0-82c3-68d1611afea0 | -11.773 | -51.7365 | 2025-08-20 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 67a12350-9aa1-374b-929f-de46bdbc7b28 | -12.6698 | -44.9525 | 2025-08-20 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| f0a5ef8d-0953-3946-b97a-eb5995ca2db9 | -13.1555 | -54.9357 | 2025-08-20 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 9ca8d589-ff9c-3a5c-bcbd-c5f9a1a8b85d | -13.3537 | -54.4213 | 2025-08-20 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 89c99c4c-1e42-3bf7-a178-c08f512416e8 | -13.3349 | -54.4027 | 2025-08-20 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 229.2 |
| 41adda27-abf8-387e-92d4-28a4945f101a | -12.8984 | -46.0906 | 2025-08-20 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2fb5bd20-fa76-3cd2-80cf-8986252cd7d8 | -3.982 | -42.516 | 2025-08-20 13:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| ed35cadf-bd2e-3444-ba84-2cfe7ab73eb9 | -12.9736 | -45.1819 | 2025-08-20 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| e485caa7-aea5-39e6-81d2-551227924711 | -6.9607 | -42.858 | 2025-08-20 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 89fb8991-6025-3aea-bd52-ca842f9d40cd | -12.9921 | -45.2252 | 2025-08-20 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 2a3bbe35-9cd0-3118-9cf0-be25331dd388 | -15.0002 | -54.8135 | 2025-08-20 13:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d11385b4-8c7c-36cf-9c42-9480e7f01d91 | -12.9925 | -45.202 | 2025-08-20 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 364.6 |
| e36af08b-77e0-3472-a532-cb6cb46ce302 | -15.0193 | -54.832 | 2025-08-20 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2eff0147-d7d1-3761-a4eb-3d9673943d96 | -15.0002 | -54.8135 | 2025-08-20 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ba9e85bf-54a7-33c1-933d-2bdd62fa665e | -15.0196 | -54.8112 | 2025-08-20 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e864f4ae-1b33-3195-b307-a05c5fca38d8 | -12.9778 | -56.8614 | 2025-08-20 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 30d76e4e-9c2f-302b-a259-158fb3060bdc | -13.0194 | -46.8219 | 2025-08-20 13:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 140.3 |
| e1c9a980-a840-32ab-88b5-a27750693622 | -13.1364 | -54.9376 | 2025-08-20 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 537c3bc1-37de-3b64-9c44-d3916daab09f | -5.9713 | -44.1312 | 2025-08-20 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| eccbc3d9-83a0-3648-b64a-2f4c51e1bfc9 | -6.9607 | -42.858 | 2025-08-20 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 38f610f0-5037-3299-ad4f-391dd932e89c | -6.9605 | -42.8816 | 2025-08-20 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 2598f107-fc31-3550-99cb-5d09749c42a1 | -13.8748 | -45.5411 | 2025-08-20 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b8184e76-936b-3b53-85d4-792f4ce1f008 | -13.0198 | -46.7992 | 2025-08-20 13:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ded5208a-3c33-3c79-ad31-660d58be9f87 | -12.9921 | -45.2252 | 2025-08-20 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| bb954df2-263b-385b-bfcd-e8e90d420fb5 | -12.6698 | -44.9525 | 2025-08-20 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 7b2e3abc-7c1e-3a8d-84cc-f1a4fc6313ea | -13.0391 | -46.7963 | 2025-08-20 13:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e8be9d97-a4a8-315b-bb2a-e7dadc16314b | -3.982 | -42.516 | 2025-08-20 13:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 0b2ce928-7afa-3d0b-abc7-89beee4daa25 | -12.9732 | -45.2051 | 2025-08-20 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| d246cd76-25e7-350f-a481-a9c64854143c | -13.0387 | -46.819 | 2025-08-20 13:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |


[Clique aqui para ver as próximas entradas](README64.md)
