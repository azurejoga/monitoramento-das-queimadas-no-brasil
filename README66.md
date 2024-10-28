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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efb1ef92-5f6d-3c84-ad33-4a3887e17596 | -1.76189 | -53.99922 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a3f7875-0a6b-3583-80bd-b618e6cd5f9a | -1.76134 | -54.00271 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 219a06ef-c2e3-3b96-b473-72d76cebb115 | -1.75857 | -53.99871 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34bb474e-3b5a-36c8-b8fe-af0ba3a6c6c0 | -1.75802 | -54.0022 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23cbead3-6f8c-302a-b802-5a93d0e7f1be | -1.65878 | -53.39917 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2ce0dab-4aa9-369d-bce3-f461478acb1d | -1.60833 | -54.77462 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 083d8cf4-7edd-3077-b3c2-ffe67f174ca0 | -1.56955 | -54.44087 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b93470c-1c38-38d6-894b-643b94dd7e21 | -1.51765 | -53.51789 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d498e7cc-e194-305e-88bd-fb0aa2347fc7 | -1.51754 | -54.66021 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf7233ca-68c8-3620-84f2-e10965ef78f6 | -1.45381 | -54.09732 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 688648b9-2fdb-3a63-af00-99448fbbce58 | -1.45271 | -54.10433 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0c43245-6f1d-338e-88ef-edc7a1a98dce | -1.44541 | -54.47229 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775e6963-5269-32d5-8847-c1350d251bfb | -1.44323 | -54.07776 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22b1629a-7f55-3bdb-a570-6155dc3a965d | -1.44045 | -54.07378 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21f08586-afd9-35e2-8db8-c89a9cb3a659 | -1.43711 | -54.07327 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 709c1c0b-a0cb-3696-9f93-e49b67de5698 | -1.42936 | -54.07917 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2b3396b-1726-324f-a398-0ff4a8a7fd85 | -1.42844 | -54.23725 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 081a649f-5f1d-36c7-8d98-020b20c50117 | -1.4279 | -54.24075 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e8f2af8-48bc-35f1-999c-adc82b36df45 | -1.42456 | -54.2402 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7dcd1931-e33c-3bb1-9869-9ffccaedb8bf | -1.42329 | -54.11773 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4723fe80-f1a1-3b43-a226-a1d72e10f3ab | -1.42127 | -54.47244 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b44a08d-657b-3307-aeb8-4627695245ca | -1.41267 | -54.05518 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edf4224a-9882-3c2d-9662-d6f58f830396 | -1.41212 | -54.05868 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b0f6ad2-6352-381b-9579-b4fa422e2ed1 | -1.40271 | -54.07507 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d031e74d-560e-3ede-a424-cccca9bd35f8 | -1.40268 | -54.05361 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1764365b-af06-3cf2-bfa2-259ab959a7ea | -1.40213 | -54.05711 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 122de318-a5c2-3d73-80c8-e349f6b0c18c | -1.35242 | -54.61176 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a30115bb-a75d-3625-a9c2-03bf0159d834 | -1.34905 | -54.61121 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d2d505b-43b0-3af7-8f42-7efd60326af5 | -1.34848 | -54.61481 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c086a0cd-5485-3173-9314-af2bccc99803 | -1.34568 | -54.61068 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aacda1bc-bc01-370a-a836-e8106e6f2d41 | -3.52704 | -54.67506 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2aa5ac1-eb22-37f8-93fd-4cff9eab6253 | -3.52649 | -54.67858 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00dedf0b-ab60-3b8d-a245-46ffd6f25d85 | -3.52314 | -54.67807 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30da019a-6aab-34c5-8edb-2868ccd71b97 | -3.5092 | -54.03332 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 255ba70b-17d3-3614-a14f-78dfafa91d0e | -3.50589 | -54.0328 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f39eb92-dbff-35fb-a100-a2b6b9db819b | -3.49005 | -54.43558 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2103cc1c-55f1-358e-bd10-e22e9a4f83fe | -3.4832 | -53.98337 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5521ed85-cbe0-3d2b-a5a8-a1f0bf8dae67 | -3.47478 | -54.57328 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 094c2d05-d025-3b5a-b52a-c94f1c98191c | -3.47144 | -54.57277 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93c955b1-3a14-3a77-8613-5d19f005136f | -3.47088 | -54.57627 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79ca4da2-74b7-387f-a7d4-ee742f7bddb2 | -3.4593 | -54.19911 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8024d8bd-5e10-34dd-b249-e8d657e9e3e5 | -3.45875 | -54.20258 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74fc2bd4-a5a2-34e5-b6f7-129369a3f04f | -3.45744 | -53.84184 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c49b1569-3fc2-3a3a-99b0-b1a0d74a1dcc | -3.42915 | -54.58395 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2eaec24-f862-39fa-af3c-6a7651079cba | -3.42859 | -54.58747 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e3ba5a3-5d92-3cc5-a734-838c43db0f83 | -3.42582 | -54.58342 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d0afa57-781e-3a95-823c-90ec21838a4c | -3.42526 | -54.58694 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e08d4602-f300-3ad6-8675-670e55af67e3 | -3.41571 | -53.87057 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f3cd6d4-b5bd-3409-ac0d-a37ba12e5228 | -3.41301 | -54.49166 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 517e2623-1bf6-3581-a981-77f38cfc6651 | -3.41246 | -54.49516 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ca1900a-2f30-3ca4-a011-042d1fad66f6 | -3.40968 | -54.49115 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8ed054c3-4a34-315a-bc02-262cb9dae9d3 | -3.40912 | -54.49465 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19a2d3b2-8324-3b60-957d-7c4bafc57702 | -3.40857 | -54.49815 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15db8e0c-e728-3f0a-b5ce-5b8627ab0977 | -3.40635 | -54.49064 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e62dc10-c7c4-305d-8e56-42b86192de34 | -3.40579 | -54.49414 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed7cb2c2-e7a7-35ac-99fe-0952ef3980c6 | -3.39682 | -53.79721 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa6c6815-6439-339c-af55-30c00fc032d1 | -3.37519 | -54.60081 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8368f7b1-50e6-3123-9b4a-66e34bd7b832 | -3.35389 | -54.71315 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d02dc5-9e72-3368-a94d-c8dc159c9b1c | -3.33894 | -54.61693 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 497be8e5-b8c7-3a02-ae54-d4e5a1438638 | -3.27378 | -54.14478 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4c744d4-916c-3f69-b4ac-c2c069f40235 | -3.27272 | -54.58139 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9adc2563-1f40-370c-a3ff-7d9d3a886827 | -3.27047 | -54.14428 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1f0e3b5-d735-3369-a0aa-253846bb89df | -3.25838 | -54.17789 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0219c4c-2d77-3496-99b4-1e381cd84fc3 | -3.19923 | -53.81867 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1eae4996-deb3-3b2e-ba63-44d4218f31a0 | -3.19869 | -53.82211 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e5fc38a-1f5a-30da-90ea-3c339edca96a | -2.46969 | -54.74973 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 015779a1-917e-3cfb-9e8b-9266ea7a29a5 | -2.45737 | -54.03387 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be1621c1-0891-31ff-9428-d486d6d9c582 | -2.3962 | -53.79774 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8764576c-011d-395c-9f2b-a17256de3c1c | -2.33763 | -53.90828 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc0f47be-9671-3734-99ed-6dfeebb660ea | -2.33431 | -53.90777 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6450348-1558-3c9a-904c-81adebcce9c6 | -2.32333 | -53.93443 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c25bb3f-9f73-36c8-a543-b87d2cbc562f | -2.31947 | -53.93737 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adae754d-1c01-326a-99e8-3820b301ecf1 | -2.28244 | -53.80413 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 231590be-2d2c-3748-8e95-804d2828a736 | -2.2819 | -53.80758 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9e794ca-c990-3d37-8b4e-40a79077a43a | -2.28069 | -53.77208 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b58314f-d6a4-3530-866a-ea6ea7e30579 | -2.28015 | -53.77552 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 97e72941-06ea-33ef-968e-6096fd57be8b | -2.27961 | -53.77897 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2da78a71-688f-363b-b9f1-206d272becac | -2.27799 | -53.78931 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bcc22711-07f5-371e-8bb7-dea6d5740d78 | -2.27739 | -53.77156 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01fbdaa3-9f60-3bc9-a17f-d340b75729c5 | -2.27684 | -53.77501 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7559a801-a37c-3d2c-ad8c-901a41742421 | -2.2763 | -53.77846 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0e3dc184-651e-3cb1-a798-531d9cda65aa | -2.27576 | -53.78191 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecb993bc-3eb3-3d04-ab9b-204dbe6a8dbf | -2.27522 | -53.78535 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d438bcd1-ceff-37a4-8b7e-b0a4eef4e10c | -2.27468 | -53.7888 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fccd84ee-bf49-384b-8139-b9eeca86f8c4 | -2.27414 | -53.79225 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6af817e2-58f9-3e04-9b11-3002bd5af1f8 | -2.27354 | -53.7745 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bfec11a5-c2b2-3808-8cda-d1632d78749b | -2.273 | -53.77795 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b6097902-dfe1-37b2-ad26-9404bbf5d355 | -2.27246 | -53.7814 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e5987fd6-5bee-322e-a2b1-543b4cd1fe5e | -2.27191 | -53.78485 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 42f18b40-b9c6-3a80-9079-267091b89715 | -2.27137 | -53.7883 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 6a97facc-024e-3434-9bca-14b78d02ea42 | -2.27083 | -53.79174 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 77c31971-6bf1-3507-8254-ead1191634a7 | -2.26969 | -53.77744 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cc7cbc43-9518-3079-945a-37164e359982 | -2.26915 | -53.78088 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 747db9c6-1865-3cd9-80ac-8cc052f59719 | -2.26861 | -53.78434 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 94846330-824f-35ec-b2da-930675a932a0 | -2.26806 | -53.78779 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| bb5bac14-3d79-3cff-9dc5-8f10213f7634 | -3.68363 | -53.83146 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8063c699-5ba4-38ec-825f-1d70bcb7fa2d | -3.66938 | -54.07681 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12356f54-05ec-3876-9583-a5f39f2674fa | -3.63451 | -53.97177 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b57275b-a48a-3727-b021-20458ad8c32c | -3.61375 | -54.03916 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a9f7f64-3770-3997-97a6-78973ea58389 | -3.5998 | -53.95582 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README67.md)
