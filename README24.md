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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0a70517-df82-343d-a212-19664effe6a7 | -8.32461 | -55.03432 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a88cf054-1432-37f4-9a24-54fe95f12103 | -2.99098 | -52.82038 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b0be214-dfe1-3176-bc39-a81ad5e3e35c | -1.99071 | -53.14066 | 2025-11-06 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f82b2eac-a818-3a2c-9f25-650edd770fe5 | -3.44827 | -51.47139 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa96fd48-2c4f-36a5-bdda-682949b75ae5 | -3.7726 | -51.71232 | 2025-11-06 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeadf182-5863-3c03-bfc4-a866b39c3446 | -4.59581 | -43.32712 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2c368f11-4d48-3baa-87b8-a369694d8a9d | -3.11742 | -51.20297 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 843ba32b-c073-3984-95ba-32a544f9b036 | -3.70473 | -50.8802 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47fde6a7-6d61-3c09-b32d-c2ccd9952d6b | -1.73388 | -55.24707 | 2025-11-06 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 878a93e7-4f93-3ad0-ba4e-a4e22ca27183 | -3.12158 | -51.20364 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3d78415-a6f2-3d4b-ba92-77683f20385a | -4.47661 | -50.90509 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91e1bde0-0bd7-37ee-8ce7-b5e4a98ae698 | -4.59482 | -43.3341 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e823143d-1565-38a0-abb2-2881e38911c7 | -3.87349 | -48.33413 | 2025-11-06 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37cb9594-2854-3d7b-b018-e6624d5f3148 | -3.44727 | -51.59023 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed1c6101-6eb2-3773-bd9d-3cc66c954fa5 | -4.7164 | -50.82881 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11dac6ba-32e9-396b-9112-6e2ad31ac09d | -3.92445 | -47.69613 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3d3deb0c-4d12-3754-a7c1-b424976104b5 | -4.50084 | -50.7456 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc3285ab-25bb-33e5-a559-9c7fc236474d | -3.89834 | -55.87752 | 2025-11-06 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca14e163-d31f-3e0b-a175-015f3b87517f | -3.85233 | -49.90478 | 2025-11-06 05:14:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 146f1e5d-5e9c-3496-9aa5-015f115a9b59 | -4.6477 | -50.93178 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d65fde-8c3b-3407-b1fc-873b673ccdf9 | -2.88099 | -52.61023 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbcba4dc-a14a-32f5-b149-326bd227102b | -4.58773 | -43.33284 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 98bbcd5d-0a40-344c-afc4-d7ca177456f7 | -5.53112 | -46.50895 | 2025-11-06 05:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d2ca375-8eec-3f22-9742-928224039ba2 | -2.88028 | -52.61487 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a83750d-55ea-33a3-b609-a562c525eecb | -3.81307 | -53.4752 | 2025-11-06 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7579acd0-9cab-3357-9e8b-d6c81d0ba1c0 | -4.60097 | -43.34199 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3aa8b398-b2fc-31c6-b1b0-5c5a03994714 | -4.10755 | -48.01611 | 2025-11-06 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2241939-2b94-3ca3-a625-58218f46d77f | -2.88141 | -49.84253 | 2025-11-06 05:14:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de7942a-9601-3e2e-98b7-48795e9c6dce | -3.40595 | -50.83978 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7efecaf7-e80f-3536-bb9d-3cd0080d20ca | -3.04145 | -51.13399 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cedfcf83-b1fa-3d93-ae36-2a8c4be5c609 | -3.48269 | -43.65189 | 2025-11-06 05:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89e50d74-0bf5-39d3-861a-84801ce6637f | -3.92886 | -47.70352 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3877a6c-5b76-3300-a052-82fe781583d5 | -4.46204 | -43.22464 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90e25e5a-edc8-35be-b9a6-d4f540546095 | -6.12297 | -57.71086 | 2025-11-06 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71894108-7076-3310-8e05-4f6527edd5dc | -4.58062 | -43.33171 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 892f16b2-ad65-39ed-b154-9e30341a01ab | -4.64336 | -50.93109 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f9dd7ca-ef8b-3dd4-96a3-c11272935b3f | -3.77858 | -51.67278 | 2025-11-06 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c606ecc0-f285-3d86-9d73-cb865ed862bb | -2.26623 | -53.55464 | 2025-11-06 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b835ca4-d4d6-392c-ac2a-1afd535896d6 | -3.51936 | -51.6591 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3256a45f-038b-3c35-82f7-8541e71ec58c | -4.10707 | -48.01933 | 2025-11-06 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2d78774-1222-34fe-adc9-c45d8799901b | -8.06518 | -54.92007 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cdcc2cb8-9f24-36af-82d7-a774619f0e7a | -3.61912 | -43.54031 | 2025-11-06 05:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9034011c-ab7a-3eb6-98ec-afa30eb6bde8 | -3.77319 | -51.81769 | 2025-11-06 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28274082-f610-34c3-af43-3c866a4ede5d | -3.47488 | -43.65721 | 2025-11-06 05:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 855cba4e-fc61-3b6b-bf64-ed2c5b146b62 | -3.08903 | -57.37762 | 2025-11-06 05:14:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8025895-6309-37bf-a9a0-0a7f0464fe31 | -3.49943 | -49.55739 | 2025-11-06 05:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 797b00a2-4967-3475-afc7-00e4c49cf1cf | -3.98199 | -47.29919 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d9cdd46-d5fe-3d20-9e8d-e490284bb6d5 | -3.86791 | -48.33631 | 2025-11-06 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 068169d4-553f-3dd6-a228-5467a4a1dc09 | -2.92992 | -51.30822 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8790054e-f55a-3246-82d8-1c24821260f8 | -3.12101 | -51.20741 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb36294e-4ac2-3014-af29-02c40e33a375 | -3.34177 | -49.9174 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0299b16f-ea23-3083-a0b7-e0025e7e0b30 | -5.19599 | -56.03845 | 2025-11-06 05:14:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aed2cfd-17e2-39ca-a513-50faf96d84e4 | -3.08769 | -51.20223 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab3a25f8-7b3d-3576-b656-476f53458c9f | -3.51577 | -56.88776 | 2025-11-06 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c6cff7a9-2195-359f-a8df-c0cad312e4b0 | -5.53171 | -46.5048 | 2025-11-06 05:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96854829-4f61-35cc-8424-028119e8f8c3 | -5.52576 | -46.50399 | 2025-11-06 05:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1abb0c5-c109-3b0c-ae75-28bddffe39e3 | -2.69463 | -51.89936 | 2025-11-06 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7ae89d5-2d89-3e1b-af2e-07a6807cc1f2 | -3.5912 | -46.05297 | 2025-11-06 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ede00475-3b29-3899-a34e-d3a564d7425a | -3.01844 | -51.19997 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd0190c4-fbcf-3116-ae78-625750464b4d | -2.88407 | -52.61548 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7706c34-0872-3b2b-bba4-6b0f1fb7b5e1 | -4.21973 | -55.69888 | 2025-11-06 05:14:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2eefc4d-f806-3ced-82f2-77af75ca9e48 | -3.50404 | -51.54698 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaa98d4b-2f56-38b6-a5c0-02d5e9803003 | -2.99029 | -52.82481 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f441c1d0-0e8b-3069-ba26-311c99a2215e | -3.41085 | -50.83647 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbcc5636-759e-39e9-a967-5b4d943d7bb6 | -3.9235 | -47.70269 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3d76c10-c45f-304e-a660-7907f6c83520 | -4.07304 | -54.10682 | 2025-11-06 05:14:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 850fdb04-1075-3d3d-923a-a4eb907477f1 | -2.82282 | -57.66662 | 2025-11-06 05:14:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ccd1dee-c566-3f41-beb7-cb68c7ef9e11 | -6.12242 | -57.71433 | 2025-11-06 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e9f7dd4-d66a-366b-9a12-40bb462b4a5e | -4.54154 | -46.44781 | 2025-11-06 05:14:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd817e36-2b4d-3a68-bcae-d7a0a2b856d3 | -2.98204 | -51.35395 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f410a4b0-5425-371d-ae04-984480b9f177 | -2.78663 | -50.31746 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29a9d7a7-c725-3843-a92d-6ffcd2f75156 | -3.47676 | -43.64427 | 2025-11-06 05:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 50c8321f-5529-35dc-ba42-fd05eee9ad18 | -4.36228 | -50.88905 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 327f82d9-ef64-335c-b6fe-5b3ac002b774 | -3.41818 | -52.67541 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4040ad0-d456-318e-8cda-e769160ecb64 | -4.10662 | -48.02241 | 2025-11-06 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 873121df-49a1-36d3-8143-f45eb8b76a05 | -2.98654 | -52.82425 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5bedc1f1-da29-36ff-bb4b-44fd9f456e51 | -3.45135 | -51.59086 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27305370-5142-3dbc-803f-b5179ed784ef | -2.79609 | -50.3145 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6674e751-bc13-3645-8d0a-84440242c2d3 | -3.82634 | -51.35632 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20e43194-61f8-3a3f-b8e5-4e356197f2f3 | -1.60247 | -59.96288 | 2025-11-06 05:14:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 391f8e2e-1c97-333f-a984-1c7a44670198 | -3.79624 | -51.38665 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6dd203b0-63bb-3414-9241-38cfb75b0aa3 | -3.84699 | -49.9089 | 2025-11-06 05:14:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db37100a-f119-384d-b270-c5160e825e2b | -4.69366 | -49.62966 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdf966e6-1550-37ba-b0bb-2261d1947064 | -3.98754 | -47.2998 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbd14d1d-fd4a-3fce-a01c-4a00e41ed055 | -3.77749 | -51.67997 | 2025-11-06 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e87931b-83c8-3dc2-b53a-6020a00a5454 | -2.92799 | -51.30888 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d57b2301-f675-3907-9598-565c56e8fefd | -6.52335 | -55.03881 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb31fb7f-0c73-3bd9-91a9-0381d4e03e62 | -4.45818 | -43.22893 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 384f21b3-9fa6-3cb0-bf39-6dba5c37a08c | -4.43107 | -50.60825 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c74b6c16-b725-3e22-9150-11fa21e3aeed | -6.21493 | -57.77242 | 2025-11-06 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 762757e2-50a0-3c3b-a4dc-6935e36825fd | -3.60703 | -43.52576 | 2025-11-06 05:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f968df5-296f-3202-9425-69979475390d | -3.25531 | -51.19965 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5466986-44c1-3ae0-9895-8f112a5679b5 | -4.18646 | -52.09631 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e5a009-a70d-3dac-b51f-9287d859a9ff | -3.61494 | -43.52026 | 2025-11-06 05:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 68070a4f-dea1-3a32-b76c-3c5417519829 | -2.98723 | -52.81981 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a4ed2b42-6a36-3e6a-a949-e2ee97eace99 | -3.61402 | -43.52658 | 2025-11-06 05:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cde12531-2469-3f8c-bfc5-c4b0d959ce2b | -4.46533 | -43.22998 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60cccf89-4a83-3ba6-92ab-be22f6119174 | -4.42786 | -50.60533 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c3eaf5-f79c-3c1c-9106-a17b3e285f27 | -3.0743 | -52.63069 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78cc3584-285b-3547-81ae-5ef31d3caffd | -3.10944 | -51.0299 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
