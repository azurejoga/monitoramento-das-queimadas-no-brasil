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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7464eba4-0065-36e9-9bbd-cfee3956693f | -3.04458 | -49.52838 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 471da175-ece3-3eb8-9bae-3db29b8192cc | -3.49902 | -51.25668 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dbe7ee50-b5ef-3fd1-9d17-eb52e71127ae | -2.89581 | -49.37308 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f7ab89d-4d59-3eda-9ab4-915c9b3c8f35 | -2.6081 | -49.19353 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9c387f0-018e-33f7-aff7-65e68cd31597 | -3.15435 | -51.09452 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac2cb05f-4186-3aac-a48b-75a0ff6f591a | -3.58742 | -50.26394 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc5cdcc8-97f3-3359-aba3-057e18941ce3 | -2.44352 | -48.94499 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5017706-a748-3ab7-b65b-1293b74a5619 | -2.77858 | -51.61117 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cc95b52-168b-3b29-940d-32ec7fdaa62f | -3.15186 | -54.25751 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e9ee1fd-79c6-39a4-9b26-e5e237e200d6 | -3.90384 | -52.27371 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6531e9e2-0ff5-35b9-baa6-3f6b36f76aba | -3.04295 | -54.20884 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c7d1b8b-19ee-35ba-ae5c-e0fb46879158 | -3.54699 | -47.38178 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 606f59e7-00b8-3040-8e4e-326e0a820761 | -2.30327 | -46.74186 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f7f29d5-1957-378f-98ae-3a4a16a40c5e | -2.504 | -46.08297 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f60a4680-6090-3f2e-8b3f-677b2bf5dcd6 | -3.06265 | -50.50081 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce913058-4e5a-32c3-8b7f-843feef0ed1f | -2.9014 | -49.40239 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a25ff46-6733-3605-8609-71b50f5fb1f5 | -3.04112 | -51.25933 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 003218f5-bea2-3610-815d-68203bd4e4f7 | -2.96344 | -48.70628 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed5cfca6-0a58-3344-afc5-f2fff624e7ef | -3.17984 | -50.5794 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09307947-337f-33d5-b0f7-48627b9289fc | -4.3956 | -50.50027 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb9b9c28-286a-3785-983c-8bbc543aff20 | -3.14641 | -51.33074 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95428c09-f6c5-3c92-9b5d-1722f35a84f5 | -3.2711 | -51.06535 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f67a0475-7dc5-3896-8185-65d14c9a1aec | -2.47106 | -49.17881 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db0e7859-0aa2-3248-8668-a629eb69e7de | -3.01698 | -53.43395 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| eaf73b09-f431-35b7-9869-9612da3f16ac | -3.44452 | -50.37073 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07e96bb4-cf32-35a5-ab51-5332c6e63504 | 0.45401 | -50.27703 | 2024-11-06 04:36:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c17e595-8755-3ba1-9704-8f76c19c7426 | -3.8929 | -48.3694 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8975e548-9b86-3641-a870-c7c6579ec23f | -2.51226 | -47.44546 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e908066-7139-36c6-9758-96fcc80225a5 | -3.52593 | -50.34629 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fab8ad8d-1646-3125-aebe-713163149f12 | -4.5013 | -46.62375 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 001afc6b-cff1-38a6-87cb-5837ce9a4e05 | -2.83142 | -52.9113 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b768e669-51f4-32ba-94fc-428e3e4e33bd | -3.01618 | -53.43908 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| e4ef444b-fe88-36ca-8bdd-9e4651aad18d | -3.53793 | -50.29288 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e3412f7-98c4-3bab-a5ab-3e93c37474db | -2.33403 | -49.12203 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18777ed7-6455-3a70-849a-676c0017cc2d | -3.54183 | -47.38179 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 9fc7051b-c806-37b4-b066-5eb72819a11c | -3.08423 | -54.51252 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ec1c17b-7f83-34de-b85a-e15a3a300b51 | -3.27445 | -51.27856 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea3fe1cf-07b5-36b3-b50b-ad558d2bb2cd | -2.93286 | -51.05333 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ec73242-e6b7-3488-a4d9-addccc0a6406 | -2.90047 | -51.77964 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdfba4aa-9f74-35c7-93ae-f5a20802c25a | -3.78017 | -51.32778 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a323204-fc2a-3e14-bedf-1e6f8085c0ec | -2.79527 | -51.48557 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11dbb92f-2413-3ab4-b78d-9156a35c3832 | -3.06475 | -52.50087 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e5e89b4c-61a6-3a21-9f6f-ff5cb9bad635 | -2.97307 | -53.86921 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b004f3f2-ef4b-30f5-a55c-5571b355fb5f | -4.67988 | -45.80819 | 2024-11-06 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c08a2b55-3145-3646-b9c1-259323830fc8 | -3.86745 | -46.44052 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fe5f926-8d44-3d1a-afc9-1fc3bfa65a60 | -4.68584 | -46.39131 | 2024-11-06 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ad9bce43-77bd-3dc6-958e-2ae8aa8dbe33 | -3.01683 | -51.4371 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64279c27-b11d-3866-9a0e-430b1455f80c | -2.90174 | -48.62277 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74cc78c5-3253-3b12-9591-1a44854b930a | -2.93346 | -51.04951 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd31fd96-8801-3876-b6cb-7eac9006ae05 | -4.4492 | -49.54325 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f4bd96a-7d96-356e-bcb8-54eacc9917d2 | -3.04403 | -49.53186 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f94ed9af-ad6b-34c4-ad86-07e8d5e40ce7 | -3.96797 | -48.15048 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6663ad08-b56a-3d5f-b94f-fd155c33f83e | -5.54471 | -44.33113 | 2024-11-06 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18a20189-d045-3f7f-817b-78ea434b5b68 | -2.90275 | -48.5948 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f3d7ab-1df3-3f18-a81f-11ed62bb4f69 | -4.1925 | -51.02411 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 430fcc2d-4aca-3ee0-8060-d750e94555cc | -2.79887 | -46.64219 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77932f17-7ce4-3904-a4a7-ec714fe64f8c | -1.35118 | -51.41526 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25ab0f2e-f242-3100-8d6e-8342e90b4eae | -4.34916 | -45.8936 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34e09c79-9b18-3e9e-bfe4-b5c56380b78b | -2.836 | -52.90727 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| febfc72c-8e77-3024-bfd0-2cd0fca989df | -2.64633 | -48.51987 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54cbc7d3-c3f7-3b9e-a663-9f6f68c4f11c | -3.95693 | -48.15586 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 44bc1077-613c-3845-8202-4d2fed93ff75 | -3.44744 | -50.13595 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6343aac-593d-325a-ad1d-c37b4e340e5e | -2.86184 | -48.70444 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4772dadb-2e76-3dda-942b-c70af3ca0274 | -5.6291 | -44.17801 | 2024-11-06 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 452423b0-ddc7-3920-81a5-30ec673682da | -2.91872 | -48.6008 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 378fa026-fdf7-3fe5-be6c-01440db62174 | -3.67078 | -50.22893 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c6ce61a2-50bf-389c-a78c-f45a2edd86bf | -4.24557 | -46.00528 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef1a8554-afe8-3193-afc4-d9e941538576 | -2.33181 | -49.11461 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d463cdc9-1b4c-3e0a-90e5-287b82f495c3 | -2.23513 | -49.18824 | 2024-11-06 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cc446e5-ad9e-385a-b3f4-3293f497ce5a | -3.01267 | -53.23311 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 930e37e9-45b6-3721-bce0-ff43981bdb55 | -3.25354 | -50.93026 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14fccb09-6243-3106-8860-b04c4fb75c34 | -5.54071 | -44.33052 | 2024-11-06 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a99bd5b-7845-3dc7-89a5-0dfbfa6fa468 | -4.11551 | -46.89639 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75b62f38-e39f-39e1-ad28-2ae5adecd5bd | -3.48113 | -50.38018 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 023a4c98-efe8-3742-9611-058c44f8396f | -2.85344 | -49.49101 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5675d7ae-241e-36bf-910f-cfd82fed683c | -3.24919 | -53.40962 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e2a57e8-4f39-3857-a18b-87b39f64fdcf | -3.3544 | -50.25311 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e3d59f1-2846-3953-b707-5fa82c9a978c | -2.95328 | -53.86261 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4c7161e-09c1-34c2-a064-670e24680237 | -2.81219 | -52.93288 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d560596c-4e34-32ba-a335-24d2b1dfae5a | -3.11448 | -54.25095 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51fe8e53-4456-378a-b085-65c5fc676cab | -4.47619 | -45.67157 | 2024-11-06 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52b2e21d-bbae-3b2b-a0e8-85863355ffd8 | -3.54408 | -47.38945 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| dc3a6860-d6c8-3269-8da7-c7cf2e9a5698 | -3.2108 | -53.10372 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52ca6774-849c-3400-a65a-30c20eb3cb3f | -2.27214 | -49.19046 | 2024-11-06 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9c7a34f-0d3e-317c-a1c1-2e707149ed48 | -3.17643 | -50.57886 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 937a9553-010a-386f-830b-70df58857954 | -3.59652 | -51.57254 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4078665-7176-3f32-ad8b-0d2e31d319da | -4.04617 | -51.08702 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fe4144f-7c95-3042-85d1-1983ee2b235e | -2.80196 | -51.6024 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e59b154-8f60-3375-8ed6-ac41f99451cd | -3.95273 | -48.35725 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38df2de7-84ea-3314-8780-de8aecbf0362 | -3.54148 | -51.32696 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dbfbc4e-8134-37b6-ae59-787a702e2d75 | -4.58505 | -48.07055 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a76e07e3-38d5-3303-9ea8-e0e2c99a4ee2 | -3.52324 | -44.72438 | 2024-11-06 04:36:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c15a1974-69df-3514-91ab-f2c2da49c1d3 | -5.22557 | -44.91028 | 2024-11-06 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 207d85e8-aa34-3d4f-9f79-6e980721dfca | -3.93345 | -49.75338 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca0e924c-b99c-3f37-b93d-3e270cec0275 | -2.83651 | -51.80115 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba7c4abb-eb13-35e7-b5c2-056e0aa33114 | -4.55268 | -48.01527 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79c2c5fb-2f53-3ad3-8069-18a524687b47 | -2.50929 | -49.17458 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df0ae160-8025-3192-8210-f365387b8d63 | -2.66039 | -46.74332 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0bf4893-6acf-33da-a55f-49451f4ecd52 | -3.17876 | -51.26386 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70b86450-355a-3dae-9b03-692ce1ad2bbc | -2.89945 | -48.59428 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README49.md)
