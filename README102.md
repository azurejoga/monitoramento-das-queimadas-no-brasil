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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22474409-afaf-36a9-bd06-abedf71fc200 | -18.0723 | -45.9553 | 2025-09-02 14:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 73f2a330-6b0f-3cfc-97a3-484a052ecc93 | -12.8629 | -48.0323 | 2025-09-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a70ab9d4-7d81-3713-a2f8-e37805146867 | -16.2953 | -52.9443 | 2025-09-02 14:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 10dce96f-753d-3267-8cbc-fa6e6cb130ba | -8.2008 | -49.5345 | 2025-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 2f8404d9-fea6-3fb3-b54c-404529e1c313 | -10.8947 | -50.8356 | 2025-09-02 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| e42bf890-2eb1-3d4e-806a-2fe659f84afc | -6.9632 | -44.3477 | 2025-09-02 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 81ac120c-022e-3f64-a003-dc53925e3677 | -7.5292 | -61.3254 | 2025-09-02 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 78d44940-8a28-3086-9c39-3592d297d134 | -11.672 | -52.168 | 2025-09-02 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 299fe999-b753-3e78-b669-95c1696486bc | -11.1037 | -44.6315 | 2025-09-02 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 294c9ec7-b9b0-3de6-ab77-7dd3959a3200 | -7.9351 | -46.4559 | 2025-09-02 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| de3b0fc9-efbd-360a-9b65-68a40489a1a0 | -7.5477 | -61.3247 | 2025-09-02 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 333.3 |
| ddf3dd3d-8bf7-3116-b618-7445297da09c | -6.666 | -45.8946 | 2025-09-02 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c314eb1d-33e1-3e77-8e6c-39be0ca8a4f7 | -9.4794 | -46.4994 | 2025-09-02 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 678823c4-9cb5-3358-a5ab-de53b5992913 | -9.0141 | -45.9886 | 2025-09-02 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 62bbda58-21ba-310b-a389-0bbf5d8da58e | -11.9415 | -50.6131 | 2025-09-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 233b9b56-aff6-32ea-801b-db9a79706258 | -11.4491 | -46.7973 | 2025-09-02 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 5af968f5-c203-37d8-b0a0-e36a85c05788 | -14.5469 | -53.0106 | 2025-09-02 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 2f318f99-ac27-3bf5-97a5-cd3db3aaed1f | -9.2822 | -47.1229 | 2025-09-02 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| aa58f14b-d609-326c-b34c-1050c4818b40 | -11.3911 | -46.8499 | 2025-09-02 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| df269055-c922-3394-a105-233064c1f7b2 | -11.0841 | -44.6575 | 2025-09-02 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| d1bc4729-c938-382f-bc51-f5adc63837f7 | -9.4791 | -46.5218 | 2025-09-02 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 503.1 |
| abf8b451-b773-3e76-868a-779fb7054ec7 | -8.201 | -49.5131 | 2025-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| e8a71baa-d63b-3c0d-aa03-2b38507b819f | -12.7734 | -47.6666 | 2025-09-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d879b33c-183f-3eb9-ba38-a05fb66e384e | -7.1091 | -44.7474 | 2025-09-02 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0d721f00-935c-3a8e-a1ad-b6b6b00aaed2 | -4.2937 | -46.2726 | 2025-09-02 14:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 65436909-6959-3d95-a68a-c55adb1118e8 | -11.6717 | -52.189 | 2025-09-02 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| e4f42ca7-da7f-3c90-a44e-9743c33aa415 | -6.982 | -44.346 | 2025-09-02 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8a844c6c-c297-3341-8242-33fb6fb614ce | -11.6647 | -57.3533 | 2025-09-02 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 310.3 |
| 3bcc724e-beeb-35a1-9071-67331c84158a | -11.6644 | -57.3733 | 2025-09-02 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6d591eab-4433-3f4b-8914-d089e9565039 | -6.0291 | -46.0103 | 2025-09-02 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 24708e3b-660a-3e73-ba7c-9058fe718989 | -4.9124 | -43.187 | 2025-09-02 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 7e678d46-b644-30fa-a759-6ec4d5dfd2df | -6.9754 | -43.2326 | 2025-09-02 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 152.6 |
| 4546134b-b120-3674-812e-d8d72897ecf0 | -5.8642 | -45.6408 | 2025-09-02 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 0520506a-ad6e-3449-a41e-beeaddce5cf0 | -6.7723 | -52.8176 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 5c9e8a0c-4308-3fa9-b8bf-3fa6e2ef57a1 | -8.6883 | -62.4002 | 2025-09-02 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 159.6 |
| de50d1a2-23b2-3ef3-8072-2e10fd15d1fe | -8.201 | -49.5131 | 2025-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 203.8 |
| 7c1607f0-6fe3-3b27-a86d-d72ae8db30b0 | -6.8911 | -45.8538 | 2025-09-02 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9b250db3-5872-3700-bd6f-ad2515eb7a24 | -7.9163 | -46.4577 | 2025-09-02 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 629901fc-a65a-3efc-b06a-6ad0a43cb857 | -6.9129 | -45.5593 | 2025-09-02 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 0907cba4-356a-3d0f-a17e-ad2ad2c2d176 | -6.9945 | -43.2074 | 2025-09-02 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| a7c4bde9-3320-3e5a-8f4e-300561514706 | -18.0723 | -45.9553 | 2025-09-02 14:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 99d2ad79-28ca-303d-b633-d845d8d7e92b | -11.3893 | -43.6075 | 2025-09-02 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 12bbc7b6-6d80-3771-89f0-49aee04bfcaf | -7.5292 | -61.3254 | 2025-09-02 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9b8b94d3-5ac9-3bb9-b7cb-45b210db10d4 | -6.8466 | -52.8132 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| a8d0aa9d-62b6-32c7-9511-bef117560ff6 | -11.9876 | -51.3532 | 2025-09-02 14:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 958e0f5b-08b2-3e31-8636-0147363e49b2 | -5.3974 | -43.3867 | 2025-09-02 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 17de48cc-ee00-3974-b16e-84ba5d5390d7 | -9.4498 | -62.3294 | 2025-09-02 14:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ef855fff-bcba-3371-8cf9-59a65081aee3 | -6.0699 | -45.6259 | 2025-09-02 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 54f07244-e92d-3672-a7c6-27bec9cd1cec | -4.9124 | -43.187 | 2025-09-02 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 331.7 |
| 0a50c2af-3524-375a-9814-5e9c87876fcf | -8.2198 | -49.5115 | 2025-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 210.2 |
| 36badabe-3a1d-39af-a998-091e10765a23 | -10.2486 | -51.134 | 2025-09-02 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 89b09cc5-0497-31e7-9762-1c8a9891c6c4 | -11.6715 | -52.21 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| bbd567ae-0c64-3623-8956-dacc6f6e6cc5 | -7.484 | -44.8272 | 2025-09-02 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2ecc7b87-2518-3f04-af74-76e439dab49c | -6.1848 | -43.3724 | 2025-09-02 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 943e6a7e-303b-3ca5-a4a0-82ca6a66f78c | -14.5662 | -53.0081 | 2025-09-02 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 08bb55f6-2aaa-3d38-ae63-958cfa5caf9c | -5.8882 | -42.9988 | 2025-09-02 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 152.9 |
| 98c78a9a-f3c5-3791-9aef-8e8b502b8413 | -6.982 | -44.346 | 2025-09-02 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| bea68bd6-09c1-33ae-8510-4755a4aa6bd2 | -10.8947 | -50.8356 | 2025-09-02 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| fd66f628-c5fa-3d30-845c-7b0725e6bff3 | -11.1252 | -50.5982 | 2025-09-02 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| cb4d10ae-c21e-3556-b03d-1893d8ddfab2 | -9.4791 | -46.5218 | 2025-09-02 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 353.5 |
| 32b5a89a-cd47-3b41-b823-dcdc8b95d149 | -6.7725 | -52.7971 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3ca3786f-24e4-3517-ac4f-6dfbc144f468 | -6.204 | -43.3241 | 2025-09-02 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 640f6099-18ec-30ec-9af1-4c445ade21ef | -8.1995 | -44.8023 | 2025-09-02 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2c2ea8d2-51eb-3484-a30e-a3e5aa843e99 | -6.2036 | -43.3709 | 2025-09-02 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c06a4ee0-e741-390a-94dc-610a3b6c7df6 | -8.5983 | -61.9481 | 2025-09-02 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 004a1240-7bac-3897-9bff-2ad6e211c60a | -5.8694 | -43.0003 | 2025-09-02 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 009d3b14-d365-33d6-86c1-68015a3172d1 | -6.7911 | -52.796 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 004c81dc-ba51-3c2b-a88d-cdd2439ec610 | -5.6761 | -43.6451 | 2025-09-02 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 92032b9f-263f-3205-82e3-3b4cb79cc4b2 | -9.5025 | -57.8032 | 2025-09-02 14:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 41dd9182-be77-3438-af0c-069c89c39a41 | -8.5947 | -62.5747 | 2025-09-02 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c89158ad-16cc-31ce-86e2-8f50f833c2b0 | -8.6882 | -62.4192 | 2025-09-02 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| c7adbb84-b732-3cae-a1e3-25975b48cd04 | -11.8586 | -52.3998 | 2025-09-02 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 439377da-662c-3ad5-9293-75de181528c5 | -5.8507 | -43.0018 | 2025-09-02 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| b0e77547-c489-38cb-a400-4de3c7514a46 | -15.7363 | -53.6772 | 2025-09-02 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e448bc2d-7794-3840-b3e6-b9d28fd02c01 | -5.8692 | -43.0238 | 2025-09-02 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 8999d057-a2c3-3db0-88f3-0c40f20de342 | -9.4984 | -46.4973 | 2025-09-02 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d6979380-d877-3e72-b535-468410641a2d | -5.9222 | -43.3703 | 2025-09-02 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 85.0 |
| a07602c7-d391-3796-9bb7-39bea7eaa1c7 | -6.666 | -45.8946 | 2025-09-02 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 778080b8-2fbd-335f-92ad-826728bc38d6 | -7.1089 | -44.7703 | 2025-09-02 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 52e5b2fd-5a82-3cc7-97bb-bc7f80991b99 | -9.4987 | -46.4749 | 2025-09-02 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 213.0 |
| d47ab5be-706f-304b-a548-be4273dd271f | -8.2008 | -49.5345 | 2025-09-02 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| ff537977-3425-3db7-8d7c-a9e380b1d515 | -9.7483 | -48.9814 | 2025-09-02 14:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 298.3 |
| cac65a04-4ddc-32fe-be03-06e6d8be9092 | -8.8854 | -45.7314 | 2025-09-02 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 254291f4-bdb8-3a38-b7be-0bed856722cd | -8.3291 | -44.9948 | 2025-09-02 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 7447bba2-b33c-3b45-a796-ba78d96c4fa6 | -4.8936 | -43.1882 | 2025-09-02 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 55d6ecd8-ded6-34f2-a47b-0522a7718af1 | -6.9942 | -43.2308 | 2025-09-02 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 222.8 |
| 2045533f-2d0c-3b60-b586-f69340bdcbdf | -6.0291 | -46.0103 | 2025-09-02 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ec364e18-5df7-3e59-88e2-e69217298586 | -6.3504 | -45.6273 | 2025-09-02 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 19dcbf96-31ac-3c35-bbda-32ed9404abae | -15.7366 | -53.6561 | 2025-09-02 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 24b5e58b-0553-3dfa-bcd2-828335398d25 | -10.0623 | -48.0978 | 2025-09-02 14:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 78e683c9-7936-35db-8f7b-b0fd3a3f43ce | -9.4981 | -46.5197 | 2025-09-02 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 59ebb19b-230e-345b-a308-c519104303ed | -11.6527 | -52.191 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| e065e993-2ce3-3c8a-b989-b10bfa9dc44a | -8.6673 | -62.8369 | 2025-09-02 14:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| a1262ed8-e670-389f-be40-bca7521a110c | -6.2794 | -43.2945 | 2025-09-02 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 04054506-fe90-305c-b90a-2f00a2e2fc48 | -7.4969 | -45.3495 | 2025-09-02 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1ce420cb-8c84-3923-aa51-5764d0fe54f7 | -11.1033 | -44.6548 | 2025-09-02 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 499.2 |
| 0c0c5919-4f89-3dec-99cc-0a111e4b3da9 | -6.8654 | -52.7916 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ea4d8bd3-bb3a-3c01-a1fa-a46665181eba | -10.8487 | -47.4546 | 2025-09-02 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 5422fdad-394a-3142-9c1c-786e7afda1ab | -5.6571 | -43.6697 | 2025-09-02 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 5dc9d8f6-3e89-36dd-9786-5ae46aff4778 | -8.6131 | -62.5929 | 2025-09-02 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |


[Clique aqui para ver as próximas entradas](README103.md)
