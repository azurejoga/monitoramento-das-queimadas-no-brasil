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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82a60db0-2069-316b-b9be-600991eeaf07 | -1.31846 | -51.74073 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9bbd1e66-9057-33f7-9a12-d195d860abf3 | -4.2549 | -50.83674 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aad37f2c-4710-3ab6-9978-179f404ca052 | -3.21054 | -54.17385 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b9130f50-ddb3-3523-8622-90a55468b9b2 | -1.33108 | -55.85237 | 2024-12-01 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbac3e33-039a-36c0-8f8a-316faa60b657 | -3.18209 | -54.33317 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be349472-f7cb-3daf-b26e-429ff4557723 | -2.62165 | -51.75665 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c74f7334-0a70-3d72-a3c8-1e9b6ccd363b | -3.32264 | -50.03259 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb18d360-1bfd-3edd-9226-798c913f63ab | -3.86076 | -47.05694 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d454a622-2f72-39ba-9796-fc7468d06d76 | -0.59435 | -51.69909 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f3d2606-8fa5-33bf-9d7d-eaeb14cecdd6 | -3.31185 | -50.44448 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aea6c46-46a3-3178-aa02-3568d78e86ab | -1.68397 | -53.94509 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 556e4957-b7f2-3f9f-ac9a-4831b4f8d28d | -3.03189 | -54.03822 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e0ad94e-1e69-319b-babf-2718978d405d | -3.07068 | -50.9893 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 86dfa258-426c-3356-b73e-b804abc73a43 | -3.26899 | -50.56512 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4459d8ae-42b1-3533-abc4-57617465f79c | -3.7333 | -49.93742 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e3182c8-9d51-32f3-8783-96c7b8be00ee | -3.13491 | -45.98259 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ea276f2-9b83-3d02-9cbd-a4d4cb7cdf24 | -3.33281 | -50.22513 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab338c58-4fbb-3fa7-ab0a-a93bac0ea76e | -1.15181 | -51.68873 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6886e9c-5598-3035-8ea9-b822cfd3ed8b | -2.9874 | -53.34686 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 021fb1e5-2c2e-31ea-b42b-2e6530f02b3a | -1.32417 | -51.74923 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 069aaa3e-a6cd-3989-a9f6-5d0f6577ee23 | -3.21285 | -53.12866 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f78c16e-3c3b-37ed-a2b2-7e515ef36de2 | -2.59281 | -53.98344 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cafc2ae-112b-3693-a3e2-a7784f26cdfd | -3.70526 | -51.06358 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cefeee99-aa99-34fc-80ae-3e40a8fecc4c | -1.44159 | -55.22623 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9199212d-80aa-3095-9f8a-38b07afbf74b | -1.43153 | -53.39675 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93a41e45-f8c9-3593-8715-c8d835a17016 | -1.26117 | -51.74696 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b67c8eab-06d0-39a3-b047-0d4f02bae1c4 | -2.68018 | -46.60186 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49935736-929d-3944-8945-8e393364883f | -3.85054 | -40.98188 | 2024-12-01 04:44:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e726c7b0-7cec-3c73-8dd8-55b3051d0c3d | -4.17463 | -48.63283 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 05ff20f7-e1d4-30b9-a828-ab34b79ac1eb | -1.18591 | -51.76253 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d89e12a5-d482-35e7-970a-534bd2ac448a | -1.44407 | -54.36845 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc98e328-6e07-3e05-9ec4-fb5e2a71b923 | -2.80096 | -54.05614 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc2e5e18-2b03-3837-8ce7-c46fd9ee40df | -2.993 | -45.57666 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2bd4dd77-ae68-33a2-8fc3-66b431828641 | -2.79948 | -53.1215 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88fde884-a62a-3fa4-906a-644664adef2e | -1.26074 | -53.37314 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f41a34d9-79a6-3864-bb93-53870125a6b8 | -2.8369 | -51.28312 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d1108c9-7ba2-3b51-b696-1156af661346 | -1.4224 | -52.66196 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5f01260-168f-31fe-b13f-00fc5b3db733 | -1.99802 | -51.17471 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 164b529e-afc0-37e8-8006-fe5a49de2faf | -4.26154 | -50.83779 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 732a3e36-a378-3325-8a94-b742347a946d | -3.08964 | -54.03843 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 175da9b2-05b5-3ed0-ba7c-cb864f022159 | -3.03417 | -54.04784 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a048e63-942e-309f-85d2-2c05c3b61ca7 | -3.50101 | -53.83837 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b4fa2085-274b-32eb-a257-d911095f246b | -3.07644 | -51.66784 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae285f36-7edd-36bf-87ad-8e1d07c6e473 | -2.79701 | -54.03471 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03f8c1ff-2904-33a5-aee8-c725c37d4e0b | -2.62459 | -46.95432 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac95f958-d41d-3654-8a15-9f3db8004e6b | -3.07298 | -53.2582 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8502b0dd-6d8b-3221-a94f-4b009bdc29ce | -4.07829 | -50.02639 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6e4fb33-6343-3b8e-90a7-6a7c5d7802bd | -1.8281 | -50.90221 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6abe73ce-a954-3671-984d-f58cb4a9df1c | -1.63808 | -53.86738 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23004f1e-7197-3ce7-95f8-e2521b3f533f | -2.75292 | -51.65776 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67182caa-bea4-3aea-a712-c93cd942816f | -2.29165 | -50.68851 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b183b205-231f-38cd-b5cf-ebaa8fee6c19 | -3.69421 | -51.81914 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a494d6e-4c78-340e-a36f-23e4a5c6ae3b | -6.71112 | -47.27625 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 252a805a-57d5-385c-b3ca-318384b778b4 | -3.03086 | -54.18733 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6cd6da5-a5d9-3172-b643-57726417317b | -3.25512 | -53.87123 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04dd31cf-d6e1-3c32-91e2-d0a6be87a2e7 | -3.02237 | -54.02523 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3249407-7350-33cf-9a9f-0abffad1cd24 | -3.33809 | -53.36969 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d12ccd0e-7f15-37d4-9dc9-6911dcdceced | -3.22564 | -54.17632 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7f1e1d4-a296-32b2-b84f-b29d5ca45516 | -1.07312 | -53.6358 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 622ff236-cc8f-377b-a66c-833bac4cfa97 | -7.02935 | -44.84591 | 2024-12-01 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b2cf4b5-b3cf-3065-912b-e878656edcd1 | -2.81698 | -53.05762 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39c87632-3150-3e7d-a2c8-137de0bf1bf7 | -2.88012 | -50.73803 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37baa9d0-f174-37bc-abad-bcb11d61e3b5 | -3.26352 | -48.76779 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff802499-1d86-3b36-a4dc-9e2e5efaa4eb | -4.06665 | -51.06326 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f74d47c-bec2-36fc-9238-6dad8a07d088 | -3.14818 | -53.83877 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0857ec6-6ceb-3564-ac3a-92ac06db57a8 | -3.19764 | -46.57701 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8948d9e6-bfd0-37a5-81ff-9003442bcbad | -3.21734 | -54.17964 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaf27917-4ba5-357d-a804-c6a584a7aa4a | -0.34692 | -51.98328 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 196adcca-96b1-3c10-aef0-8dd51d15b235 | -5.89565 | -48.27316 | 2024-12-01 04:44:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5c0f566-915c-3f0b-930a-2816ffc4bde7 | -2.51856 | -51.83398 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b351b6b6-74fb-3f81-b43b-bfe6c6758013 | -2.23073 | -52.47953 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a036432a-f752-3adf-aafe-b3a831aa03e5 | -1.27517 | -54.55367 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 081c2e93-e68a-3c3e-88b5-d0857b616b07 | -3.97775 | -49.91131 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4f14ad0-8e73-31ac-bc2e-22c920876c73 | -2.89843 | -51.57785 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 64daecc1-94ad-3fab-9efe-4a0e87510b77 | -2.44727 | -53.66486 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 851a82d5-e352-31c3-a65a-e7e4f57a0488 | -2.6205 | -51.76394 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c471a2-8ab0-3d3b-b0f0-c23ace3ad0c7 | -0.01222 | -51.16509 | 2024-12-01 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5d15ab8-237c-3a53-9c55-6f3d8008680f | -2.28966 | -45.60396 | 2024-12-01 04:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d2859b3a-c414-3c73-8d44-78b2c39bb22a | -2.83441 | -48.47591 | 2024-12-01 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89f6906f-d3ba-30b8-98ab-339d8a4d5e80 | -1.10084 | -53.38975 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb57481a-bce2-35bf-a6a8-00e54fd2a654 | -2.83385 | -48.47956 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8804afc3-ac58-3f58-8d26-3af73f09e8cf | -7.02824 | -44.8479 | 2024-12-01 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f6039e8-1004-335e-850a-60ae05142462 | -1.27167 | -52.70978 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cf49539-8ac0-39f8-afeb-8a4b8bcff8ce | -3.09589 | -53.29973 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f739b3ce-67f5-3c82-8ef8-64530450b5d6 | -1.28931 | -51.72478 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06300120-6cd8-351f-a200-2b40cca1e522 | -2.48002 | -50.3987 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61b6416d-32f8-3ce8-a154-4d33b0965b35 | -1.22989 | -51.81068 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abca3167-3a45-3c2e-8c76-4b964dc5ea80 | -2.81405 | -53.05301 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae4daca4-4f78-3e4f-8d30-3beec81ebbef | -2.20531 | -50.55082 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01d61839-e4cd-3060-ade8-e8909ffeb0ee | -1.00761 | -51.72059 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8786d9f7-85e5-3923-ad52-74e71fa54a03 | -3.89981 | -51.051 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef19abbf-c3b2-37bc-9380-4083c7dc338d | -3.17827 | -53.25225 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2aec8c6c-86a4-3331-8907-061b4b0a70d9 | -0.74537 | -51.94625 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d55b6d1-35fb-3782-a3c3-fbdb4af42e5b | -3.17678 | -53.63416 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dffc191a-1029-3395-9550-d5f8f85cf1cc | -4.00603 | -49.94413 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2340d859-f54f-3f64-bc70-abc33b7bcf05 | -2.29444 | -50.6925 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2be767a8-6e2c-313f-afb6-8b35ba6886cc | -4.41679 | -49.02833 | 2024-12-01 04:44:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29f583d0-30a9-3daa-85e9-3f08a31a897d | -2.80609 | -45.93615 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc2def4a-93f3-3d3d-a0fe-86728c32f25c | -3.69219 | -43.43078 | 2024-12-01 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fcf690a-8c14-38c3-8b9c-8cd7d33b1cc3 | -3.47105 | -50.27126 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README50.md)
