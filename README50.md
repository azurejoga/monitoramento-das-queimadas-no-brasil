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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcfe41f0-3773-3390-b71d-124e143c3c00 | -4.20187 | -48.13842 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 092e2155-678c-32af-8d0f-7af4e5a02589 | -4.11325 | -48.26753 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 56db7a3c-f246-380e-a3a1-413613376105 | -4.10893 | -48.25797 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 02d7b5a2-6cd5-30d2-a3dd-38321f67caa8 | -4.10811 | -49.06495 | 2024-10-10 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5ff3c9af-43be-3b9c-b35f-885ee9484af9 | -4.10744 | -48.26661 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 7d68888d-8912-3d07-8f2b-cdf43c90c065 | -4.1073 | -49.06968 | 2024-10-10 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e62f0f74-9a0f-331a-aa32-7821dc48d5fe | -4.1067 | -48.27093 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 487285cd-0171-3236-9897-35fdcf0c99c3 | -4.1024 | -48.2613 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a7ca67ce-9f84-344b-bee8-0de7644d357e | -4.10023 | -48.27387 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| dfd9c784-5b51-38da-be3a-0404c4eda655 | -4.09737 | -48.25594 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 90cf2d77-a014-32f1-92e6-f189ff9914e8 | -4.08031 | -48.1158 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a76fdc8-86cb-36e9-825b-2ea4016de1ff | -4.079 | -48.1162 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f63fe59d-2e83-38eb-8b83-cfca00ab7c4f | -4.07456 | -48.11488 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 173bc79f-6541-3829-a6dc-2bc2e00b9127 | -3.93926 | -47.95927 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f3147ed-be40-30ea-afa5-daffdb885f29 | -3.91469 | -48.3464 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9656e47f-3c69-3cda-91a8-762178840497 | -3.90962 | -48.3409 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0bf0bcff-6cc2-3781-a144-ec141f44e05d | -3.90889 | -48.34517 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7f275a97-80e7-355a-98b1-7550ad8fbc50 | -3.91397 | -48.35067 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2989c6cc-b7e3-3eaa-9a28-930d9082f086 | -4.98956 | -48.41785 | 2024-10-10 03:55:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6b7132d-86c3-3428-ad03-9a249183a67b | -4.48694 | -48.10898 | 2024-10-10 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81878da5-f9a9-36bf-840d-743d5f5704db | -4.20601 | -48.14023 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8771fc0a-8cac-3d64-9b5a-b76c83292cca | -4.1125 | -48.27186 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 08ddf9c2-9596-3403-af2f-0138147bbe99 | -4.10819 | -48.26227 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a027dc1f-1c96-3153-a67c-27a0394e9fdc | -4.10597 | -48.27516 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1fdc506a-effb-35a7-8070-91ec9f4027bf | -4.10387 | -48.25277 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 61838ab0-196e-3f49-b4c2-aed886067f46 | -4.10314 | -48.25701 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7391ae43-4c9c-351e-9509-4f559ed3ceef | -4.10167 | -48.26553 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c22b951d-c7a0-3e4d-a503-3a1a7e4cd1a4 | -4.10094 | -48.26973 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 59d34c86-1748-342e-9d3d-c951bee89edb | -4.09807 | -48.25191 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ff0cd30-c209-38a1-895c-9f3e904b20e2 | -4.09664 | -48.26012 | 2024-10-10 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8e85feb6-b348-310d-b386-579479582e96 | -5.7507 | -49.25045 | 2024-10-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d02d3204-a55b-3936-af6e-8eb4252b0c14 | -5.66497 | -48.97054 | 2024-10-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19685255-b868-3fc8-98f1-8496e9a782af | -5.66423 | -48.97485 | 2024-10-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed8f4a4b-3489-3325-a324-a044172f8c5c | -5.59866 | -49.03524 | 2024-10-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2e212ff-d34b-37cd-bd37-931f1f1edc10 | -5.45749 | -48.92675 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 56b94dd8-9a61-3aae-aa66-0b69a8648192 | -5.45569 | -48.92491 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 54e572ee-499c-3bde-bba2-b7fb48044505 | -5.4549 | -48.92929 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 568c2cc2-e203-37ea-8c4a-85210c14cfff | -5.45158 | -48.92569 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0737330a-c58b-374f-9fde-4e1f08f853eb | -5.77748 | -49.01145 | 2024-10-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e42bb08-db92-306b-9258-1e99b94ac342 | -5.77505 | -49.01341 | 2024-10-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 298d2ecd-bb4b-303e-afe3-14a83eba03e9 | -5.75511 | -49.2604 | 2024-10-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59581a98-d682-3e91-81a7-6d854def3c46 | -7.62331 | -49.44361 | 2024-10-10 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78552828-b3dd-3c08-a8fa-4ae4721cc7c7 | -7.61967 | -49.43996 | 2024-10-10 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 883878f8-436e-31f9-8e81-e06197d9aab2 | -7.60303 | -49.39762 | 2024-10-10 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d2e0822-11df-36a8-933e-f921bb8e72a6 | -7.59713 | -49.39664 | 2024-10-10 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98944e07-4393-3c62-99ea-09a1b88fd31f | -8.79246 | -49.66568 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07a3bd35-b2a1-3692-bc89-5622e66d5eae | -8.79169 | -49.6697 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1e39e8d-042f-3a35-9f9d-7eaf944fb087 | -8.78732 | -49.78925 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc141ad1-9558-39f2-8556-1398c4e21e41 | -8.78142 | -49.78809 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 82ece263-5089-3164-adb7-bc361bb4c43d | -8.75781 | -49.78359 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 03b69ca2-e21c-349a-a22a-ae892f759acf | -8.75461 | -49.78017 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec705b65-0a0f-391f-ad7d-6f5f74799fd1 | -8.75382 | -49.7845 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d2d2bf4-8a60-3c16-9a52-7ebd0589f22e | -8.75272 | -49.77825 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9721a49b-115a-38ee-8fd3-8893f9e2326a | -8.74868 | -49.77919 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86bcebe4-b38b-3ffd-b928-e455ce10d05d | -8.66332 | -49.42862 | 2024-10-10 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4c3604e-3010-3aad-9843-85a0f2e6a0f5 | -8.40389 | -49.56565 | 2024-10-10 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46368ce0-7f0c-3590-b738-3f53674873e2 | -8.39804 | -49.56451 | 2024-10-10 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 046cb3c6-02ae-3ecc-a781-9898eea1bf9b | -8.39726 | -49.56866 | 2024-10-10 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c5c398a5-e681-3add-a830-f9abc603532b | -8.33143 | -49.98533 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1cb7247-1eea-32bf-8015-2ec362adf6ab | -8.32542 | -49.98415 | 2024-10-10 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0215bbbf-0ef8-34e8-a793-2d7b411822e7 | -8.07383 | -49.66697 | 2024-10-10 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc03ebf0-5f9e-34c2-8c77-5eb2b255fe09 | -8.07304 | -49.67126 | 2024-10-10 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fdb47f05-0809-3214-9a56-1a8138d20c12 | -8.06791 | -49.6658 | 2024-10-10 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 941d8bae-85b2-33f2-8c12-7fae06c7d7f4 | -8.57728 | -49.21516 | 2024-10-10 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6851a71b-c202-3e92-b9ec-c49c0bd34c32 | -8.57655 | -49.2191 | 2024-10-10 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 937fbd76-481a-3a0d-b078-8c09697373e4 | -8.57157 | -49.21408 | 2024-10-10 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e64ddf13-784a-3951-933b-3bf288999290 | -8.57082 | -49.21809 | 2024-10-10 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f13a12e7-14c9-34dc-bc64-b37271ea2619 | -8.50161 | -48.64239 | 2024-10-10 03:55:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 545bfda9-0ab5-329f-a51a-51b83ae02e9f | -8.49609 | -48.64137 | 2024-10-10 03:55:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b73e038-da10-35a7-bce2-281272114998 | -8.49546 | -48.64484 | 2024-10-10 03:55:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 83d893bd-9717-30a2-88fe-9e6e4ea36345 | -8.49481 | -48.64839 | 2024-10-10 03:55:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5d6bc2b-06f7-3b21-8849-c428e012ad97 | -8.1863 | -49.18734 | 2024-10-10 03:55:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a74b23e3-c49e-3dc7-bd15-2e0ce5f2e023 | -8.14464 | -49.0921 | 2024-10-10 03:55:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df8b9895-ba4d-3ad6-898d-da947fa85275 | -10.06969 | -49.55157 | 2024-10-10 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b49092b9-b432-3b6b-9984-ecd849b7d397 | -10.06891 | -49.55558 | 2024-10-10 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ddb203c-4e83-3517-920e-71ec21fb1475 | -10.0678 | -49.55162 | 2024-10-10 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd0aac07-10eb-33b3-a8b2-1c5ab9fd625b | -10.06705 | -49.55564 | 2024-10-10 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ea986d1-ddff-3089-95d8-7b2536d65dbb | -10.86328 | -49.76144 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d44ba25-d4f0-3076-8a88-a86c603cdd1c | -10.85913 | -49.75238 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b060658-12d7-3a87-b474-8392c823fdfa | -10.85421 | -49.74731 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f28ee11f-dda9-3b9d-90b5-9614b15ad5af | -9.62616 | -48.9915 | 2024-10-10 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 735b8219-bed3-3d39-a52c-5194d71cf8fa | -9.62547 | -48.99528 | 2024-10-10 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 38868d3a-f47d-3d0a-84a0-8a8ac5c6d692 | -9.571 | -48.94991 | 2024-10-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8255bc3-279f-315b-af8e-8d7f37efc952 | -9.56627 | -48.94473 | 2024-10-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b645c97d-8083-38fd-96f3-959e05be8e72 | -9.56554 | -48.94855 | 2024-10-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f3297eb-8fe4-3d06-8392-6ccef92d6691 | -10.52677 | -49.10799 | 2024-10-10 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cea08bea-cf78-3687-80b8-c05fde8e7a32 | -10.52131 | -49.1068 | 2024-10-10 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5ac7d92-6e3f-3e93-97ff-b9b4c8113de3 | -11.20809 | -49.93231 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 074ae6f6-4fc9-3ab7-bc3c-ab349d775d5a | -10.86897 | -49.76252 | 2024-10-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b2ad721-5b00-3bb9-a7d8-ea9d77db1c0f | -3.70248 | -50.17682 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e9e806a2-55c9-3d44-88dd-5b1363a8840c | -3.70152 | -50.18239 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7df6413a-7567-3898-b394-0fde9d4b69f5 | -3.6907 | -50.12797 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42772c9d-6868-323c-a829-25d222b4a857 | -3.68412 | -50.12709 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5c158452-d7b3-3dd3-b1c2-291867fc8fc9 | -4.87453 | -50.53856 | 2024-10-10 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 58136a74-d5ce-35e5-b771-2df99c0dfb3b | -4.87348 | -50.54435 | 2024-10-10 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ee857540-cf97-3af4-b1c6-5f7cfb624abd | -4.87243 | -50.55018 | 2024-10-10 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1f1e63d-0659-3024-8a1d-63ed8670d7a2 | -4.83519 | -50.79459 | 2024-10-10 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2dfca0c-c2b3-3435-a1bd-a1cf78a6f8d9 | -4.82745 | -50.79926 | 2024-10-10 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 506a211c-ad52-339e-baf9-418aee28f14f | -3.95455 | -49.91739 | 2024-10-10 03:55:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3730a2f1-0aa4-395e-89a4-fd5a1c2d3de9 | -3.69167 | -50.1224 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README51.md)
