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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 061e6f73-6dd0-3b4f-9142-32621a57de49 | -3.23696 | -51.55384 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55b9e463-1837-3688-97a9-6bedc817c32d | -3.9591 | -48.08434 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1d4e3851-d133-3362-a5dc-c599d9158761 | -3.22567 | -53.42234 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49644da1-3ef1-3529-84c2-3b271407ce54 | -2.2124 | -52.48006 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 403fc56f-a260-3c1b-b29a-a7c64a630902 | -2.86479 | -45.53584 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87348db7-7095-3ddd-a9c5-069e16ede2f1 | -1.31113 | -51.75683 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94a12952-006d-3428-991d-2dbe02add072 | -1.31673 | -51.74295 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b1cf5179-97b4-3410-9ab4-4064023f0754 | -2.78077 | -54.02846 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebfcd6b0-ed3c-3d89-bc29-72530e8a7e18 | -2.84844 | -54.00717 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2767e6a-c7ea-32d5-9604-96d8b3340cf9 | -1.08831 | -54.0387 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f1fcbc7-cd23-3150-a1f6-c8618d1ceec0 | -2.80447 | -53.04567 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75122b02-2c59-3f7f-b16d-b88525bb8c41 | -1.44429 | -52.58599 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf5ad7cc-5768-3436-8168-1fecb927c6fa | -1.89544 | -50.57442 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d401d25c-0042-3628-a90b-af3517f0f125 | -2.31834 | -51.95464 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 279d0398-48e2-367b-bfb5-a46a85045955 | -1.2154 | -51.73883 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79f2b9b2-b20a-384d-afe7-8c65bd13f442 | -1.91916 | -52.65956 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab32679c-a793-3946-ac31-d7f9bcfe032f | -1.69821 | -55.01078 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c61583d-690c-3bc0-8bf8-3504f50bf176 | -2.88241 | -46.83747 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b3b8f0b-c26a-33ca-bcc9-faec7b3fe87b | -3.69668 | -50.16964 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16de7db3-1ecd-3e65-8744-3044bc52cb0d | -3.1582 | -54.48426 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 139e9d07-11d0-3bc9-82fb-452dbfe80658 | -3.10354 | -53.81093 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 53a42507-4b37-3ea0-acd1-2381f86527f4 | -3.6971 | -51.36752 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4711a2fc-f978-3191-b601-5c11dd534aa1 | -3.54793 | -50.41435 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| befa0bc4-1966-3875-9c87-34ee7ec7ed34 | -2.8869 | -53.98144 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 880fdb15-5116-3c54-909c-183d9e03ebb2 | -2.98245 | -53.27854 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c25afb41-9391-3e63-b783-afeb4b6d6e66 | -4.64641 | -47.15244 | 2024-11-29 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a3d8b83-2590-36c6-8be3-33b6bdd32f33 | -3.09586 | -53.81678 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44fceb86-a060-3321-9cfb-92bbb4e13034 | -1.20121 | -53.88293 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c542a9ec-4cf4-3d63-9534-9bb9c468fdf8 | -0.20533 | -51.45961 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfd10bc7-c8d2-30ab-b3aa-b1e187389ec1 | -3.08761 | -54.13301 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a382ee29-9579-3172-9b87-5acfaed9b069 | -3.07995 | -53.28653 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb96e24-18bc-339e-b57f-d2ff6dd9498a | -1.19729 | -53.71306 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a7cdfff-1402-3368-b491-758c0b90beec | -0.05184 | -50.82535 | 2024-11-29 04:57:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8bef5d2-f528-3ba2-9488-4824d29288c6 | -1.55366 | -52.01747 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9133ee9a-1913-341a-b31a-e45fc22cda3f | -1.20174 | -53.8795 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60120ef3-fcc0-356a-ae76-e788cad96c8d | -3.70758 | -51.79962 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24131799-c56e-378f-9e07-b31e79de9140 | -3.33529 | -53.22064 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| acb7e4d8-200b-39a8-a025-09b2a8d36db9 | -2.05889 | -46.37971 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49387dfe-ba8e-38f9-a646-62353e79cc84 | -4.43499 | -46.58772 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 81a031e0-6460-3dbd-b66b-df997852ee84 | -1.86591 | -52.27903 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a962874d-c7da-30b1-98fc-0ef202131d02 | -2.35127 | -53.9255 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 093444fa-ef7a-398b-84c5-a8cbd4c129e2 | -2.74297 | -54.15954 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f8dc852-b57c-3fa8-942f-08c10048304e | -3.04007 | -54.04395 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ac9db07-fe40-39ba-bbba-c47010a0f5cd | -3.78501 | -50.13794 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcac90c9-e3a0-310d-9bec-3f0d4e846ae5 | -3.21916 | -53.83289 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f9631ef-be24-3341-9086-92f54ade5c7c | -2.60663 | -51.79736 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a46795-bece-312d-94e4-0da48bee2625 | -1.27223 | -52.1623 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618af3c5-90f9-360a-90ee-28abbdac3f85 | -1.09979 | -53.39845 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3528eefa-5c11-346b-a54e-b1e904c2af2a | -3.79008 | -50.12967 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 367c0665-e0a0-35f9-91c1-0dfb3caffd6e | -2.89136 | -54.16912 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77819684-3b83-3c78-b4e2-6ba557b12ff1 | -3.41804 | -53.88845 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f53c1e2-6388-398c-bee6-682213cb61e4 | -3.3148 | -54.09428 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fb83caa-1c83-375a-89b2-87385a9d234c | -1.09733 | -53.61253 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27ffd935-4a91-3f9d-a47f-5de84e2a9834 | -1.4143 | -54.80458 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44a07b88-dd4a-3efd-bb2c-0b749bcefde8 | -1.14395 | -53.7041 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 914a79a9-a746-3bf4-974c-55142fe12a1b | -5.75935 | -43.4014 | 2024-11-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f71563d-0103-32aa-9ae2-e51215c862af | -3.17831 | -46.30541 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0d65d22-71e1-3cf6-8719-04e297e07413 | -2.00155 | -51.17364 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37f9e1a8-13c2-3ec7-ae25-46892feb2e9d | -3.26726 | -45.37446 | 2024-11-29 04:57:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e136dc78-4395-3a42-90e9-4544b2c0839e | -1.93754 | -46.5901 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 597f4e5c-f0c7-3804-baf2-da5ef89e0fec | -1.68808 | -52.50597 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81ef9ba9-ad92-3360-8291-767bdc62a9a7 | -2.15132 | -50.60772 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5ab8fc7-23f9-3b2e-8197-22f94b89d281 | -1.04602 | -52.41348 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11458e53-5540-3e9d-90c4-debf2a908a6e | -3.00519 | -54.74322 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bbf1a0d-deca-35f7-8085-0c8f9077f9cb | -3.49954 | -50.46085 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54015b87-5a81-32df-aa72-0874678dd544 | -4.43279 | -46.57783 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 012eec18-a479-3d13-940a-9c09a9584711 | -1.05874 | -51.75844 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d17a7a25-2389-3698-8ee7-b9893df09d41 | -3.05598 | -54.0288 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef20409e-bbd3-3bb4-96d6-1bc60776fd30 | -3.19946 | -46.56399 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 835ba906-f9ff-32cf-97f0-a29f03a3b13b | -1.1025 | -54.14408 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 097b2c86-24f7-382d-90ff-d22fb369e9e6 | -2.46977 | -53.97253 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8212419-307d-3e5e-9846-dca2c1b908d1 | -5.58841 | -45.21479 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1cd30f6c-8ed4-36a3-ac47-9aec329ee855 | -2.94271 | -48.33862 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61d8e915-2e03-3f05-96ac-d9c4d100b34b | -2.86389 | -53.31948 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6025abc-496b-3644-ac87-9d29b13f537f | -3.09395 | -54.02409 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27d9a759-d037-36cb-bffd-be89515b4306 | -2.12257 | -46.39076 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 510f9780-0b6e-39c2-96c2-d929d9dcab49 | -1.40837 | -53.40477 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 741ca9ca-6836-37d4-a2e1-368e69f1266c | -0.46923 | -52.01293 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bed5a4e2-1bca-363f-848e-91931fd8d926 | -1.31788 | -51.75787 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8da764d-b995-3efe-9c2d-447a51548dba | -1.6275 | -52.4574 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f73fc93-d174-37d7-b95a-404962d4145b | -1.25252 | -51.63366 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d0eb0fa-2224-37e9-877a-a8f42face51f | -3.07008 | -50.57215 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60f9bc37-97cd-31d2-8767-13f620c0e294 | -1.09565 | -53.20831 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9c8a087-b8f3-3e17-b737-f011e69c5659 | -1.69293 | -52.45316 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b5051bb-efae-32c9-a53b-4e6a8eac446d | -3.93759 | -46.51193 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de60a3bb-91f3-37eb-8109-222ff5837e99 | 0.98483 | -50.12436 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e70eb733-5344-3a99-8280-6e51cc2d5c79 | -3.67302 | -54.28109 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fe81b14-1002-35ba-8b36-9c84341c1cf2 | -4.4131 | -55.11499 | 2024-11-29 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 971cac17-68d6-3019-b510-5bb6d983f660 | -2.81399 | -54.07589 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77366265-2eb0-3522-acde-eaaf6af20983 | -3.24099 | -51.5506 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 910521f5-53c8-39b2-ad39-13a63a12b7e0 | 1.23168 | -55.93731 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 893f55a5-ef37-3c64-9880-0df0c441a603 | -1.12931 | -53.62449 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4181d3f9-77a1-3c2c-b821-5c7c1108caef | -2.98649 | -51.44682 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8a3e3c5-431b-38e4-8d00-7b6aab7cedec | -2.44791 | -48.60858 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc95f61c-9cb3-3d82-b577-a39c57d00dc2 | -1.91458 | -52.88565 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 375db2d6-bd6e-340e-81a8-8d2364e25570 | -3.07063 | -54.39239 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed18809e-e35d-3722-8152-d8a64638177a | -2.92456 | -54.36912 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aad9cb6-ee3f-3137-a9c2-28fc04ce9779 | -0.96131 | -51.65219 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bf432ef-9a0d-3459-af32-d61fcafb2e7c | -4.18009 | -48.61003 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ddd0998-03a9-36d2-b9c9-7228d671d77f | -1.65482 | -52.50086 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README66.md)
