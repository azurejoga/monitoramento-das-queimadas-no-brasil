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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f167768-a924-372a-b8bf-e0d5a53b050c | -11.73497 | -64.96666 | 2025-10-13 04:46:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a4c3baf-1a68-3c32-a02a-1b88afc288ad | -13.84658 | -45.54737 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84bfd1bd-998e-367a-8814-634cebb02d20 | -16.12252 | -53.97668 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8494a902-5745-3b33-af63-84d5cbfc83f5 | -12.76776 | -50.67421 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d6d0b0c-6e74-37e8-bdb1-a93a27a7ea17 | -12.98624 | -51.81803 | 2025-10-13 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31800527-c8ed-33c2-90ba-91b63f19e7a5 | -15.66494 | -43.90485 | 2025-10-13 04:46:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f682cf-2a8f-37e0-8d89-109674147447 | -13.88226 | -45.48633 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad6b5788-d31e-3d20-970c-e56e0c834d8c | -13.80469 | -52.7891 | 2025-10-13 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13861d21-3267-368d-a0fd-de33e4d38f7f | -17.32211 | -53.80584 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d5cc155-42a8-37c9-a1cc-cbab0749ca7e | -14.19032 | -51.51418 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9011efb3-46fe-35af-bf88-58b99e7d5da1 | -17.33105 | -53.79252 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d146d1b-d532-31f4-8b22-9ff57db5e88f | -13.51296 | -51.30319 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7145019-0133-32ca-a4f7-1a64fb07999a | -11.66181 | -47.5531 | 2025-10-13 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53bc0887-2354-3234-ab6c-791df1da1354 | -12.77737 | -50.67951 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb7c6b1f-fd51-390a-83ff-34eada908281 | -12.7672 | -50.67791 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 377a2106-65f5-369c-a798-5e7279863e44 | -16.21468 | -59.13083 | 2025-10-13 04:46:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b9edfa28-f0eb-3610-b341-828411eade9a | -13.49472 | -51.29684 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ae16431-f70a-3121-b6ab-6b01510105e6 | -14.27244 | -51.50816 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a20bcb54-3353-30dc-bf17-b4112bb690ea | -11.72838 | -64.96522 | 2025-10-13 04:46:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 196c4589-c20e-39ce-8f30-853ef5876b67 | -17.33263 | -53.80394 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf1e9bd0-b013-328b-bbb6-341fb61a9f0e | -11.73713 | -54.72182 | 2025-10-13 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe86a331-508c-3d62-bacf-684b3898ede2 | -16.12427 | -53.96577 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6233b7d1-4bb9-3cbd-8636-f8e92d1b52eb | -14.29869 | -51.53844 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a8506ee-16de-3cf6-b1ea-3f06aca84c84 | -13.24287 | -47.77184 | 2025-10-13 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8457c8b6-76f7-3979-ade9-1da8671141b5 | -9.66512 | -62.51719 | 2025-10-13 04:46:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d95e4491-389c-325e-8052-939929810733 | -14.27472 | -51.56062 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71db9981-f3b8-3af6-a90f-f8e70f4de901 | -13.86321 | -45.49117 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28474f5a-fcca-38ca-86c7-aeb8c7b30802 | -13.33709 | -47.6414 | 2025-10-13 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04285e5e-b34b-3dd9-af27-790047e2de96 | -14.29088 | -51.54463 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a20f1ff-754f-3df9-98c3-4595b80734f5 | -14.27137 | -51.56009 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccb03059-027d-3a2e-993d-6ac9710ff95f | -16.11919 | -53.9761 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 53305cb9-c732-3b85-94bb-a170391e4e09 | -17.33378 | -53.7967 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a75bf7fe-106a-3981-8566-5f563369ce70 | -17.33148 | -53.81119 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13e022c6-5ca2-3139-9004-783ac02f1349 | -17.3371 | -53.79728 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95fe080a-0883-37c6-a76c-a9bff9ce1310 | -15.56893 | -47.90919 | 2025-10-13 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a2acbf-e751-3cd3-bac0-bb56424c926d | -14.24792 | -51.534 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a39da15-4d92-32b5-acd6-da66f6ef150e | -14.31096 | -51.54786 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b643a1e2-3d2c-34d6-9409-33029cbb9173 | -13.86444 | -45.48171 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ea2ce17-3fb9-341c-b963-39be4e3f179d | -16.21375 | -59.13307 | 2025-10-13 04:46:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cffb868b-bbbb-3cb9-8883-4adf6d8a14e0 | -17.33537 | -53.80814 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91080bfb-0517-33b2-9c35-73582c858ac2 | -11.74064 | -54.72242 | 2025-10-13 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bd4da92-5a40-3fb3-a016-8bd2a0286149 | -12.76437 | -50.67367 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5acfecaa-3341-34eb-8b0e-7423dfa3d51a | -15.79574 | -42.51378 | 2025-10-13 04:46:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b628a24a-42d1-3ffd-a148-42e425eaf4a3 | -17.32154 | -53.80945 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 516e9665-2f8b-36f4-b8d9-a7db5cee4f9e | -12.15827 | -53.62794 | 2025-10-13 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99b5ca61-bc35-3e40-959f-7ca5a49c1b89 | -12.75476 | -50.66837 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb7cf374-95b9-3f13-b871-c7af609b9424 | -17.32716 | -53.79556 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c509b2dc-ea85-3b5e-bf5f-2bb0fe2ebf4d | -14.2596 | -51.50238 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4f20e30-053e-34ec-a483-6f3a56959cf9 | -15.62706 | -56.02819 | 2025-10-13 04:46:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9317e38-b370-31f6-bbee-a889c4660453 | -13.85153 | -45.50923 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c8fd2e1-7ffb-3239-b0a7-1080a9f93df0 | -13.8472 | -45.54259 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3fd007f-1aae-3b60-855b-3dde61010820 | -15.80151 | -42.51419 | 2025-10-13 04:46:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47b2db60-b62f-317c-acfb-131eff595722 | -17.33926 | -53.80509 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b9d9e33-41fe-3db2-bad9-8dc9b6f0621e | -17.32874 | -53.80699 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a46bd3b7-c8dd-37eb-bba2-ad790e4f745b | -13.80413 | -52.79264 | 2025-10-13 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3303e5d-91e2-36bd-8c7e-fc57eba1aa85 | -16.12369 | -53.96941 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 48ba3500-fc23-3cb0-9034-00123292b520 | -9.8159 | -62.19729 | 2025-10-13 04:46:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bba59f9-d777-3233-b502-69d68ec78b50 | -11.59999 | -47.51376 | 2025-10-13 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2871386c-9ed0-3525-8c60-e8a9a49fe477 | -14.19311 | -51.51834 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0265fb0-9328-38c9-83da-5aca2b8c1f6c | -14.24513 | -51.52983 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cfebb2d-01b3-37d9-8c8b-9e534a62fc80 | -15.02594 | -48.7487 | 2025-10-13 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4dc0e44-154d-384b-bbb6-8a80b005d624 | -13.78758 | -52.78988 | 2025-10-13 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b46b5324-592c-3680-a9fc-f88b7736c288 | -14.24506 | -51.48514 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 542c6ebd-778b-31ca-97b0-63a783203695 | -14.30482 | -51.54314 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91089451-615e-3f79-bfee-7b4df148ef88 | -14.24841 | -51.48568 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a2ccf28-8c30-3ef9-b8fd-dbf9a8ffdcff | -14.29478 | -51.54153 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ce6e56b-b41f-340f-9a35-700348250c0c | -14.29813 | -51.54207 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68b060ec-1a71-325d-a77d-786abfff2053 | -15.85714 | -56.76315 | 2025-10-13 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c7e6019-c200-3df1-89c0-579443ae8c54 | -15.02527 | -48.75351 | 2025-10-13 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c1acd97-9f75-38a5-940f-1a601df422d9 | -11.74416 | -54.72303 | 2025-10-13 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17127ebf-2a27-38b4-91e9-8be9715a914f | -13.88286 | -45.48151 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ba5f794-2ff7-3aa6-ab1d-005c72841145 | -16.35126 | -42.38602 | 2025-10-13 04:46:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70c25a73-cbbb-3f4e-9b40-2f9d4cd18469 | -16.97849 | -55.97926 | 2025-10-13 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 141f13f4-e49a-3ae0-b8b8-ef393eca4032 | -10.97864 | -59.01974 | 2025-10-13 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 774d1ee8-249d-3955-aa3d-a2935bbf2d94 | -11.66576 | -47.55973 | 2025-10-13 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10584b61-5118-33ba-97f8-975e92813490 | -17.33983 | -53.80148 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f7c9eee-7d63-3f8f-9379-89a758685697 | -17.3299 | -53.79974 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a265d00-2759-3641-892d-dc4d20f72a0c | -14.19255 | -51.49965 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a69a713f-dc26-3670-8c81-9b0f88f4a3dd | -14.25351 | -51.54234 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4792f4e-0433-35d2-8a86-b3457adc52a7 | -14.24009 | -51.51786 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 418346f2-83e8-3266-ba6e-bfcc77fa0fb3 | -11.13988 | -51.26871 | 2025-10-13 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97684bbc-0290-3321-9435-12efe9e1b003 | -14.23674 | -51.51732 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07ad853d-9b15-3d10-b226-267cc3c3987a | -13.82531 | -45.49568 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 629f1ada-a6fc-3b52-b839-56b4779bef25 | -14.23954 | -51.52149 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cd5efd9-683b-363b-95c8-69cd5ae950fe | -9.67103 | -62.51832 | 2025-10-13 04:46:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34a62eb4-7aee-331a-849c-1e0b5ea016da | -9.81669 | -62.19315 | 2025-10-13 04:46:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 532105e1-8d2d-3dc7-aca7-52bb5c4b5d8f | -13.27257 | -47.79004 | 2025-10-13 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a203e39-d932-395d-ab97-513291dd91d3 | -15.8469 | -56.75631 | 2025-10-13 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00c2f29b-4bcd-38bc-bbdc-a21529d98bf6 | -17.33652 | -53.8009 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dde2b12c-8cad-3c1f-a12e-3eede53d90c5 | -16.11977 | -53.97247 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c3005a5b-8019-36f2-84b1-d746453268ac | -14.30148 | -51.54261 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a582c075-9d44-387d-9cad-98fe550309fa | -16.2023 | -57.58423 | 2025-10-13 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d41a0990-69fe-3bf9-b0f2-b7ac73599fce | -14.2563 | -51.5465 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c78a1854-d89c-3439-9fb5-ab41d9214829 | -17.33868 | -53.80872 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bcd0315-7470-34ea-a015-3efb8ff4f5b4 | -12.98956 | -51.81856 | 2025-10-13 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5593ea16-6265-3076-acf8-410e05eb842a | -15.65972 | -43.90405 | 2025-10-13 04:46:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0abd5d3-aa2e-3241-981b-825d2686b7e2 | -17.32485 | -53.81003 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dea3123-13ab-30d0-8049-367f0d2b4f03 | -18.37516 | -46.73002 | 2025-10-13 04:46:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ec6e65c-7bf9-3188-bcb5-f9eaae7bf970 | -14.21988 | -51.52264 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9941868f-5bce-304b-b8e4-4565d13c1c76 | -14.29534 | -51.5379 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
