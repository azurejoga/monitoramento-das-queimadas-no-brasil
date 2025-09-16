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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c02d7940-b874-3447-b456-1e1ae5332cae | -8.651 | -46.3637 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 9258ae59-5fc2-33b6-977b-953f26bee89d | -12.6721 | -47.9703 | 2025-09-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| cb3de057-f256-3696-be09-3204c7a59400 | -11.4477 | -43.5514 | 2025-09-16 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 09e52dc7-6e64-38c0-87c3-cd48d3d33b41 | -6.1688 | -41.2357 | 2025-09-16 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| 9e9fc226-8088-30ca-811f-01d62e1da943 | -7.6927 | -44.6699 | 2025-09-16 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 46b02dd9-8940-343f-a9b9-4f919ad8803e | -14.3295 | -46.0626 | 2025-09-16 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| afe35757-a067-382f-8825-370f4e235697 | -12.6352 | -45.7652 | 2025-09-16 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 324.3 |
| d07eba30-28a4-3c55-a993-a678aa9c15a6 | -12.1152 | -44.8072 | 2025-09-16 14:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 08be7b53-d0f8-332c-ada6-a480604f8e34 | -8.5939 | -46.4143 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| da08f9bd-f70b-382a-a754-46cc68926ec1 | -6.1881 | -41.1855 | 2025-09-16 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 192.8 |
| 8de4151e-9a11-33e2-a176-cdd2ad167bef | -7.6949 | -44.486 | 2025-09-16 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 5407ae80-888d-33b6-980b-0e78faea0fa2 | -9.7445 | -47.8468 | 2025-09-16 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3367a9d1-1c64-3ce2-8fdf-7c9a9cc00809 | -13.9458 | -44.9245 | 2025-09-16 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 3a18fd61-cda7-3dda-ae03-890dbfcb09e5 | -5.8086 | -43.4956 | 2025-09-16 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 7833626e-ad44-398d-8401-cf98d9566800 | -11.1299 | -45.3426 | 2025-09-16 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 57c25d27-e6c6-3787-91a3-6d7b61a0ff7b | -13.9453 | -44.9479 | 2025-09-16 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e0e1e8fe-3e19-3ea5-a9ac-63d50ef6df8f | -10.7392 | -44.7515 | 2025-09-16 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 2a535575-f715-3564-adcf-68c7a4f5fea2 | -5.7673 | -43.9161 | 2025-09-16 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e6b73f7a-82f0-3895-a534-a3112ab0d5c4 | -10.08 | -48.1836 | 2025-09-16 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 715c4b17-f26e-3b4b-94d2-3477e96dd7a8 | -8.6319 | -46.3881 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 1bac6432-b283-3b53-b634-64d9ffe27acb | -9.7129 | -47.3867 | 2025-09-16 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 555442ec-fb8a-3476-8bd0-b98965e866d1 | -6.3372 | -43.1492 | 2025-09-16 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 48f4286e-1ecc-354c-adb9-9bae205e6f37 | -7.8261 | -46.1306 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 241fc5e4-b489-3de4-b303-deb2644560d2 | -5.7873 | -45.8931 | 2025-09-16 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f64aedff-424e-3d38-89c7-72c4424de0c0 | -5.7856 | -43.9609 | 2025-09-16 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 63294805-2ef8-3f3c-b2af-2c3de8781493 | -6.1693 | -41.1872 | 2025-09-16 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 141.9 |
| fed26fd3-bc38-3335-aa3e-cc412121c4e1 | -10.7302 | -46.5082 | 2025-09-16 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 4890ea33-42a9-3eff-b38a-d9a5ca9b9ebd | -5.786 | -43.9147 | 2025-09-16 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| bfac2060-c0fe-39f5-8a29-55037499a493 | -14.329 | -46.0857 | 2025-09-16 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 102.7 |
| b327a60f-ebca-3688-a3aa-cdcac7e9f5f0 | -8.9731 | -46.2405 | 2025-09-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| ac22e860-10ed-3cb9-bbb2-43e33c325f21 | -8.9571 | -46.0172 | 2025-09-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 183bf45a-2589-36bc-bd5d-eb5488bbdd1b | -7.9819 | -45.6657 | 2025-09-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| fda2002d-1922-38d0-9de1-c15e09f2c821 | -3.4179 | -43.154 | 2025-09-16 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2ba7f0df-3017-331d-9d7d-de84f4d6d28b | -6.6696 | -45.5344 | 2025-09-16 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 0217d136-839c-3763-ba9d-01b82bee7a9c | -12.6717 | -47.9926 | 2025-09-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 8147b0cf-d5be-32da-b52c-5d8aa642fa8d | -10.0728 | -48.7086 | 2025-09-16 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 3cecc9e6-77ec-3551-bd7c-58ea696b8739 | -5.9942 | -43.6902 | 2025-09-16 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e4bbfd30-f35c-37ad-97e1-82ea7550f70b | -7.2771 | -46.5814 | 2025-09-16 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 6b467365-b426-3d4a-b652-d0afb002e69a | -8.7677 | -46.0823 | 2025-09-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| e69e1a58-d328-3db6-a333-25b7879d956a | -6.337 | -43.1727 | 2025-09-16 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 143.9 |
| c56e84b2-04b6-3bb3-b810-972fbbe4d294 | -6.356 | -43.1476 | 2025-09-16 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 278.7 |
| bc0e3ed4-56b4-3de5-b1ee-d6b18fd6a762 | -13.7862 | -54.9512 | 2025-09-16 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 5cfc1fb1-34bc-3c6e-bb65-480e6e1ba88f | -7.0592 | -44.1547 | 2025-09-16 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 64b064c7-9547-3d27-b242-095be5692153 | -11.7151 | -46.8739 | 2025-09-16 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| a48202f5-fa98-3f91-947c-21312a0db87f | -6.3558 | -43.1711 | 2025-09-16 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 194.8 |
| af78282f-64ac-30f2-9cb7-df4f89e33c93 | -6.6698 | -45.5118 | 2025-09-16 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d1913fde-e5a0-3ef9-9606-0f03aec8894e | -7.1318 | -47.9801 | 2025-09-16 14:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 99b13e6b-548c-3b9a-ba94-6e4f241af8b2 | -8.5947 | -46.3471 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 72a9b406-f7e8-31a2-a622-8ed616ebd46c | -9.1709 | -46.9792 | 2025-09-16 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 48585307-9ee9-3b31-b8c8-ecbe258d537d | -7.078 | -44.153 | 2025-09-16 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6720c74b-efd5-3796-b3f5-8536daa042df | -11.7342 | -46.8713 | 2025-09-16 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2c823a39-1293-3e3a-a3b1-19b48135cf2e | -7.6738 | -44.6717 | 2025-09-16 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| bd11f159-9828-37db-8624-7805d17fce78 | -11.1896 | -51.419 | 2025-09-16 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 26962260-55d7-39db-9d1e-b500ffece6ca | -8.6124 | -46.4348 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 9b04e9b6-f547-346d-8789-d245c0d755b6 | -13.8889 | -44.8644 | 2025-09-16 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 51ff9931-f8d4-31b7-9c56-4fd7bce3b519 | -10.0611 | -48.1856 | 2025-09-16 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| fbd649d7-ae45-37f0-b684-533ef40b4eaf | -8.001 | -45.6412 | 2025-09-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 27803c46-fb2f-3c08-b204-ede87015174b | -10.7112 | -46.5106 | 2025-09-16 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 4ea61507-b72f-3bbe-91d7-fddb3cbb985a | -12.0647 | -46.555 | 2025-09-16 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 30e390b8-6b3c-3222-a0fe-b5acac0bd00e | -7.2581 | -46.6052 | 2025-09-16 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| dd65c11e-9240-3890-98f4-26edcd02d667 | -9.7325 | -47.3403 | 2025-09-16 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 9ef999ee-c5ec-3d78-8db8-06b86936edc8 | -8.0007 | -45.6638 | 2025-09-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 0b6442fd-cf94-3853-b45c-742966f9c33a | -6.16 | -46.0007 | 2025-09-16 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9ba4c795-5361-3aad-8642-238a88f0590b | -10.9004 | -47.8027 | 2025-09-16 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 4d2dec78-9dc5-3bea-85f8-17e4a52ec987 | -11.4665 | -43.5722 | 2025-09-16 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f99ebf26-68f9-3a3a-9925-e8c1b49b2af7 | -12.1147 | -44.8304 | 2025-09-16 14:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a42c5d11-b7ec-3b36-95ad-728d61acdf04 | -8.9259 | -45.5231 | 2025-09-16 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| cb7df35b-1cba-3f77-818c-da86b9f74461 | -6.7071 | -45.5313 | 2025-09-16 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| d27abe7a-8eb1-3fc0-81c0-35853b5cd546 | -8.0196 | -45.662 | 2025-09-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 220.1 |
| d31cd497-7292-3dfc-a1a9-cc3793b5a1fa | -10.1189 | -45.4977 | 2025-09-16 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| e5720c24-02a2-3d9b-9e64-d44e057b54da | -4.0148 | -43.2408 | 2025-09-16 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c8e0a9d6-c848-3672-a9ab-d6e4e27b992a | -7.4503 | -46.1647 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9aa78bb8-1a3d-3d7e-b298-aedf8d2d638b | -10.9671 | -47.1729 | 2025-09-16 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c7b9c971-fce3-31c3-9962-48ea2fef575d | -11.4473 | -43.5751 | 2025-09-16 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ef6fce4a-e83a-3cc8-a138-1140cc69f228 | -11.9164 | -48.5574 | 2025-09-16 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| ee6ebb47-b431-3223-80e3-1578878e1a53 | -10.7591 | -44.7026 | 2025-09-16 14:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 0ec6ab3a-fe8a-3900-85f7-a1a4b04fac26 | -8.3323 | -44.7426 | 2025-09-16 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7a35703f-0a52-3cb1-92d6-75580264a624 | -8.6319 | -46.3881 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 0a291f6d-9265-3b5e-b48c-95a7669af04e | -10.9671 | -47.1729 | 2025-09-16 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 858cd931-0cc7-36b4-b971-a7d4e0c2b800 | -8.7866 | -46.0804 | 2025-09-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ae4a1504-436c-33b2-a08a-36b68e669fbc | -5.7673 | -43.9161 | 2025-09-16 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 88e941dd-0b48-36aa-9c54-6ef28a6ed1b9 | -9.7129 | -47.3867 | 2025-09-16 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6eeb0fe2-47ed-3798-a64d-cb3fc4b950ff | -8.9702 | -45.0398 | 2025-09-16 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 4a9ff360-a193-35dd-9ad4-d509787d470e | -7.9819 | -45.6657 | 2025-09-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 494ae9a5-1172-3eb8-ab6e-0807a67fbb5c | -6.3372 | -43.1492 | 2025-09-16 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 4eafe2b2-e8c5-341c-969d-feeaac9152eb | -8.0007 | -45.6638 | 2025-09-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| f80b7c58-3640-3504-97c7-7ab75d2d50d5 | -6.1693 | -41.1872 | 2025-09-16 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| d62bf4c3-0f03-37eb-a550-a43e6f85cee5 | -8.6699 | -46.3618 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 7e9e18b2-79ab-33d6-a46b-3d1e1e53c9f1 | -9.7325 | -47.3403 | 2025-09-16 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a651aab1-779e-39bf-8e0e-8b14b12550fa | -6.7071 | -45.5313 | 2025-09-16 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 255ea9a0-be7e-3678-8dca-97fac33ca2c1 | -8.6887 | -46.3599 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e8ded870-aaa8-3058-b51b-d7b172b55a42 | -7.676 | -44.4879 | 2025-09-16 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| da12aca8-739b-353c-a2fe-224fa7877e40 | -6.6698 | -45.5118 | 2025-09-16 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d5f33e66-4bb5-3674-aaac-cb3232b375bb | -9.7445 | -47.8468 | 2025-09-16 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| dd041950-5ea9-3793-a1a7-b04ed0664dbf | -11.1299 | -45.3426 | 2025-09-16 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bee7d90f-049b-3be4-8cc8-8949816b9f8b | -7.1505 | -47.9786 | 2025-09-16 14:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| ea9f29c0-572c-3456-a598-44db7ec7641c | -6.337 | -43.1727 | 2025-09-16 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 51735d39-eee4-3dc8-9e73-b0f3a1ab9108 | -8.6127 | -46.4124 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 8d5c8572-8149-30b2-898e-fd0690492bc9 | -8.9731 | -46.2405 | 2025-09-16 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 81d10399-1c30-32f2-a533-3ce35add7260 | -13.7862 | -54.9512 | 2025-09-16 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 234.4 |


[Clique aqui para ver as próximas entradas](README101.md)
