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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb4b6e58-a798-3518-bf52-a443ee5a961a | -4.1148 | -48.2515 | 2024-10-11 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 383.2 |
| e4d3d4fc-109c-3b07-ada1-963cbb707ece | -4.1149 | -48.2299 | 2024-10-11 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 224.8 |
| 6ffcc632-16f1-39c6-bab7-ef53c1ce126b | -6.5589 | -60.0252 | 2024-10-11 04:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 78f6a494-4dda-37a7-9652-01d1c9c71a70 | -8.4417 | -55.4692 | 2024-10-11 04:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 9ed965e2-ad34-3787-b503-7329caefe005 | -8.4419 | -55.4491 | 2024-10-11 04:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| fbcfb1ad-c0e3-3663-b6b8-4b8715c78c89 | -9.6575 | -64.9658 | 2024-10-11 04:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 88446943-4769-34c7-8285-22cd8de801c1 | -9.6389 | -64.9664 | 2024-10-11 04:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 41d42007-cbf9-3ec3-8ab3-dfa23f130eab | -9.639 | -64.9477 | 2024-10-11 04:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 59a41c1f-7be7-359b-aac2-b1463539656c | -9.6576 | -64.947 | 2024-10-11 04:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5af7178d-0695-3fd9-928a-45b656de284d | -10.6962 | -53.0354 | 2024-10-11 04:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 14bde968-0751-3ab9-9bf0-e4ac76cd20e4 | -11.2407 | -53.2738 | 2024-10-11 04:16:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b1619696-541a-3c9b-bf47-e3495b2b7883 | -12.7678 | -44.8671 | 2024-10-11 04:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5e4e744b-7ded-3cb4-849a-5de929891349 | -13.7348 | -60.5883 | 2024-10-11 04:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 77eea33c-9392-3484-9ce4-3a3d98c17991 | -17.6664 | -56.3267 | 2024-10-11 04:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 31871f75-dba9-3a87-ae94-101707048eb2 | -18.1773 | -56.4676 | 2024-10-11 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| c37e6a34-2155-3ec1-9072-f560771a1e30 | -18.1776 | -56.4468 | 2024-10-11 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.9 |
| 292c8b0a-6533-392d-881b-d54743f72e4e | -18.178 | -56.4259 | 2024-10-11 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 1472093b-631c-3e57-b8c7-7c29ea313d3e | -18.1971 | -56.465 | 2024-10-11 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 1fe039aa-01d2-32c7-8c4e-305200b238ea | -18.1975 | -56.4441 | 2024-10-11 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.0 |
| 8f1573ff-5958-3686-825f-e259271ec0a0 | -0.81701 | -48.67234 | 2024-10-11 04:21:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a82ea015-0f4f-3a0a-bacb-462249b2d155 | 2.48624 | -50.8297 | 2024-10-11 04:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b3a4854-f85e-3ff6-80b9-34bd10fbbf79 | 2.4804 | -50.82154 | 2024-10-11 04:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd803616-0d9a-375a-af5c-54d0bb615751 | 2.47972 | -50.81708 | 2024-10-11 04:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c34a2d49-4bd9-3306-9c44-0e5bdba7b9c9 | 3.3424 | -51.32381 | 2024-10-11 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1992023a-5846-3364-9d4c-e913566decb5 | 3.34168 | -51.31883 | 2024-10-11 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5322ba4-03b9-300b-9f11-e1a083c7602e | -0.06617 | -51.65616 | 2024-10-11 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54b9c2f0-5941-34cc-8cdb-0d923b4c344e | -1.41093 | -46.44373 | 2024-10-11 04:21:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01f4b303-d17f-36d5-a8d7-531762979dcf | -1.17395 | -46.73106 | 2024-10-11 04:21:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f92918e-dd13-361f-8330-e3bd7923009f | -2.18821 | -48.85108 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c39d406f-6c2b-3525-a04a-8ace709d0fcc | -2.16171 | -48.85131 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d1ea4a-1427-368f-bc4d-7817ff1defe7 | -3.65367 | -49.6292 | 2024-10-11 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6364a67d-5873-34d7-aba8-ec2114663750 | -3.50878 | -50.39136 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70b4e25b-9ff6-3017-a960-35d91d0b92ab | -3.42152 | -50.38548 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c82bf238-24e5-3b58-9904-0c455d3aecdc | -3.41009 | -50.33107 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fec0a44-ab9e-3292-9986-fe112aa56731 | -3.40613 | -50.33039 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01fd0eac-4fb2-3edc-9a52-7272aa861342 | -3.38659 | -49.77501 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e37fb78f-9505-3701-a862-6945befbde7d | -3.31509 | -50.1776 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 807b8bea-0166-3e30-a92e-d7a47062fcd7 | -3.31456 | -50.17912 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 7d86a2ec-a4f0-3b77-8b54-84f382d51806 | -3.31116 | -50.17696 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 4afd8fd4-f111-395a-b54a-a73bbe5f81bc | -3.28311 | -49.09578 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9beeffd-a7df-3062-9d11-911c138c8954 | -3.26772 | -49.10359 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 979c02fd-2d24-3cbe-aef4-95e412ea663e | -3.26472 | -49.09867 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d08cb79-6272-3409-9172-0c19b836cfc4 | -3.26403 | -49.10302 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ade8b46f-8c2d-3ec4-81e7-8da9bc588a91 | -3.49733 | -49.18451 | 2024-10-11 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cca86738-3f57-3780-9ea8-05ccb90180c3 | -3.27943 | -49.09519 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 117cc43d-64c1-3690-8d76-efcb8fa2b504 | -3.26103 | -49.0981 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c4291dc-a570-305e-90be-6bb6261955a0 | -3.63555 | -49.69258 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 867f7d39-a78e-37ee-a3b8-453d74d2cc6e | -3.5058 | -50.39384 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b41b6b8-d4a5-33fe-b3b2-9de04fb986b5 | -3.45977 | -50.6067 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6783e62-a201-3287-b7e9-eb40daf75ae5 | -3.40217 | -50.32975 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be57f33c-f8f8-3360-80ed-d9f83a919ee9 | -3.38497 | -49.77661 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2de5218c-d90d-339f-8162-0f7f573011ab | -3.3355 | -50.1247 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51acc644-dbdf-32f6-846d-15bb6a4c5e30 | -3.31539 | -50.17411 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b6b9edd4-0b0d-3132-b48b-bc9ed9ac98ea | -3.31146 | -50.17348 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| be7b6172-a976-307d-a055-18cec4ab56ba | -3.31063 | -50.17848 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| d06cf459-29a0-33df-b090-ad68eb03dcc1 | -3.30723 | -50.17632 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 709eeb22-7901-3078-8757-11594a5b1f74 | -3.29276 | -49.10622 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95e95318-b2b0-3a5d-892a-05607dad3c08 | -3.28907 | -49.10564 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8bf6d50f-a458-3129-9e23-98dd3888720e | -3.27647 | -49.09608 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0aff6e56-cc57-3847-92c3-41ab409855b4 | -3.27574 | -49.0946 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d265dab-0cf5-3135-b384-f3cb374dffa0 | -3.27504 | -49.09892 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccf9498d-1665-3fe6-86b4-cefe896d80f4 | -3.27135 | -49.09833 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb63237a-89ab-3def-b012-a87cc33dc258 | -3.26841 | -49.09925 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 994ecb4f-c4f4-3802-b595-dea0ab98e59a | -3.25965 | -49.1068 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dcb2e43-fdf2-3c64-807a-bfc679345254 | -3.16719 | -50.43777 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15ce885d-6087-372d-b1f8-facc86d1e29a | -3.16622 | -50.43421 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68b0b291-0c5f-3571-9d0f-d7a7e067d08c | -3.16568 | -50.43765 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0dc9a7d9-2759-30ec-8092-2c7e7335a6cb | -3.16514 | -50.44104 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9410d15d-6aee-331d-9986-3d26c2afb937 | -3.15768 | -50.43628 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c752816e-475d-30ba-a2bf-b2c31b82ee61 | -3.1566 | -50.44307 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 95177b1c-1c1f-37b1-ae8a-f2ab23b0c639 | -3.15368 | -50.4356 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ea99270-a151-3e54-8bcc-cf9291dd8227 | -3.15259 | -50.44241 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 2630827e-f2ed-39e8-a0e8-5366ee96cab0 | -3.1515 | -50.44931 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0c2dad1f-84db-3719-b8cd-069f41ed7875 | -3.14859 | -50.44176 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| cbd6d044-43c4-342d-b478-bb763e1b38a7 | -3.14804 | -50.44521 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 52900c0c-a73c-3c36-b329-034c54d85919 | -3.14403 | -50.44457 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1648b15f-7c04-3a84-8d80-23b9b0937eeb | -3.13478 | -50.42532 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2993c49b-120b-3f05-a200-da4af84428b2 | -3.13023 | -50.42805 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f51a759-a0c9-3dec-9d49-a04502d2d3ae | -3.09659 | -50.48346 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a54c512-5d3c-3180-ae60-c81a7c1709ba | -3.09338 | -50.22803 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 338e1bda-0a65-3a46-80ec-f7ecac35d873 | -3.09077 | -50.22525 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b9144ff-398c-311d-8ee7-63b223dcfb22 | -3.08997 | -50.23031 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06546178-3ae9-3c2e-a7bc-0b8d65c921c4 | -3.08942 | -50.22743 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d92dc552-9a05-33ea-9edc-8e1ea2ce921d | -3.06673 | -50.48941 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73c93c33-cb51-3cf6-9eed-8f3024d48036 | -3.05535 | -49.37231 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c82f62d-8865-3543-8a9c-69760886faf7 | -2.96185 | -49.20712 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98b26037-bca8-3984-82e6-ad28ce125f8c | -2.95812 | -49.20652 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5826fd7-9e03-385d-aecd-adf38df28afc | -2.95512 | -49.20147 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 175221b7-6eb9-3c5e-a344-bf80e6543827 | -2.9544 | -49.20592 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36be3fbc-5df8-385a-b988-174407ce9791 | -2.94587 | -50.30204 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 056dc3a2-e7af-34a3-965a-f9606ee95a00 | -2.94484 | -50.49487 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93ecf6a3-f378-3740-b5e7-e99403c5dba1 | -2.91641 | -50.48689 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47410cb2-e61d-3fc5-abc3-29b00223c3aa | -2.89837 | -50.39369 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e03a7ac7-94fb-3525-8e30-b0245cdaf983 | -2.8938 | -50.39651 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57876a0e-ce05-3465-870b-1f7a8ea5f8d3 | -2.88979 | -50.39586 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c26ece0-cdfa-3b59-8bf7-5a81d0d3687c | -2.84639 | -49.87033 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59f91808-041b-3819-8ace-c61133d70848 | -2.83863 | -49.86909 | 2024-10-11 04:23:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d339bb4-085b-343d-9677-b1138d412cd2 | -3.16775 | -50.43436 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be23bf8e-5eee-3ef5-8f70-f4982e96ffa6 | -3.16167 | -50.43699 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| aa5b147d-4a79-3a28-b8fb-8cd387c403a5 | -3.16114 | -50.44038 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |


[Clique aqui para ver as próximas entradas](README47.md)
