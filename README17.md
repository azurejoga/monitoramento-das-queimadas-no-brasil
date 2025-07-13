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
| ffb0232c-7355-3ff4-835b-8500c06133c6 | -7.324 | -44.0145 | 2025-07-13 12:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ba8e7fce-82a0-34ac-89df-910a191e4062 | -7.3428 | -44.0127 | 2025-07-13 13:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| ea78ec43-e202-3601-ad48-de52b283424e | -7.3237 | -44.0377 | 2025-07-13 13:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 67aba0ab-8402-346a-a28c-d6ecb4ad8241 | -7.0384 | -44.341 | 2025-07-13 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0f82fa95-bbda-3b04-ae3b-f56c227b4ffc | -6.4279 | -45.3505 | 2025-07-13 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5c3499c3-3c32-335f-8ae4-bc285ef2c7b5 | -4.5429 | -48.0151 | 2025-07-13 13:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 30e072d6-d8dc-3af3-bcb2-13a4beca1e5b | -7.0381 | -44.364 | 2025-07-13 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 54f7b3dd-b197-3b68-bd82-0b28159c2e00 | -7.324 | -44.0145 | 2025-07-13 13:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| e4b1af76-49ad-341d-816a-9ec402768f02 | -4.5429 | -48.0151 | 2025-07-13 13:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 1e5db8c8-db61-3916-ae35-03988df6c2c9 | -7.0381 | -44.364 | 2025-07-13 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 571.1 |
| 89aae9e9-0935-3173-b57e-fad17a399781 | -6.4848 | -45.2781 | 2025-07-13 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 81dff13d-ac4d-3582-addc-987b9247cf4e | -12.439 | -50.4894 | 2025-07-13 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 30dcc189-1977-3d35-9bb7-cc8cca8006bf | -7.324 | -44.0145 | 2025-07-13 13:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ba1ea9ad-992b-3074-9229-5bb262082ce1 | -7.0572 | -44.3393 | 2025-07-13 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b7711975-a3a9-3672-a4bb-5476d3c11726 | -7.0384 | -44.341 | 2025-07-13 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 213.7 |
| f542574d-7f32-344b-b802-2cafd397d79c | -12.4393 | -50.4678 | 2025-07-13 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b53d12ae-2621-3783-97c9-0e79ec69a298 | -6.485 | -45.2554 | 2025-07-13 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 90fd9473-aeeb-3f97-869c-c3abbd23d339 | -7.2906 | -45.3229 | 2025-07-13 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a874e6b9-d026-3f9b-a826-684656478f41 | -7.2908 | -45.3002 | 2025-07-13 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 11d9f033-30cb-32a7-b681-9efba323d773 | -4.5243 | -48.016 | 2025-07-13 13:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| ef12d185-3c97-3a82-aea3-9f65a935b8dd | -7.324 | -44.0145 | 2025-07-13 13:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 348.4 |
| 04621be7-1572-3e56-8e64-90e6884ecfb2 | -6.3571 | -44.9251 | 2025-07-13 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 94c1c006-d1cd-301b-8ae5-b4e19b548bbf | -7.0572 | -44.3393 | 2025-07-13 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 09fab4af-2d04-3a21-a462-d153f94500a7 | -7.0384 | -44.341 | 2025-07-13 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 5b0aaa27-5e9b-3982-a569-7698328584b3 | -7.2718 | -45.3246 | 2025-07-13 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d911389e-8a49-3aa2-94ed-3d150d3bf00d | -7.3091 | -45.3439 | 2025-07-13 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6442e69c-aba0-33b6-a420-b634dd3e4597 | -4.5429 | -48.0151 | 2025-07-13 13:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| c4399703-7af6-3fe3-b48d-504609c532d0 | -7.3094 | -45.3213 | 2025-07-13 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9ff8f17a-14a3-3224-a4a4-5b334563833d | -7.3237 | -44.0377 | 2025-07-13 13:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 398.6 |
| c85fefc7-a826-36e2-98a0-d474cd607ba3 | -12.439 | -50.4894 | 2025-07-13 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| fe438a1f-7911-3177-ab34-7b686345d5d8 | -8.3299 | -44.9261 | 2025-07-13 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 59d5154d-5e1d-377c-aa75-de41976a6982 | -7.0381 | -44.364 | 2025-07-13 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 404.0 |
| f0251959-dd23-3480-b888-745c9279e6df | -12.4393 | -50.4678 | 2025-07-13 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d71da844-7d2a-3de5-86a5-4ba298db9944 | -6.3759 | -44.9236 | 2025-07-13 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| ea1fe67e-8860-37ae-bd23-f566b4933106 | -7.3428 | -44.0127 | 2025-07-13 13:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 250.9 |
| 0c0707c2-1192-388d-9143-d0bb88c15032 | -6.485 | -45.2554 | 2025-07-13 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 6303d954-27e2-3932-829a-c97971c3f5cf | -7.324 | -44.0145 | 2025-07-13 13:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| c04801fd-b97c-388f-88f4-63668c285c86 | -7.2908 | -45.3002 | 2025-07-13 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e00c7a9f-4141-3d4c-8a1c-009818b7b0e7 | -12.439 | -50.4894 | 2025-07-13 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d3f86770-93b6-3da7-b254-126b0c5749c4 | -4.5429 | -48.0151 | 2025-07-13 13:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f1320445-9959-3930-9eec-bcd75733eb3c | -6.4848 | -45.2781 | 2025-07-13 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 239.8 |
| 3f7f46b8-bd5f-3eb4-bbc3-d83ac97be186 | -6.4661 | -45.2796 | 2025-07-13 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 171.8 |
| b3c1f42c-38f3-3c9d-90a5-5ca8abaa4afd | -4.5243 | -48.016 | 2025-07-13 13:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 51a0562a-e25a-37ef-a1b3-85e6ad5da88d | -12.4393 | -50.4678 | 2025-07-13 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9fc21488-6706-3f35-a2cb-42aa7b61653d | -7.0384 | -44.341 | 2025-07-13 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| ad7821bb-5c68-348a-8049-8c11175fe77c | -7.3237 | -44.0377 | 2025-07-13 13:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 6e0cda73-ba71-3d5b-baa6-31bf313ad3f6 | -7.0381 | -44.364 | 2025-07-13 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 262.0 |
| a2affd3a-cafa-3377-b38f-367d2892d7f0 | -7.3094 | -45.3213 | 2025-07-13 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 532e81d7-a391-3e02-b527-631d43c067c5 | -6.3759 | -44.9236 | 2025-07-13 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e9410ec7-0a5f-36be-820f-032806f408f1 | -6.4661 | -45.2796 | 2025-07-13 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 9851a791-9691-3b99-a5c8-31b340dd2803 | -6.4848 | -45.2781 | 2025-07-13 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 40967f60-42ce-3a03-bacd-d7fff683835e | -10.5776 | -49.1316 | 2025-07-13 13:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 911885a9-42dd-3902-a9f0-22655813a99c | -12.4393 | -50.4678 | 2025-07-13 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 8f373f3b-44da-3463-8d1e-95f7c60c0f28 | -7.3091 | -45.3439 | 2025-07-13 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 193da781-2a97-3a72-ab71-3b0d02e0dbd4 | -6.4279 | -45.3505 | 2025-07-13 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 42eae5df-80e4-31c8-a292-37f49024ba92 | -7.3094 | -45.3213 | 2025-07-13 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 2442839c-ddb9-3d34-b0fe-2a96bb8c8f06 | -12.439 | -50.4894 | 2025-07-13 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 1f0fbfd6-058a-3895-b4d1-4793c526b6ae | -6.4659 | -45.3022 | 2025-07-13 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| a958904f-f4ea-376d-83de-b247a2957054 | -6.485 | -45.2554 | 2025-07-13 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 126f13ee-c502-323d-b9a6-13a44edb8e3d | -4.5243 | -48.016 | 2025-07-13 13:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 7643775e-a9e8-3ac5-b062-d6c6ad087731 | -7.0384 | -44.341 | 2025-07-13 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 56f84d95-792f-3083-bca6-94e87dd6a918 | -7.0381 | -44.364 | 2025-07-13 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 238.6 |
| bceb2ea7-4719-3206-adb8-2dcd9ee5b7a9 | -4.5429 | -48.0151 | 2025-07-13 13:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 3c809640-3954-3a03-98aa-6caa1b37c429 | -6.4848 | -45.2781 | 2025-07-13 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 08fdf28f-971e-3546-83ac-48b609e4484b | -7.0381 | -44.364 | 2025-07-13 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 203.2 |
| cc8a3573-498b-300c-a130-0bd7e9b24f7a | -10.5779 | -49.1098 | 2025-07-13 13:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 9c5f2094-e19b-37e0-900c-e565733aff5e | -8.9213 | -47.3374 | 2025-07-13 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 78109dfc-30ea-3ac5-9f68-6a789b6aea9c | -4.5243 | -48.016 | 2025-07-13 13:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| ff2c7700-8113-3358-9b54-2e5ddaa5170e | -7.3091 | -45.3439 | 2025-07-13 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 2373e4b0-0a45-3653-a178-8d7950074798 | -12.439 | -50.4894 | 2025-07-13 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 15d78fbd-b587-33af-957e-f39fafe3db7f | -7.3094 | -45.3213 | 2025-07-13 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8c13cef7-ce32-3f17-a195-67d2d928f302 | -4.5429 | -48.0151 | 2025-07-13 13:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0a1f7347-c5af-301f-8ab3-00dc5fd2fe01 | -12.4393 | -50.4678 | 2025-07-13 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9d2f86b9-b55e-3d6a-8a99-56227dd3a8e1 | -10.5776 | -49.1316 | 2025-07-13 13:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2afd5c0d-d661-3637-a6bf-bf66960c6e63 | -7.0384 | -44.341 | 2025-07-13 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 5c6e67b7-aba9-33c0-9852-298d7def0c92 | -10.5779 | -49.1098 | 2025-07-13 14:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1e3891b2-3540-35c0-af79-835f360718f6 | -7.0384 | -44.341 | 2025-07-13 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 0487b886-ffa8-355e-9f20-9fa933c9fff3 | -7.3091 | -45.3439 | 2025-07-13 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f128a64e-a12f-3970-9cf2-73980cc8ecc7 | -10.5776 | -49.1316 | 2025-07-13 14:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 633a43fa-e0ae-3892-9c8e-241e5ad86f03 | -12.4393 | -50.4678 | 2025-07-13 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d36b29c1-a143-385b-abbc-2b552ed5d555 | -6.4848 | -45.2781 | 2025-07-13 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| fa604656-0112-33e0-8d9c-beb212958d85 | -6.4659 | -45.3022 | 2025-07-13 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 2bdd42e8-d165-3add-b468-916b5ed33153 | -8.9213 | -47.3374 | 2025-07-13 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| bca593e7-0e6f-3ea0-a911-5e5e4a74a92d | -7.0381 | -44.364 | 2025-07-13 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 261.3 |
| 9ed33363-6579-38ae-ac65-f8b4e684964f | -10.5028 | -46.4691 | 2025-07-13 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 973fc659-8152-3e26-a8bd-52fee4e75a37 | -6.4661 | -45.2796 | 2025-07-13 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 545c68af-b69b-392a-bac4-0c6c4585f697 | -4.5243 | -48.016 | 2025-07-13 14:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cf2da205-463a-30ef-8a3b-b5ed1726a90f | -4.5429 | -48.0151 | 2025-07-13 14:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e025a4f3-c622-3bbc-9923-e143c9bb0de2 | -6.4275 | -45.3957 | 2025-07-13 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 32452675-09cb-3f72-8937-60c0061208dd | -12.439 | -50.4894 | 2025-07-13 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| a715c947-eccb-3ff6-b358-f7f1c65b9ce8 | -7.3237 | -44.0377 | 2025-07-13 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| d5d986ea-9adf-3de8-b488-d754d5351fba | -12.439 | -50.4894 | 2025-07-13 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| da3035e3-84e4-35b1-a55b-cb0abb4bf5fe | -6.4848 | -45.2781 | 2025-07-13 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 290.0 |
| 21ddf1e6-ddd6-3c88-8579-1274d0ec4102 | -6.4661 | -45.2796 | 2025-07-13 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 207.6 |
| feecf897-8499-39a7-9a28-af768e79932f | -8.9213 | -47.3374 | 2025-07-13 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b8edbea5-5007-34d2-95a6-043ab2309b6a | -6.1238 | -45.869 | 2025-07-13 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 82dda90c-a3c6-31c3-a141-5a1326491e59 | -4.5429 | -48.0151 | 2025-07-13 14:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 7a44394a-5558-3cb2-bbdf-e88acf83561c | -7.0572 | -44.3393 | 2025-07-13 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| fd6de5bc-2ca4-3bb7-93bb-4a6d6a2547cf | -7.3091 | -45.3439 | 2025-07-13 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 3f41228c-0944-359c-b35b-be28f696c53f | -6.1051 | -45.8704 | 2025-07-13 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |


[Clique aqui para ver as próximas entradas](README18.md)
