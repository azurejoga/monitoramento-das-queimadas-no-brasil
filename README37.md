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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dee378b-0046-3d0f-8e8e-be246333e258 | -3.68851 | -49.05066 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d939752-a9b4-3954-85bb-cf3216d3a31b | -5.49544 | -49.50633 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2f8513f-b578-3759-808e-d47436379c1e | -5.49189 | -49.50579 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76d7b970-a6f1-3c83-ac0b-02eec2cec152 | -5.49127 | -49.50982 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf070d6f-39c1-3dbf-9b57-74aa96097a88 | -5.2648 | -48.2717 | 2024-10-23 04:51:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40048dff-f27b-329d-bed7-1584b0ff6fde | -7.80649 | -50.02721 | 2024-10-23 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddea0603-9c95-3810-80cf-08251a47ba4b | -7.75377 | -49.25303 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35fbecc9-a556-3af2-a0b3-58a20bd0f5d4 | -7.44808 | -49.64602 | 2024-10-23 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41502153-446a-36fd-9f0e-17fb6816ae09 | -7.44448 | -49.64548 | 2024-10-23 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69c4fdc9-1d71-3392-8adf-588b446fada1 | -7.23191 | -49.51725 | 2024-10-23 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b8cba4a-e5f7-3a65-9a84-58b61ebf12cd | -7.13563 | -49.50887 | 2024-10-23 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b4bf1390-963f-320d-93e8-947e56ca6143 | -7.00804 | -49.33945 | 2024-10-23 04:51:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52ac3950-e71f-3e56-a10e-990aa5f6470d | -7.0074 | -49.34373 | 2024-10-23 04:51:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 735de7e4-a9c0-3a95-9de9-754f42fe8cdd | -8.8146 | -49.67059 | 2024-10-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 053af7d8-ac9a-30aa-b77e-bc768d8e335f | -8.73905 | -50.05686 | 2024-10-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 570e6f9f-d4a2-30ff-a520-c7a57e001887 | -8.73844 | -50.061 | 2024-10-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e1d363e-ac54-30be-8fcc-7af8f4953ba5 | -8.73546 | -50.0563 | 2024-10-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5b29f26-9d73-39df-b7d9-8b1a98fb74dd | -8.73485 | -50.06045 | 2024-10-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23b1c8e9-87fb-315e-808e-592f7b6b6eb8 | -8.64207 | -50.1026 | 2024-10-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 345dcd97-b671-3a53-a963-9caa5c84ce1a | -8.26016 | -49.47261 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d4df3de-265a-3a6e-8c81-a82e93cdf836 | -8.18421 | -49.75554 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39c08f7b-d244-38ef-91c0-036f9c826a8a | -8.18358 | -49.75973 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea6f1bb6-6fe1-36c6-adb3-010a12ff816f | -8.18059 | -49.75502 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d8ba7ee-0d76-3000-b611-d919e3957413 | -8.1667 | -49.23851 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 490f650a-07bf-31c0-81cc-3eb10b576e28 | -8.16516 | -49.23602 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2de6c1b-8ea0-3931-9a05-5cdb6558383a | -8.16448 | -49.24049 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd863332-73d0-3ece-b6fb-bd7a938cff8f | -8.10837 | -49.89342 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13c8bd9b-5d3a-351b-9d06-fbf6feedd0da | -7.97709 | -49.68897 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74ad5d32-b78a-3f8c-9d4a-45e5c828dc46 | -7.97347 | -49.68845 | 2024-10-23 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3ae5ae8-a426-3b37-be11-5a637af20536 | -3.1643 | -50.3778 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f42164a-b81f-374a-bcd4-ef951952bf70 | -3.077 | -50.50365 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e70282f-15f9-3950-958d-4a9cae9e96b7 | -3.07365 | -50.50314 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee4f13e9-5972-395f-9de1-491b369eb92b | -3.07085 | -50.49906 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d848571-343b-3152-a220-c1cd5a641028 | -3.07029 | -50.50261 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e885dff-9db6-3522-b2c4-2161450c2a4d | -3.06974 | -50.50617 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42a97bbc-9c1f-306c-8ad9-a9a1b8e8f968 | -3.03359 | -50.25127 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 074bc141-d5f6-39bc-be60-08319f554bf2 | -3.56762 | -49.92744 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d187b05-5ae1-30f4-a495-f50cd8d37c79 | -3.55067 | -50.30431 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89524366-13e8-3ebc-a183-12f35ff91680 | -3.5501 | -50.30794 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2d461df-94fb-3433-9a69-2c75de89efa9 | -3.54592 | -49.93172 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 179a0174-4aec-386f-90fd-d78c71b89fda | -3.45196 | -50.08421 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78aa7c45-7c29-340c-93bd-1a9b6515bd8b | -3.44832 | -50.40671 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e04e17a-71f3-3c27-ba24-4ceb1e648f6b | -3.44777 | -50.4103 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a43d6f-7c6b-380b-8bf7-1281a974802c | -3.44573 | -50.07948 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5396456a-4e37-38a6-9a53-83f3c55287da | -3.44135 | -50.56312 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c51d05da-058c-306a-86be-91edf9aae845 | -3.43799 | -50.56259 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc51c36e-5248-3235-9107-0af5ea39836d | -3.42917 | -50.25256 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28868de5-e9c4-39cb-9fa9-a0c17e4e8eb2 | -3.42579 | -50.25203 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 310317f8-36cf-33ed-966a-6f1b06ecc638 | -3.41899 | -50.38408 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af309fc7-2f29-377e-9d37-67bbac7952de | -3.2662 | -49.1339 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| beb62da8-8f50-302e-b492-d6258220682e | -3.24714 | -50.18771 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d8ef56fc-c681-3083-b2f6-c99a45e550d0 | -3.2359 | -49.59658 | 2024-10-23 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 10061f6a-749e-3fb0-861f-4fb3fe2283a2 | -3.2292 | -49.11597 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7679873e-69c2-3c21-af85-fa0e83739806 | -3.22628 | -49.11145 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e7e793b-1e21-3a3c-8e98-38ca4422bc07 | -3.22567 | -49.11542 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cf73e3c-0754-33f2-b776-b64f5bc00281 | -3.22153 | -49.11884 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98e1ca7c-3039-3b20-acce-ee3aba52f096 | -3.20753 | -50.29982 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e652cf8b-db05-3bfe-b3dd-c6f96c755dda | -3.20528 | -50.2921 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1e70b59-7bb4-3139-946c-4002dbabcd4a | -3.20416 | -50.2993 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1b7ae91-70ca-3152-95f0-de8f7973e2f1 | -3.16375 | -50.38139 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9947eb74-f119-38fb-89a8-618f2e34880c | -3.15757 | -50.37676 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73a0d872-04f0-346f-8c90-4a7f139beb5c | -3.15365 | -50.37983 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aba79f61-1b7a-3355-b86a-6be793d38f9b | -3.12318 | -49.51492 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb3c86e3-3348-3511-b4f2-f31fe560671d | -3.0742 | -50.49958 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56717d56-813c-303d-b4cb-57ab7627826d | -3.07309 | -50.50669 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bbba48f-f898-3385-9c7a-60cb2f3e60e9 | -3.03696 | -50.25177 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e13b9a7-b23d-319c-93b9-61b81d2ddce6 | -2.96518 | -50.52291 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0e3c111-646b-389c-a195-3bf93cc341b5 | -2.96462 | -50.52645 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cf48245-92c1-3c2c-9df9-a4a648d640fd | -2.96238 | -50.51884 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9d0def0-3e7f-3e76-9f7e-d636837befbc | -2.96127 | -50.52594 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16ffea33-0856-32ed-ad71-6f754e6b2ef7 | -2.96072 | -50.52948 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d6c0414-70df-3067-85b0-f06ce6dde51e | -2.96016 | -50.53302 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6ae663d-2c76-3e0d-aeaa-2fc3ca24312c | -2.95681 | -50.53251 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e9a7263-2421-3414-9640-ed7eee10e1cb | -2.95402 | -50.52845 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71b1903c-dc88-3679-a26c-57e8f66d59d3 | -2.95122 | -50.52438 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f6fa96f-7d30-31b5-ab89-bbb571bc0e15 | -2.95067 | -50.52793 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10f6664a-1701-3bf2-b574-d98b995a4e61 | -2.91202 | -49.42863 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5503d960-af93-33f1-ba34-c24b0d238fd1 | -2.90855 | -49.4281 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4568f5a-63c8-3282-9d0a-8bee60c291ad | -2.90795 | -49.43192 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 311d586e-ea56-3d01-883e-2cc80452ab39 | -2.90234 | -49.75893 | 2024-10-23 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf2a7a17-0323-3e9b-8af3-af7935523ad9 | -2.82313 | -50.49334 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cca3892f-f544-3083-8ede-b819645d715c | -2.82258 | -50.4969 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12e6646d-bee7-3e34-81e2-03f578c094f9 | -2.79909 | -49.58625 | 2024-10-23 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9d52a201-cadf-39ac-9ff9-519148897907 | -2.79851 | -49.59003 | 2024-10-23 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| aa4fae10-f5ed-3137-8e7a-513d2df43ef8 | -2.79506 | -49.5895 | 2024-10-23 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19918c84-c503-3458-ad80-7e7dca3d48a1 | -2.96183 | -50.52239 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c48274a-b80e-393f-a6f1-69dedf073780 | -2.95903 | -50.51832 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff153068-f6fc-37eb-92e9-9c02f60194d8 | -2.95848 | -50.52187 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4735afea-1e48-3f9c-992b-d5888fa0faaa | -2.95792 | -50.52542 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b9644b1-343f-38ba-99ea-1571c8b5421b | -2.95737 | -50.52896 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a02feb3e-5f1e-34ab-b29b-c35e757f3633 | -2.95568 | -50.5178 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8bd11c3-8065-3136-b803-b94ded6f2199 | -2.95513 | -50.52135 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b711d69f-42eb-3491-85d3-1a2e7812a1cc | -2.95457 | -50.5249 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d7fe183-132d-3ff9-9221-2d94375c8e15 | -2.9292 | -49.76681 | 2024-10-23 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 962b39c4-0cc5-34a2-bb89-b4f67272c6ee | -2.91831 | -49.79181 | 2024-10-23 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91a9759d-5567-37c1-ad79-7cad3d451f60 | -2.90075 | -50.40734 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c9cdf90-7f0f-3190-9adc-851806c452a4 | -2.89739 | -50.40681 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4734cd8a-2aa5-3eec-9fa9-29c6630f86fb | -2.81923 | -50.4964 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d875501-370c-34ab-8037-3f6b4515a802 | -2.79564 | -49.58573 | 2024-10-23 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3f03e3b-62c5-3cf8-983d-3e00b1692532 | -2.78521 | -49.29195 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README38.md)
