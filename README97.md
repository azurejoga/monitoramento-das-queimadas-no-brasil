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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9e1a85a-740d-30c3-9910-0227687502ab | -4.33508 | -48.58733 | 2024-11-02 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| efdb39d2-634a-36ae-82a0-c001b2584932 | -4.32754 | -48.63965 | 2024-11-02 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a228e7a4-0084-3d3c-9927-535fe2b3fb5f | -4.31694 | -48.6381 | 2024-11-02 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1f916f64-5b10-3397-96a5-44f0ec06ea13 | -4.29755 | -48.6221 | 2024-11-02 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 312801dc-810f-3aa0-afde-f9d4e2209634 | -4.27374 | -55.14368 | 2024-11-02 05:48:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1cac5b90-af93-3ec1-99f4-ba068afa2a0b | -4.25738 | -55.5102 | 2024-11-02 05:48:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e844d6a-c132-3431-99f4-777040b77cd7 | -4.20866 | -45.87259 | 2024-11-02 05:48:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| dbb1d57e-93ed-36df-8e69-afda34ffc634 | -4.15488 | -46.83972 | 2024-11-02 05:48:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1f4d70a7-964e-33a3-924d-637f8564d0a9 | -4.15196 | -46.83265 | 2024-11-02 05:48:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ea566f48-fa6b-30cf-b558-2356a31d5735 | -4.12821 | -51.07758 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0dcd58a0-19ec-33a9-995f-a0be409f6d20 | -4.12046 | -51.06689 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92b3ba77-26c3-390d-8459-de39b552ac44 | -4.11908 | -51.07633 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 35216282-b2fa-3a9c-8e22-5c075d11604d | -4.09473 | -50.74418 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa99daca-bd49-3a99-bccd-1ff4f1f3c0b2 | -4.09332 | -50.75386 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 28d3dfdb-7b3d-3d43-a423-4dd3d5bf474f | -3.98624 | -46.44199 | 2024-11-02 05:48:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 764c0f98-fc64-33c4-a25c-76179f43b6df | -3.98355 | -46.46108 | 2024-11-02 05:48:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4d5b7f74-ef88-333c-b455-b8accf07a786 | -1.21747 | -53.38328 | 2024-11-02 05:48:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6d52d461-d5b8-38ea-a06d-a284f37fb70d | -3.94687 | -48.34531 | 2024-11-02 05:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 981c6d8d-bdd0-3c9f-a33e-498140122a06 | -3.945 | -48.3587 | 2024-11-02 05:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9aca6a01-5d48-3943-b2d3-f4b46f994ee7 | -3.94452 | -48.3382 | 2024-11-02 05:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 50df0e67-7387-38a2-adde-243f7fe9bb5f | -3.94255 | -48.35163 | 2024-11-02 05:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| cda12f85-8b95-3b62-bafb-9b726089d675 | -3.9406 | -48.3649 | 2024-11-02 05:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b89cc38a-4c0e-3d8a-9edf-d696953379c8 | -3.93175 | -48.35024 | 2024-11-02 05:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 941c4b0e-f7c9-37ff-85ad-bd3b4fd5f769 | -3.90713 | -48.92805 | 2024-11-02 05:48:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 424fbee6-752d-359e-83f1-52706cd110be | -3.89482 | -50.97689 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73f72aee-5417-3c7d-8854-11cff85d9a9d | -3.89343 | -50.98627 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 0e967b03-0fcc-352c-b3a9-15fc8a017897 | -3.88429 | -50.98501 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 175c61a3-c576-39cb-8596-6c5cd9f2abf8 | -3.88334 | -54.13348 | 2024-11-02 05:48:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9768e0eb-bc48-3961-9c93-aa61c6da9e4a | -3.82192 | -48.88433 | 2024-11-02 05:48:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ce436e63-30b2-34ea-a571-7311e6533274 | -3.81986 | -48.97121 | 2024-11-02 05:48:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1620deec-a6f2-3d90-a871-4dfea1ba1069 | -3.81191 | -51.16027 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 983cc91e-1c1f-3dc9-8e3c-b9d502467415 | -3.70802 | -52.41544 | 2024-11-02 05:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b1bcd64-3fd9-373b-b00f-06c4002c6971 | -3.7067 | -52.42424 | 2024-11-02 05:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ee51aa53-cfa0-3a19-b62a-e135af670530 | -3.70068 | -50.14903 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2d83e637-f05f-3dd0-a823-ab5fb0dc0da8 | -3.6904 | -51.17352 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d93511ce-189f-36ed-9647-4dedf80c08ed | -3.62386 | -53.96091 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ba32ac9a-fa09-38e9-b660-0084488f1878 | -3.62343 | -50.18333 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3b40e50b-1d00-317d-b874-e15282d1c289 | -3.59638 | -50.75342 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4df1f94-f253-3a5a-92e4-dfcaca763f2b | -3.55038 | -50.3116 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1dea1b3a-6f95-3a70-bcb8-4d9d6328d8af | -3.51429 | -51.67214 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7ad2c2c7-562a-385f-b2eb-edea0fc0eff5 | -3.50782 | -53.01047 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e3d5c5e6-9092-3d7f-a121-9ab58623025d | -3.50344 | -49.94328 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| da07096d-bdf1-3bd9-b834-469d81f04e41 | -3.49562 | -51.18022 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91ee6b10-47f1-3626-b4a8-ddd7f1a3f373 | -3.4745 | -50.37193 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5130784d-3c4e-35ed-879a-b71f277d2da4 | -3.46994 | -50.3645 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f2973995-1a15-3b57-887a-02c24b12b6cc | -3.46845 | -50.37447 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e13c4968-3c22-3b14-9565-e8b80b743d97 | -3.46306 | -50.282 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7df0844f-14d5-3885-b165-db2de14de59a | -3.46157 | -50.29203 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 70ca6663-87e4-33b7-ab79-857961f7b230 | -3.45607 | -47.67076 | 2024-11-02 05:48:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0692b042-612b-36f2-9c04-018f0c621aaf | -3.45261 | -50.15683 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 532fd5a9-2f2b-38e6-a74b-8885bc3923de | -3.44963 | -50.17715 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e28b33df-bf25-3709-bd26-02067fd8c48f | -3.43655 | -51.51653 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6112381a-8836-3b70-a504-aff271c1aeef | -3.41457 | -50.28531 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c737203a-7bb8-3d18-be39-c8afff239ac7 | -3.39474 | -45.3413 | 2024-11-02 05:48:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| fb52959c-9de4-319f-9833-5c2ee3f6442f | -3.39033 | -45.31245 | 2024-11-02 05:48:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 266c92b7-7ce2-33f1-905e-6a33f9d36ad2 | -3.387 | -45.33512 | 2024-11-02 05:48:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 576a8701-1e36-3026-a53b-33ae8958cefe | -3.38424 | -45.3167 | 2024-11-02 05:48:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 6c45943f-38b3-3641-8be2-f7612afa7d17 | -3.3811 | -45.3394 | 2024-11-02 05:48:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7ef5b40c-c448-34cc-97be-71fe96a10067 | -3.37302 | -50.26348 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 6e8c36a9-d0da-399c-9b49-e042f22f08b9 | -3.35961 | -50.15856 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 313de634-160e-3605-b7c4-f68ea1c0afdd | -3.34629 | -50.24936 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6181c396-df33-3e59-81b5-2c4cef68f495 | -3.34481 | -50.25943 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea047ebc-b637-34c0-92fc-0f580b1d7a9a | -3.31154 | -54.12753 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d4f2668-b33b-341c-a66e-d3e5e5a42218 | -3.31011 | -54.13698 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b4079d3e-4fe1-366f-b613-9da1ad883225 | -3.29951 | -51.19597 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5afec214-37a9-36ed-b89e-1ed634c7fe3d | -3.29825 | -50.01798 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e64edcc0-1f39-3f63-a3ec-5abe6b2d3ed5 | -3.2885 | -53.12018 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08a8f462-6914-37a1-b121-4797bc534596 | -3.28715 | -50.90386 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e196f24a-8904-39f8-b8cf-175c3fd73cb0 | -3.28575 | -50.91325 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 95e50706-2bc3-3f05-8825-5f18e28f220f | -3.28568 | -50.23392 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c94f4886-930b-32b6-93e0-6fa82408fcd9 | -3.27214 | -53.41076 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 12bb5f93-2198-3487-b2e4-451a028230b8 | -3.27085 | -50.33378 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 79714e1b-4de2-3f73-b992-ddf70b3a41ff | -3.27078 | -53.41978 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 95b3593c-a868-31ef-bed3-88381ac765a5 | -3.26938 | -50.34371 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 775a0784-030c-32e1-b1e3-f98b7933b525 | -3.26929 | -54.17305 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eea4cf46-8c89-3f3b-86b8-4278089aeac3 | -3.26455 | -53.40041 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d4bc73fc-0e56-3429-b3de-4421d437a384 | -3.26319 | -53.40946 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| cb17a4dc-be6d-37f3-8f28-e5e7d3e17a4d | -3.26183 | -53.41849 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 22a081b4-cc07-3fa1-a403-d4ba280cdccc | -3.26149 | -50.33242 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 74aa1b1a-5c0f-3163-9a2f-84673d8009be | -3.26002 | -50.34236 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 08659efd-e39b-32ef-8bb4-9793882c1304 | -3.2557 | -50.04335 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b33a7ee3-2ff6-3760-a075-3b4937baabff | -3.25482 | -53.3437 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 586326d3-110c-37ae-be6d-86bc695fc07d | -3.25424 | -53.40813 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 3832c404-01e5-3315-b920-df2a3093ee01 | -3.25288 | -53.41718 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e8c759b1-ea9a-3e2d-8020-133a0324741a | -3.25083 | -53.06261 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ce26ed7d-0682-30f4-ae8d-301d04fbee70 | -3.2495 | -53.0715 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9c3d7b09-2c71-3c69-b583-a9b516ba4b9c | -3.24619 | -50.042 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4ee7f8ae-4fe3-3533-a800-78c416201b33 | -3.2453 | -53.40681 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| e2e2b1cf-df30-3b39-a10e-e7774a755fa1 | -3.2418 | -53.36944 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e4a1c6b6-6423-3035-9c99-bde371266da7 | -3.23772 | -53.39646 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f43c7af5-54f7-38e4-a8b3-f57a7caaa84d | -3.23634 | -53.40553 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| dd78610d-64fa-3cf6-bf21-caeadb54ce57 | -3.23423 | -53.35908 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7715f94a-f5f8-3339-8bb9-5654282d6d36 | -3.23286 | -53.3681 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 4b489c08-6ab0-3a62-8325-fb3076a7f5b0 | -3.22877 | -53.39516 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 475e0dd7-4d61-378e-bb1b-9108ec8f427d | -3.22739 | -53.40423 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5326150e-4482-39e9-9c61-14c4a6516772 | -3.22564 | -44.36351 | 2024-11-02 05:48:00 | AQUA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 206fc9ee-3a9a-3203-a469-405d9f2cb127 | -3.22538 | -44.37076 | 2024-11-02 05:48:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 969fca3e-b5b8-3cd2-8285-bd12b0760997 | -3.21982 | -53.39388 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2945ce41-a080-3d13-b12c-e0b81dd528fe | -3.21845 | -53.40289 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e1d15d82-bfbf-3b45-b1cc-86d23e402389 | -3.21709 | -53.41188 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README98.md)
