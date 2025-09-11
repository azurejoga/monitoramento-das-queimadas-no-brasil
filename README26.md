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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc4437a8-5765-3e82-98e3-c8a96d4af2cb | -7.83448 | -47.25885 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f25a35f8-0413-33b7-a3a1-8e1098685c9d | -6.67195 | -44.12922 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dcc3de87-4231-39f3-bc0c-4b338dc09f24 | -9.07126 | -47.07304 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af562414-9798-37a8-90cb-689bffb540f6 | -8.65419 | -45.72488 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d0f041b-604c-3fb7-a20b-4179e06e16df | -6.27777 | -43.3921 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2dac014-cd8b-3373-9010-f28d05a7d146 | -6.83556 | -47.90055 | 2025-09-11 03:55:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9a1e3e3-bfe4-3408-be34-91971fd031eb | -5.81943 | -44.20826 | 2025-09-11 03:55:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 990e23fc-5138-3b4a-9b1a-313c595b6016 | -9.70395 | -43.53997 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0db6fc9e-f796-3de2-9249-3cc7dcc4ac4b | -11.4218 | -43.54951 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d92e0b16-318d-370a-aead-cf6bf8e3c04b | -11.15219 | -45.29485 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1158cc54-559e-301e-b77c-db0619995d75 | -11.34261 | -46.48647 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 681150cd-632b-34fc-8ddb-6d5153b84af3 | -6.17104 | -41.08102 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 449397e0-608d-35bc-af75-b8a145fb9d61 | -11.10441 | -48.43653 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec080509-f250-329a-b25d-c05ffd90b7bb | -6.34864 | -44.08746 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f99c8940-02a6-338b-b5db-885e07309a15 | -10.40568 | -50.52473 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6656b148-55cc-39fd-a11b-c3e16b2d6cf8 | -6.85773 | -44.89405 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1e631a3-c6cd-309d-bc35-d8389b626ec4 | -11.47593 | -43.62352 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6029f70-a3c4-3d59-a5cb-8fcab914bf64 | -6.85742 | -44.89123 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59fdcc1f-70c0-3e26-a43d-13b3bb5561dc | -6.24686 | -43.42951 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d4f7fb8-d7d3-3c36-bcd2-0f9059ef4632 | -13.29431 | -43.75837 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 298d6d76-b246-32fb-a4b4-effc3b1a1509 | -7.46887 | -45.28555 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b70ecfb6-156e-328f-92cb-630b96fcc336 | -6.83654 | -45.61069 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b6143def-650f-3bae-8e8b-8197477486f3 | -12.01978 | -47.5798 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cc41669-0aef-3bff-8a67-9e784516766d | -9.02681 | -49.77584 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2439d7c5-84ef-3b08-9145-8cb8e0a33e08 | -6.18645 | -41.05833 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8607e5d0-5108-3523-abf5-b64cee11ea1c | -11.47693 | -43.68585 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c8cace1-339b-3af7-96c7-b607325c1a36 | -11.78869 | -50.57661 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed409e3a-a40a-3b94-9a63-d980c9db2980 | -6.97116 | -44.80604 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0af914bc-b2d6-3619-b0e2-f4e96466e363 | -6.25085 | -43.4302 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26048923-9b0d-3bb5-ba30-6fb7e90e408a | -8.73686 | -47.09277 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| dce65f0f-cde6-37cb-9f2d-e4769dcb5307 | -6.27437 | -43.38792 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b45d642-b729-353c-89d9-e2222412b030 | -7.29669 | -45.18322 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e40ad7dd-ea12-3e22-916a-2c349b93a1c1 | -6.39696 | -44.02945 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f97a232-0a06-39dc-9dc5-789b6fe6b9e1 | -9.07774 | -46.96342 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 140aad16-5a81-3f08-9086-c454f8cc42a8 | -11.49503 | -50.57403 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ad0e99e-8f19-39e1-bc1c-f14e8ca25235 | -6.2566 | -43.42046 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a52606d5-4b6e-3498-8c87-389a376bfd30 | -9.01958 | -49.7793 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 92886911-794e-35c7-bafa-8da378f50164 | -4.90189 | -49.9238 | 2025-09-11 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8b626df-7082-3c59-b567-39e0979901a8 | -11.14944 | -45.28614 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abc8fa6f-1d72-37f9-961a-a47de0a67cec | -11.48088 | -43.66259 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d710984b-b7d2-3395-8081-bea192c14391 | -10.16465 | -46.1787 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01945b1f-3eab-3172-bacd-61c45e29fca6 | -9.11921 | -46.97523 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aea66146-7c5a-315e-aaa1-20c76ab41d06 | -8.58087 | -45.58576 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd7fc970-4c53-319b-8bfd-5175d5b78bcc | -11.0343 | -47.61536 | 2025-09-11 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 481a5bc0-6fa8-3b18-be23-52e8ad6a76b4 | -11.41959 | -43.53973 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6db0acb-477a-3a21-9ede-0e235eb0ce61 | -11.49968 | -43.66576 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13c3324e-72ac-32d3-b161-0c3dc8237691 | -7.91944 | -44.84523 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3af6de0-254d-34d4-9f0d-5235faa43140 | -10.54611 | -49.89534 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed06b4ab-86bc-3230-b8b4-339fd3797187 | -6.68527 | -44.54008 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c369eed7-3a6b-3989-b051-661edfe3f34a | -8.52213 | -45.68682 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a79f03a9-c947-3593-928f-c8faa8d2244f | -13.16046 | -45.28989 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f4c7df5-9f99-386e-bf54-f0f2a15ff11c | -6.15985 | -45.81136 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd063f6a-48c2-3935-99ba-8c7d64a7961d | -6.73802 | -43.99027 | 2025-09-11 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fae5ced0-12a5-34ab-891c-b8024184ba98 | -10.52304 | -43.84497 | 2025-09-11 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bf988d2-eeda-374c-8a8d-8f6ddb69b070 | -11.9653 | -46.65166 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fe02a2c-87ab-3a1a-aceb-789a5478d4d7 | -5.404 | -45.93692 | 2025-09-11 03:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6a7f8d4-8709-3112-943c-9363451a7ad6 | -8.02248 | -49.04525 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48c61cd5-a900-325e-bcff-9c5103da3cba | -12.47125 | -47.48858 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 044f2219-8ee2-3fb9-9665-f92ae925ec3d | -6.83126 | -45.61553 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f4d3dbb6-9da4-3331-a81a-10661ec86967 | -12.12868 | -44.86742 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e062b4f1-9d4e-3237-a3c7-5c0bdc9d45f9 | -6.34634 | -45.19079 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f19c2358-bb9a-3394-a0a2-14b328f48df1 | -7.94279 | -44.88982 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2af7946-6a99-3e7b-8f43-c3535b5fa0c5 | -6.34996 | -44.07969 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb5bf015-30af-3fd1-9995-664659e04b6c | -7.39666 | -47.37864 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 332024f9-e7f4-3df9-b4eb-5ba979449e59 | -5.93752 | -45.71965 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1adb4e32-29ae-3ed6-b84a-e7f112fc9687 | -7.2196 | -45.31145 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c6af821-242e-3d62-b841-32dd1a17b659 | -8.93173 | -46.15258 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25919057-0f49-3996-a724-c10b6edf2062 | -6.99218 | -44.79626 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c45d0c82-2afa-3cb7-8482-131d8ad4f3f0 | -5.59366 | -48.11695 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd23f7e2-426e-32b2-aa9d-c5baa9dbb550 | -11.02683 | -44.64762 | 2025-09-11 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae63d11d-c64f-38a9-9f05-01a30bf5915b | -5.94469 | -45.71813 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cfd8be7-f032-311b-82bf-f6d2504870d8 | -6.41518 | -44.48796 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7dc3185a-beb9-3a13-b359-1ea11506f51a | -11.31408 | -50.75443 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 44b63371-0265-332d-9a26-7d19dd04f004 | -7.18921 | -44.96577 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fcacffc7-5602-33ad-a7d7-51f9728d5cc4 | -11.3132 | -50.75883 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d14bb2bd-a76d-365f-ba4d-822968f9b877 | -10.16918 | -46.17934 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e2b2e9c7-0824-30dd-ad0f-d1edb4efc06e | -9.45981 | -46.42394 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7df5bed5-eaec-3298-b3d1-0a47a4b3a5fe | -6.31376 | -43.42262 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23f05dde-e376-32da-b271-5b2c98a90ba9 | -6.16301 | -41.06364 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8a5d821c-2a15-34e7-9d94-c5a700138bf9 | -8.07263 | -50.18129 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f799157d-cf99-3e4c-8573-2237517bcbda | -11.77694 | -46.51484 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6d205a06-27fc-3c0a-95db-9b12c88ff61c | -7.66377 | -50.27149 | 2025-09-11 03:55:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9cef4969-eced-38b4-92ff-1828a9966fb3 | -11.48067 | -49.2485 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 697b243a-c1a2-380b-9607-77adedee3b2b | -9.07681 | -46.96865 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7bca20a3-8e49-300a-a4a6-094c74a366a8 | -5.72879 | -49.22021 | 2025-09-11 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f7c63e44-3029-3181-b589-66aa8cc660bd | -11.48638 | -43.63018 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0d194b57-01cb-3ea9-997a-90cf5a0c36b2 | -6.8267 | -45.61459 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ba31ca0-9fc0-3ad4-9cc8-fbe315c870e5 | -11.11869 | -48.3983 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6807609b-f5c1-3724-a6d3-25f62bc1c1b6 | -6.17643 | -41.06977 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7354ada0-b310-33a9-8d66-ab1977fc02f7 | -6.84928 | -47.88533 | 2025-09-11 03:55:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb02d375-ffdb-3652-bfd6-24062b862dae | -8.03011 | -48.65925 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b3d44cf-9543-3601-98f7-b94bed88e739 | -8.0391 | -48.6748 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f286782-2dff-34d3-97c0-227a028efe25 | -6.81815 | -44.8843 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d95346a-2f17-3568-b32a-e252098455cc | -6.30445 | -45.65982 | 2025-09-11 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a680e9a9-5cfd-385d-b2cb-78b8146f0031 | -6.34516 | -44.0827 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f668037-55f4-3813-b837-f738d99b0748 | -8.19471 | -50.11111 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23791d14-0393-383a-9470-2499abd4861c | -11.13262 | -48.35305 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44ee55dc-be56-3227-903f-df1cbc490462 | -7.65212 | -49.50112 | 2025-09-11 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1c9e678-5318-37ff-b681-e4533e04598c | -11.46115 | -43.59713 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a13be356-c80e-37c4-a737-7a2455fa7d44 | -8.58608 | -45.58205 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README27.md)
