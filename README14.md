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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0632959c-6e85-3f46-86cd-e08a0eafe56a | -2.80225 | -51.90256 | 2024-12-02 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f94a8f2-3216-38f4-b08a-3bda084fc6b9 | -1.39449 | -53.55487 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7af90bcc-9c67-3d69-8534-2a137cf7059e | -2.80094 | -54.05694 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4e4ee739-ba6e-370e-bc95-6b82707ba56a | -3.49337 | -53.80254 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 67fa780e-2a3b-360d-a3e4-e193b17d02ed | -3.29445 | -53.84018 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 59a69ab0-2d08-3d35-bcdf-5ac7a63de5d8 | -2.82111 | -54.07207 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c1662da5-6de4-3173-95b1-6ab195b396a4 | -3.106 | -53.27808 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 865c96e7-c0f3-379d-a0cd-415befffc770 | -3.09339 | -53.25266 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 02c7f55f-db0d-3de7-a611-de9c177f628f | -2.7856 | -55.34805 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2cd0e9bf-b43f-3f8c-b658-19b9d9eb890b | -3.28894 | -50.43257 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9e889073-ea66-302e-ae7d-5f777dc67487 | -2.69133 | -54.13856 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53e21007-2e28-3f90-974c-e0428d1f17b1 | -2.35847 | -53.86267 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5c7a34e9-17c7-3cd1-bc7f-034d87e0eeea | -0.98431 | -47.82233 | 2024-12-02 01:13:00 | TERRA_M-M | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 7d94bf7d-3462-3004-8a0e-d5cd235520f7 | -2.84127 | -54.08721 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bf2ef2e8-433c-3b08-9c6e-99de2e63ff1b | -3.3398 | -51.52491 | 2024-12-02 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 80798ed5-2fea-37c2-9640-7b844771412f | -3.26038 | -54.11491 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 14243758-57fd-3b0d-b8f3-e75afbd7d203 | -2.7685 | -54.03185 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 93220295-92d4-3cfb-b72e-cd49aeac23a0 | -3.43259 | -53.8984 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b36ca450-3b5e-38f7-a2ba-e8d564af0bf0 | -1.43458 | -55.43031 | 2024-12-02 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1a213c3e-2ac7-3cd4-9558-5d5ebf4afd08 | -1.72782 | -52.6423 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8cc8154a-3358-3d7a-b092-b586b236b37d | -1.7005 | -52.64618 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| af739e79-1ddc-3b25-bc13-8ab06eb3299c | -2.81403 | -53.95626 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f89ea03a-9617-3106-9b7f-e94a79696d89 | -2.62903 | -54.21032 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 69d033d7-f5d6-3d05-a669-ef5966051f85 | -2.27723 | -53.60416 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e53c469-223b-348c-af22-7c0aa6b73644 | -3.26745 | -53.64626 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| f381ecad-867b-3ca7-89c2-30637c7656cc | -2.56269 | -53.40979 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 52d4a162-85ee-31f7-81ff-8f1c7ef5d050 | -3.29322 | -53.83136 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b705f193-eaa9-390f-bb0d-8e39a11d58e1 | -1.44234 | -55.41982 | 2024-12-02 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 35d70d4d-dcb8-3a59-8975-8ecc366812a0 | -0.97101 | -53.69071 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b30f5c2-29e3-38ec-9c52-ea7dcfe4b81f | -3.29057 | -50.44418 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0e21b681-20d6-3c56-b39f-6efa0ae55b37 | -1.62648 | -53.89796 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| eebdb76c-305d-3ef4-9025-25949571ff43 | -2.9975 | -51.3306 | 2024-12-02 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 15ead958-e67e-300c-8190-bde1b693afe6 | -2.42486 | -53.93682 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 70efaa38-68e6-3dfe-ac17-e2904c1ca9f2 | -2.56431 | -54.34295 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 87432baa-10f8-3b7e-8b0e-b92d88fc85c1 | -3.01265 | -54.05987 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1eb25ff-4dde-3d50-af4c-27b3973bd7c5 | -3.25566 | -53.28994 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11a4c8f8-e2da-3289-88a7-abdf4ca9628a | -2.90234 | -51.58138 | 2024-12-02 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| aecac847-fa4f-3b12-81bf-b05a8981222a | -3.24351 | -53.92829 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94c71f71-2586-3e86-bfb4-f75c3c3c1f5f | -0.98137 | -47.80235 | 2024-12-02 01:13:00 | TERRA_M-M | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 580407a9-c146-3cf9-b164-8ba6e2d0e663 | -1.34811 | -51.38485 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6457228d-bbb3-3865-8979-3f4365a4868e | -2.68728 | -51.8749 | 2024-12-02 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9c31425-e035-3f76-8564-d9b4e1f7e229 | -3.02546 | -54.02209 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b624c317-c0fb-3a7b-a034-404d5d431199 | -2.97805 | -53.87601 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fbd74863-9189-3058-acae-e318c8c34483 | -1.17275 | -53.41633 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a0ab815-bd80-38c5-b3e2-65f399f2e49e | -2.85531 | -54.05826 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4bfb28ba-764f-3d39-8067-a913abe7c491 | -2.57034 | -53.39964 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c0927272-c4cc-3758-baa8-d2de6222fd2c | -3.26499 | -53.62863 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ce2f00d5-1e74-3d75-9d4c-2b7fae7556c3 | -1.3359 | -54.98759 | 2024-12-02 01:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| adf15504-f6ef-3ee2-989c-30d8ce803b52 | -2.87399 | -54.12757 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5bfe0ad-2031-3910-a668-22db4cf9e831 | -3.46927 | -53.50015 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ec98487-b093-3950-94b2-5a8fd8f2d732 | -1.82584 | -53.7343 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b7db4a7-85ad-3aa9-a8da-5c3f32b9259f | -2.85138 | -53.03489 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fca5f0c4-f34a-3885-9bf0-2b8963355e23 | -3.39232 | -51.14725 | 2024-12-02 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 82e8552e-8b31-3249-bfd8-db6a39eda1d3 | -2.98812 | -53.88357 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 84f55539-b9fb-3a79-ba4d-a262205ab022 | -1.39923 | -53.65394 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d70d44be-5192-39eb-ae85-67d059747c7b | -2.028 | -47.70372 | 2024-12-02 01:13:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 25208255-fb93-3fe6-b1d4-ceb786e885d1 | 1.60951 | -50.93447 | 2024-12-02 01:13:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 48e290f5-2665-338c-843a-b59dba493380 | -1.46784 | -53.41983 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0bfc543b-c21d-3bad-a307-7319dcc5aed3 | -2.97165 | -53.89488 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e7fd50bf-49f4-3d94-b0d3-1fd015764fa2 | -3.25114 | -53.91821 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 35f09d18-f5a6-3d71-8317-3c0db9cacc1c | -1.18839 | -53.86428 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ee0951a-e9dc-3541-9ffa-2f5c4e491cd4 | -3.36429 | -53.21423 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5b75d288-a8c6-317a-9828-d1b9dac5954f | -3.09326 | -54.0426 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5ddda592-44df-33e8-a529-277283255ddf | -2.56145 | -53.40091 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 218327ad-8355-31d4-aa66-b7e7b5601ba8 | -2.38042 | -48.62387 | 2024-12-02 01:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5cdad378-5ea4-3af3-b691-fb406f0cf0ac | -2.80735 | -54.03806 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 60ba2786-d68e-39af-be22-4540e8bd3638 | -3.42108 | -54.02284 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5ef9ead9-1d82-3950-88e8-2459c4e1d79b | -2.73309 | -54.03685 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de54345e-33a7-3ea0-b468-5d5521e3a137 | -2.86565 | -54.00288 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e0ffceb4-8b37-3b5f-a5a4-df4b14b7710d | -3.16038 | -51.11209 | 2024-12-02 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 56a938e0-397a-3426-a483-72a392a5d1d4 | -2.80858 | -54.04688 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4b790afb-a048-3591-b693-a24443151656 | -2.97927 | -53.88482 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 05e016d7-5a1d-3594-b500-27c2158dd92e | -2.83364 | -54.09728 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c7d45416-8818-3702-9e5f-a50deca09aa9 | -2.63187 | -53.37598 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7afc7991-842c-3d66-b346-c7b6fb00bd63 | -3.642 | -54.68003 | 2024-12-02 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d672ff11-5417-3c10-9105-98c265919ae8 | -1.46717 | -52.68818 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6dc74bac-84ac-38c0-bea4-21eccd869ef0 | 1.65864 | -50.77671 | 2024-12-02 01:13:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| aee40b9a-ba67-3c60-9de7-45b7dc2be012 | -1.43734 | -53.3968 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e12e124b-52c4-387a-a79e-9c7796f9f368 | -2.62938 | -53.3582 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b6b49463-2463-3fda-b1c0-33a29597ab0e | -3.09828 | -53.75428 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 36f0ff7d-936a-37d5-aa28-150c846ae7e3 | -2.55505 | -53.41992 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f46943e6-d41c-3e99-b670-25e82d66ab0a | -2.79872 | -53.12188 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 849d0ba7-48f1-38e4-a12c-289324262107 | -1.38258 | -55.18644 | 2024-12-02 01:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c8c5028e-5627-3c23-bb3d-fa3740e40943 | -3.33583 | -53.54025 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 27daf19f-70b7-351d-9129-7a21123fd341 | -2.55806 | -54.0379 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7cf4063f-7236-30cb-9c0c-b5d156898ff2 | -3.15222 | -51.12419 | 2024-12-02 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 00fea1e2-b5b9-347d-9544-6c2ca938e4b0 | -3.0282 | -51.54662 | 2024-12-02 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6eaa0643-66dc-3911-b438-494191132aab | -2.60226 | -54.35566 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa48c337-91de-3aeb-899e-1bdb0d66e972 | -3.74565 | -53.77268 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddcc74ab-2c96-39a1-be18-d16385d45b3c | -0.96518 | -51.65532 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7799ea0a-9384-3d13-a699-59775ddec9ee | -2.89666 | -51.57761 | 2024-12-02 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6c2af172-01ac-3e52-96a2-a2140e7ac9ff | -3.25237 | -53.92704 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| b6228e16-ffb6-3e39-abd0-05896ed64dbe | -3.4995 | -53.84663 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 15d9b13d-bd70-3d81-a418-dc97d103f53c | -1.34358 | -54.97738 | 2024-12-02 01:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 21018193-5eba-3993-9d2e-409c0519ccee | -3.09337 | -53.71903 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 124453d7-bccf-3c93-9c8b-3961dbd2e081 | -2.53028 | -54.03284 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d196342a-a971-39f3-9fcf-c35a45375ea7 | -1.73823 | -52.78305 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c3788aa0-e10b-3e61-952d-a5d4ff029d29 | -2.53273 | -54.05047 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8f5fbec5-c902-3922-b623-4138e652c466 | -3.10335 | -54.05017 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8339b806-1fd6-3c6e-84ad-10d0e9352528 | -3.37193 | -53.20405 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README15.md)
