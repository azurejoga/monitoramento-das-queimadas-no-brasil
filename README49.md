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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5298df36-cde8-35e6-96b6-e1d9a24d7c39 | -3.09893 | -50.36633 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b47656c-a8de-343e-abd5-2a061a3dbe1e | -3.29416 | -54.1305 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26ac6714-9334-32ef-b3fc-d5126a97ca13 | -3.59544 | -49.99818 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01ae397b-b52d-3cc3-b2f6-15b260275beb | -3.09629 | -54.04029 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22c33afd-e971-3c02-8c4a-6835a0e568e1 | -1.37324 | -55.8793 | 2024-11-30 04:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba1ff442-8a22-313e-9141-21434ecd477a | -4.95857 | -43.54816 | 2024-11-30 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2cb19bc-4c31-30fc-a8f2-9a7d48dd15f5 | -2.57288 | -51.83962 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dcc5ea72-161a-37e7-b831-7a6bd9836a6a | -1.51447 | -52.0288 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79f23c84-dc94-31bc-893c-43ea2fa3fd91 | -2.10596 | -48.21048 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dbcc1a1-03be-3250-b6ec-233da480def6 | -1.57727 | -52.01089 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97171f0f-97ca-3980-8259-cbebd0e8fece | -2.20386 | -48.34562 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad0472a6-6e1b-3216-b951-172d5ea3b931 | -2.27699 | -51.23922 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faea14f3-b71f-3a11-a921-723c8194b14c | -3.93741 | -46.70759 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 255bf40f-ae67-33cc-841b-b453fdbdf555 | -2.29478 | -48.50452 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0384d705-6761-3140-8922-da016b2c5cc8 | -2.72824 | -46.27336 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea4446b-0b4a-3a46-9722-ba969423e922 | -2.14279 | -54.88463 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35ed0011-dc44-3e92-9618-ab2af47fe463 | -4.20113 | -50.68487 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c90baf60-f851-39cf-a58f-f29a479c13fd | -3.14118 | -53.71726 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a8ce2c6-ab16-3636-9547-1ad0ad8e7cca | -2.42093 | -50.34941 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5ab6581-0fd3-3704-82e3-57bee7519c17 | -1.70143 | -52.44075 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6b1bff82-b7fd-315b-85c7-de66aad43800 | -2.95534 | -48.58661 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f059489-c6dd-3647-abde-e860af215c2f | -4.01947 | -46.99975 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab5d6da9-5bc6-386d-9b5a-7f342aadf68a | -1.58084 | -52.27318 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8d9d59e-2cdf-37d7-96d2-b3ded2c68f39 | -2.96242 | -48.0386 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f9a75ac-236d-304d-a5ed-236932c6fc62 | -1.49921 | -54.95871 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ee6a459-46ac-3937-8313-5ac49acffc86 | -1.4495 | -47.70779 | 2024-11-30 04:40:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9635765e-ca51-3703-8f19-549aa5ef7974 | -3.06438 | -43.02567 | 2024-11-30 04:40:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d34a6ed-1506-3446-a731-b1937ddb8a3d | -3.05157 | -49.51807 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d08cd7c-44bf-3ace-84d8-b227d07d6d30 | -3.48967 | -54.03136 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bfd4072-23b5-380e-98ed-2e3de4ab4264 | -3.86442 | -50.54053 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a5a34f5-e6fc-343c-92cc-4ab1585b2930 | -3.30082 | -50.37909 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de0b12d6-1082-3584-bfed-ca6385045ff6 | -3.4837 | -53.81489 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 054a7dda-20da-3d5a-ab2c-4d57d397a0d7 | -2.6053 | -46.55123 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7c1d31a-2b5b-3272-9bc0-54d054ff05f9 | -3.05976 | -51.0613 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caf5160a-1b62-31a0-80da-9932612813c8 | -0.96503 | -51.6569 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 187fb531-f27e-3f3d-ab16-94667b403d62 | -3.97976 | -46.73371 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f533f0-5899-35dd-8339-8fbc90599054 | -2.9515 | -48.58953 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4718d221-9e48-301d-8dc2-f89bcfda7365 | -1.28232 | -51.73695 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd2dd4f4-83bb-31f6-ae20-68738ebd635b | -2.72351 | -46.11535 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bae47c17-4c54-3209-bc79-baa4ed1badb0 | -3.2866 | -50.62386 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b83c64f0-baec-3cc4-8b71-97f92b98281d | -1.63719 | -53.8706 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 379eb4c0-c774-3364-807f-61564f3fa4a7 | -3.93857 | -46.72343 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 096592b4-4809-3116-b533-6b38fbc678e6 | -3.201 | -46.59558 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da1c5ada-df76-3bfd-85aa-2f1157121c13 | -2.54968 | -47.98137 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a32be59-e603-3b10-87b3-5b11af7f9987 | -3.32989 | -50.21604 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40f13cc6-0c4e-3e33-9881-933eb0eac100 | -6.39013 | -46.0004 | 2024-11-30 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c29d6952-56d4-3ac2-83c0-5b6ceb10c68f | -2.91777 | -53.07162 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea2402b9-3a98-38f0-989f-5f277e4f8d28 | -4.91893 | -44.83467 | 2024-11-30 04:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09b52edb-03f7-33e6-af40-1b6612a967d7 | -3.08213 | -50.25412 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2793fd9d-de81-3a22-ab9f-039c3a999bec | -4.576 | -45.64702 | 2024-11-30 04:40:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| febd0294-ed21-3b57-80d4-28d2f06029b4 | -1.28736 | -48.26977 | 2024-11-30 04:40:00 | NOAA-21 | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3adf64ad-7eb0-3f0c-8dbf-845e7ab8f238 | -3.29785 | -43.5379 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5144e0d-d853-396e-ac99-54a059e1efbc | -2.45487 | -48.87374 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f8918eb-c019-3451-8582-93a50d613945 | -3.09601 | -51.4059 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05ad2cee-f75c-3847-864c-6ce03ef7a2cf | -2.47106 | -50.38303 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29796cc5-b6fa-31ea-a60a-4a841b6ed2dd | -3.38903 | -50.33491 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4546362d-a984-3188-af19-25f379a42f43 | -3.25608 | -53.63179 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8367177f-0d0d-36d7-b145-0b190d7448b2 | -1.74024 | -53.74847 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72aa99ec-f79e-3f5c-b45d-44df9d14188a | -4.0915 | -49.74094 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1438a849-7ed9-3eab-8d2f-935c95fda15e | -4.95278 | -47.80282 | 2024-11-30 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a572b0f-9558-3ae6-bfa9-3d26aef07301 | -1.24222 | -53.35297 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40d05ff4-ff85-3263-a215-3634dbc2e10d | -2.58638 | -46.20869 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1e82e43-b894-3a2e-bfa7-f07441bb6717 | -2.96168 | -53.88797 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae7b7a52-3372-3c88-96cf-7b9406a712f5 | -4.17076 | -48.62416 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42ff62a8-90ee-340d-8d75-b0f2d78e939e | -3.27852 | -50.19358 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbf0c117-f529-3065-b03d-20e4e942d455 | -3.41423 | -50.32783 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 361a990b-bd39-330b-a92b-e2894085ab28 | -1.9533 | -48.68652 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04291252-a76b-3447-bbc8-bb052ea9d3e7 | -3.51666 | -50.25998 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f555ad29-7a60-317b-92ec-42e5ee91d6d2 | -1.12319 | -54.06855 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e11bb0db-9d60-30dc-86e3-0b7406338668 | -4.33817 | -50.76937 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 776f62ac-7e52-3561-8617-d50f16178c1f | -1.2839 | -51.73589 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 214f767d-7983-3f6e-be1f-3dc5b3677b12 | -3.57422 | -53.75301 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01c2241d-62c7-35b1-9e31-7c56f393174d | -2.04299 | -54.69324 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf02c267-a31c-3a0b-a3e4-5fbe1c73efa4 | -5.74847 | -46.18692 | 2024-11-30 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5359de32-b482-3280-b68f-5081eab85cda | -1.7464 | -47.35406 | 2024-11-30 04:40:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16ce272d-946b-3683-901f-4e6da91b6c1b | -2.20323 | -48.32791 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c86004-31c3-3782-a1ca-7278ea935802 | -2.35968 | -55.87447 | 2024-11-30 04:40:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c389f67a-3894-3576-ac1c-7fe795bd54b1 | -3.96667 | -48.09661 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a4086b0-5a59-38f7-8fe8-f87206e4d6d3 | -1.36281 | -54.65841 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 769e3798-cce0-3786-8f1b-6099e2c63951 | -1.99007 | -53.29775 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 324a40bb-b02d-3ebe-b561-89dfc6cf9707 | -1.20233 | -53.87638 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ace6893-2460-3b22-b05c-13328a811e08 | -3.59873 | -49.97717 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3c42856-6381-354c-b9eb-1b4af666da19 | -3.60872 | -49.97872 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c210976f-2a48-3284-a200-183486d5e73b | -3.27238 | -53.42749 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca12cfb2-d72c-36ef-88aa-8b97032bcc04 | -1.26454 | -51.59033 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01318a83-f001-31c1-a1a4-de4d9830c4c7 | -1.70517 | -52.44132 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c25d640-0220-37e6-a6f4-a16bd5e2e1c0 | -2.74266 | -47.98647 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 474c76e5-6308-302d-9639-2435fb0ac22b | -3.61398 | -49.85806 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92e2c374-6938-359c-8170-13308e288783 | -3.59375 | -50.37368 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fec34aa-03ba-3f1e-89b7-89a8974007be | -2.11617 | -50.343 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 889a5e11-2f84-3a8a-933f-73ad3585de15 | -2.80709 | -53.0541 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 92cef4ee-0ac5-33b4-8160-e59c79b7802e | -3.70073 | -51.79762 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d62cdc5f-efb0-3c1d-ade8-3fb72e8612b0 | -2.86703 | -48.10539 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 942f96c0-9386-30c0-a1ac-c81a2f340d30 | -1.89154 | -48.64892 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6618948d-1de6-30c2-9be7-a3e1559f13ee | -3.20454 | -50.21132 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ecbb8dc-7300-3223-b875-dc5ccd465d9b | -5.52619 | -45.40844 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e1f88ce-243c-37d8-ba25-2bbe90b08699 | -2.27494 | -46.44005 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97b22e13-dd83-3555-8627-90b07b2b1d6a | -2.55736 | -46.56337 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87204450-7a91-3e70-9d8f-085c1864eade | -0.25266 | -53.76285 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1820ab09-64a4-32f1-a651-7815a5bf8d6a | -2.66992 | -53.04224 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
