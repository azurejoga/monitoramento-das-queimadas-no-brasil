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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baedca0d-9124-3d1c-8674-e732c8a6c351 | -6.24193 | -45.36327 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9bc51560-28de-323b-bfbc-01143b395f3e | -7.79357 | -42.5506 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 311deee3-0f2c-3dad-ac04-36f9f8880929 | -7.80144 | -46.02228 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89416ece-6501-3ca1-9d21-f7f1c59478bb | -6.97256 | -44.39507 | 2025-10-03 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc4482f6-d71f-3dd6-b786-8c11cd0582fe | -7.90762 | -43.53065 | 2025-10-03 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d434b98b-d628-3d21-b179-407ae51d534e | -5.62883 | -43.91807 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87d7da38-9738-3d7b-b977-770ff9fadd58 | -7.7542 | -46.27792 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6224483-f7d8-3b72-b576-e6d7d80efb6d | -4.66868 | -45.80107 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 144.6 |
| e1754046-6f82-3b06-ba38-8cbfd99d998b | -7.79275 | -42.55533 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| beb95f31-df12-30ab-ae47-07c10144a828 | -5.34944 | -43.74953 | 2025-10-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d109fae-707d-3827-acc2-674077b27eed | -7.90566 | -43.54158 | 2025-10-03 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 40814bc6-9bb5-3eef-8f26-008ad9c04d49 | -4.67621 | -45.79341 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e279bd34-3812-3dc6-807f-67c66fea047e | -6.04079 | -44.62949 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5f1039ec-4bfe-3b76-89d9-33e90dc99df4 | -4.5756 | -46.49991 | 2025-10-03 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8686495d-2809-3d73-a8b8-a1e555be1eb1 | -7.7389 | -46.26253 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a52ac7b-9d3d-3edf-a5f7-0b43d5cf28f2 | -6.55852 | -43.893 | 2025-10-03 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3961e48c-f8ff-32f6-9383-8aa65ad437f2 | -6.04015 | -44.63316 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bc959f1f-a2f0-33c3-b9ef-a37d204fd4b6 | -7.75817 | -46.25651 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d12ef007-2e23-3b9e-abce-d2de9b2d5d38 | -6.23845 | -44.23519 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49ff90c9-d77b-3880-9eed-196a9c614761 | -6.88025 | -45.47704 | 2025-10-03 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a990f41b-4fb3-3f93-a944-da3f5ee6c799 | -6.41234 | -43.92785 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e9b0c79-2abb-34a2-9508-32c2338626ef | -6.70591 | -42.80019 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6138c272-424c-3b4f-8fe1-d6be230d22de | -2.92647 | -48.30469 | 2025-10-03 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cc6dd58d-bc72-31e9-939f-62e07c719548 | -7.74653 | -46.25404 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27fc8c53-4656-3127-822c-06973784b3f5 | -6.04496 | -44.63768 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e20307e-9868-3cf3-ba65-d6db80fbf3cc | -6.26163 | -43.88496 | 2025-10-03 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 69d74553-dd63-3fb0-a3b9-c8696f52558e | -6.05528 | -44.64262 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f541fc8-32ba-32b8-9ced-1397bec502cd | -7.55084 | -42.40114 | 2025-10-03 03:42:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f6eb2363-3948-3ca7-8241-08e1811832f3 | -7.42151 | -40.07315 | 2025-10-03 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8704dbec-6778-32b9-902a-32009661a7dd | -7.2974 | -45.26718 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dac9845-f87b-31f5-90ca-3c184c5736af | -7.76399 | -42.53117 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b3df306e-2329-3e25-ba84-15cff7966ce4 | -6.04141 | -44.62593 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7e413cba-06ab-3d0f-89bb-a1f98a073d31 | -5.59814 | -35.65704 | 2025-10-03 03:42:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dae1c5a4-eb4d-36eb-8e44-aad6c300be37 | -5.4041 | -41.3358 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4d71fa4-dc48-3444-9518-b666b9969253 | -6.05957 | -44.61772 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 38ea7064-601d-34c3-a70c-1425d8b07035 | -7.30916 | -45.2653 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3999417-5066-3acf-bcd1-1dbdc952481b | -7.74489 | -46.26287 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 026a639a-f562-36d7-bd86-d68a5b145221 | -6.2389 | -45.34723 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9641031e-ad96-33ce-b46b-a946dd3c3118 | -7.83906 | -42.85855 | 2025-10-03 03:42:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 36ce0aa7-f9b5-30c8-bbda-41b84c22119b | -5.64027 | -43.91385 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 45481ff8-f60a-3e94-afbe-f06e23bf6519 | -7.8843 | -47.34535 | 2025-10-03 03:42:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84dcad80-7dfc-3198-afde-4cde671c6464 | -6.37195 | -43.87339 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a97cdd1b-f461-3d86-9ca2-2f13ee99ab41 | -6.4099 | -43.92937 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3ae716d-a664-33eb-be6e-cdd8e247db00 | -7.75607 | -42.54943 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c4185d74-3b10-37f8-80a1-3e7712c78b5e | -7.78487 | -42.57358 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 94cbf3c2-780e-3409-bdbf-405f7a738762 | -6.70989 | -42.79873 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 655ee3fb-9a51-346b-b5fc-585cb8e065f3 | -4.64552 | -45.8116 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5079897-a913-3982-8b46-94e1c9e9eb7f | -6.37546 | -43.8836 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f6b328b-3d79-3216-8d15-18bff46c3b5e | -6.67638 | -42.82357 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0b65ae61-0e6c-3f0a-83e0-e8916c08a15a | -3.84228 | -41.57285 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9cb8c63e-8853-3c3b-8a11-105cc6f01f93 | -4.6595 | -45.81795 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 782b1e26-6588-3b4c-aedd-c21abebac639 | -8.23597 | -39.02425 | 2025-10-03 03:42:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 17857b79-e0be-3ee7-a222-6d6a14f6d3b5 | -7.75821 | -42.56413 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 16f69d51-eb95-36d6-ae5d-6bde2ea00801 | -5.78942 | -45.75779 | 2025-10-03 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 727e357b-9703-3527-adbc-0829561da8b6 | -6.06442 | -44.62198 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3a4de1c-64ac-3d09-8906-eb081b5c4dd9 | -8.45033 | -41.89287 | 2025-10-03 03:42:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3163e40f-c84e-330b-b8b9-70545fd1de64 | -6.23326 | -45.34611 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69ec617a-2421-39cb-8de7-89622f3db367 | -8.30468 | -44.86685 | 2025-10-03 03:42:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93771503-daa9-3e89-aee6-4f803f8ca92a | -6.72473 | -44.1469 | 2025-10-03 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 74437be0-8a54-35f7-8d9f-dddcbed9cf36 | -8.30232 | -44.85583 | 2025-10-03 03:42:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 989b7915-6b6d-3435-bcf7-79b15aa5ac9a | -7.77406 | -42.58145 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| e6fb2cee-4117-34ba-94e4-4e490b728b4b | -7.77558 | -42.51875 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1781cb28-ebb6-3d7b-bde6-1bbe6a64a3b2 | -6.33208 | -44.68773 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee9fb1cd-fefc-3ef3-a74a-40fc03ad764e | -6.04621 | -44.63046 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 82af1517-b67e-3367-8c6f-8b94ab9ea3c7 | -7.77947 | -42.57748 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 52dc47d7-6604-3f80-8c8e-a8176f968f1e | -7.77733 | -47.37611 | 2025-10-03 03:42:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7e1fe69-957a-34a6-a2c9-e147c9a44bf1 | -6.46492 | -44.20767 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b8cb9d0-273b-3990-8cd0-79e06406ebc1 | -4.67168 | -45.78431 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d60e70f7-7dc9-39e2-af39-f397c179487f | -6.61289 | -42.02969 | 2025-10-03 03:42:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b388227-6604-37c7-b898-e6ff2d45b489 | -6.72583 | -44.14071 | 2025-10-03 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eda2cf04-acac-3359-a1c7-62a5c6ac5c8e | -5.1348 | -45.43529 | 2025-10-03 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8d9eb36-1637-3203-b17b-779dccc81537 | -6.20372 | -45.91685 | 2025-10-03 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 792dbe8c-92de-3563-b6b5-2674a1cc5cdb | -7.75445 | -42.55869 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| de20a034-90cf-3abf-9d53-d656c4a90fca | -4.67547 | -45.79755 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84cce5d1-0b2e-3b70-95c0-137c16487347 | -7.25382 | -49.41296 | 2025-10-03 03:42:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 603c326d-28e9-3a8e-afcd-e9de7d15ffb6 | -4.05164 | -40.50607 | 2025-10-03 03:42:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e97700fe-4aa0-30c5-8278-ac17b48c09ce | -7.56611 | -42.39416 | 2025-10-03 03:42:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 87b5aab1-e5d1-362a-a181-8fab09825c88 | -6.23123 | -45.35766 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 7c8423e3-f368-3afc-90f2-03c007c6306e | -6.05713 | -44.63187 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| beae44f4-22bc-3cbb-b23e-f4bebf25fdbc | -4.6618 | -45.80508 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| fc64760a-a572-35ac-a0ca-d68046f13a99 | -6.13329 | -44.03314 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91657de2-8206-379a-a0a3-d5925ce26e16 | -5.63974 | -43.91693 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2c6278de-ce92-3eb0-b9eb-fff57319caed | -7.30851 | -45.26895 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e7f98d1-a33d-3a0d-acf7-dfecc168bbb5 | -4.60151 | -45.13401 | 2025-10-03 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59b4abb7-8b2d-3dd6-b1a7-da33c1f74dcd | -7.05514 | -43.30503 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 08461d73-8ce7-3329-aa6c-2b91693db427 | -4.64626 | -45.80734 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63388acd-4e12-35f3-bfad-5182bfe7ccca | -5.64183 | -43.90464 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 383ad1f4-9d6c-35b9-bad0-fafdd4f15d03 | -6.37708 | -43.87429 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 17b8b08f-ed56-3477-8233-1d698c7283f3 | -3.8415 | -41.57759 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 060e20bc-c7d4-3ea4-9db7-b5dbf96d484f | -7.75505 | -46.27333 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60dcb057-0011-3210-971f-a7efda10ec4a | -6.22559 | -45.35651 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| ae4287df-77a5-3765-bb0a-81f6093e1b65 | -6.24026 | -44.22513 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cdec6ad-a91f-33b1-8568-8ad94c7c0603 | -6.05589 | -44.63906 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05051f44-9e67-3375-a87d-7de2f0cacc0f | -6.73838 | -44.5842 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99495b2f-dc7d-3dee-897b-b078e677a848 | -6.6441 | -41.27265 | 2025-10-03 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3709bf59-156d-3bba-9b67-97682438eef2 | -7.66687 | -47.28876 | 2025-10-03 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ee87929-ae8b-3670-b5a5-64d2b08819ef | -4.66808 | -45.7879 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fb443cdc-564c-31c0-829e-31bf2e809b91 | -5.48232 | -44.11238 | 2025-10-03 03:42:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5eeefeb-a008-3e46-957a-d41208f06095 | -5.2352 | -45.17396 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ae0922d-ba28-3f55-b91c-f6e0867b4e14 | -7.41677 | -40.07748 | 2025-10-03 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
