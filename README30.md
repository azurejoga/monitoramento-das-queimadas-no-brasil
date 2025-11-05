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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d5fbb3b-a9b4-3a8e-a549-04a6539c51a7 | -2.60909 | -49.96967 | 2025-11-05 05:01:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 996902cd-5743-36fd-bd14-8be1ff2f8da3 | -2.48523 | -49.23167 | 2025-11-05 05:01:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87269bdf-995a-338b-a911-abca401b182f | -1.80785 | -55.68919 | 2025-11-05 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c8d9ac7-3d44-37bd-ba6d-f7e24c20158d | -3.79064 | -51.31157 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a71642fa-6164-3426-898a-a8fba0a6f758 | -4.36334 | -50.88148 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8947309f-05e4-323b-bba4-1f0134268e5f | -2.42015 | -49.29807 | 2025-11-05 05:01:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d73683b-4ade-3a87-a3f9-3e0cf12d5da8 | -4.45766 | -46.63471 | 2025-11-05 05:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 63c7f0c9-4651-3608-bd0a-035bbfbd8c02 | -2.93105 | -49.53121 | 2025-11-05 05:01:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f244bc02-20ef-327d-bb07-d132bffdee5c | -2.79321 | -50.31942 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e2da7cb3-2ac9-3ff5-ad51-30a83013ccb5 | -3.70612 | -45.88836 | 2025-11-05 05:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0915330f-28c6-3e34-8386-b836d8ebb96e | -4.46423 | -43.22858 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d4543288-d9f0-338f-94b0-aacd31d95e95 | -5.15676 | -49.87891 | 2025-11-05 05:01:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a726a051-cb7d-384a-bd0b-f7563a80486e | -3.70457 | -49.5668 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8daef59-de17-3237-a069-a8fff82b90fb | -3.96453 | -43.78183 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10dceca5-6769-34b6-ade6-0ad7cf1feea6 | -2.98514 | -48.70647 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7c5417f4-6b34-3cc6-94fd-ae407f9820be | -4.46277 | -46.63547 | 2025-11-05 05:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9878e89-75ed-30b6-a30f-b2eae3e20794 | 3.31942 | -60.07844 | 2025-11-05 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b0f25ef-bd0d-3913-bcf7-6b548ab4d7d1 | -3.27657 | -50.76579 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31b9fe8a-7895-3099-bd72-d11271ef17c4 | -4.15784 | -46.79721 | 2025-11-05 05:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6baf52e8-f9af-3b4c-802a-ae4fedbd42d3 | 0.25524 | -50.95815 | 2025-11-05 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f1a4956-2a2f-3630-88cb-5a3ccb5a44b2 | -1.61537 | -55.11731 | 2025-11-05 05:01:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc541f94-d0b1-3a5b-9470-b39d3fa0866a | -2.83562 | -49.41604 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b475edd9-df76-3b18-bd9e-8f76f93ffc40 | -5.45466 | -45.40199 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| c1e0ec58-58f4-312e-b2d3-d4512066cc26 | -5.47386 | -43.58443 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 94b4bcb0-53db-3fe5-bb59-293e80d67a05 | -3.49691 | -43.63065 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 13a6d739-185e-34cf-8dc6-7804a217143d | -3.84593 | -52.29827 | 2025-11-05 05:01:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c79e6b52-fc53-3376-b379-8d28b6f2e587 | -3.47648 | -43.64181 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e33dc0f4-ff3c-36c3-a042-4859fde725cc | -3.85007 | -49.90447 | 2025-11-05 05:01:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b609f49-f03f-34d9-b8e4-d0774be943c0 | -3.27265 | -53.26286 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ea59809-cc72-3874-9121-4d4341f771bd | -4.30216 | -43.78907 | 2025-11-05 05:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e22ffe6f-5b8c-3d34-b985-1d9640adda67 | -3.44712 | -50.21297 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f32232c-5bfc-39e8-9227-73d5e6dc1d0f | -3.13054 | -44.48022 | 2025-11-05 05:01:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a268512b-c230-3c0b-96b3-9a9c0b01c9ec | -2.27247 | -47.8537 | 2025-11-05 05:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a784dc0d-23c7-367c-aa4b-ff2b9a5af2cb | -3.31822 | -53.84517 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 164fb94b-85c2-3589-8ba9-4405bbf9d9f8 | -5.47129 | -43.58191 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5de58b99-1e1c-3799-951b-676726b13e26 | -3.7321 | -51.15833 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 501780d7-cd34-37f3-a245-68157828a4c7 | -5.0096 | -49.69663 | 2025-11-05 05:01:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 948f674b-5119-3b55-a962-93e3f59561d7 | -3.48012 | -50.02855 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4826c46b-be6b-3aac-8823-14d80940ec75 | -5.03741 | -43.62266 | 2025-11-05 05:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4c98a159-45cf-3de2-a75a-238e64b81575 | -3.97045 | -43.78257 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a3a332e-630b-3418-932e-b78ff4c78c52 | -3.7648 | -51.97437 | 2025-11-05 05:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f028cddf-32d8-346d-a16a-9a78e6f9a08d | -2.78825 | -50.3172 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e73f85bc-3fd8-3234-bf13-75a6615cb9fd | -3.59722 | -50.14878 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b715623f-b076-3986-8b53-4e19980ae97f | -5.43295 | -44.65752 | 2025-11-05 05:01:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 136b0f5c-e3cc-3a83-9220-877b26afebb8 | -3.58646 | -50.01615 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 192be051-014f-3b35-8415-3180698bd6ad | -4.41396 | -48.94791 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 60b7054b-2f78-3148-836d-7da213e2c358 | -3.25664 | -51.59739 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 676750a6-2a23-3e68-9b41-151ab98bc27d | -2.82738 | -49.41475 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1fa4f90-13bc-3c09-b486-1ec62d902f90 | -2.7875 | -50.32206 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c4be4892-685d-32b5-9b40-5d11ee18aa32 | -3.70044 | -49.56614 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39c96f1c-fb59-333e-9337-fe4eef2e7996 | -3.14754 | -53.14379 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb8bb53c-93dd-3c8f-981a-7d4b8b39626b | -4.46706 | -43.22296 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 596ff762-53b4-3f24-b346-68398f4abaff | -4.47138 | -43.22425 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b017b8a6-f609-39fd-8444-b9a7ea3a5a13 | -4.36263 | -50.88625 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 088d8548-a0a8-3664-b650-e8a3265a92de | -3.54728 | -54.69014 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5497cbf5-47cc-3c7a-92b8-31129f4e8a4a | -2.81618 | -54.35663 | 2025-11-05 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a604fed8-c0ce-38e8-a712-97c782c4c2e0 | -6.2747 | -42.5671 | 2025-11-05 05:01:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| cb57111e-d63d-36cf-9b4c-d54a4bc38c79 | -3.4785 | -43.6276 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a5340f2-d487-32c6-bfa8-f7a02d708d7f | -4.28114 | -46.93539 | 2025-11-05 05:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8928f21-0d28-37fb-a56a-caa0c140f832 | -2.7531 | -47.75084 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4517426a-73cc-319f-961a-7947b0276e65 | -3.23639 | -43.44003 | 2025-11-05 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ace49ca8-5d4e-310e-8b08-00d6cc3fff91 | -3.11164 | -51.0303 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82e85f4f-91a9-3093-a41d-071ff5f6d124 | -4.45222 | -43.22132 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 23009930-5b1e-3462-a4c8-27ec4c80e043 | -3.48463 | -43.62871 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1a10ea9e-8816-38f8-b961-971f72ebe1ec | -2.96108 | -54.91388 | 2025-11-05 05:01:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ddb5f043-f235-3c0b-b073-1aada5865a2e | -3.14415 | -53.14327 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98e2d007-d2a8-35ae-84fb-5ab13dcdeff0 | -4.477 | -43.23049 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c037f2d-793b-3349-a3ea-0ffed00dd035 | -3.49975 | -50.04887 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 525d27cf-8dc8-39df-bf39-c7343fa3f4b5 | -4.11197 | -48.02127 | 2025-11-05 05:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0aeb9d1c-2cad-3e88-9610-d9145e9f588c | -5.11201 | -46.22752 | 2025-11-05 05:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc5b09f2-6e73-356c-9b93-e32587a8e684 | -4.92162 | -47.32297 | 2025-11-05 05:01:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e48e1c90-34fd-386e-ac38-807f3e863def | -3.13115 | -44.47614 | 2025-11-05 05:01:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d641f947-ad96-39b9-9935-508d5bf5400c | -3.31598 | -53.83764 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3461ecb2-2693-342c-a6f2-33ad140b05ff | -2.8414 | -49.40553 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08efd0f5-ca04-3895-afeb-11263a4c3e90 | -3.40507 | -50.83979 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0bcda90-1c4e-3647-8926-a347d12e0f5f | -2.42483 | -49.29498 | 2025-11-05 05:01:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c4c5e2b-f3fb-3eaa-a5b7-098dc0d066e3 | -2.3746 | -55.65563 | 2025-11-05 05:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d05245e7-d415-3334-b69e-35e4f53749af | -3.40971 | -44.44172 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98752c22-7cae-327f-9191-1f1a5cf90913 | -3.82043 | -48.66483 | 2025-11-05 05:01:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1bf72abf-dad2-3a90-ab3d-3d72f6e91c9d | -5.1125 | -46.22415 | 2025-11-05 05:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 746edd31-13fe-35bf-a3ec-c589d14161d7 | -5.48154 | -43.57529 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 94ebb3fe-919e-3773-8113-378868ab5025 | -3.43608 | -50.23545 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67350777-8756-3485-a330-39e374cdd448 | -5.45414 | -45.40575 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d2b5731a-7392-387b-a2f1-b70c4568ca06 | -3.47754 | -43.6362 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae14514c-e9ca-3f22-b420-013d49ad2dc5 | -3.49748 | -50.46465 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 761ebae7-ce42-3d21-b73b-f1c495bdb276 | -3.32155 | -53.84568 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94fc8d88-6a36-3276-a73d-7b226532bfb1 | -5.05352 | -44.19254 | 2025-11-05 05:01:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf4aeab1-20be-3a27-9ea5-9eac0a9923c6 | -2.9808 | -48.70584 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f383183-36f1-3c39-b0c4-d0204828e84b | -2.29321 | -48.50987 | 2025-11-05 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec08be9c-6e1b-3053-976f-dfc9a8898464 | -4.18249 | -46.41584 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4e3671e-a641-36d3-876b-a5779c972ba7 | -5.04061 | -43.61851 | 2025-11-05 05:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f38d15ac-ee14-3356-9993-7d93f481e052 | -2.98283 | -51.3517 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 790e655d-57af-307a-a6e0-ddc42a08749d | -5.54463 | -50.07171 | 2025-11-05 05:01:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07130fd9-f240-39f3-aa39-fd9a7447d2d3 | -3.63296 | -54.75261 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1a9e446-bfeb-351d-bfcf-6b7061a29e67 | -5.46032 | -45.40265 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ced8ed0e-2326-3c92-ae96-860f236660be | -3.5861 | -50.16901 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03674c32-ddb1-356c-9020-a8e5630052b9 | -4.36669 | -48.3569 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4183e6b6-38cf-3433-8a84-2e7387e93ee8 | -3.5121 | -55.50093 | 2025-11-05 05:01:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f45d5589-b627-312c-aaae-526e8d226a19 | -4.47201 | -43.23449 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4eeb6344-fa3f-3e3d-a248-709d5844b1dd | -5.03366 | -43.62236 | 2025-11-05 05:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |


[Clique aqui para ver as próximas entradas](README31.md)
