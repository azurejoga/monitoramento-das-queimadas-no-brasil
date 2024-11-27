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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4396f3d9-798d-338f-ad8c-eff0aa8d04dd | -3.1876 | -48.4387 | 2024-11-27 05:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f2a55c3e-55df-3a79-9e99-b2c045fb1113 | -2.8347 | -54.1125 | 2024-11-27 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 420f0391-ad72-35b5-97fc-9cb05c6be431 | -3.0393 | -48.5082 | 2024-11-27 05:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c7858257-216d-30c3-a226-ebbf70db4d27 | -2.8346 | -54.1326 | 2024-11-27 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2f5b4d3b-d7c6-3219-90e8-f3413b24579c | -4.2299 | -50.8983 | 2024-11-27 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 13257454-4974-310f-97be-f4b7e870c58c | -2.9428 | -54.7904 | 2024-11-27 05:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 05d9ffbc-347a-3e66-a1bc-583f469fee98 | -3.1691 | -48.4394 | 2024-11-27 05:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 516af428-c628-3ac6-9d38-7ce82cb671eb | -4.2237 | -48.6557 | 2024-11-27 05:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| c0b29155-9363-3fc4-bd83-97fa9af683e6 | -3.9674 | -48.0851 | 2024-11-27 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d5297fd0-421d-3526-a0b2-646293ab0cf6 | -9.7374 | -36.3208 | 2024-11-27 05:10:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 116.4 |
| 7b42aaf3-11d5-3164-bc1b-1c41905efb93 | -4.2114 | -50.899 | 2024-11-27 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| f01183d5-3c14-3584-a3e2-9ab5995b17c4 | -22.9841 | -50.4019 | 2024-11-27 05:10:00 | GOES-16 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| 26be3757-e887-3516-b0db-4f302671905c | -4.23 | -50.8774 | 2024-11-27 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 91d46711-f302-3192-9cec-7db63be93d16 | -3.1876 | -48.4387 | 2024-11-27 05:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7b1dd61b-efc0-3d95-8f06-7d83adfb2b44 | -9.737 | -36.3477 | 2024-11-27 05:10:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 117.5 |
| 9fc29063-16db-3862-a947-3f059a30e088 | -3.1133 | -53.2583 | 2024-11-27 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 817fd02c-98a3-3be1-8327-4359ff3f4cc2 | -4.2115 | -50.8782 | 2024-11-27 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 71659b60-e10f-30b0-a7b7-02145e5bc8b4 | -2.8346 | -54.1326 | 2024-11-27 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 12f82ba8-b1e9-304a-9fb7-dd670f99d5b8 | -3.9674 | -48.0851 | 2024-11-27 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1b35b343-ca93-3be8-b2cb-892b82b37c9d | -3.0393 | -48.5082 | 2024-11-27 05:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d22945c1-4978-3eae-a59f-03fe70af6572 | -3.0948 | -53.2791 | 2024-11-27 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ac6a711a-09c7-30f8-aa3b-081f19e4b8fa | -4.2114 | -50.899 | 2024-11-27 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 58b14b76-1932-3567-87c5-01933e2999db | -2.8347 | -54.1125 | 2024-11-27 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8f39e102-6cd4-3583-9b8b-6933e58c049b | -3.0949 | -53.2588 | 2024-11-27 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 4696c33d-bab1-32ad-86eb-f170da547d22 | -4.23 | -50.8774 | 2024-11-27 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 534decfb-0d31-3912-882e-4fad71758871 | -3.0949 | -53.2385 | 2024-11-27 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9d1c331e-10cb-36a7-b8ba-41a1e1fd1cb7 | -3.1691 | -48.4394 | 2024-11-27 05:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 960b4aa8-843f-310e-8642-386645ebf557 | -3.1133 | -53.2381 | 2024-11-27 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 94b54d78-9622-304e-a61e-d08ab144fec4 | -4.2299 | -50.8983 | 2024-11-27 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| b80faafc-2286-32bd-967d-6699e5c3739c | -5.9975 | -45.3607 | 2024-11-27 05:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8c244c41-bd17-33af-a2ff-4b74a7f5ff8a | -2.8346 | -54.1326 | 2024-11-27 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 262597a3-b86f-33f6-9e89-82c6c9e63ee6 | -3.1691 | -48.4394 | 2024-11-27 05:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 91a1f7b2-587f-3c26-967a-851223c80068 | -3.0949 | -53.2588 | 2024-11-27 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 189.6 |
| dd816344-4509-35e1-a00f-c58be30b24c4 | -3.4975 | -53.8137 | 2024-11-27 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 547d9d7e-d465-33df-b2c7-a6c0c6cb7465 | -3.0949 | -53.2385 | 2024-11-27 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d601ff91-365d-32c4-8f3f-e042fbbf6203 | -3.9674 | -48.0851 | 2024-11-27 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9814396d-60b0-3ef8-bc68-d7e4ec883f72 | -5.9788 | -45.3621 | 2024-11-27 05:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6d0d93dc-a080-31a2-9447-ecb06f94311c | -2.8347 | -54.1125 | 2024-11-27 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d75b0bf4-65ab-332c-931a-05eadd24e5e3 | -3.1133 | -53.2583 | 2024-11-27 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| ac5c7fa1-6073-3fe5-8bf5-23f3d5e5325d | -3.1876 | -48.4387 | 2024-11-27 05:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b5f48df8-93ba-3ebe-ab28-0a9815959f04 | 4.38586 | -60.8268 | 2024-11-27 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 831759f5-b47f-3363-bd1a-25bd138d5a07 | 2.08128 | -50.63289 | 2024-11-27 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| efdc202c-9576-3561-96ff-c6e69cb156ec | 4.27013 | -60.65227 | 2024-11-27 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e327787e-3b8a-3a76-b2eb-06505a28bd3a | 4.37978 | -60.83121 | 2024-11-27 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c937ccd9-2a79-3d8c-825a-bf1580e68e78 | 4.38201 | -60.82385 | 2024-11-27 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc499ee-0345-3b3a-9e2e-3a9d370fcf04 | 2.07615 | -50.63456 | 2024-11-27 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a01b622-04c1-31ff-aa8e-b6bd47b5b296 | 2.08209 | -50.63767 | 2024-11-27 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 07f47686-3299-304c-911d-829a5ae487e3 | 2.08309 | -50.63827 | 2024-11-27 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f67d4b5-6339-3df7-87f0-f7fb39d26f0c | 4.2668 | -60.65274 | 2024-11-27 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 004fdb81-059c-33a3-9577-9d2a1038d3f9 | 4.26797 | -59.97397 | 2024-11-27 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 873baf2a-4a66-3f44-a8cc-d7b2c01c17d2 | 2.08232 | -50.63347 | 2024-11-27 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5fd0459-1313-36c1-8401-a4a9029e55f2 | 3.19919 | -61.00574 | 2024-11-27 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 862d59b2-a7f8-3a09-ba68-4e2a8e30d1e8 | 2.07538 | -50.62978 | 2024-11-27 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5382ff6f-b4e6-38c5-8f5b-99feebf1ff9f | 0.97293 | -50.12458 | 2024-11-27 05:33:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3291ab3c-9dab-3046-9fb4-758c980beef8 | -2.36724 | -56.11981 | 2024-11-27 05:35:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00dcd681-04eb-3248-8cf7-f560beaa5859 | -2.97266 | -51.5761 | 2024-11-27 05:35:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e81a7644-0db6-3b26-b796-ef0808e5ebfe | -2.6216 | -52.5361 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02a3a6ac-b05a-3239-8d07-5345ed97450f | -2.89567 | -54.1685 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4658a578-9b93-3d2b-bbd9-064ccc5b361b | -3.70793 | -51.80795 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a3f0183-630b-3056-a1a6-2095c6af9565 | -3.0896 | -54.12608 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df28b4ee-464a-3a24-a401-622ac1ef10c2 | -3.31291 | -53.75311 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96f1db7b-6c38-3c3b-a401-0e649bfccb46 | -3.59919 | -50.36209 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ddf046b2-d04f-3937-bb7d-77dcdfc2a1c7 | -3.10875 | -53.10322 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b80dc8d-ba70-32ee-b03d-dff0f3c5764f | -2.83215 | -54.12181 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b33e4404-77a9-3c8b-b05c-196868d5fca9 | -3.11055 | -53.25038 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3c75d307-b209-3dc1-8ff7-df601a3b0192 | -2.89949 | -54.1791 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a361846-fb03-35f2-97a8-7e3a124206f6 | -3.71007 | -51.80768 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a362d10-3950-3fd8-b4c3-d2b9cec4a629 | -3.09702 | -50.36263 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0ed31f3-70ce-3c63-9eba-71ef37ba5d7b | -1.62889 | -53.8738 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90ba6681-269d-3784-ad92-4fab4c846b24 | -2.80237 | -52.91289 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdccf028-2ee7-3f5e-b73a-bb690b0e4559 | -3.71417 | -51.80888 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc8be6e8-3e7c-35b7-99e5-aebb5233b043 | -3.40437 | -53.19958 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d3fbabb-6ed2-3bf7-b672-78ea693453e6 | -3.72963 | -50.18462 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc025196-3aa3-3521-acad-5c7a6a6e321b | 1.43504 | -55.90916 | 2024-11-27 05:35:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6df27475-1876-3b9c-88cf-9f0aef123e79 | -3.25671 | -51.14592 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11526fce-5eb4-34e0-9645-b966efaf7a3f | -3.71151 | -51.79797 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7965539-913c-3108-a7d5-bee9bd622fa0 | -3.50257 | -53.80735 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbbed567-0ed4-3c36-b615-2fa6280966b3 | -1.66697 | -52.71803 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a99d2e8d-01f0-3832-9f97-4aea8c65b118 | -2.609 | -53.96637 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c455fbb5-89d9-398c-b991-f62c8ae41084 | -1.73886 | -54.73737 | 2024-11-27 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 558ebfe1-ccc1-323d-bcb8-dad5d8e13698 | -3.0976 | -53.26011 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 0f46a15d-c9ac-3532-aaf0-1691149d52d5 | -3.10548 | -53.24556 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 851a567b-976e-3e21-9b2a-dd8964482c49 | -3.52755 | -52.15055 | 2024-11-27 05:35:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1fc1c31a-34bc-30ab-8c62-0ed54f207a98 | -3.29467 | -51.15754 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65dff29c-9cdb-35dd-a53f-aa6ddbb5838c | -2.83308 | -54.12139 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6b49b5c0-bdb6-3488-b04d-37af19f15ff3 | -3.59426 | -50.38255 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f140e4f2-4315-3429-a262-dc3002dac56c | -2.60367 | -53.96554 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84e4056b-b1d9-32ba-b8ab-c01bfb0ace87 | -2.80991 | -54.13123 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1eb10c99-b290-351b-9ef1-89f6e9dd7de0 | -1.06355 | -53.20629 | 2024-11-27 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06766f2d-3544-35be-a893-619cfe9fc971 | -2.18632 | -53.77505 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ede393b3-b4bf-30c4-bb41-0dba2471a4b8 | -2.83408 | -54.11483 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 88e42768-e528-3cab-ab95-cf154c45b07e | -1.44783 | -52.59452 | 2024-11-27 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fade5ecb-eead-3e93-b57a-a177245787f6 | -2.18043 | -53.77765 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fe3e9d29-8a79-3e9e-b62e-d5b530f46996 | -3.71776 | -51.79886 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d586cac4-ad38-3311-b74d-0fed910e1743 | -2.98106 | -60.98148 | 2024-11-27 05:35:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 601d366f-ff9e-3923-b376-6b31002adf14 | -2.25527 | -53.46531 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db137f54-f79a-310f-ab2f-ce8a553ea37b | 1.4401 | -55.91267 | 2024-11-27 05:35:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5231e95-555a-3f3e-aa1f-36431e090097 | -3.51967 | -50.21836 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 625a61e1-51c3-35e2-a8a1-a8af0ee6bef9 | -2.83697 | -54.12595 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 963d064d-3d4f-31e1-9b02-38b305f4cdab | -3.52684 | -52.15539 | 2024-11-27 05:35:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README76.md)
