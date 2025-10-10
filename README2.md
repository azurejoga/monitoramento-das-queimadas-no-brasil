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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99025255-2480-35e3-89d8-6aa99393860d | -8.1996 | -43.3189 | 2025-10-10 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| d22ae30f-77e7-36d9-930b-bb7444ad6ea6 | -8.8435 | -46.0519 | 2025-10-10 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| dafdb924-5ef5-3a1e-a26c-44200561fac5 | -6.4092 | -35.0431 | 2025-10-10 00:20:00 | GOES-19 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 133.6 |
| e018b288-65dd-32b8-91a9-7f30b3c0d17a | -8.1993 | -43.3424 | 2025-10-10 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 80e2c520-2215-388e-8b7f-fc3c3bbe3049 | -5.4752 | -43.054 | 2025-10-10 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 19c38027-2333-3f6c-8b17-6749a530a566 | -15.3974 | -48.039 | 2025-10-10 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3a1df4ac-26fa-3d05-8447-c18c820d461e | -4.6504 | -43.2038 | 2025-10-10 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| bff76272-f636-34b5-a02b-8fd4d2bade58 | -13.387 | -47.7555 | 2025-10-10 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e2fbe3cf-1f7f-3706-b9b3-06353435365e | -5.494 | -43.0526 | 2025-10-10 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| d04ed7cf-f042-365e-a4c9-fa9f9aee9463 | -7.4154 | -45.9211 | 2025-10-10 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6a58b584-b9ab-3629-9211-e93f429b051b | -13.058 | -43.8571 | 2025-10-10 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 9fca7869-0eb7-323c-a18f-fe332d16995c | -5.4935 | -43.0995 | 2025-10-10 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| a967e32f-2be7-3c93-aa98-a32d62fc24d9 | -3.3367 | -44.4034 | 2025-10-10 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| eca8175a-5dc6-31cb-bca6-dc85bd6801d2 | -6.5849 | -44.6327 | 2025-10-10 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 00871840-8011-39eb-a62f-68370055fe3f | -5.4937 | -43.0761 | 2025-10-10 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 2c5acc13-bfde-355e-9794-eabf184108a2 | -13.0778 | -43.83 | 2025-10-10 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ee49aba3-652f-3ee2-8c8c-ea2d4117edea | -15.417 | -48.0356 | 2025-10-10 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 5fb140dc-48c2-3034-a002-c445cbddfe6f | -3.7936 | -49.4424 | 2025-10-10 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 081504ea-d8ba-3486-a7d7-b23f63280ccf | -17.9175 | -45.0194 | 2025-10-10 00:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 34d7e739-41b1-31fd-84cf-a5ba7cc78b59 | -8.1993 | -43.3424 | 2025-10-10 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| b45934fa-d4c1-36f1-b64c-7d2f5eee0a76 | -3.3366 | -44.4263 | 2025-10-10 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 72cd48ed-9c0b-3fbd-9ce9-d79572e21be3 | -10.1711 | -44.5727 | 2025-10-10 00:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 373e0a5f-bc73-3af2-8feb-d275cdd8c6a1 | -7.3966 | -45.9227 | 2025-10-10 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 14fca637-1ddd-3cbc-abdc-81b1c9f71abb | -13.387 | -47.7555 | 2025-10-10 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 3a5dfe51-fc47-34f7-aecc-64c862b496b9 | -3.5371 | -48.9195 | 2025-10-10 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7d84305b-c220-320d-bf68-303c366c736c | -7.4154 | -45.9211 | 2025-10-10 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1a5e7d50-be21-343d-a05b-69745ba00c58 | -17.9577 | -45.0103 | 2025-10-10 00:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 129.0 |
| b3266554-c731-3841-a352-c3d00ce8b153 | -3.0013 | -48.7453 | 2025-10-10 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 0c21c0dc-bc83-3aec-8b08-bfe1db79540b | -5.6373 | -45.9705 | 2025-10-10 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4d582628-085a-3529-bc64-17c43b978a16 | -3.7937 | -49.4211 | 2025-10-10 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c5c874c9-ab3f-32d8-a7d7-639169788e89 | -15.9195 | -43.2779 | 2025-10-10 00:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 416.2 |
| 44eb1e93-18e0-3b14-8644-3870748a5c85 | -17.9376 | -45.0148 | 2025-10-10 00:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 394.5 |
| 4ec25f14-6e75-36d7-9f8f-81af5d1b6dc0 | -8.5029 | -46.1545 | 2025-10-10 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1599c38b-211a-3916-aeaa-652916c0e817 | -15.8997 | -43.2822 | 2025-10-10 00:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 2a16f8e9-1d08-360e-9c7d-6a3828c887ed | -6.5849 | -44.6327 | 2025-10-10 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 081b4b16-5679-363f-8624-fadc3dfd014b | -8.1996 | -43.3189 | 2025-10-10 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| c11eb572-8384-3f10-bab9-47c77ff488e0 | -7.7755 | -44.0396 | 2025-10-10 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 73bd88b5-ecc5-3ab9-a811-3803ccf7da63 | -15.8991 | -43.3065 | 2025-10-10 00:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 117644f5-a649-34c5-a4a5-95884ec8bc94 | -3.7936 | -49.4424 | 2025-10-10 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 90ffab39-2213-3ca0-9ac3-44b9a669d52b | -4.6504 | -43.2038 | 2025-10-10 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ad3c9174-64ad-3e5a-b4ee-c62c84448786 | -13.0778 | -43.83 | 2025-10-10 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ed303c2d-4a27-39dd-b5ad-1f39a52c1ea5 | -17.9382 | -44.9909 | 2025-10-10 00:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 96cc6b55-53d0-35e5-85fe-624b1c0ca7fb | -15.9189 | -43.3022 | 2025-10-10 00:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 369.3 |
| 76cec748-7e69-32a1-87e9-651a741010c8 | -5.656 | -45.9692 | 2025-10-10 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 414372c4-82ac-3fe7-839c-417635921290 | -5.4937 | -43.0761 | 2025-10-10 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4b316769-23be-3b34-a04c-7c3b3dd24c37 | -17.9369 | -45.0388 | 2025-10-10 00:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 9cb88a42-6606-3c2c-94ed-3cda834e4e9f | -6.5851 | -44.6098 | 2025-10-10 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 8e666909-f963-3c5e-9c60-2e9ac905bb6a | -10.1707 | -44.5959 | 2025-10-10 00:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| b1da2ade-ad41-35df-b40c-d249616da77f | -18.05375 | -44.98216 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 50cca723-f9fb-376f-9a1a-9f2cfcbdca18 | -18.64114 | -43.92635 | 2025-10-10 00:30:00 | TERRA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ffa351bf-60f4-3c28-85d3-a513b56afadf | -16.74124 | -43.98211 | 2025-10-10 00:30:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 28fb228d-3ef3-3f45-b997-b298485c880e | -17.9415 | -45.03756 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1eac1158-3805-3ff0-9457-40e9b965da88 | -17.66429 | -44.46232 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 660660bb-ddcb-38e6-a2a7-ef9e60014886 | -17.32616 | -46.8381 | 2025-10-10 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3386080a-3fce-35e6-a4aa-cebcd9b9fd2f | -17.96779 | -44.9608 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 590b2093-4392-3ec2-a601-d80547ab77c2 | -17.99295 | -45.63188 | 2025-10-10 00:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9b0b4e68-8e2f-30c7-b1fc-a3f1ee0f4603 | -17.93371 | -45.03503 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6bc30610-77a8-379c-9b25-e21af52e51d8 | -16.10278 | -40.60743 | 2025-10-10 00:30:00 | TERRA_M-M | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.8 |
| c8ce6db7-0ff7-3791-b7a4-7e7ef284c8dd | -18.03062 | -45.01681 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e0c79185-51f9-3800-83ff-34588e0df1d9 | -18.02287 | -45.01354 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 509b7259-4373-33c2-afe6-9c49cf9a439d | -17.94001 | -45.02763 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2e0e3f3d-1e25-3ac0-b398-c33365f0f60a | -17.93848 | -45.01753 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 124.3 |
| b697ae8d-cdb1-3870-8b8f-b4af6535aa8d | -18.22905 | -43.06862 | 2025-10-10 00:30:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| af3f8317-a349-33ee-9f3a-83fc7dc6aa8d | -17.93075 | -45.01492 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 50defbe1-da40-3f07-9f08-b62ab2955d06 | -16.50041 | -42.79588 | 2025-10-10 00:30:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3dc3a789-68a6-36a8-98b5-8517c2162c8a | -17.95068 | -45.03586 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 188d2ac8-ed3f-3d06-96af-cd4d6b296485 | -18.77605 | -44.62166 | 2025-10-10 00:30:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 0bd2ec44-a1ce-35ee-978e-a52df9e8fc34 | -17.66793 | -44.45547 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7a1c23a6-b863-3785-ad61-06a7eec0a57b | -17.27124 | -47.0408 | 2025-10-10 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7009e10a-0d2a-3046-9bf2-28cc8379b2b1 | -17.21864 | -47.6558 | 2025-10-10 00:30:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0c6540a7-f190-3f08-919a-83ab72e3e9ee | -18.7745 | -44.61129 | 2025-10-10 00:30:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ee4a95b0-edc3-311c-8d6f-190e2aeecb64 | -17.37839 | -46.68272 | 2025-10-10 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef48102a-f9da-37e4-b2c8-79dcf6cda729 | -18.78535 | -44.62008 | 2025-10-10 00:30:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9c2b9a51-491d-324b-99c5-50e0015d9a08 | -17.94918 | -45.02588 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 0054f6b8-db62-3e01-9d6b-efe979c07222 | -17.57618 | -47.18182 | 2025-10-10 00:30:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| feff32ed-8c46-3484-ab94-5826e14871db | -17.65176 | -47.2584 | 2025-10-10 00:30:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| abe15883-59b4-3a13-aaed-5248b5ccc836 | -17.20979 | -47.65712 | 2025-10-10 00:30:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| bcd205be-f4c3-3471-9eb7-3e10d0c2e2b1 | -16.10092 | -40.59306 | 2025-10-10 00:30:00 | TERRA_M-M | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 37735b99-3a8b-36a8-a19f-d6beef2dc633 | -17.94768 | -45.01589 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a3629f94-10cb-35b5-bfe1-870111b9aa46 | -18.23935 | -43.06701 | 2025-10-10 00:30:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 344b9170-245f-3c1f-ad5d-223e4063197c | -17.65049 | -47.24919 | 2025-10-10 00:30:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f1acc440-27a6-37d1-aeb6-545f801405bc | -17.37709 | -46.67349 | 2025-10-10 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 27ce07e5-6f07-3bf6-b265-77c25e11b071 | -17.57491 | -47.17262 | 2025-10-10 00:30:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ee7795d8-842a-317e-989b-787351d38665 | -17.93695 | -45.00737 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 91b7fd98-5e3d-3892-9ca6-3ba2a2e026fd | -18.19964 | -47.97327 | 2025-10-10 00:30:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 847c8d6b-1523-39b1-8877-7175bf1eae94 | -17.57364 | -47.16342 | 2025-10-10 00:30:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b381bfee-f124-3ba4-a8d0-1b40dd70f836 | -17.93224 | -45.02507 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 376.1 |
| 808991b6-5ede-3887-8f6b-3ef2e8aacf1c | -17.66267 | -44.45152 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e0462bd2-d0f4-3ba6-ad58-243c227feae0 | -17.92925 | -45.00471 | 2025-10-10 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3a01b0b4-13f7-3114-896c-175caaf8005c | -15.43024 | -47.97943 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8cf8e51a-32c9-3bbb-a1a1-2f2cd2aa1dd6 | -13.31448 | -47.74163 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 10d49504-f9b8-3f04-bd64-334a4d4be4f8 | -15.08876 | -46.59609 | 2025-10-10 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| aebd74a4-d01c-38b0-b938-afc9554b7ae2 | -16.74233 | -49.83312 | 2025-10-10 00:33:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b3447e55-2633-3cc8-8f3d-e9ad44578fca | -13.35481 | -47.62804 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c24a70c-e42b-3114-a877-21ea73df1877 | -14.43531 | -47.98097 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a9eedbd6-3fb2-3036-a90e-db186d10151d | -13.8317 | -45.8827 | 2025-10-10 00:33:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b824afa-d214-3b65-bf85-eda79ca09363 | -15.40257 | -48.05529 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 437fb25f-c7bd-3199-89a9-9d518cee70d7 | -14.80969 | -44.89236 | 2025-10-10 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 04148892-9527-3b65-b413-5313d949e544 | -10.17609 | -44.55004 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3d3cb525-176f-31a6-b0dc-a90902b9df44 | -9.33362 | -46.10727 | 2025-10-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |


[Clique aqui para ver as próximas entradas](README3.md)
