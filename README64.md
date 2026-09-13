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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9f28cb1-9975-38ab-a0f1-13c7b2461bbf | -8.5818 | -44.4167 | 2026-09-13 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 5091a348-c323-3d4a-bd4f-c811eeca2fd4 | -9.5129 | -45.4568 | 2026-09-13 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 45b051d4-3cbb-34f3-b3e8-45d85caee99d | -11.3723 | -46.8299 | 2026-09-13 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| c6174c0b-930c-357d-9be1-74c6297798b2 | -9.3948 | -50.1334 | 2026-09-13 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 211d8171-8961-3671-825c-07356b78b406 | -11.372 | -46.8524 | 2026-09-13 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 281f693d-8af1-30a0-a8cc-73d37fc74011 | -6.2832 | -59.9202 | 2026-09-13 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| b8d5a525-6337-30dd-98a4-e27328045620 | -11.3021 | -44.2074 | 2026-09-13 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| a27b5859-86fd-3a0a-b169-2940f3c0af6d | -8.6005 | -44.4378 | 2026-09-13 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 473.0 |
| 9fa64234-3628-3b6f-9ead-f3deeb1135e8 | -9.95 | -46.03 | 2026-09-13 14:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 008da321-c0ba-38b0-8e45-3c0feb85316e | -8.6203 | -47.323 | 2026-09-13 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 877acacb-5364-340d-94fb-98908480f74a | -13.3247 | -51.3211 | 2026-09-13 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e669c303-f6c6-3774-9797-e65d71e30cb6 | -8.2203 | -55.2427 | 2026-09-13 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a7c9516b-f573-3215-ae24-7dbf2adb617f | -15.3793 | -52.9864 | 2026-09-13 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 53805c7c-fcb6-347e-b813-fd58b163a7a3 | -6.3015 | -59.9387 | 2026-09-13 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ad6a6e0e-421f-3c98-9ce5-4ae50885c008 | -8.5417 | -54.6985 | 2026-09-13 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 2b8e3976-1a45-3a36-b9dc-0c004998e70d | -7.7634 | -46.6944 | 2026-09-13 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| d01c1092-765c-3c21-a5b2-8715b02a62ec | -8.2954 | -51.2212 | 2026-09-13 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| bad3c5ed-7e0f-3eb9-9967-121016d7a054 | -11.372 | -46.8524 | 2026-09-13 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 66e34b6f-579b-33e5-a930-013d659285f2 | -10.7271 | -50.6405 | 2026-09-13 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 813b5724-7db6-3e71-85c0-bba26e2f05b4 | -10.6431 | -45.9999 | 2026-09-13 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 227.7 |
| 4f2af052-ec34-3b85-a8c0-292161a0db19 | -2.6785 | -57.5115 | 2026-09-13 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a9f6dbd4-f5a6-31d4-a2ff-c9ec2087e69e | -10.5664 | -51.356 | 2026-09-13 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5e5a3cd0-66a0-3afc-904e-a944d5d6abb8 | -10.6829 | -54.1475 | 2026-09-13 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 432.2 |
| aa4c90e9-8493-31cc-84bc-1ba55c89c2ec | -10.6824 | -54.1884 | 2026-09-13 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 6f10488a-be39-30fd-b6e2-4cf8aeac6574 | -6.0255 | -59.9484 | 2026-09-13 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 50f9256f-8757-3f79-b6a4-9134b5067878 | -9.7043 | -48.0268 | 2026-09-13 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 981ca89b-4586-3e52-acc6-aeeaf8ba4ce9 | -10.624 | -46.0023 | 2026-09-13 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 8326e85b-92a8-3fcd-9487-41bc06a3ac57 | -8.6015 | -47.3248 | 2026-09-13 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5e8be6d0-b181-30a8-80c3-e7a12ededd06 | -10.2926 | -45.3161 | 2026-09-13 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 99af881c-3aa8-3488-8ae8-3e77841dffa5 | -9.5129 | -45.4568 | 2026-09-13 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 8fe63c25-1328-3cdc-848c-b23f75651c02 | -9.8992 | -47.5874 | 2026-09-13 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| fc2ab8be-b63d-337e-82cf-1953ec8407ea | -2.6602 | -57.5119 | 2026-09-13 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d59c4c83-73f0-3aa2-a63e-81b9f006adc6 | -6.8567 | -47.4328 | 2026-09-13 14:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f0e16cc6-931e-3940-bcc2-7d9c475896b5 | -9.3763 | -50.1139 | 2026-09-13 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3848c358-0838-30f4-a150-88851cd0a037 | -4.1223 | -54.0158 | 2026-09-13 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 356.2 |
| 5298e46d-a121-387d-8203-bd647149b280 | -2.6785 | -57.531 | 2026-09-13 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 8aba1f64-477a-3284-8210-e6b7633e5787 | -15.3054 | -53.9012 | 2026-09-13 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 5745e496-a05a-38e5-b520-ec67ce8e884e | -1.3007 | -49.1464 | 2026-09-13 14:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2a90cfae-985f-3cae-9dcb-352c2ad5cadc | -8.4292 | -46.0271 | 2026-09-13 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 802af3cc-e356-32b6-9148-56de6f0c02d1 | -3.4416 | -59.5213 | 2026-09-13 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| aa98d920-458a-3da0-b1b9-811aa45bb3b3 | -6.5159 | -42.2363 | 2026-09-13 14:20:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| e4650656-3790-3988-a291-fbd0b08226f4 | -9.3948 | -50.1334 | 2026-09-13 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 4c6e97cb-5546-3d25-b62e-820a8e4bd68e | -7.2072 | -46.0963 | 2026-09-13 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 5a8414ec-2f0e-3a4b-b914-0d6f1d6ce044 | -13.3758 | -51.7193 | 2026-09-13 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 5a02fdc3-f5d4-3b75-aaf5-1a4636081680 | -3.1697 | -58.6437 | 2026-09-13 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| fb495eba-63ae-3c78-9139-a042d05ab0a0 | -7.5394 | -44.9133 | 2026-09-13 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ba83840d-d645-3855-940e-9ffe9f2eda0a | -9.3768 | -50.0712 | 2026-09-13 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2ededfd5-5a78-3c51-8950-f9b921dcdfe5 | -9.3765 | -50.0925 | 2026-09-13 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| c9e577c9-7b59-370d-8a9c-85ebf5c88edb | -11.5796 | -46.9819 | 2026-09-13 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| f8d0fbce-1ff5-3212-beff-cca6e68c3173 | -6.7895 | -44.7982 | 2026-09-13 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 726d301e-63a3-346d-acb1-d6c2e2f59de7 | -10.6427 | -46.0226 | 2026-09-13 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 9a9e1bf6-1c51-3be6-8e8f-704ac63cf9fa | -3.7462 | -61.7552 | 2026-09-13 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| cc6f66fb-fbab-373b-bcbe-ca1130f0b7a9 | -8.9272 | -45.4321 | 2026-09-13 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a30fd81e-2cca-3468-96d7-21958ee18f04 | -6.8755 | -47.4313 | 2026-09-13 14:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 9bb33999-9449-35ce-9010-46ef7a6fdc88 | -2.6602 | -57.5313 | 2026-09-13 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d35281ab-e4a8-32f5-82a4-ab989eb3aa5b | -6.2832 | -59.9202 | 2026-09-13 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 418d9137-0c85-321b-a9b2-f6bf40ee0f0a | -9.376 | -50.1352 | 2026-09-13 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 67a5e823-2654-3159-bb21-26b1c6319bef | -11.0433 | -47.1633 | 2026-09-13 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 16193322-ebed-3c02-9625-a1709d03395b | -7.12 | -42.107 | 2026-09-13 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 250f828a-15a0-3c88-90ca-6a2d96d85aff | -10.7274 | -50.6192 | 2026-09-13 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| efc55a03-7ebe-3874-b216-43e3fb55bcdd | -5.1255 | -55.955 | 2026-09-13 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| c9673cd2-ecdc-39ff-9248-c87e14ae0dd0 | -8.8317 | -46.9698 | 2026-09-13 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 91c7c9ff-f521-39e1-b7b4-5d8d78fea778 | -5.1439 | -55.9543 | 2026-09-13 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 45cc6c8e-ba78-385f-9e70-d558aebce6c0 | -8.8132 | -46.9495 | 2026-09-13 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 67f23644-7b19-3af0-9fae-cce11db1555e | -13.3055 | -51.3235 | 2026-09-13 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 164.7 |
| e964c833-3426-3bae-8107-6971f68553d5 | -8.5415 | -54.7187 | 2026-09-13 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5f2fc487-535b-399c-adf9-e14221817836 | -10.7018 | -54.1458 | 2026-09-13 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| caffab85-1650-306f-a6db-b2e40d5d81d3 | -11.3825 | -43.9849 | 2026-09-13 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e540c7c7-e9f4-3730-a171-deab3046cef4 | -10.5667 | -51.3349 | 2026-09-13 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5a98837b-6a15-33d4-842a-fb8dde064373 | -3.6076 | -59.0769 | 2026-09-13 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 78d3e87d-eca2-34c3-bdb0-2740246e2033 | -11.5793 | -47.0043 | 2026-09-13 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 9a342be1-c746-3a01-8afc-ceda6bd3f8ad | -9.3951 | -50.1121 | 2026-09-13 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 547e00d9-b853-36a6-82e3-823c6f854420 | -8.2956 | -51.2003 | 2026-09-13 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 74f4e026-dda5-3600-9907-d705bbfe6750 | -13.3363 | -51.7879 | 2026-09-13 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d877ccc1-3b47-357c-bc24-021ef96f95b7 | -6.7895 | -44.7982 | 2026-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e622ee78-f9b9-3d51-83b5-e7304fa26f50 | -11.8193 | -46.3633 | 2026-09-13 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0509417e-1eb6-3759-9a18-5b36aa462322 | -8.8317 | -46.9698 | 2026-09-13 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 5b84957a-4fa3-3fb1-842d-db0eccd84f8e | -9.3951 | -50.1121 | 2026-09-13 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 8255d990-9d74-3115-9f8a-ad30873c78dc | -7.3465 | -45.3632 | 2026-09-13 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 84a9f63f-8f9e-38c3-b91a-bde26f27b6c0 | -2.6602 | -57.5119 | 2026-09-13 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 16c165b9-3cc6-3398-bfd2-3d838f936130 | -5.1255 | -55.955 | 2026-09-13 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 3515317e-1613-3e18-99b4-3797f5c0dc93 | -7.2072 | -46.0963 | 2026-09-13 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3d2923e8-b129-3a84-b233-9cd599a4d1fe | -3.6076 | -59.0769 | 2026-09-13 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| bd2ddf6a-1449-3b56-a321-35499311dfc4 | -8.2954 | -51.2212 | 2026-09-13 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1fdecbdd-de85-3d92-b5a0-89cd132dc287 | -9.8992 | -47.5874 | 2026-09-13 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 44ba4242-f2bf-33b8-bae8-55439dd2e4dc | -10.5854 | -51.3541 | 2026-09-13 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d90bc8eb-a9b0-340a-8cfa-95eed4ca8123 | -8.9272 | -45.4321 | 2026-09-13 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 61d1f061-d122-34c0-b853-116ec4212677 | -6.2832 | -59.9202 | 2026-09-13 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 43959fdf-f178-347c-931a-e002b6ee94ac | -10.2929 | -45.2932 | 2026-09-13 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5f9c5824-ba4e-35e8-b5ab-3a1ea39f4fdd | -5.1254 | -55.9748 | 2026-09-13 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2e1e6a55-435b-30cd-9485-e217bc4a1446 | -10.5664 | -51.356 | 2026-09-13 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| b9fde889-92e4-3e98-bf51-514cb9f35724 | -9.376 | -50.1352 | 2026-09-13 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 97276471-27ae-3215-ba51-8d6fb47257ee | -3.5893 | -59.0773 | 2026-09-13 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| a81572d1-332c-3b63-ba76-193f9235c330 | -2.9395 | -50.3784 | 2026-09-13 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 53991b01-a748-3281-b203-107c962e9657 | -6.8755 | -47.4313 | 2026-09-13 14:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| f761fd1c-086d-3923-9f54-acb76e14d304 | -9.3763 | -50.1139 | 2026-09-13 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 7b781975-255f-3b81-9968-a564d6717f6e | -8.8132 | -46.9495 | 2026-09-13 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 76cdb593-b1df-33ec-97e0-9005a551203d | -11.3532 | -46.8324 | 2026-09-13 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| fd82d66a-b12d-3508-a863-bd4f755b1957 | -8.2203 | -55.2427 | 2026-09-13 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2021af49-35e1-36af-9a1f-8b22aacacf39 | -3.4416 | -59.5213 | 2026-09-13 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |


[Clique aqui para ver as próximas entradas](README65.md)
