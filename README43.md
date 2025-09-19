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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 689c3ba9-259a-31c9-87d4-fce04a60c218 | -9.1937 | -45.2886 | 2025-09-19 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 411.6 |
| 10a56b7b-662f-36c9-9dcc-cbef5c3cecc0 | -7.7148 | -44.392 | 2025-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 162.1 |
| ebaf0314-a82c-3905-bd7e-d7fb17a74d9b | -3.1562 | -43.2587 | 2025-09-19 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| fed9e7e2-4876-392f-9ced-04b715e29a61 | -9.7334 | -45.9302 | 2025-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 6617694c-b1fd-3bc4-865e-1d71ba6e660d | -9.1747 | -45.2907 | 2025-09-19 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 3c0147c3-a71d-3a93-978f-17624f034404 | -4.6762 | -37.6106 | 2025-09-19 14:10:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 481.1 |
| ab71e047-0287-388f-aafb-c04efd62daea | -8.9892 | -45.0376 | 2025-09-19 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 38d6948b-c910-3c59-a6e4-24456a452328 | -6.1438 | -47.8342 | 2025-09-19 14:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| cbc490ca-90ce-33ee-85e2-4bcd0724dad4 | -7.1886 | -44.3503 | 2025-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f9a5d1ee-6d02-3cbd-95b3-6976f06def66 | -6.6506 | -45.5585 | 2025-09-19 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 66b91cd1-47dc-35ee-a651-d4217cc3ee1c | -6.1878 | -41.2097 | 2025-09-19 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 202.2 |
| ba842191-4074-37ba-b484-3fa1ceb5c648 | -8.9976 | -45.8098 | 2025-09-19 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 28bd4af5-d043-3fa6-9a34-497382e48b13 | -9.7213 | -45.455 | 2025-09-19 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 66ee35d1-ec5e-37c0-bc63-6e4c73d3ed2b | -8.9536 | -46.2874 | 2025-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| ff0813d3-f8f6-34b7-b936-fa4b12edf425 | -8.3709 | -44.6697 | 2025-09-19 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0bf583d1-b6d6-3907-9610-fa728f174a60 | -7.6386 | -44.4686 | 2025-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2fd12112-2ff0-31e7-bc05-6a219f6218ad | -8.9179 | -46.134 | 2025-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 77135204-45b6-39eb-8295-2982b17605d4 | -8.899 | -46.136 | 2025-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 112ee2c4-83d3-3265-b5f9-44ede5e6aca9 | -6.9212 | -44.764 | 2025-09-19 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| e48e6c48-27d7-34dc-9973-73c4f3688333 | -7.5818 | -44.4971 | 2025-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 7287e62d-970a-3839-aeac-0e03519b0952 | -8.0281 | -44.957 | 2025-09-19 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 75968cf0-a293-386f-8e34-4358d6c261d2 | -7.7148 | -44.392 | 2025-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 2a05c960-913b-384a-9338-7ffd08c82eaa | -7.8509 | -45.6105 | 2025-09-19 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1a52b951-5398-3d24-98de-8b40b05d7cd5 | -6.9022 | -44.7885 | 2025-09-19 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a6950653-602b-38f3-9a16-4650b6673652 | -9.1615 | -44.8806 | 2025-09-19 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 8198fc3d-a3bc-3522-b0c3-609d9aef73bf | -5.8073 | -43.6352 | 2025-09-19 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 077d0c84-5c5a-347c-81c3-94f4fa8cbde5 | -7.2206 | -46.6084 | 2025-09-19 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 803a5818-bcd6-3ebf-8c16-43ec55dd60ce | -4.676 | -37.6366 | 2025-09-19 14:10:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 489.4 |
| 5a77729e-1515-3cfa-b1ac-d2597423b7ac | -9.1458 | -44.6526 | 2025-09-19 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 2abf5d2e-9eea-371c-8afe-9a20c8a98ee0 | -9.028 | -44.9646 | 2025-09-19 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 149d8d58-9903-3f76-9c1d-2b2cbfb95385 | -7.6949 | -44.486 | 2025-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 21289e37-a277-3efb-9fce-9a66b11791b2 | -19.5672 | -57.7584 | 2025-09-19 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 865f10c0-d0f5-38a3-9cad-ad55013908c3 | -8.9533 | -46.3099 | 2025-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 3744a129-3d4a-36c8-8d8d-6df97dceb5c4 | -7.3366 | -44.5663 | 2025-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| afeb8e4c-9924-333f-839c-18f05608252f | -8.9985 | -45.7418 | 2025-09-19 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c17fed52-434e-3623-adfb-fc75827eec69 | -9.1744 | -45.3135 | 2025-09-19 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| cbfb455e-bb8f-3e3c-950c-6859f04d39c0 | -7.4531 | -42.644 | 2025-09-19 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| ff8fcfb3-5186-378e-893d-60150f48cb57 | -9.1425 | -44.8828 | 2025-09-19 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1684a641-a7b3-300f-9461-f54a10f9e44f | -6.9024 | -44.7656 | 2025-09-19 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ec0c4ab3-432b-3607-96e7-14fc4da07d9f | -7.3111 | -45.1622 | 2025-09-19 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 14758fc0-51fe-39b3-9ec7-8f963a755fe7 | -9.1937 | -45.2886 | 2025-09-19 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 235e98bb-6103-3559-9fb4-5d833ee9761b | -8.8801 | -46.138 | 2025-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| c880e1b8-1b28-3cb7-af34-250cfb175c82 | -8.6076 | -45.3302 | 2025-09-19 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9d974a5b-58f7-3a7a-bd79-fa1db58dca75 | -9.175 | -45.2679 | 2025-09-19 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4d79afdf-4a76-33fe-8427-6bd457072a5a | -8.6265 | -45.3282 | 2025-09-19 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 2b6efbc3-44a3-3449-b783-a8f504e053b9 | -7.1878 | -44.4193 | 2025-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 370b534f-8e11-3d8d-a04d-bb29489c89c3 | -9.1647 | -44.6504 | 2025-09-19 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 54c64540-89e1-3136-9762-269fd70b19ba | -8.9911 | -46.3059 | 2025-09-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 202.7 |
| 1ea9514f-1dbb-32bb-adbb-102fc94a8511 | -6.1252 | -47.8355 | 2025-09-19 14:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 79a87d30-6696-35f8-91a6-499fb48da154 | -4.6948 | -37.6351 | 2025-09-19 14:20:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 57000037-5015-38c7-97ab-c3818256b1b2 | -8.9519 | -44.996 | 2025-09-19 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| f20692f0-de54-3eb4-8fa3-e9a95c2dfcd5 | -6.9212 | -44.764 | 2025-09-19 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8215e15f-954c-3b62-ba41-2cd5a85fafe6 | -8.6265 | -45.3282 | 2025-09-19 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 33ca6e56-1ec1-3c66-a659-dd3332954fad | -8.0188 | -45.7298 | 2025-09-19 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 76e8d091-4364-3fb3-924e-bce8dfd8de86 | -6.6538 | -45.2417 | 2025-09-19 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| fdeeb85a-fe6c-3312-82cd-248c26f9fcd3 | -7.6574 | -44.4667 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| bdf9880c-d42e-3403-bdfb-c1637143c4f0 | -8.6699 | -46.3618 | 2025-09-19 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6dc49cfc-99b3-3d88-872f-fae206520371 | -7.3479 | -38.9606 | 2025-09-19 14:20:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 120.5 |
| d837f6d8-e7f8-383a-b27c-f466a3386158 | -7.3551 | -44.5875 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| dc1257c3-96cc-3c26-b47d-8174bd6808d5 | -7.4531 | -42.644 | 2025-09-19 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 4cefb644-a33a-388d-8912-8ca25f3429b4 | -8.3334 | -44.6507 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c9122284-dbb6-3b0d-835f-2a76bf2cb85d | -7.3111 | -45.1622 | 2025-09-19 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6fa46a63-a948-3073-bb34-d779223b30b3 | -8.9722 | -46.3079 | 2025-09-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 7485572d-a721-3d54-9afa-3ef973cecb12 | -7.7148 | -44.392 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| deebd38c-8263-314f-b24d-27c73e5b1b9c | -8.6076 | -45.3302 | 2025-09-19 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 1d1b206c-8de4-3a72-9132-4fa864324627 | -8.0092 | -44.9589 | 2025-09-19 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b86bbfc7-ec33-3b08-a300-ffdbebb0b78e | -9.1458 | -44.6526 | 2025-09-19 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 6aba7bca-3a7d-36b5-9185-f2a8fa25bea4 | -19.5672 | -57.7584 | 2025-09-19 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| c14eab1f-9f39-3302-a2c2-21b7d13c2503 | -9.1937 | -45.2886 | 2025-09-19 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 037146ab-2b27-3907-9d86-a0f30e7d4c72 | -7.3669 | -38.9584 | 2025-09-19 14:20:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 187.3 |
| 7236e46e-2845-3015-a5a0-766260467e06 | -9.1744 | -45.3135 | 2025-09-19 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 6ef4d3cc-babe-3496-b95f-15df6e1259bb | -8.9985 | -45.7418 | 2025-09-19 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| cc14a5ce-1829-3660-a7b6-f9f391f793ae | -6.1876 | -41.234 | 2025-09-19 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| d665fb77-c410-3de5-bb13-a9636e5a013e | -9.1429 | -44.8598 | 2025-09-19 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 592128f2-108d-33b7-b2bd-be08ce8e7dd4 | -8.9892 | -45.0376 | 2025-09-19 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| ef4737fa-c321-35e4-99d4-7674179104ca | -7.7778 | -43.8538 | 2025-09-19 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f8df58ba-404b-328a-958b-8e3a7a5d034e | -4.6951 | -37.6092 | 2025-09-19 14:20:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 89.3 |
| c43c7f08-b627-32b4-8ab1-addf649673bc | -7.3366 | -44.5663 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 56ae9c96-6cbd-3792-a558-2d2e9478bf43 | -9.1747 | -45.2907 | 2025-09-19 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.7 |
| c3b92dba-5fa1-33f6-9432-dbc2d314fc86 | -6.9024 | -44.7656 | 2025-09-19 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7715cc97-b116-32d7-8b8c-b73b8ae1e6b7 | -6.6764 | -44.8534 | 2025-09-19 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| af112418-fbe8-3396-88af-aca42f999f13 | -9.1461 | -44.6295 | 2025-09-19 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 2f45c85d-4023-3094-a0bf-de9c2f9ce995 | -8.0281 | -44.957 | 2025-09-19 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 6472a863-86c2-3232-8251-1632455749f8 | -7.6386 | -44.4686 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c02a6564-bb5a-3395-93dc-cdb5a9079821 | -6.1881 | -41.1855 | 2025-09-19 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 134.0 |
| 3154a58a-6fc0-3eb0-aa7e-179202eb10c6 | -9.028 | -44.9646 | 2025-09-19 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 4af85c13-ecb2-3bdc-88f9-a493be4ee5f6 | -7.8509 | -45.6105 | 2025-09-19 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2787af6a-353b-3abc-a301-ce18846059ce | -7.5601 | -44.7514 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3c9328ff-aa54-3835-a623-63d35884b940 | -6.9022 | -44.7885 | 2025-09-19 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 65be7ae3-bd0b-3375-905d-4ee11c6a8f49 | -9.7334 | -45.9302 | 2025-09-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 0cfd0a71-ea6e-3930-b075-bb5649d5d053 | -8.9164 | -46.2465 | 2025-09-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| da303339-c0f1-3cad-bba0-3117ecce5413 | -6.8154 | -47.8517 | 2025-09-19 14:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b15ba563-1030-3745-85ca-d6fc4d0c2cd5 | -4.6762 | -37.6106 | 2025-09-19 14:20:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 227.1 |
| fc7ef95c-177b-3d99-849d-4c0267a42656 | -9.01 | -46.3039 | 2025-09-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| a2d5c253-3cd5-3f61-b95a-d752ffc80b8a | -7.6949 | -44.486 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 62cebcfc-349e-36e9-baa1-17c7bd9f74c9 | -6.6762 | -44.8762 | 2025-09-19 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| f1ff1ee0-aff5-3c2a-a24e-92c0137391f3 | -7.5818 | -44.4971 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b2d68b7c-83ca-3ca1-99fe-ceb29e6b355e | -7.1886 | -44.3503 | 2025-09-19 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 28a445de-5fc5-359f-b3de-591ba5f8d004 | -6.6204 | -44.8353 | 2025-09-19 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| cd2c9358-8987-36b8-b62e-c79b460757e7 | -8.3709 | -44.6697 | 2025-09-19 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |


[Clique aqui para ver as próximas entradas](README44.md)
