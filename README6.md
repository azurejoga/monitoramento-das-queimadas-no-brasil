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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f243059-b96e-31cc-9dbf-3406aa9f6153 | -3.92211 | -52.12145 | 2024-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 19fa1627-a6be-3424-a457-ca257bfd5801 | 0.86975 | -52.0201 | 2024-11-02 00:54:00 | TERRA_M-M | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e265d1db-9245-3879-b600-ae9ab759364f | 0.72361 | -51.37255 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 189eaa13-7367-3d26-b4d5-f233c32c31b8 | 0.72224 | -51.38233 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1bfa2075-05e2-3134-934f-9762b8986463 | -0.7439 | -51.70517 | 2024-11-02 00:54:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2171215e-ef4f-3da7-910a-9722ebcde117 | -0.70101 | -51.67908 | 2024-11-02 00:54:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 38ec1772-a5cb-3e4b-862a-254cd5cedeb4 | -0.68327 | -51.69229 | 2024-11-02 00:54:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 3e7d75b1-81e8-397c-8c13-d0c5f71be704 | -0.68181 | -51.68179 | 2024-11-02 00:54:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 40.8 |
| bd2b1508-5ac5-3cc4-a1ac-d0d7d5b3ce98 | -0.46588 | -51.76229 | 2024-11-02 00:54:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c5c36518-dc43-3b7c-886b-8737e7bde1e0 | -1.60674 | -52.38369 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 63ee409d-0f6a-38f3-b1f4-5c2ac0e20ee6 | -1.6051 | -52.37179 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5f0f4415-7bd2-30dc-a013-6da6e8fdd495 | -1.59828 | -53.15112 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ca6fbb0d-5871-3567-8211-36f7cbeb0ca4 | -1.58781 | -52.17148 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2879a985-7e9d-38e5-bc81-cec71f649998 | -1.58621 | -52.15997 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| c0522406-8b53-3ebc-bca7-f7654c624f21 | -1.58463 | -52.14848 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| d117824c-2152-3aec-b93d-16ca9dfa9721 | -1.57619 | -52.16137 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 861a2d80-0c71-3d98-b9db-a36bc81075d5 | -1.57461 | -52.14988 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8b2eef9f-51d5-30f2-98d7-9f96b53d037e | -1.57303 | -52.1384 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 97464083-a08c-304d-a605-94e767857afc | -1.56241 | -52.21033 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 18a71347-88db-31d3-9db2-ab295f1e2194 | -1.56183 | -52.27603 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ccc0508f-920d-3cab-9fe6-40472cb45ca6 | -1.56181 | -52.28166 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 6b150b72-6e0f-363e-9f25-5b99273d9154 | -1.56084 | -52.19877 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6db7b1e3-cba7-35c9-95ba-1da851dc92da | -1.55927 | -52.18721 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 600ee7b1-163f-3baa-aeed-1596f735671f | -1.53052 | -52.12733 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a4ab6da7-1ac6-34c0-8f6e-9de5b588f926 | -1.51599 | -53.14068 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| dd412233-8d3d-3345-8008-bde46e735c53 | -1.4689 | -52.34261 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7de5a35c-b34b-3b49-95cf-1ee485e3432b | -1.46042 | -52.3558 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 68ea42ec-f64a-3980-a922-22abca7fbae6 | -1.45358 | -52.3808 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b9c80869-c246-3925-9685-fcad32e560a6 | -1.45192 | -52.36898 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 309d4ffa-bfa7-31af-a707-0ff900557d99 | -1.42227 | -52.23023 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2960fa7f-02db-368e-8625-c3be70500502 | -1.42066 | -52.21868 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 01f1b368-7c60-3e07-b33f-b4ad2bbaf82e | -1.41906 | -52.20715 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 254486cb-41f8-3367-bcb2-77f4a5547ab8 | -1.40902 | -52.20855 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 54dd0fa7-f62f-3ceb-b539-b16aed279bd3 | -1.38423 | -52.17688 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 27f9bffa-c1d1-3ef6-9c46-c5ce236481e9 | -1.34142 | -52.53647 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e4589938-817f-32e7-a7d1-d11f61ad8040 | -1.29031 | -51.94396 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ec718ce7-f9bc-335c-a342-0c870d1b9ae1 | -1.22562 | -51.76406 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bb22e247-d8c7-32c8-b1ab-f84e5a009d1a | -0.97224 | -51.78464 | 2024-11-02 00:54:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bd2595fb-14b8-3957-80ac-3ac7a2348170 | -0.88032 | -52.00328 | 2024-11-02 00:54:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7316782d-2c28-3f47-8209-0396684ff438 | -0.87776 | -51.9981 | 2024-11-02 00:54:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1408cd5d-7614-3337-8b33-deadda72deca | -1.93248 | -52.66921 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6a716e9c-ae0e-38c5-9ec3-48f0292c989c | -1.88955 | -52.13485 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8ccaf2a7-36ed-36d9-ac22-0c7c31139cbd | -1.86494 | -52.32981 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b90bb09c-b008-3381-8388-460683bf71e2 | -1.85474 | -52.33123 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3ffc44a8-e13b-34e2-9408-00120ec58dd1 | -1.8283 | -52.28027 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0992752d-336e-3571-9c71-788bf934aca8 | -1.81815 | -52.28168 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0a172024-6b34-3ad2-8698-22c92ac05ef5 | -1.75674 | -52.36276 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9feb79b2-9212-307a-975b-860d09e45b89 | -3.68529 | -52.4022 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6d61d617-f0a8-3a16-a78b-91d6e076db85 | -3.50774 | -53.01245 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| d719a541-5e11-3009-9d1b-2150898a54d4 | -3.50648 | -53.01908 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a18baf90-3b8d-3b93-9931-0a0d3d15aa11 | -3.31594 | -52.86748 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a46adf89-03d5-32c8-a586-4ccf3bce8e90 | -3.31411 | -52.85386 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 886db04a-7df2-3d86-bfe7-4ea4986e15aa | -3.27481 | -53.41861 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d053cc3b-8bfb-3df8-bb3d-7fc91388d208 | -3.27147 | -52.81071 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 13f497e9-2c43-329e-9e11-beb4f4b4e722 | -3.26485 | -53.42587 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5523e288-2f1d-37e8-860d-d37a4b008e90 | -3.26278 | -53.4109 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| e3a4fb24-7174-38a6-a2bc-3051ba8bcb0c | -3.26067 | -53.39573 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 13d65bf9-c3c6-3f39-abff-357438ff7912 | -3.25449 | -53.3511 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| cf80735d-3ada-38a1-af0d-c7aa6773a29f | -3.25354 | -53.42759 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 1db16b63-7bde-30b8-b63f-0b77616f9b16 | -3.2527 | -53.08072 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 68e79867-4e40-3939-929f-3673a62eabd8 | -3.25242 | -53.33614 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3f1abb5e-4d13-3831-9426-278239c4bd0d | -3.25145 | -53.41245 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 192.4 |
| 7ce18c53-62ab-37c0-93d6-596f0953e13e | -3.25081 | -53.06662 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2109947e-b864-3fcb-b071-c4e0783998d1 | -3.24936 | -53.39725 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2bad2091-c80b-3fd8-b8f5-b6e0f0bd6e3c | -3.24015 | -53.41413 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 16c48e4e-fccc-39ea-8394-fe55fa8ee686 | -3.23808 | -53.39895 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 955c33fe-5084-3381-ab7f-a9350ec3bcad | -3.23399 | -53.36903 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 3e5df501-2620-3950-a161-e3229a8b7e60 | -3.22884 | -53.41574 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 7551ad04-8fd5-303a-9683-f05935992c24 | -3.2268 | -53.40067 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| fc49603b-2941-3b72-a617-9fbafd3ea999 | -3.21747 | -53.41696 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2a4f783a-1278-35cc-93c9-e1ae61e9bf19 | -3.21547 | -53.40204 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 72332b29-65cc-3464-9b03-35d78ae25538 | -3.20816 | -53.43352 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dbf56a76-d39c-38b1-a3d7-202cc47884ef | -3.20612 | -53.41824 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| de277d10-8106-3738-94ba-28cd85dd7a6d | -3.20414 | -53.40342 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| fe21862b-6efb-33ee-9a78-c0ea554e30fe | -3.05749 | -53.16228 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5a67eae9-92a6-3988-bf4b-4a151e419b73 | -3.05673 | -53.16824 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 011c34c3-7049-3833-905a-6ae4b1874c39 | -3.05473 | -53.1539 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 509fbf06-290b-3e79-8a85-78fd0906a60d | -3.00416 | -53.44959 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 7a097836-40d9-3a0c-9bac-05254f94f33b | -3.00298 | -53.4432 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 014219cc-b3c2-3b30-aa5b-c63cf4f6efef | -3.00203 | -53.43439 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3cf39265-bb74-3f53-9a38-4a8b49fbc463 | -2.99496 | -52.37249 | 2024-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 81faba45-5530-3437-8f90-1d5f3f4d5030 | -2.98928 | -52.92282 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 48666980-c949-3d05-a88e-59da4dc43ce5 | -2.98739 | -52.90908 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| ba9d16fc-5c7e-3dff-b510-fddb954c7edb | -2.97969 | -53.26698 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 012ae56a-f709-372f-ba52-88b1a75c762f | -2.97954 | -53.27353 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4fcbb444-4440-31d1-bd99-6d16c2497834 | -2.95924 | -53.29099 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 79664e45-6915-37ca-99e5-bf6c1db6a19b | -2.94809 | -53.29259 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a980d326-460d-3360-9b90-800b6a6096dd | -2.8535 | -53.35563 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 80bfd60d-6bd0-38de-9c94-b6be8f54a890 | -2.85145 | -53.34056 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| bb5f7f3d-3efc-3658-bb2d-8d1af49c30fb | -2.84915 | -52.41772 | 2024-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 46d153b3-9620-3762-9222-a8e06b6ae035 | -2.84435 | -52.88585 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 6e9ede43-abbe-3003-96dc-e7d098344c82 | -2.84249 | -52.87263 | 2024-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 9e1b7468-70c9-3b19-a372-2448a690bcd1 | -2.84028 | -53.34217 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fa1ed7b8-58c3-394a-8a09-05e38185d8cd | -2.83672 | -52.88132 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 1c70bdbd-7beb-3ba8-9ec9-5113ba7a1347 | -2.83496 | -52.86806 | 2024-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 88723c9f-f30e-39f1-8149-476ec0f3c175 | -2.83359 | -52.88746 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ffa4a5b1-d20a-3fbf-8114-171ce73bcec2 | -2.83171 | -52.87403 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 97d89b6d-614a-39bd-9ee1-9b6a34eb7eab | -2.81619 | -53.00075 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| cc977d11-8326-3d4a-8c5e-7e453d06b41c | -2.80528 | -53.00198 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c05fb321-c3d8-328c-b116-6bb3e1d2da9f | -2.80348 | -52.98881 | 2024-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README7.md)
