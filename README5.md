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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fa9f104-caa3-321a-961c-9fad75958877 | -22.39671 | -47.2408 | 2025-11-25 03:51:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0663798-1e17-37e1-9c5d-b5835114489d | -19.33618 | -54.35278 | 2025-11-25 03:51:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c20bf36b-c6fb-37ae-9b18-549dbdee8017 | -22.47639 | -49.13558 | 2025-11-25 03:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2465855-273a-3922-bf78-7c2529fdd8c8 | -28.71303 | -52.1846 | 2025-11-25 03:55:00 | NOAA-21 | NOVA ALVORADA | RIO GRANDE DO SUL | Brasil | 4312757 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b9da364-3914-338f-8c58-3002346de930 | -28.71219 | -52.18818 | 2025-11-25 03:55:00 | NOAA-21 | NOVA ALVORADA | RIO GRANDE DO SUL | Brasil | 4312757 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2d21d73d-324d-3c24-b5e3-881e4886dd24 | -3.85029 | -50.21093 | 2025-11-25 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1c90ad2-09e4-3194-ae54-aa8de4f9d372 | -3.21082 | -46.8296 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 20542261-e2c4-3af1-9295-e8d226c00149 | -3.65451 | -42.77824 | 2025-11-25 04:16:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edc36b30-6126-3dcd-9dc9-dc9b5f801af5 | -4.40353 | -44.82364 | 2025-11-25 04:16:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20e13454-789f-340f-b2d7-9680685920e2 | -1.48697 | -47.81279 | 2025-11-25 04:16:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdeb8e68-57d2-383e-95f1-8b3b4efbfc39 | -2.88088 | -51.80666 | 2025-11-25 04:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b0a78ba-0c9a-3e97-9614-164c44fe1900 | -4.13413 | -42.91056 | 2025-11-25 04:16:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6db74571-a7c7-3384-8aac-7f07af565b30 | -4.18474 | -43.10658 | 2025-11-25 04:16:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d43e8aae-eb54-39c8-88b1-864ba6b96cac | -4.16995 | -41.6116 | 2025-11-25 04:16:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b6d644ba-aa43-381a-af73-1aff48246536 | -3.21003 | -46.83447 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 156788d7-ef82-3d11-a4f0-6f61f22e6e10 | -4.55368 | -43.29667 | 2025-11-25 04:16:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d7b72ef3-3fd1-3c12-8246-244b0dd1ff04 | -3.08127 | -44.48816 | 2025-11-25 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fcd1cfa-3a31-3c65-bc32-54ff66842830 | -3.35968 | -45.57025 | 2025-11-25 04:16:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d646212c-b207-3b20-815f-46f05892662e | -3.56593 | -41.6044 | 2025-11-25 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3662d39-648e-308b-accd-c048daf2aa84 | -2.87481 | -51.80929 | 2025-11-25 04:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fd168a5-c253-3b44-9a52-8f040d39f36e | -5.05586 | -37.92641 | 2025-11-25 04:16:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad87e2ef-d21a-3c72-8829-45cd3108e56d | -3.17315 | -48.03096 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48435b46-26d9-3a58-b82d-c82e134469ed | -3.82407 | -43.9921 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ee12122-1e6d-3db1-a35b-a123db674e11 | -4.80046 | -38.69847 | 2025-11-25 04:16:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 89dd59b4-6652-367d-ae54-25a5b6988367 | -2.847 | -46.77706 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a26e6a19-0117-317d-a179-3d5c3dcb9a17 | -3.49623 | -41.00957 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5561268d-81df-31e6-bd5c-8f723d309b7e | -4.06608 | -44.6019 | 2025-11-25 04:16:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0ca342e-43b5-3e1d-af18-f68537758fa2 | -4.44661 | -44.29434 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7ac77e9-b6d9-3282-8d50-7d60a8621e22 | -3.58874 | -40.97575 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bac1dd23-c5a6-313e-ba57-511c07cd3520 | -3.41134 | -39.19773 | 2025-11-25 04:16:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf9439ba-eb51-3b1f-83e9-a69660b7080a | -4.33589 | -44.33267 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fa1d409-9960-3b73-81dc-e36571ed93f4 | -3.99404 | -43.43316 | 2025-11-25 04:16:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25aeef2f-7941-3b63-8b94-f3e4810c6b40 | -4.7322 | -44.73501 | 2025-11-25 04:16:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257f3256-e8c8-36e7-abd3-6ecc44828786 | -4.81798 | -43.83038 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5723e067-46aa-3ec7-bebe-cf597165ebc6 | -4.82525 | -43.8279 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 110ad5b1-3ccf-3a7c-896a-8f45ea3947ef | -3.81742 | -48.87399 | 2025-11-25 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6c31438-07ea-39e5-986c-0a49d1d6104b | -4.13884 | -42.36966 | 2025-11-25 04:16:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2830a4d0-bd17-31e6-a6ff-382bdaaff48a | -3.82483 | -40.69456 | 2025-11-25 04:16:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30b16415-5618-323f-aa66-1b559548e71e | -4.00739 | -43.26338 | 2025-11-25 04:16:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0ec22e5-5c3c-380d-81c7-79a6d121822f | -3.09451 | -44.49413 | 2025-11-25 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 26163a92-0d4b-3ddf-b1d1-a6d276119086 | -4.05098 | -42.51849 | 2025-11-25 04:16:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd5eabaf-a119-311f-adf2-4480a56a85fb | -4.44777 | -44.28702 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50e7c851-8721-358e-95b8-c4393a38c075 | -4.59158 | -44.04315 | 2025-11-25 04:16:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96388a7f-6461-3ecd-a7d5-ae54eb15a19b | -3.83026 | -43.99677 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3b5442f-f6d0-306e-8ef8-fa9c161873dc | -2.4339 | -50.25916 | 2025-11-25 04:16:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f313dc98-849b-354c-adab-dfbf18d32cc6 | -2.98324 | -52.62628 | 2025-11-25 04:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1183524-e6ea-3bc7-b4bf-9b3cce2719d9 | -4.73159 | -44.73876 | 2025-11-25 04:16:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c316661-f0b9-3313-9713-38b7a5380b24 | -4.82581 | -43.82436 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 420d0c44-03cd-3851-9c3c-640c91cca34e | -3.59155 | -40.97998 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19ddec48-913e-324e-becc-08730e9e68db | -3.64929 | -43.93164 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ab75ff-7e5b-33ac-9b63-5ad96884e035 | -1.14632 | -48.09464 | 2025-11-25 04:16:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e0091b-d408-38ff-b59f-455e29becacf | -1.64601 | -52.057 | 2025-11-25 04:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42fca86e-ffcd-317d-ba78-4da27754928d | -3.12453 | -44.37192 | 2025-11-25 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 221ad4fa-a538-3db0-96e2-a51b89e9474f | -1.49123 | -47.81347 | 2025-11-25 04:16:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e26fcb75-8c4d-393f-90ad-1922be0f38ac | -5.00364 | -41.97144 | 2025-11-25 04:16:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 36ebf74c-f00e-3de6-bbad-fada457ca578 | -4.17533 | -43.82735 | 2025-11-25 04:16:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1237039e-ada8-366f-bbea-1401ba068154 | -4.46743 | -40.7607 | 2025-11-25 04:16:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9f02a4c-6634-34a5-b6f4-8cb4cb8609da | -1.68078 | -52.09506 | 2025-11-25 04:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c6def8c-be76-3dff-a08c-c495517f3879 | -4.81854 | -43.82684 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0746e61f-b2a7-33f7-99a1-875f4e9562fa | -3.84545 | -50.21014 | 2025-11-25 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 576ee9e9-38c4-3f7a-ab8f-6471ae59edeb | -1.67677 | -52.0951 | 2025-11-25 04:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 984143fd-f73f-3ffe-927b-852c4dfb3a89 | -4.49436 | -44.26056 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67a6b3c1-8271-3d4c-8c76-81f3c686f24c | -4.75054 | -44.45002 | 2025-11-25 04:16:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6902229-8366-3a2f-8ee3-759c8cebc52c | -3.81378 | -43.35479 | 2025-11-25 04:16:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cd077de-7fa8-3d54-933f-8f22bc50cbd9 | -4.1383 | -42.37312 | 2025-11-25 04:16:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65fe9b51-6138-3783-8060-0a650232124b | -3.41998 | -45.45569 | 2025-11-25 04:16:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfeca87a-a367-33c4-ab87-96183c920e1c | -5.00808 | -41.96496 | 2025-11-25 04:16:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2cd837ad-ead9-3817-923a-c761ecdb9d80 | -1.96612 | -54.70707 | 2025-11-25 04:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cce62e30-49fa-3e1a-8749-b206eacbd395 | -4.04821 | -42.51452 | 2025-11-25 04:16:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 031e18f2-66f4-3e33-aa90-a7a8d80f27b4 | -2.92923 | -48.23289 | 2025-11-25 04:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ba0b353-e756-3b97-b607-e3877d4ee6ba | -4.58987 | -44.0539 | 2025-11-25 04:16:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a28fa3bc-b310-3497-908f-ff6e948d394e | -3.02371 | -51.03436 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cfa41e3-efad-3f0b-b6dc-110b03e5ee06 | -3.09391 | -44.4979 | 2025-11-25 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| edcaf3da-64c0-3c70-8bc6-3b0324545efc | -4.58816 | -44.06467 | 2025-11-25 04:16:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bf4a2aa-1289-3084-8be6-9325c06cc0d3 | -2.98905 | -52.62705 | 2025-11-25 04:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db79e2bb-93e1-3061-8cc0-d030484fd35f | -3.02346 | -51.03755 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b978d05-00c9-3a30-b3ed-f01096db7023 | -4.33794 | -44.34066 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5a20abb-188d-3001-9b85-13af776e0835 | -1.969 | -54.71406 | 2025-11-25 04:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c237a38-d61a-3dba-a77d-6674698a7a8a | -4.04692 | -43.42353 | 2025-11-25 04:16:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03651576-fbd9-3b51-88ed-3f26c9e030e3 | -3.20613 | -46.83385 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb51a74b-654d-304c-8b63-a935aacdceaa | -4.81519 | -43.82631 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a908a6c3-c4e5-388e-b06a-96676b09222d | -4.57312 | -45.4508 | 2025-11-25 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4694e8e4-4924-3de3-9705-0c74627f448e | -3.38923 | -47.185 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0dda4ec5-7a53-3d0f-8861-2d9c82a66cb5 | -3.7195 | -43.22187 | 2025-11-25 04:16:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a62ca6c7-a0a9-3dc0-b5a2-0a9663a5ad19 | -4.33814 | -44.34052 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78267059-c867-3ceb-ad80-8f54584d158d | -4.82916 | -43.82488 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 707c4234-2bba-3dd7-8328-3baa9baaea19 | -4.35053 | -44.32766 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd7ef72c-2dc6-3627-81a4-93d6df8963cc | -3.59211 | -40.97641 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f333467e-7f10-3cc3-8637-d6a71060aae1 | -4.05044 | -42.52194 | 2025-11-25 04:16:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0993be58-ccde-3a97-a262-243449abfc46 | -4.67348 | -45.00877 | 2025-11-25 04:16:00 | NPP-375D | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 743654b0-5e44-3361-b210-38bc54e49e09 | -3.12797 | -44.37246 | 2025-11-25 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c99cd60-8aae-3dd7-8ea5-fb3218db7fb3 | -2.95753 | -41.553 | 2025-11-25 04:16:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 491d86c2-c954-3e27-ba56-6f8d623107e8 | -3.27394 | -46.01211 | 2025-11-25 04:16:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1761961f-93b9-3dff-a15c-c891c0ddd05f | -5.63054 | -35.47913 | 2025-11-25 04:16:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 47032167-7636-33ac-afec-e69a5a8315d1 | -4.59687 | -44.88029 | 2025-11-25 04:16:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b9e7777-8692-3149-ad59-23f20c8471fc | -3.02971 | -51.03222 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80568c25-584c-3621-9e20-c0e84185049b | -2.43297 | -50.26479 | 2025-11-25 04:16:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18ce7661-c8b5-37ad-a48b-73f2b5cf38a8 | -3.39238 | -47.19072 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3c5ad30-477d-3b7c-b78e-ec75508c98bb | -3.822 | -40.69024 | 2025-11-25 04:16:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37b506cb-d304-3e71-bf37-4de6e45dbf27 | -3.17737 | -48.03163 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
