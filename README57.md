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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b867fbb-5d37-387a-b179-ffd1e617532c | -1.92781 | -53.35382 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5336390-6c67-3147-a85f-e2e7909d6444 | -1.32705 | -52.39976 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7fa1261a-6b60-37d4-b332-eac4a7260fb1 | -1.41558 | -51.12844 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 621b834b-faa9-332e-897d-62a596bfbc22 | -2.91612 | -53.06564 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8bf1feac-18f3-3569-8d4d-3d63ece9ec75 | -3.18426 | -53.25065 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b09428a-7ff9-3805-bcf2-2e28c15bfa96 | -2.8007 | -54.01554 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3506812a-3df9-30a5-88af-f9822abac4ac | -2.93785 | -48.32651 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3eadbce-2188-3d1a-932d-fc2087fa3dbf | -2.22193 | -46.4731 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 661c12f8-4c5a-36d6-ab7f-544ce70a1cfd | -3.3087 | -53.367 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 285b3da6-c599-3f98-ae22-0eaa9cb40309 | -2.2008 | -53.65902 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6164bcac-41e8-3caa-a37e-fc241cae5dc5 | -3.55028 | -50.27916 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8342ee0-5fc3-3940-8183-f244e8a4a43c | -3.11933 | -54.30601 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| affc311b-1619-30c6-8a73-0e0b56aaa484 | -4.34805 | -45.88588 | 2024-11-20 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d730366-88df-38ab-92eb-1324cc48a7fd | -2.27612 | -50.5836 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ea36acf-723f-36bd-96c9-cc0ac8611819 | -2.55434 | -54.0694 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50843f64-cf16-3419-b8d1-3a5bebfaafa6 | -4.11357 | -51.05446 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e6ecb0-b24f-3f0a-9a06-0cff88fde66b | -3.77196 | -52.0021 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 254b63db-569c-3da6-b534-1e7c3963ec1b | -3.6668 | -54.65303 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0d92a7c-fb07-3173-9c95-c6718d674e04 | -2.61197 | -49.25989 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18a6e638-0617-3c6a-a6ae-b68f1d27019d | -7.21223 | -55.00185 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 346e5fd0-3f47-3b41-a8bb-55091c9633cf | -1.22095 | -51.74049 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3be08769-e032-3628-a412-2f6c7169d557 | -2.53497 | -54.01059 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90fdfdef-a0f3-3337-8a1d-38d9c719874b | -4.34869 | -45.88157 | 2024-11-20 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 95fd2797-dd06-39d8-bf73-eebd6324cf7d | -4.38665 | -47.7565 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d65f74e-cf7a-3235-8f14-fced21b3bf87 | -2.41317 | -45.81803 | 2024-11-20 04:50:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dc62f6a-5e9e-3b01-b8b5-b3990f5e4fa6 | -1.54644 | -51.11336 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0cc883c-2ef3-3baa-bf63-8c131e4e7c46 | -2.69984 | -49.32365 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3b9ca4f-20af-3514-85c2-3c0c70ef9167 | -3.24743 | -48.44291 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd3cbeb0-9e6c-37cf-9044-16fd03eee9c0 | -1.33853 | -52.2395 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c1693a-c179-3930-9d0a-5d5e5c5700e5 | -4.38451 | -47.77071 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bf03d789-1262-3199-b118-3422f9f15b1b | -1.47519 | -51.13406 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13c5ede0-3bc3-3d21-8364-b67c9ae1d51b | -2.63021 | -48.48473 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7efdc9d9-ec19-3694-932a-128dbaeed2f4 | -4.38024 | -50.41969 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87c8f6d2-b66f-3325-a4ed-cbc374d2025a | -1.54699 | -51.10992 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f5f94be-3c15-39b2-bf93-cf558a83dabc | -3.04965 | -54.40517 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6522ccb2-966b-3f91-807a-ef52e96f1e4b | -3.39547 | -54.27153 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2ba93e5-33b9-3840-80cd-e2eba10ce17c | -3.97534 | -51.24722 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33db6953-c3d8-3da4-9810-e3c6b2b60310 | -1.20167 | -51.77645 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 49dcc506-94e0-3d30-90c7-ce7418b4a684 | -2.62548 | -51.80496 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 185da29a-743b-3980-912b-5487dfa20b32 | -3.70864 | -53.75237 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b3d119f-0858-344a-8b3c-06a7be4b33b2 | -2.56777 | -54.07544 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc48991b-5761-3edc-b522-d4c3951c0194 | -2.09122 | -48.37916 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ccb2600-b593-3941-9238-7af3e16b33da | -2.69083 | -51.70906 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23f49361-2b78-351e-93f7-8e21b8d6ba3a | -7.17918 | -48.76085 | 2024-11-20 04:50:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 949cb7e9-d257-3976-bd88-3f2f8f66467c | -4.38764 | -47.77602 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5f2d7d4-2a59-3fa9-946a-9e876a50a26c | -2.88831 | -41.76154 | 2024-11-20 04:50:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6aa36a24-ff0d-3363-bed3-fa779de51581 | -2.31789 | -48.85471 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a19502b-4502-3add-a9df-562ccf07fb50 | -3.57321 | -51.56477 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98ac4f57-3a7b-3ca3-9ce7-63777ff34117 | -0.77896 | -51.75295 | 2024-11-20 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aec4d63d-44bb-3f1e-83ff-6a9b0368395f | -2.85321 | -54.00732 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b0d0cb3-97ec-3f13-bb77-a393480be29e | -0.79516 | -51.23964 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54956681-6646-340e-8168-61ab7f38aad2 | -1.23766 | -52.02015 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8732f3a-5255-32d6-89a6-c06d98a72cb2 | -3.18658 | -48.57121 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdd2196b-5732-3ef9-a8ce-e7f693d28d59 | -2.7658 | -54.0773 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 019bbbe7-8a3a-3a2d-aed2-349d0a68fdb8 | -1.7343 | -52.79052 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b3a406c-2a44-3f3c-9a32-93d67ce7f7f1 | -1.24547 | -52.03562 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d152a906-2f69-36ef-a91a-3552a1c864ee | -1.47607 | -51.96813 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3153ced3-7c03-3211-b706-e379afa9f277 | -0.77842 | -51.75642 | 2024-11-20 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 232d42f6-42d6-357c-a087-8fcffa55a09e | -2.85883 | -51.84473 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89b922bf-2b5a-339b-aefd-e2a88ffd9513 | -6.63862 | -47.35225 | 2024-11-20 04:50:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d70e0bdf-0655-3e20-a927-78e503c909cf | -1.22706 | -51.74498 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b012e50-d999-355e-9e7c-3c6716f57b20 | -1.85748 | -54.27744 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 50925e95-1f16-37da-993e-d83291b46071 | -2.7143 | -53.17065 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b32fe6-4fdd-3a5a-92f9-95226e27e83e | -1.42111 | -46.79597 | 2024-11-20 04:50:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 514afc3e-4fc7-3f04-86c7-53ae0672cc16 | -3.04319 | -54.40009 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b20af9e-492a-365f-b477-2134b0a98e6f | -2.13026 | -48.53238 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb23e7f2-9ea7-3667-b453-7d58fb8c5dda | -2.70278 | -47.98397 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77094794-5ed0-373e-bd85-201029babaf8 | -2.02819 | -49.16275 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd653c27-f81a-3adc-b3df-560cf80fc172 | -2.26403 | -50.80713 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ebf1efa-9b8a-3e26-bf1d-aab75afa9c02 | -0.88196 | -51.72289 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a358603-6fa9-3b94-83e9-cf5c733126cf | -9.16917 | -44.72614 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b50a283-71fb-3092-8699-775219cd508c | -2.65725 | -46.60763 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d96858f-a77c-3c12-be34-e35c94c3d4e0 | -2.8046 | -51.80453 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db2a0aaa-4edf-3109-8a64-05aa59359613 | -1.47287 | -52.52049 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7df0ad36-88df-367d-be52-c54823034bed | -3.23564 | -45.56376 | 2024-11-20 04:50:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30adc956-cfa6-346d-950f-c80bb86b6f68 | -4.44101 | -46.59236 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 10cc75db-9025-38ab-9604-5f14e108f1bc | -2.82587 | -45.12927 | 2024-11-20 04:50:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ba0ec17-1da0-3ba9-82d6-968c9deae7a3 | -3.51236 | -53.79723 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e79a8ce-c6e8-3b57-9a1e-021984576649 | -1.63978 | -52.68074 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb877017-9a83-3320-9ab9-55cda7d8ea51 | -2.06243 | -53.42709 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c07ec4b-4699-3d38-b185-63c5aed67151 | -1.09557 | -51.74237 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf9f1b55-3e89-3eb1-a828-b37256816d97 | -1.246 | -51.75149 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 912e42df-6468-3f07-8dce-f7694e03ccfa | -0.82743 | -52.86861 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a9045e8-f9ee-34d9-a369-2c68300b9aea | -1.06347 | -51.75155 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45185b65-7992-3197-bda0-4e1f7df3a036 | -2.60778 | -54.05359 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0728acc3-c6d6-3b5e-8d1f-e0f598b72451 | -2.71779 | -49.34598 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a0aa0f5-b66a-34d3-afa5-cfc51fff6163 | -3.13703 | -49.12648 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4feda70-bc58-348c-9c06-d0067b2ab549 | -2.92287 | -53.06674 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6771af4c-ce64-388d-aef7-a56999d24d4f | -1.88463 | -50.96483 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b54c5c84-0f3c-3019-a3ce-bc282800eb20 | -2.99929 | -45.43694 | 2024-11-20 04:50:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b51d35fe-2d59-3322-80a6-51cc6105da6b | -1.46116 | -51.99781 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d09550d-95ec-38a3-9995-3ce96a1f23bd | -1.40779 | -51.11312 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bb98654-24a9-3019-9742-eaf000019ece | -2.65649 | -48.7896 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb5da693-e726-37cc-a908-fdc827d6827e | -2.55259 | -48.04948 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be5cff8d-cae0-35d9-aa54-9c331a3a455c | -3.67329 | -54.27392 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7a651189-204a-3862-afbf-105339f36115 | -2.27675 | -53.64011 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fae7a9e9-6d76-36bd-8189-2f80818dcea2 | -3.01013 | -51.0117 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 989777f6-e902-3ce8-84fc-110eeada8ec2 | -1.74074 | -50.48246 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f2e00ed-4a5c-38c0-8606-363ecf7d63e8 | -2.92849 | -53.07499 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7392647-458f-3ba7-8763-9164f8d11f55 | -1.04794 | -51.74205 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README58.md)
