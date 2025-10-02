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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6c1d8b9-51f1-3dda-b602-49a0997c1122 | -22.27714 | -46.73643 | 2025-10-02 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| c433a50c-4111-3bf1-9bbf-a8d6299d255e | -20.42426 | -48.86046 | 2025-10-02 04:06:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd7c3834-558b-366a-9aaa-15d4352a7590 | -21.57883 | -44.95971 | 2025-10-02 04:06:00 | NOAA-21 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 883474f2-d292-3708-84bf-3300065930e7 | -20.84847 | -49.43003 | 2025-10-02 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9fc47ee0-1382-3166-b38b-ee7ba8eb3de7 | -22.5275 | -44.78703 | 2025-10-02 04:06:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d9fef53d-f074-37c5-bd94-79295995b01d | -22.27638 | -46.74077 | 2025-10-02 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 07bba9b3-8695-3c05-aded-5ff479eab1e4 | -21.68817 | -45.61145 | 2025-10-02 04:06:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b95ebe9d-f891-3c01-bd19-d4d54cf50bfb | -22.08066 | -43.08746 | 2025-10-02 04:06:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc069668-2133-349c-888c-25012424d5f5 | -21.31701 | -46.8472 | 2025-10-02 04:06:00 | NOAA-21 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 77939ff7-f093-39a8-91c3-616b0645cc12 | -22.47411 | -44.52534 | 2025-10-02 04:06:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 359ed853-847b-35e9-825a-56cf9116dd26 | -22.31704 | -49.59204 | 2025-10-02 04:06:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c06b3047-1303-3504-bdfd-406761665a31 | -21.66554 | -48.79274 | 2025-10-02 04:06:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 9b3977f0-323b-3890-bc32-2c8da18896a9 | -20.84431 | -49.42908 | 2025-10-02 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.3 |
| 70a7cddb-893f-36d5-8002-fa94b9314cc3 | -21.16139 | -45.62497 | 2025-10-02 04:06:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 540e7799-d7f1-3779-a6b7-2c86cd8a07cd | -20.42351 | -48.86436 | 2025-10-02 04:06:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c334d5ff-1750-33ef-8c90-8e5e353b301d | -22.28371 | -46.71973 | 2025-10-02 04:06:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 19a972d8-1136-3167-85a9-3974b8c3717f | -22.94521 | -43.39086 | 2025-10-02 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4187648d-40fa-3c25-93b1-5046c9988f31 | -22.72851 | -47.19157 | 2025-10-02 04:06:00 | NOAA-21 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1737ef77-5dac-3b9c-b8a6-cc18171d3495 | -22.61979 | -44.50984 | 2025-10-02 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f1890129-18a1-3aac-8410-8b2c6d795fca | -20.84802 | -49.4768 | 2025-10-02 04:06:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39d78be3-8e9a-3b32-bd7d-4ee675c0a084 | -22.52418 | -44.7864 | 2025-10-02 04:06:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 73cdc136-d5fb-33af-91a2-d827f540fc6a | -22.56327 | -46.78622 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| afe5af62-e8f2-3b44-852a-17519eb11b99 | -22.57183 | -46.77901 | 2025-10-02 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7f1f9b59-1a4e-3ae6-b058-4300c96e9076 | -22.6249 | -44.49926 | 2025-10-02 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f534cbcd-7981-3e70-bf39-e964ea0ccd15 | -10.9949 | -46.6094 | 2025-10-02 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f1370fd9-a61c-3b90-8074-2115dd116228 | -9.9182 | -43.7212 | 2025-10-02 04:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 126.5 |
| 01a73c9b-32b8-3ec4-b25d-8d862f3b1405 | -14.3114 | -45.9967 | 2025-10-02 04:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3e3eae3a-3881-3000-8c17-9d1afb552a5d | -9.9372 | -43.7187 | 2025-10-02 04:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 253.3 |
| 94715c26-65ac-3839-8e07-8d876c6d4d82 | -17.1698 | -47.029 | 2025-10-02 04:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| d49cfe74-03c4-3473-bdb9-c2aa3ed9817e | -21.6834 | -48.7921 | 2025-10-02 04:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f5e07d8a-9c01-357b-bc72-754607010028 | -11.175 | -47.2581 | 2025-10-02 04:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 686cc3b7-0e04-304a-a389-2558143ad89e | -21.6626 | -48.797 | 2025-10-02 04:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 157.2 |
| cdb3010e-81ba-302d-af2f-9d5157963ca6 | -11.0144 | -46.5844 | 2025-10-02 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7cfdf738-bf5d-32ad-ba43-21cf01468c98 | -13.4248 | -47.7945 | 2025-10-02 04:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3aed5fb4-3903-3bda-9dcf-e0512b0a7d56 | -11.1746 | -47.2805 | 2025-10-02 04:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| db700000-6b3a-32ab-9990-2e6a6149276f | -14.4753 | -48.436 | 2025-10-02 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ac14165b-ba10-3266-bb92-3d2592c65b6e | -10.9953 | -46.5869 | 2025-10-02 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 142.2 |
| eb18e461-270a-3253-aafc-8446630c63f3 | -9.9178 | -43.7447 | 2025-10-02 04:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| 727e55fa-f501-31e2-b9b1-880dfceb1a01 | -16.0221 | -50.8989 | 2025-10-02 04:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| d6deb8e6-e235-3486-a57f-539e004a9489 | -16.0029 | -50.8801 | 2025-10-02 04:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| d1719547-b89d-3b9b-b252-77b4ee2c9f5f | -14.4757 | -48.4137 | 2025-10-02 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| cebd231a-c296-3bb2-9000-f904844537a5 | -16.0025 | -50.902 | 2025-10-02 04:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 3953a62c-54f5-38af-b881-d84df8dcb47e | -13.8156 | -47.5332 | 2025-10-02 04:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e4e2cfbb-2e05-32ba-a3d2-3b725ca58ee6 | -16.0426 | -50.8522 | 2025-10-02 04:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| d09d72bc-22bd-3b29-afee-22e239ad1617 | -9.9369 | -43.7422 | 2025-10-02 04:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 310.5 |
| 32f2fa6f-45ec-3798-93af-690ab23b77e1 | -13.9585 | -48.1376 | 2025-10-02 04:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 08c533f5-0f33-3684-b699-d2a8c6b3f43e | -9.9365 | -43.7657 | 2025-10-02 04:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 9e10cde8-c492-37b4-954d-66fee390a40c | -14.4757 | -48.4137 | 2025-10-02 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6c0f8d36-21df-3bbd-a989-c16ea7addeb4 | -10.8428 | -46.6064 | 2025-10-02 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c0d6bcd9-3ca0-31f8-9313-63024b2b77f0 | -10.8237 | -46.6088 | 2025-10-02 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b4330b6d-5f2e-3dcc-ab9b-a918423e71c2 | -13.959 | -48.1152 | 2025-10-02 04:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 17fb3c83-bd5c-3c08-9aba-82923b91709e | -10.2031 | -50.2681 | 2025-10-02 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e02434fc-37c0-3314-8e37-147dbefed146 | -11.1746 | -47.2805 | 2025-10-02 04:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 08550731-52a6-3542-b95d-0c8f48107aa1 | -13.4248 | -47.7945 | 2025-10-02 04:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 7ca0c9b4-4dc3-3253-9366-08d5c2549fcf | -20.8455 | -49.4202 | 2025-10-02 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.0 |
| cc71949a-1b41-3d15-8cb8-a4dc3069481d | -10.9953 | -46.5869 | 2025-10-02 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| cc583b34-768e-3760-9d69-ccb3aa50116f | -17.1698 | -47.029 | 2025-10-02 04:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| bda63848-526f-3e73-9338-8d29fa25d4c5 | -10.8424 | -46.6289 | 2025-10-02 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 5c073e71-9aac-3aaf-9ed9-059829b690dc | -11.175 | -47.2581 | 2025-10-02 04:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 5fdb2cf2-51be-310d-863b-ec1cde562d03 | -14.4753 | -48.436 | 2025-10-02 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a30acd47-b0c3-3de2-98a7-757e9af7b654 | -16.0025 | -50.902 | 2025-10-02 04:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| cfefa69f-08b8-338d-a6af-34f8fd7b3bc8 | -3.87401 | -42.51967 | 2025-10-02 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ec5ef9b1-5134-317c-8f6f-c9c81a1264be | -5.6409 | -45.96599 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 945dd26c-9e84-3fbb-a036-467d233bb439 | -5.23081 | -43.7757 | 2025-10-02 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e827b381-924e-3fd8-88a1-820750f638cb | -5.18154 | -41.24153 | 2025-10-02 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4c86a3e8-009a-39c7-810b-c4226e205d2b | -5.33374 | -43.76407 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cfe80b89-7cd4-3a3a-9e2f-f2177ae1adc4 | -5.61428 | -43.24335 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 48e63c98-a248-3b55-abf5-83b937fcc6b7 | -3.62501 | -42.77604 | 2025-10-02 04:27:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a42a5c4f-9f37-309b-9a7a-0e79929b3f1a | -5.87125 | -44.80178 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75f4e3c8-2937-30ef-a52b-d23d70f73d83 | -5.49877 | -42.72501 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a0a243b7-52c5-3143-8377-343a8d9ba94a | -3.35446 | -43.1896 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65a0b92e-bcec-305a-bb7d-7e58c499390e | -6.11565 | -43.12448 | 2025-10-02 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc7297f3-1b0b-3759-917e-faa756a5351c | -5.33781 | -43.76077 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 900e8213-6d02-3ef6-9d51-8c065a49d8a7 | -2.2447 | -47.88997 | 2025-10-02 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc4c9cb4-4ee7-360a-b672-8303cf7f20a1 | -3.6892 | -49.05174 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7403a9de-f6f0-3de2-9102-93abce426664 | -3.81425 | -47.5887 | 2025-10-02 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2bd76e5-d4c7-353e-92f1-f79e986e6fc2 | -5.99363 | -44.57469 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b2a9c3d-e75f-31e6-93a8-fc81d3081d9e | -2.96043 | -48.59571 | 2025-10-02 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c3f15ee-ae7c-3c7a-9afc-5ae94414f466 | -5.19334 | -45.07389 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 464f44c4-453d-3c2c-a1a9-82d04aea5d40 | -5.4895 | -42.7367 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b0d652aa-0bfa-3c3d-b7a5-f18b9b97f2b9 | -3.69555 | -49.56483 | 2025-10-02 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06109222-04c5-3d6f-9793-d407654cdb3d | -3.78581 | -48.63152 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e259509-9612-34b2-9ff7-d927d0c9b11e | -3.34659 | -43.19344 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ab078f12-7a01-3806-827b-5a01b9561642 | -5.82812 | -42.45296 | 2025-10-02 04:27:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2857d50c-4230-3aee-bbd6-01accd435ecf | -5.48628 | -42.75813 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c9c0bb6f-f520-337a-b9a6-f6e3f6e39d00 | -5.3947 | -37.6996 | 2025-10-02 04:27:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d9791d5a-b96c-3a5f-9e4a-5f2450f8ec72 | -6.10314 | -43.4455 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1304b8d3-32d6-3330-a214-9ab345f1b15a | -5.27045 | -43.17032 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af50767b-27a6-33de-bb34-848e3ae20550 | -5.81181 | -40.58524 | 2025-10-02 04:27:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2953172b-00a5-3b37-a41d-0f765a928327 | -5.88336 | -42.93803 | 2025-10-02 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 052db678-4d29-3b68-875b-05b640703132 | -4.15215 | -44.85783 | 2025-10-02 04:27:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f4ab8ab-227b-3c2d-895d-33303f498fbb | -2.63464 | -48.04441 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdf26353-9a58-3701-b802-cb9228948a3c | -5.92546 | -44.85774 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02842d42-f99d-3089-ad1b-a25ec60eb186 | -3.81543 | -47.5813 | 2025-10-02 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf9d908c-bba5-394f-b7b9-376387efbe9f | -4.08458 | -50.75238 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0078ef2a-de99-3d5b-a267-e2d7cf908dd2 | -3.22409 | -47.12854 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fe0ae69-6ff3-3685-b258-1c29c2c2bdaf | -3.62143 | -42.77549 | 2025-10-02 04:27:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08af64d7-4dca-32d5-818b-3b38e4fb05a4 | -3.77864 | -48.63036 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c37ddfec-2de8-3ec0-b8c7-33402d67d030 | -5.97601 | -44.59829 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a38bc77e-3e65-3dc2-96c6-bbe3601aa282 | -4.00427 | -43.27285 | 2025-10-02 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README57.md)
