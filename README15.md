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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4aa0a161-1fc3-3018-9742-e687a156f93b | -5.4373 | -47.6833 | 2024-10-24 02:55:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4d073a24-1eff-3573-a123-fbb76cb51590 | -5.4559 | -47.6822 | 2024-10-24 02:55:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7cf59970-ba6a-325a-87f7-7818d2568bbf | -14.2703 | -51.1328 | 2024-10-24 02:56:27 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| f41fe497-f5a8-3568-b81a-873669cb63bd | -17.2383 | -57.2462 | 2024-10-24 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 60862dbc-fc54-3bbc-a7cb-4b3b819c44d0 | -17.2576 | -57.2644 | 2024-10-24 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| f5b25bda-9a35-394e-a6cd-8f46b53ce133 | -17.2579 | -57.2439 | 2024-10-24 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |
| 1dae32bd-370f-33aa-bc58-2e0b54170a14 | -17.7834 | -57.5708 | 2024-10-24 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| d991f68c-a294-3a62-942c-b28fdcc1502c | -17.7844 | -57.5091 | 2024-10-24 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 34e7e993-9f97-3912-a400-dff678fb30f1 | -18.0837 | -57.3076 | 2024-10-24 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 6f206219-37d3-389b-8d05-a9e049978526 | -19.5681 | -56.6114 | 2024-10-24 02:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 7dc4164b-9834-3a93-a1e8-e586a93b2180 | -19.6438 | -56.8521 | 2024-10-24 02:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.5 |
| e8917ffd-2083-3eee-9257-3b9712ce5e1f | -19.6442 | -56.8311 | 2024-10-24 02:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| bce5127f-ea55-3988-97d9-14e24a9c695a | -1.5878 | -53.3089 | 2024-10-24 03:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5abf0349-c1f1-3011-833e-7decfb2dd2e5 | -1.4945 | -54.1761 | 2024-10-24 03:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 27bb7bde-00ab-3ef0-8080-cf7f999e1a57 | -1.4945 | -54.1962 | 2024-10-24 03:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 2a084810-48d1-37f8-a585-8067be1ca9fa | -2.9763 | -50.4193 | 2024-10-24 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| dd318feb-dd6f-3105-af9d-b62ac2db7771 | -3.1607 | -50.4556 | 2024-10-24 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1aea115e-cd5f-3cbf-bd24-cc9b405e956e | -3.1102 | -54.146 | 2024-10-24 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 80225814-df33-373a-8dbc-a0f497a55c5e | -3.1101 | -54.1661 | 2024-10-24 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 94243617-dda5-318a-a3a2-d3ce6674b5ae | -3.9396 | -46.4229 | 2024-10-24 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 41ecd73e-3cb8-3231-ac89-736993fba850 | -3.9394 | -46.445 | 2024-10-24 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 80c5ca19-cb3c-33e5-a966-3916a0babecc | -5.4559 | -47.6822 | 2024-10-24 03:05:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 99e72ffa-edaf-3c82-a815-c722e2dd6549 | -14.2703 | -51.1328 | 2024-10-24 03:06:27 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 17e738fc-b98a-3ba3-ba54-1e0f859adb4e | -17.039 | -57.454 | 2024-10-24 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 986ad5b1-5c96-31da-92fb-b052501db0d9 | -17.0387 | -57.4745 | 2024-10-24 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| d5f2017e-0d7e-316b-b79e-1547871928e0 | -17.2579 | -57.2439 | 2024-10-24 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.5 |
| 65bf089c-91ec-38a8-ac6b-ac648fbf4d5f | -17.2576 | -57.2644 | 2024-10-24 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 45446ea3-a8d3-3cae-b887-a44ad5965582 | -17.2383 | -57.2462 | 2024-10-24 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| ca5bbca4-6e3b-3f1f-afea-a1dd5b5f0ab9 | -17.238 | -57.2668 | 2024-10-24 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| c092bcfa-06fc-374e-b6c3-2c7feeaffacf | -18.0837 | -57.3076 | 2024-10-24 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 2293a44d-fd73-3ea1-b356-7d62872fbdd2 | -19.6442 | -56.8311 | 2024-10-24 03:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 25f910ff-13c0-33a2-bc8b-a73e3d5a3ff1 | -19.6438 | -56.8521 | 2024-10-24 03:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.4 |
| 371e023a-4d88-3069-989a-d58c0dde90aa | -19.5681 | -56.6114 | 2024-10-24 03:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 017371b8-3806-33b4-89ce-adbb234b32b2 | 4.8312 | -60.138 | 2024-10-24 03:14:38 | GOES-16 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 80de08b3-7c87-37b2-83d4-55eca0cc044e | -6.83099 | -35.15084 | 2024-10-24 03:15:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| c3de2eb0-1fef-3043-b0d0-6b62b068100a | -6.83025 | -35.15511 | 2024-10-24 03:15:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| afe17757-bbb5-3788-a05e-7e88ed6c9b43 | -6.82719 | -35.15247 | 2024-10-24 03:15:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1d529136-ae6a-3f23-bc6e-3d3fb609eb3a | -8.9797 | -35.55912 | 2024-10-24 03:15:00 | NPP-375D | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b1fc0a7c-83ed-3fdd-82b5-a3dd8b52a530 | -8.98405 | -35.55997 | 2024-10-24 03:15:00 | NPP-375D | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 008cd45f-c002-346c-835f-c9f910d5c4a2 | -8.7275 | -35.116 | 2024-10-24 03:15:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e6996fa2-b9af-3356-b93f-ea9f4a7ec439 | -8.72681 | -35.11999 | 2024-10-24 03:15:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed0d7d2d-0f09-3ff9-9925-c3b3862e8d52 | -5.16678 | -37.71218 | 2024-10-24 03:15:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dc4cbcde-c921-3330-bcff-77cd0fa95394 | -5.16621 | -37.71557 | 2024-10-24 03:15:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 03b78e3b-9e81-32dd-8db6-c681ed0b6dfe | -6.72082 | -37.51145 | 2024-10-24 03:15:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 88995578-f900-343c-84cb-b4f5c1678fe5 | -6.17213 | -39.41335 | 2024-10-24 03:15:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11818848-efc8-332b-aaa5-5561e6f31b3e | -7.30618 | -39.14249 | 2024-10-24 03:15:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9d22a716-e519-3db4-9981-8f5657359417 | -7.30045 | -39.14155 | 2024-10-24 03:15:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5f691e35-70ff-33f1-8b34-267f71e1c578 | -6.73484 | -40.48497 | 2024-10-24 03:15:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf6292dd-219f-35c3-8fd6-0f63e242c724 | -6.73301 | -40.49477 | 2024-10-24 03:15:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1c438d4a-9d33-3b31-86f0-37c4bb38e20b | -6.7322 | -40.4837 | 2024-10-24 03:15:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1f9b82c2-60af-3e5d-88d0-ab30cbf1a3af | -6.73209 | -40.4997 | 2024-10-24 03:15:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bf71f47f-dbf3-3dd3-b231-59de6b613f83 | -6.72955 | -40.47861 | 2024-10-24 03:15:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c0f54567-ccc5-3439-887e-b11a9c8126a1 | -6.72862 | -40.48357 | 2024-10-24 03:15:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0242f5fc-5552-3711-addd-aac8c72561b5 | -7.30588 | -39.13669 | 2024-10-24 03:15:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8c9f6d2-e7de-3946-ba27-7ef1106147d4 | -7.3051 | -39.14112 | 2024-10-24 03:15:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c0faa4a5-a4ae-306b-88c9-70be5d675b83 | -7.30126 | -39.13719 | 2024-10-24 03:15:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5b3e16c9-ab39-3baa-8b44-31dd6cf42863 | -7.30011 | -39.13603 | 2024-10-24 03:15:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02d14a42-d6c0-3669-b242-a3dfde335f0f | -6.73578 | -40.49981 | 2024-10-24 03:15:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ab3c209-0eb7-3b26-9e08-85c8c166e81a | -6.73131 | -40.48863 | 2024-10-24 03:15:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7fba8c6b-8eba-38a0-a12e-d879df0a1356 | -6.72953 | -40.49855 | 2024-10-24 03:15:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 784cd796-5fa7-34bb-b6f3-5ef1ba7c5356 | -6.73576 | -40.48009 | 2024-10-24 03:15:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cfa1f5bd-a58b-36b0-a746-28c93e031dae | -6.73309 | -40.47879 | 2024-10-24 03:15:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d8714ec5-f581-329e-9a71-826733075bca | -8.36399 | -40.2977 | 2024-10-24 03:15:00 | NPP-375D | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c31492e3-3c87-32c7-8569-505bf0ae9aa4 | -8.36313 | -40.30215 | 2024-10-24 03:15:00 | NPP-375D | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7f0cdd7-4395-3322-a54a-fa5d6ba0a686 | -6.94009 | -40.84708 | 2024-10-24 03:15:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 734c559d-f86c-3129-8aba-0bce29e3906c | -6.93913 | -40.85232 | 2024-10-24 03:15:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d03d75b0-a81f-3b7a-8302-a216b8647bb9 | -6.93279 | -40.85088 | 2024-10-24 03:15:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a78dd078-7575-3283-a7a6-07c90f13183c | -6.93375 | -40.84566 | 2024-10-24 03:15:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e1efeb96-3156-3a11-8ad8-6f351f036c0a | -3.71433 | -41.68434 | 2024-10-24 03:15:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| a94b1490-3135-3f37-a962-fe37d189f01c | -3.71314 | -41.69114 | 2024-10-24 03:15:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f656dfdb-a60e-3e5f-95ce-f27d62ea5e40 | -3.70729 | -41.68304 | 2024-10-24 03:15:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 2d84ffa7-5ac9-3d32-94d6-c93f4ac24e10 | -3.70608 | -41.68993 | 2024-10-24 03:15:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| d59122da-baae-3c2e-8782-3b1280783557 | -7.07126 | -42.56011 | 2024-10-24 03:15:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 512935b7-a456-3ac2-b6e4-4725695292de | -7.06768 | -42.55544 | 2024-10-24 03:15:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8e7d755b-3aa6-37f6-a302-d01ebc220609 | -7.06631 | -42.56272 | 2024-10-24 03:15:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c0907964-2e24-3500-b617-5ec7600792b4 | -7.06423 | -42.55878 | 2024-10-24 03:15:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 211f2569-ea03-34ec-a595-2a70a8228522 | -1.4945 | -54.1761 | 2024-10-24 03:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 4ae15921-8dd1-34fc-ac88-03ccb568e06f | -1.5878 | -53.3089 | 2024-10-24 03:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 3fe5f24e-04bc-3e3c-b9c1-d0fc989a6433 | -2.9763 | -50.4193 | 2024-10-24 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4ab5e9ce-cdc5-3a1f-8e42-862fdce33a51 | -3.1094 | -45.2293 | 2024-10-24 03:15:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| cda0113b-db20-3f62-b217-e6747896cf65 | -3.1101 | -54.1661 | 2024-10-24 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| eb190e4e-2e5b-3583-940e-11e6e444a5f0 | -3.1607 | -50.4556 | 2024-10-24 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| efd923b2-ca6e-3db0-9614-253d121d05bc | -3.9396 | -46.4229 | 2024-10-24 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e76de894-0df6-3397-a401-690de0cca9db | -5.4373 | -47.6833 | 2024-10-24 03:15:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e8ae53c2-d1ae-3e9a-bdb0-33332c36e416 | -14.2703 | -51.1328 | 2024-10-24 03:16:27 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 876f3ca2-7556-3fc1-a732-a51b0f3ee6ae | -16.94 | -57.5268 | 2024-10-24 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 4fb1529e-6274-3361-9482-b593c2df832e | -17.0387 | -57.4745 | 2024-10-24 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 387c4bbf-c41f-3090-b1a4-9d9084b5c4b5 | -17.039 | -57.454 | 2024-10-24 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 640b71f1-dcd0-3bc4-9c13-ef18496f64b8 | -17.2383 | -57.2462 | 2024-10-24 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| baddaa79-5d1a-3da7-af9c-08c430de2a00 | -17.2579 | -57.2439 | 2024-10-24 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 8b5760c3-1658-34fd-afab-2b2cfc491231 | -18.0837 | -57.3076 | 2024-10-24 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 195d730e-00a8-39bd-8302-6617e6c315a2 | -19.5681 | -56.6114 | 2024-10-24 03:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 105.9 |
| dc2c988d-5425-38e9-a508-84be06b267e6 | -19.6438 | -56.8521 | 2024-10-24 03:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| a41bf50a-563d-32fb-9b10-102ef00811c0 | -19.6442 | -56.8311 | 2024-10-24 03:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 599604bf-b7e3-3524-bc9f-2d5d6417fea6 | -15.77503 | -41.27847 | 2024-10-24 03:17:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8993bd82-a51b-3185-bc72-fcb20a20dd55 | -15.77425 | -41.28224 | 2024-10-24 03:17:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b97af880-119c-3ee5-9883-28f9624fd708 | -13.70318 | -42.88118 | 2024-10-24 03:17:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f8ecf6a4-837f-3c4e-a38c-6ca4abd1ee1d | -13.70206 | -42.88644 | 2024-10-24 03:17:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96c1af43-4dc4-36ef-8c95-ae87d355113f | -14.94563 | -43.16685 | 2024-10-24 03:17:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 06e99377-18ad-3b80-ab64-fad130a2128c | -14.94447 | -43.17225 | 2024-10-24 03:17:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README16.md)
