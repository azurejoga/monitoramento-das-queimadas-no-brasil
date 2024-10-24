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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 152c5428-f905-3ac7-b284-9d5dce0fd9c7 | -19.6512 | -56.78733 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 08e68754-1c8a-318e-987c-0fbc0f39ae53 | -19.65116 | -56.73301 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.5 |
| 659b432a-9b20-3cce-b871-eaf75391ae91 | -19.65082 | -56.77581 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a25bbd07-de8e-3b69-b16b-2ed0396c3c4a | -19.65071 | -56.75407 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9d3daeee-3ceb-3a12-ba81-d4195c395c32 | -19.65062 | -56.73772 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 51b32fe9-b9b3-3b9b-ae3b-258354c7c564 | -19.65029 | -56.78048 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 49493b5e-c11d-38ab-bb91-4ec7b5856bee | -19.65014 | -56.75875 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dbb670e9-8cba-3260-915d-4ab9b6b30662 | -19.65009 | -56.74242 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| c7ecb0f5-15c6-39ee-a88c-6c450e0af2ed | -19.64975 | -56.78515 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ed0ae496-8a58-3c60-a913-0648ccc260e0 | -19.64957 | -56.76343 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ed0ccdee-57fd-32d3-b123-064079d827f7 | -19.64955 | -56.74711 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b491850a-4f6c-3f24-aacf-4c728684bdc6 | -19.64902 | -56.7518 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f159a853-a1a5-3926-af46-46f21af84863 | -19.649 | -56.7681 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| bf4cde93-5d0e-3420-a83d-6b468dd5d4d4 | -19.64851 | -56.73473 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.6 |
| f1a9f1de-e8b0-34aa-b041-439ef65bdd7c | -19.64848 | -56.75649 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b72bfdf0-6448-34b4-a101-226665516899 | -19.64844 | -56.77277 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| d07cfef5-c25a-37d9-b83a-824bd004171c | -19.64794 | -56.73943 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 54d5cf59-28c2-3d0d-812e-e6ad1c6527a3 | -19.64787 | -56.77743 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b2a81f63-f7a7-3fa1-be05-021062b78c45 | -19.64742 | -56.76586 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| c4605f9a-a0a6-363f-9636-e42a29455a99 | -19.64737 | -56.74412 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 7fc8778b-8496-3336-87cd-fe9987e7e72e | -19.6473 | -56.78209 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 66019d41-9bf7-38ea-b91c-893f801d278d | -19.64688 | -56.77055 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 29bed52f-d0d5-33b5-bbeb-58ede0d126f7 | -19.6468 | -56.7488 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c764ca20-367c-38bf-aac5-2912ec3a845a | -19.64674 | -56.78675 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c2abd9d8-5ff2-3f3c-bd31-097bf3371f9b | -19.64635 | -56.77521 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 4cf2b9af-a67c-3368-87b4-5a5a7f3116ff | -19.64623 | -56.75348 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c1250793-9f91-30e0-b7d3-685aa34f8da7 | -19.64581 | -56.77988 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 02ee4e71-159d-3420-b6b8-02e53b2a7f73 | -19.64566 | -56.75816 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dc50ad7b-0581-3897-b671-18c73eb9f304 | -19.64528 | -56.78455 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| aa977bf5-801a-3ba1-a7a5-4d32cf36f3b3 | -19.6451 | -56.76284 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 31326537-265c-3a61-8b7c-cd4bcdc50f83 | -19.64453 | -56.76751 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ed2f0b6f-3263-30bd-af08-cfbac27c89ef | -19.64396 | -56.77218 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b78ac7f0-9661-3d75-9d11-41e4092bcc99 | -19.64345 | -56.73884 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 0fcab879-e25b-3c9a-b353-1fb9738a45eb | -19.64289 | -56.74353 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| dbfffc64-f23e-3810-a1e4-e45a36ca917b | -19.64283 | -56.78151 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 703e0e9b-24d2-3c0a-92ba-7d6ac1ed4a6d | -19.64232 | -56.74821 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d3ee8353-aba7-3652-80e6-3bf185cb2d8b | -19.64175 | -56.7529 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c222e5aa-c194-3f32-b3c9-2eefb5526bd5 | -19.64006 | -56.76692 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9e81ca48-d457-3311-b0a5-b912fe7d1bb2 | -19.63897 | -56.73825 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 929be1db-995a-3f43-8966-11da59aa82b5 | -19.6384 | -56.74294 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 83c56c50-c48a-32b8-bf05-c8eed8f55287 | -19.63784 | -56.74763 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5b70821a-dbed-3e46-a38a-ee68a350da4b | -19.63392 | -56.74235 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| dc599e7e-b1af-3514-a2ee-9a8d567e0375 | -19.63336 | -56.74705 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5aa3ad54-bbf9-33bb-a0a8-a1340541993a | -19.6328 | -56.75172 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c3a9bda0-b37f-35ea-a2e3-ae2b6fc5822b | -19.63223 | -56.7564 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2e0e16db-018e-3478-85d8-a98b3544481c | -19.62888 | -56.74646 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 3f60faf7-57ea-3005-96c9-8c226da4182e | -19.62832 | -56.75113 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 141a686d-5c5a-3cbd-a200-59ac9720def6 | -19.62776 | -56.75581 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| acbd4542-bde1-3656-9c69-135afdaf376d | -19.62719 | -56.76048 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 597da18d-3fbb-36d5-b0db-b5a964cf2e21 | -19.62663 | -56.76516 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7c80473c-426f-39f5-a493-9e37d5aade7b | -19.62607 | -56.76982 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9a8726cc-acd0-318c-89ef-609905490965 | -19.62216 | -56.76457 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7cf6e3c9-f74d-3488-8d40-d202ec972dc2 | -19.6216 | -56.76925 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4f39d205-3f38-333c-a411-5fdf8b7268d8 | -19.61657 | -56.77332 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| db723fae-ee03-36c8-923b-7e00e32eaeac | -19.72294 | -56.74252 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 64f68ba8-ff20-353b-8797-0b7cff6a4795 | -19.71846 | -56.74192 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| cbac7c1b-2f82-3fec-9e3e-5bcbcc239406 | -19.71508 | -56.73192 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 2fcc541d-3cf2-3251-a627-7fa75dc85e86 | -19.71453 | -56.73662 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 54623797-ae8c-3c94-8998-f05719a3035e | -19.71397 | -56.74133 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8c1dd7ef-846b-36a5-9722-f40907561124 | -19.71059 | -56.73133 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4938a86e-070b-34b0-848b-7de9df633b25 | -19.71004 | -56.73603 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 91e47880-9f40-3691-9497-ef7dff470ffb | -19.70948 | -56.74073 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bd655ecb-dc57-3174-9ee8-998b62ffc2e5 | -19.7061 | -56.73074 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 44aaa0eb-7864-3d86-adbd-daeec32ad416 | -19.70555 | -56.73544 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e1034925-c2f5-30fe-8381-eb1b23702f87 | -19.70216 | -56.72544 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b00c34c7-cb65-3005-a434-35a057c9266e | -19.69768 | -56.72483 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9f3b77a7-605d-3931-bec5-bc1d0e6af782 | -19.6865 | -56.74247 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 135737a6-dec9-3bd7-bbba-44a6e61d57a1 | -19.67467 | -56.72659 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0cbd5b3b-ed62-32ad-a98c-0f6403ae8e64 | -19.67019 | -56.72598 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0979bda1-a1ae-3265-917a-ce1232a3acd0 | -19.66759 | -56.72769 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 86c4e1d9-9ac6-3cf1-9eaf-802685abe6dd | -19.66516 | -56.73009 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| abb90d1a-cdf1-3991-ac47-1affd372cf10 | -19.66424 | -56.77759 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| de48c545-8d0b-3482-985c-8d86689f0e00 | -19.66408 | -56.7395 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c6f5f3d7-d15c-3389-ba6e-18cb2ee808c6 | -19.66401 | -56.85773 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7cbbf999-c7e0-3ac6-adfa-4344cea7bba3 | -19.66253 | -56.7318 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f5754540-7610-38f2-8ae3-0cb659d5b031 | -19.66196 | -56.7365 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5a4d1c82-272c-35c9-abe2-37dfba949fd7 | -19.66186 | -56.77452 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 22a2d5e9-18de-3899-969f-b24b169e3737 | -19.66155 | -56.80091 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 22379aa9-87b6-3d31-a576-a5da37cd76d7 | -19.66138 | -56.74119 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b8292354-20f3-3849-9d58-35331a4ee4a1 | -19.66128 | -56.77919 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e9551d18-4dc7-3ca6-844b-d20cf43eb3ae | -19.66081 | -56.74588 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4ccbe63a-8e26-3441-b0f6-26415bb6d3bd | -19.66067 | -56.7295 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1d5f187e-56db-3c89-9963-7357e96e0c45 | -19.66031 | -56.77232 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| f1597068-5934-3dee-b36f-9d123a835344 | -19.66013 | -56.7342 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9386c543-de52-382c-9ef3-3d1e1062c49a | -19.65977 | -56.777 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| d2db5d32-2ec2-3200-ae2a-9d6e95870435 | -19.65956 | -56.85714 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 40e1db52-19a8-3b31-a1b0-fd4b1d314de4 | -19.65906 | -56.74361 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f2a21db9-798b-376b-9f80-f607fc950e6c | -19.659 | -56.79781 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3ad8acd2-7be2-3879-9b27-005f1aaeaa66 | -19.65853 | -56.7646 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 51081be7-6c33-3fc7-bd6b-077a38b6debd | -19.65852 | -56.7483 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2e8b152f-edf9-3639-87c9-4423e16c6781 | -19.65843 | -56.80246 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 459ab04e-bfa0-3a79-86de-cdbbd7922b0d | -19.65805 | -56.73122 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 8e159f2f-953f-398f-9b9a-3471eede4f1c | -19.65795 | -56.76927 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 3baf8ef3-b840-3417-9eaa-70df9db3bb9c | -19.65762 | -56.79566 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3ec04774-f9bc-3430-b185-aa632e2832f1 | -19.65747 | -56.73591 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 2e986e3d-0554-3a2d-8d3c-6b89e27c776b | -19.65738 | -56.77394 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 9b1e26cb-7abf-3147-9d17-371d464611fa | -19.65734 | -56.99149 | 2024-10-24 05:25:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 309f4f28-b285-37b4-830c-4497439a3e02 | -19.65708 | -56.80032 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 38921401-448a-385a-a97a-13634f72cc85 | -19.6569 | -56.76237 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8a1dfcff-3612-3569-9092-e3982859721d | -19.65681 | -56.7786 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |


[Clique aqui para ver as próximas entradas](README108.md)
