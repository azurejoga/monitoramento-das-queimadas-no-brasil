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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d7758f4-bdea-3e59-a06b-6ccf7278f8d2 | -2.96283 | -49.06825 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdc2fc6c-85a7-327b-94c8-85a29d9f5f8f | -2.96253 | -49.06751 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f9dd70f-0d57-32e9-bd0c-90c72d1f125b | -2.92365 | -48.23316 | 2025-06-20 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3068fd18-6f2a-358b-a3e0-554713d22908 | -3.00723 | -46.71906 | 2025-06-20 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9b0406c-1e7b-3955-b1b9-4b9f1dbbcf3e | -3.04554 | -49.42725 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5131db0f-e518-3dff-a980-377e8ae73bae | -2.29116 | -48.57538 | 2025-06-20 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b35b45aa-b4ef-372d-8174-735005c24579 | -3.70353 | -48.86668 | 2025-06-20 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a057e10e-fb44-30bd-a61e-a7cbdcde11b7 | -3.03446 | -49.42952 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7158d115-d785-3afe-bb18-686698ce1ca4 | -3.03796 | -49.43005 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bdbe3329-7778-3f3a-be09-f117d1512050 | -4.8515 | -43.18888 | 2025-06-20 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de2f7d1c-adb7-39a0-89bb-8b28d4e688d4 | -16.3047 | -58.2676 | 2025-06-20 04:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| e61c06e9-eb1b-3ca8-93b3-23e32ea75980 | -10.4754 | -47.0325 | 2025-06-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 258.4 |
| f8bba951-edff-39c0-bdd0-d07f4d590aea | -10.4944 | -47.0302 | 2025-06-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1c05e1b2-d1aa-31ef-843a-eb6a977ab877 | -10.4564 | -47.0347 | 2025-06-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 612bf332-8eee-3873-96a3-b9874dee0dad | -10.456 | -47.0571 | 2025-06-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 473c7dda-3373-3032-9158-05a97b1af384 | -11.952 | -58.7376 | 2025-06-20 04:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| ba83e95d-b691-3b64-bd41-42591606ef2e | -10.475 | -47.0548 | 2025-06-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 2ce9309a-993b-330f-aca0-77ce2578db69 | -11.31657 | -45.20384 | 2025-06-20 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47b7a900-390a-3fb7-85b6-4e27eca8ca26 | -8.95911 | -47.97667 | 2025-06-20 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9777a7fe-6f8e-3d79-ad8c-11c471b07875 | -10.23309 | -54.29735 | 2025-06-20 04:51:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef78f72a-9342-3e2f-a0b2-b3949be95429 | -9.84587 | -44.69042 | 2025-06-20 04:51:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa4195ad-05f7-3b91-a929-a5a2e90464b5 | -9.30157 | -47.78996 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88b9fae4-baf5-372a-b674-5b53761fd1df | -10.47048 | -47.04875 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 8e029c78-624b-3777-bafa-4aa9843245ae | -6.16042 | -47.27113 | 2025-06-20 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae1fcccb-344a-3146-8f07-86bb7015874e | -11.16789 | -47.40221 | 2025-06-20 04:51:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 575a8265-dec4-3978-a86f-f9898ae25436 | -10.49465 | -47.03823 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1301081-40f7-3e13-8aa6-741a5ad2793b | -7.38901 | -44.56408 | 2025-06-20 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b27d10d-3a21-3091-8cb7-f376206841a5 | -11.81788 | -48.08074 | 2025-06-20 04:51:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67c0520c-6a7b-3568-ab27-4fe20f6d5c1a | -10.48693 | -47.02816 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 68a4af37-f1b6-3acf-9163-b0017c75eef2 | -9.84626 | -44.68731 | 2025-06-20 04:51:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca303159-0236-3cf0-a2cf-d5e17eed3a6e | -10.85936 | -53.7575 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36624b18-1236-3268-9a86-0a9d32b3fee4 | -10.82932 | -54.01378 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc5f17d9-5277-3192-8627-26ce7935a564 | -10.86157 | -53.765 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d1ffe83-5be8-316f-bbb0-58cedbfcd666 | -9.45941 | -57.85295 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a529eb7-cd5b-31dc-93c5-02747efead55 | -9.37551 | -47.63608 | 2025-06-20 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b1df8ef-ad26-3df7-8f4c-e3ee22fc9918 | -10.85664 | -53.77494 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a4770b7-1172-3a46-9288-105bf812a4a0 | -5.30379 | -55.97071 | 2025-06-20 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 462179d1-b778-3db3-91a0-7424c20dc46e | -12.21014 | -45.52621 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d52dc1d3-1731-3ae1-8012-2381f2ab05d5 | -7.01707 | -44.58968 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c538f2a7-2dcc-35f2-8a69-3f43318add79 | -12.20975 | -45.52928 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a700a301-0296-338f-9770-96b588d4d073 | -10.66045 | -49.36513 | 2025-06-20 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6dfed873-620c-322a-91ac-1d8f4dcd4774 | -9.30844 | -44.83244 | 2025-06-20 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf44badc-4816-3cf3-a0fe-fdf1be1ff4a2 | -12.21769 | -45.53925 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fdbe96f-1a86-3f95-9230-30ba4e79c890 | -11.46986 | -47.28887 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfca447b-6002-3fc3-9be6-f7cbe30b9655 | -10.36993 | -57.50757 | 2025-06-20 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f2737b4f-c15b-39a1-9a53-8b1d8f87d4f0 | -7.38871 | -45.40366 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1288f95-a40c-3d09-bcec-61669815ebf5 | -10.48123 | -47.0366 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 60e30352-fe14-3791-8f52-25833a18d288 | -10.47555 | -47.0449 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f3272544-d5e8-3f06-9d26-76d4ee4893fe | -9.95201 | -46.62867 | 2025-06-20 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f81d84d5-47de-3286-87c5-3b4acb2809c9 | -8.26016 | -44.96101 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0da85bfc-1f5f-3617-9b3b-8a47f23fee87 | -9.46107 | -57.84314 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5a5c62f6-e84b-3009-b489-7134409ddb7a | -10.46038 | -47.05622 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| e08024cc-63f5-3ffe-b2c3-38fdf0a306df | -9.3183 | -47.79192 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d653d4a7-d8a3-3e80-ace5-f4a45058757b | -12.20792 | -45.53482 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9a8b8a3-bebe-33c9-9424-d416c295843b | -10.53415 | -46.64719 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 976fa918-0c80-3615-9c98-b5d3757db173 | -10.24269 | -47.45925 | 2025-06-20 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57cbebd3-0d54-3313-acd7-cc261ab302e5 | -7.13808 | -43.28272 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9f21f39-3206-37d8-a77b-b7bee242e318 | -10.72976 | -49.55783 | 2025-06-20 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b23057e-6cda-35c3-962e-a6c8e1345b7d | -10.5035 | -47.00707 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09a4429c-62f4-3a29-b690-6ad46f759ae8 | -8.98866 | -49.87183 | 2025-06-20 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f6000c5-31e7-3efa-8f63-4ba576f31cf6 | -9.45335 | -57.8419 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f123e5f3-2b21-31c8-8677-4006b08d832c | -8.87264 | -47.27294 | 2025-06-20 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b5ded37-7ad0-303b-aaa5-e7ddcc403193 | -10.52957 | -46.64652 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c95631f6-35bb-3c1f-937e-e0fbbcd36b28 | -7.21698 | -43.0745 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e7c02697-8a75-3622-880d-2a22039f9b08 | -7.02048 | -44.60209 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffe4bfc2-7860-380b-9720-cee4dd8e960c | -10.48836 | -47.05095 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7152eab9-d7a4-3b0a-88e7-8e8b4ced34ea | -10.08093 | -52.74443 | 2025-06-20 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34b73187-6ebd-30af-bfff-df40bcb05f4f | -12.2235 | -45.53389 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5de4d6a2-0515-3458-a2a4-83b6abf70da4 | -10.46483 | -47.05689 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 6471ac29-1ccf-3e2f-818b-0a956efda0b4 | -11.47315 | -47.29842 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0b2a5e2-2af9-34a2-a4ac-6618c582f178 | -7.70511 | -49.3901 | 2025-06-20 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39b409a5-2455-3572-abd0-f0c3ee8200f8 | -6.84422 | -42.79555 | 2025-06-20 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83922629-bfeb-3693-bc02-cc847d4282b5 | -9.46272 | -57.8334 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c6cdf36-2c5f-3e90-aa15-f2d7492b67cc | -9.49258 | -56.08633 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76147f12-d4a9-36d3-a391-00379a63ef74 | -9.30902 | -44.72645 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e1d328f-c7be-3548-9cc1-10e3bf67921a | -7.267 | -45.3617 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d518b608-7e02-3e68-a60b-d01af6f8b98b | -10.41946 | -47.09075 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5db80e2e-3cf6-3852-b135-809be04ad61d | -10.45473 | -47.06441 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7ff6a021-dfae-3153-a720-e2b4163530ec | -10.86267 | -53.75803 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 165ace70-70cd-36b2-9fc1-c0a808cdb2ca | -9.37816 | -63.42943 | 2025-06-20 04:51:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7a80a01-1274-39bd-903e-9bb3d290d1e2 | -10.48246 | -47.02753 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 9445d5a6-73bb-31a9-92e0-4b9db895d79a | -11.15058 | -46.65395 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5efb90f7-cc15-3acf-83b7-367ea17a0f06 | -8.26595 | -44.95581 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16cfabb8-9892-37b3-b347-ce352832c8ee | -10.53851 | -46.93652 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fec70f4-cddc-345a-bd9b-c88a635e0693 | -10.65977 | -49.36995 | 2025-06-20 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b401402c-7898-3840-871a-d1ae484a1356 | -9.47921 | -56.08004 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4dadd27f-e108-3be7-a1d2-d47921b7b425 | -6.45095 | -44.79681 | 2025-06-20 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5afc012b-dbeb-37ca-bc0f-2ec43ea3da4d | -10.83593 | -54.01483 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcd17511-137b-3f4c-9727-a5016ad475b2 | -5.49127 | -42.14487 | 2025-06-20 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e6c5b950-c762-35b6-b995-89ed47ab2aad | -9.31681 | -44.72643 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f6b4ac59-5e59-39ff-af81-dd2785e81fe2 | -9.2983 | -44.72828 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14aedc69-a4e0-37eb-bbcf-eaea6544f893 | -10.36247 | -57.50631 | 2025-06-20 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40fd615b-37f1-30ea-b73b-1b0069401f73 | -7.90062 | -47.52314 | 2025-06-20 04:51:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98858715-c4c3-3273-9313-a6d7e1516fdb | -5.60778 | -44.91561 | 2025-06-20 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b9ef7c7-7041-36c7-8ac7-70762734c96d | -9.30428 | -44.72273 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a4b68a-34be-3cbc-8c7c-b606fc41a844 | -7.75885 | -47.61121 | 2025-06-20 04:51:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d5de71d-b536-33c2-b361-7b5ae0752bb6 | -11.27497 | -52.46899 | 2025-06-20 04:51:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 256ed2d5-2b8e-36f9-b811-eaf51f33afb2 | -11.47045 | -47.28439 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd4423d4-e9d9-3bcd-b04a-3c1c2b06d0c1 | -7.23959 | -44.68232 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48e1eb40-70e8-3cd9-82c9-d5b8145e198b | -3.22458 | -54.86649 | 2025-06-20 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README17.md)
