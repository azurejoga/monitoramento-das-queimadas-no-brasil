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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 904a8f5d-6af4-3543-8ad1-af15786946fc | -9.3554 | -46.747398 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7d894f3-6410-3032-9766-3a3064765c69 | -4.0112 | -48.948399 | 2026-07-13 00:49:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff42c1fa-1cb6-3513-898f-2bfd8a7dca75 | -10.1473 | -50.1101 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a118f30d-c092-3cbe-9959-649078ac86a1 | -9.3533 | -46.738602 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b093e06-3918-32f5-a618-407fd465d306 | -9.3763 | -46.7052 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a312e137-134e-339c-a323-5c4e7f26f38e | -10.1489 | -50.117001 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 698d9cb1-741e-3b2d-ad6d-29f6ad5544dd | -13.196 | -48.330799 | 2026-07-13 00:49:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55ea3c18-8100-33dd-9e2c-5c884f040f7a | -8.0972 | -47.101601 | 2026-07-13 00:49:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe374f9-4ee5-382e-b9f6-004b2c1d3ea9 | -10.1555 | -50.100899 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16927534-ce13-3183-91ef-a57f9b98b7b7 | -10.1653 | -50.098701 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 793777fa-b8f2-3e80-b75f-9719af8fbe68 | -8.1328 | -47.8657 | 2026-07-13 00:49:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7c4dfb0-8120-33e1-aef1-211b97e08521 | -8.8805 | -48.503399 | 2026-07-13 00:49:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38b69105-6b57-3bd9-9722-ba2be5ca33d0 | -10.1783 | -50.110298 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3639af75-3354-3a3a-951a-fa68d0a9651d | -10.1587 | -50.1147 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c47d624e-8859-3873-9f04-7d6e874bbd53 | -13.1944 | -48.323601 | 2026-07-13 00:49:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8f4c360-b479-3731-a272-875e9aee174a | -6.9597 | -43.712799 | 2026-07-13 00:49:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 756eb31a-9735-397d-9475-e98b48259e70 | -10.2277 | -50.055302 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9063a5c-b552-3a35-bfda-cb18f61a1919 | -10.1324 | -50.1353 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c4f2bde-df92-3d08-99cb-81e9a1e40629 | -9.3512 | -46.7299 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b28547cb-9dda-3b8b-a14d-b92cac4d584b | -10.1669 | -50.105598 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e562b0b9-dc84-3b2a-864f-af2e535c3ceb | -10.2045 | -50.089802 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad3089f6-41bf-30f3-8c86-b9598b4819ee | -9.3882 | -46.7117 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e05a439-418d-35ff-bced-8fa9d19d1bfd | -9.3609 | -46.727501 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cbb6b5d-5ef2-3e6e-9a10-16a347022ff3 | -8.8788 | -48.495899 | 2026-07-13 00:49:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4454429b-0bba-3f8a-8376-bc0c8ece533c | -6.95 | -43.715199 | 2026-07-13 00:49:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c573a4e6-f8b4-3e8f-a1cd-39cb277e296a | -10.203 | -50.082802 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1199f6-9681-34de-aa95-d7103e75a461 | -10.134 | -50.1422 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f95414b-2de4-307c-aa2d-d11659907b02 | -5.8061 | -45.110401 | 2026-07-13 00:49:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d642ab8-aaf0-31c7-a71e-a369431a855d | -9.363 | -46.736301 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3148f761-01bc-3de0-be50-09aaacfaba32 | -10.1685 | -50.112499 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0191e74a-ed4a-3eb4-a6fb-0750018405bb | -10.1505 | -50.123901 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0c33dbe-a9a5-34da-8d0f-201bcc05d234 | -10.2308 | -50.069199 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d63a97c-6b74-33ca-bc90-83412cbb072f | -8.8869 | -48.486198 | 2026-07-13 00:49:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 768618e6-075d-369d-b13b-9f3082bec5b6 | -4.1872 | -47.8451 | 2026-07-13 00:49:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 730023ef-2d34-3acc-b621-27d58af33465 | -10.1375 | -50.112301 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bafc8df-1cc3-3fb3-a89e-6e23874f9935 | -10.1407 | -50.126099 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 614d0f39-1da5-3b32-9ee4-4b7aebfcd1cc | -8.0853 | -47.0952 | 2026-07-13 00:49:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1053298e-630b-33c8-a597-ee64e408ec03 | -6.4954 | -42.209099 | 2026-07-13 00:49:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d34752b3-9386-3b8f-b7d5-958b4c9627d2 | -10.1571 | -50.1078 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9cd18d1-62a0-3bd7-9e2c-ed22d3550a80 | -8.093 | -47.084202 | 2026-07-13 00:49:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10b9682e-0539-3627-9193-b28275979a15 | -10.239 | -50.060101 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 683d9073-71aa-30c5-9fc8-9c2af9835876 | -10.1391 | -50.119202 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2d4e1e9-a916-3f23-92ab-f3ac4f235f4c | -9.3784 | -46.714001 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| daedd1ad-1d44-3f1a-b9d5-848a4791f702 | -9.3861 | -46.7029 | 2026-07-13 00:49:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d40393b1-1fd4-3288-a545-08f7e110c3bb | -6.5001 | -42.228001 | 2026-07-13 00:49:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b30fb804-89c5-3ea7-ba82-35168e83bef0 | -10.152 | -50.130901 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6a84025-66d5-37d1-aa69-fff1ab63d328 | -10.1422 | -50.133099 | 2026-07-13 00:49:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ab6cac5-87cb-32b0-8e5b-d6c77b26df89 | -8.8903 | -48.501099 | 2026-07-13 00:49:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8da58bd3-54e1-32b3-b160-5e3118ef9f27 | -10.1673 | -50.1222 | 2026-07-13 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 6b05b296-5cdf-3889-b719-6097f71e4e5d | -10.1295 | -50.1261 | 2026-07-13 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 5ce804d4-e8f9-3fdc-ae9b-2962ce3e53da | -10.1481 | -50.1456 | 2026-07-13 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 2b49d192-bcb6-3785-93b3-6d9f1802f7f0 | -10.1487 | -50.1027 | 2026-07-13 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8f6d3563-f573-31d4-931d-3ee148ac1796 | -10.2053 | -50.097 | 2026-07-13 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ca794ddf-38d6-3132-b14c-dffb5f496036 | -9.3821 | -46.7114 | 2026-07-13 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 1d1ae207-85a1-3277-b8d3-b59171769a81 | -10.1484 | -50.1242 | 2026-07-13 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 91e34ed7-5873-3de0-8db9-3d8d6caebf79 | -10.1675 | -50.1008 | 2026-07-13 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 3a8ddef7-05f3-302e-a8d1-7520b1d99520 | -10.1481 | -50.1456 | 2026-07-13 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 7715392d-4d09-3876-90be-15551ebdafbf | -10.1487 | -50.1027 | 2026-07-13 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| db6cf78c-ba16-37d1-9439-daf2ac88864c | -10.1675 | -50.1008 | 2026-07-13 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| fe7a7587-4580-3cc6-a72a-16e1b35550f1 | -10.1673 | -50.1222 | 2026-07-13 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5dc93bfb-6e57-31d8-8367-11350f1dd55a | -10.1484 | -50.1242 | 2026-07-13 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 92cc6130-55c9-3899-885a-58581dff8bdc | -10.1295 | -50.1261 | 2026-07-13 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 8a0f6073-2246-3aa8-95bb-44538797fd5f | -9.3821 | -46.7114 | 2026-07-13 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 21390559-dcc9-361d-a133-96f856254b29 | -10.1487 | -50.1027 | 2026-07-13 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 21ebba02-b0cc-3583-a2da-131f3f01396d | -10.1481 | -50.1456 | 2026-07-13 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 61325d42-bbdc-3081-afb4-306cfd4d9d02 | -9.3821 | -46.7114 | 2026-07-13 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e0e2bc94-3b9e-3533-b852-1c3984ec6d49 | -10.1484 | -50.1242 | 2026-07-13 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| f9d7278c-96b5-30b1-959f-ed9d6cebb009 | -10.1295 | -50.1261 | 2026-07-13 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 501da950-c643-325d-b56a-0223a5b251b7 | -10.1292 | -50.1475 | 2026-07-13 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 7bfcfe92-2b6e-34e3-a1f7-ccbc032bc094 | -9.3821 | -46.7114 | 2026-07-13 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| bc733431-b7b3-3089-a961-5c6abac9278c | -10.1484 | -50.1242 | 2026-07-13 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 0ce516bb-a83f-354f-a83a-da4c1238398d | -9.3821 | -46.7114 | 2026-07-13 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 03f49827-8bee-3948-9510-e4a5721297f7 | -10.1487 | -50.1027 | 2026-07-13 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4eec909c-6f1c-39e9-96b1-7b0aebf85fdd | -10.1484 | -50.1242 | 2026-07-13 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 482d5a67-4724-380f-9b9d-2b3ccf1b2c49 | -10.1487 | -50.1027 | 2026-07-13 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 67b0c811-e969-3f6a-8528-276dba9f3bbd | -10.1295 | -50.1261 | 2026-07-13 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 2797930c-8d01-3926-abd4-068286993cc6 | -9.3821 | -46.7114 | 2026-07-13 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 59e4d74b-8bb9-3bb0-a667-c1ce369cacff | -9.3629 | -46.7359 | 2026-07-13 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| c419b23a-4e7c-3d03-891d-3711f773971e | -9.3629 | -46.7359 | 2026-07-13 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f537157b-efde-300e-b15d-7e278eeeff13 | -14.6642 | -45.8656 | 2026-07-13 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 24997525-983e-323c-a6d2-38f21bf63ff9 | -9.3821 | -46.7114 | 2026-07-13 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6c02ecc1-eca1-3d79-94bd-3cd1c7258a33 | -9.344 | -46.7379 | 2026-07-13 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c524cbc8-75d8-3c82-8e5d-b5f9be13152a | -9.3629 | -46.7359 | 2026-07-13 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 164.6 |
| ea837fca-9a16-3ac3-8100-1ffff442af8c | -9.3632 | -46.7135 | 2026-07-13 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6581436b-5cca-3dc4-9ae8-620635004257 | -9.3821 | -46.7114 | 2026-07-13 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 74acb0c0-1715-3f81-803f-5cc1d6f67b05 | -9.3626 | -46.7582 | 2026-07-13 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 683ebb06-eb86-3b88-9c56-2f6e0bf71be6 | -9.401 | -46.7094 | 2026-07-13 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 608e04ff-44f6-36a7-a3b2-6640e444fe90 | -9.3824 | -46.6891 | 2026-07-13 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0b74dfa1-68dd-3a9f-8d0d-b0009f3fb48c | -9.3821 | -46.7114 | 2026-07-13 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 0018c4da-918e-360f-a022-baee16e1ffcd | -9.3632 | -46.7135 | 2026-07-13 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 630c4f44-386a-3563-8107-f28810c603de | -9.3818 | -46.7338 | 2026-07-13 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0b8baadd-282b-3a5b-b44c-cd30fc50cddc | -9.3629 | -46.7359 | 2026-07-13 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| ca9569e4-eeda-32de-a82c-3ddebca05ae1 | -10.2437 | -50.0503 | 2026-07-13 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 229bc7e4-0066-38aa-be37-d2d6f6571877 | -9.3629 | -46.7359 | 2026-07-13 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 02fc3bda-c402-3881-b5c6-90b77e50e4a5 | -9.3824 | -46.6891 | 2026-07-13 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3466a960-585d-3d43-919f-b84de042d422 | -9.3632 | -46.7135 | 2026-07-13 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ce01617f-2892-350c-88d3-fd3ad44f1dd3 | -9.3821 | -46.7114 | 2026-07-13 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6ba784c6-5193-3d82-8ae6-4f598ed579c6 | -9.3824 | -46.6891 | 2026-07-13 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f5bf1f18-d934-3365-b4cd-5a1459950cd9 | -9.3821 | -46.7114 | 2026-07-13 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f3adbaf2-1c86-392e-8fce-16139645c05b | -6.94802 | -43.71113 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README3.md)
