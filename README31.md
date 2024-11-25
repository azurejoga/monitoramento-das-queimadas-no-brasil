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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba58d356-8e58-3edb-854b-cc515a0931e2 | -0.32667 | -51.92048 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f2fffc6-de45-3a88-ab17-ce929594b72b | -1.23135 | -51.74011 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09ab9bfc-5da5-3d5f-b6a5-5cdd13fa8d37 | 1.83532 | -55.90734 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0955ecd1-18e9-3655-9ea5-8ea8f2994c6b | -0.81978 | -51.6041 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 920ef1d3-00fa-350d-953e-6162be17436d | -4.66077 | -49.45718 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8150b980-de5f-35bf-9078-1d325e98bfa3 | -1.24917 | -51.62642 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dad71f6-c2a8-38be-833f-6ea5f414690e | -3.81565 | -52.2243 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a087a1b2-d24f-3e27-987a-14152b7e78c9 | -1.45373 | -53.40529 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db931995-89b2-3b7c-8a8b-9fdf8eb63421 | -1.38638 | -52.32772 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3526f2a-e6f9-32e4-8972-7e6f883b024f | -4.24237 | -48.66721 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfcbf12d-3771-3572-a736-3fb4eef5c249 | -3.8486 | -52.15206 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fff42c7-1fa8-36a3-a12e-6f06c411d274 | -3.28502 | -53.83024 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b8770b5-9c62-39fc-958b-599b58ee0479 | -2.21615 | -46.38815 | 2024-11-25 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3b602b8-e293-3766-9efe-e635f42e8cda | -3.77805 | -51.81945 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9457a6ed-da24-32e6-9462-f690566bfb8a | -3.21238 | -53.84027 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af0b5839-cc7e-325e-8b77-82cc20e1d744 | -4.35281 | -45.78876 | 2024-11-25 04:55:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 389088b0-1dfc-3d57-8443-1a89e8ac3271 | -1.18164 | -53.92222 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abe8cb50-9d60-37de-b6e7-b316ddbdf87d | -2.96946 | -53.85567 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ce92afe-3208-3a78-92c5-8e7fa3d49085 | 0.3325 | -49.7226 | 2024-11-25 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9786ced4-28d4-3ac1-94e7-aeb86bb520e7 | -1.25938 | -51.75896 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c87d819c-6bbf-3b3d-a67e-67888f4df6e6 | -3.52502 | -53.81149 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 345b0c00-2c56-3b2e-869d-a1b738cef1d3 | -2.67511 | -51.83724 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ce6ad19-b3d8-385e-ae4d-581cc776a700 | -2.68622 | -46.2755 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00c97615-9e9c-30fc-8b48-bda8cdc32b69 | -2.99652 | -51.45768 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 922ac950-f01c-33ad-a29a-34cbec4fb5eb | -2.82728 | -54.11473 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fc2d5ed-e433-3e5a-8c73-641dcc93f432 | -1.63802 | -52.4019 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3831edc1-b7e9-313d-a65e-978efe97e735 | -4.24452 | -48.70678 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a0c1f08-8281-36d9-9b27-25d81a6d4cfa | -0.97288 | -51.71158 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbafb0cd-2a05-3ee4-878a-594fb1986363 | -1.06421 | -51.75455 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 865d9f39-13a4-3fd6-b6e2-d7f594c0becc | -1.36487 | -53.83989 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0906fb8f-d600-32ee-964e-56f73f06ddc7 | -4.0716 | -54.48582 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a0511d4-2a42-3479-86a9-9f86ae5b95bd | -3.9424 | -47.98568 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d84154a4-640f-3530-9fe0-09675c046a75 | -0.81361 | -51.59951 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6361d139-e3ca-3eb9-90db-b94a689eb243 | -1.12923 | -53.61392 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0849aaaa-7238-3864-95a1-b5dfa210cd3f | -3.2814 | -53.01295 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56b8c48f-d8e0-3e48-94e9-575ac280ba53 | -1.60572 | -55.12798 | 2024-11-25 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc869572-a654-31ab-8572-25a7998eed79 | -1.30206 | -51.7362 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8241bc8f-c58a-3218-8a58-3e8b77597a88 | 0.32284 | -51.07383 | 2024-11-25 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47e222de-963c-3159-a8e7-ec10d25423ab | -3.9955 | -54.17311 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cb1504c-e178-3b85-aacb-e83650f8d5d9 | -2.61331 | -54.25049 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 865b24ac-7bea-3d19-90a4-24f8c1ac21f1 | -2.82615 | -54.10023 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01d0b23c-ca39-3c87-84b2-ac18f852401c | -3.95574 | -52.22713 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d2269a0-a787-3f98-b9e6-6ff70c27f50d | -3.74312 | -51.83999 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ffae4f7-7f84-3ac5-a85c-df6037e62237 | -1.57786 | -53.81965 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a785f243-5da1-3965-8792-31e7f95e5432 | -0.92477 | -51.73309 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef29d60d-19c4-3f8b-a4e8-fef93630e320 | -0.36719 | -51.5525 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e0b4bbb-4c84-36a8-90ec-461274eedd07 | -3.16045 | -50.58355 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9df7df5e-3740-3609-a437-bf7db32112ef | -0.81136 | -51.59188 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd740796-bf28-3fe1-9000-a1b7ea940162 | -2.71255 | -46.2893 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 307ab214-b9c1-3373-ad64-746b00174444 | -3.24961 | -53.28026 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 210df700-b150-3c1c-9e0e-3d822c1f841b | -3.27874 | -48.75425 | 2024-11-25 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8882bbcf-e81b-3a6e-8c6c-fd9e113f7f97 | -2.76252 | -54.05456 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed4357fb-83ac-3f70-9400-a3c590303c1f | -2.82211 | -51.79358 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 785af97b-272b-36aa-b6fe-e732578b435d | -2.65029 | -51.77453 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d90c58f-fec8-3370-87c2-a18898a9550c | -3.51896 | -53.82827 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91ffef41-cc51-351e-8d08-cb03a1d4302a | -1.19558 | -51.77081 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff9fd157-c7e8-364d-8f51-52d9e9b98a32 | -2.84271 | -54.01704 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39be8a38-1ebc-3649-9099-d2e93c28a615 | -2.57692 | -54.06881 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e59cafc8-c1b5-3afe-8593-759626a65f34 | -0.62462 | -51.70842 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b86596d6-9e8c-39e8-ba33-cb47b3327c49 | -2.57243 | -53.96788 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d3af29b-0484-3388-bfe7-7d990a72b53d | -2.40548 | -53.84875 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e399217-0ac6-3083-aeb1-da85e971ba7b | -0.89566 | -51.72133 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66808090-28f7-3ea1-a6b4-5e2426122999 | -3.5325 | -54.49159 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92374784-c25e-30b5-a82e-f2b541c48208 | -3.51887 | -53.78571 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99cb2f6c-bc6c-3cca-ab4d-52cecf0aab80 | -1.21791 | -51.73802 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 921f28ca-55e4-34be-b0d8-5be1ec6741d0 | -1.31159 | -51.74131 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b5f195-e932-34a1-bf31-4f18ffd02652 | -1.75293 | -52.66495 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef08bd75-924d-3b4b-8604-85d800b0a899 | -2.02348 | -51.18705 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21ad33b4-f246-39a7-a57f-7c94b6ffc798 | -2.71613 | -46.26547 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f151a4bb-d7ad-3f37-bdb7-2b0717a0ede3 | -3.63897 | -51.45442 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ed064f2-cca3-3fd6-89e4-f1f8f2dfa868 | -2.19304 | -52.12667 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe1caea8-8da2-331a-a87c-2f9d7b1dd023 | -3.09346 | -51.32336 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 206ea301-0dc4-3f7b-a6d6-adeed06c6a48 | -4.13813 | -48.76017 | 2024-11-25 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ad5e480-52fa-3279-a2f8-15c65e7359ad | -1.1259 | -53.61341 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0c81bfd-8876-3947-93d9-99db8c461d7e | -3.79237 | -51.92969 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de28dfad-4f98-39af-9b6b-303bef20e8c7 | -1.12868 | -53.6174 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94b08a0e-40bf-3317-b9d8-43392f360920 | -2.17347 | -53.7736 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05de9468-ec4b-3b4b-844a-49f065ba0b3d | -0.28081 | -51.52119 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f64a8f61-f9cd-3f37-ba30-6210b9131edd | -2.68315 | -46.27193 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee0deb70-d6ea-3ba9-8a38-f2dbff61ec81 | -2.58354 | -53.96247 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de29e9b8-57bf-3fb9-9ec6-e8d8689ecdda | -2.77079 | -54.0237 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 137335d2-b318-318a-aeb2-175634901a61 | -3.57856 | -54.51677 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66e9bcab-fb85-39fb-bf9f-66c218a30adc | -1.61427 | -52.59681 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c42695ed-9982-33c1-a888-16738cc35a68 | -1.75679 | -52.66201 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54ec85ab-4051-30b6-a356-54729b53fc35 | -3.72674 | -51.1851 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00c177f4-c95e-3dc6-8dcd-72037a60250a | -3.26075 | -53.70604 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 077e63d3-7226-3537-ba34-54775dc97596 | -1.66877 | -46.05923 | 2024-11-25 04:55:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d56ef645-a064-3d54-99a9-3bfa70f8e260 | -2.60918 | -54.03798 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6da6102-060d-3950-81c9-74e8d04c1ac4 | -3.52497 | -53.79021 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 496131fd-1b74-30bd-8bfa-942f74028ead | -3.05195 | -52.75356 | 2024-11-25 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac078ccb-8db1-3fe1-abd9-77ecde5313c0 | -2.67924 | -53.05699 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0e56377-0892-35fa-9224-a08ace3db463 | -3.93911 | -48.15136 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f6c23b9-775d-37ce-adcf-fe216060de93 | -3.26775 | -54.11224 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f34856e-68a7-381c-8778-be53cd1a84e5 | -3.61486 | -51.47369 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 129e959c-241b-32b6-b390-411cc6bee1a0 | -3.97844 | -49.93498 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9bbdfaa1-3998-33f8-aac9-6ee6e63cacc9 | -0.94765 | -51.65326 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1792504-6cd3-38bd-a9c2-8fdf297d0593 | -1.98929 | -53.29094 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5081bbec-b6ed-306c-9638-6806b559199b | -3.53562 | -50.44287 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df82d379-b92c-3f3d-b144-63129c8cbbbe | -1.24635 | -51.62233 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b2ff354-fd41-3109-a215-a1992eb3e7bd | -1.05629 | -53.64813 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README32.md)
