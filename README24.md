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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 629cb8b2-3e9b-381b-833e-fb1b05665b81 | -2.91791 | -48.30333 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c95528f4-116d-3c01-b7db-bd88a0da053a | -3.91748 | -47.68513 | 2025-08-22 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64dab2e6-8d34-3740-a229-5c6a401d1aaa | -4.82294 | -47.31625 | 2025-08-22 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a80035f-f87a-34b7-8913-248464bae1a8 | -2.5833 | -51.92289 | 2025-08-22 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 897f051f-d160-32f0-add3-403377fd919f | -4.40112 | -44.08368 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c53bd3d6-7bc0-3d90-99b3-02806aaffee8 | -2.38925 | -47.65976 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 245be9f5-71dd-3703-8243-b2d08f8c8115 | -3.98723 | -42.51315 | 2025-08-22 04:17:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8dd1ce16-45ae-34c4-9ad3-82fc10f04bf0 | -2.91405 | -48.30272 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae8daa42-938a-3463-99d4-b03690d55493 | -3.483 | -47.68433 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b47555b8-5e0d-3eeb-b1c1-a6ee05df1526 | -5.25724 | -40.73072 | 2025-08-22 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e8ea08ec-5ff5-3d71-b26c-327f10144b7d | -2.91329 | -48.30752 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0bd50f9-c497-3db1-8593-df773365e0bb | -2.93186 | -53.69538 | 2025-08-22 04:17:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b11188c2-aeb8-3b8c-9167-3caa144f1cef | -2.24917 | -48.06968 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19797b6f-f3ba-33ca-9663-40bd10992b36 | -4.64627 | -43.12176 | 2025-08-22 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 97a78f5e-7d7e-3e62-9ef9-a2d86874703e | -2.94167 | -49.46284 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c51a2f0-2fcf-331a-b152-6d296753bed3 | -2.25734 | -47.85053 | 2025-08-22 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 52499399-0720-3abd-8f46-6333106fd939 | -4.64239 | -41.40391 | 2025-08-22 04:17:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9174a5aa-e3c7-3156-84bc-e70fe83004f4 | -3.58255 | -49.54506 | 2025-08-22 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b60e49e0-2f65-38d9-bfea-6324349dba2b | -3.81859 | -41.56179 | 2025-08-22 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cce04bc8-87e0-346b-9874-82502ecea63a | -4.42699 | -47.75608 | 2025-08-22 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8119abf2-4c58-336c-9bae-9241a1228f3b | -3.17247 | -49.48032 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b77585b-5e83-3d3c-abaf-c4f8feb0276b | -3.38689 | -47.60823 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4a930a7-30f7-3a22-b78f-a84e8c95604c | -5.37288 | -36.75835 | 2025-08-22 04:17:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1447a921-6d2e-350a-805d-b005f2908d3d | -3.58194 | -49.5488 | 2025-08-22 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f16bf88-5077-3075-9155-b3ba604b0212 | -2.81126 | -49.20672 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c51c0284-6278-392f-aed4-6b875521ad9c | -2.81186 | -49.20305 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f47f8e57-d887-3513-ba92-dd72eedd3429 | -2.96789 | -49.2989 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebe92b2d-f337-3c29-b389-ad43e769bbac | -3.42422 | -43.33917 | 2025-08-22 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fae340a-931b-373b-8c9e-ea215be9f737 | -4.40388 | -44.08764 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1190ee9-dc02-3ef8-a965-495ee439be60 | -4.40573 | -48.94416 | 2025-08-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b54677f0-f5b1-3dd6-9799-0c3b2bd09bad | -5.49111 | -42.16277 | 2025-08-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c8a254c-f956-3c12-b6c7-d42cf40b31b4 | -3.23456 | -46.78529 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3c85f49-e02b-32d7-8be6-4e18d816a6b7 | -3.83466 | -47.73572 | 2025-08-22 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c38fd3ff-f87b-3d39-98de-d3eeb70a7d5c | -3.81678 | -41.57355 | 2025-08-22 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d08349e-cf47-303c-bcf4-3cbddca18fab | -4.72029 | -44.34234 | 2025-08-22 04:17:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50c88d94-da4e-38b5-bb52-70afd5060366 | -3.30113 | -52.64961 | 2025-08-22 04:17:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2893995-c4a8-3b83-84f4-fe2e5eee4701 | -5.37093 | -36.75823 | 2025-08-22 04:17:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d20f2d9-22bc-3c7a-9823-977491440c35 | -2.55093 | -47.71157 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ca664c4-ef92-36ef-9d39-46ffb8dd7ee3 | -4.14153 | -46.46192 | 2025-08-22 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a139ade-c2dc-3351-a9ef-90838bee9063 | -4.48811 | -43.81072 | 2025-08-22 04:17:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd4c939c-ff07-3321-8722-8c7a0a0bf881 | -2.78628 | -49.59512 | 2025-08-22 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb90842c-7fd0-3af1-a567-898a4137a36a | -4.95799 | -43.04574 | 2025-08-22 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03c5c359-468f-3edd-836a-ae472520bd70 | -2.1101 | -47.11829 | 2025-08-22 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d69e9c-0a51-30a7-a6d5-0303b67e4309 | -2.47235 | -47.19575 | 2025-08-22 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53f61f20-f385-3923-9f39-6f1c3e0f2f80 | -7.60445 | -44.38091 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e93326e-02fc-3ab1-8d9f-30c41402f24d | -7.62093 | -46.26912 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 480cb5f8-6f4b-3fb1-9a0f-e3ea8212fed0 | -6.63224 | -47.90418 | 2025-08-22 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 52ec876a-c62c-3068-abb6-809665b59181 | -6.16044 | -53.77485 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40987999-bff7-3d50-99c1-a9157c155241 | -5.7972 | -45.18147 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64176f7b-2cc1-364a-a975-fc074082fce3 | -8.1204 | -47.14796 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3bdded6f-0bda-3ebc-b73c-2188253356b3 | -6.25169 | -53.68718 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b7691c-3a3d-3a51-b9f1-74c0e7ecb637 | -5.95852 | -43.33078 | 2025-08-22 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7bc0ca5c-2fcd-3719-9853-2e4f171c63b8 | -10.72879 | -48.25142 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9c51f3ad-5c74-398c-8648-d4e470ccb2ae | -7.61275 | -45.25732 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12fa8420-962e-3d36-9174-90c41be6f8c9 | -5.88585 | -53.62006 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a3268dd-269f-3bd9-815c-d21624674d0a | -0.74748 | -47.75238 | 2025-08-22 04:19:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd9fe6eb-990d-3e8f-a7a0-912de06fc258 | -10.85941 | -50.82083 | 2025-08-22 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dc6580a-6b28-3e23-b3b7-de48e15c0fd5 | -5.78717 | -45.07318 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58c3561c-b398-3453-adf1-c981dc98266e | -6.20292 | -43.56882 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08c34af9-0211-3149-991a-673549474a51 | -6.97226 | -44.16712 | 2025-08-22 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e669d4f6-315b-3eaa-b57b-0e633ec20043 | -7.24568 | -44.6986 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11f5795a-641a-319c-aade-5c8f05bebd4a | -8.75089 | -45.47155 | 2025-08-22 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6175bfa7-6979-35ab-b141-5c25268de462 | -5.42703 | -46.36339 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b57807a1-e835-3728-a198-ac2f11b24c61 | -9.13787 | -46.38901 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe690329-9f21-3af9-82f4-323306d93f4e | -7.25121 | -44.70657 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d830bd5d-8010-343f-9820-6a61005ab923 | -6.01451 | -42.85646 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2a64bd94-6846-3c19-bf69-7bfd59f444be | -6.07714 | -44.13762 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9011a979-99ec-332b-8cc2-2a6447ef9d00 | -12.97056 | -42.5313 | 2025-08-22 04:19:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26106a1c-ea9c-362f-8cda-13deec234b87 | -6.26499 | -53.67258 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cc1762c-b36b-3ba6-b551-dd2ec0cbd78e | -6.55365 | -42.99423 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eec20ed9-176d-36db-a597-612f76ebe330 | -7.61496 | -44.37896 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ec2fad7-ac78-3040-b291-c7407ad83640 | -10.72157 | -48.22987 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ef18d1b-3fd1-32b5-ac64-2e292fae7fb9 | -7.94307 | -42.65755 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 303daedd-5f38-36b3-91cb-78f5ee11ad77 | -10.19285 | -47.56127 | 2025-08-22 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ce464c2-7f97-3657-b070-5f5e67b9345c | -7.15291 | -44.66261 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3d244bc-4eec-38d9-a214-31d617adb47a | -12.6769 | -44.95981 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce285fa-ceb7-3534-9625-64718f9e846e | -7.63257 | -45.23912 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 20d4c447-2553-3a54-93c6-d34faec5051d | -3.737 | -53.98434 | 2025-08-22 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd1a2123-194f-3baa-b3ec-1d7f7d29115f | -7.16506 | -44.67162 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ef80a46-36e9-3b7b-b4f0-255e21b7b05e | -7.15513 | -44.67006 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da2932e1-c77c-33ba-97f7-35781c35a6bf | -7.94492 | -49.88187 | 2025-08-22 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 981226ca-1eb9-3956-a880-514f525318d2 | -6.43068 | -44.67558 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 406491cb-e540-37f9-badb-9c2750a7c58c | -8.28919 | -47.27467 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cb71238-c41a-3cc2-ade7-296f2b9270c8 | -7.85909 | -47.00613 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b76a78ef-a44c-3462-bd5b-96733d2ece25 | -10.73775 | -48.2406 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ed241b6-0e40-3042-8764-ed689d30fa91 | -10.45787 | -48.8059 | 2025-08-22 04:19:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b8cbf25-4fdc-33da-aea4-9fe91f631a24 | -12.68026 | -44.96034 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab7f528b-dba5-32fe-869b-c88e0f717c20 | -8.29202 | -47.27901 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7df4cd41-bd04-30d9-9722-6fb0238e2bda | -9.20654 | -59.452 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff97cb6b-3f58-3234-8193-134e0fcd8332 | -6.02689 | -44.37113 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12fd25b5-6ee2-39ef-81f1-22c9232995db | -7.85872 | -46.98686 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| acd20e3a-3eb5-306a-a52e-9071d9b54490 | -11.31757 | -44.94911 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26f96d00-835b-3449-9b43-efecfb07bd55 | -6.01445 | -42.81142 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 10bb5892-6b6b-3f4e-bcfa-521fddcf8b6d | -8.85245 | -52.0451 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d11c240-da47-3c8f-a26d-0dcfbf877e57 | -11.01811 | -45.63114 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32748d85-7063-39c3-970d-ce67d42cba2d | -6.0649 | -44.10729 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57d2099a-bbea-3d29-bf20-0729a2c84112 | -10.88465 | -45.22538 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33038b21-335a-3532-9b8e-25cc9d106961 | -6.34757 | -43.37905 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acf6e17c-a557-33c7-b594-c6fdf268449f | -6.27004 | -53.70472 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9db7327e-ca18-3a1c-ae94-289048072a45 | -6.29302 | -43.68792 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
