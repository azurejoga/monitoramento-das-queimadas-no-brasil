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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32a7f448-706b-3d52-be5e-3a7592eb1060 | -3.07384 | -51.26732 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca106707-4a2c-36a1-80a4-c577480abb7c | -2.44116 | -51.78707 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79348b8e-5fed-374a-adbe-39d88cfd83f8 | -2.86644 | -53.99035 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fa31321-e7aa-37f6-9332-8bd5d6ba5f1d | -3.21849 | -54.23541 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5137f7f5-87b5-338c-8008-21674ecf0dea | -1.43894 | -53.39264 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92eab1fb-ebc4-31bd-9885-f3020cc1f539 | -3.09579 | -53.72749 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9f0256d-e929-3c21-9df9-31d7d0e5d40d | -3.10528 | -53.22864 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1885734-3b6b-3ff6-b8db-ed06dd677c19 | -3.25463 | -53.93265 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f17861a9-60d8-3d26-b001-83a69896d5a4 | -13.10794 | -58.05273 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58bb76d5-491b-3097-a670-aa90bb0210ff | -3.25796 | -53.66502 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a334351-2392-3578-9ce7-ca9459810b83 | -3.06952 | -51.26622 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a66b41e6-c3f0-3f4a-b6b8-8800c7e1aee4 | -2.37033 | -53.8561 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ebb4d3a-dfd9-36fc-9b53-507b8e8cd7cd | -2.78816 | -55.36561 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a3d3ad7-63f9-34a4-bdd6-cae1fdb1e171 | -3.10979 | -54.0315 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a2f8513-9732-3668-8adf-9cd010ec07fe | -2.63864 | -54.409 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c01d587f-4e69-3c61-b0e0-9cb223d50b1f | -2.8203 | -53.05861 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3d7fa27-a067-3b92-b52c-f5a628a222e3 | -2.97807 | -53.87957 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ee125ac-431e-3605-a009-445727cbea67 | -3.17741 | -54.33725 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c00f7953-e63f-32ca-93e7-180687a8c7c5 | -1.93164 | -53.44193 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 923b002f-23c8-3c74-94e9-961356ca87c5 | -3.17857 | -54.32941 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62b49f64-7a5e-3078-a7d5-1dc8b3b28d77 | -10.05141 | -59.12094 | 2024-12-03 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e00879d-9925-349f-8de1-6148a8815bfc | -4.1648 | -48.19543 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 769bf6a7-6f34-3482-8474-41512f8fa7cf | -2.21318 | -53.78522 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 34b3221c-c065-31ea-aa47-d3c25b76aeeb | -3.70128 | -51.82632 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2086fea6-3e69-3ce8-b527-cee7209f5ee0 | -3.09557 | -54.05088 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cd455eb-180d-3f1b-9e8d-0f8cf20e668a | -2.44458 | -54.00374 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 940b4872-3954-316e-a0bd-eb932ca976b4 | -9.31022 | -62.08736 | 2024-12-03 05:25:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a881a2ee-a9bd-359d-a47a-a6eab4177906 | -4.04759 | -46.99992 | 2024-12-03 05:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f436a65-9790-3fd2-8095-b6f08dcacddb | -3.2985 | -53.66628 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dcb8b457-5fb9-365a-b1ff-4907af2932a9 | -1.75808 | -52.78749 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f17923f-041c-3607-8139-1860ee10c74a | -2.85595 | -54.05907 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc7b5a3a-664a-3d57-9851-61bdfc8dfc2a | -2.4572 | -53.63124 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7645dac9-071d-3f2d-b582-4c5a753fc7f9 | -3.25788 | -50.60977 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a901c6bf-d044-3975-b9cc-b2779560442c | -2.78032 | -55.36446 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bafcd46-4a4b-3d45-859b-bb626a6dbee6 | -3.24981 | -53.66202 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67e27124-397e-3972-ac6b-eef72060bc6b | -4.17186 | -48.19658 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0aa8f829-ec56-3a77-a52e-23cbb50c4736 | -1.49645 | -54.44657 | 2024-12-03 05:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f63fc53-deb7-32dd-bccd-b7678fb9b611 | -2.46222 | -53.62766 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5092e087-8426-3cc1-9509-3cafc4059ebd | -3.25086 | -50.61945 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c633445f-9e21-3676-b36a-01ad8ec28143 | -3.39241 | -51.14924 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0e3adb3-50b8-3d6b-956f-0437e6d41d39 | -2.20148 | -53.77482 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b348960-bca6-3857-bd5c-38c9f132d359 | -2.84068 | -54.1019 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b87c01b-9708-3eb9-9a06-19ec8453288c | -3.25047 | -53.6577 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5930a90b-84a7-3574-8448-90134ddfd11b | -3.21003 | -53.12069 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3af4de40-c8ac-30ca-b0ab-a0e2d35c4c67 | -3.38761 | -51.14521 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c640664-a0cc-3b1e-8001-decf790b66a3 | -4.17124 | -48.19651 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e17fce7-3b8d-31a7-8695-1c47998c1178 | -3.10073 | -53.75436 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4653ce1-16de-3bb8-93de-0b103750e805 | -2.90289 | -54.17496 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da1e7457-4c2f-32c0-bd56-09f82562d836 | -3.12501 | -53.98794 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7018628a-16a5-3769-bcbb-4bfb04a92978 | -2.87559 | -54.01674 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 814321a1-f841-3f5a-93f7-c7f29c74c2af | -12.71012 | -58.2146 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d8b7414b-e460-32eb-872d-b4dd2bddf539 | -1.69599 | -52.63619 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 050cf35c-d30a-304a-80c9-0ffe02056c84 | -3.25858 | -53.62949 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 322a5b33-4e1a-38dc-af9a-3a201daffc6f | -3.26237 | -53.63458 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3d61fa9-e201-3193-adaf-2ac4e2a13d75 | -3.29271 | -54.14858 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa4512f2-5098-323c-a5c9-48d1d804a047 | -13.10861 | -58.04794 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 835fa36a-6c94-3af4-949b-be0c9c37aa74 | -2.71022 | -54.9574 | 2024-12-03 05:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f28e320a-444d-34e1-a670-8f6ca4f46f75 | -2.58597 | -53.67174 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5301f3e4-5b97-38af-95f8-d19d15c67d38 | -2.46288 | -53.62328 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d47a4112-4d41-3b30-9212-c88f4f2dacab | -2.56237 | -53.40786 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6a1c67e-9881-342d-94a6-b2c4826ed31c | -1.27095 | -54.11897 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a2b8a4a0-ab15-3444-b38f-a9a8222dd12a | -3.2192 | -53.12218 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04daee6f-2ac5-335e-ab05-8bd9ebf1f76e | -1.50128 | -51.93604 | 2024-12-03 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cbcc755-c60f-3905-8f3a-3e714facd2ab | -3.30358 | -53.66256 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ffdadab2-f9ad-3bd3-bf31-3c73d469a37d | -9.03003 | -63.52903 | 2024-12-03 05:25:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52261c8e-5581-3be1-b1b7-299e3a1b7523 | -3.21462 | -53.12143 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b2b547c-0a8f-36eb-8131-30ea3ec0a9df | -3.25578 | -53.62277 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b645c4b8-a2d7-31c1-8668-1ea29639d27f | -1.40057 | -53.66874 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e056fc26-b53f-33bc-a9b0-83bee46f4cf9 | -1.50722 | -60.39531 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97f0e473-e474-3c4e-ad53-5c4d2b10cdbf | -1.75517 | -52.8063 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8f4625dd-e27e-353c-80a5-4dbd37bbfe39 | -2.80584 | -53.06115 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f5da6fa-da77-384a-86f1-4eb9fb58c356 | -2.78656 | -55.35009 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0089edf-3c49-321e-8b94-aa60668e5a57 | -2.78419 | -55.36647 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2eb821c-28db-3def-85b5-c1b27005a2a6 | -3.28049 | -54.14253 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab9d1cbf-15d5-386a-b097-b8dd4d4936fd | -10.68563 | -62.87314 | 2024-12-03 05:25:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51f600b1-c997-38d1-ab19-0b0c519949b6 | -13.11149 | -58.04614 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1a48bf9-ddaf-3e09-9e62-444188787fe9 | -1.25285 | -54.53867 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb34dd14-1b6a-3cda-9f21-e98dc890ae92 | -3.25859 | -53.66069 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8ca2e697-6b5d-35cd-be1b-b8e1728be745 | -1.73283 | -52.61225 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 996dacd1-520c-3bee-b15a-16041f891912 | -8.57722 | -63.42169 | 2024-12-03 05:25:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 329497bb-1e0e-318f-bb32-126e40e31719 | -3.10885 | -53.75999 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2da4e2e-459e-3a29-94d8-08799e210828 | -3.25179 | -53.64902 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be82d838-f3f7-3258-bbe6-949b79eaa2cf | -2.58529 | -53.67615 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6506371-690c-3848-a439-0ac24d729b6a | -3.37531 | -50.70233 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b1c587f-a847-3569-987e-bdd95ebd8fa9 | -3.28263 | -50.795 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec257a94-ffa7-30ab-9f53-876fe376be19 | -3.25402 | -53.93674 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af036d39-d35e-3140-9b4c-bb63cb090fbc | -3.25112 | -53.65337 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d7ddcbb-8be8-361b-bcae-59a58d08be3e | -2.21011 | -53.77627 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3afc70c0-5589-308b-8e2a-89b7e59146ec | -3.10562 | -53.29034 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81996750-5249-369a-a96e-a5848a5ab394 | -10.9373 | -58.97024 | 2024-12-03 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b07cd36-f8b9-3f4d-a69f-602cd9c4c010 | -2.81716 | -53.04853 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de90aae7-401d-3f3d-bd99-fbca5ecffe11 | -2.74757 | -54.17287 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9892dd1-cac4-312a-87bb-020eaacbbbd1 | -2.62814 | -57.69916 | 2024-12-03 05:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6a19b6f-859f-3f6a-8ac7-b17284ba45a8 | -10.46294 | -58.67779 | 2024-12-03 05:25:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 698419dd-d4e8-30ea-817b-390e9c766dc2 | -2.80774 | -53.04863 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 638afe90-3897-384a-9f24-c350b8def93c | -3.21456 | -54.17389 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 852f71e2-6a25-3be1-84c1-fc817a045049 | -2.97436 | -53.87474 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2552cfcc-116b-3e46-b0d9-2df09139a7b6 | -2.37189 | -53.85835 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4237fdb1-f468-3d60-884b-517d2a53e764 | -12.70569 | -58.21874 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5b05a998-734f-308c-bbfb-bfc71cedc0aa | -3.0982 | -54.05058 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README59.md)
