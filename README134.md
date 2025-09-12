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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 706c21d8-5a94-3788-87b0-3097408b1f30 | -12.9101 | -54.7558 | 2025-09-12 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 283.1 |
| d5989943-4eb6-35ce-bf5c-fb4d6a8dc6e2 | -10.0717 | -46.116 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 511.1 |
| 39c8ea7a-138f-3bd4-b7fe-39b50545d824 | -8.956 | -46.1074 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 09c490ed-688a-3eb3-9f0e-4cd12068bdb3 | -19.1522 | -50.7565 | 2025-09-12 14:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| afd44006-22c0-351b-9df0-0d27f966d9f9 | -9.0376 | -47.0819 | 2025-09-12 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 602239da-c139-36cf-a759-fdc1dea01fa7 | -9.9004 | -51.8811 | 2025-09-12 14:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4083f97c-db40-3a9b-a3ee-b3cc0aa9ff0c | -8.4143 | -47.2545 | 2025-09-12 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| adcdf441-754c-3a53-966d-555368c04435 | -11.5232 | -50.6182 | 2025-09-12 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| f8689c01-8667-376f-a972-1009b3e8af2a | -6.3226 | -53.4553 | 2025-09-12 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f3185acc-e581-310d-b5a5-8d2661bd4e58 | -11.4093 | -43.5573 | 2025-09-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 590cd5ec-92d6-377a-8929-ce515a3d56ba | -9.0748 | -47.1224 | 2025-09-12 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 292.8 |
| 07e22dd3-6752-30ab-abdd-9338b66bb68d | -9.0166 | -45.8077 | 2025-09-12 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ea7de974-bb3f-3d11-aede-4d7c0fc7c331 | -14.1907 | -46.2012 | 2025-09-12 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 81a5608f-a1ae-3f33-a5de-c6311950dc4e | -9.4804 | -46.4321 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 233bb44b-d88f-3bd3-91cb-e5ec92cd6c54 | -15.1053 | -48.0209 | 2025-09-12 14:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 128.0 |
| a11e5f8d-6cd1-352d-af65-538d26a27163 | -14.4394 | -47.3206 | 2025-09-12 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ae624096-f8a2-390d-ba6f-49892e67b13c | -16.08 | -49.9709 | 2025-09-12 14:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| d61904d2-f155-37d1-a8a8-919fc6f8a336 | -14.1717 | -46.1815 | 2025-09-12 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 57cfbd12-6d9c-3a34-bbbe-ebfd47103522 | -16.3623 | -51.4969 | 2025-09-12 14:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 05eb33a0-4833-3209-87e2-acba22138627 | -8.9749 | -46.1054 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| a1390a30-d034-39dc-8034-786577efc642 | -8.4705 | -47.2712 | 2025-09-12 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 31ce76a1-2a04-315c-82bc-2d022b36f146 | -8.9087 | -49.9433 | 2025-09-12 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 3103414b-46ef-3ab6-a755-2cdb0b6dd15d | -11.5425 | -50.5947 | 2025-09-12 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 9a537749-f751-3715-b510-ca5858d88ba0 | -9.0936 | -47.1205 | 2025-09-12 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| b71e7b2d-a92e-39a1-b93e-c3b9a3fb64d4 | -8.1837 | -46.0965 | 2025-09-12 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ff4bf1d8-a9f1-3213-a1a3-f972642cf13f | -14.4588 | -47.3174 | 2025-09-12 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 65b6668c-c947-3c5f-afa5-e1d7e2113e98 | -13.2798 | -51.7312 | 2025-09-12 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3524b8de-fdc4-3f27-bade-df4bb1ee6734 | -7.4511 | -44.4177 | 2025-09-12 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| a000b09b-3f09-356a-ae84-b7ee2ea52ee3 | -6.1705 | -41.0658 | 2025-09-12 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 9e5f9b61-21f1-3180-88fd-4ed694b06d57 | -9.5137 | -54.6292 | 2025-09-12 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| fe5b55bd-e848-3b8d-83e7-60cd9a3dac7e | -6.8182 | -45.6574 | 2025-09-12 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| cd0ce92e-9c39-327a-b27f-ff98a1f1bc54 | -8.0817 | -50.1836 | 2025-09-12 14:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1349a870-e080-3411-b35e-33807bcc0ecd | -9.673 | -47.5459 | 2025-09-12 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 9836c147-1ec8-3e34-a6cf-775f1733d4ef | -7.5643 | -44.3838 | 2025-09-12 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 190.3 |
| ac57ea09-52d1-35d0-b146-17978c5576b8 | -8.4893 | -47.2694 | 2025-09-12 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6558a260-2ebd-3f15-9d72-c325e4681917 | -19.0618 | -48.7281 | 2025-09-12 14:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 155.9 |
| b003738b-d820-3f6d-80ed-628f4df1d4c4 | -11.1949 | -48.4277 | 2025-09-12 14:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 49f8be74-8459-30cd-ab6f-a7afb77979ea | -15.1058 | -47.9983 | 2025-09-12 14:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7a769b79-facf-3d52-84b2-27fd58c48abd | -14.2927 | -45.0495 | 2025-09-12 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 77515ed0-7d49-379f-ba1a-c14f0612242c | -8.9563 | -46.0849 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 438f07a2-3dc2-3658-89da-d0a5086f6093 | -7.5452 | -44.4086 | 2025-09-12 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 167.3 |
| d1f5359d-2a02-3e09-8f12-33daf5cdaad8 | -11.1061 | -51.9958 | 2025-09-12 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 3b40e462-4e86-376f-bdc4-391077756519 | -6.309 | -42.2311 | 2025-09-12 14:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| dca5f607-b9a8-3162-9a25-63d651a17784 | -9.5324 | -54.6277 | 2025-09-12 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 3b74695c-7787-380f-a33e-c49e45f47fff | -7.542 | -44.6844 | 2025-09-12 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 66d3d501-9b81-36ef-bcff-fffad4c29cbf | -8.414 | -47.2766 | 2025-09-12 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 368e75f1-22c9-3bde-96e6-0b9cf75985e0 | -7.5641 | -44.4068 | 2025-09-12 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 1f02d9ca-944e-34f2-948b-81ee70dbb9b4 | -10.0754 | -47.1686 | 2025-09-12 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 1d55952a-a657-3f88-a355-10d983ac27a9 | -8.8768 | -51.111 | 2025-09-12 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0d9d10f7-6d11-33f2-8655-fda340c55924 | -11.5422 | -50.6161 | 2025-09-12 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 214.0 |
| cc00c1c2-e343-3faf-aef1-f5b99caf355f | -8.9368 | -46.132 | 2025-09-12 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 45173f6b-be41-367e-90f5-434bb4337521 | -9.0759 | -47.0335 | 2025-09-12 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ef941873-2167-380c-ba3d-511278daf3c1 | -7.5455 | -44.3856 | 2025-09-12 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.2 |
| d7deef8f-b8ea-383c-868e-197fdc094720 | -6.1732 | -42.6458 | 2025-09-12 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 0dc23eba-91d5-38a1-a789-2b96d7609c5c | -9.5137 | -54.6292 | 2025-09-12 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 5a210104-32d5-3d39-8d31-ab5fa655bdfa | -12.9292 | -54.7538 | 2025-09-12 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 228.7 |
| 624ed52d-2be3-344f-94c9-95b85f6f479f | -9.9571 | -50.3353 | 2025-09-12 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 3386fe75-85d3-3053-a3e0-ed4abe5d999b | -19.1522 | -50.7565 | 2025-09-12 14:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| cee9ece0-2dc0-38f6-8f88-5be8f50c0b42 | -9.0748 | -47.1224 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 392.7 |
| 5b99c8b6-0af9-3941-b1c2-1c808ee67642 | -8.1837 | -46.0965 | 2025-09-12 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| dea4c80a-e730-370a-8b5d-026b061911d5 | -13.2801 | -51.7099 | 2025-09-12 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| b7c44bb4-bcae-3759-bac5-1380ede94e19 | -8.4328 | -47.2748 | 2025-09-12 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 385e832f-4983-35f8-a8fa-9842cbc87808 | -15.5819 | -54.7637 | 2025-09-12 14:10:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 68683c03-6683-3e07-908d-1a9e56fecdc8 | -10.4441 | -50.6059 | 2025-09-12 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 224.7 |
| e36553c0-8b6c-3900-a7bb-a59d3d9a289e | -8.9365 | -46.1545 | 2025-09-12 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9df0f920-129c-387a-a675-6dff64cb78f3 | -6.1735 | -42.6221 | 2025-09-12 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 147.0 |
| 605f0dcc-90d2-32fa-9c75-92a90f42b184 | -16.08 | -49.9709 | 2025-09-12 14:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 234.3 |
| dc1f98fe-cf78-37cd-9a49-7c5215ebc9aa | -8.9087 | -49.9433 | 2025-09-12 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3cb0dd5d-c4ae-3d09-8246-22d2455a88eb | -9.057 | -47.0355 | 2025-09-12 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| beca61ab-3455-304d-8bba-e96d32a48004 | -7.5643 | -44.3838 | 2025-09-12 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 08411352-90e3-3b13-a9a0-250b146f06fa | -9.075 | -47.1002 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| f68b3f08-3491-33ea-9f83-95f0f7959425 | -10.1405 | -47.9133 | 2025-09-12 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4112c972-84b6-3317-b94a-490a1afe235d | -6.3226 | -53.4553 | 2025-09-12 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ce687378-857b-3461-a23d-36c41c721e09 | -6.1705 | -41.0658 | 2025-09-12 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 1c6e9d66-3105-3ef5-bb20-af49c1bda74a | -8.9371 | -46.1094 | 2025-09-12 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| cd56e292-e463-3234-918c-c7b37bed0b63 | -16.9621 | -45.8176 | 2025-09-12 14:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 38d93788-8cc6-39c0-907e-f833fcb66375 | -11.526 | -50.4255 | 2025-09-12 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 9c4b7864-a1e5-305d-bed8-df4378ba1f82 | -12.0849 | -47.6065 | 2025-09-12 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c29c08cb-c4ce-3fdb-b21d-1c155d3bb01e | -6.7501 | -44.9839 | 2025-09-12 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a47757a6-3134-31b4-a6ee-a7fda673941f | -15.0246 | -50.1148 | 2025-09-12 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| de8ee5f1-0a28-3cb8-9ca4-61acb6ff9302 | -11.6806 | -46.6536 | 2025-09-12 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 99158b58-41dc-3151-a17d-39debb73160b | -15.1363 | -52.4679 | 2025-09-12 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| df81e14e-63bb-3cb1-a617-e0b703d90162 | -8.096 | -45.5641 | 2025-09-12 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 0113e973-bf85-3b66-9a9c-a9c344394e08 | -11.8761 | -47.5232 | 2025-09-12 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 2cde4283-6a88-351c-8306-38264dfd9684 | -11.9713 | -51.164 | 2025-09-12 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 362586dd-533a-3c5b-9e6c-de58efd5d354 | -10.1133 | -47.1642 | 2025-09-12 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ca501d11-8877-3df4-880a-3c3a33fa26e0 | -11.4477 | -43.5514 | 2025-09-12 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| cd9fcf21-8a23-3b30-b486-80de2770a40d | -8.2085 | -45.5981 | 2025-09-12 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 78883841-a172-3dd7-bf04-7459d5a8401e | -6.8182 | -45.6574 | 2025-09-12 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| dd021353-fc7b-3e49-a885-9c1e40961758 | -9.0936 | -47.1205 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 195.4 |
| a794cc10-5b26-3dd7-bac3-ebecf3695b15 | -8.414 | -47.2766 | 2025-09-12 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6ba961dc-ae88-352b-b5ca-cb70b145a366 | -14.4394 | -47.3206 | 2025-09-12 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3ca080dd-be2e-3451-905e-c904a871696d | -7.5452 | -44.4086 | 2025-09-12 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 1e8e720a-47c3-3614-b99a-682953bf7354 | -15.1557 | -52.4652 | 2025-09-12 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 48f64b82-b6a3-3590-a511-1fbead18f6fa | -6.7503 | -44.9611 | 2025-09-12 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f9975fba-3561-3f2f-9195-7b8f9a92282b | -11.9723 | -51.1001 | 2025-09-12 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| fcdad6e2-5a5b-307f-928d-96d085fcf8ee | -11.5422 | -50.6161 | 2025-09-12 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 941a32bc-e552-32c0-9a4a-8cf77f1e040f | -8.4143 | -47.2545 | 2025-09-12 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e06d8855-79d8-3722-9a4b-0cfbbcff877d | -10.7172 | -48.6371 | 2025-09-12 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| cd7815bf-5e83-309e-b94d-369dbb18778d | -11.9332 | -51.1683 | 2025-09-12 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 167.7 |


[Clique aqui para ver as próximas entradas](README135.md)
