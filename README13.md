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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8710fe1d-d45c-3419-bbf4-0db87fc6b7c8 | -3.44877 | -50.29265 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 7f5fb8e0-b08a-3b75-aa93-a94994c8ebee | -2.98523 | -53.8973 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dd737981-d9a5-39ab-80d0-62ea33830e32 | -2.83248 | -54.12456 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 22fd84d7-3b9a-3c89-95a6-aab28c8d6092 | -3.68408 | -49.9318 | 2024-11-27 01:09:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 28c0b20a-73f6-30db-94c5-41f11f30317f | -2.79362 | -49.2088 | 2024-11-27 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f3f49eae-c157-30ee-b948-c8b15b26650d | -3.17639 | -48.44031 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 7605ec0e-6f0b-36f7-a9ca-8a2942d71f14 | -1.65621 | -52.42184 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f17f7612-2d61-3aeb-b076-f2aad9ea3963 | -2.22859 | -53.68834 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 005af145-231d-3bfe-b820-feb729791267 | -3.40328 | -53.20032 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 557ea659-9631-3493-8652-a9ab56967fff | -1.0872 | -53.36479 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a2d44f7b-051a-3c55-892b-6ed4585bc7e1 | -2.53313 | -47.32632 | 2024-11-27 01:09:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| d19ea1d8-f12b-3a7d-8ad1-4595ed2ff643 | -2.80163 | -53.04317 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 44bd225b-2cc4-339b-8281-ecf5c72ba352 | -1.38211 | -53.62816 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4079578-74bf-3080-80ef-69e563275199 | -2.82113 | -51.79703 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 73daa298-a69a-3d3c-a351-194099a9a254 | -3.56847 | -54.65432 | 2024-11-27 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d0aec0cd-82fe-39cb-870d-e75d3f89bc12 | -3.10821 | -53.25998 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 515.1 |
| 01fc1522-3750-3827-b110-3e6c07c5964b | -1.65495 | -52.41284 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8456eecf-0b67-303e-8c54-0f52c11bed39 | -2.86569 | -46.81359 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| ca960a36-ef6e-3bde-ba96-8f2bcd53a0b2 | -2.99177 | -45.45173 | 2024-11-27 01:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b7d528f8-1a1f-3ae7-840c-07d55d175295 | -3.03807 | -48.51031 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 1dfd101d-221a-343f-b25d-3a9a462f9bd3 | -3.34101 | -53.74059 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67fb53d5-6f63-32cc-bffb-ef097bfce2ee | -1.89734 | -50.5981 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2aaadc17-5214-3010-8a0c-37d0b8288ba5 | -1.62121 | -52.57026 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9a6e69bb-72c9-30d4-849d-697a8f7b9e04 | -2.49296 | -54.53445 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2d043594-a2bc-3908-9317-ea0f68dd0894 | -3.31546 | -53.75336 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 01d2b7ff-e3de-3eed-addf-19360d434767 | -2.60933 | -53.97438 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 41f25270-50f5-34af-bf1f-181419054cfa | -2.90498 | -54.18293 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c098ca9-f041-3ef4-acde-f40ed4318614 | -3.00589 | -45.44963 | 2024-11-27 01:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| dc231f8e-1ce6-3f0c-bb76-70ed4e20017b | -3.10505 | -53.10759 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dcdbe4f0-8762-35e0-acb6-b986e2501640 | -3.20831 | -51.33933 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc84c6b2-66cd-3054-8da7-48cd0c86cbf1 | -3.51183 | -54.63871 | 2024-11-27 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8aeb05d1-fd7c-3c0e-8f2e-c51f13e8c904 | -1.79449 | -52.75134 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f352318c-fa0d-3fff-a7c5-593e59fade2e | -2.80093 | -52.90851 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| f084e274-a3cf-3df7-8f21-ce251e4d42fe | -2.44253 | -50.40728 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c537972-338a-3da7-841b-758d83f59f34 | -2.80973 | -54.02603 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 66f103d3-9578-3730-abf3-f570bf71fc9e | -2.62671 | -54.30231 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 87d66e6a-7d08-38c8-955f-bf747a6bab78 | -3.04112 | -54.03687 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f1ee7b0e-94f4-36d1-a588-8d3b58b73628 | -2.6828 | -45.64636 | 2024-11-27 01:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 8705161a-9d27-3d22-9599-7f5fb4a5a805 | -1.70969 | -52.47838 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8de75ff2-7b83-3992-a97b-9c46c0500a6c | -1.2401 | -51.61788 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 327e5da4-88f8-3225-93a8-db257baca046 | -1.48856 | -52.54016 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf8b8569-cd73-3734-8c91-0546d49037e2 | -2.83001 | -46.84481 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 478edf50-b397-349e-9628-1411e3b3429a | -2.95687 | -51.06331 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 922d0a76-7ac0-34d5-a304-217e51e5ee29 | -1.59768 | -52.27062 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 614c2388-b4c1-359b-adb2-5b9ac57bfa5a | -2.82722 | -46.82571 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 35429611-4a48-3f40-ac4e-c40c974a9ef5 | -2.18573 | -53.78218 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| dbfdf738-7988-34b1-99b6-5496e06c8bfb | -1.44989 | -52.59747 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 270efc40-c4ce-3ea9-89e1-d9026bfba557 | -2.99132 | -49.59161 | 2024-11-27 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 19439b33-c886-39b9-9505-d5dfc0c1a754 | -3.11463 | -51.26195 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c6b5f518-6e87-3fa3-8264-620677ff8c8e | -1.66779 | -52.7091 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3f9b9b80-e2b7-3e1c-bf97-539ec82f2318 | -2.8547 | -53.9553 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 31208ca8-a65a-3d4a-bb3c-f3b94ecce4e9 | -2.86247 | -46.80086 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 89ea628a-3354-3eeb-be3f-12accf82709d | -1.79325 | -52.74247 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 6410adfe-3d08-3bc6-87ac-45cb3dd0fea5 | -2.43434 | -50.41938 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 30329f95-66f7-323e-bae4-9af9e1223c48 | -2.18938 | -53.66674 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3fa4a50b-3303-3965-a63c-d2caf77412ff | -3.0575 | -53.28513 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 76394e71-3626-318e-b6c9-a571ba3db490 | -3.43308 | -54.54299 | 2024-11-27 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f5c20543-9a92-3761-9c00-c07cd5922862 | -0.805 | -53.06365 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9accc790-b291-3238-bff6-e19865154d94 | -3.09945 | -50.35671 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9c0c094f-29e9-36f3-b160-46d66bbabe05 | -2.32618 | -53.85919 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fef081f9-346a-36f5-8d97-5edd04ba2d1f | -3.05362 | -53.72639 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| be6e3524-0c9a-3247-b918-b50b5d905197 | -2.09879 | -53.35272 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f8604e4-a36d-39bb-9b56-5756c5b3ccd9 | -3.02568 | -54.05756 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| be86c69b-744f-36c0-be5f-02294b87ee2d | -3.70975 | -47.12542 | 2024-11-27 01:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c241869a-895a-3d4a-9128-561a0b5bcfd9 | -2.99538 | -45.47611 | 2024-11-27 01:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 56f7d457-48bd-3b02-b7b5-b8cec793716b | -2.94155 | -51.54034 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0fb45f80-2147-39e3-ba22-4744647204f4 | -2.62049 | -52.53413 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c4369e9f-22d1-3a6e-805b-daaa3d51cc74 | -1.94919 | -45.73087 | 2024-11-27 01:09:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 252.7 |
| 84b38db9-4ec4-3367-9508-c9db3218e9c5 | -1.44864 | -52.58854 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c56394ea-131e-392b-a75e-d1c680a80c08 | -2.64281 | -54.28438 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f28d1afe-19d0-3897-81df-57fc3354ce25 | -3.7067 | -51.80573 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a9be082a-b7ca-3fee-b6c1-8c8444c812ba | -2.99426 | -53.36336 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5a9c4a9c-7328-3462-9f52-81bb619b9ec7 | -3.54619 | -50.4012 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 538e14e0-eaac-31c5-8d4d-ef8551dc3298 | -3.51049 | -54.62916 | 2024-11-27 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5623146b-e3aa-3d89-a15f-9f9646c31a09 | -2.61004 | -54.24862 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 15d99234-47c1-33a9-aff9-14fc92c58478 | -3.23254 | -54.22147 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f3ec5ac4-6e26-371f-b3cc-75dc115a7512 | -1.66767 | -52.43855 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 747a9e29-47ed-319a-82fb-26adb416d16f | -1.26904 | -52.15845 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a00939b9-6d36-3b09-a909-a1906417358d | -3.32836 | -53.71494 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7b420287-8934-337a-a8c3-f8f8638677a2 | -3.28026 | -48.75636 | 2024-11-27 01:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c66dccb5-2d9b-3fc0-b64e-92e0234a2409 | -1.9894 | -53.29326 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 55a39115-19b9-3941-983f-72faff078c32 | -3.52092 | -50.22204 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9cca1d72-3775-3c59-97d6-a1820e79c206 | -3.09935 | -53.26123 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 328.4 |
| 101336ce-a3d2-33d7-9f49-b132485c2c26 | -1.6407 | -52.4487 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| ce9ae655-fbe6-3987-ace9-eed063c47194 | -3.10623 | -48.03049 | 2024-11-27 01:09:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e5863cce-c475-31a0-b6ab-c368bcb5b5d0 | -1.564 | -51.22938 | 2024-11-27 01:09:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b720e011-ed45-39b9-a559-fbdeb480db5d | -3.10058 | -53.27006 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 63f45a67-edbc-3f97-98a1-49bc59661fa0 | -2.82891 | -54.03257 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 71d58644-a906-386a-9d3f-aa5259afaf3f | -3.71569 | -51.80444 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6830d8d2-58d2-34a1-864e-16ea2ce7b77e | -3.37441 | -50.11754 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 16a6418a-ea86-3263-81db-78ab6a47ca99 | -3.12994 | -50.27037 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 452c32e2-fbf1-30a2-accc-bd5ff3e178e4 | -2.1709 | -53.27345 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b6db457-0f3b-3452-8e1e-3759dc27bc0e | -2.60474 | -51.83064 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d04cb502-9320-36ef-84b6-4dee40f517c8 | -3.45841 | -50.2912 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 632105fe-b2f9-30a2-8462-fe4fa7de8d3c | -2.92127 | -53.90339 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4e840b87-b01c-3a9c-b5e2-ad6af285594e | -3.11332 | -53.7635 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e38d725f-7a16-3b15-8b48-971efbc9e2a2 | -1.67019 | -52.45652 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| c3ddb5b7-46e3-3500-86fd-86aef4f4397b | -3.08147 | -54.12734 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 911d56bd-6d50-3a87-8f9d-4561a29a1a5f | -1.64235 | -52.72176 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 97388d9b-5210-398e-9b9f-f01cd5041289 | -2.60485 | -54.27734 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README14.md)
