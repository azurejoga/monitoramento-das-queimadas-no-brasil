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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f17ea7a4-f100-355c-ad41-1d1176a20943 | -10.60761 | -53.98768 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| fa584392-6602-35c2-83be-acad3c474c8e | -9.60727 | -66.11938 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b051d96-975f-3cf1-b2f8-2f92ac09d483 | -8.67587 | -70.02573 | 2026-09-22 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28bf6656-5406-3d62-91bd-1b015eb5615f | -9.76374 | -65.06576 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 805a8d46-d731-3d7c-9cfc-c8fc76d3f810 | -9.48658 | -67.15703 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b56b23fa-b711-381b-a6f3-34aeb8a0d20b | -10.90261 | -54.07757 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aadae4a1-ae77-3b53-98c3-1e332b9a250c | -11.32518 | -54.04079 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 365600bf-d3ec-39f5-b5e1-c49c45ff4064 | -9.36914 | -68.66007 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c1b1904-2a7b-32eb-8ea3-3aefbcaf2106 | -8.7934 | -69.02632 | 2026-09-22 05:44:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74dd41b6-4929-39bb-9310-2d2a6b706137 | -10.60707 | -53.99204 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e1a0e5fb-95d3-38de-9415-be34d9e49f8f | -9.20316 | -64.5103 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ffa7dd7-b888-35e4-8259-b67b046b8d97 | -9.18207 | -65.85739 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b644c4-b2fd-3d74-8af7-79eb6e4c6e8d | -9.18265 | -65.8538 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf55867-af91-31f9-b46b-2d3892cb0d7c | -10.24333 | -68.74813 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0ca3dff-5bb7-337a-b56d-1a0b1f038d80 | -9.72768 | -64.69489 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e05dfcb-b686-333d-b0d8-9c1a628e36f6 | -10.88925 | -69.34592 | 2026-09-22 05:44:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75650ce9-998b-3afb-b5ba-9fa4f05e7626 | -13.51126 | -51.52296 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3d31313f-8c26-3377-92fe-58c4c648e20b | -10.20805 | -68.74896 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8bf2cf1-dac9-3b29-acdf-af46db0862b1 | -8.7973 | -69.02697 | 2026-09-22 05:44:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92c5afb1-ec61-37a0-86ac-30acfbe7eeca | -9.55818 | -66.02961 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9784b291-0704-3455-8d70-bcf7129ffe73 | -9.7659 | -65.09481 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ac29625-fa0f-395e-bff4-d772459ca998 | -8.9204 | -64.30121 | 2026-09-22 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc833b6c-a9cd-363a-9f9c-0dd86253e1e9 | -10.59676 | -53.97742 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 950eb8b9-017a-3a33-bbd7-c9ae6ce6e6df | -8.79565 | -60.79633 | 2026-09-22 05:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9ebb38a-d07c-36b6-aafb-f65becbf2576 | -10.61412 | -53.98399 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0deb36eb-28db-338e-bd15-bf903bf988a0 | -9.65964 | -54.33804 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adaad7ba-46b8-3710-989c-52025d04d869 | -11.96226 | -64.04149 | 2026-09-22 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13cf112c-f68c-3f4b-a37e-deb6f4721b0a | -8.5323 | -67.00931 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d9d43e4-f740-3fb6-8ad4-658a9eae54d7 | -10.90355 | -53.9699 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8a46ee5-8b17-3ce2-8ea9-ec7b2b55442a | -13.51588 | -51.50826 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 312e2a73-d685-339a-a686-955a0c28fde9 | -8.69748 | -66.93369 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eb4b2aa-96f9-32cc-a1a5-ffc3ed4c7025 | -8.67938 | -70.0303 | 2026-09-22 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d5c9141-eda1-35a8-9c83-e7ad6c63b13f | -11.14925 | -51.10015 | 2026-09-22 05:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe900c2d-caf2-35ab-81d5-bb4513108de3 | -9.56316 | -66.0416 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ead44ef-3e9e-3ea1-8f01-db7e3640bc5d | -10.606 | -54.00071 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa81a807-c62a-3496-b534-900bff0876a5 | -8.7913 | -60.80019 | 2026-09-22 05:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b5dc057-31e3-3849-801c-d96ed6d6c43e | -9.87368 | -55.7342 | 2026-09-22 05:44:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb2f2a1d-362f-3ebc-9001-3be995a16c02 | -10.60055 | -53.99578 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77d2a0d7-bf78-3c71-b902-1d6172906afa | -11.31657 | -54.04192 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59237742-e64a-3a09-91fc-d69baadf8449 | -10.60002 | -54.0001 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 108cdba8-59ee-347a-a56f-75cd15df493a | -11.31545 | -54.05075 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd433000-1658-3712-b408-c6a00e9b8583 | -11.04854 | -54.14778 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16c8f4ad-6b54-3919-8e8e-51264bc63360 | -9.63202 | -63.15028 | 2026-09-22 05:44:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c745100-aa14-3324-b121-0ee36d4288ec | -9.10303 | -67.82446 | 2026-09-22 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4184155d-8bff-353e-bfa9-fcf95386741b | -9.10525 | -65.3802 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb312cae-0dde-3aad-830a-4cc6e2c08d88 | -14.04459 | -52.06341 | 2026-09-22 05:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 282a3197-d5af-3b3d-8381-578d6acc29b8 | -10.60218 | -53.9826 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 26b187a0-d3bf-3feb-94d9-62df9dbd47e4 | -10.89704 | -53.97339 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 978a66c4-3bc5-3e43-85ab-045a0763db6b | -9.40117 | -65.92193 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43178705-c4ce-3248-b608-60ccad533a07 | -8.72308 | -67.08376 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e4b6aea-8d66-3d69-bc6d-005a1e36e00d | -7.96801 | -71.34268 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9242f3d1-553b-3a3a-8066-9823321724e8 | -9.1292 | -58.88641 | 2026-09-22 05:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20d28dc7-4581-3bd8-bf19-f8d54f33605d | -9.40811 | -68.37939 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c25c0530-d4a5-3774-89ae-b182e650daf2 | -9.55921 | -66.04467 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 927051ab-880e-3c49-9056-50538bf3d1a5 | -10.22683 | -68.7523 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a60b3fbc-2245-30b4-9c5f-bc9878bd832d | -9.80503 | -68.1321 | 2026-09-22 05:44:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49876fc3-a45b-311d-bf29-f079a318f7ac | -10.47045 | -69.19571 | 2026-09-22 05:44:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2841453c-f2ba-3f5e-bf78-26e96c1e75d2 | -10.45545 | -51.27545 | 2026-09-22 05:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72ddf4fe-d45d-34cc-bdcb-7bc9e6a333e9 | -12.14373 | -61.17134 | 2026-09-22 05:44:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e97c3b2-6859-35b8-8cbe-8a615999a483 | -9.55862 | -66.04829 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 242fb2c2-b1e0-32cf-afe6-2fb6c7f7f79d | -13.52378 | -51.5018 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2fc4bcdb-1974-3524-bd72-701339a12baf | -9.28163 | -60.61587 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 590ae84b-abc0-3f86-b75b-9dfaceec18af | -10.61842 | -68.80228 | 2026-09-22 05:44:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90199c4a-f06c-3e1f-b38e-f76e7b4f6822 | -10.2276 | -68.74771 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ce1b249-74a9-376c-a283-a9e1e2b50c6a | -9.1883 | -65.8508 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 186e04ce-31b3-390b-a3c2-1302d79bd249 | -10.24412 | -68.74354 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67089911-5682-37e6-84b3-563b12c201a4 | -9.46716 | -65.39243 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ae4781b-8176-381b-824c-e104dc8c2097 | -9.69942 | -64.91568 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80cb714e-2518-3a92-ac32-4273b081b999 | -13.51661 | -51.50105 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 9f7aa670-c91b-3434-af82-f1cbe7f1139f | -9.6654 | -54.33879 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abefc482-7224-35cd-b2a4-1e0ab0234148 | -9.47753 | -68.02768 | 2026-09-22 05:44:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b8c1d33-4eb2-3a5e-9712-58802349c503 | -9.36915 | -68.65758 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65e9c60a-03ff-377d-9ec2-aca4b4e8e61a | -12.7887 | -54.04037 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41c215a0-17bb-3568-bd42-986e0d91e3da | -9.40454 | -65.92246 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17c4d881-b815-3da0-958c-0a97b2deead2 | -9.12479 | -65.87018 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebe9c723-5740-3729-9a67-a00d728149e4 | -7.92971 | -71.34914 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4183c41f-27ff-3f77-8cf9-17bcdc930ffd | -8.00233 | -71.30923 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4913d41-1f30-3225-a8db-230857bf0859 | -9.29736 | -67.53482 | 2026-09-22 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50f0215c-28ac-3329-8c84-408815e03b7f | -9.09859 | -65.37912 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56543dc2-368d-381d-8049-8e1d3c01ab48 | -9.56038 | -66.03742 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69bfaf73-b15a-3ea8-9e5b-74191f4f2fef | -10.60272 | -53.97819 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d69158e4-dc7c-3ed6-9fdf-1bdecc8a1d29 | -9.54851 | -66.0466 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b9a4e7c-29ca-3970-8576-85cdbd2ea23d | -10.93069 | -58.33494 | 2026-09-22 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b835a6b-9cb8-3036-af82-f103b7f59632 | -9.55584 | -66.04412 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc95984e-a912-37cd-9711-3aa90db08b96 | -10.61303 | -53.99279 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0d3f2efc-cdce-3fc4-acdf-b6887c60188a | -9.69611 | -64.91515 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e314a781-8ed8-3a61-8f9f-49e950968e8f | -7.85602 | -70.5914 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4232b27-eb93-3a21-b40c-3a176dc4e6d8 | -9.5677 | -66.0349 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 057cab4e-eb65-3357-9a18-537bd639d81d | -9.67688 | -54.34058 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0896b472-d643-3231-9501-3a0047e60288 | -7.85526 | -70.59573 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c861f017-d694-3a3f-baf0-1506b6c4aef8 | -8.76627 | -69.47066 | 2026-09-22 05:44:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0491ae60-2d80-3fe7-99b4-c230ae273d74 | -9.67106 | -66.82533 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f6291d3-b30d-3b31-af4e-38db5c2076a0 | -10.15476 | -58.76344 | 2026-09-22 05:44:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d93289a-7756-3601-9771-35943a5cd59d | -9.2934 | -58.91708 | 2026-09-22 05:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad90574-03be-3255-a577-2c8b7f7a81dd | -10.46661 | -69.19504 | 2026-09-22 05:44:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e37b2ef2-a0eb-32ac-b263-ff2e2c30b02f | -10.60164 | -53.98697 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9f56dbfc-4c32-3d61-b1e0-4d93801e36f3 | -9.80869 | -68.13272 | 2026-09-22 05:44:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0982728-a3ab-396c-a3d4-3d81f4f862e7 | -10.25081 | -68.29132 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3da90d52-e706-3b22-9f1f-58c67e71e19e | -7.92488 | -71.34483 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87d83c98-7b27-3856-b400-000f2278a4a6 | -11.15198 | -51.10885 | 2026-09-22 05:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README118.md)
