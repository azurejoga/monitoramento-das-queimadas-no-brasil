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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 161e7e4c-45d3-3128-9b1d-05fd4c6e6b54 | -6.93451 | -43.51365 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 64b011f8-278b-3c65-ad45-ed7eaa5f0ac4 | -10.91446 | -56.83231 | 2025-01-30 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35ef241e-8d29-36c6-81d8-c26fba25a0b7 | -14.1133 | -49.74928 | 2025-01-30 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1f3dfb2-e4b8-3781-bb09-78eaa0309304 | -12.0835 | -54.58365 | 2025-01-30 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0baab40e-12d8-3572-a2eb-2f315e6f3173 | -14.11689 | -49.74984 | 2025-01-30 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce437935-5705-35d7-b069-62451ab0a8d1 | -14.11032 | -49.74449 | 2025-01-30 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b45cb7b1-ff60-3a61-9385-9f5332edca80 | -21.29701 | -55.90597 | 2025-01-30 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 338be17b-d591-3d85-8354-ac64e6d04a4b | -21.19033 | -55.78867 | 2025-01-30 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85ce9487-dccc-36d9-928e-d9910782187f | -21.07516 | -56.39404 | 2025-01-30 04:48:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 575c9087-7eba-3845-aeaa-be11c0f23383 | -21.885 | -56.11108 | 2025-01-30 04:48:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bfbe4065-1c50-35b8-9fee-8deb515b8fb7 | -21.88165 | -56.11041 | 2025-01-30 04:48:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed46b486-1bd0-3104-88c2-1bee445f8796 | -20.6319 | -55.70673 | 2025-01-30 04:48:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17b401b5-2aa8-3840-acda-400039540fac | -21.9669 | -54.87457 | 2025-01-30 04:48:00 | NOAA-20 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e9e86156-2c18-3eb4-94a7-e274d5cdb691 | -20.26874 | -54.99979 | 2025-01-30 04:48:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc2c81ff-53aa-36ac-8f3d-4d97b5d0751c | -6.9349 | -43.4934 | 2025-01-30 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 00e713de-6f9a-31b6-a16e-e0338e69d0fa | -6.9537 | -43.4917 | 2025-01-30 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 293bdad1-9eee-36bf-bdf4-d264a42b8acc | -6.9346 | -43.5168 | 2025-01-30 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| f3b8a1da-954f-3b3d-9086-a32a905096ad | -6.9349 | -43.4934 | 2025-01-30 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| e3afd78c-da19-339f-bc59-5c42ae81053a | -6.9349 | -43.4934 | 2025-01-30 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 35eb68f4-6333-33f5-b433-ce44d3d493d5 | -6.9537 | -43.4917 | 2025-01-30 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e20ae972-32d1-3677-8cf8-d13ab8c20b49 | -6.9346 | -43.5168 | 2025-01-30 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b8b54cc4-951a-3fd2-8000-18e1e59e9403 | 3.74606 | -60.61583 | 2025-01-30 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34acef3d-2da6-3103-8a78-8e44e8da6e48 | 3.74715 | -60.62275 | 2025-01-30 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9305c292-3822-350a-8475-cca7d4da0105 | 3.15087 | -61.00959 | 2025-01-30 05:31:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b649b5-30e5-398b-b053-131776f5e8c5 | 3.72856 | -60.5263 | 2025-01-30 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 263d34f4-6874-3534-bbcd-a18022b1510b | 4.3499 | -60.53911 | 2025-01-30 05:31:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b895ed32-6b34-3942-ab02-d5cde43667e8 | 3.75213 | -60.61134 | 2025-01-30 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f744b1d-ea53-39a7-8626-ba5384944a92 | 3.72801 | -60.52283 | 2025-01-30 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f483d925-8522-3d67-b949-39460b190685 | 3.61674 | -60.79208 | 2025-01-30 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6ee8d71-d02e-32d7-a508-1bd8c4720947 | 3.74937 | -60.61531 | 2025-01-30 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be46f16a-87d3-3a1c-b069-0e918abec81c | 3.49286 | -60.43525 | 2025-01-30 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abe43690-7cfc-394e-86b9-b1884abcbf4d | 3.6129 | -60.78915 | 2025-01-30 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3834d71b-f4d6-323e-87d0-4c5e8ddec5b7 | -3.32981 | -54.92454 | 2025-01-30 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a714958-1de5-3c94-9952-6a0fa83ec013 | -3.3235 | -54.91226 | 2025-01-30 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ddd509aa-bc06-3cf2-84e1-b762fdce3b0c | -3.32683 | -54.92429 | 2025-01-30 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49c9be75-10a4-32a6-a7d3-d8d7e477cfde | -3.32432 | -54.9065 | 2025-01-30 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 567e5af8-5095-3ace-8080-216307f94f4c | -3.32165 | -54.91182 | 2025-01-30 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 44d7046e-b93f-3e79-b327-ed5d77232b01 | -3.32488 | -54.92385 | 2025-01-30 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2629c92f-9aaa-36fb-9263-7ff1008c980f | -3.32251 | -54.90604 | 2025-01-30 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ea4d7b69-bcf0-38d4-8946-be86e311a8e7 | -9.23798 | -60.33665 | 2025-01-30 05:35:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8952796f-d5ee-3434-a8fc-3557446a918a | -10.91941 | -56.83019 | 2025-01-30 05:35:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8dbd8a0-c0e9-310f-9f9d-1b22f6134dbf | -10.91827 | -56.83071 | 2025-01-30 05:35:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7c96a8c-4b53-36ab-803c-1fd1b7b62047 | -9.26011 | -60.31659 | 2025-01-30 05:35:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d3810f16-adfe-38b5-b408-f89b1b75f218 | -21.88669 | -56.11189 | 2025-01-30 05:40:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1006d784-7ccb-36dd-8760-3249983da110 | -21.07322 | -56.39594 | 2025-01-30 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b980c361-bf40-38ea-b30f-46f25e45f128 | 3.74474 | -60.62381 | 2025-01-30 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33f82ea6-afd1-31d3-bd6e-21b026020230 | 3.74863 | -60.61799 | 2025-01-30 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 839c251b-e600-307b-a55c-76708e8e07d7 | 3.62989 | -60.78207 | 2025-01-30 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d118f03-c08a-36e8-830a-2488838d2d98 | 3.75253 | -60.61216 | 2025-01-30 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5221e808-cf4d-314e-aff5-4ad735fefcdd | -6.9349 | -43.4934 | 2025-01-30 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 41603247-88d9-38be-8959-884a329b1452 | -6.9346 | -43.5168 | 2025-01-30 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| bfdba5a9-5653-3d7f-884a-30732a50d559 | -6.9349 | -43.4934 | 2025-01-30 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 099e516f-5df2-38a0-b5a5-2b2d64a51add | -6.9349 | -43.4934 | 2025-01-30 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 9edd1a9e-d1c1-3a21-a54c-add5870e020e | 3.74792 | -60.62359 | 2025-01-30 06:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a2ddbd7-2fa8-3513-89ad-47f852d8495f | 3.74911 | -60.63029 | 2025-01-30 06:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99aab128-3463-3234-a979-33e3468b8de1 | -6.9346 | -43.5168 | 2025-01-30 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a6abd291-00c9-3ba9-ab8c-de41e096ba5f | -6.9349 | -43.4934 | 2025-01-30 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| a2b0b11e-e32d-3b5f-8e06-1f42a937a795 | -6.9349 | -43.4934 | 2025-01-30 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| bece6218-4955-3657-8cda-5b3919150a01 | -5.13545 | -37.59727 | 2025-01-30 11:46:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 735b859f-78b6-344c-9eec-1d2e1320dd1d | -10.49444 | -37.80738 | 2025-01-30 11:49:00 | TERRA_M-M | CARIRA | SERGIPE | Brasil | 2801405 | 28 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 98ce6a83-686c-39fa-a344-801b13ea05ef | -10.84859 | -37.54452 | 2025-01-30 11:49:00 | TERRA_M-M | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| b7a960f5-085f-34f6-892c-7a3c881a5303 | -9.25316 | -35.72621 | 2025-01-30 11:49:00 | TERRA_M-M | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |


