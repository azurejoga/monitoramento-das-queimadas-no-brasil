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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc158ca5-3bb7-3c9b-81da-5866a0b3f8a1 | -3.2385 | -54.2431 | 2024-11-22 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 210.4 |
| 3eaa1eee-bce2-3e05-9435-836f16885433 | -1.2041 | -51.9683 | 2024-11-22 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 44bd071d-a17e-3f27-8f0a-716f67d0a88a | -3.2768 | -53.8199 | 2024-11-22 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| fa789a0c-0e70-3b7f-97cf-4c25d5af3f5d | -1.1103 | -53.3953 | 2024-11-22 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 85ad29e5-ff52-36f5-ab6f-7a52bde4ba8f | -3.2384 | -54.2632 | 2024-11-22 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 41902edc-f806-3d0b-9b40-12734f30bee9 | -15.87482 | -53.26793 | 2024-11-22 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57091295-a6b2-34b5-aa0b-4479da61dd40 | -16.44125 | -52.56457 | 2024-11-22 04:40:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d350452-51fc-31ad-989b-e287a9f53010 | -16.88689 | -42.84028 | 2024-11-22 04:40:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e16566b9-75ef-3235-b890-418f032a0b12 | -14.53048 | -50.81411 | 2024-11-22 04:40:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6511d09e-b220-3c48-b56a-e87be4ae4011 | -15.87081 | -53.27113 | 2024-11-22 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3359af70-b62f-3617-a8eb-bb94242d5efa | -14.59601 | -50.74048 | 2024-11-22 04:40:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38c8aee3-a40f-3fbd-aa45-e12b312618f3 | -17.44853 | -55.84995 | 2024-11-22 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 7286cf04-922e-3473-b9bf-a43028d3191b | -14.52717 | -50.81357 | 2024-11-22 04:40:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 643f3fdd-7515-3290-ada7-c5bdef4e4589 | -16.88725 | -42.8371 | 2024-11-22 04:40:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 466001fc-e697-3334-8c51-2b1ffe80a517 | -16.67342 | -56.47898 | 2024-11-22 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3a558aa9-f955-3799-8130-49b9cd5b1497 | -15.8742 | -53.27172 | 2024-11-22 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48db87c3-a01a-3e17-b2f5-d0630ff2545b | -19.44482 | -42.637 | 2024-11-22 04:40:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fd727f8b-6f47-338d-a1ca-a1aa83d98c11 | -14.2598 | -46.33211 | 2024-11-22 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e297b9f5-5c9b-3d36-bd41-5777a90ff91e | -15.56947 | -47.85622 | 2024-11-22 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67b6a455-2f2f-3c3f-a260-a121bfd74517 | -16.44066 | -52.5682 | 2024-11-22 04:40:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 136ca632-fc58-32f7-8864-be24e05fdecb | -25.77395 | -52.9015 | 2024-11-22 04:42:00 | NOAA-20 | SÃO JORGE D'OESTE | PARANÁ | Brasil | 4125209 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 13c65716-e0f8-3b26-a1e0-3d84fff325f0 | -25.77003 | -52.90476 | 2024-11-22 04:42:00 | NOAA-20 | SÃO JORGE D'OESTE | PARANÁ | Brasil | 4125209 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| d686d1d6-8cfa-3bcf-baa3-f1a94b0d6796 | -3.2385 | -54.2431 | 2024-11-22 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 207.9 |
| 0bf41ac3-32e7-3eff-a3d0-b630208a154f | -1.1287 | -53.3951 | 2024-11-22 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 66b6f8c3-d2c7-32d4-8f52-9c853f8a071b | -3.2569 | -54.2426 | 2024-11-22 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| d5a80277-3c67-31ab-aa65-e9457830fcad | -3.2384 | -54.2632 | 2024-11-22 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| ef96e21e-0bc8-33dd-a054-e7b378297ce1 | -3.2386 | -54.223 | 2024-11-22 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d805b133-6d36-3bef-9877-89408c22e17a | -3.22 | -54.2636 | 2024-11-22 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2d1b36db-4833-300a-9888-43990cb46a55 | -3.2201 | -54.2436 | 2024-11-22 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 36944dfb-2906-3065-97ed-13e8a38089fc | -1.1103 | -53.3953 | 2024-11-22 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 3638d5e1-1178-394e-bb61-bc1583da83d6 | -1.2041 | -51.9478 | 2024-11-22 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b52a52cc-4398-30b0-b0a3-a6661a82e17d | -3.8719 | -52.3589 | 2024-11-22 04:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| fb12f34f-3cc6-3dcf-92d1-7548ed0ebeff | -3.8535 | -52.3596 | 2024-11-22 04:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| bc1ea53b-4c95-3caa-968d-3f5e0cb696ed | -3.3451 | -50.5126 | 2024-11-22 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 3d7171b5-8a2a-39bf-935b-a1ddb99d1a42 | -3.2768 | -53.8199 | 2024-11-22 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 68754af9-417a-3de1-9612-291579d90218 | -3.2569 | -54.2426 | 2024-11-22 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8fac8615-f81c-3b2d-b56d-31a5748c50bd | -3.2768 | -53.8199 | 2024-11-22 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9e2b454d-898b-336f-9319-fb39a6e4e78c | -3.8536 | -52.3391 | 2024-11-22 05:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ebc9b9e0-0ca5-3ff1-8fae-4319650b158b | -3.2201 | -54.2436 | 2024-11-22 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| aebed3e8-42b2-3669-a41e-aa54add1efc4 | -3.8719 | -52.3589 | 2024-11-22 05:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c1b5178b-891d-3286-83bd-c1591df923e7 | -1.1287 | -53.3951 | 2024-11-22 05:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 1fd72623-c87f-3353-98fa-900ce644879c | -1.2041 | -51.9478 | 2024-11-22 05:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 27c8c898-ace1-3c11-868b-d21e026c82f4 | -3.5159 | -53.8132 | 2024-11-22 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 612ddb08-5131-341b-8a39-d4a8008304b3 | -3.4975 | -53.8137 | 2024-11-22 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1c2506bf-70b7-32c6-9c4e-dcecc550beda | -3.2386 | -54.223 | 2024-11-22 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e12d9bee-836f-3f9a-9ab1-f33f8a8c2d25 | -3.22 | -54.2636 | 2024-11-22 05:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a3b2ba57-d885-3802-a701-fc851fea3acc | -3.2384 | -54.2632 | 2024-11-22 05:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 7ab10666-50fb-36fa-9d90-5ad7a080e06f | -1.8106 | -52.1652 | 2024-11-22 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f3cf8176-d420-3480-b229-242189af73b6 | -3.2385 | -54.2431 | 2024-11-22 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 199.3 |
| 4d17c793-6d40-3d24-9980-8e9f6d246aad | -3.8535 | -52.3596 | 2024-11-22 05:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 39ba68e4-0e72-3206-a0a5-ddbdf7bbe75f | -3.2569 | -54.2426 | 2024-11-22 05:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 47d25670-f875-3e23-ba77-d894e9feb3d2 | -3.2385 | -54.2431 | 2024-11-22 05:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 1f6c795c-1dc1-3505-ac9c-8d66ce7fc3ca | -1.1287 | -53.3951 | 2024-11-22 05:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 3c987e64-cdb6-3f13-829b-aec1e31dfa38 | -3.2384 | -54.2632 | 2024-11-22 05:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 26567137-5c14-3b12-9384-e3bdde874afd | -4.0131 | -49.9207 | 2024-11-22 05:10:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e2a09ead-677f-3ca4-a642-6330571cfccb | -3.2768 | -53.8199 | 2024-11-22 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 1dad6cc1-90cd-3253-aecc-c8fa560e96ef | -1.8106 | -52.1652 | 2024-11-22 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| ef48aa53-e56e-3a7e-97ed-f8401ea40f1c | -3.8535 | -52.3596 | 2024-11-22 05:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 6a35094c-015e-3371-8f3f-6d254f3ddc49 | -3.2201 | -54.2436 | 2024-11-22 05:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| c20fd4f6-c295-37c4-963c-6afae5a646cf | -3.2386 | -54.223 | 2024-11-22 05:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 97eb1f4b-e2a6-3d0f-919c-b42b604a32c5 | -3.22 | -54.2636 | 2024-11-22 05:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 48d9db1d-d079-3eeb-90cb-79b9b7b7e746 | -3.2384 | -54.2632 | 2024-11-22 05:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 9e59d22e-dcc8-310f-99ec-255744858567 | -3.3451 | -50.5126 | 2024-11-22 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d35f1111-11d5-3605-bb12-57e50545ce8b | -3.8535 | -52.3596 | 2024-11-22 05:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 8d25df15-bb5e-36f4-a20f-bb1701b4439b | -3.2386 | -54.223 | 2024-11-22 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ca69adc2-08b2-3b0b-9e8f-137a9a90675b | -3.3452 | -50.4917 | 2024-11-22 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| df4c44b1-6e58-3917-8bfd-ab15dad91682 | -3.2768 | -53.8199 | 2024-11-22 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 56ed9e46-5e24-3805-8be9-c3ac6950c640 | -3.2201 | -54.2436 | 2024-11-22 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 5967fbf1-9b88-31ce-b7aa-17adc9e96077 | -1.8106 | -52.1652 | 2024-11-22 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 33d60585-4a1c-3286-a989-00300ec7ba0b | -6.5631 | -51.1126 | 2024-11-22 05:20:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9c47a418-126c-313e-98cd-4ba3ffa401b4 | -3.2385 | -54.2431 | 2024-11-22 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 189.7 |
| aab930aa-8e0f-364b-aa0a-cf19066d12ea | -3.2569 | -54.2426 | 2024-11-22 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 5dc88cc9-06fa-322d-bc04-e9096d87b6f7 | -1.1287 | -53.3951 | 2024-11-22 05:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ad64eae4-67b5-36e0-ba59-0b72b99b4b2f | -3.27989 | -53.83635 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9b865c0-c4d2-3727-a8e0-dde610a3d176 | -4.07492 | -53.71976 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6fd90c8-8c6f-3b35-981e-f7fc897907fc | -3.00981 | -51.31123 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b5d18f7-50ec-3067-9e94-8fc9b4a5220b | -3.35026 | -50.50408 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbbaf1a7-e762-3abe-bebb-02fcabaa4de0 | -3.3425 | -53.33662 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10049f05-7050-3dca-982e-ce606872a950 | -3.32621 | -54.09272 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5421b02e-39b9-395f-81b7-510b46ef481a | 1.37372 | -55.95084 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcb77811-ac93-3823-a203-19ee403e2db0 | 2.33925 | -51.64762 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fcc5d8c-1a71-3445-8e3a-6df96149e311 | -3.71075 | -53.75195 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27a897a2-e003-3edc-8975-18210d6387df | -2.82108 | -54.02946 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd25c0f4-a648-3a8c-9342-188761a8125e | -3.27914 | -53.8227 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4e2d5e80-82ae-39bd-bfaa-cd09c61fe93e | -3.52016 | -53.80149 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 88fdce97-f1c9-3ce1-908f-a6fe9d0b8d78 | -3.34347 | -50.50782 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12a822a7-3076-34f8-ac44-7e7165a545e5 | -3.83297 | -52.25505 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0f806843-d3fc-399e-8a0a-3a7b3308f4d2 | -3.24205 | -54.23267 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2fe34ba2-8c19-300c-943e-cd8bb3516acc | -3.23368 | -54.2568 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 9022ae9f-5786-3132-bab9-0d1ab695af68 | -2.81309 | -54.01773 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b44b6c30-7658-37c0-a93d-38a20008ab31 | -3.53762 | -52.78859 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 284fe998-be05-35ad-9f83-e16dcdf83b68 | -3.11016 | -54.28684 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 289620ed-cba6-3fa9-9d2f-ddba04dca75a | -3.85703 | -52.36027 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fc441d47-9fd0-3886-a810-04d159d4bd63 | -3.24931 | -54.24925 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 14556da6-0b5a-35d0-84cd-a9c6cd72682a | 1.37712 | -55.9488 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c33f0df0-ab96-381e-b81b-175fe792477b | -3.28718 | -53.83546 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4d309d1a-4613-324c-9d4c-4ef254b8aba2 | -3.23513 | -54.24686 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ca8d4275-6e20-3d15-ac59-ba3585c61755 | -3.01129 | -51.01716 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6fe702e-e64a-3e9c-9859-9c94dac08aef | 1.37765 | -55.95023 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aab9e905-649b-3aaa-bc64-ce968777619e | -3.20595 | -54.24766 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README55.md)
