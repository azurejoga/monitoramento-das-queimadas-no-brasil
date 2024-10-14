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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a32e703-72ea-3e9a-9171-45c97f3c3c44 | -2.57731 | -51.86049 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 708e8688-9271-38ec-b647-d078ec2855d7 | -2.57401 | -51.85799 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fa356f9-45b9-349c-884c-7fa6e19bb548 | -2.3966 | -51.1827 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46f27559-1488-3dee-8466-d56857d7c004 | -3.58198 | -51.51358 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61e8ca34-abfe-37fb-8a02-0d589007f73c | -3.57736 | -51.51654 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a4a78fa-9549-32cb-9158-4fec9a329731 | -3.56393 | -51.44044 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edb7cddf-9563-361f-8e2c-bb64907c367d | -3.55984 | -51.43985 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 208a870b-2336-3b6f-b8d8-9803fedb0d51 | -4.6397 | -50.93351 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 756bb216-c779-37e4-8820-3feda0dce256 | -4.61513 | -50.95058 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3eea4bc-086e-39f0-8b95-88700320bce9 | -4.6145 | -50.95475 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a6e3eb6-53f5-3061-998b-9953f66b5a03 | -4.61084 | -50.94986 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08005b46-d2ab-3446-bc9f-c0ebd82111c0 | -4.26788 | -50.95883 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 150b0256-dcc8-30fd-b6e9-3bfc58ac3d03 | -4.26728 | -50.96289 | 2024-10-14 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e260e6d-4fad-3c52-85ef-ac7adf21d4ef | -4.26421 | -50.95416 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b01342a9-32d3-3835-8fd5-d540da89a7b3 | -4.26361 | -50.95823 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd98a584-2ff5-313e-a742-ba1911c45782 | -4.12398 | -51.11332 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 622fde46-6eaa-34e3-b326-b21c038f23a0 | -4.07284 | -51.07875 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f634b49-9c06-3231-aefa-016c04f03541 | -4.06921 | -51.0742 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a087024c-b87a-3a5d-ba46-10c983bdd649 | -4.06861 | -51.07811 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecf9dabc-b21b-3e3a-ae4e-ca4ab4fe7950 | -4.03973 | -51.09774 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbe7fb79-2cb2-344c-bd41-4de19ad1325f | -3.91175 | -52.20952 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eefa9aa6-feef-38a0-a7d7-b365677fc28f | -3.91174 | -52.21113 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eadfdb2d-59bf-3a3e-b09f-e7bd013dbbc2 | -3.8965 | -51.91155 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb26f83a-a82a-3977-bdde-2a61372a9d20 | -3.89598 | -51.915 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0a5dcd9-8e96-3360-882f-1165183fc069 | -3.88893 | -51.93483 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8aa9d776-56f6-36cb-a73e-35854aaf850d | -3.8879 | -51.9417 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52d2312f-08ef-396b-b146-0b9d2e8ae54e | -3.88391 | -51.94113 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 966aad0b-192d-31a3-9288-c141291ff7c2 | -3.87063 | -52.26904 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63b5104e-022c-36b9-86fd-5dc06045f057 | -3.86673 | -52.26847 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d9cfb2f-f393-387a-a99f-8dab58657195 | -3.83395 | -51.38264 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a86e38f0-ed1d-3429-87da-9fe6f75fb78b | -3.83068 | -51.40486 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db7e19ef-432a-36cd-8e91-990741ce3337 | -3.83013 | -51.40854 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d5dd741-fa8a-30e7-98fb-7c2f1f0d57bc | -3.82786 | -51.40448 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17077428-1547-3163-9375-f90634fa4dcf | -3.82729 | -51.40816 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1501069e-dad7-390e-90f6-ca1180317007 | -3.82601 | -51.40794 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85b5848d-fcb7-30b3-8004-78cefdfaf97a | -3.79041 | -51.17604 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbca9e68-897e-3c1d-8b84-244ed9eed1a8 | -3.76703 | -51.86354 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3190825e-a60f-3d70-b775-6b253b296090 | -3.75017 | -51.332 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e43b7dfe-dd75-3a4e-ac65-1875a92219ef | -3.74571 | -52.24805 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36c9d3e8-fc4b-393b-b361-adf5f5b898dc | -3.72913 | -51.2061 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01383cb0-eb1a-3300-8bfb-e4115aedb602 | -3.71409 | -51.79469 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6ff512f-361d-3d2c-81f7-45d119eb3e14 | -3.71008 | -51.79411 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b94a12a8-8c9a-3f44-923e-9cee99b91353 | -3.62044 | -51.53426 | 2024-10-14 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1aaa03cf-5111-33f7-b23c-7197671ac69d | -6.41047 | -52.70699 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 050c0049-8e32-3359-8fb2-eea5eedbfb12 | -6.40972 | -52.71201 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc0e04ef-6188-3fe7-b950-5cb1ea827f49 | -6.40654 | -52.70644 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4872804-2731-37ff-af35-210f82f9701d | -6.40579 | -52.71143 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c37ba585-6ce8-334a-ad8a-c3f57aacb832 | -6.05933 | -51.22455 | 2024-10-14 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b774fedd-2128-3650-9810-c4093e7e7067 | -2.00593 | -53.30071 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c73eb8df-ce5b-32e1-a6be-41b7a1197224 | -1.93805 | -52.103 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e46c0001-2f5b-358d-8c45-bbe6aa771ecf | -1.93494 | -52.09772 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 308bf14b-4eda-34b6-86d5-36857bc2a9b4 | -1.93421 | -52.10244 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f680a103-0fc1-340f-860d-bdb7a535a77e | -1.71814 | -52.52721 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1644fa2f-ebb9-3d9f-a2de-d7bac44abb57 | -1.71035 | -52.50317 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13e2637d-71c3-3c10-8455-a9a1fd6faa8f | -1.70967 | -52.50764 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cb7b236-167d-3e24-ab30-b733350ef7c0 | -1.70846 | -52.50531 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b639281-6f64-39ac-a411-b932783767c2 | -1.65795 | -51.99065 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f62a4780-2211-31d0-bcfb-7dc347836392 | -1.65732 | -52.13772 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dfc83ae-0fa6-31a6-8b8a-0b45446fc3c6 | -1.52075 | -52.07336 | 2024-10-14 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f152d6f-df37-3b3e-a356-256d8a2927ed | -1.3553 | -52.94149 | 2024-10-14 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49f05ffb-2742-3ce5-a4fb-3d92790f6858 | -1.354 | -52.9499 | 2024-10-14 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 031c931a-4200-3cf6-96e3-aa505a45bd1d | -3.17642 | -53.16442 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 735a0862-e5a6-37d2-8be4-4204048d1e5f | -3.10282 | -53.03506 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2e40df3-cae0-3719-9e68-1d4759e9433a | -3.10214 | -53.03945 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cfe3bc3-7799-35c3-a059-12916a3f4ea8 | -3.1008 | -53.04814 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a1a41ae-10ef-3f4c-b882-0c11ceb9de7b | -3.10014 | -53.05245 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb4474e8-f1de-39b5-bab7-bfa96c521d04 | -3.09914 | -53.03449 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4190cce-9bcf-36c8-9188-199762c6480b | -3.09846 | -53.03885 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d72fbd8-38cc-3448-980b-d4fa916cbe19 | -3.09779 | -53.04321 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6266740-fbb9-32b5-b37c-e8be3a952fee | -3.09712 | -53.04753 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f752d199-6018-3714-a28e-40c5aba3d2a5 | -3.09646 | -53.05185 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40b47ae9-a4b2-3d07-8112-7588f57dd1e6 | -3.09545 | -53.03391 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b937a3d1-d1a2-338b-a15a-0f564e004dd6 | -3.09478 | -53.03827 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81c4a5c4-a963-32fc-8867-031dc1657964 | -3.09411 | -53.0426 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebf57e35-cce2-3319-bcd1-266ef530badb | -3.0911 | -53.03768 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a3829e7-129c-3d6a-bad9-4132b5f6e729 | -3.09043 | -53.042 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc3af1d7-3dab-38d3-8dc3-3bb54b26db06 | -3.08742 | -53.03709 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6b2865a-4d23-330a-8725-aa1bd461d444 | -3.08675 | -53.0414 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34dfd845-5908-3409-bb14-bf568e921758 | -3.0098 | -53.44602 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1f39bf2-ec47-3850-8862-447064d6376f | -3.00619 | -53.44551 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4217893-2ce5-3cca-a9f1-3c9204c0ae0b | -2.98502 | -53.21682 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b69e0a18-e060-3427-865e-512c2f1a5a1e | -2.84437 | -52.93654 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13bd865a-fa8a-3036-9161-a90943424dd7 | -2.67007 | -53.34724 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdced4d7-63c5-3690-813f-1931321a4d3a | -2.66584 | -53.35085 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba45564e-c2da-3fa8-9b7f-28346b042671 | -2.66469 | -53.34817 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffe04ed7-13fc-3314-a41a-3c789b265eed | -2.66403 | -53.35232 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 516abb9b-156b-3371-81da-9442546a1d4a | -2.66286 | -53.34614 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 721c8116-db7b-38df-acc5-2051d4733ade | -2.66223 | -53.3503 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efbb8301-11ae-3226-8fdc-4653fe4c3757 | -2.6616 | -53.35445 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d62febe-4f3d-35dd-a393-3c5b83497323 | -2.66108 | -53.34762 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb836f1-e0d1-3331-9b5b-e3cafa190d71 | -2.66043 | -53.35177 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f89efdf3-3d42-3be0-accd-c2b9d34a5794 | -2.65862 | -53.34974 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94a138d9-4bb3-32d0-9eca-e14c56b54151 | -2.65799 | -53.3539 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10daa1bb-81f9-36e9-a9a1-2db0b724d97f | -2.65682 | -53.35122 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 387ea412-1020-3cf8-a336-826461385213 | -2.65617 | -53.35537 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab835e65-582a-3b61-ab97-16f88373d880 | -2.65322 | -53.35068 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 192fbc0b-5c4e-39bc-9213-bb8d9226c13f | -2.31017 | -52.88584 | 2024-10-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c431df66-87ba-3ef1-a719-e2e84504d43a | -2.25945 | -53.48206 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa7ea848-65db-3cdc-adfa-77c7019e936e | -2.25882 | -53.48614 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d5bf129-41b4-310a-a5da-4631f4ef7817 | -2.25588 | -53.48153 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README110.md)
