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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c388e06-645d-3913-ae99-520f70f84e55 | -5.33577 | -49.54526 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b530d351-3716-3f74-8dab-a2417844e3ef | -5.33278 | -49.53845 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5c5874c-9ce5-3d45-824b-728007e59070 | -5.33168 | -49.53955 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46e44764-6d72-339c-9306-0cf183acf613 | -6.40366 | -51.06385 | 2024-11-03 05:10:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f4835160-8d1f-348f-a3b1-487e44cdc2b3 | -5.33648 | -49.54022 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c28ba2d8-2b94-3de2-8e5e-2ab79653b78a | -5.33203 | -49.54353 | 2024-11-03 05:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87aa95b0-de9a-3e6f-b5cb-969a94319716 | -15.47759 | -58.61815 | 2024-11-03 05:12:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 294cffe7-a700-3c19-80be-983cf6a76d52 | -15.24962 | -59.00155 | 2024-11-03 05:12:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e86ea9f-7df5-32a4-b780-bfbdee17ac57 | -15.1786 | -60.33597 | 2024-11-03 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| faf79244-32d2-3e6e-8893-0a407df5915c | -15.17801 | -60.33962 | 2024-11-03 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 03e43a76-5243-33f8-a18c-42204585d9fe | -15.17524 | -60.3354 | 2024-11-03 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7385d558-2209-35e7-8e13-a40a8f81b6dd | -15.17465 | -60.33905 | 2024-11-03 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 478ea6bd-4ff4-3875-b715-31a4f409a519 | -13.28154 | -61.33838 | 2024-11-03 05:12:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1645671e-1fe4-31db-bdba-1aebc38ce42d | -13.28087 | -61.34235 | 2024-11-03 05:12:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22ce5ba5-72f0-3f2e-b13d-20dd4e508b06 | -13.19888 | -61.27215 | 2024-11-03 05:12:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 087336f6-7409-34fb-9451-ca2c8a5f01c1 | -11.89213 | -64.07729 | 2024-11-03 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8325b43-8803-3718-851b-b187dcd79be0 | -11.88866 | -64.07268 | 2024-11-03 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e613a892-e562-30b8-afce-74536a4b5a6a | -11.88799 | -64.07651 | 2024-11-03 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dc32a49-5cd2-3cc9-901c-2bb4db652f92 | -11.82549 | -63.4833 | 2024-11-03 05:12:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e88d299-d378-31e9-8714-e458ff714dfc | -11.82487 | -63.48682 | 2024-11-03 05:12:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c964eae-1bcb-30f1-8397-c8224626681a | -11.8215 | -63.48254 | 2024-11-03 05:12:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f3c3c4d-c573-3e43-8766-a9683165f22b | -11.82087 | -63.48606 | 2024-11-03 05:12:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71ea4a76-719c-3dea-a8a2-0b175aebec4e | -11.77992 | -64.0259 | 2024-11-03 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87b211a4-12af-33f6-a1c3-9d9842ec041e | -17.4802 | -57.48234 | 2024-11-03 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6a5dc860-6af0-3def-9c5d-b93c25f7ed97 | -16.24703 | -58.24131 | 2024-11-03 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d8538f99-77dd-3e36-940d-b27a8542d2ae | -16.24586 | -58.24164 | 2024-11-03 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6720eba3-ec86-3e0c-a03b-b1272fb7f07e | -1.0441 | -47.9272 | 2024-11-03 05:15:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 8f95da7d-fdbc-36f2-8e4f-ee8175a1682b | -1.2755 | -53.4138 | 2024-11-03 05:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ccd03302-76e8-3c2f-b401-d7f3d6ee871b | -1.2755 | -53.3936 | 2024-11-03 05:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8eff3e05-c02c-32d9-ab67-3965aba8dcfe | -1.2756 | -53.3734 | 2024-11-03 05:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 03c454d1-0a1b-3f97-9734-60925d3740c0 | -2.5796 | -53.3927 | 2024-11-03 05:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a1fce824-af5e-3c8a-be31-3edb8959d12f | -2.5797 | -53.3724 | 2024-11-03 05:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| fa8b21dc-a16b-39a2-9374-797f89663f31 | -2.7419 | -54.4353 | 2024-11-03 05:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 503ff09a-9346-3de8-81f6-b97dc105bc3e | -2.7419 | -54.4153 | 2024-11-03 05:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 42bd09a2-a57a-3d3f-bdcc-03f3ec7251a0 | -2.7602 | -54.4349 | 2024-11-03 05:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c199713f-1a57-3de3-a47b-551cf24ee7c1 | -2.7603 | -54.4149 | 2024-11-03 05:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| de2daef7-251a-3b8b-9812-915d11fead5b | -2.7876 | -51.6099 | 2024-11-03 05:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 7299c76a-6a7a-3844-8cbd-472de7487fd2 | -3.055 | -54.1474 | 2024-11-03 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| be31b155-f139-3b11-859e-adcc49ffd002 | -3.0734 | -54.167 | 2024-11-03 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5f9430d4-c03a-32b6-b18c-d712f208716d | -3.0734 | -54.147 | 2024-11-03 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fd57a33d-c196-3598-ab8a-9b5b61cb8f66 | -3.0875 | -50.2901 | 2024-11-03 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3c299774-9436-34d8-969f-90369dd59700 | -3.1059 | -50.3105 | 2024-11-03 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9b03d524-a6e7-3b4a-bd80-cacd4791b287 | -3.106 | -50.2896 | 2024-11-03 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| d010c493-9665-3cae-bd09-65ce01ec7c7f | -3.1061 | -50.2686 | 2024-11-03 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 800ecff7-bf4b-3b03-9cde-375df1c7497b | -3.1245 | -50.289 | 2024-11-03 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b85fc4ce-b643-3c38-a831-0b8288cd71ea | -3.1501 | -48.5689 | 2024-11-03 05:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 936679d4-a637-3b18-98db-7bb48f31d27e | -6.5239 | -41.4929 | 2024-11-03 05:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| 65249a31-29d5-3221-9f88-65894e97de01 | -6.5241 | -41.4688 | 2024-11-03 05:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 366def3b-e5a4-33d9-b51f-3a9b77c3eae3 | -1.0441 | -47.9272 | 2024-11-03 05:25:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c3f8e377-1e5c-37f7-892b-4cc54a20d0c5 | -1.2755 | -53.4138 | 2024-11-03 05:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1b5342e6-012a-3b52-8fd3-f1ef69b36efa | -1.2755 | -53.3936 | 2024-11-03 05:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| e2399cfc-8a08-3763-87e4-15bc912d57a6 | -1.2756 | -53.3734 | 2024-11-03 05:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 73810231-4a72-3eb3-bc05-dc1e682613bb | -2.5796 | -53.3927 | 2024-11-03 05:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 80c649da-474f-3165-915c-7e861ef9b90a | -2.5797 | -53.3724 | 2024-11-03 05:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| da243b3f-e53d-38ae-abb8-1432441f5807 | -2.7419 | -54.4353 | 2024-11-03 05:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ee945fda-1416-3781-97fb-b661024836b7 | -2.7419 | -54.4153 | 2024-11-03 05:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| bbef1af1-be51-3963-b439-d18ab0b8f95f | -2.7602 | -54.4349 | 2024-11-03 05:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 00beba2c-4cc6-3621-97df-8de4e110d7b6 | -2.7876 | -51.6099 | 2024-11-03 05:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| fec491d3-a94e-3bcf-a80c-a2009595ee4c | -3.055 | -54.1474 | 2024-11-03 05:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| de0db31f-7456-3cb5-aaad-73ea833e0bb4 | -3.0734 | -54.167 | 2024-11-03 05:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 76dab5c2-176b-31cb-aefa-7090f0c7b3b7 | -3.0734 | -54.147 | 2024-11-03 05:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fe427ed0-605f-3cc9-b3cd-dd18d046a73d | -3.1059 | -50.3105 | 2024-11-03 05:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 79d6cfcb-7230-3c98-9e50-70adc5c82e4f | -3.106 | -50.2896 | 2024-11-03 05:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| e4ab125e-80d7-3ffd-bae9-2cbecbbad5ca | -3.1061 | -50.2686 | 2024-11-03 05:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9da2d5bf-7305-3f49-851c-565515e92ca7 | -3.1245 | -50.289 | 2024-11-03 05:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3f76f205-d373-33ae-ab24-e36767eec77a | -3.1501 | -48.5689 | 2024-11-03 05:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| be151665-bc83-3ef0-8fac-b211e075c2f2 | -3.3277 | -50.2615 | 2024-11-03 05:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| b6fbfb7b-364d-35d6-8824-4909875f42c6 | -3.3276 | -50.2825 | 2024-11-03 05:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 7eddbeb9-5e94-337b-8d9d-c0471e663119 | -6.5239 | -41.4929 | 2024-11-03 05:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| cc1d0af7-b28d-30cb-8845-2e891c8c8866 | -6.5241 | -41.4688 | 2024-11-03 05:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 8703f7e6-c050-3f30-ad76-e7be102f5259 | -1.27613 | -53.36914 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83617d1e-094b-32b4-92ed-cd8ad9b05833 | -1.27583 | -53.4066 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1fdd6e1f-0e5f-3129-a682-38b863d22279 | -1.27561 | -53.37253 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9461984d-62c3-3350-83ee-7701de98af1f | -1.27531 | -53.40994 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9153209c-8f27-303f-869b-d687775b5e3e | -1.27479 | -53.41329 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9edbfbc1-8c5e-3b27-9202-0adcce8a06df | -1.27458 | -53.37915 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fe0d5786-9165-36c9-bda0-b803afcb9164 | -1.27408 | -53.38242 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8709f985-1345-3edf-8cae-b7b442367119 | -1.27357 | -53.38569 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e86cde2d-8702-3d2b-930d-ce6eab4a7e47 | -1.27306 | -53.38901 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5902528-0e79-3062-846b-83419b27bdc4 | -1.27254 | -53.39238 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1431a066-daf7-31b1-95ed-92fd02e60382 | -1.27202 | -53.39574 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc75de2d-50fe-3649-a8aa-40299e125e7c | -1.2715 | -53.39912 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4be1609c-4775-31a4-818c-45adb931eeb8 | -1.27098 | -53.40248 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2126a281-2503-38f2-b1ff-b814c618ee7a | -1.27079 | -53.36812 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 842633d2-6121-30c4-93dc-0f4eec7dcbfd | -1.27046 | -53.40585 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 120d5185-7cc2-3b3e-a49a-710c5771e0be | -1.27026 | -53.37157 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 926e99ad-5dbb-348f-a113-5034cdafe705 | -1.26993 | -53.40926 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48ad25dc-15e0-34af-b0c8-71408eb70618 | -1.26974 | -53.37492 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44c98bdf-7f5b-3840-80b0-6ba6989e59c1 | -1.26923 | -53.37826 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 74ace02a-e836-3be3-ae25-f3e95d2bb488 | -1.26872 | -53.38158 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 595f3a02-0378-339f-b9b6-c860ef2e3c2f | -1.2682 | -53.38492 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f5d56bdc-2f62-31b9-ab35-6bed2e2f28b7 | -1.26769 | -53.38827 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 794e8872-40f4-39d3-90ce-64386f737e8a | -1.26717 | -53.39165 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9abe1d4-0e03-3fd4-9844-21cc9ba8938c | -1.26665 | -53.39503 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c817e32-d5a9-3162-bb32-b0b378cadd6e | -1.26612 | -53.39843 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8df2deee-4ade-3fcc-9371-a5fc0558912e | -1.2656 | -53.40183 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a52a038-6bc7-3c76-ab18-c061d0de5d44 | -1.2653 | -55.71112 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a5cbe05-98a9-3344-a409-d17c81764630 | -1.26507 | -53.40526 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 473de741-b331-31ab-8256-3a84904ca4d3 | -1.26453 | -53.40874 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 067189c0-64bc-31b6-b7da-efa2b689ef06 | -1.26386 | -55.72029 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README83.md)
