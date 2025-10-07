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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81dbe8e5-7687-3450-9cc3-4c47f3f9f02b | -10.3721 | -50.3363 | 2025-10-07 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 5812ee0a-0844-3baa-b91d-691f0d35e5ba | -11.4678 | -43.5011 | 2025-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c7a67fa4-ff7d-3075-8d3e-abf22aa12f40 | -14.3144 | -45.8579 | 2025-10-07 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| b7b04d03-55d3-3a7b-ac9c-186e7c9ac020 | -11.7409 | -45.371 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9ac429db-06ba-3e41-9ee7-65a10a297f48 | -7.4666 | -43.0909 | 2025-10-07 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| a7f9e643-b324-358c-aa39-805f67280697 | -14.7585 | -46.0104 | 2025-10-07 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5a904e05-047c-3d05-8917-c66e70d36183 | -9.2166 | -47.8142 | 2025-10-07 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| fc7e0e0c-ad63-3acb-8350-28cba385367f | -17.9778 | -45.0057 | 2025-10-07 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 139.2 |
| ac2daeae-afe0-38a9-a351-5fcb9f6286b6 | -9.1978 | -47.8161 | 2025-10-07 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 0f0939ea-e689-3690-9f36-563975bf5007 | -10.3665 | -47.9978 | 2025-10-07 13:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| aacc66d4-3bc6-31dc-b954-953b15dbcb65 | -10.0868 | -50.5141 | 2025-10-07 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| a6d802bc-5054-341d-95af-b3e02067269b | -8.1879 | -44.2283 | 2025-10-07 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 198.2 |
| bc358c5c-6a88-3237-904d-18d322ef84c7 | -12.7637 | -50.4921 | 2025-10-07 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 3f0367d7-b91b-388d-b532-81bd5f1d440d | -14.7194 | -46.0173 | 2025-10-07 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 73eac40b-b862-34c9-965d-697eddc21210 | -11.9519 | -46.4352 | 2025-10-07 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 992563d4-cf95-3e40-ab3c-4cb13b540421 | -8.8429 | -46.0969 | 2025-10-07 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1bb88293-7f3a-3cf5-acb4-b1255e959d95 | -14.7389 | -46.0138 | 2025-10-07 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 626b35af-c94c-3aa8-84b3-1179b5ac81b9 | -15.6198 | -52.5715 | 2025-10-07 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 6b71a103-1c8b-3011-9fc0-6d24acdd2440 | -13.7927 | -45.7627 | 2025-10-07 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 25916677-38d9-31e4-a1ee-99e403b383fe | -8.501 | -46.3117 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a8435aee-8df2-3e31-8d1d-ab8eb1230745 | -15.1548 | -45.73 | 2025-10-07 13:40:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 04421d97-3246-3c0e-94db-ac7e31cd0cb9 | -8.5395 | -46.2406 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| b2b05a5e-5254-396f-9883-7816a9262c2c | -13.3291 | -47.7641 | 2025-10-07 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3a29df6a-c94a-3dca-a7ef-e4c6179a6ebc | -9.7463 | -47.7144 | 2025-10-07 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ce4b784c-329a-3fb7-a90c-66e2f593e928 | -8.2346 | -49.8734 | 2025-10-07 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 82f072ce-6cb7-3719-9c0c-dbb7171330a7 | -18.2856 | -45.4587 | 2025-10-07 13:40:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 4e89f23d-eec6-35ec-a5e7-4ed2f868dcfc | -19.0295 | -44.7327 | 2025-10-07 13:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 7302310f-d49c-343b-9f5b-bff2d5ca39fb | -10.4245 | -45.3907 | 2025-10-07 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 0c63c894-0ebf-3c5b-ab6d-bbbdaaa5988c | -8.4519 | -47.2509 | 2025-10-07 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9f9c225f-be58-3dde-8625-474aa74eda83 | -11.8413 | -45.103 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5872e07f-7710-30ab-a288-4e687d390bb1 | -8.1324 | -47.2589 | 2025-10-07 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| bd09a362-7d96-3c03-b062-38cfe342930d | -15.8091 | -43.7597 | 2025-10-07 13:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 8c33d9a7-d953-3e38-8b31-d36d3c512ec2 | -11.1644 | -54.8804 | 2025-10-07 13:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 23e8f669-364d-3ea9-9681-3a7661567864 | -8.4525 | -47.2067 | 2025-10-07 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 16da9e6b-f96f-3a85-a38a-e0b42ecbe310 | -7.6932 | -46.2548 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 0bb17620-6ea8-3346-af14-6ea986083edb | -11.9515 | -46.4579 | 2025-10-07 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 2020fdd1-5980-3835-905e-bb473ee060ff | -8.8986 | -47.6483 | 2025-10-07 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| a597dcad-310b-3363-a1f2-c20f54e7d545 | -10.1573 | -45.4701 | 2025-10-07 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 248918ef-1b91-3a2e-8e1a-8d14c5cfab8d | -15.6367 | -53.8165 | 2025-10-07 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a39c5870-d197-3356-bf3d-aae3d764159a | -18.5093 | -43.9162 | 2025-10-07 13:40:00 | GOES-19 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 2a6d2f1b-ea98-3e91-811c-bfc842994d7e | -8.5393 | -46.2631 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 2b2429fe-0f2e-3b30-bddc-71a81252e961 | -15.3742 | -47.2973 | 2025-10-07 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 87adf5ad-2aed-3fc7-ad1b-3f8c050f247b | -21.4055 | -45.0614 | 2025-10-07 13:40:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.8 |
| c02d6c70-ef88-3f1f-b4c4-eb8a06150ea8 | -8.2071 | -44.2032 | 2025-10-07 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 359.5 |
| 7306c788-0660-3d50-bc9f-f78f901f9d20 | -11.2433 | -50.2859 | 2025-10-07 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 165c9b6c-4a61-3493-978c-6d0de9586539 | -11.8221 | -45.1059 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| e27f3074-fabc-3bb0-a4bf-6d9328c4de1b | -9.4068 | -46.2831 | 2025-10-07 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 760b7e83-9856-3a5a-ad7b-ad67478b2b4e | -8.4824 | -46.2912 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 50bd616c-6d6f-3629-8b91-ca6f8868e406 | -8.0946 | -47.2844 | 2025-10-07 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5bb5dfd1-23d2-3351-86bc-17b0e88876ee | -12.2215 | -44.2543 | 2025-10-07 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 1767f0e7-7dc1-37f0-9515-dd5a2c09dff4 | -9.3891 | -47.5982 | 2025-10-07 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b58ade5c-9d40-315f-a6e9-d63a6b7c4fb5 | -8.5007 | -46.3342 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 0cc78ab4-4224-34a5-9a89-0a94ea9f71dd | -9.6804 | -45.6645 | 2025-10-07 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 814bc471-91ed-3c6e-8e91-2cb8cc977fcb | -11.6859 | -46.3366 | 2025-10-07 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| b7e16183-17f6-3cfe-ad95-31afeb279181 | -8.1136 | -47.2606 | 2025-10-07 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e3a95ed7-8d13-3731-a1d9-3bc751317e1e | -12.3162 | -45.3545 | 2025-10-07 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 3f902474-35f3-3a36-9526-c2eb1d4e726a | -7.693 | -46.2772 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 377d0ea3-67e0-3962-a260-ade07d698360 | -13.243 | -47.2165 | 2025-10-07 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 1047cd6a-0452-3fbd-a3a7-51ee8d43acd2 | -8.5584 | -46.2387 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| af619428-b6f3-3c16-ba9c-ef4e76ccff15 | -18.9846 | -47.8282 | 2025-10-07 13:40:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 121.4 |
| f02e7863-8771-3e22-b270-526159f8d1bb | -7.6648 | -45.4471 | 2025-10-07 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 80903a0b-0c62-3cd9-9c00-ade0096224d3 | -8.6519 | -46.2964 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 244d44ad-fb54-32cc-af36-83594a70bc51 | -11.7217 | -45.3738 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 2418aeb5-e5fa-303c-932f-a66ffd61dd45 | -17.9784 | -44.9817 | 2025-10-07 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 209.1 |
| b45b86cd-87e2-3909-80e7-c899527319bb | -12.4893 | -47.4613 | 2025-10-07 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| daa708c4-6770-3ff1-8c26-001259397c34 | -17.9979 | -45.0011 | 2025-10-07 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 310.3 |
| d2119acb-4bcf-34e2-8541-cdfcb05f4cd1 | -11.8635 | -44.938 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c13ae532-7311-33fb-85d6-60f19a0e8df4 | -8.8618 | -46.0949 | 2025-10-07 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 4960c35d-fd7a-3c74-ab0f-a71ab1055abd | -13.2421 | -47.2617 | 2025-10-07 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| fa27b28f-b0a0-35e1-b82d-e6cd6f450859 | -8.1618 | -43.323 | 2025-10-07 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 108fdbc9-8520-35b0-86e6-5a71ac072f19 | -7.4669 | -43.0674 | 2025-10-07 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 15007604-3f97-3731-8426-6a8f066db617 | -10.3854 | -47.9956 | 2025-10-07 13:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 3dba0063-d75a-37b3-af15-9ad000bafd76 | -15.3737 | -47.3201 | 2025-10-07 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 354c093a-8bb6-391a-ba2f-99b0113b1647 | -10.8919 | -47.1153 | 2025-10-07 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| c533117a-86ad-3e00-8246-bec493375f5a | -8.9759 | -47.4864 | 2025-10-07 13:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 9fcf9490-535b-3954-bc14-397e7c35ccd6 | -11.2436 | -50.2645 | 2025-10-07 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| f685b4cf-6381-3368-b58d-c03763c521e4 | -10.4091 | -50.3965 | 2025-10-07 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 120e0535-a3c7-31aa-89c7-73030069dc62 | -18.2862 | -45.4348 | 2025-10-07 13:40:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 110.0 |
| fa6afaef-f68e-3899-8ec0-d7f45e4b4a70 | -12.6159 | -44.7519 | 2025-10-07 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2add1d7c-0ed5-30ab-a9ec-980bc1e78ba3 | -8.539 | -46.2855 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| a8079d78-b74e-3773-ae78-f9d013069a35 | -7.756 | -42.5648 | 2025-10-07 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 7162833f-0abd-32ac-b6ae-6bc7da3a32d6 | -12.4041 | -50.2787 | 2025-10-07 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c7647bad-ab37-3586-b57b-3d71158cb8e1 | -13.2619 | -47.2362 | 2025-10-07 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| d735a224-7cfd-316b-9c78-049708322930 | -10.3718 | -50.3577 | 2025-10-07 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 214acf42-4e63-39cd-b9a7-6c865e92cc9d | -9.1786 | -47.84 | 2025-10-07 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 12c58048-75fb-33ad-930d-18364c5a4052 | -13.2232 | -51.6744 | 2025-10-07 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6d3a3903-dc7e-350c-9613-ad417e927f14 | -12.9101 | -54.7558 | 2025-10-07 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| b90434d8-e6c4-3bdd-8d39-48bb474c6527 | -11.7837 | -45.1115 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 7161439e-aa42-3263-a5aa-93bfb21ef9f3 | -9.2166 | -47.8142 | 2025-10-07 13:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| a68ff81d-5029-35c4-8200-84d37d8e4b48 | -11.1644 | -54.8804 | 2025-10-07 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 293.9 |
| c231ca0d-7df2-3b84-bb56-be1fc7bb565a | -14.9414 | -51.448 | 2025-10-07 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 44e1527a-babc-3c69-b3f5-5878b30b9adf | -6.9893 | -42.0004 | 2025-10-07 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 85b1ef07-d983-3f8a-8d79-cdd60b4d8082 | -15.8091 | -43.7597 | 2025-10-07 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 7a52da27-45ff-3f23-94e5-974f9f59daba | -12.2215 | -44.2543 | 2025-10-07 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4d9121ee-63d8-327b-b4b9-c4913a6ab6b0 | -11.2228 | -47.8516 | 2025-10-07 13:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f4a9da67-49ea-3008-9cbd-9e57c488f903 | -8.1879 | -44.2283 | 2025-10-07 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 91858d03-77c9-3637-bd5a-72135b79b542 | -14.3144 | -45.8579 | 2025-10-07 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c942bdb2-9a8c-387f-9ac7-f954ed193c2e | -8.2346 | -49.8734 | 2025-10-07 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 22cd1a0e-a666-34dc-ae53-2712a9513147 | -13.243 | -47.2165 | 2025-10-07 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 90281343-731c-3194-b3a3-16170f28ec9a | -7.6651 | -45.4245 | 2025-10-07 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |


[Clique aqui para ver as próximas entradas](README124.md)
