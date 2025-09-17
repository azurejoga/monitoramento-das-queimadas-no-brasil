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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b3916de-920a-39d9-a634-169317edfd33 | -11.6626 | -46.5884 | 2025-09-17 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c440f140-4d4b-3d13-8c2c-810420c98f85 | -3.3816 | -42.9689 | 2025-09-17 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| b0a9009f-9dc0-3fcb-9911-9e16d9454736 | -7.5412 | -44.7532 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 352.3 |
| 045096bf-8aa4-3afc-bec8-b88b203af5f4 | -8.4315 | -47.3853 | 2025-09-17 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0fa5d77d-72be-3a3d-be2e-a32d416e07d8 | -5.7673 | -43.9161 | 2025-09-17 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 2de81683-aa27-3ca0-a95c-b24424d20672 | -3.804 | -44.1302 | 2025-09-17 14:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| bcb2c781-3277-34e4-82bc-c5f8d32eec14 | -12.729 | -48.0068 | 2025-09-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 4196be12-7b51-3d1c-b08c-67ea016f8c5a | -8.5609 | -47.5712 | 2025-09-17 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c3380f9d-aa9d-3f0f-93a5-af1b21fdf8ee | -13.9648 | -44.9445 | 2025-09-17 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 50b71803-4806-3227-867d-7f7b573100c7 | -9.1425 | -44.8828 | 2025-09-17 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| d672b887-bc43-398e-bda2-30e0bab09642 | -12.1048 | -47.5592 | 2025-09-17 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| d4d0a15a-7273-3bc5-97ad-8c1ba74bac91 | -15.0549 | -42.4653 | 2025-09-17 14:30:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 47728f4d-10ca-3e63-a1e0-80665d6f736b | -12.7145 | -47.7419 | 2025-09-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 70e7e912-a2a2-34f5-9ca2-5701a4e1d6b6 | -5.7869 | -45.9379 | 2025-09-17 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 2a7629de-edd8-3304-b95f-20c43ee1945f | -5.8807 | -45.8865 | 2025-09-17 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 45cb5c83-1e58-3dab-9e94-28b879cede9e | -5.8058 | -45.9142 | 2025-09-17 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 8dbdab64-6add-3a79-9ff0-06ace58d3cc5 | -5.8809 | -45.8641 | 2025-09-17 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 64fddccd-627f-33e9-a2aa-a805fb8fb092 | -9.0478 | -44.8936 | 2025-09-17 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 497ddd08-6623-38fe-82c4-151a0c8a522a | -6.8734 | -43.9636 | 2025-09-17 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 80942054-6927-3623-af99-33789f3354b9 | -8.6699 | -46.3618 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 67457359-bee7-3515-a758-22456ce725d4 | -6.1739 | -44.5058 | 2025-09-17 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 09fb4dcd-7caa-345a-8441-65667e47ed60 | -9.4749 | -48.2479 | 2025-09-17 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 697b2fde-5c55-377c-923a-6ae7d79bd6ad | -10.6925 | -46.4904 | 2025-09-17 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 83580fc7-cf11-3580-a920-e6d0d03f4093 | -7.5996 | -44.5872 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 4adf8c76-fbb5-3e34-a80f-a3dccad1c765 | -12.124 | -47.5566 | 2025-09-17 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| c1e430bd-af57-34e4-85bb-dd0d54fa8d4a | -9.9418 | -45.9281 | 2025-09-17 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e3575d34-b879-361f-96b2-cbcf3d118f95 | -8.6313 | -46.4329 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a001eb01-b079-3fcb-a23b-505066c36a3d | -12.7482 | -48.0041 | 2025-09-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 2bfb1ae0-b6d0-3c15-a98c-391b0cdbb061 | -3.8004 | -41.6708 | 2025-09-17 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 276.5 |
| 7cdd2c3a-6ebc-3289-9a1d-983eafdfa09b | -7.45 | -46.1871 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 0eee9020-7ec6-33bc-96b3-52b921152ae9 | -7.4688 | -46.1854 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 4f300060-2caf-353f-9836-823032031bf8 | -6.1253 | -47.8137 | 2025-09-17 14:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7ace6887-c90c-319b-aaa3-040f498dcb71 | -5.8056 | -45.9366 | 2025-09-17 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 4a060df7-e9af-3327-93b4-b39971a14d3a | -12.0051 | -46.6763 | 2025-09-17 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 6ddba82c-be1a-3848-bf75-aa7b11649ae6 | -8.6885 | -46.3823 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 224.1 |
| c73e5c5b-e0ca-3799-9114-871fcd9ede4b | -8.9638 | -45.519 | 2025-09-17 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 01437e3f-f0fe-3788-bcac-8677ad783ba9 | -10.6334 | -44.2324 | 2025-09-17 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5c47fe34-f5c2-3441-9edd-5bd2f275072f | -8.4467 | -47.692 | 2025-09-17 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ca57f43e-fcae-31b6-a9ac-fec8274e4ae9 | -9.7316 | -47.4068 | 2025-09-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c998fa14-214d-3c9f-8c47-5c3c9f95f3d9 | -8.7836 | -47.8134 | 2025-09-17 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 763544ae-a33f-309e-a7fd-718b6e54337a | -3.8756 | -41.6188 | 2025-09-17 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 209.1 |
| 9d26725d-71fd-3873-97ba-1e06076a61b9 | -8.5421 | -47.573 | 2025-09-17 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 3f357329-be2d-3fc4-999e-b777efdd3efc | -9.1715 | -46.9346 | 2025-09-17 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 8b9504d6-65ea-35da-8ecd-7eab7138f3ee | -10.6731 | -46.5154 | 2025-09-17 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0839627e-89cc-31ec-b4aa-89f99c20ab55 | -6.3799 | -44.5122 | 2025-09-17 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 271.3 |
| 12c2854d-ca93-3f63-8ffd-68620c4c84f6 | -9.0661 | -44.9374 | 2025-09-17 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 79c99a3b-1ef6-3844-9b6c-ab8132123390 | -6.3073 | -42.3975 | 2025-09-17 14:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 561210cc-31c4-3078-8ede-7832a8a9967c | -8.5611 | -47.5492 | 2025-09-17 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e58639a7-673c-384f-b488-ca9c03da7afa | -12.6953 | -47.7446 | 2025-09-17 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 465705fb-4851-3111-9a68-77aae6eda059 | -8.917 | -46.2015 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 5b9b47bd-c396-3437-9394-fcc72f3ebfda | -5.8807 | -45.8865 | 2025-09-17 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e716b79e-3149-336f-89a0-4efba8561938 | -6.6129 | -45.584 | 2025-09-17 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 13628df4-0ac4-328c-8f1c-615dc9b85e3e | -8.6885 | -46.3823 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 1ee59d69-b365-34f7-a7eb-d78dd8cc563c | -11.6434 | -46.591 | 2025-09-17 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0867ffe2-c711-3d32-ad4d-078cfaba16ad | -10.6401 | -48.7332 | 2025-09-17 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 26ecd7b7-1fbe-3ac0-a19e-77d4b6e3f351 | -8.6702 | -46.3394 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 9b53eda9-ff86-3c3a-b0a6-eee2e5376615 | -7.8073 | -46.1323 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 759f94a7-b403-34c8-9ec8-4d8ee41b8309 | -7.4503 | -46.1647 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 4386e34e-f91d-3662-85ac-50d3bf5d93b9 | -9.7409 | -48.1106 | 2025-09-17 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 144c1df3-7d4d-39db-ae05-bece1ed84fab | -7.581 | -44.566 | 2025-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 1e789f5c-08ec-3eaf-96a9-4aba5cbc1da2 | -9.8124 | -48.4093 | 2025-09-17 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1ee7c226-6fa9-3d5a-9462-c8a6c31444af | -8.4467 | -47.692 | 2025-09-17 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| eb970f12-6777-3dfd-830b-dcdd75252cb7 | -9.1236 | -44.8849 | 2025-09-17 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 1429758d-39ba-3b96-a04c-97a5ef74bbf2 | -8.9536 | -46.2874 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 57397a4f-6ef7-3150-b36b-367048e204d4 | -8.631 | -46.4553 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 8fe150c6-d7ca-3c4a-9d06-a729e020e575 | -5.8809 | -45.8641 | 2025-09-17 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e7aa8f21-0b34-3206-ab32-48e0657b41f0 | -3.8002 | -41.6947 | 2025-09-17 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 219.8 |
| 097b45fd-4f8e-3473-a29d-0ed61ee2d5e5 | -7.8261 | -46.1306 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 21f93e7f-4a11-3294-b46e-dbe69d269b98 | -7.5998 | -44.5642 | 2025-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 9953bbcf-f8ef-3f3d-b9c9-0abc3bef5dd6 | -10.8994 | -45.4426 | 2025-09-17 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 46f829a3-d82c-358c-8226-96226aa82dd5 | -9.7412 | -48.0887 | 2025-09-17 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 415acfe0-03b4-32d0-a408-a8a78edfe884 | -8.9725 | -46.2854 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 85fc8d6f-2494-3583-afa2-5288866357b0 | -8.6499 | -46.4534 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 1c7611e6-72ed-33b3-a248-95a5619cd8ac | -8.0092 | -44.9589 | 2025-09-17 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| aa922cf0-5e45-3284-9a1e-fbdba929bb8e | -6.125 | -47.8573 | 2025-09-17 14:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2fa46f67-7bd3-3fc6-9cbb-d72340a4f1e4 | -7.6574 | -44.4667 | 2025-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.2 |
| f74e4220-eea5-36a6-b208-c2b990effa2a | -8.5797 | -47.5694 | 2025-09-17 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 9d130769-1010-3f35-9a00-56dc5d8f0665 | -7.8259 | -46.153 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| ae43ae98-3744-359e-9172-63db8f95fa63 | -8.6313 | -46.4329 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2d1ccd3b-ca05-3e68-9453-9e1dd154753a | -7.3363 | -44.5892 | 2025-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3ae3f205-c757-3eed-bf5f-902d0c110509 | -12.6729 | -45.8052 | 2025-09-17 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f4b925dd-eac3-3db5-94f5-97aa7f2a759d | -9.0851 | -44.9352 | 2025-09-17 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 20f5fe89-9c48-3993-bf2f-50b0088c5553 | -5.8058 | -45.9142 | 2025-09-17 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| c8f6075e-f92a-3fc0-9c87-fcce45461215 | -11.3636 | -47.3677 | 2025-09-17 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 0e41293c-8c26-373d-b21e-803e783aad86 | -5.9179 | -45.9063 | 2025-09-17 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e7736e73-18ad-3451-b3c6-4369ff29a332 | -5.7673 | -43.9161 | 2025-09-17 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d0c7c922-fd20-3bbe-92df-d7f3c1064f0b | -3.804 | -44.1302 | 2025-09-17 14:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| dba27700-e75f-3cd3-8bed-5ce748b47da2 | -7.45 | -46.1871 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 608f09f2-06d5-3ace-b811-efe17f7e7c41 | -9.5711 | -48.1066 | 2025-09-17 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 60dc810b-0ac6-3e67-b1ca-579411e181a8 | -6.2055 | -45.1187 | 2025-09-17 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 9d4eb8c1-f0d9-3c7d-b10d-cc290a887a7a | -8.4336 | -47.2085 | 2025-09-17 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 5b3b9fa9-655f-3280-b6c5-27aa787b9483 | -14.7719 | -60.2305 | 2025-09-17 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9cf7e13f-0ea8-3a10-a8cb-84755b0d0195 | -3.8756 | -41.6188 | 2025-09-17 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 156.3 |
| 1a7d2dc6-0bac-3904-a40b-d2e5a7db399a | -6.1868 | -45.1201 | 2025-09-17 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 994159fb-f137-3ed6-9c34-5283f2ff604e | -8.9167 | -46.224 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 9fa905a5-329b-3162-bfda-7e473bb933ac | -6.1252 | -47.8355 | 2025-09-17 14:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 23f99da2-56a5-32f9-97ec-1b2fcb9bff83 | -13.9453 | -44.9479 | 2025-09-17 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 84319dcd-04a6-356f-8256-e475af5c14c7 | -8.9638 | -45.519 | 2025-09-17 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e7968b3e-5397-3c07-9ec3-8eadc52b909d | -8.5609 | -47.5712 | 2025-09-17 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| ddcf837b-b27e-3b2d-b230-ad8c48a443fe | -10.9643 | -47.3514 | 2025-09-17 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |


[Clique aqui para ver as próximas entradas](README70.md)
