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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9381b41-2282-356a-8dd3-2c762ba9c102 | -3.25858 | -50.09571 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a49f9286-1e56-3498-bece-6200ff913010 | -4.39979 | -43.08793 | 2025-11-15 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee95550e-667e-3a42-b749-124b8c67cf07 | -6.41356 | -41.46547 | 2025-11-15 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fe9a6712-bc41-3d3c-b27b-3dd30a2cd48f | -9.85662 | -44.17368 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f425e752-9c52-38c7-b880-971ca20d6a9a | -4.68574 | -45.85402 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a05e26f6-e699-3df9-b9db-4bc51cd9b0a6 | -4.0514 | -49.07858 | 2025-11-15 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3199d47c-5896-3e81-a937-20b642b9b0d6 | -4.49229 | -45.91844 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e69fc1e-5b03-3fd5-9960-052d3deae310 | -4.90823 | -49.99755 | 2025-11-15 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc8cd05f-5f1c-33ad-a0e8-0255567ef034 | -6.81468 | -48.78824 | 2025-11-15 04:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bd53c1e-f931-3bbf-92e8-cc2afc49b015 | -3.99821 | -44.17045 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cee89e05-e168-3d7c-b9d0-0f11809ccf6c | -3.86232 | -49.13697 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fd0cc45-1544-3529-8aff-18f13ed6fb22 | -6.16323 | -48.03951 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33edc0d6-1a3f-366f-b450-ae82b4ffae2d | -8.56577 | -46.04654 | 2025-11-15 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e5234d5-fd0a-3945-bb0c-94e702d004db | -6.28623 | -41.75177 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 925b1b32-d968-3871-9ff4-0011277cc622 | -3.39318 | -52.44927 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8af25664-9cc2-362d-851f-06c7842ea3c8 | -5.91567 | -45.53042 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c858e911-0471-32c1-b8ed-ec51cc2e62b5 | -8.73135 | -45.6598 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bcdfea4-af0c-3cb5-bd5f-dff4e8ca8438 | -5.09889 | -37.78695 | 2025-11-15 04:25:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 436aeac4-75e6-3730-b2c7-fa32eaed6df1 | -4.17769 | -50.42487 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba919f30-1501-3c8d-8fc4-916c789cc7e1 | -4.71762 | -45.11208 | 2025-11-15 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db684ee4-6a7b-3446-99b9-560bbf8858b2 | -9.51815 | -47.26912 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a92c1474-b0e8-3b15-879c-7968ca7dd942 | -3.66397 | -44.81218 | 2025-11-15 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa62cb26-015f-362a-b646-fa05cd44b5b5 | -4.70366 | -40.12257 | 2025-11-15 04:25:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fa2afa0f-32e7-308c-8c56-2396af8e1daa | -9.15841 | -45.16913 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b32b43af-78e3-3bda-bfa0-6613710aa736 | -8.94952 | -44.5139 | 2025-11-15 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 111434c7-ff20-3c4a-9ddc-d2536c991678 | -3.94878 | -44.79527 | 2025-11-15 04:25:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd7d2059-c962-317b-95ae-e7d09ece8471 | -4.3024 | -46.00093 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ea072e6-d2c3-3eb5-841b-fb1ea993751f | -2.51469 | -47.80944 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| b6c4dae2-9289-34fd-a5bc-006da6ffa51f | -7.88825 | -48.39693 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 592b0877-8989-324e-a92b-438431bdde97 | -7.29322 | -45.10503 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59a4eaee-2ffc-3b0f-ab8f-050cc9d08c5e | -9.15163 | -45.16796 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c602126-f0e4-31d7-9e3b-1e0dc76e267b | -4.41037 | -50.82278 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c24d896-3173-3c70-925c-47895cb0ab8d | -4.309 | -46.00197 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9964ee0-87d7-3dde-b1db-e60835cbe055 | -4.88186 | -49.38898 | 2025-11-15 04:25:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23145cfc-2672-3e94-a284-3a09417ca1f5 | -4.06237 | -46.4229 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e94c47ba-4ee5-3fbd-a7c2-2cd97cff7c66 | -2.73905 | -45.2935 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e4a2d75-c3e1-3212-ad34-16539eafffe4 | -3.66342 | -44.81567 | 2025-11-15 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6403a520-60ab-3214-9773-2c469aa29a23 | -8.32294 | -45.40313 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01da8efb-17be-35fc-a04a-164f2460e368 | -3.01364 | -49.43615 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b31ecc9-acc7-3198-82d2-73c601049993 | -4.43055 | -43.66207 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82c6f5e2-e662-30b0-aea1-33a56ef43a22 | -4.59414 | -44.32038 | 2025-11-15 04:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| db587edc-38c3-3bb3-a988-3f8ce7bafb39 | -4.94414 | -44.75093 | 2025-11-15 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d7c352e-92f6-3d30-aec5-b842264e64a1 | -7.42891 | -45.23177 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ff203a9-511e-3850-a741-c67250d3e7dc | -2.8556 | -53.01121 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d5f4514-27e9-39c4-b79b-a8354c3d686b | -2.69418 | -49.85622 | 2025-11-15 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e11ce29-6687-3059-8236-b1f419e04879 | -6.15866 | -48.04625 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1e8afbf-b424-33dc-86e6-1215126d7aa9 | -9.12325 | -47.12355 | 2025-11-15 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c511c79d-0aac-3660-be20-08a7674ac738 | -8.85212 | -47.33319 | 2025-11-15 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 761ab061-ebab-31fa-93b3-2c7483ef99d8 | -9.09573 | -47.78681 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f99acf05-7119-33a8-878c-0a79b6dc0197 | -5.09274 | -41.47989 | 2025-11-15 04:25:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5816beb3-ff91-3dbb-acb1-4f2b6c14991a | -1.10768 | -52.59419 | 2025-11-15 04:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f17a8db1-f4ff-31c5-ab0f-c548d6ec9195 | -4.57932 | -43.40229 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b128d51e-a41e-3785-9671-10d48c57e85a | -5.28452 | -45.54885 | 2025-11-15 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df21e093-b430-3378-9209-a07d3127fa68 | -4.18564 | -50.42287 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c6852b8-badd-39af-8efe-5d85a8b00714 | -4.65967 | -50.91018 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94e19c6a-e51e-3ed6-81ce-644a20c36843 | -3.27876 | -51.54512 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db4f71d-c802-3105-babc-56c2d4a87bb4 | -3.4637 | -50.11582 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88f42224-0ae2-3087-a3e9-e607d020da76 | -6.03564 | -45.80531 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00074a3c-766f-3be4-b706-3dc09a521665 | -4.2677 | -46.84191 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 140d5460-460a-37df-9985-91613989ca10 | -2.68566 | -49.8598 | 2025-11-15 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d388c13b-19a3-3a65-aeeb-f2b04c62ba48 | -3.45981 | -50.11518 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f446429-88cf-3556-8de3-c2e317c9d0a2 | -4.37444 | -47.25541 | 2025-11-15 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7eda6e6-71b7-3570-87e6-2a0e05ab1827 | -3.67948 | -45.83544 | 2025-11-15 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03516168-b750-38e2-b936-1329a496a88e | -4.57026 | -46.94715 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6738ac24-8d8c-3aa9-82db-389843635340 | -3.87583 | -45.1082 | 2025-11-15 04:25:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e896bead-a56f-3847-9634-83bb29631138 | -4.72106 | -50.83784 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c328b9ef-07d1-3ed4-94ac-6edad7b7eee8 | -6.73439 | -42.95517 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f111356b-c4d8-3e8c-b195-b87a6594fb67 | -7.53476 | -47.19691 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10ef1efd-1a40-3191-b204-efc9c83bf5ab | -4.04419 | -46.1298 | 2025-11-15 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df64d742-5109-3364-b121-a66b66f70a86 | -8.74264 | -48.31635 | 2025-11-15 04:25:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 975c80e3-dbae-30a5-a130-f0e1a58b49cd | -7.21128 | -35.03376 | 2025-11-15 04:25:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f77dc564-767c-3632-8ed0-07379172a239 | -9.85722 | -44.16958 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 110e1016-155d-387f-aaf0-133782c3a05b | -4.40007 | -44.08326 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de1a85e2-4c82-3247-aa71-048d9c7979e2 | -9.05947 | -48.83187 | 2025-11-15 04:25:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c98ccc67-ba1a-30ea-952a-4e7e3cede6d1 | -5.3586 | -44.9023 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20f1fcef-1905-36a0-aa02-a92cad3e5066 | -9.86107 | -44.71822 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7926f1-c128-31fc-a1b3-f856518f33f0 | -7.31305 | -43.83368 | 2025-11-15 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0aaa3175-230d-3623-ba91-2294fb36f8d3 | -7.4424 | -42.77433 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 210b10ae-e24b-3811-a52c-173741392148 | -8.38265 | -43.83352 | 2025-11-15 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32033015-7c14-337c-b508-77c9ebeb48f7 | -3.06723 | -44.74055 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41cc5e2d-cac3-3001-bde9-4ede80e5f74a | -3.53069 | -50.87331 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a88fafe7-e100-30d1-9ab1-d06b86f2302f | -4.17695 | -50.42659 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ceeb92b-72eb-34be-ba80-974cf82136e0 | -7.53807 | -41.17139 | 2025-11-15 04:25:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2c68a7be-0cf6-3106-bef3-bf0337835aea | -6.25972 | -41.41652 | 2025-11-15 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4aec1a97-33e0-35e9-9569-e3e002482e50 | -5.71929 | -46.75302 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43b107b5-9944-389a-9c7c-5202083187e6 | -7.87565 | -48.40994 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f8b3b047-1a79-31d9-8120-da63d12d0d2f | -6.28159 | -41.75608 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c7c8d3f7-46b6-3738-84b8-fb4022c7030f | -3.37954 | -46.03532 | 2025-11-15 04:25:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3afee97-ca2f-337c-acfc-6d03534d317b | -5.53939 | -42.70165 | 2025-11-15 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4cdd18fd-2a40-3748-9261-841123985c55 | -5.38066 | -45.36848 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8969504-e921-3f1b-9750-66ca43be9d06 | -4.31155 | -45.90017 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e54e10cb-491e-3fb0-8da8-884efb31dc7c | -7.53852 | -45.85992 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d838ec1-505d-38b4-8e95-1135d36e778f | -8.30907 | -43.64751 | 2025-11-15 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6fe1b04-33da-3c72-bd23-b9d72bf405f7 | -6.07773 | -41.64621 | 2025-11-15 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9930c4bb-b362-3587-8fb8-536834a778e7 | -9.80804 | -42.21172 | 2025-11-15 04:25:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3e0ff7a9-76d9-38a3-b48f-904126c6a0e1 | -4.90542 | -44.05787 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 301be2be-6852-30db-9579-8a2e9e722ea7 | -4.7143 | -45.11156 | 2025-11-15 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84c19999-948b-36b7-80d0-8cc8ae623457 | -9.20368 | -44.16812 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 134b7366-bf11-37e2-a571-22e2722eab76 | -2.85355 | -51.2827 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0779674f-cb49-3550-8b3e-8ba5f0cccbea | -2.63741 | -47.30052 | 2025-11-15 04:25:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README33.md)
