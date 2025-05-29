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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abab6ed2-ed30-378e-afd0-1378f60d787b | -5.76546 | -43.48135 | 2025-05-29 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09f6751b-a70c-3e3b-bd98-e6f027ce45d4 | -7.58273 | -45.86913 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a85a28bc-a0c0-31c5-b110-5dc012fd2089 | -5.21186 | -43.31782 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 14fe6c2c-76ed-3e36-a776-e5ca2cfef4f5 | -6.23802 | -43.37759 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 950a98ec-9b56-3f10-a514-d0787cc2c321 | -5.07919 | -37.64569 | 2025-05-29 03:49:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df91c9a8-6c00-3af1-96d8-8f9a3f46468a | -8.06394 | -47.12696 | 2025-05-29 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e1fa03c-0fc2-3220-bdc0-f8b55654ce24 | -4.95958 | -37.93914 | 2025-05-29 03:49:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b1274c6-8c50-3511-9114-897243d24fa4 | -6.22466 | -43.3479 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 96cc8077-8f1a-3a06-88c4-332aad65bebc | -6.82752 | -44.64722 | 2025-05-29 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a58cd963-adde-3730-91d9-95d0a88d5bff | -6.83364 | -44.65418 | 2025-05-29 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2543aa38-399b-316a-82ed-ded0243f4394 | -8.09306 | -46.28854 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5599bd96-62b4-3f2c-b271-845143cb5e68 | -7.57458 | -45.85453 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9a60032-b035-369d-8b2a-5bb6e96fce39 | -5.96122 | -43.75989 | 2025-05-29 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0be1943d-af17-3277-92e2-468048918438 | -7.62211 | -45.74465 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bec4701-c023-339f-86e2-38a8e4dc9f71 | -7.18404 | -43.10711 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e2b2b992-a922-380b-b67f-63423db667a5 | -8.79455 | -47.94518 | 2025-05-29 03:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d14ae234-58a8-3f72-aaa1-8e64bb7ecead | -7.23652 | -43.09366 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 895c5c28-671f-3c86-bf9f-1f9c93aea444 | -9.20711 | -49.47416 | 2025-05-29 03:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fdc1f625-70e0-35cb-831f-2d3a6665a503 | -7.58442 | -45.85952 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82f1e227-0d31-35a3-83f2-828179a14fad | -7.54125 | -43.3581 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb647dec-5837-3db6-abc9-0c7355d86729 | -9.20073 | -49.47302 | 2025-05-29 03:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 86200621-f1b3-3661-a5b8-e730719df6a8 | -8.00577 | -46.14909 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eeb1b8f7-90e5-340d-ae5a-ec260c5404ac | -6.20479 | -43.34723 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59b17a69-670e-3e36-9242-6b38bfdf0ba6 | -6.83064 | -44.65817 | 2025-05-29 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| aa0d5e52-a652-3ba7-b82d-2a274d13303d | -8.66651 | -48.28655 | 2025-05-29 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3044c3e4-29e7-3e1c-aa89-b2b30ae21b63 | -6.34706 | -43.37214 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26495e99-d388-3cbb-ab6b-5e9f14ad5975 | -5.64789 | -43.59131 | 2025-05-29 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5abc4dea-b8f7-3d2c-a800-5e3eee98c249 | -6.29884 | -43.65193 | 2025-05-29 03:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 947d521f-6aa4-3681-9442-8a0a6a4d841b | -5.10915 | -44.45115 | 2025-05-29 03:49:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0d40110-fd8d-3df9-af54-11be14b9ee25 | -7.61965 | -45.75009 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83877811-d60f-3cc1-bfb0-df789dabce6e | -7.95087 | -44.85512 | 2025-05-29 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc58b7fb-8987-3b0c-8923-3eaa79d4d4c6 | -6.83154 | -44.65294 | 2025-05-29 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 176ca195-ceea-30ab-a047-926b3d3800ac | -7.43564 | -45.42165 | 2025-05-29 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d533ea4b-7aa4-3be1-9395-353ab30f246a | -8.09894 | -46.28633 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b209aa04-d2db-3b31-a0c4-e42cb57df01b | -7.54272 | -43.34965 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caa6715f-613c-3f23-81c8-b72a8ba3c010 | -7.56099 | -43.32233 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0396f9d1-1e09-39f3-8b55-1ba922697798 | -5.21719 | -43.3139 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8430ea7f-7f52-38c4-94bf-f66f618e3dd7 | -7.62427 | -45.75407 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68160276-c515-31e1-80af-0be4e12e9881 | -5.21263 | -43.31323 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 111f88a0-fc12-310d-ad28-d0e0dcbbc0ac | -7.43512 | -45.42458 | 2025-05-29 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9670257c-eb37-348a-a334-6b935ea0037a | -3.28807 | -43.46947 | 2025-05-29 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cff982ec-a3f4-35f3-a53d-34674c00e3de | -7.47289 | -47.06117 | 2025-05-29 03:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41b7d5a2-ab19-37cd-86c8-e6394b8bb36c | -9.11141 | -46.93471 | 2025-05-29 03:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8aa82e66-1c52-327a-9cc2-c86452f4f6ee | -7.58386 | -45.86272 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f75072fb-3f90-3846-adfe-ed4924363672 | -7.23148 | -43.09697 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f3934e1d-3417-3f6b-9510-10b629559470 | -8.78875 | -47.94394 | 2025-05-29 03:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f4698e4-1d4c-377c-abb1-6e068690c697 | -6.20929 | -43.34794 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8356031-6298-39a7-98c9-c4e6f72906f5 | -7.18838 | -43.1079 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0a063dd7-ef74-3e4f-b405-e54f659f8a37 | -2.65526 | -48.80939 | 2025-05-29 03:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6aeea39d-5e72-36db-8f30-ff14f5b590c0 | -7.57288 | -45.86414 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0525f821-0855-3032-b568-85d15b3b3589 | -7.94605 | -44.85427 | 2025-05-29 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 309b4d46-76a5-3fa6-b3ae-41981cf1ad9e | -8.00822 | -46.16548 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6233aee5-ee3c-3146-a2ed-6bbf9994cca8 | -5.76857 | -43.48867 | 2025-05-29 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa1bf03-92e0-30ae-82da-5b363dab9fd5 | -6.8324 | -44.6479 | 2025-05-29 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11893ee4-af83-3b0a-80d8-01577e967772 | -6.82574 | -44.65755 | 2025-05-29 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8bd4125f-0667-3a5f-b53c-1658589bdbc8 | -8.1932 | -49.81671 | 2025-05-29 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 671a4822-424b-39d1-9ccd-58cb602a7aa6 | -7.07092 | -44.92953 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8abaae95-5ccb-3e80-9335-105013e10b4f | -6.90728 | -47.85801 | 2025-05-29 03:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b50b8803-25e1-3d9b-a2ad-a2948270cef7 | -4.53927 | -38.03333 | 2025-05-29 03:49:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 538fa8ce-e7e2-3760-a85a-16f654571ffc | -5.76479 | -43.48335 | 2025-05-29 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1775ea35-26b5-3380-871b-f03928f4d9ac | -6.53568 | -44.46422 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a45c850-2224-34af-b282-be4682c87eef | -6.53655 | -44.45913 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76228cb4-c91a-3af3-842a-78e102efd0c2 | -6.2425 | -43.37844 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04421026-d61c-395e-85fe-0e52e0b1ae54 | -7.58422 | -45.95195 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96f8a746-d8fd-3a92-8626-5b2928e285d4 | -8.74371 | -49.76522 | 2025-05-29 03:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b183076-4f40-31d3-a4b6-868100a426b7 | -7.58385 | -45.95466 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 799dc268-aa7b-3a64-8ba6-355f5d490bf0 | -7.18908 | -43.10379 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d884bce1-b35a-3b02-a606-72d7c4c7f1f8 | -7.63061 | -45.93408 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d3be21a-206c-34b8-8084-e9ae272ab14f | -5.10426 | -44.4501 | 2025-05-29 03:49:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 08aa1e67-8943-3728-9cb4-f47fc35eb36f | -7.46728 | -47.06001 | 2025-05-29 03:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03a8f69e-2dde-3b34-8f12-4c773a21fb1e | -8.74917 | -49.77196 | 2025-05-29 03:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd740549-246b-3f40-ade0-e1a5ad42db99 | -8.00522 | -46.15212 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5df24f9-ff20-36f3-9cd5-bdc7459978df | -6.90808 | -47.85356 | 2025-05-29 03:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e97a9da-cf3c-313a-bcc6-52e429d56bde | -6.80516 | -45.3674 | 2025-05-29 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 428d4cb3-072c-3d1e-99ea-58aa6a3fdd70 | -8.01402 | -46.16351 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2976357f-9e62-3d40-8a2e-5f539c4b7231 | -9.20165 | -49.47316 | 2025-05-29 03:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5a3817ac-1e1f-309d-9496-6c7c1016d7b3 | -7.67774 | -46.09558 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2aa7468-0049-3f38-953a-5f65743f9b4e | -7.66979 | -46.10074 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d729f71-e132-3dad-9ff1-7e427af3f56b | -7.54125 | -43.33208 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4dc68ba0-20c4-3d50-a084-bc8e1656c6a6 | -6.80973 | -45.37133 | 2025-05-29 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01748279-6f15-37c9-9c31-06c3934deb99 | -8.65814 | -48.29843 | 2025-05-29 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b0d46c0-c335-3b1b-bcee-2e3b5f1c9c4a | -7.94512 | -44.85955 | 2025-05-29 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 143d134e-4e52-3423-b808-0b22c5ae8233 | -8.00879 | -46.16237 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a8efd01-2fcd-3546-b920-09c2a0f47cf1 | -8.40328 | -47.09441 | 2025-05-29 03:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13df733b-6f8c-3860-a27b-bea5268576cb | -7.57898 | -45.95108 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f132f9ac-5e7c-36e4-9fc6-6315b78aead6 | -7.24014 | -43.09852 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ac6ffa9b-6ccf-3d41-9a07-a4f9445b8673 | -5.21109 | -43.32243 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30846280-e69e-343b-8bed-9a844cadc55f | -7.57344 | -45.86097 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acea1eac-f943-3741-beaf-0c32ac3134d4 | -7.08077 | -44.93122 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 786eadca-79e7-3318-a7e2-9b1b7fe2265c | -9.20065 | -49.47828 | 2025-05-29 03:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 27e99a22-0dc3-36d7-8ed0-2be4cf805228 | -7.63526 | -45.93822 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cfa66c2-c796-31dd-8636-81f1ec00639a | -9.39759 | -48.42355 | 2025-05-29 03:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17a49e40-11cf-3659-8fbe-7d1af5cbcb57 | -7.63119 | -45.93089 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11836729-6235-3bbd-8643-f03f697b71af | -4.48923 | -47.79236 | 2025-05-29 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 121161ff-c87c-3cb3-9c6c-f38320150dcf | -7.62153 | -45.74783 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4c662a7-5b85-36b1-9981-8e806e0d2a4b | -7.18768 | -43.112 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a45c6774-785e-3817-a448-7ac04698e911 | -7.2358 | -43.09775 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 17405ec7-3499-369f-93c9-70204cf9b44a | -5.2134 | -43.30861 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 61d0dcb9-28f9-3c83-b74f-9b2cc5513c54 | -9.10596 | -46.93376 | 2025-05-29 03:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c40afd4-1ac9-3935-a259-c47b9819c0c1 | -5.31959 | -38.00262 | 2025-05-29 03:49:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README6.md)
