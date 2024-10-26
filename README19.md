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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0225c822-8282-3137-af80-f438dd0b3527 | -12.5311 | -63.052898 | 2024-10-26 01:28:42 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 76a339d9-7f01-3234-82f2-2dffe9ce405f | -8.541 | -49.547401 | 2024-10-26 01:28:56 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72a3ded2-d489-3cef-9b9b-b20442925e29 | -8.5459 | -49.566601 | 2024-10-26 01:28:56 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c162b8fd-7466-35d0-afae-b7d1642b093e | -10.0934 | -56.190899 | 2024-10-26 01:28:57 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eaea785b-49db-352e-b5b0-4639fabcda10 | -9.909 | -55.7127 | 2024-10-26 01:28:58 | METOP-C | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7b19ca6-9abf-3202-9777-eb828ee0784d | -9.9108 | -55.720501 | 2024-10-26 01:28:58 | METOP-C | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47b888f2-254b-36f9-9d22-648e35604cc8 | -9.9927 | -56.245899 | 2024-10-26 01:28:59 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99888ef7-4c2e-3957-872e-51e36584d236 | -7.9805 | -49.690701 | 2024-10-26 01:29:06 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f624f878-42b7-3868-8ef2-88309fe52f8f | -5.5565 | -47.018002 | 2024-10-26 01:29:34 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bed460b1-f4ac-31f1-b8f1-86f7fe4b9df9 | -5.5647 | -47.049999 | 2024-10-26 01:29:34 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9efd8f65-8b1d-33d5-ad1f-d4cc5c13fad4 | -5.5469 | -47.020401 | 2024-10-26 01:29:34 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15fbdaf9-8318-31ea-8395-f041902da439 | -4.5822 | -48.0033 | 2024-10-26 01:29:54 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edba2159-ddd5-37f4-bd53-283577e139c9 | -4.5894 | -48.0317 | 2024-10-26 01:29:54 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72cc8163-03ab-3e46-821a-27df0babd360 | -4.5727 | -48.005699 | 2024-10-26 01:29:54 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 287ff30e-206c-3c06-a8aa-d3f19281d298 | -4.5798 | -48.0341 | 2024-10-26 01:29:54 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b58ed1eb-d3df-3773-b852-bce737e5102d | -4.563 | -48.007999 | 2024-10-26 01:29:54 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f35125ed-b7b1-3f00-967d-0be7eaca92b0 | -4.5701 | -48.0364 | 2024-10-26 01:29:54 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a846aac-32b2-3ec8-bb70-84512bcb5b62 | -4.3047 | -48.650101 | 2024-10-26 01:30:01 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bebe6e2-efdf-3347-bd09-51cd9c001a8f | -4.2951 | -48.6525 | 2024-10-26 01:30:01 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67db692f-91eb-3aec-b6c9-db4de932f5f8 | -7.6461 | -63.438702 | 2024-10-26 01:30:03 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 931ca084-4812-39c0-b4f7-ae87d7f62595 | -7.6483 | -63.448799 | 2024-10-26 01:30:03 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28a7e505-b086-3980-bcf1-480f7ce7b31a | -7.6385 | -63.450901 | 2024-10-26 01:30:03 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4a0d84-06ee-3534-81cb-cb307fca2b6e | -6.3314 | -58.3064 | 2024-10-26 01:30:06 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60af480c-aa39-31da-976d-516088358412 | -6.333 | -58.313301 | 2024-10-26 01:30:06 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7030b8e7-6588-3613-829e-2bf387366801 | -6.0867 | -47.215099 | 2024-10-26 01:30:10 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a09fa3dd-268e-3a05-8a30-8dde5aecc596 | -5.2496 | -55.9618 | 2024-10-26 01:30:15 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e360c64d-5ed2-301c-a712-0cf7de405cdb | -4.3439 | -55.355999 | 2024-10-26 01:30:27 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5f965bf-598c-3039-82e8-17193f3a69d3 | -4.346 | -55.3652 | 2024-10-26 01:30:27 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbf5ad1d-ec7e-3410-8002-c57763e8b3d2 | -2.8203 | -49.254101 | 2024-10-26 01:30:28 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0ffbd97-0e1f-3954-9ab3-c3f59c7e7898 | -3.7697 | -53.410198 | 2024-10-26 01:30:29 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99095d2a-7c1e-3240-a739-62cac7708495 | -5.3122 | -60.116402 | 2024-10-26 01:31:13 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e315d65b-9894-3e3c-8223-3fcc17f98d50 | -3.0135 | -50.472801 | 2024-10-26 01:31:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 189090f7-aaf3-3fbf-be72-2baab253050b | -2.9989 | -50.454601 | 2024-10-26 01:31:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2340124-c286-38e9-aa89-9c868902ded4 | -3.0038 | -50.475101 | 2024-10-26 01:31:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc184713-e69c-3a19-8b4a-49e80cf479a7 | -3.0989 | -51.337002 | 2024-10-26 01:31:15 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aad4df07-4fd9-3cb6-8e59-193ea42a641d | -2.3735 | -48.297001 | 2024-10-26 01:31:15 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b7e7ba-7718-3463-9096-ee86c78b9e81 | -2.3639 | -48.299301 | 2024-10-26 01:31:15 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 985fecbf-a6b1-3ca0-97b3-94d30dffa59e | -4.0437 | -56.274502 | 2024-10-26 01:31:19 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80776fff-7a14-3f4a-afc3-8aac52022b5c | -3.4166 | -54.570099 | 2024-10-26 01:31:23 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd61d78-5bd4-316c-9583-3e67cf7e1aeb | -2.9507 | -52.5616 | 2024-10-26 01:31:23 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08bc5e4e-7ea3-3b16-a485-221c74a07a41 | -2.941 | -52.563801 | 2024-10-26 01:31:23 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b33d7579-4dc0-32d9-b34c-d7045081d1ca | -3.4191 | -54.5807 | 2024-10-26 01:31:23 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af025519-9e08-3c98-af56-fb7bf3a76747 | -3.6375 | -55.509102 | 2024-10-26 01:31:23 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77fdf291-a763-3d3b-beab-a3fb793d688c | -3.6256 | -55.502102 | 2024-10-26 01:31:23 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb2e577-366e-3fe3-ab7c-a8c0a668f4c5 | -3.6277 | -55.511299 | 2024-10-26 01:31:23 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ce05a6-c6fe-3a93-ba7f-7b7adde6c69b | -2.6962 | -51.795399 | 2024-10-26 01:31:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71638a50-c822-33c7-ab2c-d3ec34fa157c | -3.1 | -53.7094 | 2024-10-26 01:31:25 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f352484-088e-3ac9-ad2d-b70c1bf52b76 | -3.1029 | -53.7216 | 2024-10-26 01:31:25 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b3d2ea8-8559-38f7-87dd-1c0e0ce230db | -3.1058 | -53.7337 | 2024-10-26 01:31:25 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d954c619-2c1c-3cd0-b59d-846560d242b8 | -2.6868 | -52.056999 | 2024-10-26 01:31:25 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef5ee88-a360-3508-b752-92acc3163bf5 | -2.8815 | -53.307598 | 2024-10-26 01:31:27 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de66e8a-60e4-3ba1-bfb9-b6c53b2ee00b | -2.8846 | -53.320702 | 2024-10-26 01:31:27 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2d4ead-e8c2-3190-86ea-610aa228f2d5 | -2.9794 | -54.637402 | 2024-10-26 01:31:30 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb9a899-b7eb-3550-b9d0-fbfa33f3f2f3 | -2.772 | -54.7187 | 2024-10-26 01:31:34 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5040c574-7caa-3aba-948d-6a13002a1850 | -2.7745 | -54.729301 | 2024-10-26 01:31:34 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8376ed1-0fa8-3514-9bb5-caac420a070d | -2.1982 | -53.722401 | 2024-10-26 01:31:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64cdb0a8-4601-39c8-a19e-a940e3260441 | -2.1855 | -53.712101 | 2024-10-26 01:31:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db7614a5-a088-3807-80e0-2ffa7743aab7 | -2.1885 | -53.724701 | 2024-10-26 01:31:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81f0e308-1288-3a54-882b-234a7239a690 | -2.1914 | -53.737202 | 2024-10-26 01:31:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c8b467-0868-37fa-941b-467fec9debf8 | -2.0933 | -54.5896 | 2024-10-26 01:31:44 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee231a3-0067-3cbb-93a8-89fd9bc6b3aa | -2.1494 | -54.917099 | 2024-10-26 01:31:45 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b76ab78-b97b-3dfa-99c3-2094c1050503 | -2.1519 | -54.927601 | 2024-10-26 01:31:45 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a298870-89b9-3e33-ae2d-0a8905b2c85e | -2.1421 | -54.929901 | 2024-10-26 01:31:45 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a95106c-eb00-33ad-9031-68cb881d1f32 | -2.7312 | -57.459499 | 2024-10-26 01:31:45 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 026acdc2-cfaa-3b26-8ca5-95f91947885f | -2.7214 | -57.4617 | 2024-10-26 01:31:45 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c10d147-ba8a-3e52-a3f6-609a57ba6389 | -2.7231 | -57.469299 | 2024-10-26 01:31:45 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b2a1dcc-cf94-36cc-a02d-429e73f931a3 | -2.0884 | -54.920101 | 2024-10-26 01:31:46 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92283a98-dad8-3431-9866-4ef4f8e9ca99 | -2.0909 | -54.930599 | 2024-10-26 01:31:46 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf38b69-6207-39ee-9593-8c90b5aa4595 | -2.0138 | -55.880501 | 2024-10-26 01:31:50 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dff326c-03ac-3681-bcb3-4fed4be111de | -2.016 | -55.889702 | 2024-10-26 01:31:50 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96629753-cbe7-333f-bc5d-7686dde17224 | -2.0409 | -56.0853 | 2024-10-26 01:31:51 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a436dd80-0806-3ca7-9c06-4796b523bdce | -2.043 | -56.094299 | 2024-10-26 01:31:51 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51026bd3-373c-3ae4-b049-33f5d3924861 | -1.344 | -54.595901 | 2024-10-26 01:31:56 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08b9327d-d28b-3587-a892-77a912cb644a | -1.3466 | -54.607201 | 2024-10-26 01:31:56 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e0ad10-cc59-3e2f-bce3-c28ae87f38ef | -1.0731 | -53.655102 | 2024-10-26 01:31:57 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01dcb555-9cc5-3871-b297-00b8c72ef4d8 | -1.0634 | -53.657299 | 2024-10-26 01:31:57 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c2bcd9-64cd-3aeb-8d2b-56dbc747fa11 | -1.3856 | -55.835999 | 2024-10-26 01:32:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93e0888d-6681-34b9-9439-5b12e4a84c07 | -1.2861 | -55.7178 | 2024-10-26 01:32:02 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aad87052-efd4-33f5-baee-66f3d188b242 | -1.8734 | -59.554798 | 2024-10-26 01:32:06 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f08aae6d-8ffc-3bc3-804e-dda4ce92a474 | -1.875 | -59.5616 | 2024-10-26 01:32:06 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 542f5060-fdba-3d91-bee0-11b819db72c2 | -1.8935 | -60.001202 | 2024-10-26 01:32:08 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67a3ce6b-25be-38c6-9337-e6757ce83404 | 4.032 | -61.195801 | 2024-10-26 01:33:48 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a8675288-24ff-3b5d-8d7b-550659535f4a | -2.1929 | -53.7234 | 2024-10-26 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 560f1619-b05e-31b0-9b5b-bdf3439fe978 | -2.8739 | -53.3252 | 2024-10-26 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 154a52ad-2bc8-3123-a903-45cc246fd42b | -2.874 | -53.3049 | 2024-10-26 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 75e76bb6-006d-378e-8f54-438d857a1dc5 | -2.9317 | -52.5713 | 2024-10-26 01:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e7303598-bd1e-3c12-97c8-88994be46456 | -2.9501 | -52.5708 | 2024-10-26 01:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 5cf3c44f-fd3f-39e1-a6ad-6b4e4abff8e4 | -2.9501 | -52.5504 | 2024-10-26 01:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| dff3e482-4b14-3876-b353-cbed55aafe43 | -2.9578 | -50.4198 | 2024-10-26 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| ab278b4e-fe3b-375a-b9e6-aa1cb7000a09 | -2.9944 | -50.5025 | 2024-10-26 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 2750277d-da56-343c-8ac7-351595b1f5cc | -2.9945 | -50.4816 | 2024-10-26 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c70b9809-5f17-32e1-bd3f-d055afa6c4b0 | -3.0129 | -50.502 | 2024-10-26 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 22d9f693-ae36-333a-a51d-bfc937842c14 | -3.013 | -50.481 | 2024-10-26 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 81cb9031-1e35-3c4e-a5ee-5016ed231869 | -3.1116 | -53.7234 | 2024-10-26 01:35:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| fa8af299-f8ee-3dcc-88b7-4ebc57d91042 | -3.2393 | -45.2918 | 2024-10-26 01:35:23 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 101.4 |
| f380a81b-9491-3145-b19c-390910b3594d | -3.4729 | -43.3377 | 2024-10-26 01:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| eb63dddd-a4b4-3f11-b97c-cc27ed09b652 | -3.473 | -43.3144 | 2024-10-26 01:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| aa8f0fee-f4b6-3584-9085-8a620a2ade9e | -3.4915 | -43.3368 | 2024-10-26 01:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 3fdef53f-a51b-3597-8f68-5fc618eefd04 | -3.4917 | -43.3136 | 2024-10-26 01:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6baba216-bed0-30c6-b304-84e35a78cbcd | -4.5613 | -48.0358 | 2024-10-26 01:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |


[Clique aqui para ver as próximas entradas](README20.md)
