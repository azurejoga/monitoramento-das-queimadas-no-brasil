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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 954ccb14-36bb-3da9-8b5c-d752156474b1 | -10.4745 | -44.34278 | 2025-08-06 03:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e0977ee-0b48-3027-a2fc-0467586bb25a | -12.02453 | -44.8211 | 2025-08-06 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bdc67f2-0349-3392-b6d2-6e4ac96f838f | -12.75725 | -44.41883 | 2025-08-06 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f6b9dad4-2777-3790-bd15-79e7f57fa81e | -11.42778 | -45.13992 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9ed19af3-54f5-3eee-b13e-23a4f6802f0c | -12.97093 | -44.8869 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7c2f8f1-c8ef-3e8c-a747-160654b5113f | -13.00208 | -44.90089 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c365037a-4c1b-3ced-9c23-0b88e37f89ac | -11.42511 | -45.12905 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e9b98043-45ab-339e-880f-dec2951de394 | -11.42888 | -45.13452 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d3fb923a-9020-3936-93e6-1a21d8bc9460 | -12.97686 | -44.88821 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 779373fc-ee7a-3287-9b1b-e4ae92056c7c | -11.8432 | -43.7196 | 2025-08-06 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cccbe71-e78b-376e-a3cd-4c0cd6e53713 | -11.72904 | -47.52573 | 2025-08-06 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8817d6c0-1da5-37fc-83ea-57a4e8d48ece | -11.9161 | -44.92399 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 402d0f2f-a6c1-3334-9a36-b364bf24fc29 | -11.02969 | -45.0702 | 2025-08-06 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1270754-0fb4-3c7a-a452-eb578b1bcdef | -12.98877 | -44.89047 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 57827277-7e94-3c5b-9988-82955be8ebb8 | -9.07411 | -45.05843 | 2025-08-06 03:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f0a2443d-a968-3334-9b60-d1c81314576e | -9.46905 | -46.31136 | 2025-08-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8ed32db-24fe-3d51-ada2-54c085b0b41e | -8.99069 | -45.69324 | 2025-08-06 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eb93e67f-2f67-37d7-a35c-939a204a75c6 | -11.42995 | -45.1292 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ea3e2644-e916-3614-b134-06ac2383d00c | -11.91025 | -44.95298 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cb5d1d1-3b82-3962-8539-8a3cb4dfcf95 | -11.43407 | -45.14073 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8f874c09-020f-3a87-9f30-cd027a2cd8db | -10.48054 | -44.34375 | 2025-08-06 03:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 729edabf-fd25-3922-b62b-d850f0fdcbf1 | -11.84243 | -43.72352 | 2025-08-06 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e28ddf28-1f4b-3bc5-a1e9-f7a105c8bf03 | -9.07414 | -45.05229 | 2025-08-06 03:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2db320ad-684d-3dfc-be2c-bdefe0f756b6 | -15.11786 | -47.43317 | 2025-08-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a0f1bdf8-09d1-3845-a83c-fed2e21e895f | -11.91105 | -44.98034 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5be749aa-82b3-343d-8db5-8ed23084e14e | -11.91114 | -44.94855 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af9b6c31-bd71-303b-91c0-aea9271efab1 | -15.62633 | -39.25117 | 2025-08-06 03:32:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cc5f1d72-cfeb-3b72-a556-396e3e9c5a91 | -12.97518 | -44.88116 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f707d88-bcb5-3ec5-845e-bdedb57e7a5b | -10.47968 | -44.34827 | 2025-08-06 03:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aad659e5-631e-3eda-b42a-34477de6c34c | -10.46534 | -44.39055 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10b6c945-0cbc-3e47-a1f0-c97e6b080914 | -10.48118 | -44.37299 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ae758c7-3052-36ae-941a-d687a242a9bf | -15.64256 | -46.96099 | 2025-08-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2b7faa7-f7b1-392e-bd17-1c4532d4d758 | -10.44312 | -44.37616 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 593b229d-928f-3c57-8f72-995993aa884c | -15.54176 | -42.65619 | 2025-08-06 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8014b1fe-c4a7-34b7-8f81-91e2484ab640 | -8.87791 | -44.7929 | 2025-08-06 03:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6073de57-9f8f-3101-8f2f-e8d90be0c9a1 | -10.64979 | -45.24154 | 2025-08-06 03:32:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e11ce093-3d75-3ac4-adc9-ca84a2d81a27 | -11.43927 | -45.14688 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0aaeb065-07d1-39b2-9504-b58ffeddf9f3 | -12.97773 | -44.88383 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6938e7d4-99e3-3035-88d9-d2bf3c750c1f | -10.4821 | -44.34638 | 2025-08-06 03:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eccd079-d525-3e2b-8cf9-687f17f91a3c | -12.76381 | -44.41468 | 2025-08-06 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3c26c47-2c60-387e-abad-9d005e00ed3c | -12.96838 | -44.88416 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb119a75-c514-3365-8b80-2b12e92f8ba7 | -12.9971 | -44.89499 | 2025-08-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c126360-c7e5-308a-8ec7-b0917fb30f01 | -12.89508 | -43.79044 | 2025-08-06 03:32:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b026f69-b182-35ac-a897-92f7b01da468 | -9.07224 | -45.06235 | 2025-08-06 03:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a5d1103a-5a0b-3f05-a569-7c0b3b08e85f | -11.44033 | -45.14164 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b8c27270-9516-35cd-b79b-28c4ca5383e4 | -10.48299 | -44.34193 | 2025-08-06 03:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b7d54f5-0f4d-363a-8c64-815866235296 | -12.76296 | -44.4189 | 2025-08-06 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36049d72-a26a-3fd4-b965-070b026e8d8d | -15.1213 | -47.43252 | 2025-08-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2f1abe3e-2beb-3cf0-99ea-74ac4ba754c0 | -12.53308 | -47.17943 | 2025-08-06 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 56fe1056-536e-32d5-8606-de5e1e042209 | -10.4398 | -44.36108 | 2025-08-06 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c347195d-5e5d-3958-994f-15ac80bfa532 | -14.47301 | -43.25456 | 2025-08-06 03:32:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a75166d-4989-3621-bde6-178db1732df9 | -12.40501 | -44.70494 | 2025-08-06 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37fc2d2c-971f-3545-ba06-ae1761f257d7 | -11.75648 | -44.95942 | 2025-08-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65f6e17e-3977-39ee-a286-dd247e8133d9 | -9.07508 | -45.05346 | 2025-08-06 03:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e0eb8ed-1700-39d9-a461-fc935041443a | -15.11919 | -47.42723 | 2025-08-06 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5f8a737a-b6a7-3f80-9af7-3ba756fc877c | -8.984 | -45.69206 | 2025-08-06 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bc169d9-ef61-3099-af52-658dbe8c1f66 | -10.64346 | -45.24034 | 2025-08-06 03:32:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a8d44d0-0945-3f41-88bf-3235cf7a3288 | -21.07817 | -49.99249 | 2025-08-06 03:34:00 | NOAA-21 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8019e50f-202b-392a-b228-d5882d2555f3 | -23.31029 | -47.49236 | 2025-08-06 03:34:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7664b411-aada-3b9e-8625-ce90003ae478 | -21.31148 | -48.56748 | 2025-08-06 03:34:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77fd279c-7ee6-3453-976c-757d9a557428 | -23.31699 | -47.48947 | 2025-08-06 03:34:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 97f1995d-afb5-3f37-9f9d-0289345c3d07 | -21.68703 | -47.36195 | 2025-08-06 03:34:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e2049a5-0616-314a-9675-f28fa722cf3d | -21.06979 | -49.99703 | 2025-08-06 03:34:00 | NOAA-21 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5dfa8d0f-c256-3716-9d8f-b221253f3a08 | -21.68835 | -47.36405 | 2025-08-06 03:34:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 269d6511-d72f-3da2-8e43-760dca0b7e20 | -13.0731 | -56.8527 | 2025-08-06 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 77a5ab3d-384d-33bc-8b55-d88c3a62c2e2 | -8.9215 | -60.7297 | 2025-08-06 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| cb809aee-e935-3aad-b748-bbeceaceed11 | -11.4389 | -45.1385 | 2025-08-06 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1236b4b1-2886-3234-bfbf-99019434f8fa | -13.0728 | -56.8729 | 2025-08-06 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a525e638-6fc1-3131-9fbb-582cde518472 | -15.5541 | -49.9016 | 2025-08-06 03:40:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b120c7ef-6456-3e37-89b5-2555250f7d9a | -8.9213 | -60.7489 | 2025-08-06 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 11b958da-f23b-3b86-aed9-17b57d1bc6c0 | -11.4393 | -45.1154 | 2025-08-06 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 98ece837-6b00-3273-bf74-2b09abfcf6eb | -13.0728 | -56.8729 | 2025-08-06 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7905720a-eada-3c89-b5d9-2280807d4576 | -11.4389 | -45.1385 | 2025-08-06 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5e5041ae-219a-3ca9-917f-1cb1448a3741 | -8.9213 | -60.7489 | 2025-08-06 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| cba77ade-d548-3996-811f-de6e1699fe6f | -8.9215 | -60.7297 | 2025-08-06 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 744d14a4-b386-3d3a-9ea8-82ec58519cfd | -8.9028 | -60.7498 | 2025-08-06 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1114c8a4-f5dc-3a17-9075-1577bd031be1 | -13.0731 | -56.8527 | 2025-08-06 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e0b233ab-7f19-30fb-9781-ddbb37177847 | -7.36619 | -44.15935 | 2025-08-06 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f9e8f9b-2701-3275-9768-8a81834f7786 | -4.77804 | -45.33086 | 2025-08-06 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91a5f55b-001b-39e7-9070-d31a37f47b6b | -7.57677 | -44.90435 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb748353-596b-3c24-a6b9-2f18a8af8d6f | -4.02418 | -48.06416 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a764b0ed-c6c9-39b7-922b-0100596f654d | -6.73178 | -43.57366 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 276e4937-4771-329c-b8cc-503ccd4b9775 | -7.52308 | -44.85176 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baca98f8-576f-372b-9c74-f81f00062f27 | -7.58413 | -45.31091 | 2025-08-06 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3989616f-4a41-38d9-8232-f14682f0689a | -5.42523 | -47.15242 | 2025-08-06 03:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44452d89-16f2-387c-9b8a-e929408349b5 | -7.06754 | -44.3886 | 2025-08-06 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dee9e6b-8b81-37df-ba96-a2218583af63 | -8.00108 | -43.14226 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 82e70c40-06f9-3009-9c42-476235cd784e | -5.93787 | -42.5623 | 2025-08-06 03:55:00 | NPP-375D | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 43048b47-d1d2-363a-9bea-69f27cd3d927 | -4.02346 | -48.06824 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf7461d0-038e-37f5-88be-7421d91b768f | -6.85507 | -41.70341 | 2025-08-06 03:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c0d122b-214c-301b-ada2-d1b91d18b8d1 | -6.95781 | -41.57919 | 2025-08-06 03:55:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 756caf9a-7d66-31c1-9c3d-f378b2ef4a97 | -7.90686 | -45.53198 | 2025-08-06 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b17dbb78-f102-3a3a-a066-f52ca6011cb9 | -8.00822 | -43.23898 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b56b7c26-59d4-3c81-8147-0178be706b66 | -7.9867 | -43.15273 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d407884a-8b9e-31f7-9265-2cb30be8274e | -4.91397 | -39.81429 | 2025-08-06 03:55:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5cc0a37a-25b4-3aa4-8bb8-f8dad08a7681 | -4.02925 | -48.06924 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8840efd-72d3-36dd-99ed-4ae9ecba47ac | -6.4837 | -45.55151 | 2025-08-06 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d6f3a1d-4b51-3e96-bdd0-6bfe5eaa1b4f | -7.5135 | -44.85472 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b1dbdbc-8bb3-3449-a233-d3e8f06e803a | -6.95309 | -41.58427 | 2025-08-06 03:55:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db82932d-0649-3a2e-af92-a94dc7b86692 | -6.48843 | -45.55212 | 2025-08-06 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
