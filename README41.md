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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 613c2bb8-5655-3ec4-873f-7c4506b11889 | -1.2189 | -51.743 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6e69540-238c-309d-8481-1e2bc481fbe9 | -1.65166 | -52.66779 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4206b1b-ab96-33da-87ab-e5858efb6af8 | -3.23485 | -54.24527 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 95365ad1-4c63-3a35-9b32-278ec027ccc9 | -2.72155 | -45.70262 | 2024-11-22 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7191e790-f463-3863-b9d2-f22539a65c44 | -1.87228 | -54.36367 | 2024-11-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62b4f484-edfd-38d5-8f92-02934085b25e | -3.18285 | -54.32 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a997c751-d45d-3b0b-b6fd-f4472a3aea74 | -3.6224 | -45.76721 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d3a200c-3718-31e4-ae2c-b449a826dc8e | -2.71504 | -52.96025 | 2024-11-22 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 707c6eac-95e8-31cb-8509-91e1159b3eda | -2.7477 | -51.87861 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 07dc903e-3191-3b1f-8b15-3c6baf0b634c | -3.07089 | -53.29604 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b47be578-c463-3ea4-93b0-c04a450b7602 | -2.22404 | -53.72738 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a033e99c-9dbc-3ee0-9fd2-0dca5f38982e | -1.62936 | -52.68393 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72734c0c-a88d-31d4-94f5-bafbf7086bed | -1.4999 | -51.97876 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21b1643a-b017-37f0-a089-a80269ccd4b9 | -3.23345 | -54.24528 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5c81fc6d-e9d2-3b96-b506-17c7c314b62f | -0.18536 | -51.36429 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dffd15b5-a41f-3523-beb7-3bb8e178fbb7 | -2.66003 | -46.1637 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e1c4836-bc64-3938-8a56-22bc35ef0d1e | -3.73046 | -50.43781 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d96d0af-5336-3f2e-b98e-83cbefa37e34 | -2.21137 | -49.87341 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c8b88cb-42b9-374b-8cb4-2f5a43ddbd4a | -3.88811 | -46.66763 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c3dc57b-0a23-3de8-9467-27568ee68122 | -0.9355 | -47.55799 | 2024-11-22 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d6bde2f-cbaa-38e4-b0f0-7e2a39a76d2c | -0.27748 | -51.56644 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0c2c0cf-7c59-3d6c-8a1e-0fa30504586b | -2.39225 | -46.79905 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c561becc-9df1-31ec-9f23-355ac7781294 | -1.22549 | -51.79731 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 277b8863-083c-30d8-861c-68ba5712a1d4 | -3.22634 | -54.23616 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 475994c9-2f81-3c1e-abb8-2abda64903ab | -0.06243 | -51.24289 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 226abe32-6df0-3a82-b798-1f21114ff092 | -3.51244 | -53.80015 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 520b5ffe-e79f-330c-89d5-5e9ddd6d3c18 | -2.07662 | -50.3213 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| be05ecc4-e2a5-3727-bbd6-f9787a4756e3 | -3.40629 | -50.98095 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfde910e-f5da-349f-ab1d-62af8f6b8a10 | -4.68928 | -40.69318 | 2024-11-22 04:36:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 19c43dc5-da71-3180-a486-d15df4df1fe7 | -4.01249 | -49.91891 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b7facdc-bc5f-372c-adfd-f8319cff9286 | -1.26725 | -51.60153 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fda2eb26-a055-3945-b02f-b10a69fca1aa | -3.67895 | -52.373 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac7ce696-80a3-3fa7-8337-ea21180f08d4 | -0.94571 | -51.64561 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dc3a8e3-65b5-3c0b-8e7e-c7dc0ef135ad | -2.86401 | -53.96762 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cff8644-90f3-3244-bc51-5c72dab5d215 | -1.83107 | -46.28424 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b798f1d7-4f9f-33f2-9e1d-7f2b33232c2a | -2.83245 | -54.01593 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 334a0491-d24d-3e7b-9e76-61c899fc9e75 | -2.00412 | -54.52259 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 041603c3-0f53-3226-9748-3e967e6e2bf0 | -1.39144 | -52.34597 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73aae972-692c-3c7a-8433-e8f46cf0ee55 | -2.64501 | -46.57027 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94918064-4182-3162-af1e-34bbacb86ae0 | -4.24162 | -50.50979 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 385e3d0b-ab7d-3405-bc75-9da4a6fcfb16 | -1.30667 | -51.8758 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6ad9622-eb0c-3de4-878f-689a81f23573 | -1.01794 | -48.0714 | 2024-11-22 04:36:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dd0404e-9b10-3dc7-8118-adacde223cd6 | -3.83662 | -46.54321 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 547d3ffa-9c81-3d57-a599-19cce190586b | -2.01022 | -54.52107 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85cea88c-8c34-3e9f-a038-77cc032911dc | -3.56172 | -54.22409 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ace8de6a-b851-33b1-9557-ede26c0aee0e | -3.0646 | -53.28481 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad42035a-ecb8-3aa6-a8db-6f48a5a7432d | -2.85104 | -53.96935 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40924126-255d-3e52-9aeb-35cdd328340e | -1.20651 | -51.74991 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9972e0d-af1c-344b-a9aa-5726cd0135fa | -1.1168 | -53.40359 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7dd19b0c-cb3c-3dcf-aa21-10ed2789c624 | -3.50614 | -53.8137 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3a42b09d-1461-3c22-adcf-fe8a88003872 | -2.14012 | -53.77837 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe614dac-5de3-3563-a056-d977040d6e82 | -1.81633 | -52.69795 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee0dca34-81e0-3a81-b54e-87d770513404 | -1.62213 | -52.60424 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c366869-49ee-3c9c-a057-9f781a993eae | -1.58155 | -50.43537 | 2024-11-22 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc4eb5cf-8848-34b3-97cb-857abb02f665 | -2.91182 | -48.32248 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cc9291e-a6b6-3271-8150-bb356bf51573 | -2.5772 | -46.55658 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b4a016d-0bad-371c-8333-718db32b0b1b | -2.18821 | -48.56081 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2fc6d7e-77d8-3f99-8df8-692220561d4f | -3.32411 | -53.19491 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cc7fad3-bcbb-3e4c-a80e-cf9ca7f0fea6 | -3.19335 | -48.58455 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e23cf25c-614f-32e8-8463-90253b688d0b | -2.15549 | -50.46585 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a6453a4-061e-35d4-bc0f-71a4dcf5a0a5 | -1.51628 | -47.06195 | 2024-11-22 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ba1fc8c-51d3-3473-b2d6-61ffacc0a432 | -2.65781 | -46.24559 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2219d47-b2c5-3eb1-b022-7ccc298f7dfb | -3.22927 | -54.24464 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 70a630b9-888a-3483-b03e-486987b908b7 | -2.89806 | -48.32387 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb67aa13-36a4-38ec-930a-f3ce5f98a332 | -1.22617 | -51.79297 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d62dd679-2eaf-35be-885c-e16cd47ba81e | -4.53863 | -50.32458 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65f18642-4f3d-3d85-bac5-7817568882ed | -2.8413 | -46.68267 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c93335e-b45a-3596-85d6-49284b0984e0 | -3.80251 | -46.60409 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3ba85c7-7208-33cf-8839-d46cdf19b7fc | -1.9403 | -49.52604 | 2024-11-22 04:36:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ed19b93-169a-34c1-b60f-6faf57ba1a9d | -3.27361 | -53.83456 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5618333-5e29-3bea-bc27-71c3e37e3edd | -3.28231 | -53.83223 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d97b594-6357-3718-b4e9-8a43d1fa4c19 | -0.84998 | -52.41162 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc825e84-90e1-3037-86a0-4c91d7299012 | -3.79807 | -50.25968 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62848a55-62c8-33e4-8f4f-ad605995e690 | -2.47479 | -49.17689 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e0011fd-aa7a-3275-8f1d-80ee1f5f4783 | -3.83315 | -46.54271 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9409220-860c-394c-b9a7-cb4fa491a611 | -3.61128 | -54.74662 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 292816d6-3125-31c8-baa1-e7c1c16c7651 | -4.08272 | -46.83484 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 384d2e2a-2d22-388c-ad12-ee49d0874ca4 | -3.4669 | -54.49286 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9748158-d1f8-3eb1-8482-d7902041b8f8 | -3.10194 | -53.99352 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24c29f56-2309-3fe5-abba-310924c40f17 | -1.19642 | -51.76603 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f64ad7c-51db-30f3-9f40-e56a0619fe48 | -2.70093 | -46.23194 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 204db5bd-f72b-3901-ad23-13f2f49b7db2 | -4.68872 | -45.66246 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c1df2b5-cc4f-3282-a28e-ed68be23b7f9 | -2.68062 | -46.24839 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05a56c33-ddd7-323c-874b-28c76cc87bf8 | -2.14389 | -50.49459 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96bde7fd-14a8-3b19-82a8-ded2cd49d8fd | -2.64562 | -46.14184 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b81b2bb-13ce-31e4-ac57-03f104f4b9a8 | -2.62684 | -46.05591 | 2024-11-22 04:36:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aa519c4-04bc-38e7-ab12-14341e1f71c5 | -4.01138 | -49.92595 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a02a40b2-2acf-371d-9d68-c56aba04eaa8 | -2.66037 | -46.60679 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23ce965-08fc-362d-a8ce-7108034f57fe | -1.47131 | -52.015 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e8df976-54f9-3cec-a99f-8848af7c3188 | -2.56208 | -47.32424 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef270144-774d-334c-8a6c-797a4968c493 | -2.52821 | -46.39614 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f222849-b5c0-3fde-8f58-323422083ac0 | -1.25459 | -51.75175 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5ce02c7-6cbe-3fec-89ae-a2bf94b5d888 | -1.77303 | -53.60093 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21e91cd3-7b03-36e7-abdf-d183aa85e83a | -2.80385 | -54.46653 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4b34f90-b4d2-356b-97bd-de3efadc15b5 | -2.59829 | -47.02688 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f2c7dc1-e558-307e-86a0-7517135ed421 | -2.45832 | -48.80681 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f25b043-372e-3098-9daf-ae1f2617aae5 | -3.24031 | -54.23817 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5ddef202-4abb-3d28-8bf7-7a94b534904b | -0.81368 | -51.60654 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcfad906-5f8f-316a-858b-f155a17ffb3d | -1.73086 | -52.70221 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 95191e68-8374-351b-b5aa-2d0a9956ba4c | -3.34157 | -53.3096 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README42.md)
