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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08649870-331f-3c8f-8ae1-c9718d74b585 | -7.06392 | -46.75828 | 2025-10-18 04:29:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 748c87ec-fea3-3b03-aaa3-f8ce703556f9 | -4.77616 | -46.61304 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15018ec5-30b5-34e4-9465-ff04445e1e67 | -5.88754 | -43.92096 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2f33edd-0b8f-3294-b61d-42451b3ad5f6 | -5.89401 | -43.90208 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6e6afd6-b0c0-34be-8cc5-0ae06ba656f9 | -10.10149 | -44.57427 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5a1723f-8042-356a-aa69-1501827e956d | -4.49961 | -50.45468 | 2025-10-18 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 464ae57c-2bf7-3714-a4a5-a50cde54c51f | -5.29358 | -47.93583 | 2025-10-18 04:29:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e15a6995-6945-3b33-86bd-e18218ba02c4 | -8.15388 | -47.98103 | 2025-10-18 04:29:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 991673fa-d362-3a1a-8db6-7acdf935d090 | -10.36905 | -48.06032 | 2025-10-18 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f80b3961-fcc7-35ff-987e-04a7abc514ab | -10.1682 | -44.53946 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 442f771e-8557-31ca-9ab0-0d500a0e57f4 | -9.22653 | -45.26758 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56f2079f-c499-34df-b44b-e4a4244cdcd9 | -3.79007 | -51.76717 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e5f97ca-a67b-3c78-9e0c-e58d3bffbdda | -10.16232 | -44.53048 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7bb269d6-a6bd-33b8-aa76-40e87854812e | -8.10293 | -45.43207 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38718caf-89e0-3b03-a0e9-4a6f64c2ca3e | -7.43092 | -46.89482 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc68b1e3-64a3-32e5-95bb-a6a59af02786 | -7.9347 | -49.36469 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6cb8269-ce07-31f1-a803-9d23cd2b1bfb | -10.48834 | -43.41102 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f799a5f7-1fa1-3524-87a2-2b5a2d10f110 | -8.24629 | -44.01266 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7669818e-ad81-3783-87d8-4b6e8389ed68 | -8.08876 | -44.1 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76ec3ad8-0e6a-38c0-b0bd-f1f342285b0a | -9.24771 | -43.76046 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 28a44e34-cc17-34bd-a5bf-075e26c76412 | -8.36891 | -46.20771 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8195b2fb-9016-3d2c-96f7-e9657f5af9fd | -7.18541 | -42.18234 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e26c7fa-2147-32ea-a5a3-e68178f553a5 | -8.83413 | -49.6665 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb4fdf7c-6c88-3af1-8b15-6721bc165152 | -10.62592 | -45.23149 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d120c50d-c37f-38b0-a6bc-574281f8382a | -5.36712 | -45.87461 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ec355a2-6961-38f2-b329-a2b1926ba63d | -7.65934 | -44.64441 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9600fde0-ab89-39a7-b188-a25cde1d533f | -9.91708 | -47.66426 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6917cf68-a141-3dff-b298-7aa1b3f8f30e | -5.93309 | -47.31903 | 2025-10-18 04:29:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e03ff317-f1d9-32ba-a3d3-bff57fee833e | -5.29418 | -47.93212 | 2025-10-18 04:29:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33f82b8f-419f-318c-86f5-19a4529daba6 | -10.52307 | -43.88536 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 856f7236-f677-372a-a76b-2303adb8997d | -10.16845 | -46.59248 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00a9c2dd-56fa-3236-9337-b0437441dd38 | -5.53233 | -51.38929 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3c4ee9f-1eef-393b-ae56-b5163d12ab16 | -8.10811 | -49.75942 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ede415fd-4bbb-33f9-add4-b5aa3736eba7 | -4.28958 | -48.64113 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2836157-7ba2-3d9b-8775-9b8c9908c4db | -6.326 | -44.30727 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f278695-73c0-3f0f-a7c1-885642d1cdbb | -10.70264 | -44.55019 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b38ec319-2101-3fd7-9ee6-947ab8b0b351 | -7.53546 | -50.41529 | 2025-10-18 04:29:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19df3388-de1b-3be7-a3af-89c46511f345 | -10.24776 | -44.03901 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e30eb33-ff8a-3e50-bf2a-98925609b65b | -7.4409 | -44.74926 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaab512d-d0e9-3d15-a94e-089e513047d3 | -5.09527 | -45.42941 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 64306a75-f1cb-34e9-b562-1c6ed1fc7cca | -6.32543 | -44.311 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34751ce7-2f54-3d19-8d63-8fd37579c174 | -5.89825 | -42.79609 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8006b9f4-816f-3b7a-83b8-c9bf68686410 | -10.4982 | -43.44876 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1305227-8ee8-30ea-aac5-90f1470913c2 | -8.82498 | -49.67743 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7162bb16-6fb3-3ed0-bef5-afc67e51a39e | -9.24708 | -43.76474 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7f50c9af-1c7e-3828-9af6-6ec108c354dd | -8.75283 | -48.59717 | 2025-10-18 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b07d97ba-c28f-3b1c-b918-552dd34f8a9f | -7.17757 | -42.17428 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2066fb57-b19e-3f3d-8b15-27117422d5d7 | -5.95059 | -44.18976 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fad1194c-c699-3077-8373-785df8d9889c | -7.48139 | -47.0281 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1550afd2-30ab-3513-9925-c023fa2749f0 | -4.73326 | -46.15773 | 2025-10-18 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49ca17d4-3435-3784-8a8d-f7111c0ad1a2 | -10.11563 | -44.55222 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82763f3e-da12-3706-9b93-859bb044eb43 | -9.97063 | -48.24076 | 2025-10-18 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b36f7c9-cb7b-3495-a21f-7ca73b577e7e | -6.60211 | -44.44454 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86194e95-dd34-3d79-bb3e-7027739fef80 | -8.37552 | -48.70485 | 2025-10-18 04:29:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5207e74-e417-321a-be4c-d4e67e45fd2d | -6.61632 | -43.60874 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c1237bb1-5b61-30bf-a5ca-ed112f227d03 | -4.53207 | -50.42893 | 2025-10-18 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aabca37-0fa1-39e4-9487-427fac1b66ef | -7.07444 | -46.75639 | 2025-10-18 04:29:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97492d8b-9655-3fce-8716-33ac80f53790 | -4.98778 | -49.76792 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79531c59-33b5-3f31-b734-8a415a355cf7 | -4.24727 | -48.56453 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d9fd196-c7d0-33e2-9d41-1c89dafe73e2 | -7.36679 | -44.06849 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42482f85-9c81-3d44-8619-dcdf964c3865 | -9.21218 | -46.886 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b8a5f76-54a2-3ce5-8281-1514f973d853 | -8.27592 | -48.00425 | 2025-10-18 04:29:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c8fb44b-2b34-34a2-98eb-c9f60f6dd7d2 | -7.58204 | -44.9852 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8726083e-460b-3e7b-9c29-802243d28c94 | -4.42507 | -47.75405 | 2025-10-18 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87a4987a-5716-38b8-81ef-ad2af539dfb7 | -6.97878 | -44.87133 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5646da4-be90-3b17-a152-a7a9dd216739 | -9.09598 | -47.78859 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0f9de7c-59a4-3752-981e-addae5d804c2 | -9.12204 | -46.62123 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f666484-5966-3573-852a-6e61281ddca1 | -7.42528 | -46.89422 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15dd2ff7-f121-30fe-9406-8b92e2c329a4 | -7.07397 | -44.73151 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecc9dea3-ee3e-377a-98aa-3b6c7efcbdfd | -9.52646 | -47.86918 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43027280-4a6f-3cff-84bc-c8a94a1ed583 | -6.24183 | -44.09478 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b7661b6-207d-39a8-9d79-08640bd3d9ba | -5.34633 | -45.74699 | 2025-10-18 04:29:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 808cf3dc-3d16-3b85-a7b6-0b07169c9682 | -8.43872 | -48.6992 | 2025-10-18 04:29:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31528082-5ed1-3062-8842-cc1f42b35ee6 | -6.65926 | -47.28222 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20bacf88-7208-3921-abf2-5f9aa7c2b470 | -10.8862 | -44.39956 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52c6b7d2-1f3a-31eb-a2d0-034d0f0630fe | -6.66299 | -46.53414 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42bc0c5f-df1a-35b5-9629-93a6fb82b11a | -9.55454 | -47.77927 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11f0697f-b651-3c13-96ae-4ed42e709755 | -8.56706 | -45.42918 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 352a956e-2434-31b0-ad31-207ca237b011 | -10.49874 | -47.54183 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9b29e50-a120-3bc0-adf1-7d8041e9b0f1 | -10.69492 | -44.55317 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cb06c7a-51f3-3987-8260-2b2c8e6472e6 | -7.76117 | -42.48925 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ef096b70-6fe8-3496-89f7-667f0cba93df | -7.01962 | -41.82073 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a6aa4bb7-7915-360f-a2b6-75b63b456454 | -10.24509 | -44.03154 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a51993cd-197f-38c9-9113-c2559d37d078 | -6.50897 | -43.72016 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db0d9a39-d122-3a44-99a1-2500c3a4c657 | -8.09229 | -44.10055 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a052cd23-9f1a-3862-8946-caf9916a7411 | -6.97537 | -44.87082 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8e649d-03bf-3c51-9777-9b49f8c3dbb3 | -7.60894 | -45.85056 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70ff95d3-3676-3c21-a8de-e92ad9295da2 | -5.15477 | -46.2735 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf319a4d-9dc9-3731-8c67-b9b3b0e1569a | -5.632 | -50.03101 | 2025-10-18 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99c4da2c-38c7-3203-a26f-5d912e52000e | -7.11617 | -44.73041 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8615551-d174-3e80-a23e-698bd2920880 | -5.73456 | -47.47435 | 2025-10-18 04:29:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba801b00-89b4-3ad7-8fa2-4a749ba93991 | -10.09794 | -44.598 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6aefade7-bca0-373c-9e46-a2c79ca754c4 | -6.86881 | -44.70464 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6194675c-815e-308a-934d-b1170d8176da | -8.58489 | -47.02594 | 2025-10-18 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdfec66e-2a55-3b46-8037-fe673b1addbc | -10.22792 | -44.07181 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9351c4b-1072-31e9-9ee3-df42f9c38f2a | -10.24477 | -44.03404 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 915a3693-4b36-3e42-9aa1-3121281b6b18 | -8.8348 | -49.66246 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a415ea3-b06a-3d09-8785-eb52fca07685 | -6.41614 | -43.57663 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de742f12-3c1e-3c2f-9643-bac271386b51 | -10.49439 | -43.28892 | 2025-10-18 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b36dfdff-2ff4-3f38-80f3-90c088c6fccf | -3.80503 | -51.64866 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README53.md)
