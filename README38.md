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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba32e855-e393-302d-bac8-e36750cbc72d | -3.2765 | -50.65982 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6838d91b-02cc-339a-9b7d-fe74756510db | -3.27578 | -50.66423 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52a266ef-4cec-37b9-904f-bab14d312c47 | -3.27206 | -50.66367 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eef790d9-d8ea-3e76-a030-026bbf7dcc9e | -3.24225 | -50.84613 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6f72c06-bc04-3d49-b248-346ece697f41 | -3.24152 | -50.85064 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9363ee2e-e259-3eb3-82ef-54528fdbbfe6 | -3.2385 | -50.84551 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51897819-14db-31b3-9278-25dbe832d26c | -3.23776 | -50.85003 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e535e678-a6e2-3866-ab6d-84bf1454a23a | -3.55786 | -51.48594 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa2dfd40-e13e-39ec-9ec4-f61392a12a73 | -3.54832 | -51.51943 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d2b01c4-a10f-3dd6-a3ec-f2b2e765243e | -3.5482 | -51.17563 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 615ce254-aacb-3070-aef1-561e9f557850 | -3.54793 | -51.5225 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41c28515-3cf2-306d-8990-51fcd9200ecd | -3.54751 | -51.5243 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e51b2e24-e98f-3009-b9ba-90ae96ab710a | -3.54162 | -51.38746 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c23a3def-9e5d-3fb6-9d05-b0af4736588e | -3.51198 | -51.59717 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d9029b4-c690-393a-9cef-036ea38578f9 | -3.47371 | -51.20918 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f7ee7b8-a4ca-34a6-9096-da7ab176bbb7 | -3.47296 | -51.21385 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e4e0327-fc91-38aa-87b9-2354e09ef74a | -3.43366 | -52.05951 | 2024-10-20 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af467a10-9ff9-3bdb-bc1a-d83fdcc71cf8 | -3.43309 | -52.06303 | 2024-10-20 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61a7c664-1f86-3ee8-a446-36ce101f5d75 | -3.38684 | -51.42929 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea913f96-17fd-34c4-9d70-1583e92568d4 | -3.36941 | -51.51173 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09b49373-1f99-34d1-b687-174701452cea | -3.30098 | -51.10898 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 429c74e1-736e-3c39-825d-f52f4ca67dec | -3.28482 | -50.94121 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f64004e-90a6-3f10-969d-92953fa47639 | -3.27859 | -51.0532 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 842e1c8a-39d5-3292-8489-9c1041658c0f | -3.23499 | -51.27707 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 437930d5-0b45-324e-ae68-59587c9cc634 | -3.23423 | -51.2818 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 964a97e9-c3de-307a-8c33-cf52c020c370 | -3.20563 | -51.02243 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9639e780-bc33-3768-9087-06aab47be3cb | -3.17954 | -51.25338 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96e51a69-018f-307e-ab55-ce705b81cf0d | -3.17569 | -51.25276 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7f22d140-ad03-3204-b73e-0668e1ea7590 | -3.16797 | -51.25159 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60bad500-ca7f-337e-83ff-464e50d65374 | -4.636 | -50.94941 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db7df82d-255e-3294-bb84-c9a857ff5d8b | -3.71273 | -51.11397 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52402d2-92b3-3fcf-9ead-54f169b139ff | -3.70321 | -51.60162 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce85725a-5708-3244-9e5a-5a883d67d83b | -3.69509 | -52.01198 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a9eb57b-a990-3616-b53c-944ed4196c0b | -3.67928 | -51.08022 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9099a6d3-dd38-3100-9fc4-a8127b7e8eaf | -3.64215 | -52.02855 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9524c13b-cddd-30d2-9c2c-3f57e08be09a | -3.64159 | -52.03201 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bdb2130-2261-35bd-ac8a-192ad6376b7c | -3.63757 | -52.03137 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69cf3e81-0516-33d7-98e0-259eeaba2f8e | -4.25387 | -50.99053 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cb17238-6fdc-3838-852f-dc9e8d658ba9 | -4.25315 | -50.99503 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b57d2871-ba9a-3a18-b6f6-ef9726cfc5ff | -4.25086 | -50.9854 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0c3b716-603a-368a-a748-74ba373543ce | -4.25015 | -50.98985 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 193d3d9a-a7b1-3603-8dce-f762fb5b82a9 | -4.24942 | -50.99436 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56691efe-012b-36e9-b836-91a3d6d0a6aa | -4.2487 | -50.99886 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53938869-e1b5-3dab-8020-15c2aacddfbb | -4.24642 | -50.98917 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27aab736-0ff8-3b69-9924-66f248f450a4 | -4.24569 | -50.99369 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 007b2d9e-245d-358b-9f78-daa64935d667 | -4.24496 | -50.99821 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55f279cb-1c58-3e3a-891a-c6a50809482e | -4.08031 | -51.13127 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e1580de-0e41-3916-9821-85b3ad4b7ba6 | -4.07654 | -51.1306 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bb72278-ee4d-336e-aae2-b363cddcbcf8 | -4.07494 | -51.06956 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9722d6a-1bc5-3631-9883-18d66221e73f | -4.07027 | -50.981 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdb4de2d-9f7a-3d3f-8d65-d3830a2c122a | -4.02259 | -51.0125 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d6ae69a-1acd-3aff-b812-c87aac69e990 | -3.98581 | -51.02538 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c03db1d7-0137-3c7d-8707-2fba53b35884 | -3.89284 | -52.12281 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6c77d40-db2d-3e50-a5df-8fc4a6874561 | -3.86562 | -50.97969 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a66e36c-6721-34bf-abf7-4a6ffd7b38ec | -3.86488 | -50.98421 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb77b55a-9ff5-304a-8412-22d154e87256 | -3.86187 | -50.97908 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddfe6df1-df2d-3f0d-88b4-ba4b2dec7c65 | -3.86137 | -50.98145 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bb69ad1-e779-3e74-8291-37a3e467d6de | -3.86112 | -50.9836 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37534a1b-4dbd-32f2-ac40-4be7e8c27b1a | -3.86066 | -50.98598 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3edf9a61-f491-33a3-a346-53dedebdf4b7 | -3.86038 | -50.98811 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d844410d-5111-3406-948d-1266d62aa0eb | -3.79791 | -51.60896 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd01c9e0-3fd7-3889-bfd8-0551015d03b6 | -3.78884 | -51.35017 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99af158b-c0c3-3f92-b89f-f43954de776e | -3.78769 | -51.97292 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63443c31-df6f-3dc5-a5a0-f810891ea270 | -3.78763 | -51.34812 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f90000c2-1902-3938-9b36-f69c6cb090c8 | -3.78369 | -51.9723 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35daf489-0fe0-3fb7-80d8-b65d19914d43 | -3.7783 | -51.308 | 2024-10-20 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47c0cab3-fb3c-38c3-b0b1-c45492a0df5b | -3.77487 | -51.97619 | 2024-10-20 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34c82111-81b8-3255-a8d8-7ef942f9b14f | -3.72594 | -50.72038 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eb8644f-ffd9-3714-8fe4-e13515b7fab1 | -3.72223 | -50.71981 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e73045b-8c71-37ea-8793-6dd25f38929a | -6.0885 | -51.21511 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5da4808-5200-384d-a37c-ed21a69d02c0 | -3.55773 | -53.10216 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5cb0ef6-7850-3a98-90cb-850295828226 | -3.55707 | -53.10619 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39599081-52d4-374e-95c9-1fc5d9b7f61d | -3.28363 | -53.04542 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fcbb5cb-49d1-34f1-b303-297d4dcdb387 | -3.2793 | -53.04475 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf5311bc-5e6a-3f24-ba05-2ceaf3dd2fe3 | -3.27381 | -52.9693 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be1c7d0-6262-35e5-bdc5-0b5dc1383a36 | -3.01785 | -52.18647 | 2024-10-20 04:32:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 347d6d52-d5b6-3075-aa17-9de8f5f20c06 | -2.99646 | -52.36722 | 2024-10-20 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a633870-f7f0-39c1-997e-927d6fa9b59d | -3.0629 | -53.24654 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ca4ec55-80ca-34ab-9843-5e4ab2947e4e | -3.06229 | -53.24552 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65978859-9b16-3292-9894-dd0837d45873 | -3.05915 | -53.24173 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a88720f-73ee-37f1-b8d5-295c7a07d6a7 | -3.05858 | -53.24073 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cefbb63-a0ec-31f9-af73-25b16f9c9ca8 | -3.05475 | -53.24105 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c40b5b63-e195-3b8a-a91f-528dfd586f26 | -3.05418 | -53.24006 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca92af17-f6b6-3ea0-89c4-af0e383aa3ee | -2.98338 | -52.84559 | 2024-10-20 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db6b2aae-521b-38cc-972a-719b1744eb94 | -2.98274 | -52.84961 | 2024-10-20 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 469a08a4-f949-3991-b1cb-5b4ecde5f619 | -2.98209 | -52.85364 | 2024-10-20 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b129675f-c213-3a85-b8d2-ef644788f02d | -2.97911 | -52.84485 | 2024-10-20 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21c68120-925f-3e99-808e-6ddcbcb56eb8 | -2.97846 | -52.84889 | 2024-10-20 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 573192c0-e537-3a02-a9ec-a9450d921e4c | -2.9778 | -52.85294 | 2024-10-20 04:32:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f289825-46fb-3d6d-880f-695fa1cd240c | -2.96017 | -52.90752 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f9ff325-379a-398b-be82-405bf2643508 | -2.95953 | -52.91146 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9073c8cb-2a87-3d4e-bc4b-daa07501eccb | -2.95651 | -52.9029 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6cd69fb-e33e-368e-9f11-82490b463178 | -2.95586 | -52.90686 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1712c5cb-0fcc-39f3-a364-3009b556f040 | -2.95523 | -52.91079 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7457045-ad9d-3383-aba7-0a3c7abb1f96 | -2.9522 | -52.90223 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 922c0e8b-14f8-3e48-bb81-f5d5c05862de | -2.95155 | -52.9062 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bbff3b61-29e6-34ae-9747-11ca4c771457 | -2.95091 | -52.91017 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 821ee520-1885-343e-8258-855be26c6c3c | -2.85486 | -53.33289 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18c1d020-2f38-38d1-9b76-0463a2ab6d20 | -2.85415 | -53.33721 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e8ad751-99c9-31e1-bd72-3c8b92788219 | -2.85343 | -53.34156 | 2024-10-20 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README39.md)
