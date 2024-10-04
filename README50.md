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
| 0e9e7407-a840-39c3-9a92-79254ea34b4c | -18.07338 | -42.60001 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5d50f418-d772-3245-b613-1bd1a76bbfbc | -18.07252 | -42.60397 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| faac3ffd-1019-3bf4-b99d-fb693acc76a5 | -18.06806 | -42.62455 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a272ab5-809b-3d07-b7fd-f60e6f46d4ed | -18.06764 | -42.59842 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 65bb5615-8184-369d-87bc-4f7c05890de4 | -18.06238 | -42.62259 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 58a7ef89-d330-3e42-ba26-c6830c697c5b | -18.0615 | -42.62666 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 947f1848-4a94-3bd0-9389-a86262d85f73 | -18.92341 | -42.02579 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b98f6d2d-9e7b-3a5b-a9e1-70ee1deca4bf | -18.91885 | -42.02014 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d59b5278-ee75-3036-8dc9-a82bae9858f7 | -18.91799 | -42.02408 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 6dcac1c8-8861-3faf-b404-18a9655617c6 | -18.91709 | -42.02823 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 6c941c73-6a2f-3a79-894b-a77b0afd4a9d | -18.91629 | -42.03194 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 27b7acc6-3019-37c3-94f0-f2e0b4f50cf4 | -18.91413 | -42.01523 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2319a974-e569-3460-870f-9f1d57e10eff | -18.91337 | -42.01872 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a08b57e5-5282-3386-841e-62de6a312d85 | -18.91254 | -42.02253 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| cfdcdaa5-5b29-3098-bba7-be69fcf720ba | -18.91163 | -42.0267 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 7c3afb79-1177-33a2-b222-668bda4a7f92 | -18.91078 | -42.03064 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4be1d413-eb7a-38ed-bee9-97cf48827584 | -18.90789 | -42.0173 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7f209646-f8c2-3095-b8ec-63f59ca51d25 | -18.90705 | -42.02115 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6b1a757a-ec40-355f-ae35-2b819dc9c6bb | -18.90616 | -42.02525 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6a9a4886-7373-3a2b-82f5-ac2fe0809da6 | -18.90528 | -42.02929 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fe5e43cb-db46-3df8-b5d9-37ffbc322956 | -18.90409 | -42.01339 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7c1c2fe-a78e-3600-8443-1f3cd9c898aa | -18.90404 | -42.00845 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 982a4aa9-1de9-3c1c-a4e8-7e62c50cb120 | -18.90327 | -42.01731 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 641e4f98-26ed-3637-90d0-05af9d62cc9e | -18.90327 | -42.01197 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7652b686-3915-3caa-98a4-8ee3223d52c1 | -18.90243 | -42.01583 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5dac9047-f29e-31d0-8a90-c7e73e51c775 | -18.89933 | -42.00859 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d3051c0e-7bfe-39ea-ba45-b9fde2dabf95 | -18.89857 | -42.0122 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e504a390-55cc-3e42-b048-2313dcce7fad | -18.89851 | -42.0073 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ed3bf75c-b5dd-39d3-a55b-94e2d48b7246 | -18.89772 | -42.01089 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 45ceae73-4adc-32f7-8828-1f7108fbf2b1 | -18.89692 | -42.02 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b37bd167-2723-3187-88be-9fafa4bb3649 | -18.89604 | -42.01857 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2cbb9e23-e20d-38a2-93bd-c4ca9ea80ee6 | -18.89522 | -42.02233 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d179ca11-fc1a-3803-b7a3-e3f2ef8b61fc | -18.89063 | -42.02242 | 2024-10-04 03:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 42eeb8fb-1612-31ea-88a9-036c2c842be5 | -18.61826 | -41.84705 | 2024-10-04 03:17:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18243341-7553-3394-a5ef-ccc2e090300d | -18.61744 | -41.85081 | 2024-10-04 03:17:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 45723c47-7914-3167-9d4b-a10f29cd1a43 | -18.61662 | -41.85458 | 2024-10-04 03:17:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d292a5e3-a89f-3802-83ea-bc80c5c0bafc | -18.54377 | -42.24346 | 2024-10-04 03:17:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0b660c1a-291e-31ee-91d1-91809615bab3 | -18.54016 | -42.26006 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 801ced32-4e3f-3247-9b65-fbd1936d7d95 | -18.5392 | -42.26443 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 0b29c84b-d091-3e70-9c5a-fcf699fedbd7 | -18.53907 | -42.23798 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 31e981ea-3cf9-3318-9de6-4bb735e2dfff | -18.53819 | -42.24201 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 974870c4-1026-3ee9-a1a4-23f748bf8e06 | -18.53522 | -42.25562 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6b96273a-856d-3c60-875a-932fe7fc403b | -18.53433 | -42.25965 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| cc89f6c4-1d47-3264-b9d1-2d027e75834c | -18.5334 | -42.26391 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| b205996d-4b1b-33bf-8c4b-51c851ccee8d | -18.5324 | -42.26851 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 8ab1954b-07df-3bb8-aa0f-81b939fabb04 | -18.53025 | -42.25131 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 92e2d12b-3634-3d1b-88db-bad6ca344b94 | -18.52936 | -42.25539 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 554aba8e-c63d-33c8-9084-dce621f42eac | -18.52773 | -42.25141 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d48bb9cc-4a3c-3f9b-8f8b-d85bd65bb006 | -18.52687 | -42.25546 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3a6d12c0-acaa-3876-8868-bb4e6150be18 | -18.526 | -42.25959 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7832ca8e-d2ea-3173-b9ea-f8ec838d638f | -18.52264 | -42.25906 | 2024-10-04 03:17:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6d2fb54c-7dcc-3d08-843b-e11024367772 | -18.43026 | -42.2104 | 2024-10-04 03:17:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4cd64b87-2934-3b8f-afaa-d76351153d98 | -18.42871 | -42.20667 | 2024-10-04 03:17:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5c1b1e05-b173-3042-9d95-cc7b579d51df | -18.4277 | -42.21148 | 2024-10-04 03:17:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2163fc12-1170-335f-adc2-3d59392a179f | -19.51081 | -42.32845 | 2024-10-04 03:17:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99921f23-9784-30ff-a516-1c253f981f51 | -19.50967 | -42.33366 | 2024-10-04 03:17:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b91e202b-a400-371e-a1bf-110e8ecc6f88 | -19.57203 | -42.73486 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bd8e51c3-aa21-305e-9ac6-72400351cd5d | -19.57017 | -42.74332 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ba5dcdd1-81f2-34f8-b8c3-0578d5a2ecb9 | -19.56862 | -42.7232 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2b8b9cf9-7c6c-398a-8d3e-983019a8cea0 | -19.56783 | -42.7268 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 310cdb9a-b0a5-390c-9032-8e17c16317ea | -19.56704 | -42.73037 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5e996080-6f40-3bab-bc94-c18dfdd50d2c | -19.56627 | -42.73388 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| edd366db-1678-35f3-a4ef-d434d9b8f38d | -19.56549 | -42.73743 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b4053fa5-452e-3c06-b84c-0dc7b3a26017 | -19.56463 | -42.74134 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bdf40a5f-b416-35ed-b650-8e0383eb0a6c | -19.5638 | -42.74513 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 598f00ad-62c1-3c00-8af4-16a1313cdef7 | -19.56296 | -42.72179 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a16a47b0-5ac0-3149-a509-76d120ca18c6 | -19.56209 | -42.72574 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f8f5f4f9-5c7d-37b4-ad31-977047629623 | -19.50028 | -42.89652 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3986b2d4-a8bf-3d74-9554-909f2053993c | -19.49605 | -42.88839 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6eb8222e-0199-3d33-997f-9bf9e103ac02 | -19.49058 | -42.88583 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e8a82b50-0f37-3926-9fc4-d6978999e4b7 | -19.48928 | -42.89165 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e8cc5c6f-db89-3a95-982a-b562077cfb9a | -19.48496 | -42.88391 | 2024-10-04 03:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 759ff143-c3f0-38fa-9949-f7b8cee1dba4 | -19.44887 | -43.07227 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3a681516-a7d0-3641-a2f7-1910bd00dc11 | -19.44557 | -43.08699 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| afa65e2f-fe72-34dd-b1d8-3eab9d2233bb | -19.44202 | -43.07557 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 007bf669-bfd2-3c85-afc2-8cc670653811 | -19.44088 | -43.08065 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cd4718b7-f13f-3af6-ba25-cc2e6c20cfc1 | -19.43965 | -43.08609 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e60e99bd-88ef-3a31-bee7-5b16adc7fa91 | -19.43695 | -43.07597 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1abb560b-f1ac-3ad6-9d77-506b9219e83c | -19.43585 | -43.08106 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ecdf8c6-85ab-3b51-8f7b-fd7a2aa06d40 | -19.43328 | -43.06479 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 580531e0-9dc0-3b76-af29-92684b9c5425 | -19.65359 | -42.38766 | 2024-10-04 03:17:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 21923862-48b5-3c53-bce6-dd2c786184d5 | -19.65271 | -42.3917 | 2024-10-04 03:17:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 3b2ad477-b0b6-3d07-a3ba-93620fb28234 | -19.64807 | -42.3862 | 2024-10-04 03:17:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d18a7a24-11cc-3020-8b2a-a51a9b5eb88b | -19.64716 | -42.39038 | 2024-10-04 03:17:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 05541033-469f-3b26-920b-5e4cb5cc3b2e | -19.61891 | -42.25351 | 2024-10-04 03:17:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ab9c34d6-2aad-3e34-b959-38c4620fd797 | -19.61802 | -42.25757 | 2024-10-04 03:17:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 53916860-3d68-3d79-9353-7086aebc2610 | -19.61437 | -42.25252 | 2024-10-04 03:17:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c3debb85-3873-3675-84e8-5c6019254d83 | -19.61349 | -42.25664 | 2024-10-04 03:17:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 08504b11-77ee-3651-a83e-b37d5fe08d04 | -19.61263 | -42.2607 | 2024-10-04 03:17:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 61a3331d-3c34-33e9-a6a4-d8ac0501ec82 | -19.61247 | -42.25644 | 2024-10-04 03:17:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b5bdb5a-6aae-3738-b48c-84477f7ef51a | -19.61159 | -42.26046 | 2024-10-04 03:17:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8734648e-0b45-36dc-a1ae-5e75d293a503 | -14.33009 | -42.34336 | 2024-10-04 03:17:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df687bfe-309a-38a7-8c30-cc94d3ec375e | -16.47263 | -43.81718 | 2024-10-04 03:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c84190b-8a77-39aa-bb33-4641e9682c10 | -16.47152 | -43.82214 | 2024-10-04 03:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 093d63ac-88a0-39ee-a097-7571c8ad5bbc | -15.59081 | -43.64862 | 2024-10-04 03:17:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 448bc5d8-bc41-3086-ae29-b047217fc9d1 | -15.59013 | -43.65102 | 2024-10-04 03:17:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3685a9a4-3bdd-3d5c-959a-fe23e4fcaea8 | -15.58964 | -43.65403 | 2024-10-04 03:17:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1b00f3db-3151-349e-8fb8-7638198c0b97 | -18.04832 | -43.32861 | 2024-10-04 03:17:00 | NOAA-20 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ada963c-86ff-32e7-b13d-481b4284812d | -18.04725 | -43.33334 | 2024-10-04 03:17:00 | NOAA-20 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8d1f0a4-222e-32e2-a205-b22b85b3b215 | -18.04131 | -43.33146 | 2024-10-04 03:17:00 | NOAA-20 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
