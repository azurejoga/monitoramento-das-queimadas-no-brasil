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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59693333-b21f-3657-8ef5-fe8964a99d15 | -9.9651 | -47.373699 | 2024-10-16 00:40:54 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 634b791d-0f60-31e0-9f44-fe8b5eddffc0 | -9.9668 | -47.381199 | 2024-10-16 00:40:54 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b5358b8-499e-3d02-8651-c2116c8f6d87 | -9.9685 | -47.388699 | 2024-10-16 00:40:54 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3b772f0-8d90-3d72-ad8e-2b1534835fbc | -9.9535 | -47.368401 | 2024-10-16 00:40:55 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb08c7b-d5f9-3265-b50a-74c0699ec85c | -9.9553 | -47.3759 | 2024-10-16 00:40:55 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1e5b761-8ddf-3db6-8fa3-062a7f033e7e | -9.957 | -47.3834 | 2024-10-16 00:40:55 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b414d796-7c69-3411-a569-5869842b9f0d | -9.6099 | -46.022999 | 2024-10-16 00:40:55 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74b198a3-7fed-3904-9536-22c47902d162 | -9.9934 | -48.628101 | 2024-10-16 00:40:59 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 566a5819-eb07-3f10-84f1-c1de8f4a083f | -9.995 | -48.635101 | 2024-10-16 00:40:59 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9857862-a860-32d7-98b5-9819ce7d5710 | -9.6119 | -47.542599 | 2024-10-16 00:41:01 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 099a0f56-7306-3d30-aa58-8a9f50fb3690 | -9.6136 | -47.549999 | 2024-10-16 00:41:01 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa3a2aa6-6c95-352b-a587-0bca4aeb9119 | -9.6236 | -48.5429 | 2024-10-16 00:41:04 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc69e3d9-bf11-30e9-a142-5b24364432ac | -9.1699 | -46.968498 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6566c0d3-6c10-3993-920c-373f97df6771 | -9.1718 | -46.976398 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01639356-fc60-3a57-8f74-effa5c36f014 | -9.1736 | -46.984299 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28c7d1f6-c8cd-35bd-ac51-f25f6f96f183 | -9.1754 | -46.992199 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d08b01f-9291-3667-8862-dcbc003e47a6 | -9.1601 | -46.970798 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10bb0778-b5db-3a96-abde-0be8630a8f8e | -9.162 | -46.978699 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d04cf640-54c7-35a8-8dd2-3f13e75f0fdf | -9.1638 | -46.9865 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e848611d-0649-32bf-a2fc-031f46f8b884 | -9.1656 | -46.9944 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4591f81f-9d0d-3b40-b73c-b9cdd4fe5b39 | -9.1674 | -47.0023 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73cdc8f0-802f-3218-9adc-7e3c60c4c360 | -9.1558 | -46.9967 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43498941-5f03-372c-aab1-6b9c9014e16a | -9.1576 | -47.004601 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87bb3c14-4121-3165-98f8-d8172a9fa067 | -9.1595 | -47.012402 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92ec4d4d-10a9-3ce3-b48b-ce8fcbe489aa | -9.1424 | -46.9832 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8bcb2086-cd70-32b9-baf4-3221cce2fb57 | -9.1442 | -46.9911 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9b61d7f-2040-3e14-aea9-902fb61e42ae | -9.1461 | -46.999001 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebcbf5f3-242c-3f75-9790-a0dff6e6e8bb | -9.1479 | -47.006802 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d44d55c6-e629-3f99-94c0-b096a2180dae | -9.1497 | -47.014702 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4efcf2-3aca-345d-9632-8c609105812d | -9.2836 | -47.595299 | 2024-10-16 00:41:06 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 250c89a7-ea9d-3b10-8346-0e488307766f | -9.2853 | -47.602699 | 2024-10-16 00:41:06 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9aaebabb-ca92-3634-864c-b677b3ed14ea | -9.129 | -46.969799 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7232f6a7-d38f-3394-a657-77fc2ad9f7be | -9.1308 | -46.9776 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5bb3587-a769-34d6-aaf8-bf5aded7ce71 | -9.1326 | -46.9855 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28d63fd4-0808-36da-b0b9-7b1eb3cb49ef | -9.1344 | -46.993401 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d23d1e61-b55b-31e7-868e-dba4a69448ee | -9.1363 | -47.001301 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5420a79e-e9e2-3ef1-8122-feefb85494c8 | -9.1381 | -47.009102 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52e5c2c0-0a92-360d-a4c9-8ff35bc61195 | -9.1399 | -47.016998 | 2024-10-16 00:41:06 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac73a491-c034-3137-ad1d-1877dd079936 | -9.1229 | -46.987801 | 2024-10-16 00:41:07 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 983fe5fe-9967-39a2-8d2f-660eadcdb5a2 | -9.1247 | -46.995701 | 2024-10-16 00:41:07 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a66444e8-1683-3a35-a760-5ebe34326d4b | -9.1265 | -47.003601 | 2024-10-16 00:41:07 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da131365-43fe-3552-9aae-d276e95a3bf8 | -9.1167 | -47.005901 | 2024-10-16 00:41:07 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5644bccb-2236-3723-b81d-501b8c5cc251 | -9.1185 | -47.013699 | 2024-10-16 00:41:07 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 277abeda-cf93-314d-ad09-f65fbdf30346 | -9.2076 | -47.938702 | 2024-10-16 00:41:09 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de0c64b3-433b-3ccb-af7b-5e81d1d34fbf | -9.2093 | -47.945999 | 2024-10-16 00:41:09 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f77ffc10-517e-3fc7-8ded-12f574370716 | -9.1978 | -47.941002 | 2024-10-16 00:41:09 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89b2a9aa-4a8a-3ce6-8d66-1b33f69c38d1 | -8.9289 | -47.0415 | 2024-10-16 00:41:10 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d2f90d0-dbda-3e76-9aae-6c935a9b72b8 | -8.9192 | -47.043701 | 2024-10-16 00:41:10 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a7b75c4-9dd5-3d18-87e2-632ed83960ab | -8.921 | -47.051601 | 2024-10-16 00:41:10 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 688d8859-88b2-3dd6-962a-8998e2a9f529 | -8.4788 | -47.013302 | 2024-10-16 00:41:17 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c253ddd6-44bc-3eed-8b43-8a34f6b8bf83 | -8.4806 | -47.021198 | 2024-10-16 00:41:17 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f74ed8f3-bb4b-3836-8c15-99b03a222894 | -8.141 | -47.0247 | 2024-10-16 00:41:23 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e2119f2-a3c5-3692-b774-9ba3d575b5b8 | -8.7462 | -49.770901 | 2024-10-16 00:41:23 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 823b6f00-d70c-3384-bdc4-d828ba179e38 | -7.8542 | -46.236 | 2024-10-16 00:41:24 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea5a142-1112-3328-9e8c-7c3c58fc0cfd | -7.8562 | -46.244701 | 2024-10-16 00:41:24 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f24a2bce-c50c-359c-bf19-2c707e69e619 | -7.8444 | -46.2383 | 2024-10-16 00:41:24 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f4ab4a0-b344-3d82-92ed-7e45dc1f61f4 | -7.8465 | -46.247002 | 2024-10-16 00:41:24 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9c9a94-03eb-314d-aab4-6bb3f78a0eb6 | -7.8486 | -46.255798 | 2024-10-16 00:41:24 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ceb702d-7174-3530-8254-5354f73c0e93 | -7.3248 | -44.258801 | 2024-10-16 00:41:25 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36f05f20-fa94-31a4-be89-1901022fa4f0 | -8.3996 | -48.918098 | 2024-10-16 00:41:25 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1f283471-daf4-3c2a-a64d-2c28c4aa33b6 | -7.6017 | -46.789799 | 2024-10-16 00:41:30 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b512720-9479-3faa-a05b-a618550b6508 | -7.6015 | -46.8335 | 2024-10-16 00:41:31 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cdc5174-6733-375b-afcb-2a6e1053d9ed | -7.1471 | -45.027802 | 2024-10-16 00:41:31 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f08cbf78-fe2a-3599-b7ee-d03e52100e0f | -7.1496 | -45.038399 | 2024-10-16 00:41:31 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b077fed5-be86-3247-a5b3-dd02a8011b96 | -7.6455 | -47.156601 | 2024-10-16 00:41:31 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a62663b-161b-3fee-9508-4f01e4a3fe3d | -7.6339 | -47.150902 | 2024-10-16 00:41:31 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1380f68-07b7-382f-a6be-49d52ced0573 | -7.6357 | -47.158901 | 2024-10-16 00:41:31 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14d032bf-eb69-3b85-93b8-3a4695b1c261 | -7.6241 | -47.153198 | 2024-10-16 00:41:31 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a92f9b8-c169-3618-9b37-0ffd99e1ddca | -7.6259 | -47.161201 | 2024-10-16 00:41:31 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01c508cb-cb6f-3de4-9e9b-02079b504390 | -6.7118 | -43.548801 | 2024-10-16 00:41:32 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44a58457-81d3-3c2a-82c7-7d444ac115a3 | -7.5037 | -46.8563 | 2024-10-16 00:41:32 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bf47aef-78b1-34a5-ac15-5ab8f52c4505 | -6.9057 | -44.3592 | 2024-10-16 00:41:32 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c82b9e20-f7f2-3cf2-bb9f-5655167f3a11 | -6.9085 | -44.3708 | 2024-10-16 00:41:32 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97442cd4-fa8e-3fcd-aa33-24a14a455c7e | -6.9112 | -44.3825 | 2024-10-16 00:41:32 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45eca27c-d859-32b3-9051-0e768bbfb9ae | -6.8987 | -44.373199 | 2024-10-16 00:41:33 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98091992-411a-30b5-91db-00ef5856c021 | -7.1267 | -45.421799 | 2024-10-16 00:41:33 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aed82da3-5eb3-3db6-a8a3-31dae1518350 | -6.6047 | -43.403198 | 2024-10-16 00:41:34 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 11b1e439-7988-3b47-848f-38a03af5e53f | -6.608 | -43.416901 | 2024-10-16 00:41:34 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8c2e806-6cfc-394b-ba05-b63135b75759 | -6.8054 | -44.456902 | 2024-10-16 00:41:34 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78ed62e7-d8e2-322e-9d51-e2dbd252d7d0 | -7.0575 | -45.5219 | 2024-10-16 00:41:34 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53ca6d58-0c18-328f-bb23-bea8968758bd | -7.0598 | -45.5317 | 2024-10-16 00:41:34 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b967eb14-3406-392b-86de-b7e704b47ef5 | -6.6011 | -43.6455 | 2024-10-16 00:41:35 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3001512e-7ae5-3fd6-a1ba-8b112d185c0f | -6.4792 | -43.866798 | 2024-10-16 00:41:37 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21b14ae6-6f61-3ff5-bcfe-fa1ab5292d62 | -7.159 | -46.527302 | 2024-10-16 00:41:37 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43a2f42e-979d-300d-9163-ad4c598bed3f | -7.1374 | -46.523102 | 2024-10-16 00:41:37 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91f8ba7d-1410-3102-b572-04c1385b8b2a | -7.1394 | -46.531799 | 2024-10-16 00:41:37 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4302268-f757-3081-be33-65ac88e921bb | -6.1793 | -42.7057 | 2024-10-16 00:41:38 | METOP-B | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c1a6573-f23e-350d-82aa-8d4ae15df6cf | -6.1831 | -42.721199 | 2024-10-16 00:41:38 | METOP-B | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f8850d1e-e31f-3a20-af30-59f85db2a297 | -6.1696 | -42.708 | 2024-10-16 00:41:38 | METOP-B | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef55414c-23e6-376a-804b-9df08f5fc76e | -6.1734 | -42.723499 | 2024-10-16 00:41:38 | METOP-B | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d710aba-d62b-3a9a-8f42-e88a11b295bd | -6.6662 | -44.694599 | 2024-10-16 00:41:38 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba7ff45-b480-3050-9a9d-29d82de5cf05 | -6.4903 | -44.129101 | 2024-10-16 00:41:38 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f20092d-2469-3ad2-a9e3-85b9d44efb1f | -6.4933 | -44.141399 | 2024-10-16 00:41:38 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f514c13-71f6-323a-8cfb-5d338905fd03 | -7.0912 | -46.7677 | 2024-10-16 00:41:39 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f88812b6-069e-3c93-9577-df7e9ea26608 | -6.5241 | -44.4006 | 2024-10-16 00:41:39 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2bba1d1-1c9d-3bcb-a893-25e8a633508f | -6.5269 | -44.412399 | 2024-10-16 00:41:39 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdd499d4-e7ac-3b93-8b7d-d2e9e4a92159 | -6.5297 | -44.424099 | 2024-10-16 00:41:39 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0b8ef2e-f03d-3ce9-82f9-8954e5b41105 | -6.2178 | -43.806702 | 2024-10-16 00:41:41 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00ff7bc1-294a-3b46-b66a-b64a3a834e4e | -6.896 | -47.304901 | 2024-10-16 00:41:44 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85192eaa-cd40-3227-a913-5aa8575ed5c6 | -6.8979 | -47.312901 | 2024-10-16 00:41:44 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
