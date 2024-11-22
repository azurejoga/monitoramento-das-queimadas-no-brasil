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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61f70153-1519-3222-8d81-2a0cc8414733 | -3.1831 | -54.3247 | 2024-11-22 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 51de589e-007b-37a2-993d-531bca4e12b6 | -1.5265 | -47.0716 | 2024-11-22 01:40:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 694084d7-ff82-3413-a55e-13708dfc83f4 | -2.504 | -54.1598 | 2024-11-22 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 5e2b8b51-3dc1-3b80-97d5-89b24cce5881 | -3.0169 | -45.1426 | 2024-11-22 01:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f81680bc-ebdf-36a8-b963-9c112747a109 | -3.7554 | -46.1204 | 2024-11-22 01:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 108.1 |
| e984212a-c939-3b01-b841-b76fc432760a | -1.5266 | -47.0497 | 2024-11-22 01:40:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| dd97246b-4f80-375b-8a0a-2dc5e25250ef | -1.1857 | -51.948 | 2024-11-22 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4fbac224-a5b5-3c37-ae23-bbfdd03c6225 | -1.1103 | -53.3953 | 2024-11-22 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6c985781-2f62-3633-b89d-e3a99eaf9a93 | -4.2424 | -48.6334 | 2024-11-22 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 091ede18-1bac-33cc-a332-cbcae1af407f | -3.4976 | -53.7935 | 2024-11-22 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0811886d-cb62-3791-b7f5-67dc7c6903af | -3.017 | -45.12 | 2024-11-22 01:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| fcb20be0-ca31-3d01-908b-9b7f84c2a5ae | -3.516 | -53.793 | 2024-11-22 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 352e9505-bc9b-30f9-baed-7d124b9aa16a | -1.2041 | -51.9478 | 2024-11-22 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 062ca14e-fd78-3126-b80b-b1f529e09360 | -1.2041 | -51.9683 | 2024-11-22 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 4b1d5667-90bd-340c-b08c-b4d9e9db0984 | -3.8355 | -52.2576 | 2024-11-22 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5cb031af-3be5-3d0c-bf31-9e0da1dded88 | -3.4592 | -45.9104 | 2024-11-22 01:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 3d646608-253b-34bf-ae27-d4939d4e42ec | -3.3452 | -50.4917 | 2024-11-22 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0bac8489-6a4f-36b8-89f3-172d30936cc1 | -3.5159 | -53.8132 | 2024-11-22 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| a958d154-e075-313e-95d9-a9e8b2100807 | -2.9984 | -45.1207 | 2024-11-22 01:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a22b53d8-02f7-3116-8b8e-0e22d1df0ece | -3.2943 | -45.447 | 2024-11-22 01:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 25ca3ade-edf7-3930-bee3-8d0f01afba0a | -2.3549 | -48.5493 | 2024-11-22 01:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0a25c5f7-09f4-38d0-9542-ec71c8ed5f05 | -1.1287 | -53.3951 | 2024-11-22 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 7087c78a-13e8-3c1d-8663-1d7634f5aeb2 | -9.9116 | -36.2634 | 2024-11-22 01:40:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.8 |
| 26cd71b0-bf3e-3dfb-abcd-df7e1a677ac4 | -3.3451 | -50.5126 | 2024-11-22 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 6b7f5b11-3bde-3141-8d1e-87e431b977f0 | -1.5265 | -47.0716 | 2024-11-22 01:50:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 19a8a165-2a34-37dc-9331-e4fffcc2371b | -3.4778 | -45.9096 | 2024-11-22 01:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| bb891eca-9303-3a01-a92e-0f539ad23595 | -1.1857 | -51.948 | 2024-11-22 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| dc10e6af-fa82-358a-b5cd-0569ae605062 | -3.3452 | -50.4917 | 2024-11-22 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 400bb25c-700a-3190-8ac2-b5e354f2ef3d | -3.5159 | -53.8132 | 2024-11-22 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 91ab6360-1819-36d8-b78e-6fbbc203481e | -2.3549 | -48.5493 | 2024-11-22 01:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e649823e-4c3c-3db9-8e90-de6902cb21a2 | -4.2424 | -48.6334 | 2024-11-22 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 4ff0f31c-5afe-3b23-a688-d89179bb8eb9 | -1.2041 | -51.9478 | 2024-11-22 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| afb9ce33-c3cd-31b0-8a98-231e73e5c1ab | -3.1831 | -54.3247 | 2024-11-22 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 14ebc2af-4f0e-317b-aed4-ebeae8fb1f1a | -3.4975 | -53.8137 | 2024-11-22 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 72f6e328-6939-3c05-9277-fb6ccfed0346 | -2.9984 | -45.1207 | 2024-11-22 01:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fd015bd1-3f72-393e-bc67-677921959b66 | -3.017 | -45.12 | 2024-11-22 01:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 40ad5eb7-422c-37c8-b9c4-4dc5a2f116a8 | -1.7549 | -52.3913 | 2024-11-22 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 416ac400-0139-309e-903d-8fabd299f2c8 | -1.1103 | -53.3953 | 2024-11-22 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0dd38dd5-2042-3c06-8f92-55190c3e6e50 | -3.0169 | -45.1426 | 2024-11-22 01:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 111.4 |
| caf165c5-789d-38ae-ac0d-13d264bb466c | -1.5266 | -47.0497 | 2024-11-22 01:50:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c260e107-213a-3f14-af3a-617b92f3446c | -1.1287 | -53.4153 | 2024-11-22 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 934e2699-8adf-3ba9-b93f-9c949127f823 | -3.7554 | -46.1204 | 2024-11-22 01:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 96f4f482-bb27-3421-977c-f2d58f4e3c6f | -3.4592 | -45.9104 | 2024-11-22 01:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 77a95313-168a-34cc-a9b7-d2db116f4bfe | -3.774 | -46.1196 | 2024-11-22 01:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| eb0607ac-46c1-3c1c-a7f6-ef4afb60ce3f | -3.4976 | -53.7935 | 2024-11-22 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 85b388c8-cd24-387f-a78a-3ad6aeee3f3b | -1.2041 | -51.9683 | 2024-11-22 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| a2ae96f6-4069-395b-bab6-2b9147a27ee0 | -1.1287 | -53.3951 | 2024-11-22 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| ed4f54ff-0bff-33fc-9bde-e9a888da28a2 | -3.2943 | -45.447 | 2024-11-22 01:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a609c79c-ad08-3740-b2f8-6eafa1d25bec | -1.7366 | -52.3916 | 2024-11-22 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 204c5471-605a-3c3d-b0aa-33e0598af9e9 | -3.516 | -53.793 | 2024-11-22 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| c2e44894-05c4-38cf-8a4d-d8c24986d087 | -2.9983 | -45.1433 | 2024-11-22 01:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d15cf4f2-0fd2-3f48-9547-613c585059ce | -1.1287 | -53.3951 | 2024-11-22 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d2a201b2-b2cd-32d7-aa84-e24b61309712 | -3.1831 | -54.3247 | 2024-11-22 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 2c1bcea4-367e-3d3c-b217-445563f62488 | -2.9984 | -45.1207 | 2024-11-22 02:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 50a88196-3c10-3000-810c-fc336b667cb8 | -1.5265 | -47.0716 | 2024-11-22 02:00:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| c2c4b838-2680-3cc3-8ba1-15acdbecd853 | -3.5159 | -53.8132 | 2024-11-22 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| d09d397e-47af-3b9a-826e-b16d6ffaf4bb | -3.3452 | -50.4917 | 2024-11-22 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 42ba618c-8d07-362b-a9b9-d94e3436e3b8 | -1.1857 | -51.948 | 2024-11-22 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6b68d3dc-61c2-3763-bb6e-d72e42a8939a | -2.3549 | -48.5493 | 2024-11-22 02:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f3cc5c64-3e22-3c8e-ac2c-9dc27bba1487 | -3.4975 | -53.8137 | 2024-11-22 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4ff5bc1b-de9f-3116-a4a7-aa5810c95e28 | -1.5266 | -47.0497 | 2024-11-22 02:00:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 610ba554-42a8-3acd-96c3-609df5ca7089 | -3.4976 | -53.7935 | 2024-11-22 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| fc69a447-9451-3ea4-8dea-887eebf33142 | -1.2041 | -51.9683 | 2024-11-22 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 3488595a-2e2c-3775-9d49-890637e28033 | -3.4592 | -45.9104 | 2024-11-22 02:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 02ae0d67-a268-3d6c-afd1-17162bbb9d54 | -3.017 | -45.12 | 2024-11-22 02:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| b0ce16ef-015e-3ab7-9db9-34fef0543ec0 | -1.2041 | -51.9478 | 2024-11-22 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| c91c1595-4695-3193-a90e-7c61ed04da1e | -3.516 | -53.793 | 2024-11-22 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b93528bf-1c05-3b9c-aac0-9105f24a47e2 | -3.8355 | -52.2576 | 2024-11-22 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 9fc0a3f1-3d15-3077-8562-78e12639f916 | -3.7554 | -46.1204 | 2024-11-22 02:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 99.2 |
| c447877d-1ad5-3bcc-a674-9f90f3e200a7 | -1.1103 | -53.3953 | 2024-11-22 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c91fcadb-cf7f-33a0-835b-de56120514ca | -3.0169 | -45.1426 | 2024-11-22 02:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 59477dc0-bcb7-3804-98a5-7612ad3a8cc8 | -3.3451 | -50.5126 | 2024-11-22 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| a3b8d479-c4eb-355a-9203-fbdb27dbfd35 | -3.774 | -46.1196 | 2024-11-22 02:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6cbe8a50-a037-3ca1-9c07-267f57bd99c0 | -3.4778 | -45.9096 | 2024-11-22 02:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9fafa35a-2717-35fb-aeaa-c40c02e87772 | -2.9983 | -45.1433 | 2024-11-22 02:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d36dd639-35a7-3354-9874-527616a47b91 | -3.23 | -54.25 | 2024-11-22 02:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c97c3060-e166-3b97-befd-d96ec0da1db6 | -3.2 | -54.25 | 2024-11-22 02:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca7728a-eed4-3046-9c9e-c2086e387435 | -3.516 | -53.793 | 2024-11-22 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c853a988-84be-38ed-9db4-6e08703a1aa2 | -2.9983 | -45.1433 | 2024-11-22 02:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 460c56d3-9a63-304c-9fde-5c2f6def0f31 | -2.9984 | -45.1207 | 2024-11-22 02:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 98016cce-70c5-3b4b-8f84-1c90020f5a22 | -1.1287 | -53.3951 | 2024-11-22 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 7402cbdc-9058-3b72-bb56-4c449d0cdafe | -2.3549 | -48.5493 | 2024-11-22 02:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 526c1e3a-aedc-3815-a93b-948520a40da2 | -3.774 | -46.1196 | 2024-11-22 02:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| cb9bc4f8-e142-3a59-8ee4-e451ea54bf74 | -1.2041 | -51.9478 | 2024-11-22 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 4b5ee366-9604-3e43-b42a-54d55cb6ab6a | -3.4976 | -53.7935 | 2024-11-22 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7d836b71-584f-3561-a8e8-49abe8ab1e41 | -3.4975 | -53.8137 | 2024-11-22 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8923aba7-b36c-3195-a4cc-b5d8ba90a9d1 | -1.5265 | -47.0716 | 2024-11-22 02:10:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 1471ceef-2431-3d17-8ea1-654154c57b31 | -3.3452 | -50.4917 | 2024-11-22 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 2b6f4a0b-336d-31fe-828c-66691d79200a | -1.1103 | -53.3953 | 2024-11-22 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 816101da-f1ec-3447-b1e8-fe7e9b896984 | -3.4592 | -45.9104 | 2024-11-22 02:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 8e8dbee9-ff3d-339d-922c-f6a5be85c143 | -1.2041 | -51.9683 | 2024-11-22 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| da27a42e-922b-3afd-8a93-a643f9adb1ac | -3.5159 | -53.8132 | 2024-11-22 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 3625ce39-5a04-3f33-974a-3fa6bfbf1613 | -3.3451 | -50.5126 | 2024-11-22 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| dd498986-9d83-3974-8164-b34ae7a9178a | -3.8355 | -52.2576 | 2024-11-22 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ad502609-78b6-3e03-83ca-ba58c3acba14 | -3.0169 | -45.1426 | 2024-11-22 02:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0a931d40-b30b-32cf-8a84-f3fd7894dca9 | -1.5266 | -47.0497 | 2024-11-22 02:10:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b16510f3-4242-3876-94e0-3a5c47cc7a8c | -3.7554 | -46.1204 | 2024-11-22 02:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 23cc6c61-ae59-3c14-afe5-f2105acd3869 | -3.7553 | -46.1427 | 2024-11-22 02:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 3eeeace8-f744-3999-8331-50ccdfd1800b | -3.1831 | -54.3247 | 2024-11-22 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9457cb8a-47b1-3787-9bd7-d30be3f9559f | -3.017 | -45.12 | 2024-11-22 02:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 111.7 |


[Clique aqui para ver as próximas entradas](README11.md)
