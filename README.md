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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 438ae4e1-bfc9-33da-9be4-3d387d81988f | -1.0733 | -53.658 | 2024-10-24 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 248bfcb8-bfd2-39c0-ab8a-c93d8304c183 | -1.5878 | -53.3292 | 2024-10-24 00:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 699680ad-089f-37de-a1a5-3c2f07bc13e6 | -1.5878 | -53.3089 | 2024-10-24 00:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c0b49b41-3a9c-3630-ac5d-5531510ec87a | -1.6062 | -53.3087 | 2024-10-24 00:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d052c6f7-c3b8-3575-ba8b-83c9ded27e1e | -2.9578 | -50.4407 | 2024-10-24 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 56115f25-3575-3520-aae1-a2dfa5944348 | -2.9578 | -50.4198 | 2024-10-24 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| d04dd762-dedb-3134-8145-c63def88e600 | -2.9763 | -50.4193 | 2024-10-24 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 87e611da-98b7-38d4-942c-4bb93b72c6fb | -3.0745 | -53.8252 | 2024-10-24 00:05:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 89bed3d8-adc3-3159-8550-5cedf02a00a7 | -3.1101 | -54.1661 | 2024-10-24 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 4d6a7e67-db6a-38f7-83dc-8f7f45a2bc6e | -3.1102 | -54.146 | 2024-10-24 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a5a42256-67e4-3566-b219-2100deefbc70 | -3.1422 | -50.4562 | 2024-10-24 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fb1dfc8b-5b9a-3775-a925-517f4483ffff | -3.1606 | -50.4766 | 2024-10-24 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| aea1711a-4290-3956-9d21-c6b67c350ac2 | -3.1607 | -50.4556 | 2024-10-24 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| d0813db8-a86f-3419-96cf-41699f9b54d0 | -3.7066 | -41.6997 | 2024-10-24 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| e2d98188-5ec0-36e5-978d-8448bb280ca8 | -3.7068 | -41.6758 | 2024-10-24 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 1b4ce6ab-7e1e-34dd-9a51-6758740b9add | -3.7254 | -41.6987 | 2024-10-24 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 3f716ba2-64df-3637-b0c2-be5d7a4c6889 | -3.7255 | -41.6748 | 2024-10-24 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| c0336ef3-2345-31e5-9c5b-89c30419fa76 | -3.6612 | -54.2715 | 2024-10-24 00:05:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 77b2cb20-529a-35b7-8b91-0f570d179646 | -4.2134 | -44.2696 | 2024-10-24 00:05:30 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 42d08c19-ab53-36a8-ba12-29dd67176e56 | -4.2321 | -44.2685 | 2024-10-24 00:05:30 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| e9767b74-1bea-37b3-93c8-ac2044ef5aab | -4.2907 | -46.7597 | 2024-10-24 00:05:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 645e377f-2eb4-38e5-9dc9-eed7c84a3efb | -4.5572 | -45.8128 | 2024-10-24 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 851af2c5-46ae-3269-9be0-efbe6ecc4367 | -4.5574 | -45.7905 | 2024-10-24 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 7054bc9d-b7c3-3806-8ee2-8fe7d78c913a | -4.6586 | -44.6328 | 2024-10-24 00:05:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| fd6bdb01-d2cf-3eb4-a502-73759f9a9efd | -4.6588 | -44.61 | 2024-10-24 00:05:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 257831f3-a8f9-3bd8-98aa-069e48382db0 | -4.659 | -44.5872 | 2024-10-24 00:05:32 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 029b5797-c0df-36f8-a3bc-b73d24b0cc97 | -4.6773 | -44.6317 | 2024-10-24 00:05:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e9a8f05a-6d73-3767-8056-47476d100578 | -4.6775 | -44.6089 | 2024-10-24 00:05:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 227.9 |
| f4ebe4f3-e43a-3ece-adc3-69d9b3675a14 | -4.6776 | -44.5861 | 2024-10-24 00:05:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a50b5a8c-7b1e-3afc-bcf8-158b113796ce | -4.758 | -46.4033 | 2024-10-24 00:05:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 51115701-2118-34b3-9a48-76e4476c4bc6 | -4.8423 | -45.0309 | 2024-10-24 00:05:34 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| c1fce5a2-9b7d-3cf7-b368-76328a64fc62 | -6.9272 | -40.8466 | 2024-10-24 00:05:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 183.3 |
| bf7df7a7-156e-382f-9f3f-c665be5ba378 | -6.9461 | -40.8447 | 2024-10-24 00:05:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 371.7 |
| 76ef9125-33ea-33fb-9109-4bedf290cb74 | -6.9464 | -40.8203 | 2024-10-24 00:05:45 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 00cd03ba-aec7-35a8-b9f7-c365d2a4c047 | -6.7666 | -59.1129 | 2024-10-24 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a814091f-b7e2-3e5b-8d21-8de9aa33d2e1 | -7.481 | -63.5577 | 2024-10-24 00:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7b91f592-3387-3d08-91e9-930ade340011 | -11.5924 | -48.5544 | 2024-10-24 00:06:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f42e4cbe-9f69-3656-a024-a55b10d69d13 | -12.672 | -43.8517 | 2024-10-24 00:06:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| db016290-d715-3ba3-9e48-33abd54184a7 | -12.6725 | -43.8279 | 2024-10-24 00:06:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5d31fa14-c024-3455-bb8c-b1e3257a9fc6 | -12.6914 | -43.8484 | 2024-10-24 00:06:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| ad47b3fe-016d-3e4a-88e2-83c2eaf1b81d | -12.6918 | -43.8247 | 2024-10-24 00:06:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 492b4340-7d9a-3527-8230-d9fb0c02f63b | -12.3595 | -63.864 | 2024-10-24 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b836b239-e905-3b05-bae9-28dcb05d0e22 | -12.3783 | -63.863 | 2024-10-24 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d0fc59e1-20b7-3a69-a59f-b36a7d457ef1 | -13.7609 | -54.0661 | 2024-10-24 00:06:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a8b08d77-9740-3a12-8ea0-392ca001a6f7 | -14.9145 | -45.1224 | 2024-10-24 00:06:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 9bc6ea9e-ed53-3edb-b9ed-dd9ced1da44a | -14.9341 | -45.1187 | 2024-10-24 00:06:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f78f5c61-943f-3a44-90ec-c5b97a0e98ad | -15.5389 | -50.6688 | 2024-10-24 00:06:33 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 6620e9c5-30dd-373e-b8e2-0660901a92cb | -15.5393 | -50.647 | 2024-10-24 00:06:33 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b76585bf-0203-36d4-b585-540e2f84854a | -15.5584 | -50.6658 | 2024-10-24 00:06:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 301.3 |
| 89f7ac8b-f21c-3807-a957-96cf9246cbf7 | -15.5589 | -50.644 | 2024-10-24 00:06:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 252.9 |
| 7e23d763-b93d-3abe-8527-212f499d4c35 | -15.578 | -50.6628 | 2024-10-24 00:06:34 | GOES-16 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| eb05cf64-7cbe-34e8-aba1-9f745187082b | -16.94 | -57.5268 | 2024-10-24 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 84512f56-119c-3131-8d01-b498aedba6f5 | -16.9596 | -57.5245 | 2024-10-24 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| e32b6b83-d395-34b1-92ec-09aa18487b9b | -17.0207 | -57.3743 | 2024-10-24 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 858ef569-5161-3389-be81-f94c29a0d583 | -17.0596 | -57.3902 | 2024-10-24 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 6843fb58-53ac-347f-bf87-09275e58e295 | -17.238 | -57.2668 | 2024-10-24 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| c88dc070-5fe0-34fe-b78e-c8d156fde4cf | -17.2383 | -57.2462 | 2024-10-24 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.6 |
| 08c8ab67-243c-3360-a311-6c2431551d28 | -17.2579 | -57.2439 | 2024-10-24 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| b14d9964-6775-3451-b7b4-c28e3b6fec9b | -17.7841 | -57.5296 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| a2f838cd-c523-3d52-925a-dce0cbf85809 | -17.7844 | -57.5091 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 3dde16f2-5de6-3d6e-8caa-17626898f862 | -17.6671 | -57.4616 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 871f0418-b44e-3511-b8c3-e2f8c41b839a | -17.6865 | -57.4798 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 2dafb9a9-bd9a-37d8-a4ab-32bf4210a8d6 | -17.7062 | -57.4774 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| e54838e7-75ca-32ec-ad12-74d772018670 | -17.7453 | -57.4933 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 04ab6eae-41e8-3ab7-a489-dfb7038cc6f5 | -17.7456 | -57.4727 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 80505071-93ad-37ab-a2e8-cdec317d30da | -17.7634 | -57.5937 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| fdbdf0e6-9bce-3877-be25-b0b27fee3e1a | -17.7637 | -57.5732 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| bbc72fd1-38e0-32e9-9566-f9037e5111d1 | -17.764 | -57.5526 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| d15d7aea-db41-3d9f-af7e-6553ce7cecbe | -17.765 | -57.4909 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 82b30233-4b83-3905-b0ac-57165c416f39 | -17.7831 | -57.5914 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| cf5bf471-e2e5-37dc-93c5-a0c8a463b46f | -17.7834 | -57.5708 | 2024-10-24 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| ab76fd0e-a5df-36df-9eac-c608172f3357 | -17.9667 | -57.2191 | 2024-10-24 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 7bd416bd-cec5-3597-a6fc-d8784ae70b9a | -18.0639 | -57.3101 | 2024-10-24 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| e0994872-88d7-3f0b-84ba-da4a9d89d540 | -18.0834 | -57.3283 | 2024-10-24 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 401767f9-cba3-34f4-9084-65a1c7295d86 | -18.0837 | -57.3076 | 2024-10-24 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.0 |
| ba4e8aa7-a4ed-3ea7-9e0b-1a1d9963038f | -18.1032 | -57.3258 | 2024-10-24 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| feafbdac-09bb-302f-b4cc-b0391015f586 | -19.7061 | -56.7386 | 2024-10-24 00:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 3df277a6-3391-3518-9919-cba8fa854e3c | -23.816 | -55.2713 | 2024-10-24 00:07:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| fe45c018-73f6-3f01-972d-66b86e2aeb93 | 1.7959 | -50.4677 | 2024-10-24 00:14:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 49.7 |
| adefaebe-b726-32e1-ac23-c761cc8391a9 | -1.5878 | -53.3089 | 2024-10-24 00:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 345b8e05-de50-3a38-bf6a-3be73964d2ef | -1.6062 | -53.3087 | 2024-10-24 00:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| ebbf395d-ab4b-3cb4-b068-64fcb701ffc0 | -2.1244 | -45.3285 | 2024-10-24 00:15:18 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 239f30dc-be4d-310a-b276-a6ca28c6422f | -2.1245 | -45.306 | 2024-10-24 00:15:18 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| a9e32563-fbc5-3733-8f1c-8c5d8b43e581 | -2.9578 | -50.4407 | 2024-10-24 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 6680804a-85ee-3fbd-bd76-1956ad874b9b | -2.9578 | -50.4198 | 2024-10-24 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| b0110d68-86c6-3eb3-bec2-cee9081c8c0d | -2.9763 | -50.4193 | 2024-10-24 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| df5e0937-8b45-3654-b7eb-5e6bc45170d6 | -3.0745 | -53.8252 | 2024-10-24 00:15:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| ec72aba4-ad61-3122-abf0-64b9c54ad6a7 | -3.1101 | -54.1661 | 2024-10-24 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 0d418a7f-ff52-3e5b-8757-b8b1b773738d | -3.1102 | -54.146 | 2024-10-24 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 28dd4a93-0eda-3606-aad2-782f45a22d16 | -3.1422 | -50.4562 | 2024-10-24 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e5093892-8360-3b3e-be11-0c632c5bb069 | -3.1606 | -50.4766 | 2024-10-24 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| faf81905-77ed-3f3f-9809-39afa432b565 | -3.1607 | -50.4556 | 2024-10-24 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| fa0d4db9-80c3-3e19-bf05-01928a5e3273 | -3.7066 | -41.6997 | 2024-10-24 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 564e30d8-5ae0-3c51-9bd3-94552cb5517f | -3.7068 | -41.6758 | 2024-10-24 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| bf4dd019-3ec2-3410-bdd6-b3cdba5ed8fd | -3.7254 | -41.6987 | 2024-10-24 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 18a9de39-6a81-322c-89f8-89e6385a53cf | -3.7255 | -41.6748 | 2024-10-24 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| cf4d5458-6e4e-3c76-b959-4f1c91ed1b1e | -3.6612 | -54.2715 | 2024-10-24 00:15:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a75e074d-6026-3261-bb79-28b7ffc457ce | -4.2134 | -44.2696 | 2024-10-24 00:15:30 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 7f41cf6a-26cc-3c69-8983-ffa2fa8e7240 | -4.2321 | -44.2685 | 2024-10-24 00:15:30 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| d9059680-f333-3e06-bc72-ed47649c4d42 | -4.2979 | -45.6026 | 2024-10-24 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |


[Clique aqui para ver as próximas entradas](README2.md)
