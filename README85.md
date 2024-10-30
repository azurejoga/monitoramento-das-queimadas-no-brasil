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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5e559cd-22ed-3f61-8630-50068e7fde41 | -3.90067 | -49.07679 | 2024-10-30 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 399f1f4a-ffa4-3058-9755-ae65e0352d0a | -3.8999 | -49.08216 | 2024-10-30 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7f3c731-20d1-3023-8904-43bf0e0eb967 | -3.94982 | -48.12847 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2b84d81e-5b29-3094-b68d-8f6153fb8b37 | -3.94935 | -48.13177 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 71b432af-0a84-364b-a31a-ed22f20f942a | -3.94887 | -48.13513 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fef580ad-eea4-3dd4-97c7-c3b456622b6a | -3.94886 | -48.1277 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 25d8ad98-b362-3505-b20c-b6e62b5882a5 | -3.94837 | -48.13097 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2a69814d-4452-3c06-b6e1-b03025dd0ea2 | -3.94786 | -48.13432 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2d935b57-10e6-3e3d-9377-bd320edf086f | -3.94735 | -48.13765 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b73447a2-3235-3156-825b-fa3ad7bfa6f2 | -3.94417 | -48.13092 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5a05ff2e-d602-3fbf-bf18-c16e35a8e47e | -3.93846 | -48.35263 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5d93a73b-144e-3de9-8e6c-cf12941c95cc | -3.93333 | -48.35194 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 81011d47-ca38-3d5f-adca-9692d66d3e3f | -3.91211 | -47.9447 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d266b2f-a246-3d60-b154-7a4a1599a943 | -5.70795 | -49.31378 | 2024-10-30 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e417e2e-2da0-3e32-9885-63d50dcd775d | -5.23014 | -47.95034 | 2024-10-30 05:08:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 165bb1c6-82fb-36de-b601-a7ad6aa7fb48 | -4.96272 | -49.37302 | 2024-10-30 05:08:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 202710f2-eb6a-38cf-b3d6-fe66406d7650 | 0.08539 | -49.875 | 2024-10-30 05:08:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ce22360-e3d6-30dd-a22a-01574e710d88 | 0.08476 | -49.87092 | 2024-10-30 05:08:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd725c63-2199-312e-a4f0-4a4a64f1d551 | 0.08107 | -49.87567 | 2024-10-30 05:08:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3813db17-8b1e-3830-b854-95bedd7a8d95 | -1.42675 | -49.22462 | 2024-10-30 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dcde7ba-1e9c-3eb1-985d-f6db8fdf97c7 | -1.42358 | -49.2143 | 2024-10-30 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16236c22-a125-37f1-9a56-952dc83d0b4e | -1.42285 | -49.2191 | 2024-10-30 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f15814c2-2008-30c8-9522-7bd8bc9f131e | -3.395 | -49.76017 | 2024-10-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 832a9f8d-f547-3d7e-bab6-b4cc539250b5 | -3.39041 | -49.75943 | 2024-10-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15436f9d-b7de-3823-8b89-c076ed36a082 | -3.37092 | -49.5473 | 2024-10-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87fd04e9-f22d-3347-8749-44b49d5214b8 | -3.36301 | -50.16245 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efaa486b-d6b5-3861-8481-3705851bbc24 | -3.35855 | -50.16172 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbf1aa9b-562d-38fa-82aa-3afbf7a239be | -3.35673 | -50.26485 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e40b547-858f-3d95-972d-3795809cd14c | -3.35163 | -50.2686 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cbaed66-bf65-3d32-9ff5-a11625cb1aa9 | -3.35007 | -49.23086 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a43bf283-0fa2-3e41-8a77-1880f152495a | -3.34538 | -49.23196 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eceb4ecb-0e33-3e47-a9c6-effaad1fc160 | -3.31484 | -50.30275 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bac7b6f-40ae-3197-81bc-701d69af2892 | -3.28528 | -50.23279 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efbe2b64-acd6-39ca-9f6d-6a5395b666e5 | -3.28458 | -50.23733 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a49c769e-4d82-33ff-9cef-9ce63b784df5 | -3.26798 | -50.34572 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3f72b129-6933-3bd2-a1e2-ada95ebb4cfa | -3.26733 | -50.34999 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 95d8e8c1-c5b5-3e92-958c-c8d3c1dfb4d3 | -3.26667 | -50.35426 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| db3d605a-c7e3-34b1-8837-df7392e8593c | -3.26424 | -50.34075 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 393ab83a-beaf-3566-8c59-74f5676f3dc6 | -3.26292 | -50.34933 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a69d72bc-c26a-3e59-85bf-f7f43a1a8bc3 | -3.26161 | -50.3579 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b70663c6-e530-3a2a-b970-0e2cb4598c49 | -3.25917 | -50.34439 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8bac26a1-196a-32bf-9c54-f6bf9a3d7732 | -3.25721 | -50.35725 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7ba1aa53-0b55-390c-97b1-ed1f26257295 | -3.25655 | -50.36155 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73dde9ba-9f81-3586-8760-69e61abbd0ff | -3.25477 | -50.34373 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 325e7b54-095e-338c-b78d-4333b255d03b | -3.25346 | -50.35231 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b97fd9b4-9682-325e-bde3-4fc76c8227b5 | -3.25281 | -50.35661 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0bce022e-e70d-3bbe-b0f7-af5c1670765a | -3.25215 | -50.3609 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ef40939-e400-335e-8058-d886764d06cb | -3.25037 | -50.34305 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e63d332c-572c-31e3-ac4e-8914115b6f42 | -3.23121 | -50.58553 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcd6a9b1-3055-36fb-90ab-fe926d3de012 | -3.22383 | -50.18804 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e6f1f9e2-9672-307f-afb9-a4af72ffdbc5 | -3.22319 | -50.19236 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4938c0c4-4b1f-3259-8ed2-75a73d44f61e | -3.22002 | -50.18304 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 997cbde4-95ad-3652-8805-d362a1314294 | -3.21937 | -50.18744 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce58523e-ed44-325e-b3f7-e4c98d1738d0 | -3.18552 | -50.38582 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e040f4fd-bf3e-3531-8bcd-c8471fc27dff | -3.18113 | -50.38515 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57bbab91-fd06-3f48-bd62-f51da8ac1db2 | -3.1805 | -50.38942 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc4b2373-35d9-3e51-af5a-f005b56f20ab | -3.18006 | -50.39095 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 991f46d9-558b-3fde-b156-6d92d3baa670 | -3.17988 | -50.39367 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fb1459f-421a-3e86-a2ef-b3c41b61514b | -3.17925 | -50.39789 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e1d7ac3-f89c-38bb-8d08-95ea6651870a | -3.17634 | -50.38605 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b781da8-9092-3be0-9470-38d5f9c94fb8 | -3.17612 | -50.38876 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2d34bbb-286b-3b71-9616-18e14fa9a4c1 | -3.17568 | -50.3903 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f555fba0-56aa-35a6-af1e-f54eedc9cf9b | -3.17549 | -50.393 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83110c1a-4ce3-37b8-bf70-1300792e85a5 | -3.17502 | -50.39453 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac995563-d281-3b63-a32a-d0adac1e28df | -3.17437 | -50.39876 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9923f755-703c-32b8-a531-8700b6574c66 | -3.17307 | -50.58944 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c51fe3b2-71f8-38cf-8791-17ba209714a4 | -3.12501 | -50.36954 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc65dc77-58c9-345c-a16b-b458c376d1e4 | -3.12129 | -49.2928 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5c0a5d7-83cb-3468-a5b5-5e3cee999a1a | -3.12062 | -50.36892 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e5fe369-fc18-3466-b5b8-7f67a47a8949 | -3.06861 | -50.50739 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 734cb91f-e77b-3ac4-859e-6f966354dc99 | -3.05451 | -50.41614 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e77677c2-eeac-3c7e-bb9e-2a444f7a2ad3 | -3.05014 | -50.41553 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f064d211-ff76-3a94-a338-990f86891028 | -3.04576 | -50.41491 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7b4b190-8097-36c4-9346-8efc7baf7bd8 | -3.0414 | -50.41425 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecc1912f-6224-3c3a-870b-a24ec39d4b20 | -3.04076 | -50.41841 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec7f264-7996-36c7-b873-7b0a8a64eb23 | -3.02892 | -50.40814 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3b6fc51-aa98-38e9-9484-02b64013692b | -3.00336 | -49.58959 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec3d67da-dc3f-35d6-ac3b-3297464b228f | -2.97398 | -50.47668 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08775003-9164-341c-a600-0d3a6a2d0ddd | -2.96466 | -50.47964 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31086618-8714-3ae9-a509-77f791eede39 | -2.96405 | -50.48368 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 279f7acb-59c0-36ea-9640-7b8734fa3135 | -2.9603 | -50.47908 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1aaf9110-4062-35da-8634-beafa774f410 | -2.83596 | -49.2348 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b753025f-d5cf-3406-a719-94654c5d82a4 | -2.83446 | -49.24488 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6570fcf4-3d52-382c-b011-a62ef82a9959 | -2.83199 | -49.22905 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36e39622-4f95-3d46-b6b3-0ca3b4019b47 | -2.83124 | -49.23409 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 74abb333-542c-3e3e-92d9-7f5159837545 | -2.82974 | -49.24417 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c3e5472-b420-385b-a899-50bb0e804b54 | -2.82178 | -49.23269 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 036689b7-6540-320b-91b9-84db58ba9a3b | -2.80909 | -49.22039 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8a800642-4a92-371f-92ab-213d7a677357 | -2.80802 | -49.2178 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8147405-afb4-3ddd-b7bc-c5f7625cd852 | -2.80723 | -49.22288 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8187af08-9e5b-36e7-8882-d68dada4cc6b | -2.80435 | -49.21971 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 317828ac-0ab5-36b9-baec-61f83fa4f1c7 | -2.52414 | -49.09308 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff126431-ed59-3fe4-abd1-07cc01074bc8 | -2.51877 | -49.09172 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8f65a01-cbda-370d-850e-fa10388de7e5 | -2.49284 | -49.30328 | 2024-10-30 05:08:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5088d4fa-044e-3d37-8dfc-d5ac86333e89 | -2.38766 | -49.17766 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5131700-baa0-3e8d-aa7c-5aa3eed31e08 | -2.38687 | -49.18269 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25aaec39-588c-34c9-a011-c4525e6e5746 | -2.38501 | -48.94316 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53bc6eb1-c98c-3eb8-9b63-8f43e3073410 | -2.36223 | -50.32465 | 2024-10-30 05:08:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46586c7f-ba5c-3ad3-ba8c-a9378cd4fa9a | -3.56978 | -50.03692 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3f59a93-05db-3e02-be45-6c02883da1f7 | -3.56525 | -50.03626 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README86.md)
