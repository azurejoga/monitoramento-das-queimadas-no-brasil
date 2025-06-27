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
| f1f92f73-dd27-314d-8135-fe9322e4a57a | -11.5776 | -52.136 | 2025-06-27 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 888c8677-8a59-32d4-a69b-b21072183d21 | -11.5592 | -52.096 | 2025-06-27 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d7948540-93a9-363e-bcd7-e3b231746cd3 | -6.9791 | -42.9034 | 2025-06-27 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 183.8 |
| 42c192b3-0dec-3bdd-a1a4-d876fc7e7a3d | -11.559 | -52.117 | 2025-06-27 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| ba7dc3c4-f9d2-3c3a-8c8c-8f84e680fc66 | -6.9605 | -42.8816 | 2025-06-27 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 299.3 |
| 1e2f5c2d-b243-3714-9288-86a7205bb8c2 | -6.9602 | -42.9052 | 2025-06-27 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 395.5 |
| 7b410207-4a35-31c6-8047-9d0430dc80d4 | -6.9414 | -42.907 | 2025-06-27 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 1f1b97b7-11a1-3187-b1df-484871e9b190 | -11.5779 | -52.115 | 2025-06-27 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 441.5 |
| 1b25486e-90d1-3634-8fdc-463d32d814a6 | -11.5776 | -52.136 | 2025-06-27 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 1a91625c-774d-3481-8ba0-30d9a7036ce5 | -11.5969 | -52.113 | 2025-06-27 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2d776c37-c798-3e77-b9be-f7a2c6ca2077 | -6.9793 | -42.8798 | 2025-06-27 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.5 |
| 46e85486-4616-304b-b3a6-f9a09e91a28f | -6.9416 | -42.8834 | 2025-06-27 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 9d6de38c-fd7b-3020-8023-64684623a4d0 | -11.5782 | -52.094 | 2025-06-27 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 27539be4-183b-396e-9c4e-5a70b29ca26f | -18.95524 | -39.91312 | 2025-06-27 03:10:00 | NPP-375D | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 641b8735-4f11-3e55-a857-8565adc2e460 | -18.94939 | -39.91172 | 2025-06-27 03:10:00 | NPP-375D | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| acfa688b-8f5b-31b0-bbb3-c92cc287f2f5 | -22.50814 | -43.50393 | 2025-06-27 03:10:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d7a905dc-608b-3a19-872e-2e54ff9e5400 | -18.7486 | -40.07561 | 2025-06-27 03:10:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f4ace1fb-26f5-3418-aeff-606ab687445c | -22.67662 | -42.85666 | 2025-06-27 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 63a076a8-9ea1-356d-ac98-a99e6fe3484c | -22.6752 | -42.86242 | 2025-06-27 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 134623e2-9711-3363-925a-d928fd404d46 | -18.75451 | -40.07711 | 2025-06-27 03:10:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ed04cbb6-ce60-3ba4-9fac-d45cc1899571 | -22.5064 | -43.51081 | 2025-06-27 03:10:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4cd7d280-ed37-3cd9-ab8e-d30e5cef5797 | -6.9414 | -42.907 | 2025-06-27 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 3eaefc3b-46c9-372f-83bd-19c11b05be93 | -6.9602 | -42.9052 | 2025-06-27 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 364.3 |
| b563bd45-a417-3ab1-b617-3c6db7f29bdd | -11.559 | -52.117 | 2025-06-27 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 52e5e4d6-0a22-3bcb-98c9-ab099f8842a5 | -6.9605 | -42.8816 | 2025-06-27 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 358.1 |
| 20ee87be-336b-396c-afa5-a8163f22d378 | -11.5592 | -52.096 | 2025-06-27 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9249a5ae-4b5e-3525-bf53-2dded5cef661 | -6.9416 | -42.8834 | 2025-06-27 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| d03317c2-7039-302c-83f5-85a37f8b3b03 | -11.5776 | -52.136 | 2025-06-27 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 61068e9b-9b51-3c9f-9fe9-bb5732eb174b | -11.5969 | -52.113 | 2025-06-27 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8ed99393-5344-3311-b3e7-38b9b2c4c248 | -11.5782 | -52.094 | 2025-06-27 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 8c465492-73d7-35d6-acdb-57a454f0094b | -6.9793 | -42.8798 | 2025-06-27 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 153.4 |
| 99175dbc-41cc-3358-85cd-55bd3cd11857 | -11.5779 | -52.115 | 2025-06-27 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 358.5 |
| caaf1fa3-1d77-3c9e-aae4-3234292b37ba | -6.9791 | -42.9034 | 2025-06-27 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.7 |
| ebf630b3-eff6-36bf-bdc2-12a9530a150f | -6.21675 | -43.35891 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 139ad631-8b70-3227-8fc9-1cd3f198ef7a | -7.21394 | -43.08299 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| c50dcdcb-dd6f-3dd7-a192-b1314355f158 | -7.54579 | -45.83391 | 2025-06-27 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f21803f9-7d12-331b-b5b5-a4c5cc64e783 | -6.95687 | -42.88821 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 0213daed-b5cf-342d-9668-398c06bfab93 | -6.97368 | -42.89592 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.5 |
| b4cb2b52-a363-38df-89dc-7fefc196aef7 | -6.95437 | -42.89356 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| eb1a397c-ae61-3f15-9512-e1853e631a0c | -6.27737 | -43.67921 | 2025-06-27 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bbab4b4d-5a6b-3ad3-8f92-c1dcf4dfc580 | -6.47393 | -43.75552 | 2025-06-27 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb2e7548-650a-3dd7-bd12-f0a5478878e1 | -7.20958 | -43.07336 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 538e909f-8cb4-326a-a161-2fcf09a268aa | -6.95455 | -42.90119 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 6d127410-c01e-3441-b856-f9717fb683bb | -6.97118 | -42.90116 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| e77e95aa-e3ee-3971-a7f3-7215c85e2abd | -6.96609 | -42.89584 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| e4615b3a-b888-3f87-91a5-8300d270ffe7 | -5.0697 | -37.7178 | 2025-06-27 03:28:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e150778e-b213-343c-83ea-7b7d5c113d3c | -5.91848 | -43.47158 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 649fd0fb-dd0a-3137-9a39-6dd8b5d04186 | -6.96271 | -42.88944 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 2ae55417-a4c8-3316-a230-47f68c4ff40d | -6.95275 | -42.90231 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| cd53de76-b22e-3c2f-8415-d591e5375e5c | -6.21613 | -43.36216 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d39aedae-dff5-3824-a4d2-fb77210a0de7 | -7.20803 | -43.08184 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 32635a05-3fe3-3dd7-a61d-8aeca0e23db4 | -5.91758 | -43.47655 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2da641e6-29af-30b4-9842-5e7326ba49e6 | -7.21831 | -43.09266 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| af190ac9-c0c0-30dd-aadc-7518e6463fc2 | -6.97272 | -42.89276 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| f4c8548f-0e04-326d-b6d6-fa9a4a8b5375 | -6.96435 | -38.5804 | 2025-06-27 03:28:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 250f6537-d56d-3f63-bfdf-6969ccb9069e | -6.96707 | -42.89904 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 303901f6-6d29-3e3c-bb9d-2eb6b03cfa78 | -6.2724 | -43.68441 | 2025-06-27 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0acd8cdc-cd2c-3e9a-87b8-2fd4e5899080 | -5.85482 | -43.64391 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b23b5d69-7a10-3a0d-9dda-fe89f7f73755 | -6.22228 | -43.36309 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d92f89aa-e7aa-3c6c-b275-3e0e68b3383a | -5.91668 | -43.48151 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b6c14faa-1bcd-3935-87eb-a004cb191b80 | -6.69266 | -43.06208 | 2025-06-27 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9595c72c-025a-3343-9f9c-bd2c2079fb5f | -6.95944 | -42.89896 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| b9685bc6-d0d3-396b-9c3a-8afe2584d631 | -6.96452 | -38.58226 | 2025-06-27 03:28:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2962416b-934c-3917-a04c-cb1563bd3992 | -6.96346 | -42.8852 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1dabeff1-827b-3b1f-867d-7777f3e029aa | -6.6851 | -43.0699 | 2025-06-27 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45ec48f5-7fcd-369e-9386-9004cdeb30d4 | -6.95023 | -42.89142 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 0ec05b06-2919-37f3-bcf4-d755718215d2 | -6.69108 | -43.07094 | 2025-06-27 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99d6144a-85f8-30e2-b91a-b430b893f5f6 | -6.96531 | -42.90003 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| afe079cf-23b0-37ec-aca3-69ec8bf2f822 | -7.54449 | -45.8407 | 2025-06-27 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f01c376-0749-33e5-86e7-f43e54317084 | -6.94946 | -42.89573 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 97296844-3b17-3701-b446-665c1b0d2f56 | -6.94868 | -42.90012 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 4d00f4c3-33d8-3c94-96ef-aa874f3c6432 | -5.85072 | -43.64695 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| afe37ff1-28f2-371e-bdd4-7977ca65c48a | -7.20881 | -43.07758 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 966ff30a-1b25-3c88-a7f4-8819212cacda | -7.53189 | -45.83142 | 2025-06-27 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 78760046-0cc4-3cf1-8a06-3a13fca77323 | -6.9693 | -42.88643 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 0825619a-b574-3193-861b-8fad292b6eea | -6.68428 | -43.0745 | 2025-06-27 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f3738a3-0afe-3ae2-9cc5-f5ef00991c47 | -6.97294 | -42.90014 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 9ab32b4d-8246-33f2-a0c9-4bf16dbae14e | -6.94849 | -42.89255 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb79d6d5-479b-32da-9572-524caecf40b0 | -7.53886 | -45.83255 | 2025-06-27 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1790e7a8-7bce-3a1b-b8b6-482271de7e14 | -6.47303 | -43.74645 | 2025-06-27 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b450e70-f0cf-3422-99df-66d3ce759c2a | -6.96856 | -42.89065 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 66a54852-18e1-341e-af46-20cf2e66ca20 | -6.96101 | -42.89047 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| 1d74bd93-9e1c-30c9-a002-2f5928e8d5b4 | -6.21593 | -43.36349 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f2f18e22-cef7-3265-8fcc-5c6fe6e2b862 | -6.47211 | -43.75143 | 2025-06-27 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe2534b9-5a04-3132-bb16-73c18c12bd5c | -6.96764 | -42.88746 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 7d086c18-450b-3c23-b87c-9b47af4cde03 | -6.951 | -42.88711 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c4e9bd8b-dab5-3b52-a55a-bfdfb55485ef | -7.54007 | -45.82622 | 2025-06-27 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c8226257-e14c-35fb-8f50-94894707119c | -6.96196 | -42.89366 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| b6284925-18c1-3087-b15d-9abcd48109e8 | -6.96023 | -42.89469 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 9343afa3-9dea-3402-9fbc-27eb3b570758 | -6.95517 | -42.88926 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| 0246fb45-a998-34ab-bf60-92af280fab8a | -6.2711 | -43.67826 | 2025-06-27 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e190c607-d1b2-308f-82c6-8945d382f5b4 | -6.97195 | -42.89697 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 3a215492-704a-3445-b601-ff1daded8788 | -6.96781 | -42.89484 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 55ff9ff7-1f4b-381d-9105-fa1a212662ea | -6.96179 | -42.88625 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| 083c4cfa-fa9f-3b5c-b28e-cb06fb6513f3 | -6.96633 | -42.90323 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 71b720c1-f16a-3609-8d3c-d76c59fda0d1 | -6.96121 | -42.8979 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| f6c2d290-cf3d-388f-bcdb-e2423361f079 | -7.19325 | -43.19701 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85defaf6-5896-3619-acc1-24635e31fcc6 | -7.20597 | -43.19484 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05aafdd5-8a6b-328e-8bf4-840e0fea98ae | -6.96454 | -42.90423 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 7d36cc19-91e1-35cd-875c-bd77db60da1f | -6.96045 | -42.90217 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |


[Clique aqui para ver as próximas entradas](README8.md)
