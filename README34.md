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
| 49d88f31-4bc5-3071-b92a-30f83d15602f | -2.42089 | -48.49237 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef755e2d-c65c-3db4-8f4b-583483077da8 | -2.40318 | -48.22299 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38177306-8505-3b91-9566-2990c08de750 | -2.40032 | -48.43788 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 805b1337-00a5-3c09-9514-b20d1e891228 | -2.39983 | -48.22247 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8317bedf-905a-31a9-beb6-bb3ac78b11dc | -2.39927 | -48.22601 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a39bf966-8fc9-3ebb-8d37-157f23a32fab | -2.39861 | -48.58861 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2fdc710-a280-3e48-b780-bb9d344b0724 | -2.39696 | -48.57724 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7152d7e-5bae-3c18-9cae-10ef5cdc218a | -2.39638 | -48.58085 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 432ee709-b745-3d79-b0f0-60d284ae38f3 | -2.3958 | -48.58447 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b7d47b8-1536-3e04-910f-95f26c3d6765 | -2.39523 | -48.58808 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64e7b1d7-3e0e-38bc-9bdb-01259e2999d5 | -2.393 | -48.58032 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5416e092-fe57-39f8-8260-ebe280141457 | -2.39242 | -48.58393 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eb6dd46-7ff2-3c16-9454-5f2b44f16944 | -2.3918 | -48.58041 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fedaf90-7db6-3582-81c6-9cde5ac39de6 | -2.39123 | -48.58403 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06f87322-e565-3e9d-a2f8-9151ab5cdb60 | -2.34021 | -48.44682 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8fd8187-d263-3cb5-a271-7c531a6baf9d | -2.33684 | -48.4463 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac72bab5-9d24-3870-b973-ef2ce14f8c50 | -2.32972 | -48.60031 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24f27ba5-736c-3e56-8200-f121c967cebd | -2.30155 | -48.58105 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6dbe3fa-d348-30af-8b4c-25e69d3019e0 | -2.29755 | -48.39959 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96c1007c-7a2f-3303-92cf-3f2cbb76e9fa | -2.28513 | -48.50069 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc693c32-8dd4-3dbc-8c4f-b0efc73d6902 | -2.22442 | -48.23914 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4c54e0-e6a4-3f2e-a870-8470c172c985 | -3.06575 | -47.77138 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93bb2a22-adbb-3961-a747-d958f4e3491a | -3.06271 | -48.95269 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10dc9250-48e0-3c9f-a4d1-7b69bc303bac | -3.02674 | -47.93206 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8be34d4b-aac8-386f-b754-63aadc236c69 | -3.02178 | -47.94197 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2052e82b-2ca9-369c-917b-c3f9d6b92671 | -2.99681 | -48.94985 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec28f0fc-c9cb-32cc-9ca3-7f6ee5652e94 | -2.98069 | -48.63101 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65b37492-fc17-3e22-bae9-ceac1f780470 | -2.97746 | -47.92076 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab5987b7-d3c9-3468-b8a4-5c7a94b12395 | -2.97674 | -48.63407 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63d00328-5c3c-305b-9192-84bc5fb5e6e8 | -2.97617 | -48.63768 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6896f616-d559-3cac-9920-729fa2119d2c | -2.97602 | -48.92439 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5f292f6-69e0-3c62-9e4f-2eb26b05a6f2 | -2.97506 | -47.76396 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 336c9688-9ed6-37ac-b42b-d3db9b8df47f | -2.97414 | -47.92024 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a122bbb-70e3-3a92-a5c9-0b0005fbcb14 | -2.97223 | -48.64075 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aab8c28c-f30a-3548-a10a-1a5b8b8e5b8e | -2.96885 | -48.64022 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d00d6f9d-bd7b-3409-8674-86a72477d3d0 | -2.96639 | -48.72117 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68c51803-a6cb-3631-afe9-b721f6eab66f | -2.96548 | -48.63968 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80ccf16d-074c-3779-996e-b2ddb5112384 | -2.9593 | -48.63501 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee05de6d-58fe-31d8-b60c-5b66c49c396f | -2.95873 | -48.63862 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 766818e0-da31-3bbd-ab18-627c39969d7f | -2.95814 | -47.99985 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c65c9a67-34dd-3fdb-8358-6d1f51c7bb03 | -2.94764 | -48.06622 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34c8fe8d-3744-365f-8391-3e8f0d33253b | -2.92425 | -48.30039 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f62c5e49-4f8c-3b65-8304-74b2622e0c45 | -2.92192 | -48.95728 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a51b820-29e3-3ffe-aa91-628519dbc010 | -2.91699 | -48.30288 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08cc3e8f-60aa-3116-860a-4f3ef571bff8 | -2.91617 | -48.61337 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 860befa4-5fe2-35a8-8763-88ff33321b3f | -2.91336 | -48.60925 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58f5f713-47d8-38ac-bff8-feddf2d207d5 | -2.9128 | -48.61284 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5dc7306e-d543-3354-8b75-66a4193efa98 | -2.91223 | -48.61645 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 807574dd-b813-3ab8-97ac-053e901085aa | -2.91166 | -48.62005 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d96cad7a-75fa-3f69-ae68-49a806cd13df | -2.91112 | -48.60152 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04311716-47a1-3f01-b57b-8a2764b55286 | -2.9111 | -48.62366 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d69bfcba-6bfc-3870-8b0d-e2dc8683c6fc | -2.91056 | -48.60512 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acc44906-6316-3aea-a6ee-7bc784ae6382 | -2.90886 | -48.61591 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3011d23-a0e4-3437-81db-bff7744c9056 | -2.90829 | -48.61952 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c0d7baf-27bb-3cd0-a6fe-eeacc50a8687 | -2.90772 | -48.62313 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b76a2dd-43b5-3f84-b981-f589b192d8a4 | -2.90381 | -48.60406 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53188b8f-2dfe-3a11-b8dd-b2eae418e100 | -4.2291 | -48.04298 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0872655-096e-3bcf-91da-5f65f84e0a4e | -4.22855 | -48.04643 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b708c43d-90b7-3766-9b49-203d98149219 | -4.22248 | -48.06328 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e53c8693-d6d8-3a93-b17a-c849a6a68352 | -4.21916 | -48.06277 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a36ff93-f939-3dd2-abf6-0c42eda253a4 | -4.2164 | -48.05879 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c7ed1a-029f-36ff-9de8-37e2649af261 | -4.21585 | -48.06227 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ff3e95b-6787-38a0-a065-3167e18bf73c | -4.20971 | -48.55259 | 2024-11-01 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02ca7cc6-6270-3cf8-9fb8-c980c9ac662f | -4.12429 | -48.2547 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f250746d-dfab-3972-8f08-0ef14c052d58 | -4.08435 | -48.31297 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78240f0-2eeb-31a5-a984-d81d1863322b | -4.06881 | -48.30338 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb0d9191-4c80-3125-b81a-ddc17b1f2d24 | -4.06255 | -48.30211 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55ddb177-d8d3-38c9-be2f-13f56871bc8f | -4.06138 | -48.24455 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7209fcf8-4021-30cd-88bf-a309b9d80d4d | -4.06032 | -48.29459 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5397b155-a2c7-3d03-9c97-3de1ba1cd0c3 | -4.05977 | -48.29809 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b1b094a-83dd-38b1-8fc4-d9350e6b5799 | -4.02593 | -48.29632 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e3f76c9-8fb6-3ad4-acb8-0ed80a4c8761 | -4.0226 | -48.29578 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fd3c5b3-eca9-3632-b480-c45482da97b5 | -3.95913 | -48.13916 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06973db4-f34d-3e3d-9688-a9295a44d59a | -3.9427 | -48.35167 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e848799a-2673-3512-bde3-6af5e134aca9 | -3.9416 | -48.3587 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a900533b-628d-3677-8086-4bcaa63a7c2f | -3.94104 | -48.36223 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7cd8e776-437e-36fb-9d06-b9369b04d2c6 | -3.93937 | -48.35114 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 94d92b17-096e-3151-bc92-b1d04e11a995 | -3.93882 | -48.35464 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 86cb5fb6-ad3e-30ac-a58a-5c48c592893a | -3.93826 | -48.35817 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5ad6462c-7dad-30ff-9f2b-cbf5c78974f3 | -3.93771 | -48.3617 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 48fb167e-5f9d-37f5-a09e-c950ec052cb9 | -3.93715 | -48.36523 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a2bf9e8-f53b-3927-9b5b-084d8380f59b | -3.93714 | -48.34358 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 763b3c23-9a06-347b-8f8a-9e994ba4dd3b | -3.93659 | -48.34709 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 107aff08-86ce-309a-ad2c-eca913491a48 | -3.93604 | -48.3506 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a11ed7e-f5e8-3471-8ed6-4b63734b6978 | -3.93548 | -48.35412 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15633308-5772-3932-a1c3-4036209c7438 | -3.93493 | -48.35764 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b393bd3-07f8-3e47-8d46-faf0dfc63beb | -3.93159 | -48.35711 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a081533-271e-3616-9be3-ea311ca0a96c | -3.92937 | -48.34954 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc3f26dc-114d-3a60-b414-e1fcdaad7aa6 | -3.92603 | -48.34903 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85e51bd2-e1c1-3c38-bc7d-e2b5a15563e0 | -3.91249 | -47.93972 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28e7e531-555a-3078-bc7f-0e47605f719b | -3.90918 | -47.93921 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 972dd725-a564-31b9-ae29-6b68d0f62423 | -3.87266 | -48.36226 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 567626ee-87df-3897-a854-c033e7856039 | -3.86932 | -48.36174 | 2024-11-01 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b66bf3e-2fc2-3266-beb7-7a185c1f9d7e | -3.73089 | -47.64581 | 2024-11-01 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d900738a-9914-3146-8489-cc4392044a6e | -4.92888 | -49.15292 | 2024-11-01 04:29:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2596fd0-908d-3584-8d39-056954b94624 | -4.91462 | -48.64884 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0733d46-a026-3f49-abe8-4de747dd6608 | -4.90477 | -48.06808 | 2024-11-01 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e70bfb6c-58cf-3cb8-87de-c1c6d2cfdfd0 | -4.90146 | -48.06756 | 2024-11-01 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b3eee90-a42e-3591-8b69-9e4e6e2b3334 | -4.90091 | -48.07104 | 2024-11-01 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c560c47-c4f0-3713-b0a0-7c45850459ea | -4.8987 | -48.06357 | 2024-11-01 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README35.md)
