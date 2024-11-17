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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9054ca60-5eaa-3e49-a275-c4400b030c07 | -3.09682 | -51.31543 | 2024-11-17 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89138138-6fcd-3731-8f69-93374e54babb | -2.99984 | -51.4586 | 2024-11-17 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed785304-1b87-3cff-b6c9-34d50ad16d0a | -3.52717 | -50.25977 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73e6746a-9358-3593-9713-d0db3af93740 | -3.52503 | -50.24662 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b88581ff-a055-3de9-81ca-7f1ebc5c3f7c | -3.53062 | -50.24753 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42ffc6c3-7d97-3dea-b63c-5372cd8f2a65 | -1.63882 | -52.67194 | 2024-11-17 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 71319c43-085d-3953-95d1-f10384eafcc6 | -1.11173 | -51.9202 | 2024-11-17 05:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8337767c-33dc-362c-beef-c585b7749df2 | -12.39458 | -57.52346 | 2024-11-17 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e36838a4-69c7-3c1b-8aab-d47a60a2a120 | -2.32898 | -53.57447 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b95ab1a-011c-3244-9c16-8304be1041d0 | -3.66362 | -50.60482 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 168e0b77-ab06-3eec-9e6d-953a3a07eee9 | -1.21999 | -53.36737 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29a38561-9784-3260-9e6e-b1c40f9d1960 | -3.32966 | -50.49829 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 65354a95-52a1-3d0b-907f-6e76ad8c8b6d | -2.6703 | -46.21475 | 2024-11-17 05:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2d1ec86-f739-312b-b481-32d3eea07c36 | -10.99429 | -49.3602 | 2024-11-17 05:25:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da4916f2-e681-37be-9549-7d9ec590c71d | -1.63421 | -52.67123 | 2024-11-17 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 000b8ce3-fd7c-324b-abff-0e47289cca16 | -2.35534 | -47.46445 | 2024-11-17 05:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8736971-38ae-3a1b-9782-b94c3e577278 | -1.62936 | -53.28655 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c27fab1-010b-35b9-914d-6e3c06b38784 | -3.02868 | -54.10163 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5030039-b33e-31f5-a091-12603ede5d04 | -2.69745 | -49.28866 | 2024-11-17 05:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5af67e9e-29ce-3d35-b7b4-34e108472fdd | -11.00146 | -49.35556 | 2024-11-17 05:25:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5512b96-b6d1-3e49-9281-4ad71a3888fa | -2.87108 | -46.72297 | 2024-11-17 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| baee4c46-c15e-3596-93b1-8de15dc874da | -2.21843 | -47.21788 | 2024-11-17 05:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 835dd82c-d79f-33bf-93fe-39a433e62dd4 | -1.1421 | -51.69776 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e660f8d2-f5b0-329a-99fd-40a04d1bfea6 | -2.87201 | -46.71648 | 2024-11-17 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 184a8fd0-f0f3-338a-85c2-2b9f7ccb5c59 | -2.98955 | -52.60664 | 2024-11-17 05:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 406a005b-c372-34da-948a-f8e9149d17e6 | -3.24723 | -53.5205 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c43b3e9f-506e-3051-b650-e02700a12bd3 | -2.354 | -47.46402 | 2024-11-17 05:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3fd77905-98fc-3970-ab1c-e0307a77da11 | -2.99426 | -52.60756 | 2024-11-17 05:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f1006ce-fc55-322a-a18a-e41915386cb5 | -2.9437 | -54.79899 | 2024-11-17 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4945736-f8c1-3f1c-b3dc-db85ec52e9c0 | -12.56823 | -57.82571 | 2024-11-17 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25466afa-5588-3615-b0b7-b287cc48bf0d | -2.23804 | -53.60917 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c1fc30b-1b15-3a3e-81d0-1c258df0d433 | -3.0003 | -51.45557 | 2024-11-17 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d34b1567-93db-3cc8-8b30-e30537bec5b2 | -1.29102 | -51.74035 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 560a3300-d738-397e-a007-23383d19a474 | -1.36994 | -52.25345 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfea2681-7e68-3d25-8718-a5656044b17a | -2.23304 | -53.6127 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c48b4db-14ec-3c1d-ad44-900c1a7f919e | -2.66319 | -46.21372 | 2024-11-17 05:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0ff0607-9b46-3aa5-87a8-5337e26dacb0 | -2.69806 | -49.28439 | 2024-11-17 05:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32429da0-c8d1-37d0-ad75-bd4677cc37a1 | -2.34878 | -47.46338 | 2024-11-17 05:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbd66b7b-a43d-323f-a250-b9465a36225f | -2.5663 | -54.73188 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8233186f-9627-3b83-a17e-9cf31a06e433 | -2.86516 | -46.71707 | 2024-11-17 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a3564806-cc27-3d3c-8bc0-d71aabd0ca42 | -2.76295 | -54.7541 | 2024-11-17 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b3bfc8a-6044-3825-a460-75c4738492e8 | -3.02441 | -54.10098 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e875a8d-89c8-3dfe-a273-748815486e0b | -3.2421 | -53.52424 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41fdbceb-0e36-3524-b460-69aa8487a4d9 | -11.8845 | -62.97861 | 2024-11-17 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c2df77b-f5bf-3bf9-abd9-1f913c434cbd | -3.52368 | -50.24394 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32dfd984-5dc2-34a8-9215-994dd5fd1b75 | -12.39137 | -57.51789 | 2024-11-17 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 93cd1c84-b014-3baa-a816-48d15eeaca16 | -1.64402 | -52.51461 | 2024-11-17 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50996490-d0d6-3d42-8466-77682629f2cf | -1.37035 | -51.10902 | 2024-11-17 05:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d8dfc9c-7439-32a0-bae4-453c54fb70c7 | -1.91212 | -46.5723 | 2024-11-17 05:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 306e4175-ac72-3df8-a888-6792ee2f2ee1 | -12.55586 | -57.77399 | 2024-11-17 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f30393dc-b6ca-32db-b5d7-f47a0cee2dc5 | -2.22191 | -50.5107 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b82af85b-35e3-377b-94ed-54d5a9b7be4e | -1.1054 | -51.93352 | 2024-11-17 05:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 883c10e1-46c4-3a67-9523-df61d564d455 | -1.14295 | -51.69226 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3041cf6b-81ea-32bd-899b-79823d81f784 | -3.58492 | -50.52725 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f36f1692-daad-357c-9edb-e4d56ad3a00c | -2.06441 | -46.5436 | 2024-11-17 05:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa6752c2-85ea-3a70-a9ab-c0a2471e04d5 | -2.73621 | -54.11783 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 921620d1-d7ec-3dcb-aad2-be7b92d00b79 | -10.99826 | -59.08701 | 2024-11-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44fa26cd-c2a1-329d-b6a7-973b5195d45f | -2.67018 | -54.57222 | 2024-11-17 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b306d74-7d69-316c-ab67-55ed5b26342a | -2.62586 | -48.56361 | 2024-11-17 05:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd2fe301-3096-3988-8264-4a38e308872a | -2.60822 | -47.54521 | 2024-11-17 05:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f3a969f-d259-3ad0-844a-94b14ffb056d | -3.10989 | -53.74493 | 2024-11-17 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1c06e9f-a4bd-3072-be4d-e0dbcdf15f2a | -1.37863 | -51.08868 | 2024-11-17 05:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3f94311-baeb-3f00-a311-0d1c70a9d280 | -2.87112 | -46.72453 | 2024-11-17 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 272d1e6d-3b49-34ac-aed8-e6acd9a1f7f7 | -1.91034 | -52.0539 | 2024-11-17 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4e17881-6837-32f0-b0c2-cfb5a08001ca | -2.95888 | -54.44967 | 2024-11-17 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 072c814f-1f6d-3347-b80f-2289126c3366 | -3.91532 | -46.52354 | 2024-11-17 05:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39937af2-5875-3298-924d-4758c6a7411d | -10.99543 | -49.35804 | 2024-11-17 05:25:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5927ecd2-ecaf-3d5c-99d8-a5b1ea1ef60e | -1.2046 | -51.76506 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46d43ae6-5abb-3637-9a98-a5239a2e3b14 | -3.5841 | -50.5322 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a86355c6-5284-3ada-b5f5-4498d0b35e3b | -1.63315 | -53.2914 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3c9d28aa-6dd7-36d5-93f7-f60fc57d32e2 | -1.15277 | -53.79658 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dae69321-fed0-3ac4-a5f7-77b92aa93106 | -2.63204 | -48.56454 | 2024-11-17 05:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 524a648a-1a00-3f96-9085-e602adffa59f | -12.87766 | -56.7624 | 2024-11-17 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 262fb2d2-d01e-3a2a-98df-0fb6de46410b | -2.21757 | -47.22366 | 2024-11-17 05:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8d83357d-4c66-3b37-b19b-7e46e0edb2eb | -2.15642 | -50.7062 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f62a9cc-4f0d-3bd2-8f33-381f22633387 | -1.29237 | -51.96035 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e8cb977f-4bbf-3f22-99d2-a5c33eb786e0 | -3.03296 | -54.10227 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92d378a0-72f0-3073-92ff-8c2c7db7c01c | -2.87208 | -46.71809 | 2024-11-17 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28c321f1-4b40-3a05-8a75-65c6197d6212 | -3.33018 | -50.49472 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa772114-e964-3473-9183-53ff777224e9 | -3.39698 | -50.73292 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cd33801-1358-3fd9-acad-97c7d300901f | -1.79746 | -48.43814 | 2024-11-17 05:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9021c86-6e30-3066-98c3-5b5ac21d9ff7 | -2.99499 | -52.6026 | 2024-11-17 05:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 621ad337-8cbc-337f-8b06-e7f82c40211f | -12.56054 | -57.82462 | 2024-11-17 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05388397-937a-3207-bc12-940f1f0aeedf | -2.57038 | -54.73246 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b34d9e5a-0f40-3d9e-8c48-3dd99273edfe | -12.39208 | -57.51286 | 2024-11-17 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 085577fe-1d06-31dc-b67c-5203cc218ee1 | -1.32727 | -51.86255 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f5125de-0246-3b7c-93ae-f6320d78dca3 | -2.4156 | -54.62705 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 919d6840-cf6d-34ef-990b-2408d7d026f7 | -1.20293 | -51.77595 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88ed8c82-5b9c-38f9-900c-b365fae43be8 | -3.53009 | -50.25109 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77e78644-7ac3-3a53-b23c-bcf7c0b2b7ac | -1.13046 | -54.17128 | 2024-11-17 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ac78927-8d0e-3c8f-8973-44892886f968 | -3.56186 | -50.25746 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c6de7a4-923d-3a7e-8903-ef01e123a61a | -10.99492 | -49.35454 | 2024-11-17 05:25:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89cc069c-1dc3-3e21-842c-a1b41643df10 | -1.20781 | -51.77669 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c1482ca-7676-3ffb-bb14-b02890cdf236 | -3.52338 | -50.25764 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e98752c0-e0cf-3802-a5b9-fd5314749a77 | -2.92627 | -54.12052 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6bafd3a-e98f-36a7-94a8-bbb1edf18243 | -2.23239 | -53.61692 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afcf66b8-8065-31ca-8469-da201779caa8 | -1.91304 | -46.56599 | 2024-11-17 05:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ee71798-d8c6-339d-8b9d-75a683fd95bc | -3.52559 | -50.24287 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2446ba54-ac18-37ba-8d27-7cfd23f2f587 | -2.80132 | -52.99448 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63aabd5f-cf25-3198-9c1e-9d05a6f12fca | -12.39528 | -57.51844 | 2024-11-17 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README63.md)
