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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bf8ccdb-cd72-3744-8d93-a68083cd5bad | -16.47657 | -57.31059 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b0099b08-1045-38ff-8270-39ee21fcd9cc | -16.47599 | -57.31456 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4cca45ff-9823-38d8-bac6-d4e26ecf4a00 | -16.4754 | -57.31854 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ec26c873-1c6d-3674-8c66-7a9b759d6dc8 | -16.47424 | -57.3508 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a483a90e-7099-3ee2-9915-ce5c05d87c93 | -16.47366 | -57.35475 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 98a3ac46-5a3b-390f-858e-cf6450c540b5 | -16.47366 | -57.30607 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 139d3b6a-b7fa-31be-9928-86e285a32e86 | -16.47308 | -57.35871 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 969590e6-564c-3bab-afce-f98072ed1a1a | -16.47308 | -57.31005 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7420d19e-5eb7-302b-98f5-0dda3a4bfc4e | -16.4725 | -57.31401 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fd9f005c-98e0-3d2c-9611-b76235a9f6c2 | -16.47192 | -57.31799 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1e061942-b451-3431-822a-09ec7772573e | -16.47134 | -57.32196 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2f371fab-2a9f-3fe0-a213-41bc88bb03e2 | -16.47018 | -57.35421 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 228ede79-193f-3bea-93e0-f7c261198544 | -16.47018 | -57.30553 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5b946a88-cd66-3b1c-8152-0070883c163c | -16.46959 | -57.30949 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b6b2fffb-6716-3751-8ad9-46ed7bcf24e8 | -16.46902 | -57.31347 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 17e789e5-ffad-3671-85ef-2bd716c57434 | -16.46844 | -57.39034 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 292f23b4-83e6-3ddb-8248-675c8c6b2a3d | -16.46844 | -57.31744 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 775895b5-79fb-392f-a8f7-112cbb5ad0b3 | -16.46785 | -57.32141 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 72ac27c7-6df7-396f-8820-26f5406950e4 | -16.46727 | -57.42242 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f6c326f5-45b7-3cfa-87a3-d995cd98974c | -16.4667 | -57.35365 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| afe944f6-26e1-324a-96e7-cf73263de13a | -16.46669 | -57.42636 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 49e16f44-9880-3563-a7cd-f395ca0b85d0 | -16.46612 | -57.3576 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| cdf04f07-ff83-3048-b48f-2067a45fc21c | -16.46611 | -57.30895 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 55e531b0-ac7d-34f8-a498-6aee79484614 | -16.46554 | -57.38583 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dbc9a504-51bc-3909-8c7e-5557070302a7 | -16.46554 | -57.36157 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0b6f6a39-55d1-39e8-a772-5771e0ccf0b8 | -16.46553 | -57.31292 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c91a2879-f50e-3f11-861f-f07505baed19 | -16.46495 | -57.3169 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6a1217c1-613b-3c82-a1f7-d0fd818817cc | -16.46437 | -57.32087 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 54d5b751-3332-39e5-be45-86c4dad55065 | -16.4638 | -57.42188 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| dcc12d55-1a78-3413-a4b4-3a2a28268215 | -16.46379 | -57.32484 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e82cbe59-ca33-33e0-8fd7-148718028393 | -16.46322 | -57.42582 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fb72eec2-9d53-3946-a768-806aa2ba5bae | -16.46322 | -57.3531 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| bd3e44d5-2ebf-3689-870b-61a16ba77735 | -16.46264 | -57.42977 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5b691e8d-4795-3d87-bcf5-ec1fc873cd2b | -16.46264 | -57.35706 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| cebc6b48-a0fd-3303-8ded-59cf4de096a2 | -16.46206 | -57.36102 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2536e974-8a75-36ec-8523-9e32a9557001 | -16.46148 | -57.36498 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4b96c468-9d6a-3be6-a063-c02ac19fe966 | -16.4609 | -57.36894 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 629e9ca8-7a2b-3987-bfd0-51476fbf24c4 | -16.46088 | -57.32032 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9d18b100-6ad6-37ea-9e52-25877bb438a7 | -16.46032 | -57.37289 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 27fc03fb-e80c-3731-9d55-8f64b78b4b36 | -16.46032 | -57.3486 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 535c0ebf-c56c-3452-9b9d-cd181df4fca7 | -16.4603 | -57.32429 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bd3cad60-c86e-3918-8132-9ba77db2edd3 | -16.45975 | -57.42527 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1259bf7a-aeaf-3e16-ab90-1dcfffaf5c3a | -16.45917 | -57.42922 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| faaf1a47-48d7-39c1-a06b-8c1c9735b125 | -15.79964 | -57.34421 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b4195b8-f0c7-328b-862d-e749cb701334 | -15.79905 | -57.34832 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a22479a3-9b90-3928-b0e2-090e014d3a53 | -15.79845 | -57.35236 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9e574cb-6954-3609-9ec9-eeb0296530ae | -15.79787 | -57.3563 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e162ab6f-89f3-3a0d-9365-c64a8bc4ff9d | -15.79731 | -57.36013 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a37c8d6e-579f-33f9-a60f-88dd11bae2c1 | -15.79566 | -57.37136 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba93b52f-d794-398c-8f81-9d07b83ad00b | -15.79511 | -57.37508 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a9198a7-f363-3078-ab80-6175c28f14a1 | -15.7509 | -57.42394 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 673d216f-5356-358e-9f2d-b7ea77ea5e0c | -15.75032 | -57.42781 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb409248-2a41-38ff-8c46-0efa961f3c49 | -15.74918 | -57.42324 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 272dfc87-b2b0-30fd-bb62-993fdd5421a4 | -15.74861 | -57.42711 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c55abd5-cac2-34ae-bfc6-25e72c7a3237 | -15.74745 | -57.42339 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ead3a89-973a-3a89-b9a6-7d8160945d34 | -15.74687 | -57.42726 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 879c1431-a67f-3a40-b35b-a46495fafb42 | -15.744 | -57.42286 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4f8254b-e3c7-302d-8737-fce726e4f447 | -15.74342 | -57.42672 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d2152bf-7af7-35e8-b62c-e5cb76af04db | -15.68822 | -57.44183 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 854b6cc1-a5fa-3d31-a556-dcbe98afef90 | -15.68592 | -57.43355 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64bef180-0a79-381e-a86e-db49d85c60c3 | -15.68535 | -57.43742 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27e6b235-6e9b-3fe7-ac38-973bdc6dc52a | -15.68478 | -57.44128 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe282d07-84f5-306a-9a7f-b7e36ba8bc1f | -15.68421 | -57.44514 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c234bce6-3fa9-3d2f-8da8-511690ae435f | -15.68247 | -57.43301 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e3b7063-c3f3-357f-84e8-6b659e93da9c | -15.6819 | -57.43686 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c7087f3-4da4-3e55-96c2-c45818dd3178 | -15.68133 | -57.44072 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 434f47ab-0371-364c-9411-bbebbeeb1e2d | -15.68076 | -57.44458 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5dec3ce0-7089-3ea0-967c-db58f9ad92aa | -15.68019 | -57.44843 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9da32c25-705a-3942-b1b8-009ca7308395 | -15.67789 | -57.44017 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e763336d-16d4-3f32-8301-29d909931d70 | -15.67732 | -57.44403 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4040cff5-0fd0-37b4-a8c5-6b394653642c | -15.67675 | -57.44788 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 428bfb2d-b721-3947-8971-da6c1af2b0b7 | -15.67557 | -57.43191 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c57c810-7370-3f2c-a53d-6f1e69931ff3 | -15.67269 | -57.42751 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ce6969e-282b-34ec-b9e7-bed2e9fde1a5 | -15.67212 | -57.43137 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bbc7403-28b1-375c-a3b5-8f0e322ea004 | -15.67156 | -57.43522 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 500c3b42-4f2a-3ef2-9d38-b99fdcc84d17 | -15.66811 | -57.43467 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83521355-6e23-3e56-b4b0-5f1196f3194c | -15.66003 | -57.41761 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ccdfe259-affa-3b5f-af87-9bff491c80f8 | -15.65947 | -57.42146 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2c168b78-6ebc-31f1-bc3b-6305acfe7a89 | -15.65489 | -57.42864 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a3c38d1-1f2d-38ac-a813-94e98d2e8652 | -15.65432 | -57.43249 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50487352-a941-31fd-a51f-0be776fadc7c | -15.65149 | -57.45178 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdb411a6-c1a3-3760-880f-7f8259cc3a71 | -15.65144 | -57.42809 | 2024-10-02 05:12:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27003d7f-fb5d-3f8a-994d-47df0bb1e41a | -16.09599 | -57.53096 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ccb59574-c453-3a4d-922e-d03813e563b8 | -16.0931 | -57.52667 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d58a26c7-26e5-387e-a939-de2d627f7ede | -16.09254 | -57.53044 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d98dbfe-ba1e-389c-910d-b17bab44f2bb | -15.92397 | -57.45019 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f08f0d57-e2ae-39e0-9d6b-c9e1818e1e25 | -15.92109 | -57.4458 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4048061e-fb3a-3543-8ace-633e0399e3df | -15.92052 | -57.44962 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49bee6d6-a31f-3f5a-b76f-15a32fd7dbcb | -15.91996 | -57.45341 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9cfb00f-d06f-3119-89be-ed9613c2c466 | -15.91707 | -57.44904 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af0e2a66-6ce0-37b0-8054-e664f8235303 | -15.91651 | -57.45283 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44b0eb9e-df10-3003-be2e-6bf1506047b0 | -15.91363 | -57.44844 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce0e1598-897a-3be9-9b05-dcdd7f8747c5 | -15.90929 | -57.16258 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a8ef51f-ecf4-3b38-a6eb-6371b2df52a6 | -15.90812 | -57.17076 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41bb743f-3831-3114-82a8-e9a08d70d481 | -15.90752 | -57.17492 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 420dbec8-e9d9-38da-8f5c-54cc4dcb3754 | -15.9058 | -57.16206 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af46a94f-e003-32b8-97a7-c1cbb4263f38 | -15.90521 | -57.16618 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b3471c83-3c05-3b1b-9623-dd8e3016d933 | -15.90461 | -57.17033 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b977c43-087c-392f-9813-a230d80cf00b | -15.90402 | -57.17448 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81a800a4-3818-3691-a154-b9b7cbf022f7 | -15.90111 | -57.16988 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README148.md)
