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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36837e53-87c8-3321-91b2-d1cf270fdc67 | -7.20731 | -43.12193 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 28b6019c-06e0-3a0c-a044-ee874c175b12 | -6.23016 | -43.35094 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4652c92d-66f1-3e30-982c-7b5591650307 | -7.21163 | -43.11819 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| ead20678-6a34-3312-9661-6357a562cbb7 | -8.43424 | -46.65487 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f444121-b9bf-3620-9297-ffad342211af | -7.54474 | -43.18092 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4d36289-1b5f-344a-b6d4-1bc53c110994 | -8.75517 | -49.75267 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b70eab7-4db8-31d6-988d-1c56365b4dda | -6.65038 | -41.99822 | 2025-05-27 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45cba7e9-e8ce-32a7-9e37-78cf550ef4cc | -6.21412 | -43.33583 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 011554e9-a6f3-3def-9971-c0c33611ab9a | -7.23196 | -43.10811 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 1b682648-8ab7-345d-b8c6-7432f6e66dd1 | -10.34247 | -47.97659 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31f4bdcf-c4d0-3207-8905-1bc20dde8fab | -6.63907 | -43.21298 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5d829974-be30-31f9-9a2d-87296971f4f1 | -7.40638 | -49.37602 | 2025-05-27 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0461824d-106a-3812-963a-65d0a0bda1cd | -6.23144 | -43.35039 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fd99cb6-3018-3d6c-a3f1-02fb3432de64 | -6.65189 | -43.20196 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a03c6109-79bd-3b23-b0a8-152afc5b2f8c | -4.48421 | -47.7913 | 2025-05-27 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a398689b-1183-30fd-8d25-02c0e380de5e | -7.22029 | -43.11071 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 58b27f67-85b9-392f-94f3-d69eb9706781 | -7.60186 | -43.41408 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91648f80-4d83-3c88-b728-4222ce96a19f | -7.47604 | -43.36251 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96f1add8-c666-33b7-8cd3-ebb34b59c95c | -7.57806 | -43.34991 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b11f3985-aec1-3210-873f-d1acd3cf1967 | -7.21229 | -43.11388 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1785caf1-6f1a-3b1a-ae73-2adab70c879a | -9.39694 | -48.42725 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd9e4ead-f21c-34a5-b300-f38e098915ce | -9.8438 | -44.69724 | 2025-05-27 04:27:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ac88e34-d469-3d3d-a96c-46abbae838ae | -4.17656 | -47.53237 | 2025-05-27 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69a5bd0f-33de-3c5c-8d0a-d2c7270150eb | -8.01905 | -43.18591 | 2025-05-27 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f3c62bbe-063b-3c4a-882c-d89ea8f557a9 | -7.19825 | -43.10732 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 18cd08fa-0e5e-3921-9c5c-dd982f27b367 | -7.6025 | -43.40987 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aa8c834-455b-396a-8245-c6bc263ca560 | -8.42869 | -46.64683 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9fe6392-5e6f-3caf-8d07-fc2db09be334 | -11.80136 | -46.65239 | 2025-05-27 04:27:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c5826c3-0a89-3350-85fe-6fa8635cf1d7 | -7.56522 | -43.36105 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48d80e4b-55d8-3571-b1c4-56d328781101 | -11.56332 | -47.44295 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0eff3221-efb4-3a84-ad0c-71146b3e052a | -6.64649 | -41.99765 | 2025-05-27 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0f94131-5926-3dea-869d-83dfb84ba2a4 | -6.63544 | -43.21242 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7f194a32-3e50-3026-899e-511e49216e47 | -9.49567 | -40.30634 | 2025-05-27 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd055053-d38b-3751-8f2d-5465c20ca702 | -7.60379 | -43.40145 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ae36059-d57a-3062-9107-b92ead499e90 | -6.4993 | -47.48695 | 2025-05-27 04:27:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 61b1f69f-3e8d-3108-acdb-36a5f8e88ac0 | -9.03761 | -47.75444 | 2025-05-27 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4af023ba-e135-3786-9a69-9e7a03c5c775 | -7.56094 | -43.36477 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6383cf27-c42f-3d2a-a9ee-cdd6df9e49aa | -10.72402 | -49.54517 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f36ce69-c94b-35cf-9e6a-5051d982c55b | -6.22785 | -43.34985 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 34209cdb-1009-3de3-bcbd-4a721480cb70 | -7.21416 | -47.05434 | 2025-05-27 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 72f4d805-f3c8-3800-980b-b5440796cc79 | -9.15424 | -49.64875 | 2025-05-27 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f323257e-2175-388c-b393-dc9194290af9 | -7.16971 | -43.32042 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1dc5e2c-40f5-3c49-a3f4-35fb2c79af48 | -10.17509 | -48.15317 | 2025-05-27 04:27:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84cc0053-f4fd-3ec2-9fee-3431c2f97fc4 | -6.83628 | -42.79736 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5cfda52f-840b-320a-95d6-0a3a97da0683 | -11.56943 | -47.44755 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05d44078-afeb-3967-8283-68fc904dc4d5 | -8.16851 | -47.2248 | 2025-05-27 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb5345d5-5f7a-36c0-b6cf-f632f20b4ef4 | -8.43312 | -46.64038 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40a0cb12-613a-3621-bfc6-42d45ffc20ed | -11.80365 | -44.26893 | 2025-05-27 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4f2b3f36-f059-3de8-8cba-06724b4a36c8 | -8.31835 | -55.11811 | 2025-05-27 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 514f2a41-30bf-36a2-b68a-bcd9cc28bac4 | -6.63971 | -43.20877 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c15b9834-9a40-3608-9016-353cfb2f3838 | -6.22846 | -43.34571 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fb77038-805b-3ddd-8dd3-94e021b38c1c | -8.43202 | -46.64736 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c575f17-7dd0-3430-852e-1af38eb2d4e1 | -9.35144 | -50.23325 | 2025-05-27 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8bbe948-a8b3-3dad-85c5-d59586e3a2ff | -8.01924 | -49.6884 | 2025-05-27 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3d094b1-12cd-3613-8e52-b9ee6ed82d68 | -7.15945 | -43.31454 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97354b62-9b06-3221-9187-7d7d3e24f114 | -9.0354 | -47.74683 | 2025-05-27 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeb0ce0e-b350-3e6b-8852-699a0e7cce89 | -7.46442 | -47.05822 | 2025-05-27 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 48230ae2-b9b8-34ed-918c-0c68ddb9d8f2 | -11.8043 | -44.26577 | 2025-05-27 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7ebb545-2233-39d4-bae7-24de30f8aef6 | -11.28708 | -47.50305 | 2025-05-27 04:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f44dfb7-b5da-37cc-bbd2-6c6499cbaa03 | -8.78145 | -47.95737 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85418d51-68b5-38fa-b835-f3776258096e | -6.32061 | -43.36788 | 2025-05-27 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1b180c8-786f-3910-b2c6-17f97899f496 | -11.77122 | -46.41561 | 2025-05-27 04:27:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 644eecb0-bd82-3fd8-90a6-d1148cc0006b | -7.56157 | -43.36053 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae427ebf-48c9-351d-8e4f-0d059e56f63f | -10.63883 | -48.80532 | 2025-05-27 04:27:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53289075-0f47-3fe5-8c2a-cca08e8cf40f | -8.42924 | -46.64334 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17ea452f-1a29-3ff7-a7b1-5a26dd602c90 | -8.7545 | -49.75676 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4f9e39b-61f9-32ab-b5b6-c22362958949 | -7.16716 | -43.33719 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4906a33-d9ac-3f57-a34c-807b164fe569 | -7.48695 | -43.36419 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52715c90-caa6-33c7-b9c4-23757b57c92b | -9.03262 | -47.74275 | 2025-05-27 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5d56f78-d270-33e4-8571-5a31a322e95e | -9.57117 | -49.11514 | 2025-05-27 04:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beda5584-ffdf-38cc-b371-f062578c8963 | -9.02984 | -47.73867 | 2025-05-27 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0d02b80-cdcc-3943-a781-43209a09d52b | -8.43037 | -46.65784 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f5d6883-2424-39e3-8c1d-8fd7393fe966 | -6.31999 | -43.37195 | 2025-05-27 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d983dff4-8744-3c91-9a8b-cdab6588a74b | -8.75292 | -48.0484 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e94f74c-dceb-3b1a-9ba1-2660dd56cd91 | -10.73794 | -53.8848 | 2025-05-27 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70e6eaec-f122-38bb-b3c3-6191f67525fc | -6.63119 | -43.21596 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 126ab482-b2da-355e-8922-d7ec3d4d2acb | -9.38177 | -48.41357 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d343815-90d8-3e82-816e-ccfd7b75cc4a | -10.34524 | -47.98069 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c477d670-a20e-3431-9399-19925ec722a2 | -9.38398 | -48.42139 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8340dd3-607c-315a-8a3b-7b1da2f485c5 | -6.86536 | -47.83871 | 2025-05-27 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54a43e34-4914-3309-9c3b-7eaad8c3b7a6 | -6.63181 | -43.21183 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 515f4a40-e211-330e-9e6c-564f424a65e0 | -6.16359 | -48.0543 | 2025-05-27 04:27:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d117aaa7-5d91-3ea3-ac7e-3c0e991ac0b9 | -9.15357 | -49.65276 | 2025-05-27 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e40d90b-bc62-3286-9ce8-e63b5c4b00fc | -6.16701 | -48.05486 | 2025-05-27 04:27:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eec9f42f-09a0-3374-86df-8177f0307197 | -10.3419 | -47.98014 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 043aa593-3dba-3254-95f8-07f988457209 | -5.78461 | -43.61864 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d7a7a01-de03-3fe1-a4c1-eb094c2962c7 | -6.65055 | -41.99646 | 2025-05-27 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| caf00310-f6ad-3fde-8418-831befc5bf91 | -10.36423 | -47.96917 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6377a91-2640-3ef0-a32b-501355a2530c | -7.45713 | -49.63558 | 2025-05-27 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8ab326c-4373-35ec-8af0-24a22f965272 | -12.15914 | -43.2073 | 2025-05-27 04:27:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbe48ef0-d311-33b8-b501-7f5a8b538ebc | -7.16353 | -43.33665 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6da63a3-a909-3883-9ffb-1f6744a7ac30 | -9.38678 | -48.42559 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 908b753d-86b7-37c2-ab31-1f127528f6ac | -8.01841 | -43.19027 | 2025-05-27 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0a5f52a-892b-3375-8d2a-c3c675af30ee | -11.57488 | -47.92225 | 2025-05-27 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ab40187-38a4-3c6b-bb5c-8dd37da0a10a | -10.64167 | -47.4784 | 2025-05-27 04:27:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df2828ab-2389-3354-b161-f7a91195ebb2 | -8.42982 | -46.66132 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 204bcd17-9b8e-384c-b4b8-fdc21ea2bfbc | -6.49873 | -47.49051 | 2025-05-27 04:27:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2bdc83c-fee2-30a2-a579-b1a383be2427 | -11.23661 | -47.47687 | 2025-05-27 04:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59ccc19e-50ba-31d8-91fc-c9ed2165c0fb | -11.05359 | -48.85384 | 2025-05-27 04:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adcb1e2e-93ae-3cb1-b474-484678e75855 | -10.71758 | -49.62778 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README9.md)
