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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87ace545-708d-3ab6-ba58-8fd0d22f3059 | -17.5675 | -57.5351 | 2024-11-15 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 9ad2433f-3a73-3079-92d2-a866b745a167 | -17.5675 | -57.5351 | 2024-11-15 09:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| dbdebb40-fc79-363a-9f7a-c16341f7173d | -17.5675 | -57.5351 | 2024-11-15 09:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| ae8ef206-a02d-3f35-8478-a231c6d8d30a | -17.2543 | -57.4698 | 2024-11-15 09:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 819287c0-78b5-3c18-9518-426e62bee49c | -17.5675 | -57.5351 | 2024-11-15 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 22dba1a0-7efc-3c6c-8a10-7ec35f816c00 | -17.5675 | -57.5351 | 2024-11-15 09:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| cdbbaefc-5e76-36bd-956d-fdd028958627 | -17.5675 | -57.5351 | 2024-11-15 10:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 817bd196-63bf-393c-940e-96e9be843612 | -17.5675 | -57.5351 | 2024-11-15 10:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 4ed38967-efdd-31f5-8ba0-6b1388a4e215 | -23.2596 | -54.9373 | 2024-11-15 10:20:00 | GOES-16 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| 6fe1699a-0d94-3830-957c-fc3f83ddaa26 | -17.5675 | -57.5351 | 2024-11-15 10:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 576b6809-efed-3466-8798-9e21a058f899 | -17.5882 | -57.4711 | 2024-11-15 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 5e8d6cd1-5dbd-3521-87f1-3a12205ba7a8 | -17.5675 | -57.5351 | 2024-11-15 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| 598121e8-566b-3c50-9fa2-60f57b9db01b | -23.2596 | -54.9373 | 2024-11-15 10:30:00 | GOES-16 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 147.8 |
| 3bb4c86d-a25e-3752-9bbc-26bc0889e1d4 | -17.7048 | -57.5597 | 2024-11-15 10:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| e18cc3de-8432-37fe-a801-2911104fdb2b | -17.2543 | -57.4698 | 2024-11-15 10:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 2dadc9af-5a98-30c0-b14d-429a1ce3a659 | -17.5675 | -57.5351 | 2024-11-15 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| 56dd9897-6e3d-30d1-928c-137fb12f59a0 | -17.6851 | -57.5621 | 2024-11-15 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 4b28d7e2-9a8d-3db9-91b4-dd474f310ffa | -23.2596 | -54.9373 | 2024-11-15 10:40:00 | GOES-16 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 105.9 |
| 67314652-a037-3415-a53d-ff84ff380337 | -17.5882 | -57.4711 | 2024-11-15 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 71148aec-bdc3-352a-afff-5f118111ee66 | -17.7048 | -57.5597 | 2024-11-15 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 265.9 |
| 83354a0c-beb5-3002-9ac6-ed768e64ea2b | -17.7045 | -57.5803 | 2024-11-15 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 1e4cc398-336a-3b27-922b-fd1512b99d71 | -17.5879 | -57.4917 | 2024-11-15 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| eecdee67-100a-3c5e-bf28-9911daee1132 | -17.7052 | -57.5392 | 2024-11-15 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 942194eb-c7f1-3484-a0a4-2e304760237e | -17.5675 | -57.5351 | 2024-11-15 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| c2bcafb8-a796-3862-87ab-2814965f4f50 | -17.6851 | -57.5621 | 2024-11-15 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 4a77b912-2f34-3e77-8af4-8fdb263d7031 | -17.7045 | -57.5803 | 2024-11-15 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.3 |
| 99c1833b-f631-3216-a60f-b6e16413ccef | -17.5882 | -57.4711 | 2024-11-15 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 5adb1363-c400-31ff-b219-c5f2b5b54e4f | -17.7048 | -57.5597 | 2024-11-15 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 332.9 |
| c633cee4-f1e0-3668-9a2e-649592d8a944 | -17.2543 | -57.4698 | 2024-11-15 10:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| bfa59dd6-4e69-3b20-857f-f98a5f36e22b | -23.2596 | -54.9373 | 2024-11-15 10:50:00 | GOES-16 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 171.1 |
| 8e3c47fc-abff-3aff-988f-53a84e8e7366 | -17.2543 | -57.4698 | 2024-11-15 11:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 4435c87c-a498-350b-8b22-e513294bcd93 | -17.5879 | -57.4917 | 2024-11-15 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 2b66182c-e49a-34b6-9860-38aff82655d5 | -17.6263 | -57.5486 | 2024-11-15 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| f57661b8-198d-3a6f-9b27-108d1d2a8da1 | -17.5869 | -57.5533 | 2024-11-15 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 6f807e6b-5c44-3325-8887-1f93164ae281 | -17.7048 | -57.5597 | 2024-11-15 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 228.5 |
| 0442870c-3321-3fa3-a16f-09524e0f93e4 | -17.5675 | -57.5351 | 2024-11-15 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.4 |
| 07e86ace-a03b-30ad-87f5-e5e8b1865d2b | -17.5882 | -57.4711 | 2024-11-15 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 26c01dd8-b5f8-3c27-b715-050027f2a33d | -17.5879 | -57.4917 | 2024-11-15 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 1495a325-94c9-38a8-8cbe-459daaa10e65 | -17.2543 | -57.4698 | 2024-11-15 11:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 7f40c6a8-78fa-326e-a95c-a40ef4933aa2 | -17.6263 | -57.5486 | 2024-11-15 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 26588779-6874-321b-8cd8-405913705c67 | -17.5882 | -57.4711 | 2024-11-15 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.4 |
| 1ded4bba-19ec-3185-ba4b-704cc9d58cbf | -17.5675 | -57.5351 | 2024-11-15 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.4 |
| fbc24228-e55d-3a23-a5c0-cd623fa1d1e5 | -17.5869 | -57.5533 | 2024-11-15 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 9bda905b-8dc1-3685-96fa-2ecc85294c5a | -17.7048 | -57.5597 | 2024-11-15 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.7 |
| bbabba3c-d5b6-323b-80e9-51c5b6918407 | -17.5879 | -57.4917 | 2024-11-15 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| b03f9c51-6be4-3a28-a696-62d22591fb4b | -17.7048 | -57.5597 | 2024-11-15 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.1 |
| db98a1ca-50ce-3df5-b910-dc8c1a023e1d | -17.5672 | -57.5557 | 2024-11-15 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 88e101f0-be7f-30a1-b09e-fde2b18aede2 | -17.6263 | -57.5486 | 2024-11-15 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 2b2393ff-2fb5-3087-a27d-6458b6d9c282 | -17.5675 | -57.5351 | 2024-11-15 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.2 |
| 2a5cc93e-7d06-32e0-a8ab-aa03e88342fd | -17.5869 | -57.5533 | 2024-11-15 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| d4813957-c07b-3ae9-a432-85082510b5fa | -17.2543 | -57.4698 | 2024-11-15 11:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 99f559e1-6be9-34a5-b8d6-485606859e72 | -17.5882 | -57.4711 | 2024-11-15 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.5 |
| 08152084-3997-3ce4-bc4f-44d52904f1fa | -17.5675 | -57.5351 | 2024-11-15 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 5ae399af-d7ca-3cf1-8918-3a185226810e | -17.5879 | -57.4917 | 2024-11-15 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| d75ee590-8b25-375a-be2a-3216b2e8289f | -17.2547 | -57.4493 | 2024-11-15 11:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| bc03cb13-d0f7-3872-b16d-7cc9ea35b7c2 | -17.5869 | -57.5533 | 2024-11-15 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| b2774ea1-b091-360e-81d6-b3b6db8f2c64 | -17.2543 | -57.4698 | 2024-11-15 11:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| d9490079-17ec-3301-983e-9c079c7ff210 | -17.5882 | -57.4711 | 2024-11-15 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.6 |
| b79c96b2-7cf3-39ea-8dd2-fe7deaadf5f6 | -17.7048 | -57.5597 | 2024-11-15 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 267.0 |
| 6fc93041-9755-3d24-9a76-57c82d03b864 | -17.5672 | -57.5557 | 2024-11-15 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| f45be513-df7e-3068-9bad-216a77602abe | -17.6263 | -57.5486 | 2024-11-15 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| b55aab9d-3954-31a3-b130-9952c368e5f2 | -17.6263 | -57.5486 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 300dec82-be24-36cf-a01b-1c563ac6ef04 | -17.5879 | -57.4917 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| cf804b12-89ae-365c-9ea6-350ae3fa4cd1 | -17.5882 | -57.4711 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.1 |
| 8bf6240c-bb59-3dea-9535-5dd29119167f | -17.2547 | -57.4493 | 2024-11-15 11:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 78caba45-c47a-33d5-abf4-aa3e6458cf73 | -17.5672 | -57.5557 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 0ea0007d-f064-3159-b8dd-59a6b3d2b7ba | -17.7052 | -57.5392 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 89979013-ea3f-3e8e-9d7b-aeeca9eaf7d4 | -17.5675 | -57.5351 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.1 |
| aea1bd2b-278d-31d8-bb85-f6140d18d236 | -17.5869 | -57.5533 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 9498e07e-22a0-3511-919a-b759093e6b3a | -17.7048 | -57.5597 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 202.0 |
| e6944da4-9556-3692-a9bd-1d36b72e0a14 | -17.2543 | -57.4698 | 2024-11-15 11:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 738eb01d-c5a4-377c-a014-d7de2c81eae4 | -17.5865 | -57.5739 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| dcea9b8d-a0c5-32ef-a519-71d44d2e9382 | -17.5885 | -57.4506 | 2024-11-15 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| b82b9b13-ea7b-3b7a-99b3-ee0d148a85a4 | -17.5885 | -57.4506 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 40578979-7a50-3918-9c16-96b418dbdf88 | -17.5882 | -57.4711 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.1 |
| f93d6d97-44b6-38f6-bf52-af51c19a2e69 | -17.2543 | -57.4698 | 2024-11-15 11:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 956d7fc0-d075-3f37-af10-f1e44ca6ed11 | -17.2547 | -57.4493 | 2024-11-15 11:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 51962058-4deb-31aa-8d94-c7dac8334737 | -17.5879 | -57.4917 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 4c92d76e-c078-3da2-83cd-c727bfdf0b11 | -17.5675 | -57.5351 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.3 |
| 31ebb9b7-1174-3a3c-9cf2-18a83945dbf3 | -17.5869 | -57.5533 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.5 |
| dde9b246-b214-3cd0-93ff-869a3b8219b3 | -17.5865 | -57.5739 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 2dd630c5-dddb-36d2-b260-60ea9bb0eed9 | -17.5672 | -57.5557 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 6178d3ce-e0d1-3995-b938-a2cbfa9e246b | -17.646 | -57.5463 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 87a9799e-8d97-33fa-af56-2ded3d66fc95 | -17.6263 | -57.5486 | 2024-11-15 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 4964a2a0-9c67-3281-a401-a7636e1c037f | -17.6263 | -57.5486 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| b887320d-fb4d-3e4f-a35c-dfac314666e5 | -17.646 | -57.5463 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| d3773307-52c2-3d17-bf5d-bc08cd85695c | -17.5869 | -57.5533 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| b286deac-77e1-34da-9a90-eee630b91e5f | -17.6079 | -57.4688 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| b1475606-485e-3902-80b1-ce08ed41562c | -17.5885 | -57.4506 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| e3829862-9f18-355a-bc5c-22533b129560 | -17.5675 | -57.5351 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.2 |
| 735bd640-65ec-33d4-af2a-5ac83971b443 | -17.5865 | -57.5739 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 7a3181bf-f879-3191-9e4a-7518b097a815 | -17.5879 | -57.4917 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| d6c0f333-948a-3d4c-a2a8-ae888db33755 | -17.6477 | -57.4434 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| c576b9b9-d906-3a82-9047-1780d7221a22 | -17.2547 | -57.4493 | 2024-11-15 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| b4a116cf-90a8-3154-a3d7-694fc5857aca | -17.2543 | -57.4698 | 2024-11-15 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.1 |
| aa2337b8-ae2a-3ed7-97d6-b9ce845abb75 | -17.5882 | -57.4711 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.5 |
| 03cb097e-7cae-33fb-bfee-ee6cdf7c7faa | -17.5872 | -57.5328 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 03de65cd-fa22-3452-8a8c-2d66523fd9e8 | -17.5672 | -57.5557 | 2024-11-15 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| f03fe0e0-f9fa-3ea1-85b8-954f949ece47 | -17.69 | -57.58 | 2024-11-15 12:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26fe6e20-5bf8-353e-b129-d8ddad18c3f6 | -17.69 | -57.5 | 2024-11-15 12:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README35.md)
