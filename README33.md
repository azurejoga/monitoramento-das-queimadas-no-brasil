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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad83d92e-bdcb-34e9-9937-af2e5adcb3c9 | -4.11416 | -51.05175 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed644bf4-8a55-354e-93f9-2d226c1c4954 | -2.80002 | -54.00891 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efb2b84b-701f-3edc-b43d-46c40f236c16 | -3.11088 | -53.70551 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 057ea42a-14f2-3472-b391-58be41751176 | -4.10808 | -51.04729 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bbea7d37-47a3-3888-862a-292eea409fa5 | -3.7747 | -52.12456 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc2464d4-741a-37e8-baef-9bafe93b06fe | -2.35939 | -49.01749 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09ca538a-afe3-3c6b-8084-173f390a450b | -6.48665 | -47.49955 | 2024-11-19 04:46:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9eb63986-cf9e-3b2b-bc4b-f71e89475da9 | -3.51441 | -50.22873 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e4959907-a506-3a9e-ad56-d83e10a2fd36 | -0.94728 | -51.72391 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1fafd56-41db-3455-b0bc-37c9b4fa1dbf | -7.4405 | -44.68188 | 2024-11-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf9cf639-8c05-3b26-98f0-63ce77af874c | -2.79189 | -48.60273 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5b00f1e-3cc8-35c4-91f6-8159a4d79c75 | -1.2084 | -51.77913 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d387997-ea2e-31f1-b24f-14d38001a553 | -1.5032 | -52.18532 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d540df8-3cf9-3c5e-a61a-42bce2e5361d | -2.62697 | -48.55925 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd20e798-b88c-3441-9211-e40a2376e071 | -3.74268 | -54.72355 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe487ede-27f5-38dc-97bd-0b8a7a042758 | -2.37152 | -53.6839 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c8eb4e2-88a3-358b-a62f-7535d936c23f | -5.97072 | -45.36483 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46a03ff3-7750-3bae-ab03-8a87c6aa4707 | -0.82971 | -52.8649 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| febb8377-99fe-387f-a809-d1d4becf4a3f | -2.51723 | -48.36056 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eb8685d-20ff-39ff-96b3-c516b0f6146a | -5.60088 | -44.87889 | 2024-11-19 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 97ba9d44-3687-3709-991c-81752d223f66 | -2.32278 | -45.64517 | 2024-11-19 04:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3efce772-7eee-37da-beb8-06129f944bcc | -2.28512 | -50.58891 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a9775ed-5fda-3941-b01b-522c7d0b1c19 | -0.97554 | -51.72084 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53ed032b-8a6a-3cce-ba77-bbd0059b594d | -4.19076 | -48.56342 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a8edda6-991b-37c4-9366-799b19312ad6 | -4.39847 | -47.7756 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d180ec60-a67e-3cf6-a9da-984266d17992 | -2.6264 | -48.56293 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c65777c5-1f7c-3904-95e5-cbdcfa3a80d8 | -2.8134 | -54.01989 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a45e59dd-c45b-3384-9a87-df54a9c91a5d | -1.94434 | -52.10487 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a745a3b-93d3-31af-963d-3f39160593d1 | -2.14284 | -48.94407 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a87aa48-eef3-3485-ba72-65e1d08adb0a | -5.86673 | -39.66482 | 2024-11-19 04:46:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc176eec-c50d-36b1-9f77-e8ad69896e05 | -1.24595 | -51.61469 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77cbd0f3-75ee-3fc1-b7e4-dd76e336959e | -3.48525 | -48.24976 | 2024-11-19 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa226f49-b631-3a10-9c07-8c1990b5324b | -2.31843 | -48.62494 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9b7ec27-6a49-378c-9595-b5103670fbb0 | -3.04419 | -49.4695 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b7b43e2a-a76c-3dbd-add9-b140d0768813 | -1.20372 | -53.69655 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 253a7250-6e69-3967-b900-56db8ea08e00 | -1.23267 | -51.78643 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bc29643-3720-3ad1-86ab-c440c6ade1b7 | -7.47349 | -47.3684 | 2024-11-19 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 453cdab1-f400-3f8b-a92e-bad655977744 | -3.57281 | -51.44547 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9378996-8522-3be0-b05b-fa31f2f81d15 | -2.0798 | -48.53637 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c9dae81-61ef-315b-9bbd-19cf86470938 | -1.58735 | -53.80478 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1ae9abbd-d701-371a-b5fc-d194826e6a51 | -3.59373 | -43.62429 | 2024-11-19 04:46:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee07be5-bef8-3f49-8eb0-180238517f07 | -0.88877 | -51.80825 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb914c00-c72e-3704-a6e2-5bef6d47b575 | -3.16845 | -54.69571 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0716e452-291d-303a-863a-db280d98d889 | -1.95302 | -53.00786 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51f3cf2d-b298-32bc-a3d5-2b9842639b7b | -3.95232 | -49.92844 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93bd1649-c8a8-3b20-963a-ad983add5008 | -3.09498 | -51.04354 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1f672ae-a2ea-3662-9c70-0e28293d325b | -1.54327 | -51.11029 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b9dc60a-b72b-3832-8802-730a332367a3 | -0.97215 | -51.72033 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64169ad0-08ad-3a06-a91c-811e6f6ddfe8 | -0.03452 | -51.12065 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a4f6ba0-15df-378c-a989-0fc24f91aa7a | -1.1365 | -52.10691 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5812ee64-1e4b-3666-9a8e-8f9b5120213d | -2.95017 | -48.3299 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ce2a9e4-df44-37b7-80a8-9ee360ebbce5 | -6.98123 | -47.82258 | 2024-11-19 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e69b09f-1d2e-356b-84ca-c615b8d785c1 | -2.07696 | -48.5322 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 502b1cfe-2e8e-3423-b0f1-2ef715abe85b | -3.94846 | -49.9314 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfc9b6b2-fb67-3e70-bf70-788c6d4b7ad5 | -4.11362 | -51.05519 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6c245393-d993-39ba-92a6-a2beceff2b08 | -2.28932 | -53.63359 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 91c7d470-06eb-38d5-b2a2-01da825f0a6e | -0.04497 | -51.74752 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a234d058-7e6f-3816-8bde-2297d4610a1a | -4.0627 | -50.00641 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df1a255-1747-3dc3-90a7-459f1619ab59 | -3.60707 | -54.21304 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b465723c-c98c-3e85-aa69-df82a729710a | -2.20984 | -53.70932 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30b6a3c3-acda-3fc4-8af5-1ce723b88969 | -2.95024 | -48.32581 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 435bb46e-0547-3d94-be55-2d026aaf72a9 | -1.58365 | -53.80418 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 59e2b8d0-4dd8-38d5-9dcb-053d9b6694c0 | -3.88904 | -46.9399 | 2024-11-19 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a822f453-45b2-38df-b196-8c0631be05a2 | -5.71926 | -44.8084 | 2024-11-19 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| add5baa9-9eb6-36fa-9318-a91ff153167e | -3.50587 | -50.80811 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bb6bd50-d9a3-3e41-87ce-87a54ddb6774 | -2.90062 | -53.04831 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 239f8651-a546-3e79-8394-e520118ee49e | -4.86803 | -50.53566 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 869e8114-2e9f-37c3-9d97-30a2fc61de49 | -1.0664 | -52.39725 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 66e54d15-3037-3225-914e-7fd58d66abe2 | -2.45061 | -50.40009 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e00c80c1-a495-38e6-a1bf-8d5ed1cd9635 | -1.7027 | -52.14353 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0c09b7e3-48de-3b8c-b6bb-809b8ae34d75 | -4.107 | -51.05419 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db52f30d-970a-362c-8a5c-daba00e9c5e3 | -2.11197 | -48.10188 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1574d482-faae-3661-a27a-7b5f71792dc3 | -7.49907 | -47.35306 | 2024-11-19 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a338d017-d65e-3bba-a7d2-1ddeabed85ce | -5.98092 | -45.35432 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d250d4bc-8831-3161-a426-21613fe40be2 | -2.02602 | -51.17825 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0194be09-bdc8-3ea8-9ce8-693f2b9ace3f | -3.66593 | -50.43599 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec119f77-5e2f-3f7c-9083-223e64c0a9b8 | -4.57665 | -45.64498 | 2024-11-19 04:46:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de5e72f1-106e-3ed4-9065-34ca40f2e71a | -2.77119 | -52.60454 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d7af269e-a6e0-3ee7-b21b-ea69347ec359 | -3.98715 | -49.92311 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12407fbc-6bcb-3d12-af1e-05ee89ed74c6 | -4.10754 | -51.05074 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d87764ef-97d2-39b0-ba85-668f7a5207c4 | -3.34106 | -45.35824 | 2024-11-19 04:46:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 45e6002e-4330-3dcf-99c2-c2b735db0243 | -2.58456 | -51.71592 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 198e145a-6664-3352-a4dc-cd4a83d1b7e3 | -6.48293 | -47.49892 | 2024-11-19 04:46:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf3ea61a-621e-35e2-b370-5a74bcceaf7a | -4.26724 | -48.42676 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e9e2a20-498d-36da-b799-16bd884b0727 | -3.54922 | -54.57439 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 495bcdac-8d47-346a-bf83-9e00ad42bde7 | -2.75299 | -54.01962 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13297db7-cff8-3f1d-94fc-31c604d9b2de | -3.75068 | -52.67052 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b20ce962-8d1d-3e9e-a66d-2499f52a1bbd | -1.22203 | -51.74396 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d461e439-639e-36e6-9373-d3a39ce08de5 | -4.58275 | -48.01643 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 86d704f8-d040-34e3-ab8c-86b4508fbda3 | -2.85661 | -51.58815 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a78c419-bcc0-30c4-b7f8-444fa88d084b | -5.38791 | -40.65763 | 2024-11-19 04:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4e45cde8-2ad7-3749-8e8c-85cceda6c07d | -1.39511 | -52.42719 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a47ddc2-1a32-37ff-b052-48d7aba16afd | -3.51387 | -50.23217 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 74f8b4fc-ad24-3071-af74-602e84ee957c | -0.95746 | -51.72547 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc472fee-ca3c-3185-9f7d-03a6f1472a5e | -5.45201 | -49.68737 | 2024-11-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79d74f8f-be8b-32ca-a008-4fc11137cc39 | -2.584 | -51.71947 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 542577de-5ab9-3ba4-83d3-1c57dc4531f4 | -1.32987 | -51.86068 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24312e30-a1ea-3025-bbf4-c7f163b94630 | -3.90125 | -52.40673 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb32cf86-d8e1-306d-a4ca-16c4b9f6dc29 | -2.22871 | -50.62169 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e404a771-4766-3371-a0a3-d074426901e6 | -2.90001 | -53.05217 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README34.md)
