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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1cd399c-4bb9-3be7-b294-ea81c54796d5 | -21.0137 | -49.9988 | 2025-09-25 01:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| 5b01cc4f-eeaa-3329-b818-f19a5138a530 | -21.0131 | -50.0217 | 2025-09-25 01:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 55d1a7ae-c9e9-3fb9-9390-69dff7c4199a | -6.4317 | -43.0942 | 2025-09-25 01:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 209.7 |
| b5d9566d-53a5-378c-bd58-9482b88bb11f | -17.9312 | -55.8548 | 2025-09-25 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| f16ac985-edf4-3c1a-acdb-3545865916d1 | -6.4129 | -43.0958 | 2025-09-25 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 47c846a0-4c2e-383f-b687-d95716ce105a | -20.972 | -50.0305 | 2025-09-25 01:30:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 01c3e216-3f2f-3a2c-85de-c43354eab986 | -23.7004 | -51.7001 | 2025-09-25 01:30:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| 7bd2912c-1eb2-37f4-9211-8e64d6386868 | -9.7241 | -35.9991 | 2025-09-25 01:30:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 4c923778-d702-3d4b-b5ea-00697538d37f | -4.7974 | -43.5435 | 2025-09-25 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 1f5113cd-2279-3e40-8254-fc55252fccc2 | -2.9291 | -48.3181 | 2025-09-25 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 08387368-d801-300e-a9e2-76de915f544f | -6.4131 | -43.0724 | 2025-09-25 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 5a376e97-e788-397b-ade2-dea0d6f8c3c1 | -20.9925 | -50.0261 | 2025-09-25 01:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 234.7 |
| 03dca95e-cbef-3d64-af1b-2c6c6ea46309 | -4.8161 | -43.5423 | 2025-09-25 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ebeba1fe-5500-3c4c-b6c5-60f60aff86cf | -17.951 | -55.8522 | 2025-09-25 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 34b08891-b6fc-34c8-91f3-567a1e0e75a1 | -20.7127 | -57.8531 | 2025-09-25 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 9e872814-b319-3bc0-8552-fbd695b83c87 | -13.8345 | -45.6173 | 2025-09-25 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d88ce9a8-6b11-35e4-816a-be295b33d753 | -4.7976 | -43.5203 | 2025-09-25 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 82062238-d2f9-364a-9373-2b593b4ffcc6 | -22.0603 | -48.609 | 2025-09-25 01:30:00 | GOES-19 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 8c607d16-3f6c-33a8-a24a-b636cb7bcff1 | -13.8539 | -45.614 | 2025-09-25 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c08d8c60-609f-3ef9-a857-fa7ebba3f43e | -6.4319 | -43.0707 | 2025-09-25 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 65799aea-4e51-326f-97a1-92d68c72d74a | -20.9931 | -50.0032 | 2025-09-25 01:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 198.3 |
| bc6c3f8c-87af-3238-af66-77d61f6e5875 | -20.972 | -50.0305 | 2025-09-25 01:40:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| 2d140dc3-0916-33b0-9635-1d2598734323 | -17.9312 | -55.8548 | 2025-09-25 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| c5966027-e543-3db2-bef4-41bb141ac896 | -6.4131 | -43.0724 | 2025-09-25 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 2ed36e79-4370-32a8-914c-4239c90b0694 | -2.9291 | -48.3181 | 2025-09-25 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2c89a3a8-3e71-3b0e-b7d0-e6a2ac9013df | -13.8345 | -45.6173 | 2025-09-25 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fcb0cb6b-4948-3663-935c-b3c9a267852b | -6.4129 | -43.0958 | 2025-09-25 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 86058d7e-646f-3cd7-b6ee-b983a1ea3790 | -20.9925 | -50.0261 | 2025-09-25 01:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 336.4 |
| 233d4fed-90a8-3151-a8ae-dd0706797ae3 | -22.0603 | -48.609 | 2025-09-25 01:40:00 | GOES-19 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b849e018-12fe-3431-9f2a-c14be51677f7 | -4.7976 | -43.5203 | 2025-09-25 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ace949f9-a72e-34f0-b7fa-b918f413739e | -4.8161 | -43.5423 | 2025-09-25 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 7d5b81c5-f525-3718-864b-7cb955c15427 | -4.7974 | -43.5435 | 2025-09-25 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| ee7e4141-254a-35ad-9dd3-a039517ca511 | -20.9931 | -50.0032 | 2025-09-25 01:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 254.8 |
| 1b3c57b1-e27b-3f5e-8588-caa096b31bc6 | -21.0137 | -49.9988 | 2025-09-25 01:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| a73e5d0a-c658-3b5b-8dac-561ded6d617b | -6.4319 | -43.0707 | 2025-09-25 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 106e7166-5072-300c-b4ac-23ce222a3367 | -17.951 | -55.8522 | 2025-09-25 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.1 |
| daea4c9c-693c-367a-81fe-fa9c854f2c89 | -21.0131 | -50.0217 | 2025-09-25 01:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| 66d67094-b00e-3fa0-9363-00c0c0f90f62 | -23.7004 | -51.7001 | 2025-09-25 01:40:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| 8cca1461-f507-355a-afa3-732263e2b678 | -6.4317 | -43.0942 | 2025-09-25 01:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 5cf36eb8-3c28-318a-ad29-e3c7f842d85a | -13.8539 | -45.614 | 2025-09-25 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a10619f1-e803-36e4-ba92-9d21ce71fe7a | -4.7974 | -43.5435 | 2025-09-25 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 4489e4b4-c4d3-3d28-912a-6d55e5c6ba7e | -6.4129 | -43.0958 | 2025-09-25 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 8d5e7aca-437f-3ba6-9851-4f0c405470f0 | -6.4317 | -43.0942 | 2025-09-25 01:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 6a5cd65b-adf2-375a-8bc6-f803c1f8d17b | -6.4319 | -43.0707 | 2025-09-25 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| be950bea-4d2e-3a8d-92f1-6da32b173595 | -6.4131 | -43.0724 | 2025-09-25 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| fa98bf28-3063-3cd3-bb93-b1d4c7a3375f | -4.8161 | -43.5423 | 2025-09-25 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b6f1a2b4-024d-308e-b717-95627964337f | -13.8345 | -45.6173 | 2025-09-25 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| d76da337-abdc-3625-b63d-de3e20610e49 | -21.0131 | -50.0217 | 2025-09-25 02:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| b1ddb12e-2639-3078-8128-9bacb885f12e | -20.972 | -50.0305 | 2025-09-25 02:00:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 304.2 |
| edb6baec-2bb9-3b42-ac2d-0056b7625d4d | -20.9726 | -50.0077 | 2025-09-25 02:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 141.2 |
| 4495b7c7-2a2a-33d2-92be-5e1a47860825 | -4.7974 | -43.5435 | 2025-09-25 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| bc8a3a8f-3a33-37c6-b58f-945e979092fe | -6.4131 | -43.0724 | 2025-09-25 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b7a1a1df-4a88-3b20-824d-a78111849ca8 | -21.9721 | -49.5102 | 2025-09-25 02:00:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.0 |
| be5ac944-736a-304b-9e00-b855bd1d6e6f | -20.9925 | -50.0261 | 2025-09-25 02:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 426.2 |
| e749ada3-70d9-370a-93be-6ec773167dae | -5.0091 | -45.1792 | 2025-09-25 02:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 0c04d2ba-26a5-3983-a714-66239e5222f9 | -21.0137 | -49.9988 | 2025-09-25 02:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 27682a54-94c2-3ad3-9cbe-58a411bd0173 | -6.4129 | -43.0958 | 2025-09-25 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| c9546959-a677-3850-9b0a-5fa4f5f7e1aa | -20.9931 | -50.0032 | 2025-09-25 02:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 308.7 |
| b4eef57b-f0ad-3524-92ce-4f2efa1221d8 | -21.9929 | -49.5054 | 2025-09-25 02:00:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| 67c8a3f5-e2cb-3c14-8a09-2b800397a20e | -2.9291 | -48.3181 | 2025-09-25 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3623e59d-22a7-3071-b841-f80791c20f00 | -6.4319 | -43.0707 | 2025-09-25 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 5877f452-0c26-3c7c-95a3-4181ae110ab2 | -17.9312 | -55.8548 | 2025-09-25 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| c2720fd7-ff13-3a90-a332-74860433e2d3 | -6.4317 | -43.0942 | 2025-09-25 02:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 175.8 |
| ee78e6ee-bd2c-3ce8-999b-ffd4365c008c | -4.8161 | -43.5423 | 2025-09-25 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ead4a83d-6d5e-34c9-a784-90d1c75d602f | -10.57297 | -69.18228 | 2025-09-25 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ad11e4f0-9ac0-3215-8cb4-9e4d1bb79f75 | -10.72033 | -69.48061 | 2025-09-25 02:09:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9874be81-f52b-316c-aab1-a90427bdb8c9 | -6.4319 | -43.0707 | 2025-09-25 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 2223fe00-320c-34db-b78a-02a2cda19754 | -20.9726 | -50.0077 | 2025-09-25 02:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| 8e55c439-8e09-3cd5-9d0f-69d523843845 | -4.8011 | -43.054 | 2025-09-25 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1707a5cc-4e2d-34e1-af88-08f4920775a2 | -20.9925 | -50.0261 | 2025-09-25 02:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 346.4 |
| d543d76e-2384-36b3-af62-dd48be17ee53 | -21.9721 | -49.5102 | 2025-09-25 02:10:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| 226788cb-0f56-33fe-85d7-bbfabb4d1ead | -13.8345 | -45.6173 | 2025-09-25 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7f778ab8-9d19-354f-b9de-792247e31182 | -6.4317 | -43.0942 | 2025-09-25 02:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 3ba9e46d-2fc2-3dba-a4a7-2d948ce7da30 | -4.8013 | -43.0306 | 2025-09-25 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| a1f25764-9c5e-32f8-aef5-85293ad0e607 | -21.0137 | -49.9988 | 2025-09-25 02:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 0a2c7625-a08a-3795-8b9a-577ca1090bda | -4.7826 | -43.0318 | 2025-09-25 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 45a09462-6bfd-329a-913f-8ce5d870ffe3 | -21.9929 | -49.5054 | 2025-09-25 02:10:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| 8592b59e-a1b0-33ec-8e47-b1e2c8af08d3 | -21.0131 | -50.0217 | 2025-09-25 02:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.9 |
| 97069c20-a5ab-3cd7-a66c-3fa12a5d74f1 | -20.9931 | -50.0032 | 2025-09-25 02:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 259.9 |
| ce6290ee-b8e8-3168-b2a9-40de5ec3bc9a | -6.4129 | -43.0958 | 2025-09-25 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8cf32549-811d-3f45-8cd9-158dcc8e6209 | -2.9291 | -48.3181 | 2025-09-25 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ca49b652-76d8-3d63-87a5-365198cd2e3f | -4.7974 | -43.5435 | 2025-09-25 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| dbe0e019-e4ae-396f-9eac-5d26fdfa45a5 | -20.972 | -50.0305 | 2025-09-25 02:10:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.9 |
| 3fa9067b-152a-342c-8282-fce841ac8999 | -6.4131 | -43.0724 | 2025-09-25 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| f97f2b8b-51d9-3275-8879-81c77021e984 | -6.4319 | -43.0707 | 2025-09-25 02:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 0c446ebd-d298-399f-8253-59720246a0ed | -17.951 | -55.8522 | 2025-09-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 0d472531-b5e8-3983-aa2a-0d9bb3fea044 | -2.9291 | -48.3181 | 2025-09-25 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f93dc8db-0f26-3a7a-9b1c-faf045bfe032 | -17.9312 | -55.8548 | 2025-09-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.8 |
| b248fcca-d5b4-37b8-ae91-f085fd99d15d | -21.9721 | -49.5102 | 2025-09-25 02:20:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.3 |
| 1398b123-73ac-3c6a-8d0d-9d1e736da434 | -13.8345 | -45.6173 | 2025-09-25 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 98e80085-0272-3c8a-b8ce-50f56a60fc27 | -17.9308 | -55.8758 | 2025-09-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 4dd8e187-08d2-3d2d-9841-9c838bd09258 | -2.9291 | -48.2966 | 2025-09-25 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0733f28c-ecb9-3ac0-8161-bff914a26a69 | -21.9929 | -49.5054 | 2025-09-25 02:20:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| 8d16b97c-fd9e-3486-b3ee-cb349211b0e7 | -6.4131 | -43.0724 | 2025-09-25 02:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 06155498-6477-32bc-8e49-21c41184c168 | -6.4129 | -43.0958 | 2025-09-25 02:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 382b37de-3f3d-343e-8fc3-9022e380ac95 | -17.9506 | -55.8731 | 2025-09-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 0c97f9d4-c389-3255-bc3b-db62b2241426 | -6.4317 | -43.0942 | 2025-09-25 02:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 07b75074-02d7-36dd-88f2-4682cd2226d2 | -21.9929 | -49.5054 | 2025-09-25 02:30:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.3 |
| a27b214c-d0d9-30fb-bba7-a79154aed1da | -21.9721 | -49.5102 | 2025-09-25 02:30:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.7 |
| 19598c86-904c-3503-a54f-c8443e48ac7b | -6.4319 | -43.0707 | 2025-09-25 02:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |


[Clique aqui para ver as próximas entradas](README6.md)
