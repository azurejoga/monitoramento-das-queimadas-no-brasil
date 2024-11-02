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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4165e73-8120-3b32-b4ff-df81dab630f8 | -2.96793 | -51.42732 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24d6ba4f-e548-3455-a1f6-485e7a77d9e7 | -2.96728 | -51.43169 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ec50559e-823d-3671-9da3-c99455f2678b | -3.66558 | -50.75676 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f9a081-a6f9-35b7-b3ee-4ff43f658901 | -3.63272 | -50.79125 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b4a5aa1-e08c-3468-b072-a93c5828cc49 | -3.62886 | -50.79068 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e98f1aa4-c59d-3629-a211-65ad0f176a47 | -3.59839 | -50.75631 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6700b517-4c3e-340c-a454-aa51d5eb0d50 | -3.59694 | -50.75448 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 954eef23-dbd3-3765-9caf-a9a1b3d3f15f | -3.59619 | -50.75936 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d8b7e17-ef80-3eec-abea-79c4821cc6ae | -3.59452 | -50.75571 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16394443-ab5b-397f-a77e-6e8e0cdf69f4 | -3.5938 | -50.7606 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 990919f2-9901-34c6-81be-f0ee94108825 | -3.59307 | -50.75388 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 083c52ed-2f9b-34bf-96b2-223db3f1cafa | -3.59233 | -50.75874 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efb6df7f-95ea-3386-a6f1-b3cd5933699a | -2.6523 | -51.75341 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da06c297-b0d3-361c-9a73-362da23105f6 | -2.65166 | -51.75756 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1beb34f-c358-34bc-b470-2c9d81a95969 | -2.65085 | -51.71482 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91771713-e26c-31e4-9d73-8a9853e6c18c | -2.65021 | -51.719 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8645a2d4-b1bc-3b0a-84c2-40992eaad312 | -2.64957 | -51.72317 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 74f5da22-089a-3610-9f77-55af1883d91a | -2.6487 | -51.75286 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ff45efa-effd-3140-9eff-d5172199b242 | -2.64806 | -51.75701 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e62c0055-776e-3593-a081-b6f714a1d730 | -2.64723 | -51.71428 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff2a0ce1-f95a-3f24-96f0-94b508b26ef4 | -2.64659 | -51.71844 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 370847cd-bced-3cb9-8578-0ee1d1c67822 | -2.64509 | -51.7523 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96277fdb-17ed-3347-93aa-c024927b3745 | -2.64445 | -51.75646 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84839a38-119c-37d2-b318-da48dd2e8dea | -2.6434 | -51.73928 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a125b3ea-da21-3b36-974b-7951a64b6947 | -2.64212 | -51.7476 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92575818-a272-3927-9330-08d76ff21b27 | -2.64042 | -51.73456 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 363f4571-3909-3c19-bcdd-cb24cfbe2619 | -2.63745 | -51.72984 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed5fcc9b-1739-3de9-ac7f-bb237d41d312 | -2.63681 | -51.734 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80a5db2-d533-39a7-a730-37e15730e5e7 | -2.60884 | -51.77221 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc9f2676-af7d-3ef6-89c5-7c6e360ab062 | -2.60586 | -51.76752 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7e39902-1938-3b7b-b2e0-2b751d887cef | -2.60523 | -51.77167 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 110cb1ac-499b-3867-8cd4-ffc58ef9c4d7 | -2.60051 | -51.94707 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8faf99e-27dd-3d56-af34-cb4897b7aee3 | -2.58574 | -51.92411 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b22baa0-45e9-3dd5-949c-28bd6b7b53de | -2.58368 | -51.86531 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfbc44a7-afad-3d3f-9137-c83c263e306c | -2.58258 | -51.84834 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e10b4f15-f230-3ba3-8256-f0ab2969e450 | -2.58216 | -51.92355 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 674a8bf1-e93e-37fd-a8f3-be03479b74d2 | -2.55082 | -51.91974 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bf58193-9a03-3524-9366-514558637496 | -2.54999 | -51.91866 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8353d8c1-d5b5-305d-a647-77cdda4b114d | -2.54724 | -51.9192 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcf7b819-57b0-352e-ace9-96dd25111e74 | -2.52451 | -51.78144 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ec7e25d-47c3-3efd-9749-8554a49a2f26 | -2.52387 | -51.78559 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 563fc847-d6e8-3d53-a571-a298a098ed42 | -2.52324 | -51.78974 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59b49ca1-6620-3871-8a2e-ffa25bad7d41 | -2.52027 | -51.78507 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79b30705-8d30-3e33-9c87-edd9f4bb0920 | -2.51964 | -51.78921 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b5b8017-48bc-351e-ac0f-c8863c3a6ca6 | -2.47601 | -51.97861 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdf93b6c-7452-3ff6-88b8-58fba4724552 | -2.42429 | -51.96389 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00dc7211-b934-3f23-a20e-0843b45240a4 | -2.28173 | -51.92287 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 881810bf-833c-3390-aa8a-8412c0c5cd9b | -2.27816 | -51.92234 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e646302-c693-36d6-970e-527870961db4 | -2.27755 | -51.92637 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6181e15-a790-3cc6-80a3-abca43c604aa | -2.2746 | -51.92179 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d7a1b14-0584-3bd6-8b23-4c589f74a9f1 | -2.27398 | -51.92582 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a1eb94ac-759c-33cc-8795-1ee08fbc4aa7 | -2.90317 | -51.77586 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 18ab8518-9142-3a4d-af81-39ea8c4d4e8a | -2.90096 | -51.77461 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1a43c959-15c3-3e79-9781-6110cfb897a9 | -2.90033 | -51.77881 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca8b066f-2679-3677-9590-c0107c2029ff | -2.89955 | -51.77534 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c87f0dcd-69ff-383b-b66c-eb136da2a93c | -2.8989 | -51.77952 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 685d7d8a-1182-33e8-bbec-51bc53807d1e | -2.89671 | -51.77827 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| af51f25e-a710-389d-a8df-7db7433ab228 | -2.88033 | -51.82769 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec00a456-3c4a-32b1-b13e-fa33646cb00e | -2.87673 | -51.82715 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c618b710-78d9-3de0-b460-742f014383fc | -2.84746 | -51.80151 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91b1c5ab-66ae-33c2-8ddc-4e45f1ecd927 | -2.84683 | -51.80566 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e83462f-72ad-3623-a5d1-83b027b9b6b2 | -2.84386 | -51.80098 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7ed6d26-c4e9-3d39-91a4-988f712c78f6 | -2.84322 | -51.80513 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c3fca8f-a432-3423-830a-389a5e5dd030 | -2.83898 | -51.80872 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd00d2ce-9540-37cb-b894-7ad9de6696ed | -2.83835 | -51.81287 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7d2395c-be65-388c-8d26-26d35c58eea5 | -2.83538 | -51.80817 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c1ed2b3-777f-3807-8bd4-a3f138ee3ec0 | -2.83241 | -51.80344 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89ac738e-e307-37f9-b216-2457c2b63ab6 | -2.83177 | -51.8076 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da4cfb1a-4ae1-3156-9a9e-3d4818e2ec53 | -2.8288 | -51.80288 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f04bd39-a16e-32cc-a649-22d7e7eac861 | -2.82817 | -51.80704 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c66c12aa-6b28-3488-8174-2676d360c134 | -2.82754 | -51.8112 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6e9dbdd-2329-3a0a-a23d-9b80da7cccec | -2.8122 | -51.96 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0012171d-eb3a-3ee6-b4b3-0476286333b4 | -2.80621 | -51.75688 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c0b0249c-8f93-3c40-89a2-a1b093a266c9 | -2.80558 | -51.76105 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 82436246-8b10-35d4-998d-be9b6cd862df | -2.80322 | -51.75215 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 994414dc-f052-3658-aa5e-5e77ddba4613 | -2.8026 | -51.75632 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f827f1a6-4521-32cc-8537-8031dc000963 | -2.79961 | -51.75159 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d8b88b7d-0adc-3ea3-a72b-ac995d43e04e | -2.74503 | -51.73632 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e942a90-513b-3e68-b8f3-2e5f187fcfe5 | -2.74439 | -51.74051 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82403f4d-4f6e-3c43-ba23-c15ee5bf5506 | -2.74205 | -51.7316 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08cba8c5-3ab4-33a9-bd1c-55a3d45f01f0 | -2.74141 | -51.73579 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62d9c51e-e6af-323e-9d56-a2f2030849b5 | -2.74077 | -51.73997 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 260c131e-de2c-31e3-aeef-4e18e1103915 | -2.74013 | -51.74415 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb40dbd5-de04-3c98-9ec4-321e431eba08 | -2.73843 | -51.73108 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b66d924-8889-34c7-8862-4f01bb1ddd70 | -2.73779 | -51.73525 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eef5fd07-1d76-3c38-9786-f215ba85d086 | -2.73715 | -51.73943 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e7a0973-bc70-373b-9cdf-3e4980ebe9ed | -2.73609 | -51.72215 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 437d72ce-8499-3640-b6d3-10863fab3d07 | -2.73481 | -51.73052 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12378802-d13d-361b-86e1-ce056f09f9c4 | -2.73418 | -51.7347 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4a9a68a-06ae-3640-9aba-7f09af5d2208 | -2.73184 | -51.72577 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac60518-c347-305d-9281-2edc3b9e2b80 | -2.7312 | -51.72995 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f150b36-23c2-3903-b7ef-b8c2e585fc67 | -2.72715 | -51.70784 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5709356e-714e-39a5-ac01-1540bdb70501 | -2.72652 | -51.71205 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6cf8d5f-386d-3073-afb7-b3ba566d7968 | -2.72417 | -51.70311 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1130a17-81f8-3205-b9cd-a6291734a5bc | -2.72353 | -51.70731 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7787e7d0-f94a-33ab-865d-343639e6ace7 | -2.7229 | -51.7115 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35c209a1-f9e3-308b-adc6-756bcea04ed6 | -3.55234 | -50.86545 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 194d9d5d-c65b-3a42-aa7f-c3cbd2542f30 | -3.53048 | -51.47186 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d8b93bc-a62a-39ca-ad5d-53d44bf8ec56 | -3.52982 | -51.47628 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfad63e1-6fc0-3877-8ff5-9a837188d7a6 | -3.51563 | -51.66957 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README69.md)
