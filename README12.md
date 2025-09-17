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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6aa526d1-6527-37b6-b11e-1db424577924 | -11.50736 | -43.63378 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07bf17d2-bb59-3961-bec8-6c2dde625889 | -12.99214 | -47.94197 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebe8b104-9c39-3c50-8bb6-7993e6f268e9 | -11.47198 | -43.56965 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 686d75a5-3020-3ca9-a95d-030b87201d27 | -12.72858 | -48.02144 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f363fc2-fb27-3cd6-b7ca-e1798519dea4 | -13.32629 | -43.09869 | 2025-09-17 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f2110de4-8865-3bc8-bcce-ec97aac73aa1 | -8.68529 | -46.37645 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 348c98d4-7fb2-322b-acc3-e83c2ce65fd7 | -7.88248 | -48.16179 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0666804-2bec-35dc-8403-0a03a8004493 | -8.47174 | -44.727 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0c31b7b-2d71-3427-b781-81aeb1c77e18 | -14.15405 | -46.13952 | 2025-09-17 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ed667ca-91b6-38ac-a16e-686e412c1a6e | -7.60905 | -47.47232 | 2025-09-17 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a09326c9-75e0-34d4-a516-c4c1c007d68a | -14.47593 | -46.35712 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa67855e-8a30-35b3-a198-351918e891ca | -8.00968 | -45.65521 | 2025-09-17 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ad16f70-0f57-326f-89da-903ec80d577e | -13.3282 | -43.10007 | 2025-09-17 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 86282990-929d-32e8-b7d8-ccb303ec8296 | -8.13269 | -43.64254 | 2025-09-17 03:45:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03946785-42f8-308a-a6ec-f5620bd469a2 | -14.60788 | -46.37681 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ae11595-e2cb-3baa-b79e-d2276ab47405 | -9.05583 | -44.87762 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e105ff4-75cf-3f86-b217-a9ce512e95a5 | -9.09571 | -44.92679 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e6d68dc-8152-3a06-8322-65a9a675a506 | -9.08117 | -44.94687 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 801323a1-974b-33b8-a2d1-777b01cecdc8 | -9.08641 | -44.94778 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aec10ca-2bba-3af5-b127-9ce08a8a2e62 | -9.09981 | -44.93385 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50ebc672-5030-3720-a110-7f28d19a2ac7 | -9.05648 | -44.87404 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 064f8118-1d51-36cd-931a-1c0b9d0bbd26 | -12.60281 | -47.9849 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f313ceed-74d7-3d4d-8969-7575be7d573f | -13.17869 | -44.48453 | 2025-09-17 03:45:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c280c0e-2ad5-3417-9823-bf4469680e07 | -14.60851 | -46.40101 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 25b53471-7ca5-3198-9f99-77c7e2c15bac | -12.70168 | -47.95624 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d6a83479-ee9e-36db-b18d-46abd3641892 | -13.49666 | -43.67402 | 2025-09-17 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97722737-5426-3125-8e5a-41e1ffcbe5d7 | -11.12046 | -45.11962 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81c20b9f-5cf4-3d20-96fb-a8bca342bf7c | -7.82755 | -46.15372 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 42810dd3-376d-39ee-ba4b-5c779940ddce | -8.01033 | -45.65163 | 2025-09-17 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0aab1235-9f59-3b79-a1a2-2e56f73283ca | -11.49629 | -43.61666 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bba301e5-49ec-3bee-9ff0-2b0fcbebb615 | -9.04949 | -44.88289 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16884d95-5daa-317c-bc25-fe86b3e16a9c | -13.22478 | -47.29493 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f755bbe9-44a3-3015-a019-3b152a87fb4c | -11.07472 | -49.75383 | 2025-09-17 03:45:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e4b85a3-1c36-3de7-8998-a3d6fa48227e | -7.85972 | -48.17461 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4c6f11a8-a342-37f1-800d-8770555b7e08 | -12.99131 | -47.94605 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9584231-a173-36e1-9c01-69db26097250 | -12.72653 | -48.01842 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5b88355-6961-3ca5-8758-8f76381c5d70 | -12.60689 | -47.98306 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b48bc458-71e8-3fe7-a710-0de50d7751fc | -11.03978 | -42.25369 | 2025-09-17 03:45:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d806f58-748f-3f26-a4ca-798a5ad50dbe | -12.10962 | -44.81014 | 2025-09-17 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3aa4685c-197f-3557-8a91-d3eae2daf81b | -11.59822 | -49.82035 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b89d8b41-47af-3469-8249-70064345f4ae | -9.07576 | -44.9468 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dd73e08-2599-3261-96eb-8f82786912d4 | -13.85769 | -44.89077 | 2025-09-17 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1427dfbc-2748-38d7-b546-073ca31e1931 | -12.7122 | -47.98019 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c5ca5b9-abe4-36a7-82f2-982ed220a2df | -11.77568 | -44.7437 | 2025-09-17 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 527f3ef8-2fb7-3ff0-8404-e1d3f911522a | -11.49172 | -43.61812 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4ab3df4-1c99-3d07-875b-ea11a93d8093 | -7.72832 | -45.29753 | 2025-09-17 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 834346b3-7fb3-331a-82cf-5a2284d643f4 | -13.65182 | -44.26406 | 2025-09-17 03:45:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55764227-89a0-3ad2-86a5-d28d5d12fa10 | -14.63288 | -46.38728 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bb98428-f8d3-329a-8032-b79c73b1b26b | -11.07594 | -49.75443 | 2025-09-17 03:45:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f02747fd-771a-3787-a65d-b760fb36a8d6 | -9.05273 | -44.83541 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eccc510-9510-3078-a8b2-ca89e5c32227 | -8.56626 | -46.33994 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f841214-62b6-3969-905d-3a5df455f1a9 | -14.63226 | -46.39044 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b5e8fbf-c7fb-3055-b731-a391aa1fe375 | -12.99059 | -47.94959 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f77a9263-5f20-3919-b916-f670e27d0577 | -8.137 | -43.63007 | 2025-09-17 03:45:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6db47e47-1df5-3d44-9c18-5eb4a4453cd1 | -12.28042 | -43.82984 | 2025-09-17 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 355f35ab-0f2b-3a93-ac32-fad85169dc4a | -7.68026 | -46.63704 | 2025-09-17 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6668398-2ce0-3b00-84d0-643890fb1db9 | -7.88689 | -48.17422 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 869cec13-3fe6-3f7f-83a6-65f73e372dc1 | -12.71628 | -47.99055 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fe10dfc-b224-3bcc-8517-803e574eb06c | -7.71732 | -45.29573 | 2025-09-17 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53f98630-db91-3e33-bfcc-97a3b77bf02f | -11.12156 | -45.11378 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28bc8f3b-70d3-36ae-b64a-d186cba0eed9 | -9.37625 | -40.41885 | 2025-09-17 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87179eb0-911d-3d82-95f8-2b7d6dfa1738 | -8.93822 | -44.49189 | 2025-09-17 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2da293a3-a6a2-325a-932a-3c86c9b656f8 | -10.29883 | -45.36471 | 2025-09-17 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 006e649e-1295-3169-8a26-2b0eb2e3d9a4 | -9.07519 | -44.94998 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bfd1e9e-a2c8-3e24-ab0e-e6ce892d2674 | -9.04823 | -44.8898 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 695c7032-fde3-3030-8eb9-3ee6b2ee1b01 | -7.72766 | -45.29916 | 2025-09-17 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b996648-c5e3-309f-a2fb-9aec51d22687 | -8.68023 | -46.37141 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8923eea-2f5c-3738-8c0c-450aefd9b92e | -9.04887 | -44.8863 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1269cf56-eb22-3442-bab6-cd236788226f | -9.11618 | -44.90372 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3aa500d3-ae56-3f1b-b8c6-b553cb5fbeb3 | -12.71315 | -44.67286 | 2025-09-17 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75b8deb4-82aa-3a7f-bc43-b72d442628b8 | -15.76855 | -41.61171 | 2025-09-17 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f5c9bd53-8333-309d-bdf4-e765d9e1b165 | -14.20759 | -47.00986 | 2025-09-17 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 857c1fe8-ce20-3bdf-81ec-28fe99058b80 | -12.71313 | -47.99205 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 570188da-5fb4-35b0-910b-1f7c318b1f50 | -12.98452 | -47.94915 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea475d56-2ca6-37f8-8979-eb86cb77197d | -8.16403 | -46.76532 | 2025-09-17 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2288cc5-9870-3e86-8e44-d820cb84912a | -13.62899 | -45.36874 | 2025-09-17 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 915db1af-7153-3d7f-bc01-bd5cc01d597c | -12.36118 | -47.05943 | 2025-09-17 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b99af4d-b9f1-3358-b543-e0a58181b61d | -11.07344 | -49.76019 | 2025-09-17 03:45:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fda2ced-5248-3c49-b55f-0093bbaae350 | -11.02804 | -45.06229 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 662b263e-eafd-3968-a774-5347a86ab164 | -12.71941 | -48.00553 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b79a237c-3b00-3f43-924c-ba17967f68f1 | -13.22562 | -47.29073 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebbbebe0-02b3-3f91-ac67-185cdc66e21a | -9.11609 | -44.87499 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70d0752f-18e2-371f-9317-cf76c7b3072b | -12.72508 | -47.99434 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7a3acc45-52bf-3d14-8544-9280847863d7 | -8.47117 | -44.73009 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bbb87c2-bdfb-3b69-83bd-d16b8ee99716 | -8.97295 | -44.19132 | 2025-09-17 03:45:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f178d4a-2215-33b3-bbd2-dd6278b5fbfd | -9.49883 | -37.96816 | 2025-09-17 03:45:00 | NOAA-21 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 056c33e9-a5ce-33e1-986a-a7bb87b8bac5 | -9.5891 | -45.66589 | 2025-09-17 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7360b05-60c5-305a-baab-c807336c0f27 | -14.60237 | -46.3229 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74502fc2-1c16-370e-90e4-ae97ce376709 | -8.68455 | -46.38046 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84c82f5f-f034-398d-b043-2ef4ee89d4c5 | -12.6009 | -47.98194 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 101e4b55-fdaf-31cd-878d-505a70eb111d | -12.72446 | -48.01118 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 59f2a458-9d20-3787-9973-aaf1eef9fe3c | -12.86417 | -47.1353 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abbe7fcf-292c-3311-b605-87db15727d98 | -8.99246 | -45.75489 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d59c334-2619-36ef-8970-5613fcbddbdf | -9.11563 | -44.90667 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28bd8360-30c5-342e-a530-13dc608b783d | -9.36942 | -45.38035 | 2025-09-17 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fddb7e61-a8ff-3da1-bc2b-aaf13af27bce | -15.72153 | -39.32034 | 2025-09-17 03:45:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 82cc326b-1d7a-37a1-b524-a7267209d7e4 | -12.70252 | -47.952 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7aface82-54d5-3adc-8c5e-fcd4e9130b71 | -7.37755 | -47.04498 | 2025-09-17 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33b76ec3-afbf-387c-9eea-591f07ffe484 | -8.62364 | -40.19822 | 2025-09-17 03:45:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8bfb9a1a-bf41-30e2-ba9c-91163aca875b | -7.889 | -48.16309 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README13.md)
