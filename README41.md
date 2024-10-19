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
| a1f3f28e-9d8f-387f-8322-7cf393e08ea3 | -4.17866 | -51.2347 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d739131-0621-35a9-b222-b500a38260aa | -4.17 | -51.2284 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c5ba72c-570c-3999-bad9-27c96515e422 | -4.16929 | -51.23332 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0e4a7f60-7a43-304c-9064-e1adf8e6c655 | -4.16732 | -51.23096 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40cb561d-9170-3c23-a494-d8394606dec1 | -4.16532 | -51.22772 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fd582d7-fc8b-396f-bd02-661010034111 | -4.07654 | -51.13178 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ccb7d03-220e-3c08-a41e-f989b765b665 | -4.0758 | -51.13683 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba687540-029d-3230-ba2d-ed5f255e37c2 | -4.07509 | -51.14173 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cff930ac-50a9-3a9e-9cde-dc7a45c086ad | -4.0742 | -51.13401 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04ab828e-3b91-39c9-bcb0-0de4bd45672e | -4.07344 | -51.13898 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f45dcd34-098b-3a40-8147-2148d497ab6c | -4.07269 | -50.98478 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7659ca5-22a6-39bd-aa2e-9aaeb4885030 | -4.07252 | -51.12634 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69d50572-a57c-36af-92ec-201cade3f845 | -4.07179 | -51.13132 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7be32ac6-1ade-30f0-a991-fb583429e1a7 | -4.07107 | -51.13633 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf8e98e4-8b03-3d7f-b30c-e3f137b9225b | -4.07022 | -51.12856 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| effcd70c-c0df-346f-b410-bdd611c1eaee | -4.06946 | -51.13353 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18286205-bf10-3b50-9d04-d6629de84abb | -4.0679 | -50.9843 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7f1e143-c11f-3ba1-b55e-580c05be5782 | -4.06071 | -50.96743 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ea082f3-b23b-3b36-89c8-a8e9ad17d453 | -3.98381 | -51.02828 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72276d6d-7512-3abd-8f6c-e4bcd0d93857 | -3.91183 | -52.25996 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46b74f7e-e944-3149-b622-ad3e24dde52b | -3.85236 | -51.29045 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb9fce3b-76c2-3528-b9b9-f48fd22b878b | -3.847 | -51.29462 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b61d5d3-64fe-394f-a3c8-1e44c0b1adb5 | -3.83384 | -51.29494 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 517f6b7e-1ba2-331a-926f-fa7e22c4e65d | -3.8226 | -51.1497 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 506f4df6-1217-3024-9ef1-50a36f71624a | -3.81793 | -51.14897 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab225e26-62d7-30be-8e7d-b1359810a65e | -3.80669 | -51.19188 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bda0fc5c-e95f-3607-bd1f-4463991913e2 | -3.78798 | -51.34755 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb239158-197b-3f20-9a1f-0bf9f1468ab4 | -3.78341 | -51.34654 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b07a0e1b-53a5-3e9a-b5a5-a288a859330e | -3.76043 | -51.65213 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1e1e9ff-5591-34ba-8ea8-87bec1cf8cdf | -3.75694 | -52.05929 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78bc640a-ed84-3c17-9518-849b7aada52d | -3.7563 | -52.06359 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e514ef0-52de-3c91-bcb0-6d9142f1a7d4 | -3.74437 | -51.78732 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bf0dc18-b0e8-318a-b3f3-0f14a976c810 | -3.72801 | -52.13341 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9604c71f-47e0-3449-b31e-4fb351757f88 | -3.72741 | -52.13748 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77c6bdf3-8b1e-3e23-82ba-6b8b222bd5c2 | -3.70325 | -51.60176 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c7c69e8-51ce-341d-9136-e1968730721c | -3.70257 | -51.60637 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1279d2d-4d90-3bfe-9b92-a457cd7ad8ba | -3.69871 | -51.60115 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d629957-a881-3d15-b44c-36c7b032d900 | -3.69803 | -51.60577 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 858322db-5047-311f-a1c8-21a3f30db228 | -3.60411 | -52.11982 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efcb46ab-83f9-3513-943e-493a921440ea | -3.60349 | -52.12407 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd2f54e1-def9-3f9c-8ec8-f2a271cbd825 | 1.0105 | -52.22091 | 2024-10-19 05:14:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 124d21dd-e6ba-3adf-a6a3-74c90c265b8b | 1.00994 | -52.21736 | 2024-10-19 05:14:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 145cc50b-fa74-3920-8971-6840d674e928 | -0.60575 | -52.16774 | 2024-10-19 05:14:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42d0c8ff-a92c-36a7-91e6-a9076a644844 | -0.36554 | -51.79401 | 2024-10-19 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a479fc51-7902-399f-87c2-4d9417482cba | -1.98333 | -53.19246 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57f49641-9894-389d-a3a8-93d0081fa37c | -1.70542 | -52.53698 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f15bb5-9c03-37d6-98dc-d1f1a561b3d4 | -2.20866 | -51.9486 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3eebebf7-fc6a-34b5-adaa-53eb5a318be4 | -2.20637 | -51.95002 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0c81d4b-a28e-3bb3-b4c6-01c9b27eda8a | -2.08896 | -52.11434 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 596470d2-eeb9-3d5f-b6c7-cb513cfcfa68 | -2.08837 | -52.11828 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 727d6cc3-3791-30a5-be41-a7c19ea73e60 | -2.08563 | -52.11489 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d64413b3-4bae-3f6e-b8e6-47b9164e8445 | -1.8926 | -52.67418 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd0c3aed-8d5a-3a5f-8272-acb9db7371a4 | -1.88913 | -52.67346 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b7980c4-ec05-329d-8319-ea9fa0624cfe | -1.70898 | -52.54129 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b84a5083-36f2-35e6-a028-65938a9ea1e6 | -1.433 | -52.44381 | 2024-10-19 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d7b6d96-d4c8-3c73-bbed-8cb13b9e710b | -1.27834 | -52.92896 | 2024-10-19 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6f1a74a-a287-3a65-bc70-a214e7058619 | -0.87722 | -52.92953 | 2024-10-19 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72f94421-5720-3b60-9aac-8009d9b1e232 | -0.87557 | -52.93118 | 2024-10-19 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4344cd99-cf5d-39ec-b9eb-6c56cc1b8950 | -3.31278 | -52.85765 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80071c5d-ca45-3b83-86a7-1b1f4507d355 | -3.22399 | -52.61681 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f65cb9b6-2686-3312-b8f4-cc4380ecbbed | -2.98046 | -52.85477 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ade7c0d2-57f6-30e7-ae3d-27d69da6c8bb | -2.97634 | -52.85419 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6ec16035-977d-3033-abb0-de4cdc048346 | -2.97277 | -52.84999 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1d36619-75df-3b6a-876b-d42a2f53b7b1 | -2.95924 | -52.91208 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7476c44f-ca1c-3656-bb63-0e7b50a22582 | -2.95162 | -52.90703 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7cc39b39-4c3d-3cdb-8e62-4d4ddd47d46a | -2.95106 | -52.91075 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 2beea098-6871-3983-b5b0-7633a775132f | -2.73682 | -52.57398 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98a2a0e3-6d6f-31c2-8453-a202cc2eb6e4 | -2.73623 | -52.57777 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0c8c6e9-0a6f-3b64-b945-554099362d98 | -2.73264 | -52.57334 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21c14cd3-6507-3ef1-9d7a-3020a385fef1 | -2.66307 | -52.58191 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a6e5eb0-7909-3e92-9fbd-62d3bb818734 | -2.65891 | -52.58126 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffc71b14-22a3-3e56-9f69-b973c8d637c8 | -3.54219 | -53.02069 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d9d5163-4648-34fc-922d-80fd888fc5ef | -3.54164 | -53.02426 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb33fad2-c0b9-39d8-886f-84c6842e566c | -3.45595 | -53.01481 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 008683bd-eee5-3194-ae61-2ebf66abbeba | -3.45513 | -53.01427 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f9f09fd-fa6c-34b9-8225-ddb33aa6238b | -3.45241 | -53.01057 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3badfe7-66ae-39e3-ae6b-9219e08eb09f | -3.45185 | -53.01422 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56cbb94d-51c7-3bbe-8629-bb7fb735a1c8 | -3.40677 | -52.72567 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4533099b-8020-391f-abce-532a9ca20d4c | -3.36245 | -53.21799 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12d19ccf-206c-33f1-92c4-8309a3195016 | -3.3619 | -53.22163 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dd4a281-6cad-3335-aa1f-9035f52d0f22 | -3.05892 | -53.24049 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c6bb355-121c-3485-bb3b-dc55afb4457a | -3.05838 | -53.24405 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82777add-9a02-3622-852d-2cfe2047d1f7 | -3.05491 | -53.23986 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6db7f9ed-67a2-33f0-9007-315f928fe1ed | -3.05437 | -53.24342 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44e5c974-f6f2-32da-a4f6-984a0885ec68 | -3.04769 | -53.26024 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a139228-8ee2-372d-9412-30c0e3a32158 | -2.98101 | -52.85112 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| dc120717-88a6-39d4-a299-56442612d9f6 | -2.9769 | -52.85053 | 2024-10-19 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3aac9924-9acb-309e-b824-137c5572b5a4 | -2.9557 | -52.90769 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9bf6d33d-d587-397a-8454-c53b4bc5bec8 | -2.95514 | -52.91143 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c8626dc0-9bf9-35b7-81ab-075ae1d4b728 | -2.9546 | -52.91505 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 79b0394e-f786-388b-9033-13194103f2a5 | -2.95051 | -52.9144 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 2db63a0c-2e97-30dd-93cc-64d2ae117465 | -2.85661 | -53.33325 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 092302e4-e55b-3791-84ab-c488b9b36264 | -2.85639 | -53.25583 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57db7f42-4999-3e7c-9fbd-35123c9dee9a | -2.85608 | -53.33669 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71396c28-a941-3841-a481-f5893d5ec8a2 | -2.85476 | -53.31898 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37e5fc23-f0b4-33ad-8a10-58f1dc4b11e6 | -2.85316 | -53.32924 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3fd4ad19-dd7b-3b82-a0a3-e51cac6e2eb2 | -2.85263 | -53.33267 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36d34dbc-1312-395c-b22d-dc244ab61eee | -2.8521 | -53.33609 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7ae1d256-9d6a-37ba-aea2-41beee8b6934 | -2.85157 | -53.3395 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7fdb34da-db7f-3920-b419-5832b669b9a9 | -2.85025 | -53.32179 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README42.md)
