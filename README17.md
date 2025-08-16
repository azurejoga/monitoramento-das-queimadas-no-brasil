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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb8a48d3-e61e-3c22-815c-5ce1bbb3f3a1 | -6.9302 | -59.5497 | 2025-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| cf6b658b-35ba-3b9a-80a8-da2afbffb5d6 | -12.8414 | -46.0538 | 2025-08-16 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 614ae2c5-315a-3abd-9b7f-785e79c48322 | -8.9706 | -61.7224 | 2025-08-16 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e781fcc5-61b3-305d-8565-99f9992df4c1 | -7.9148 | -61.7478 | 2025-08-16 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 4ccab745-aad1-3b3b-986c-276b2346663b | -8.9708 | -61.7033 | 2025-08-16 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fb9fd5e3-be43-3b35-9219-01d37d3c440d | -9.518 | -60.5268 | 2025-08-16 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 8de9b6ba-e2ee-3aa0-9c2a-f28f460dda04 | -13.4294 | -43.6733 | 2025-08-16 02:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 94789fac-dbfb-30b0-bd71-29d74d796d58 | -14.9632 | -54.7143 | 2025-08-16 02:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 68fb026c-4a24-3c49-86cd-cbb2c8accac6 | -6.5638 | -43.0357 | 2025-08-16 02:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 230.3 |
| d7e5c8ca-af37-3fec-9e83-3734404dc4df | -9.5179 | -60.5461 | 2025-08-16 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 09923bb1-e3cb-3ec9-a295-a0d9565d894f | -7.9149 | -61.7288 | 2025-08-16 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| ff61910a-9259-3263-8ea0-c7f89f71a5b6 | -14.9438 | -54.7166 | 2025-08-16 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 08b6d127-09f5-3dec-9d8e-c842e2548d0b | -8.9893 | -61.7024 | 2025-08-16 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 075407ae-bd73-37c5-848c-45324be280c8 | -8.9709 | -61.6842 | 2025-08-16 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 03d5f472-4f2d-3167-99dd-b0850c88ff82 | -14.9435 | -54.7374 | 2025-08-16 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| fa236afb-2f2d-388e-8b82-58da6d2edf30 | -9.4992 | -60.547 | 2025-08-16 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0ae7d458-4c05-349b-ab9f-e03f15a6fb23 | -6.9486 | -59.549 | 2025-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 8a876453-6bc6-3b62-885b-20ee546175fa | -6.5641 | -43.0122 | 2025-08-16 02:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5ce369a3-a2d7-3db1-8c33-fca325b16b93 | -7.9333 | -61.7471 | 2025-08-16 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 1ca1e26b-1c7a-3d23-9146-debc9d698253 | -7.9334 | -61.7281 | 2025-08-16 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| af4ea838-d2e9-3249-ab6a-882d984f715a | -14.6018 | -47.9243 | 2025-08-16 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d6e9f82a-f5de-3fe3-875e-7398354f6b4b | -6.9303 | -59.5305 | 2025-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 5a74fa23-b86f-3d44-ac00-70db5c15d3dc | -6.5638 | -43.0357 | 2025-08-16 02:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 7cc5c6ef-cabb-3884-a6a8-3ed406538b2f | -14.9628 | -54.7351 | 2025-08-16 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 282dcdd9-47a3-3cb9-88e9-4399c57f34e0 | -9.1708 | -59.6568 | 2025-08-16 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 88b508b7-1745-31f8-b201-afd88f1e8ffa | -9.4994 | -60.5278 | 2025-08-16 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 9a8f1b71-f239-3577-b8fb-d631f70f483a | -9.1709 | -59.6374 | 2025-08-16 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 54c9fe6d-3ae2-3b71-a10e-b6263e4f9716 | -6.545 | -43.0373 | 2025-08-16 02:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| bad31d52-11b3-373e-8a99-e308060bb827 | -6.5641 | -43.0122 | 2025-08-16 02:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b1b2661e-2e72-3481-90fa-0a85845dd325 | -14.5828 | -47.905 | 2025-08-16 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 79eee14e-b10f-3894-8c6e-d651b3e07655 | -14.9435 | -54.7374 | 2025-08-16 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 70ad64a9-89bd-3d95-a6c5-6cda2d853f9e | -14.6023 | -47.9018 | 2025-08-16 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 7ed2ee55-ea5b-3c1a-bca9-addd9d7c7a61 | -6.9487 | -59.5297 | 2025-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| bf568c6a-1617-3473-bcba-163e88a4534b | -7.9148 | -61.7478 | 2025-08-16 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 27ffc0df-9c05-34fa-949d-ee751dac55c3 | -8.9893 | -61.7024 | 2025-08-16 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 05dd3900-2cb2-30e9-883a-fea3fceb686b | -7.9149 | -61.7288 | 2025-08-16 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 014f0aab-8af7-3010-9f11-7b8bdb89554b | -8.9708 | -61.7033 | 2025-08-16 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c2b76feb-5daf-3123-b8e6-8ab8b31b1019 | -14.9632 | -54.7143 | 2025-08-16 02:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 76663fb7-9f5c-3264-b9d6-c3aaff2ad1d9 | -7.9333 | -61.7471 | 2025-08-16 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 4027ff53-8d28-3517-9867-6e3389a786c9 | -9.5179 | -60.5461 | 2025-08-16 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7c8d5b18-d9e3-353a-885b-9ca1e654efc0 | -9.4992 | -60.547 | 2025-08-16 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3aca2f78-6741-3e92-8298-c75613c1b567 | -14.9438 | -54.7166 | 2025-08-16 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 52dfc25c-b9ef-350b-8cd2-3babc5c8222b | -6.9302 | -59.5497 | 2025-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 77d576a9-5d57-3519-a5d9-6ee3f2e54cb3 | -8.9709 | -61.6842 | 2025-08-16 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 9087f2c2-b432-324b-90ec-992ea71029f6 | -9.518 | -60.5268 | 2025-08-16 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 51002725-d143-3353-8554-bf13e95b78be | -14.9441 | -54.6959 | 2025-08-16 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c1fd2413-8ee4-3c80-b134-c02131201508 | -6.9486 | -59.549 | 2025-08-16 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 4fd63c82-2b2d-3c8e-b606-8fec4347f8ea | -13.4294 | -43.6733 | 2025-08-16 02:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4601af1c-36cf-359f-9e0e-3beb9a85360f | -6.5641 | -43.0122 | 2025-08-16 03:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b97a6aec-42ec-372e-aac7-d19b24bafef9 | -14.9632 | -54.7143 | 2025-08-16 03:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 888f1df3-817d-3574-9822-f361c7e8d488 | -9.4994 | -60.5278 | 2025-08-16 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7c40ad48-8e3a-3d8a-b8e5-0cdcb042d50b | -7.0796 | -59.2351 | 2025-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5e2e2dd5-7a6f-3cb8-ad2f-5cbd75f61817 | -6.545 | -43.0373 | 2025-08-16 03:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 70853af6-c2a0-3ff4-9144-2adf08830c45 | -9.5179 | -60.5461 | 2025-08-16 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3e3d0af3-de18-39b6-bb3b-1b4534b7e072 | -9.518 | -60.5268 | 2025-08-16 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6737afb4-0f82-3523-a041-d4c2799ea544 | -14.9435 | -54.7374 | 2025-08-16 03:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 0eeb93a9-05ca-3b99-aafe-072509784fd7 | -7.9149 | -61.7288 | 2025-08-16 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| b23cfc6b-1476-3f23-a4f6-44e565c2b80f | -6.9487 | -59.5297 | 2025-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3f7e6b46-c517-33f0-b6e5-c05aeda9800f | -14.5828 | -47.905 | 2025-08-16 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 932f9069-1083-3469-8e00-6ba1757868da | -9.1709 | -59.6374 | 2025-08-16 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 2c01cfa8-37ee-3748-a595-7b4e9f2c8f8f | -8.9709 | -61.6842 | 2025-08-16 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 8ef3fca2-a48e-3bdf-8bd3-2e42ad9cfc0c | -8.9708 | -61.7033 | 2025-08-16 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9a0ab971-1ce2-3fbf-97b7-d4bd798f8b14 | -8.9893 | -61.7024 | 2025-08-16 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5d0be270-a88b-3806-830b-45717d4fb1af | -6.9486 | -59.549 | 2025-08-16 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| cc14ef5c-6449-3434-a38d-886d24b72896 | -14.9438 | -54.7166 | 2025-08-16 03:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b1c5bb27-dbbf-3f57-a970-f99ecbb51c00 | -14.9441 | -54.6959 | 2025-08-16 03:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| bde36a5c-c2dd-359d-a4f7-4c9e1a795495 | -7.9148 | -61.7478 | 2025-08-16 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5be49129-d2d6-3ac8-8003-fa0b1b0b2322 | -9.4992 | -60.547 | 2025-08-16 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 44147705-29a8-33a2-ad56-9e62fca53bc8 | -9.1708 | -59.6568 | 2025-08-16 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4c44fd68-249c-3c7f-8dc5-3137042f8dc7 | -14.9628 | -54.7351 | 2025-08-16 03:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 824209a2-01dc-3935-9c11-f5b101b9db4e | -6.5638 | -43.0357 | 2025-08-16 03:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 247218d7-ec6d-3781-a9d7-24f5920ad2c1 | -6.9486 | -59.549 | 2025-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e1dc7a95-aace-3b52-866a-b84bfcf85405 | -6.5641 | -43.0122 | 2025-08-16 03:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 292f78ac-d09f-34f9-bb29-bee696e6b5bc | -9.5179 | -60.5461 | 2025-08-16 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0d646386-c4aa-3c74-86f3-3a8b2a4c2544 | -8.9709 | -61.6842 | 2025-08-16 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 25af2d4e-6571-3670-b20e-73cc585b6af9 | -14.9628 | -54.7351 | 2025-08-16 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| aa6b0436-8f51-31d8-a35e-f8aab41d94ed | -7.0796 | -59.2351 | 2025-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 4a4f1b89-285d-3198-825e-3194985f9dba | -6.5638 | -43.0357 | 2025-08-16 03:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| fcc2ca68-390b-3d81-8afc-f2191ce73a8e | -9.4994 | -60.5278 | 2025-08-16 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a53080cb-5668-3d6f-9bce-867456ca7338 | -9.1709 | -59.6374 | 2025-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| aefaf4e1-1275-3e01-98f8-5a6bcf26cb9b | -14.9441 | -54.6959 | 2025-08-16 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d72779b2-d28d-3ac7-b1fc-2d0cb1614bde | -14.5828 | -47.905 | 2025-08-16 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| dd1797e7-fbed-3062-b8c5-2680fb6b4bdf | -6.545 | -43.0373 | 2025-08-16 03:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 64b2c065-76f4-3d01-8136-f5da735dd4e5 | -7.9149 | -61.7288 | 2025-08-16 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e91d8c23-02ec-3539-9012-fad4c6634160 | -9.1708 | -59.6568 | 2025-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 012a980d-4d71-326f-8078-15bb02b4afff | -9.518 | -60.5268 | 2025-08-16 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 599ba895-9bd2-38cd-b0f6-c728c7070e9b | -14.9438 | -54.7166 | 2025-08-16 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1804d5f3-b685-3f76-87de-1ed589954f31 | -8.9893 | -61.7024 | 2025-08-16 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a328869e-6f7d-316d-8b26-2135a7709098 | -9.4992 | -60.547 | 2025-08-16 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 654904b2-a1dd-35fb-b682-6d7d6bf87c9b | -7.9148 | -61.7478 | 2025-08-16 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 00a02985-fd19-3ad8-a797-ffd7dbbb272e | -8.9708 | -61.7033 | 2025-08-16 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 515447e9-213d-30cc-92d6-252feb3dd1f7 | -6.9487 | -59.5297 | 2025-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 82e43f2e-6217-33db-9ee7-fc8300fbd29d | -14.9435 | -54.7374 | 2025-08-16 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f358075e-604a-30e0-a94d-15c778c0711d | -6.9486 | -59.549 | 2025-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e7f7a0b2-846b-31a2-a56c-feacd6066388 | -9.518 | -60.5268 | 2025-08-16 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0583c004-53c9-3455-adbd-bbb622273444 | -8.9893 | -61.7024 | 2025-08-16 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| eb4712f6-a516-32c5-9701-8ec784083967 | -8.9708 | -61.7033 | 2025-08-16 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1f1e110e-7cbf-3422-bebd-e42100f12f10 | -9.1708 | -59.6568 | 2025-08-16 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 34967121-de50-3b25-95f9-0af38973bf54 | -9.1709 | -59.6374 | 2025-08-16 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 39e91651-7aea-3a9b-947d-3304da20cbd2 | -9.4992 | -60.547 | 2025-08-16 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |


[Clique aqui para ver as próximas entradas](README18.md)
