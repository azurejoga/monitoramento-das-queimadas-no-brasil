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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 875b0893-f1f7-3174-a63f-a99447f65a2c | -3.79259 | -49.86135 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40a6a76f-18c3-3e4e-83ec-613f810278c3 | -4.39942 | -50.3208 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9303f52-f690-3749-a5b6-202d2550571e | -4.27011 | -50.66774 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b3cd160-32ef-3ec2-91ca-87716fc73e38 | -4.26938 | -50.67212 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a7b5164-6ac9-3fa4-99d8-9aede98b5f04 | -4.26046 | -50.67083 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 18b0b89b-ea01-33ed-ac95-c8dafcdfe4f6 | -4.25749 | -50.66137 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2e6899ca-44c4-3b13-a72f-34358ea1fecc | -4.25675 | -50.66576 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5236040f-2a15-38c3-a8e4-4de61d8a5f8b | -4.1389 | -49.42546 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0ffc083-ac9e-3cdb-9b32-e1eff9084227 | -4.07662 | -50.52785 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6151ede8-e569-3eb8-8a25-3e4b7886fbc4 | -4.07614 | -50.01152 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 7490d2fe-21ab-36f4-a685-1b3b22f9e03b | -4.07547 | -50.01557 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| dc4d7b30-d148-3b6b-ba1d-b3ed998252dd | -4.07187 | -50.01088 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 24c425e8-e71e-3b65-b956-78e8a4b4206b | -4.0712 | -50.01492 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 2d49af06-479f-3910-b741-549abcf901da | -4.06723 | -50.03894 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cfd318b8-8aba-3547-b33b-954ed7cfbf6a | -4.06693 | -50.01425 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c917b063-b862-3212-9cbb-d54e77576a5e | -4.06201 | -50.01755 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cf9d19c-ac26-34e1-8819-d7cb532500a5 | -4.06135 | -50.0215 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22a22e8b-0e48-3674-9777-ecd07099302e | -4.04115 | -50.55375 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 696b610d-b1ae-3249-b1d5-af5023137774 | -3.92142 | -49.86997 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b25aed3-edf0-3982-ab99-d4841a07a02b | -3.79684 | -49.86202 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7252de02-f1b9-3694-bb58-6035211d770f | -3.74202 | -50.06334 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82a129a6-33c3-3cc1-9261-162d7bfa5a66 | -3.66933 | -50.11567 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1f0afa4-f733-3dd1-b598-4c852fb27f92 | -3.65702 | -50.16449 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b336258f-216d-33cb-80cd-e5f366f4816c | -3.65634 | -50.16868 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f289e4d0-c56b-3480-bbb2-5c058e05c3a8 | -3.65269 | -50.16375 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d490e917-375a-3ec1-b9a8-edc8c42e5847 | -3.65258 | -50.44143 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 877095c1-c25b-3857-bc39-cdf65fe98276 | -3.62961 | -50.16879 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42758be0-b098-3b92-8127-c5bf8588ae00 | -3.62527 | -50.16811 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfede09a-6ab4-3040-b156-72f1a2293efe | -4.13951 | -49.4218 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 982f2306-a4d4-3ebe-9869-4c335b7adce2 | -3.66868 | -50.11972 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71818793-7dc5-377c-bd53-d4f772adfed5 | -5.73471 | -49.98644 | 2024-10-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 106f0102-2546-34d4-8c2a-6b676412aa88 | -5.6985 | -49.87304 | 2024-10-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35c60d92-ebca-3d6a-901a-081a57169989 | -5.51175 | -50.89227 | 2024-10-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e21d7fdb-89e3-38c6-a3d9-ccebfb3135b9 | -5.4733 | -50.53502 | 2024-10-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98a86c23-de48-3c35-abc5-6619ea8196e2 | -5.46898 | -50.53431 | 2024-10-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 712a0a2d-0cdd-3207-aa70-0f41dfb13b85 | -1.86709 | -51.11045 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffc3a766-ebcc-3437-924f-2f661892c918 | -1.86133 | -50.99487 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb6b9d59-abb9-30ad-afbc-857a38d03476 | -1.41906 | -51.60099 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23a98f5b-c840-36a8-a24d-8054192c8e5f | -2.2009 | -50.58438 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4471ee0-e63f-32e7-922a-1c91675efa46 | -2.20073 | -50.58203 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20f8b58e-5814-3248-bb07-f1ff9e0c3b7d | -2.19999 | -50.58672 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf296cdb-72dc-3b04-8570-66575b41a522 | -2.19925 | -50.59138 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2edb6f42-3a4b-3013-b78b-b57272980c2b | -2.19633 | -50.58365 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77e43604-719f-34d2-a05c-ea0514ffec8a | -2.19616 | -50.58131 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84862fb7-8699-33ca-9bee-7bc9473fd0db | -2.19556 | -50.58831 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1416971-f4b6-38e5-8902-a30d26f8257a | -2.19542 | -50.58597 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 524bc686-0748-3946-b3aa-d94034a438f4 | -2.19468 | -50.59064 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 747bf886-dc4f-3b6c-9a2c-e482199d1397 | -2.16506 | -50.62931 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b245a0d-e378-39e8-b5c1-e8be05b4c4d9 | -2.15542 | -50.80122 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ae0d44b-564f-3b12-b675-812ccbc6ff73 | -1.96691 | -50.72358 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba824979-35d6-3472-a179-1e3fef71bb2f | -1.9656 | -50.72582 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc315e01-1665-3470-822c-30cd8bdbcec4 | -3.10956 | -51.0977 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df4ef969-fdba-35a5-abf3-6e4d21202eb0 | -3.10875 | -51.10259 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5e98ce0e-8c0a-3aad-a01f-72c8fc814774 | -3.10489 | -51.09698 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86c3100d-7f92-3620-a320-14d1520fc68e | -3.03727 | -51.4426 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5be735a9-a949-3bea-80b2-fbe72c26d674 | -3.03638 | -51.44788 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13e31109-ec19-352c-bdc9-660ad9981d1a | -3.02973 | -51.78641 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e48c515-944c-30ca-8d30-734b61e0df88 | -2.87222 | -51.31068 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59489bb5-0ea7-3399-a7c2-e0904643bd5e | -2.80154 | -51.953 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62399132-561a-37ee-bb7d-5bf737cba118 | -2.78569 | -51.95625 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aef99c2b-01ea-39fa-b423-6fabc500a4ad | -2.74045 | -51.72705 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3910b3a-0f95-311b-b999-d988314a4102 | -2.65056 | -51.75246 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b21eac2e-1304-3885-a5ce-0a3a77c90e2d | -2.64962 | -51.758 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a51fe31-a9f2-38f8-be4d-6ed200091de4 | -2.64863 | -51.75051 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d51d39f-364c-3ffd-955c-114a2fd5f0bb | -2.64657 | -51.74617 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee7f7e11-8a3b-3dc6-a921-d9be991f5240 | -2.64372 | -51.74973 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 569b5c30-8d75-3705-8027-54565356b954 | -2.64165 | -51.74539 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9d8f9ad-fcca-38e1-9ec8-f6e4969d64fc | -2.64147 | -51.73238 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53c2c721-8d23-3f54-bfca-c9826fd02a40 | -2.5851 | -51.92324 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ec9bbd1-d6f7-3990-808e-418010e11a0f | -2.58011 | -51.92253 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| da5bf3ed-07ec-36cd-a137-268078d7de60 | -2.50615 | -50.46951 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e13bd13f-c1b9-3c7c-8f10-e73a86313ada | -2.48064 | -50.48409 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f71777bb-defc-3484-8d6e-e1e24856ff7a | -2.47909 | -50.46517 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84e6eda0-c386-3362-8352-ed3b5f340489 | -2.21316 | -51.55361 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68bb9144-6baa-3bd0-9e74-a6830ef671b2 | -3.56354 | -51.50346 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b282aab-96a9-3196-ab19-fd51d8b8697d | -3.45148 | -52.00409 | 2024-10-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd18112a-e585-3a92-a3a8-129d01b8f3f8 | -3.37729 | -51.07703 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aaf1644-5da5-3361-a389-32d4e175b319 | -3.29124 | -50.94149 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58854667-1880-3029-aa4a-a11abf90e093 | -3.26488 | -51.01566 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0aa3bc71-7e20-3750-902a-f223dfa5b1b7 | -3.26408 | -51.02048 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9609a35-1a39-33cc-839c-e4527afbd3f8 | -3.25946 | -51.01971 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d93ebce-38ac-3363-8015-10477cdb00d3 | -3.22462 | -51.02908 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f6b62fb-4571-3af8-bfa6-5848a9677572 | -3.2083 | -51.01919 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb20f5af-7083-34d5-886e-c4d344ac1c04 | -3.20771 | -51.0164 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce4465f0-acb8-3283-9fb4-d51e32c5ddd5 | -3.20691 | -51.02117 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c142e8bb-6db3-3acf-9b91-00b15d0336a2 | -3.20627 | -51.37173 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9551f5b3-5cf1-3803-9e27-90d4fc1323fe | -3.20445 | -51.01357 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0f8ea4f-13d9-3719-ac05-51968d1f18a2 | -3.20368 | -51.01834 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 729a36b8-b221-3340-a322-77adef813e1a | -3.20309 | -51.01558 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 907a1e79-9264-365a-b0d3-98c9d97277f3 | -3.20153 | -51.37096 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84e5bd7a-a07b-301c-a5b4-f514eaf39671 | -3.188 | -51.21913 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0a20938-0c4c-35d3-a202-113525821ecf | -3.18622 | -51.2168 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5a7100b-925a-3e37-93b6-f9d39857f507 | -3.18425 | -51.35759 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3857c9da-9e23-3d61-9144-ed5ae1e9f8c4 | -3.18341 | -51.36264 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0b96e3c-01ba-3f1b-8960-706b1f9d1590 | -3.1833 | -51.2184 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e28303f3-670c-322a-8335-189a787efb70 | -3.18153 | -51.21601 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1c31b00-4a50-3ddc-81a7-a2eae61a0af1 | -3.10793 | -51.10752 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d4b46607-fa0b-3cf2-96b4-5982237dc159 | -3.10407 | -51.10191 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d76ed0d6-2698-34e5-8999-11673d63a26e | -3.03676 | -51.44577 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e139bc5d-99d7-3bb9-aca1-1f3c7eaf8ca1 | -3.02881 | -51.79201 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README45.md)
