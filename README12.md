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
| f9fc27be-0668-3754-8238-865d8bfef964 | -3.24268 | -46.80563 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80d66562-a4b0-33f9-a17a-fb8c733c7f76 | -4.02011 | -46.81905 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6af976e5-44c6-342d-8f85-ba13763e2ee4 | -2.51315 | -49.05877 | 2024-12-17 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6721c5e1-fbdd-3c9a-8284-58329d894a4a | -4.0596 | -46.91679 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8994aa9f-a46b-3cc0-b10e-219078cb530c | -1.28342 | -53.18984 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c56c561e-7867-3896-a498-3041652438c1 | -3.47227 | -42.9273 | 2024-12-17 04:21:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 387a5527-8d76-3b2b-9a7e-b5ca92a33040 | -5.10299 | -43.90526 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6612fa03-b876-358b-bc9b-934e414747a8 | -3.05282 | -47.08717 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ef1f4e6-782e-3dbc-a21c-e976aebf7d26 | -4.02598 | -47.03616 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84948611-b07f-3ee1-b9bd-9405e9e6c70c | -4.07578 | -47.10902 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1f9db8c-5ae5-3797-89d2-e2597a1db4eb | -4.07816 | -46.6085 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad73d8c8-f56b-3b68-89e0-a9838eefd5a8 | -4.08871 | -46.7353 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b30eaeb-4ef1-3741-8950-b193cb4e4a47 | -4.04846 | -46.91906 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1dc505bf-0d13-3d28-b850-e136569fef76 | -5.24918 | -46.35224 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bc7b27c-67f3-3843-88e8-d0145a2acaa7 | -5.10245 | -43.90874 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| bb35043b-d5e8-33a7-97a0-8c30875390a5 | -4.96847 | -43.7205 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c50de1c6-61fb-34c1-a93d-6ab738b2517c | -5.80343 | -43.04542 | 2024-12-17 04:21:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17d0f7eb-3227-314a-8d89-f5d0fb5cd836 | -3.01373 | -48.02956 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15ea42d9-7d7b-3301-b039-6900c4537b44 | -4.39668 | -44.87957 | 2024-12-17 04:21:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac807a54-c2fc-30c0-aad4-ee5a9f73f331 | -4.05671 | -46.91241 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23edc896-8cbf-3c06-8e3c-2edabe70c07c | -5.73108 | -43.75582 | 2024-12-17 04:21:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd53407d-a282-37b6-8ed1-e1f82d2ad5cd | -4.79992 | -46.39505 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 68ec3d3a-7688-3bcc-af20-f48d72a71aa6 | -2.47103 | -49.03044 | 2024-12-17 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fbfe76e-c942-3404-b71c-625cd5400708 | -4.01722 | -46.8147 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 964cd6ca-2455-3e96-8aba-c8e601998bd6 | -2.05122 | -46.65916 | 2024-12-17 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14d41ca6-3ace-35b7-894d-ac9768fd7583 | -1.46277 | -53.48328 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ee2bb94-2f9a-33aa-a8ac-ea1a4d14752c | -3.95603 | -46.92887 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1cc4395-7812-37bb-96ac-5ef8ec9749ea | -4.79651 | -46.3945 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e9580f04-45ec-3e08-be63-c47be63f6463 | -3.60608 | -44.91051 | 2024-12-17 04:21:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efd698a1-8c67-3227-9778-32ce60408149 | -4.09667 | -46.81937 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c1780d-b16b-33df-a8d6-04bb1ea45e00 | -4.02247 | -46.89492 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99048704-7ad9-3ac1-8005-464f424f2358 | -2.57263 | -49.41203 | 2024-12-17 04:21:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b605b12-5f1e-367a-ae26-bfee294a4ad4 | -3.0879 | -47.78104 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ace8466-2ab9-32c0-853e-bd6458d82b96 | -5.08864 | -43.9102 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| de73e0ce-a9ee-33a8-8747-ccdbc21c751e | -3.79484 | -46.84497 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 128e1008-c22c-3e9b-bf10-de4168908ccc | -5.14646 | -46.1836 | 2024-12-17 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 521ae981-f6e0-3f0c-9434-920fbccf37b3 | -3.76964 | -47.1655 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17522af5-a7aa-3229-9600-6d091961a9ad | -3.84784 | -45.86211 | 2024-12-17 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b54689b-ee11-3ba2-b7a8-2835c3356448 | -4.05532 | -46.2414 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 808b960e-fed5-3616-8b4f-44d19e0b659b | -4.05321 | -46.91188 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7de31395-80a6-31a6-a32b-f1fc155fffc0 | -4.27305 | -43.42302 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c61363a-0705-3eaf-9d9a-01a512643775 | -1.69603 | -45.77288 | 2024-12-17 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7043365f-da9f-3a24-a1b8-6b93a08f9c70 | -5.0986 | -43.91171 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f6f97c3-2a9a-3bcc-b5ba-65fa0148c1c4 | -4.36966 | -44.87891 | 2024-12-17 04:21:00 | NOAA-21 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83a17e5c-b683-3902-9b49-1b080f6e7b44 | -3.23018 | -45.37448 | 2024-12-17 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9c74e09-f958-3a8c-b33d-20e872e2441f | -3.30387 | -53.37135 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 7a7cf521-8db9-3bd0-911a-d172b1c81bbc | -1.89554 | -46.81643 | 2024-12-17 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5fd4ef17-5761-3108-9e33-ffc5103c03c9 | -4.71298 | -38.45124 | 2024-12-17 04:21:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5d8ee94-7949-326e-8f91-a46faa5428a9 | -3.44042 | -45.59666 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7325f7b0-a8fd-3279-87e4-db732bfc9c46 | -2.74174 | -47.83558 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13e1d8ea-366a-3ae7-b25d-73094ccf6766 | -4.37897 | -46.5467 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56549838-289d-3fa9-93b6-ff2f9c185b87 | -2.93193 | -52.71355 | 2024-12-17 04:21:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d372edb4-8ae2-3307-8d90-2ec12c02d665 | -4.05355 | -46.67477 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62b5af8b-22e7-32d6-9f20-4e2e4db64ac8 | -4.67818 | -44.03434 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 002a6ff0-d753-3a80-b488-2a8a04a355cf | -4.25246 | -47.57574 | 2024-12-17 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ebbf6e6-1016-3f98-b9ca-274369002285 | -2.17967 | -53.743 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 799b1c7e-d96d-3f78-a152-c9a4a52b9048 | -4.517 | -47.94308 | 2024-12-17 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20158c4d-ddf3-3fb7-af5e-00f9e76db5ae | -4.25186 | -45.99546 | 2024-12-17 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf22185a-4066-321f-8f0a-88807cdab179 | -4.02951 | -46.8048 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1ad75f6-3603-3ed6-8819-fc66f7df56ff | -4.04496 | -46.91853 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99f30564-98c6-35bf-a98b-3170d5104f2b | -4.01478 | -47.0384 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f5aa95e-15d9-3167-b415-a4c1a5f6dbb3 | -5.30322 | -46.49936 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df82df0f-67ef-3484-a9c8-75cfbe363de2 | -4.00989 | -46.92919 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa05d970-f7df-3f5e-a5b1-fd02567d87f4 | -2.05981 | -45.33439 | 2024-12-17 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d6be987-3a12-38d9-9ff9-4522bce9fe00 | -4.06373 | -46.91343 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9bb6c2e-0e7a-37e1-a3dd-74f58ae3318c | -3.2978 | -43.11385 | 2024-12-17 04:21:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8f8fb69-df02-318c-a5fb-87f38bcf51a3 | -5.20883 | -44.5591 | 2024-12-17 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7b2d541-6880-3bcc-9f61-86746ea89eeb | -3.44077 | -54.05424 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a89b0d-b09c-3ca1-a6da-fcf7b7ca5f30 | -4.02466 | -46.83554 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15e1c591-9e4f-392e-b0cf-9e6c8f0ab31f | -3.11864 | -52.69922 | 2024-12-17 04:21:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d419e3f5-3d8d-34a0-8a70-910981a33296 | -5.14199 | -43.23732 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c3a4255-ca82-31a6-bc5b-0d650506cbfd | -3.6094 | -44.91102 | 2024-12-17 04:21:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 442bff7e-1b69-389f-9fc3-e439f353fce2 | -4.033 | -46.80531 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74b0e664-ef3d-3cd0-85de-c9f8a7997470 | -3.47172 | -42.93086 | 2024-12-17 04:21:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ba033a3-66ae-33db-8c44-4ca4af1b4baa | -3.5038 | -53.9505 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07d27c82-39a6-3575-be20-d6572dc93ea1 | -4.89437 | -44.1744 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2984a8b4-83b4-31d4-bafc-2e422ab2e296 | -3.7619 | -47.16837 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dd33fe7-f9fd-3973-9658-bee669631f2b | -2.5697 | -45.95583 | 2024-12-17 04:21:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4396299e-e137-3fc0-a8ec-021832063e0b | -5.21213 | -44.55961 | 2024-12-17 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa97d96a-1c25-32c6-bfec-100a68301404 | -2.77969 | -48.5835 | 2024-12-17 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 061b209f-2e58-3d5d-8d6f-95bd2666a289 | -1.40848 | -47.47645 | 2024-12-17 04:21:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a83b28a5-9c6c-39f4-9841-0402dae0bff7 | -4.10361 | -46.68665 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5404377d-41a2-3a40-859b-c023a9c25432 | -2.62453 | -48.64488 | 2024-12-17 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d6f8bf0-b2c5-3df5-8919-67fb7126528c | -2.58788 | -47.48316 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b38ac80-d118-3be8-8558-7f0023342321 | -5.26111 | -43.76242 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed538858-d2f5-3f00-86d4-be4110945761 | -2.58413 | -51.92451 | 2024-12-17 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 552dc054-24d8-395d-8f98-c93a3d20e59f | -3.15693 | -45.97069 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14f027dc-735a-3613-b5bb-3e4696003ee8 | -4.03147 | -46.86045 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 295e945f-9466-34fa-9aa7-298b829d4ba6 | -1.63414 | -45.85456 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 344c36d6-d918-309f-acaa-7968dca086c2 | -2.17813 | -53.74615 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f62e872-ce39-3871-8b29-27c2f4979a27 | -4.10301 | -46.69043 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36bfde8a-5a41-3cfe-8b2e-79d76e6090ac | -4.04434 | -46.92238 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03256a13-c5ed-35e7-a6d0-c8efb4728753 | -3.79256 | -46.83669 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4da1cdf1-2f04-323b-8ffa-13b1c1eb29a8 | -3.44138 | -54.05062 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47fd81df-7b11-3bbd-8165-b73e32c16072 | -5.3078 | -46.49256 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5398e5d-070a-3e89-9713-5827ba0c665a | -3.7182 | -50.16131 | 2024-12-17 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d01ad48a-bd8e-3d68-bbbd-70edc8f1bbe9 | -4.07994 | -47.10558 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f9b8f9f-92b1-3078-96b7-e242de33d8f3 | -3.84446 | -45.86158 | 2024-12-17 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9ff30f0-c44a-300a-989f-2a623c1fe6de | -3.04935 | -47.97515 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2d012da-ea26-33b9-b58b-3a3df8a233e1 | -4.57362 | -46.58071 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README13.md)
