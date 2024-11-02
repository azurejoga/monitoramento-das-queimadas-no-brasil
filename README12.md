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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d3f57e5-eb0e-3661-a68c-8a26ae36c27c | -2.7749 | -48.57649 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 58300003-34af-3cfb-9c77-a9875e5d0524 | -2.76065 | -48.66811 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 62c4f262-2d64-3620-a22b-0e0000f1ef84 | -2.73634 | -48.75219 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e27b35fc-4b75-3132-be88-eaa5c73d4d71 | -2.73512 | -48.7434 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| b9012e62-c288-3312-98e8-4057c109a715 | -2.73389 | -48.73461 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a3093015-dee6-3b20-bfd7-0b14ad083574 | -2.73267 | -48.72582 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f38bc912-067a-3ed7-b164-e79afcb160ab | -2.72505 | -48.75113 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f215a566-a0ff-34a1-8d0c-c78d6cff7940 | -2.72382 | -48.74234 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 99906568-8fc8-3f71-859d-f0523303fea9 | -2.72221 | -47.99274 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 883f8d99-3dd4-3218-80e5-800909fab56e | -2.72138 | -48.72477 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8e761bca-22b9-3849-8669-91f4031fba88 | -2.71499 | -48.74359 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05076496-5127-3bef-9a52-66722b79ea51 | -2.71036 | -48.64569 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5173b088-ca01-3c97-8c74-d601f313a5f8 | -2.70914 | -48.63691 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2832ab8c-36d5-3898-be1f-c0f994ebc92d | -2.70153 | -48.64694 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ef8443fd-4760-3514-991b-50dbd4748f1a | -2.7003 | -48.63815 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0c9efef8-836d-3660-84f6-ee228d8ef79f | -2.67677 | -48.13189 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f26be1d-b4e9-3b0b-b2a9-a011c54c7f2d | -2.67504 | -48.65068 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bdbaa3c2-4c94-3cb8-9f1f-476de990d477 | -2.67381 | -48.6419 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce388c86-cfbc-3f31-a119-3ba422d99caa | -2.66791 | -48.13314 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 05fb2085-e6c5-385f-abee-cdf29d80f7a7 | -2.66402 | -48.57159 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 59f95493-2965-3c4b-a1de-b5f5907cdb1e | -2.65789 | -48.52764 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 288c8901-f81f-3ef9-90a0-99d6a3182071 | -3.45913 | -47.66608 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 631f7a89-ce34-3d93-bad4-7c3c493f4a56 | -3.0882 | -47.77985 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ca50f59d-19da-3a38-be63-777fcfa5ea75 | -3.06933 | -47.58063 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b8c196f-45ff-348a-97a3-40e8afa7b469 | -2.66638 | -47.402 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f9c84b84-465c-396a-a838-ca7696553957 | -2.53498 | -47.51699 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a35f14a7-1a43-31db-80c1-f91538224b05 | -2.53383 | -47.37671 | 2024-11-02 00:54:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6b8bca57-d78e-3c24-aa7a-f166037dd7bf | -2.5183 | -47.46336 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4d5ab33d-6046-3b7a-9b97-f4aeee4b7b33 | -2.51702 | -47.45421 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec0ac87e-3f8f-32ee-a158-7e8d48234f78 | -2.36739 | -47.63674 | 2024-11-02 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| cb0a29ad-5cc9-347a-8566-e2ac6f83ed16 | -2.6277 | -47.97574 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b533e7b-e0b1-3bb7-97ff-c7670a1e4566 | -2.62645 | -47.96682 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9e9492ea-2815-390e-ace4-18a442afb6fe | -2.62203 | -48.33523 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 73a7705a-f727-34a1-a9f0-192844b870e1 | -2.61957 | -48.31759 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 780c616e-9d08-37d2-9452-6fded9d87049 | -2.61319 | -48.33648 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b50acc39-bec0-3854-ab66-a6ca830ae600 | -2.61196 | -48.32766 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96f05593-c0db-301f-8749-339567672eed | -2.59714 | -48.2217 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0e94e681-b04b-392d-9c0c-025416f8eb60 | -2.57924 | -48.28729 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f16725d8-895f-3153-8097-6df111663ad4 | -2.57248 | -47.9808 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e0dd01c4-ca9c-34f4-a017-2094eeac12c5 | -2.57123 | -47.97189 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72c0c430-7674-3361-adbc-6815ff1ae642 | -2.5534 | -48.17973 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0a736a15-0f36-390c-a01b-f8517dd1c1da | -2.55217 | -48.17088 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 130d588e-4484-3f60-85ee-51df9651e20a | -2.53937 | -48.2088 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e979b1f-8bd3-367d-945c-66b960ead990 | -2.53084 | -48.47084 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8422eccf-f0fd-3a75-99c9-a3fe098f6b49 | -2.5006 | -48.06055 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 51dac1e8-454e-31c6-bf68-f05d95d83e39 | -2.46137 | -48.50483 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6d2a5da1-6e81-3c67-92f7-2c64853675ab | -2.46015 | -48.49603 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 86436b24-ee56-3a2f-8b81-69bf302bea54 | -2.42357 | -48.49223 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2a9d87ff-3fad-3cc2-8472-7d88776ed245 | -2.42235 | -48.48343 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 883da120-2fbe-3726-bbdb-7116cafed51c | -2.41726 | -48.52597 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 387bd354-ade7-3f31-917a-1ac963caf79a | -2.40694 | -48.58121 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c34e161b-9764-3d3d-a3e6-1b8931ab8083 | -2.39933 | -48.59125 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9b1ad020-1a9e-37ca-a267-ed7394c28de0 | -2.39811 | -48.58246 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3d3e32a1-997a-3ca1-8c4a-8ed82563de49 | -2.39539 | -48.22638 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 99fcc4ec-bc34-38ab-a15d-07550fbc1229 | -2.3591 | -48.56108 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 746eb1d6-26d2-3830-82a8-4aed2c98de93 | -2.35835 | -48.4266 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8aab8d34-e1dc-3227-bba2-99b1b97afecf | -2.35712 | -48.41779 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 897835d3-69da-3df0-99fa-a6afd53e9e69 | -2.34951 | -48.42785 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d8f9eedc-42ca-304f-b582-6f41145a7dd3 | -2.34313 | -48.44672 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 182d1389-30be-3ffe-8d72-e5a7e4a466cc | -2.33629 | -48.60655 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5bc88e09-e54b-33d2-8cf9-60c1f4d267c1 | -2.33507 | -48.59776 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d81cdf47-0d66-3253-900e-57dd52a16982 | -2.33406 | -48.51081 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 025e0bd1-481d-3c1f-b46d-7fdd1c3cde39 | -2.32991 | -48.62538 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 919a0832-d5c9-31a8-b626-c4a40794061d | -2.30122 | -48.54876 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4888ab36-d2ca-38c1-bc08-c7fc7aa8f12e | -2.2386 | -48.42297 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cbc8a8c6-ce1d-3f7b-8a92-a293bcdf6173 | -2.23736 | -48.41415 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 342b0437-48e7-33d2-8c50-86571955c204 | -2.22975 | -48.42422 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b542544e-0fde-3598-ae4d-423a6f233400 | -2.22852 | -48.41541 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 6ef2fc10-b485-3988-b6fd-e683dcee5f97 | -2.21711 | -48.47681 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b0f98e13-8709-3cf7-b5fa-c9156d12a642 | -2.20116 | -48.36222 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7076699c-0c21-3ba3-951a-6118477563b7 | -2.19993 | -48.35339 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| acd9fa66-9c4d-3d5e-840c-6396596bf0ba | -2.15254 | -48.53081 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5d9d454-8b1f-39c8-9769-c29ce25cb5de | -2.52603 | -47.45292 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 14bb064f-4993-3ade-a7e5-42bdf71f9bb5 | -4.37077 | -49.11354 | 2024-11-02 00:54:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e16febf2-45d8-34f2-981e-545020e99afc | -4.3587 | -48.63507 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fa98b910-7941-33ed-908f-7a9d87265618 | -4.35798 | -48.16186 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 08ff30a8-42d0-373a-99f5-451e218f07f1 | -4.35747 | -48.62625 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1c74ff12-d7c7-3cf8-9bd6-4cfae7059f9e | -4.35675 | -48.15306 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| ad67fd6f-a788-3d80-8080-ee51af5c96cf | -4.35625 | -48.61744 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 7691a6fb-1d7c-30bc-b256-ae41632d0307 | -4.35502 | -48.60862 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1a23c6be-ca52-3c8c-a28e-73b9397b7fe1 | -4.3538 | -48.5998 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba2feefa-190c-3b98-876d-c4098f462cdc | -4.34914 | -48.16311 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cd29ab65-adbb-3413-bc2c-12edfb002dd8 | -4.34791 | -48.15431 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c0ad6a20-da5a-3830-b68c-0e05e965b33f | -4.34618 | -48.60986 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 73c3c23e-e0bf-3ddf-8b80-e2435bade5bc | -4.34495 | -48.60104 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 77598803-9fbd-3e18-8638-29464687d490 | -4.34445 | -48.72717 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23216b63-8479-341e-8995-626a032e4d87 | -4.33611 | -48.60229 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d5cbaf8d-9f1e-3497-bd12-f34013e59d77 | -4.33488 | -48.59346 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 2e81f0e9-7a4e-33cc-9dc5-ef1786c8304d | -4.33366 | -48.58466 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| aa3fe2f1-7fdf-3c4e-bf56-95667f6a9987 | -4.3334 | -48.64765 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d93dbf55-8e5f-3f9f-9f5e-92f4660eb24a | -4.32456 | -48.6489 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| cb36fcf8-d444-3c63-8a97-772f77f47e1d | -4.32333 | -48.64008 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 7bbc5395-7a3b-31b3-ac2a-c2eea2cf60b1 | -4.31572 | -48.65016 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b39af164-3073-3e58-8be2-2897bd5170ab | -4.31449 | -48.64133 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| baa6a470-f1ae-353f-9ed3-fbb96bc911b5 | -4.30442 | -48.63375 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a98b3f48-ec07-3354-ae22-6b5370531687 | -4.3032 | -48.62493 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 090d5117-47b2-3c22-ab8a-bbe85cbafab3 | -4.2968 | -48.64383 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 26318799-ff7a-349e-8515-eab17bf007ac | -4.29558 | -48.635 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8618be9d-4b4d-39f2-a7bb-3697c2e48ced | -4.29436 | -48.62618 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 49bfee03-a904-3884-bc3f-88ad51919cfe | -4.29069 | -48.59972 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README13.md)
