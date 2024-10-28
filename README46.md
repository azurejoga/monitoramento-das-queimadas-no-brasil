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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 049753f8-9faa-39d7-ac0b-c6db12d29eb6 | -2.833 | -49.2413 | 2024-10-28 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d4afc1ea-cd41-38ff-8181-e3b9cbd45e09 | -2.8699 | -49.2615 | 2024-10-28 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| d2c669ca-39df-3e77-b4f6-57c8372891dd | -2.87 | -49.2402 | 2024-10-28 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 3c873841-56bd-31f0-b55a-8c0ec533cf7e | -2.8884 | -49.2609 | 2024-10-28 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 3a7bbcf0-5021-3bce-ac1b-834d88c16a46 | -2.8885 | -49.2397 | 2024-10-28 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 6f3b1441-1091-3ddf-a723-ceaea904d1ca | -3.0317 | -50.4176 | 2024-10-28 04:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| f5f32266-bc13-3382-a267-157df0c47a36 | -3.0317 | -50.3967 | 2024-10-28 04:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b4b84cc4-d8c0-3313-9456-d4ad3f547e6d | -3.0501 | -50.4171 | 2024-10-28 04:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 82138a81-100b-3d94-a409-b989117bfdc9 | -3.4968 | -45.8195 | 2024-10-28 04:25:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 183cab5a-7531-3ad9-9270-d9641fb45f6f | -3.497 | -45.7971 | 2024-10-28 04:25:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 990bae60-706f-37be-ba25-7da3e559f707 | -3.5154 | -45.8187 | 2024-10-28 04:25:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6e0085c3-6176-3e4d-aa7f-8550f229e508 | -3.5155 | -45.7964 | 2024-10-28 04:25:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 189.2 |
| baeb3852-060e-3e20-88b8-7da9abbb843d | -4.1201 | -47.3169 | 2024-10-28 04:25:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8f02b100-bcea-33c8-89cb-e4e369054660 | -1.9763 | -52.0804 | 2024-10-28 04:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a5c9f2b3-fad0-32b1-8d7c-b6d8a5533149 | -2.2662 | -53.7825 | 2024-10-28 04:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 603c38c3-c8a2-3be1-bfc7-d9488bc65325 | -2.2846 | -53.7822 | 2024-10-28 04:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f43a5df0-ee9e-3fde-ba14-447b8c48d9aa | -2.4104 | -48.5479 | 2024-10-28 04:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 38f4fe74-8a99-333f-9327-e9b41b972548 | -2.833 | -49.2413 | 2024-10-28 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4976e37e-e745-3d7e-9625-6d5fed4bacdd | -2.8885 | -49.2397 | 2024-10-28 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 80cacd89-657a-39ad-ae6f-a92d77c4e3f8 | -2.8699 | -49.2615 | 2024-10-28 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| e81fda78-5716-333e-b0a7-030fd2eb0623 | -2.87 | -49.2402 | 2024-10-28 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 0807d6d9-18b8-3874-b822-d191c628ce30 | -2.8884 | -49.2609 | 2024-10-28 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 28861f97-1a24-3883-b435-c70c8ca60fe4 | -3.0317 | -50.4176 | 2024-10-28 04:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| a6876cda-736e-3270-9363-b7cd15edad40 | -3.0317 | -50.3967 | 2024-10-28 04:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 2ae03475-9b0c-35e4-a299-8e090f9acc2b | -3.0501 | -50.4171 | 2024-10-28 04:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 864c2d1e-d2a2-30d1-95d2-2eadabc8bee7 | -3.5155 | -45.7964 | 2024-10-28 04:35:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 75f72969-ee6a-3c78-be5d-2a7fe8cbd6f1 | -3.497 | -45.7971 | 2024-10-28 04:35:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 10baf21d-b284-35cc-9c9f-667a00e67aa0 | -1.1836 | -53.4956 | 2024-10-28 04:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 81438d62-5a84-3b92-a86a-c3a7cd828410 | -1.9763 | -52.0804 | 2024-10-28 04:45:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0a099d24-0c71-31c0-ac99-553e2eb79ba7 | -2.2662 | -53.7825 | 2024-10-28 04:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| d3708729-b0f9-3415-bd33-d8cdff5e62dd | -2.2846 | -53.7822 | 2024-10-28 04:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| a82ad18c-0e88-3bbe-9520-65d38aec504c | -2.4104 | -48.5479 | 2024-10-28 04:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3f7602c5-a281-332e-9a7a-e6bb35cf78d6 | -2.8884 | -49.2609 | 2024-10-28 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 88db31be-431c-3889-af3d-5e0d54a2d009 | -2.8885 | -49.2397 | 2024-10-28 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 927a816a-f361-33ba-89f3-bd120d352b2f | -2.833 | -49.2413 | 2024-10-28 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5ac1edd4-9bdc-3cd8-9526-766def48ca27 | -2.8699 | -49.2615 | 2024-10-28 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 9514afd5-6afe-3ba5-aa71-8a16c38bd260 | -2.87 | -49.2402 | 2024-10-28 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| d219735a-b0a7-3c0e-8f6b-1e82f098888e | -3.0317 | -50.4176 | 2024-10-28 04:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a8a410c3-42ce-3ada-bbf6-539b260d9712 | -3.0317 | -50.3967 | 2024-10-28 04:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 9160ebc7-7254-392f-ab35-3e24152e29f3 | -3.0501 | -50.4171 | 2024-10-28 04:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5add5e9f-74e3-39f0-bea9-1ff7292c9dc0 | -3.497 | -45.7971 | 2024-10-28 04:45:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b1f92407-a442-3b9a-bc0b-c401e54f4f2d | -3.5155 | -45.7964 | 2024-10-28 04:45:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 933c0047-d98c-35ca-8daa-cef03b1cab24 | -1.13055 | -48.38599 | 2024-10-28 04:55:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45cb5f24-2144-35a9-b7e1-9c9609cb21c0 | -1.12818 | -48.37547 | 2024-10-28 04:55:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 733013f7-280d-3feb-be77-729ab599c6c0 | -1.09237 | -47.23806 | 2024-10-28 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 956ad916-e6ca-32c8-a2b7-a1261cbd4d68 | -1.08876 | -47.23352 | 2024-10-28 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3414f9f2-9391-3b89-93b5-9f6417953c4f | -1.08815 | -47.2374 | 2024-10-28 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14ab9139-9877-3101-9a50-4882290c1a03 | -1.08454 | -47.23288 | 2024-10-28 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e5cceb8f-d2a9-3722-8448-f17ba42ceffd | -1.05758 | -48.26071 | 2024-10-28 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f7ea3e7a-b97f-376d-ab12-d3e7775f21fe | -0.95048 | -48.27735 | 2024-10-28 04:55:00 | NOAA-21 | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdc2c38a-d1db-38a1-8c77-5d33e90fc8c9 | 0.08094 | -49.87395 | 2024-10-28 04:55:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4e3d251-beb5-30e1-a350-70dc0fa30e26 | -0.6702 | -49.53636 | 2024-10-28 04:55:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad036a96-aa2f-3aba-b184-79ad0bdf7c11 | -0.66908 | -49.53807 | 2024-10-28 04:55:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5540ffe-dfb8-33ee-8696-38d9f5aec9b5 | -0.66592 | -49.54001 | 2024-10-28 04:55:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01724ce9-547f-36f4-828b-023fbeca0165 | -0.66478 | -49.54171 | 2024-10-28 04:55:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c9b1ba9-8cb0-37af-b8cf-3073c380f559 | -0.63769 | -49.57196 | 2024-10-28 04:55:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36a1fca5-c28e-3d62-b155-3f6059fa8e42 | -0.63472 | -49.5672 | 2024-10-28 04:55:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 031dc950-0c27-365b-8176-94d8a282cc08 | -0.26506 | -48.78643 | 2024-10-28 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dd730330-0193-373f-a4c1-3e27c8311787 | -0.26129 | -48.78583 | 2024-10-28 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 999ac0f6-1784-3f35-86d6-195ab5b3f2d7 | -0.24431 | -48.94549 | 2024-10-28 04:55:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8dcd8bb7-8abd-3a1e-8f44-48971dd38cc4 | -0.22378 | -48.80043 | 2024-10-28 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7ed09a7a-6300-35ec-adc5-5a25cbf708f2 | 2.36358 | -50.75716 | 2024-10-28 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c56187db-919c-333a-a173-46fa5f1993a0 | 2.35966 | -50.75412 | 2024-10-28 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aeba0a6-34c3-368b-af51-63b56588a209 | 2.35687 | -50.75821 | 2024-10-28 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22a9f5e0-33ac-32ef-bfeb-ada1d1419b0b | 2.3563 | -50.75465 | 2024-10-28 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd872b79-7892-3052-a6df-ab3830583966 | 2.35454 | -50.75819 | 2024-10-28 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f02e819d-6fc0-3f7b-9df0-d0bf648ae8ae | 2.35399 | -50.75462 | 2024-10-28 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1cdb223d-1501-32f2-98cf-8b900aea2d6d | 2.29745 | -50.76714 | 2024-10-28 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6b78d17f-5a0d-30cf-9dd7-9100fe35b9f0 | 1.93665 | -50.83442 | 2024-10-28 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a077d82-37cb-3241-98b1-37291826958b | 1.80539 | -50.4543 | 2024-10-28 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a74ebfa-66b0-3bf1-b560-e693711b23a7 | 1.80199 | -50.45484 | 2024-10-28 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a77a70c-5549-3862-8850-d0025b3f52e2 | 1.6055 | -50.99528 | 2024-10-28 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0237afb8-3653-3fe3-a4a3-55a92eb7b030 | 1.40034 | -50.8223 | 2024-10-28 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffa10832-e371-3be0-98a3-51f9ecd40923 | 1.26468 | -50.86111 | 2024-10-28 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 561731d9-7850-3616-b68b-0ee787bc67e6 | 1.09082 | -50.77762 | 2024-10-28 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7414ca40-32b0-3a23-a0af-d98afcf52208 | 0.83171 | -50.22421 | 2024-10-28 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a3369d1-b757-3c90-bbc1-a3dbe9d8ac53 | 0.52219 | -50.13814 | 2024-10-28 04:55:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b86c41d-cb39-3ad6-a274-f727bfc0e505 | 0.31661 | -50.92235 | 2024-10-28 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22da3b82-6a12-30c6-a45f-5454ed068012 | 0.31322 | -50.92288 | 2024-10-28 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c7986bb-ca41-356a-ad3c-954214802c9b | -0.09929 | -51.32125 | 2024-10-28 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e76c27fa-fe8e-303e-9794-3fea20ad1865 | 0.92238 | -59.66133 | 2024-10-28 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3432d0ae-1b50-366f-a6bf-9898411ebc02 | 0.92334 | -59.65844 | 2024-10-28 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 524a0e0f-1bce-36be-afae-3364508e9f3d | 3.73784 | -51.80444 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 991d34d5-2116-31a4-a7f8-c9d27f2391fa | 3.59614 | -51.27386 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00b14f9c-e78d-3899-a5d6-7ac6ab4678bb | 3.59284 | -51.27438 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f51d557-01f6-35fe-87bf-16431a862a5c | 3.58953 | -51.27489 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49326d87-4617-3723-b3de-22288f622c92 | 3.58731 | -51.28232 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ef8d111-91d3-326c-a6d7-b5d372059d0e | 3.58677 | -51.27887 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 96324309-e661-3991-9494-8373a510191b | 3.58622 | -51.27541 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5acb11f5-8776-34ff-a75b-917fd19b7279 | 3.58346 | -51.27938 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bbbb0e56-f8cf-3ad8-b05b-2e64453319da | 3.47339 | -51.25106 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31d40773-3bb5-3739-ae0e-338a9b7fc407 | 3.47284 | -51.2476 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a651c4e7-6ca5-32f1-8db3-c34de15d7e9a | 3.46953 | -51.24812 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85c8e63a-0cd7-36c3-92be-ef067d04b2e7 | 3.46899 | -51.24465 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52f8a048-b9f2-3893-a82a-6fd3a9a31f31 | 3.46568 | -51.24517 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfcb4d7d-1ae1-3c03-a90c-be793c871be1 | 3.45296 | -51.27196 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22d910d1-3df3-3f70-b77c-df3c7eb08114 | 3.44965 | -51.27248 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77bc71c9-cf3e-3f8e-90b5-1dcb79c7c8e6 | 3.19208 | -51.30276 | 2024-10-28 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d3e43bf-73eb-37fe-aba1-d554b451cfa9 | 2.42038 | -51.41703 | 2024-10-28 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f473d1a-8c77-3414-8394-6ee2cf487bd4 | 1.36447 | -51.26118 | 2024-10-28 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
