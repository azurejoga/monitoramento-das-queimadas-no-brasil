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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd15f967-0035-3454-9284-d235144fb59d | -6.4596 | -53.37989 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95aff004-0142-3a33-bd20-fb61e9bebd2e | -13.58236 | -47.01903 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a62e02cc-7185-3439-9011-150695ff0355 | -10.24241 | -64.48043 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50eeca7f-e145-3509-9501-75c125beb5d7 | -13.00304 | -45.18169 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1071725c-b318-32a5-a30b-8cc4bf8c6087 | -13.40234 | -46.36242 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed45b1e2-fb46-3b31-9a35-64c740ce757a | -12.94623 | -46.15639 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fae40e5d-f1cb-3bd4-8ace-e8fe63cbf2de | -13.40427 | -46.36289 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8ab8959-9036-3e31-aacd-0b1e9d4a5cf7 | -9.25164 | -44.49564 | 2025-08-20 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7a99de9-ae32-3c92-bdb5-0d95d7b47c82 | -9.17167 | -59.62246 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53676f01-aef2-365e-a4c4-0bd74513ae72 | -11.74147 | -58.32335 | 2025-08-20 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b6bfa428-8352-3037-b070-7c9221bc9569 | -10.2471 | -64.48473 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e408302-aee0-3d58-94b7-36ce1637a8f4 | -8.03396 | -47.66652 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 52fd0426-2e70-3e5c-94eb-34b2b65febf6 | -11.56776 | -50.45089 | 2025-08-20 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36983760-ebbd-3f99-b55d-90496c258a00 | -13.03213 | -46.80661 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 757277e0-86a3-302a-b5d0-6912e5604778 | -7.27168 | -50.18021 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7b21726-18c6-3702-a03e-1cd53d59ddd7 | -7.5058 | -63.83212 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0143564d-cb79-386c-936f-62758c871e6a | -13.57599 | -47.02798 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3f2bbfe-1b26-3a79-87b9-b17fc8f1e180 | -13.57678 | -47.02148 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59d45f4e-917a-3ac4-8ee3-17f4d8936132 | -7.55748 | -63.85233 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bcd7ce5-4bf5-34b2-ae6a-170573096ba4 | -12.90297 | -46.09537 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cfa8e1e-7ac9-301d-8de0-0840fb2dec62 | -8.96907 | -60.49835 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dba54bf-d17a-3d89-8db7-6335463713f4 | -13.57118 | -47.02408 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d2796a7-acbc-3019-882a-57b4992ee5ac | -7.5855 | -44.39593 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41b5e09b-0136-3318-9e02-a29366c99a70 | -11.61174 | -51.58909 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7435c0c6-b8b4-3718-a496-5955b00cee21 | -9.51161 | -60.52445 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e43ce172-8356-381c-a4bf-c9e744aea9e4 | -12.98993 | -45.19668 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd07be0e-16a8-3d8c-8a1e-b2e798c98eb3 | -13.029 | -46.78864 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f40ee30-19ee-3022-b7ca-5949b2cdf86e | -12.90254 | -46.09881 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47d38f07-1f30-32eb-93b9-3db17c23403c | -7.25242 | -50.17746 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 519dfb83-0a02-398e-abe0-35ea96642578 | -8.62788 | -67.26552 | 2025-08-20 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93347a64-c710-34c4-8da9-9493d315a07a | -11.59462 | -50.53412 | 2025-08-20 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36bba6b5-d8f9-35cd-8941-8acdc16dcd7a | -7.04527 | -59.23224 | 2025-08-20 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 236be762-670a-383b-a0ba-ebe5d5309700 | -12.98893 | -45.20505 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bf7a3fc2-0f91-3a14-9498-682ebdbbcabb | -7.63716 | -45.26704 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8da984a-d3ce-3e06-81b3-c8e8e2fc1145 | -9.52273 | -60.53429 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06f9adb8-5972-3822-ac6b-9d1b037d733b | -10.24938 | -64.48518 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4a7d76b-84e7-347f-9810-8466e4e3e67b | -9.19424 | -59.62801 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 299238c5-51f1-3488-a0cc-7063fc425121 | -7.65323 | -45.26999 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 919a47b1-acdf-3488-a880-f2bd18ff272a | -11.66817 | -60.1804 | 2025-08-20 04:57:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83c576e2-de8c-3688-a8e8-e071471e43dd | -9.51247 | -60.54422 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b663ca67-e98f-3d3b-b33e-2fe1c7dcfc4f | -13.86684 | -45.5616 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d957b117-fe31-3a75-a164-0b96bb2b3418 | -9.89549 | -60.28527 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9f0424d-a3f1-31b7-bd49-750d70c0397b | -9.18374 | -59.6419 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e739e133-a6e3-3467-bc15-9e31a91de730 | -7.55006 | -63.84734 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dc6b9ea-b892-3614-b240-f836e3aed27b | -11.6743 | -60.19179 | 2025-08-20 04:57:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a57460b8-fa2d-35ca-8093-c035e5adb848 | -10.24999 | -64.48186 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b3fc1f5-8786-3790-874a-aca3101efc9d | -11.90281 | -55.89035 | 2025-08-20 04:57:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebafdb24-7d0f-3805-891b-b1a4dd9e1826 | -8.88197 | -62.40432 | 2025-08-20 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5759d55c-9ddd-311b-aea4-57af03f75b4a | -6.13293 | -57.71084 | 2025-08-20 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b8b37f1-5bb4-36ca-8388-d13690ea8af7 | -8.61822 | -49.85077 | 2025-08-20 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed8889e3-10e1-3aa1-aa62-31507c408589 | -14.15854 | -45.28213 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43549608-4774-3200-a699-cbc6a56d80c3 | -9.17729 | -59.61298 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b22ecb38-0459-3174-a87d-b0098b977c5a | -13.184 | -46.87376 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 473b1f24-27e1-3028-b6e2-405933e5275f | -11.19493 | -55.91897 | 2025-08-20 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ff646c2-f75a-367f-a950-d3a53cb16609 | -7.12677 | -44.63945 | 2025-08-20 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bf7befe-b55c-3507-b834-dd67db7dafb3 | -13.02858 | -46.79217 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af357a0b-7865-3c98-849d-0517a5c2ed70 | -8.55532 | -66.9474 | 2025-08-20 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ead2a512-6363-3e71-96f9-bcc0e47f447d | -9.52207 | -60.53811 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b07982-015b-343a-b9d7-88853ffc545b | -13.14283 | -54.93093 | 2025-08-20 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fc15281c-9385-350d-a083-b8df6847322a | -9.23476 | -59.60397 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2faa9c1-6440-37c4-bfa9-578cbb79c394 | -9.23217 | -59.61918 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cccd0147-7d42-347f-aed6-741cdae8cd52 | -13.39162 | -47.49383 | 2025-08-20 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7fcd38a-cd31-371f-a9a3-e2130443242e | -13.19331 | -46.88434 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34889037-19b7-333c-891a-a12fcfc6636e | -13.19081 | -46.90455 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ae1a995-7e92-3ed0-aec8-c4c49fa29127 | -9.89205 | -60.28097 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbed3190-c648-3de3-92e2-b1958ce1761d | -6.92371 | -52.85632 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27fce683-ee5b-3f75-a286-6f132dcb76da | -8.55967 | -66.95936 | 2025-08-20 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61461722-c93a-3b0c-825e-8cacf3c036de | -7.12762 | -44.64396 | 2025-08-20 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7daf926-96de-3dc0-a5c2-a54ae4f2bbfb | -9.17677 | -59.5887 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c93380ac-f164-3493-a3d1-552b339c69eb | -7.5554 | -63.84834 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7380d324-3060-3c00-b5a6-a2e87ff1ce9f | -7.65275 | -45.27346 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0739524-e85c-3ee0-9516-c6cffa020782 | -8.9684 | -60.50221 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a45de6d4-ccd0-373b-8f10-fc47c6dd2af4 | -13.02977 | -46.7822 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a3eec02-4f52-3f7a-a376-43944a4dbe10 | -13.40193 | -46.3658 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e738fd9-471f-3f4a-97ce-51e490ad7c51 | -8.63437 | -67.26688 | 2025-08-20 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42577a76-28d8-3fbc-b934-21a4029ed860 | -7.64009 | -45.28557 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3df5af8f-2306-3fc5-9384-94d1007bfeaf | -7.63206 | -46.22274 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f0a2fdf-5b40-304b-aff3-2b8a35dab648 | -8.78903 | -45.47979 | 2025-08-20 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f558d39-0a46-3f53-8fd0-8ebab4a5ef98 | -11.44308 | -47.31548 | 2025-08-20 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b0cf871-33ad-33f5-a907-a4639bdb4c03 | -13.40348 | -46.3697 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f36572f-5a99-35cf-b3dd-127efab80232 | -13.41095 | -46.35292 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3d7588c-533e-3cf7-885f-6ba7212a5ba1 | -12.99325 | -45.21826 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4428635f-e6b3-3bda-a66e-85ebbd17d164 | -7.635 | -56.75444 | 2025-08-20 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcfa9557-bcc4-37d2-986a-093d3cc51a9e | -13.87691 | -45.57531 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be9cff5b-e0a5-3f53-b8a5-9adcf28e3ed3 | -9.21132 | -59.69405 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 746fe31b-5d8f-3fd5-8240-15fadab4243a | -7.97081 | -55.30007 | 2025-08-20 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee1ae6f5-203b-30a9-9e03-01a9b0341f13 | -9.17982 | -59.59441 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaeb20a0-7f5c-305a-9efb-c2e8a312ec44 | -11.74138 | -48.18927 | 2025-08-20 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e14778b-d537-3633-9f47-e31da9b6d5c7 | -13.19377 | -46.88066 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11ac456b-4abb-3d5b-aa19-ea93b8c11627 | -10.24465 | -64.4809 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8683e1f-d2a0-3038-974e-6ad29be1e3cc | -9.87154 | -45.9729 | 2025-08-20 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d0709cf-a48e-3e89-a257-2515484e0280 | -7.58601 | -44.39205 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7da5380c-adc7-31e2-94b3-4af47c1aece8 | -7.65958 | -45.2639 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54d0cf9b-6383-3bcd-9c2b-20cc3151bd97 | -10.00891 | -47.80368 | 2025-08-20 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34766537-6464-3556-86bb-7044eec6c4e8 | -7.63666 | -45.27066 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8dc3812a-bd60-3840-b5f6-fd519f7056e1 | -10.44587 | -64.41299 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b81f82-88ed-39b7-8dd8-42e949ab5257 | -9.19165 | -59.64305 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0c7443e-f0d1-3146-b525-2fbba1df1560 | -7.25869 | -50.18816 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 963b57b3-41cd-3c24-b706-782cc16eac57 | -13.87164 | -45.57051 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88ded3e1-ee1c-39f8-8607-cbf1a386c9c1 | -13.49028 | -47.0707 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
