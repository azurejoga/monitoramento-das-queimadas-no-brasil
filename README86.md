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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8c52994-64fe-3971-b7c5-0c2768d517ce | -4.12563 | -46.6853 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b686dc2f-3d59-30db-9743-ed9bba6c14ed | -4.6583 | -46.44086 | 2024-10-10 04:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 798cb75b-d4c4-31d1-ab4f-d387ea66d26a | -4.55098 | -46.40777 | 2024-10-10 04:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43d2a18f-cbdc-34f2-a869-c0155c798cf0 | -4.55028 | -46.41247 | 2024-10-10 04:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 131bd34f-e9f6-367b-b3d2-f71eb198a52a | -4.48341 | -46.59941 | 2024-10-10 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67ab83d7-805f-3fde-9090-3517659ee422 | -4.47395 | -47.73283 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74551268-8fe6-3d11-bc20-e350b6d38559 | -4.47334 | -47.73677 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b44f86d-d944-3dc9-92ee-0d290180991a | -4.34992 | -47.29395 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce60fccb-170f-37f7-9bb3-2482f7648765 | -4.31869 | -47.70577 | 2024-10-10 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3ad66d56-6574-309f-a490-dfd92060b79e | -4.25955 | -47.19976 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43a94744-78af-3a23-9818-e7ef3d11641c | -4.25592 | -47.19922 | 2024-10-10 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e66e2ca-edc1-347f-bf66-05337a5c51a8 | -4.0411 | -46.32814 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72d07a9e-3598-3cc2-963a-0e1ef1858aa7 | -3.93677 | -46.45356 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66215c18-2222-3eda-95d5-31f42d9f9443 | -3.93231 | -46.45746 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bb2f136-858d-3d1d-9910-afe4e7193cae | -3.92922 | -46.45246 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f2466ba9-8fd2-31c9-bb6b-bb5d94e78736 | -3.92853 | -46.45696 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c0fe7e6-0047-3c92-adad-18ee71aa2fa6 | -3.92784 | -46.46143 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6951c2ab-c0fc-3593-8e66-18ee8ee8022d | -3.92614 | -46.4473 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04678893-1209-3fc8-a482-bd9fa81ec6c2 | -3.92544 | -46.45189 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72b1aa9f-4f48-3e94-a974-12a8f10c16e5 | -3.92282 | -46.41838 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be5e7cdc-1cb1-3259-8cf0-7ebdbee82e6a | -3.91482 | -46.44559 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fae8359d-09da-384c-95ee-5fe61cc23d70 | -3.91343 | -46.45474 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aea1d56e-5f99-3644-8b8a-b9ba8d6726b9 | -3.91174 | -46.44043 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c853933-3dbe-3759-9e58-0b040247eb26 | -3.90966 | -46.45414 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44fd87ec-16c7-33f5-a6f8-2fc120fbda96 | -3.90896 | -46.45874 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75b1a460-f8ac-3a2e-ac56-2797760c6071 | -3.90826 | -46.46333 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 076fa6ea-ae0f-3e1f-b8a6-6167b959dc34 | -3.90519 | -46.45814 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1185fbd-8124-319c-9400-05380e2d3bf8 | -3.90142 | -46.45758 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2971c17-a409-3fa5-a98d-b99cce2c1aad | -3.90072 | -46.4622 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3f8de661-4953-3c97-b390-532194935c72 | -3.89834 | -46.45242 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2cba13d-f645-3b0d-b1ab-ccaa6da0aae6 | -3.89764 | -46.45705 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 066b180b-0251-399b-9866-8b4c0411a649 | -3.89695 | -46.46164 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 084cccbf-0f8e-3cae-a0ef-23b354232f04 | -3.89078 | -46.45134 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aaad75b-35c2-31b4-9832-4623a5fd0dd5 | -3.89009 | -46.45596 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60811ba4-5e73-31fa-8c2c-ef1eff78df06 | -3.87363 | -46.46282 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf8ca906-8e55-34ea-adea-17ccf29ef129 | -3.85277 | -46.47105 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bd35fac-7e3d-3af8-b128-f776750210e5 | -3.84899 | -46.47057 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f421a51d-96d0-3b3b-88c5-02b87295539e | -3.8483 | -46.47501 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| debaba78-6fbd-3699-a8c0-e8fb1d807931 | -3.84522 | -46.47004 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a75d6b96-25b8-3059-acee-7423524a0bdd | -3.84215 | -46.46498 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6edf70f9-7f68-3cb6-ab9e-88cfcba8ac94 | -3.84146 | -46.46943 | 2024-10-10 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a1d4209-7310-309c-9fda-a90ae82826d7 | -3.8222 | -47.49987 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5f4047b-4428-3b57-9c8a-687d9b3675d7 | -3.81925 | -47.49525 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5ba4dce-ec2c-3216-af61-f89d7bb1c7b8 | -3.80973 | -47.49118 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 396b1641-3f74-37da-aa3e-7924b78ffa34 | -3.80856 | -47.49367 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c8cbe276-5550-3eda-9ac6-574ec964a96d | -3.80616 | -47.49065 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 714d7754-9551-3594-b28e-4674e3d59917 | -3.70115 | -47.60611 | 2024-10-10 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1e8a87b-8d4e-32bf-9f04-7895def0740a | -2.14086 | -47.98672 | 2024-10-10 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7360c3d-805a-3530-ba26-a54f5e7c657b | -2.12633 | -47.49527 | 2024-10-10 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21fbdfa0-420c-3340-b5c1-09c1a1d5ca9b | -1.78519 | -47.84224 | 2024-10-10 04:42:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65361cb8-bea8-3ae5-a0bc-f231dea581e5 | -1.7846 | -47.84599 | 2024-10-10 04:42:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cabe6651-5494-3e5f-ad15-ddbf399508e8 | -1.78116 | -47.84546 | 2024-10-10 04:42:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99397c52-6fb4-3f6c-86ba-5b3404e9a4b2 | -1.69832 | -48.15069 | 2024-10-10 04:42:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f39972e-08b5-38ba-a27f-c77bbecee702 | -1.58561 | -47.63939 | 2024-10-10 04:42:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41e67621-cc5d-3bdf-96e0-03093340ae7d | -1.46492 | -47.23465 | 2024-10-10 04:42:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 915aeb5c-91e2-3062-8954-775ed6dadbc0 | -1.46432 | -47.23856 | 2024-10-10 04:42:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bae99e25-d49f-3506-9959-aedc32b4cd8c | -1.46424 | -47.23506 | 2024-10-10 04:42:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01f390a6-0552-3ec2-b5ba-be053f1d14cb | -1.46362 | -47.23897 | 2024-10-10 04:42:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64c2dc11-2d6a-388b-99f1-ade077b12e47 | -1.28989 | -48.43622 | 2024-10-10 04:42:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 330ffddd-0b9c-3e85-86b9-c90048173e07 | -1.2501 | -47.83489 | 2024-10-10 04:42:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39d23edc-5fe4-38ab-b777-530a4b5d7a49 | -1.05582 | -48.00103 | 2024-10-10 04:42:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e9c537a-bcdf-34a1-bede-38a83ce63c73 | -0.7074 | -48.03419 | 2024-10-10 04:42:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e33662ef-a1ca-3b7f-8f25-33f1a552c97d | -0.70684 | -48.03782 | 2024-10-10 04:42:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2b7d23a-1046-352a-a6da-38eacbd2be11 | -1.83012 | -48.58813 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15b2f458-d773-34c0-80ca-4989c667115f | -3.46153 | -47.66022 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d02afaf-d7cd-312c-825c-293b1fe77517 | -3.46111 | -47.66109 | 2024-10-10 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e6a1fe2-ff05-38f2-848f-ff934a9e1700 | -2.76293 | -48.64608 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec0a5626-64c1-37aa-bbcc-e25878c0ec03 | -2.75956 | -48.64557 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3df35850-596a-33ea-a4b0-8a6b2320bde3 | -2.75899 | -48.64915 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1907920-d151-39c0-a31a-02a9a2ca66b6 | -2.75618 | -48.64505 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a84e51b-005d-3128-a239-21a69aef6aef | -2.75502 | -48.69633 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f7d73f4-372b-338a-98f0-ce987c176940 | -2.75446 | -48.6999 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 149d920c-7ada-3aa9-8584-874179487d15 | -2.75165 | -48.6958 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2aac5b6a-bd05-30c8-b68c-65495c4e1e80 | -2.75109 | -48.69938 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ef6ebe3-daef-30ab-ac30-0e242d4b8936 | -2.75054 | -48.68095 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb529ea4-9752-363d-9ee4-758b84cd5e80 | -2.74997 | -48.68454 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff985585-a617-33b1-bab6-9b9f782ab5b5 | -2.74828 | -48.69528 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffbdeeef-eeef-37eb-9616-d5bbdf026361 | -2.74716 | -48.68044 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74cc0956-a0f2-330c-8605-7fafc52fb66f | -2.7466 | -48.68402 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc259080-d593-33c0-9f5d-50ed9758fa8f | -2.74548 | -48.69119 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11dca403-eb11-3a6b-986b-468f541f8096 | -2.74436 | -48.67633 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 503b90f6-7cb0-396e-ac2c-9e99195881cb | -2.74211 | -48.69067 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97cc3b5a-4016-3fb3-8eaa-4b7c0e707b00 | -2.74155 | -48.67223 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b9267aa-4eeb-3741-9441-54b8bf5b2972 | -2.74098 | -48.67582 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0278584-23a8-3e57-88e5-2d37aac5df04 | -2.73929 | -48.73058 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b47a2dff-44dc-35cd-bb4f-1da192a99a69 | -2.73536 | -48.73363 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59da362c-a1dc-38a0-950d-67cff7884a8d | -2.72414 | -48.73922 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05027bc5-152f-3b93-818f-1a7e2d306f02 | -2.72078 | -48.7387 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38d79001-2ecb-373b-8ef9-668b2227a96b | -2.69438 | -48.70898 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 102eff9e-8f5f-3236-aa33-92072de856be | -2.69261 | -48.63158 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| de66c8c2-6544-392d-b610-6a16d795368e | -2.41021 | -48.59637 | 2024-10-10 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a31d1c58-2d72-309b-8d04-2e08b2f0b330 | -2.40684 | -48.59585 | 2024-10-10 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 936c4471-7477-3976-8af0-79e1cbf66f1c | -2.33275 | -48.48486 | 2024-10-10 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56530d9a-ee22-3901-86c7-57ec2330979e | -2.33219 | -48.48846 | 2024-10-10 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3abcf0d-90c8-317f-81f8-5ecc3e6e85b7 | -2.20523 | -48.81631 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2d3f2bc-04fa-3f84-9cf3-a6c4ff36840a | -2.20298 | -48.80872 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f7c0ca4-5fe0-368b-97fd-10cd29111fc5 | -2.19185 | -48.79987 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5b004f2-99ca-33be-8263-ad2ef5696dd8 | -2.18291 | -48.79124 | 2024-10-10 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b92c795-e547-392c-9aa6-3b5804b03fd5 | -2.94762 | -48.61162 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8707781f-e5c1-3809-9c10-314c85a9eda7 | -2.94424 | -48.6111 | 2024-10-10 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README87.md)
