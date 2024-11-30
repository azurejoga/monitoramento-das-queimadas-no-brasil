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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e593cc4-8e29-37bb-9d57-f79a9a914b27 | -6.07502 | -48.04963 | 2024-11-30 05:03:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 59efcdf7-737c-3432-9745-2c01e1d91034 | -6.25688 | -44.96569 | 2024-11-30 05:03:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 099bfc57-6622-3253-83f3-7dbc3569b51f | -6.08616 | -48.04053 | 2024-11-30 05:03:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88d80d76-73d3-31cc-86a7-8cf51d0b94b7 | -9.83553 | -63.36435 | 2024-11-30 05:03:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e1439f1-122d-395d-8ce0-dc107300964c | -9.4124 | -63.23423 | 2024-11-30 05:03:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 504ea1a3-677b-3ce0-bd56-28818a09a0f5 | -9.6354 | -64.19904 | 2024-11-30 05:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac33499a-54ae-35d1-98c6-da45c52810af | -7.1368 | -46.41651 | 2024-11-30 05:03:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56306abb-0076-379b-a7f9-2e468547cf00 | -4.45822 | -56.18369 | 2024-11-30 05:03:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 403af2dd-7fc2-3903-9d28-258937fc2599 | -4.28958 | -59.68901 | 2024-11-30 05:03:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 300c571a-dfe1-36b7-a386-f1ea442b5b27 | -10.18816 | -59.52906 | 2024-11-30 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 674c7588-8cce-322f-a75b-a9d335b325ab | -6.13789 | -43.9588 | 2024-11-30 05:03:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 863d2e0f-fda9-3394-94f6-d0f91e5fbe84 | -8.63963 | -63.46064 | 2024-11-30 05:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76bb1145-5b95-3f9d-b439-71130bdb0fa5 | -3.52138 | -62.77019 | 2024-11-30 05:03:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e7b4d05-ebff-3698-b7c5-76ac3a6e099f | -6.64388 | -47.91574 | 2024-11-30 05:03:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9793bf5-1b41-36f7-b304-c0685d27f020 | -5.27635 | -50.05156 | 2024-11-30 05:03:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c00e4fbf-56ac-3544-8ad1-d4837e5b793b | -6.92725 | -45.20454 | 2024-11-30 05:03:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 135a81ec-9442-3672-81c4-bed2a507ade6 | -10.18458 | -59.52845 | 2024-11-30 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3e91f48-b393-392f-a77c-649d09e8233c | -7.977 | -55.30342 | 2024-11-30 05:03:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79063d8c-8ef9-317a-be87-5c27c224f61f | -3.84299 | -59.58065 | 2024-11-30 05:03:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 39c7f38d-7126-30ec-a0bb-d7242a1865fe | -4.98347 | -50.48919 | 2024-11-30 05:03:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32f15be9-d0d5-3ca2-899d-cb9b6378b5a3 | -9.29052 | -64.24435 | 2024-11-30 05:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 411b8e5a-78d2-3086-8f8d-b9d96ded9c9e | -9.65028 | -65.74158 | 2024-11-30 05:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713f06ab-97c9-3a84-91c8-d942ba0e9cf1 | -6.63896 | -47.91503 | 2024-11-30 05:03:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b729aaeb-9548-33d3-b652-9ef659f74abb | -6.8187 | -46.7747 | 2024-11-30 05:03:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd1bcc9d-262e-3314-a9d6-617534ee3cb1 | -6.07648 | -48.03925 | 2024-11-30 05:03:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f737f6aa-842c-305e-aaf8-f4eccdee1c33 | -10.88239 | -54.3193 | 2024-11-30 05:03:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b872e69-71df-3469-9f19-68c2b5c056db | -7.13729 | -46.41284 | 2024-11-30 05:03:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 227da673-a80d-3fa2-aa72-4521556cc03d | -6.13229 | -43.95244 | 2024-11-30 05:03:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a8a34e6-f60c-37b8-a537-26a52107a1f2 | -9.63633 | -64.20155 | 2024-11-30 05:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d1f91d5-c285-3ae6-8979-7e45356de379 | -3.51347 | -62.8458 | 2024-11-30 05:03:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d78269ee-5de2-3a44-b0f2-3a699caac84b | -8.13754 | -54.85484 | 2024-11-30 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a8266bf-c046-321e-9070-890b9b8c166a | -9.80671 | -63.31636 | 2024-11-30 05:03:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fda7465-3350-32c5-9340-071b9d1df58f | -6.70528 | -47.27163 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a89e8578-ff8b-3992-aca1-bdd393bc3461 | -4.28568 | -59.68838 | 2024-11-30 05:03:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| effae5f4-e287-3972-bb45-2499783db59a | -6.21324 | -44.50009 | 2024-11-30 05:03:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a05e6ad4-91a6-3149-b8b9-acfba420edbf | -3.78751 | -58.98052 | 2024-11-30 05:03:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96228a99-b422-3c78-984a-df6ef4cd23f5 | -8.14091 | -54.85536 | 2024-11-30 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb776581-0a31-310c-a58b-cc38861aca73 | -6.81915 | -46.77148 | 2024-11-30 05:03:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdbe4773-8899-3aa6-a0c6-f013a22b513c | -9.86032 | -63.9889 | 2024-11-30 05:03:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01a18e6f-4126-3ef4-b146-3029b2ebcdc7 | -5.74569 | -46.18287 | 2024-11-30 05:03:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a38840d-03bc-3e0d-a98c-30a07dce1678 | -6.82448 | -46.7722 | 2024-11-30 05:03:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d245981-6c96-355a-978b-a145e44f3942 | -9.73922 | -63.03913 | 2024-11-30 05:03:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20825214-2987-345e-83a3-07b1bae907c2 | -5.5109 | -46.25727 | 2024-11-30 05:03:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9af8f10b-9cbb-36c6-ae23-d0b50dff982f | -9.82221 | -63.24915 | 2024-11-30 05:03:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70ee163e-003b-3f07-adaa-caefe1b55413 | -9.74334 | -64.63981 | 2024-11-30 05:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c527df30-b529-3e84-893a-f4082442f3e1 | -7.96792 | -50.6809 | 2024-11-30 05:03:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed640932-f80a-3769-adb8-22103954efe1 | -3.52144 | -62.84615 | 2024-11-30 05:03:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03131f3-c225-3d74-a655-65147536b54b | -9.64555 | -65.73727 | 2024-11-30 05:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ab91fc6-3cd3-3aec-b0de-626a661255fc | -7.96738 | -50.68466 | 2024-11-30 05:03:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5489f924-dcc3-3b26-9422-03038855fef4 | -9.66156 | -65.74035 | 2024-11-30 05:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 938c732e-07ef-3ef4-98f8-a9dd13bdfe37 | -6.70269 | -47.26842 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f31e389-a362-3dcb-b74e-5a3c433b3087 | -5.40798 | -49.15923 | 2024-11-30 05:03:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adba0201-f74e-3876-ab98-6728bc6260c2 | -7.97979 | -55.30747 | 2024-11-30 05:03:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cebd8925-2643-3d3e-94aa-97ab52497386 | -6.70103 | -47.2647 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0243cf33-2ff7-30e2-a89b-3b9dd7e96c01 | -7.21817 | -59.8572 | 2024-11-30 05:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71eb25e8-32a9-377a-9ab5-bd14dddd1b2a | -6.12341 | -44.9247 | 2024-11-30 05:03:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cc1a230-fcc3-3c0d-92ff-cbc2dce413db | -6.38281 | -44.75935 | 2024-11-30 05:03:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 28357804-6917-3c2c-b804-211d46983925 | -9.80574 | -63.31731 | 2024-11-30 05:03:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd9bc892-99e5-3af3-9a5d-0b3f4fe3b178 | -9.1891 | -62.38056 | 2024-11-30 05:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1382a871-446e-3d62-a4fa-6e36c8f9c544 | -3.52389 | -62.76951 | 2024-11-30 05:03:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8154bf2-d6da-3e4f-a60e-69bbcc587387 | -6.26225 | -44.97099 | 2024-11-30 05:03:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 526a52d4-c646-3b0b-82e7-306c64f7f603 | -8.14036 | -54.85895 | 2024-11-30 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 978c17ca-1298-3cdf-882b-5f4c4215b084 | -9.09897 | -43.196 | 2024-11-30 05:03:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 67fe5d27-95d5-3e0f-8ee2-76a4c38bddf7 | -7.86262 | -45.92049 | 2024-11-30 05:03:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da810818-b056-31e4-bf35-ed893d0c1e09 | -7.59119 | -63.23099 | 2024-11-30 05:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63ce9430-ac17-39e1-a74e-018be6c8e1a0 | -3.84346 | -59.5776 | 2024-11-30 05:03:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f8fd2e2-c61f-3b4e-a5ca-e2a29694bf3a | -5.73572 | -46.62407 | 2024-11-30 05:03:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b446839-1a26-3231-89e0-161642771269 | -8.37997 | -44.47268 | 2024-11-30 05:03:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a09ce90d-f150-3bc9-9172-ca62af99e3f4 | -6.21344 | -44.49873 | 2024-11-30 05:03:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ff4fce1-1aae-3e4c-8865-30eabb0ef5ae | -6.3768 | -44.75825 | 2024-11-30 05:03:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2eef593-33e2-3483-8eb4-b6f1147704ba | -6.92666 | -45.20888 | 2024-11-30 05:03:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2bafe97-bc42-328b-824d-4e47fe85449b | -17.57514 | -57.60997 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d8c5750f-0d75-3b91-9a38-29b0869f609f | -17.58183 | -57.61109 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e9204070-24d8-3ffe-8afd-7cdd597148f8 | -17.58239 | -57.60743 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 09976687-5c3f-3956-b79a-544e544723d8 | -17.61467 | -57.60839 | 2024-11-30 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 400d2642-cd70-37e4-9e31-467bb3c4d5bf | -17.57849 | -57.61053 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 892da2bf-6a97-33a3-bff0-27c1904e2fec | -17.57905 | -57.60687 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c6e0e8f3-6b95-3bb5-8c3c-9a544dfef595 | -17.57237 | -57.60575 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 304032cd-028e-31b0-bde0-7bf427b2241c | -16.18125 | -58.17653 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| fd6eca58-989c-377b-af24-1e3af51ba069 | -16.25199 | -59.95841 | 2024-11-30 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d07564ab-8ac1-341f-a5aa-d4530b947e4f | -16.24856 | -59.9578 | 2024-11-30 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a293e41-b47b-31e3-805a-12378eccad61 | -17.57571 | -57.60632 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4d1a314b-dfd7-30f1-a4e6-92763896d6ba | -17.57293 | -57.6021 | 2024-11-30 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d45858f9-39fe-3680-8f73-58e00984af90 | -20.11685 | -57.14267 | 2024-11-30 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f5cacbe-96b4-3574-904c-0bb77543c1dd | -20.64746 | -56.58702 | 2024-11-30 05:08:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78078e0e-f8ee-37da-8d94-85f399aea7f8 | -20.64807 | -56.58287 | 2024-11-30 05:08:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f1ae7f4-9b1b-3e77-be16-0cde9b674e94 | -20.114 | -57.13824 | 2024-11-30 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2294383e-7e37-372b-82cb-340ab182fc1f | -1.0733 | -53.6378 | 2024-11-30 05:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2367b136-055b-36a7-9f8e-eb6390290d95 | -1.6602 | -53.8728 | 2024-11-30 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0db329d4-8fa1-3e50-9be2-40b049645988 | -3.6061 | -49.9784 | 2024-11-30 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 183f8ef0-5829-3ce7-b22c-1fccd0ace55a | -3.259 | -53.6388 | 2024-11-30 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ea601aef-84f0-3d34-9ccc-3b753f70d180 | -3.2591 | -53.6186 | 2024-11-30 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1b19659f-c62e-3eb6-aae5-3b61068d48ea | -3.606 | -49.9995 | 2024-11-30 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8c260b6d-664e-3eaa-bcb0-330e2ce8e1ee | -1.6419 | -53.8731 | 2024-11-30 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| c3b83b29-c3fe-303e-b03c-0b5bd85524ff | -1.6938 | -46.7833 | 2024-11-30 05:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d71d3a42-c065-3152-ab38-946466d226cf | -3.259 | -53.6388 | 2024-11-30 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 0dae41ff-a4da-3d0c-9211-e99e81d166b0 | -6.9341 | -43.5634 | 2024-11-30 05:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| ef40f4d1-3757-3bfa-8b73-9374ab8aa19f | -3.6061 | -49.9784 | 2024-11-30 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| d564b241-665d-3b46-bf67-5689757a9779 | -3.606 | -49.9995 | 2024-11-30 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 60c3f887-47f5-3ce4-b66a-3c04d6dad02b | -1.6938 | -46.7833 | 2024-11-30 05:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |


[Clique aqui para ver as próximas entradas](README119.md)
