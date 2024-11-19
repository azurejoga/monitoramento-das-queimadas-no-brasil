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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94c84f21-cec1-3e5a-881b-f3fd08ee7066 | -0.98176 | -51.72552 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6bc1cfc-98e6-3bca-b23d-dc3b45cae635 | -0.24947 | -48.52319 | 2024-11-19 04:46:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bac2faca-1f1e-3db2-b32e-a3f7c400528c | -2.35549 | -49.02053 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b63df3b-18c3-363f-a622-6faf9141f8dc | -2.25774 | -50.45741 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c003e913-a95e-3165-93a4-e26b09210059 | -2.28316 | -48.49236 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24fa584e-5ff1-3963-9d62-1f907df0d991 | -3.55296 | -51.52814 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d5f5e46-0e54-3256-b10d-bf2434a8c88b | -3.39822 | -50.73511 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c18b0c7b-aa85-3399-8b51-79b9302af117 | -3.77595 | -50.03627 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c728403-887f-3d37-87d4-50d5d832ac96 | -2.95134 | -48.32238 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40c973ad-5e6f-350d-9856-b037e6dbe6ea | -2.77522 | -52.60139 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9e99b363-4ff1-36a2-b271-1bb01f25f5d5 | -6.39536 | -44.73813 | 2024-11-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee349393-f7dc-3e17-b34a-a25ebb173d9c | 0.15914 | -51.07666 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33c7fb83-91e1-3f37-b597-9d7a999dae21 | -2.92313 | -48.95721 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6bc250d-561d-3c5c-97e0-854da9049da5 | -4.94847 | -47.80159 | 2024-11-19 04:46:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61475db4-813b-389e-b19c-698df5f6d041 | -7.48446 | -47.15652 | 2024-11-19 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d280d6ba-3d2a-38e5-b0bc-437f896ce418 | -3.66779 | -54.65739 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47e75803-c078-30c6-92d2-4340fedba7db | -3.949 | -49.92793 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a031e01-dffa-3c40-bcbc-10be4d50f87f | -2.17473 | -48.55803 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05080fdc-02e9-3ebc-924f-5fc92e15f701 | -6.22854 | -46.13206 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aae582bd-3f8b-3942-8103-b18fa2aae96f | -3.51772 | -50.22924 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 70177f80-8571-3ab8-aeb1-3e6d1c430b59 | -2.60027 | -51.79129 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 955c266a-bf17-378a-bb8e-dcd674bffb5a | -2.92144 | -48.05689 | 2024-11-19 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f660bfc8-54cb-3299-9286-79b7ba043901 | -2.78252 | -51.75424 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 795a41a8-8ef1-3cdc-bdca-5a834b943c94 | -7.89146 | -44.22262 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1773b851-12c2-3f74-840f-332dd926d2da | -2.93826 | -48.06341 | 2024-11-19 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 422323f6-25d0-326f-a654-927c59aeaa72 | -2.26942 | -50.81899 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a379afe4-2b2c-3a53-bbb0-a569b810b752 | -4.55083 | -48.01154 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7f954f3b-559b-342b-86c4-a36d412aea08 | -3.38224 | -52.80208 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7a26aa5-4fcf-33d7-b8b4-60fc324750ca | -3.21391 | -54.60719 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52d1d62b-b719-30ed-8ee4-e0418a2f26fe | -3.60625 | -51.05693 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 338efe8d-7932-3f2c-a990-22bc96fac5d1 | 0.10873 | -49.84135 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 396053fc-7aab-32e2-98eb-46d1a8cfe9ee | -2.9295 | -48.32673 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c826f4ae-83f5-30ae-bac4-b7a1280e3593 | -2.93478 | -48.06288 | 2024-11-19 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffa8593d-b3df-3ce3-9a44-0755cf341593 | -7.89618 | -44.22329 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 933d4d35-5b6b-3017-bb7b-c7c69f598f7f | -3.96677 | -49.94491 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5136a49-6b35-37c1-a9ca-3f08d6a53e5a | -5.52465 | -47.70521 | 2024-11-19 04:46:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c23d745-e03e-3775-ab8b-462a6a784fb2 | -0.97272 | -51.71667 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f93a3657-09a2-397d-8ff0-205fdd20455c | -2.60251 | -51.79895 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44757c83-3b3e-383e-9d6e-c3b0108143f9 | -0.84869 | -51.85869 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30237419-4d6a-30b3-b0dc-37fc7075226d | -2.43579 | -50.40835 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74146755-e43e-300a-b976-8ce6bca8662b | -1.60818 | -52.23165 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a3faf9e-97c7-3fe3-81ae-8210abb60c5a | -2.74974 | -54.06366 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| adb2784f-86db-34c0-8c87-b6ece08ee48a | -1.51103 | -52.09155 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b70af3a-7da5-360f-8e74-a31b5e8f37cc | -6.93032 | -45.08318 | 2024-11-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 225d8e43-648d-3863-952f-bb668412ba31 | -0.85349 | -48.74979 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 41714767-4c48-33d1-bd6e-7512bf2e5dea | -2.11638 | -53.32819 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 255fdf6c-79d8-323f-a16a-7addd0cf0684 | -1.58434 | -53.79984 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| af8819ab-8722-368c-b9e4-fbebc710e387 | -0.1258 | -51.43152 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24f9d56d-77b5-357f-a24a-dfac2829d215 | -1.53994 | -51.10978 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02e42b40-4378-3e80-91ab-e1533bdf91a2 | -6.97981 | -46.81511 | 2024-11-19 04:46:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8194e41f-240f-3d09-bc29-7ea0065d67a1 | -0.90992 | -51.74052 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 188ccc4b-e327-3aa5-960f-956db57fa213 | -2.16743 | -48.91866 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18516f58-4082-3c9c-8ea6-f24fb28e0f0d | -1.39146 | -52.09248 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58102ff9-849b-380e-a9c4-790756cc0da8 | -3.06579 | -53.28629 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0782234-48d4-3cc7-b2c6-75dd72128d9a | -3.04365 | -49.47302 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f30d5e5c-1647-3a9d-9b79-5a50517b01f2 | -4.05938 | -50.0059 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70f94155-0ed6-3c71-addd-bf3738d25f10 | -1.33839 | -52.51625 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdb9ba2e-ac35-3f06-bc6c-6e8a22aeb786 | -6.41586 | -46.1844 | 2024-11-19 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c0497f4-736e-3a56-a3bf-cff78278ecc9 | -5.58706 | -46.43987 | 2024-11-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3d5d142-27d0-3d60-adba-60614a7bcaaf | -0.85493 | -51.86342 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd6862fe-4fef-3127-9dd1-5320386b5904 | -3.4534 | -52.73183 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fa15ff6-16bf-3de1-b05c-1b2bece8e8bb | 0.11203 | -49.84085 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14197474-2798-3826-8dba-9c13d3863694 | -1.4772 | -51.96983 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb74a723-a64c-3290-a007-0a21e8a147ec | -1.44001 | -53.38591 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5ebfa88-0c87-3b26-9092-0d99474f03be | -1.37134 | -51.10111 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8cb7bdf-c2c8-3847-8f6d-ec07708e6dd2 | -4.55023 | -48.01554 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5ab342b4-6409-3180-9f06-c8fb2074e035 | -3.7409 | -54.44866 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8ea4494-7393-30d0-8f90-5918602b7395 | -3.7901 | -51.07847 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 15e1f9ef-879d-3d2d-bb9a-89dc5614e0e2 | -2.65938 | -48.48496 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e3a9775-d444-3e80-bdd4-8fe80ecc954f | -3.79915 | -52.25375 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d93f0bbb-c29d-3611-a997-28a77d349136 | -1.13733 | -51.6792 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f9f32c5-740b-3e3b-bda9-322cbef0c58c | -3.04031 | -49.4725 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60067b7d-7541-360b-8120-12f66fc7bda8 | 0.29402 | -50.85307 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92899ed0-c740-32d3-bd11-aabc7acfd3a6 | -2.02324 | -51.17425 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe496c85-4a2a-3f89-87f1-0996c3be546f | -3.95324 | -46.69592 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fdc8634-63fe-3f35-830f-8377c5c2843a | -4.38352 | -47.77753 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3d5ef72a-0dc5-35e5-9b8c-4155ae8d9e77 | -1.32589 | -51.8638 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e57a2eb-7d22-3e83-8bed-55b33cf68e6f | -4.55672 | -48.0206 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 16510b5b-8714-3750-8329-ac4235b25379 | -2.76131 | -54.0386 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f65ded55-732f-3b2b-9675-59e171db7e9b | -4.22607 | -47.18154 | 2024-11-19 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 887f2040-98e0-3ce6-b0a5-c34ea81f963d | -1.06353 | -52.39289 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db0446bd-e518-3a6d-ac54-f203bfb2f864 | -4.48492 | -46.71621 | 2024-11-19 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed435c63-342c-3967-8781-2bfa593b86e7 | -3.95307 | -46.69802 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7a87c83-da9e-37a0-a6c2-c94ee8ea5a0b | -0.85404 | -48.74624 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 23c0451b-211d-3337-a29e-5d35b46c2d98 | -1.85153 | -47.82919 | 2024-11-19 04:46:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 283f9aae-22ef-383e-a4bc-6996f2f0243d | -0.12242 | -51.431 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58cbce55-bfd2-3b04-97e9-a591df4108f1 | -3.06933 | -53.28685 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45164c1f-f1b6-31c4-9331-7acf4f3a0c81 | -1.64581 | -52.77251 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cf97657-c1ae-355a-99d1-f5e18000e337 | -4.1622 | -40.71618 | 2024-11-19 04:46:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8361311-dac3-31f9-9bbd-1b152782e247 | -1.24856 | -51.75174 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 519bf9d5-0c45-3d8b-beea-b0f7ca5bd52d | -2.32946 | -51.28283 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21ebb80f-fcbc-332c-8891-58612088ce6d | -4.01315 | -49.93115 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35e38567-ea38-3386-b60c-017932d13629 | -1.24651 | -51.6111 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8c5a4d3-5ea8-3a9b-b78e-7723d77a76f2 | -4.39488 | -47.77508 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 769b800b-08de-32dd-b17c-4436e4fe486c | -2.59127 | -51.71695 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d1e7e8d-0f8f-3a06-b449-b70e966ac299 | -2.76838 | -53.21767 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55b6cba9-62f8-3a8f-abf9-ed0e7ce635eb | -2.19758 | -53.66818 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ce35133-c391-3bc3-b563-d74cba715e97 | -1.63624 | -52.58469 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e52fb1f7-9102-3cb0-99b1-7bb123345b65 | -2.58792 | -51.71643 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33e2c149-46a2-35d8-aa7d-2a3996c4e6d2 | -1.58648 | -50.44364 | 2024-11-19 04:46:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README30.md)
