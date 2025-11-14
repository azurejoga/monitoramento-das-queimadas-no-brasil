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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28fdaa7f-2690-3882-a18e-555bc95f2bac | 3.10186 | -60.77428 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 344ad299-d8a1-30b0-946c-fa70651c83c3 | 3.1405 | -60.71367 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 25149e35-00d3-39b8-895f-4f3222ecbcb7 | 3.14126 | -60.71889 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b095e821-3eef-31b1-a589-7980a9189cad | 3.16621 | -60.28784 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62080ee1-a0d9-3359-af9d-2fbcbd6f8517 | 3.10978 | -60.77184 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5ac7538e-ef25-307e-a296-df91ce2d37cf | 3.16551 | -60.28295 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 289df2ce-203e-3bcf-8a91-dce1716b8159 | 2.33747 | -51.65306 | 2025-11-14 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdedc2d4-657b-371f-8edd-613abf37c92b | 3.16706 | -60.28591 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25f1100e-8e23-352e-9af3-e06bd458f0ba | 4.26121 | -59.84566 | 2025-11-14 04:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe4f724d-3e3a-36fa-82e8-c4018ae57d9f | -5.52588 | -41.75392 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 222b194c-dcc2-3867-8eee-bbad56f78db2 | -3.43069 | -50.16761 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de494429-54b3-3b7e-be59-b2ac09097f43 | -0.96036 | -52.05514 | 2025-11-14 04:44:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa117139-8f06-3eec-bebf-8c9e36d12e74 | -3.75645 | -52.00854 | 2025-11-14 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b8ca484-a6f5-34c7-9a46-d8705239cc9e | -5.85674 | -47.58648 | 2025-11-14 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66376cf7-eb1f-3b12-91fe-ddd85da40f28 | -4.99311 | -47.51465 | 2025-11-14 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e7d3a4-51ce-3bb0-a6dc-458192f794d8 | -3.3526 | -46.86996 | 2025-11-14 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbdc6154-0f76-3238-bf08-97cde1b0bc92 | -5.45606 | -47.1008 | 2025-11-14 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 023d89aa-e3f0-3530-885e-273c89110a84 | -2.05976 | -56.62546 | 2025-11-14 04:44:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5194fed1-e2e8-3e67-93cf-24b2ef65fee2 | -4.2167 | -49.11668 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0032a620-9393-3235-8e1e-67a0eb6a6aa4 | -3.36343 | -48.40258 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5701a7f0-fa6e-30ab-b544-d9607b0837d0 | -4.6981 | -44.37451 | 2025-11-14 04:44:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48a53b46-a17f-3ced-b854-04e17cf83ccb | -3.9912 | -47.19129 | 2025-11-14 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b343c992-7e29-3ec6-9308-72860d3db17a | -6.56939 | -42.13116 | 2025-11-14 04:44:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c49abb1a-e986-317b-84ce-17bb2022e493 | -2.93929 | -49.36097 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4ae8a311-b000-31ae-b8ca-7451c73e6b11 | -4.05149 | -46.44046 | 2025-11-14 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb56d4c8-1776-38f5-8618-6719594a00bd | -6.28695 | -41.73396 | 2025-11-14 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc7042e2-574f-356a-a218-fa2d95f9f9de | -2.79685 | -52.9671 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76f263d2-7780-3cba-8247-e8dde44ad682 | -4.71232 | -46.44898 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8406106d-69ae-3984-bc55-51d80fdf9f54 | -5.37548 | -41.05009 | 2025-11-14 04:44:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a765b7a-5fee-3af0-81b0-787d2c400c5b | -6.15312 | -48.04729 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 115f86e0-c7ba-34f2-b3cb-f016ad3f0957 | -5.57497 | -50.40252 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ecedd9c-e3aa-343d-af76-473f628fbdff | -7.21548 | -44.73336 | 2025-11-14 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0405319f-1f0a-3a2f-bc0e-1d75127c698b | -3.28681 | -52.11041 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a7e2363-0117-366f-abc8-fafd55b31479 | -4.11372 | -50.05931 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 736ce50f-820d-3500-bf76-712595cc03dc | -3.08239 | -49.27219 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2860ea72-d05b-372e-9c6e-dadcbfb44876 | -6.09758 | -41.59685 | 2025-11-14 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 113994d7-6d11-3ac9-b4fe-0af77b7149db | -3.47895 | -45.6523 | 2025-11-14 04:44:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee03d2f6-b350-3bb9-8582-6e088f832fb1 | -5.49705 | -41.91291 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 25ce55d3-e734-3c77-9b5a-6c0fb234948b | -4.77407 | -48.68342 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b7c387f-defe-3524-a0a9-a0c1f4c62279 | -4.53366 | -46.39593 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f277609-125c-3e7c-a9be-3adea469ea2b | -4.63476 | -45.16161 | 2025-11-14 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e73509a6-98be-31f8-b9cb-f73ccffc0c5c | -5.45484 | -48.92456 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb101e27-8fcf-3602-9390-1ca685e5ccce | -4.30466 | -46.26909 | 2025-11-14 04:44:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d6aecb-7418-3fe9-b49a-52436cb5b662 | -3.42291 | -54.62484 | 2025-11-14 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79920e2f-38aa-3f66-b892-3cb41ae532b1 | -6.28666 | -46.95708 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e9e5e47-ff17-3e07-9730-9d04be78e33d | -3.80561 | -45.03651 | 2025-11-14 04:44:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85bc257f-a085-35ff-9f00-e403df1fc5f7 | -5.5423 | -41.82035 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7624e87e-f0a9-3ec7-9628-c5b58444028a | -5.59556 | -45.18038 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a27d6597-24f3-3bf3-b4d4-b0ead1e9b985 | -7.11057 | -44.06987 | 2025-11-14 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc460bae-e43b-33a7-a11b-513d0f49b69a | -1.83588 | -53.79847 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93e54791-937d-3256-9624-c0bf8fdc1bf8 | -6.85288 | -46.75811 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31464728-08bf-3731-a25e-1be3479b5ffb | -4.69728 | -49.65144 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 623c46aa-a81a-398a-9197-b5d2c6f0d7e5 | -1.90159 | -47.16039 | 2025-11-14 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83c02140-df13-3d1d-ae3b-e8eb64db1b30 | -4.32219 | -48.63767 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98e512e4-6ced-3383-acfe-2f9d0ac31b75 | -6.16381 | -48.04895 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8b878c76-ee12-39da-a666-d2bf2695cfd7 | -5.85738 | -47.5822 | 2025-11-14 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60992120-27a8-33c3-b2ea-aadc179879cc | -3.91364 | -44.32426 | 2025-11-14 04:44:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4fa2c8c-3e0d-353e-9c8f-faa634674a93 | -6.92249 | -44.13785 | 2025-11-14 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fab159e0-271a-31b1-9ee2-e5d26123d3bb | -2.37741 | -48.67765 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1913462f-ad97-35c3-a683-e84d6ceceabf | -2.51743 | -47.80754 | 2025-11-14 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3acd0eb-b3c7-3006-9077-07bc474e8f07 | -3.90975 | -50.03818 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 462e220f-4d10-3b8d-a192-4e11f264630d | -1.83215 | -53.79787 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ba2ef1d-e38a-359a-be4e-dd136c158ce3 | -3.16131 | -50.62479 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1b0e8c2-1350-38a7-acab-d7f3c3ed10e9 | -2.46918 | -48.22685 | 2025-11-14 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c00e4ab-1584-3049-9f8e-48852d6ae563 | -5.00881 | -50.91314 | 2025-11-14 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4559b1b8-1894-3fc3-8b7f-bd283d7d56d0 | 0.61964 | -50.76395 | 2025-11-14 04:44:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ff8a714-a973-3cce-b120-79c61a830165 | -3.82059 | -45.29277 | 2025-11-14 04:44:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b830f15-fbca-398b-a317-275149e9d6d5 | -4.40801 | -50.82204 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28758f1e-4a09-3d1d-8517-16498279f49e | -5.33294 | -41.86179 | 2025-11-14 04:44:00 | NOAA-20 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b774199-eafe-3148-96f8-9435d28025cf | -2.59932 | -51.93676 | 2025-11-14 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c01beeb-c891-395e-95d0-4e603f3727fe | -4.71206 | -46.44156 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9856bbb9-098d-312d-88f7-2504d9ae97c3 | -6.16024 | -48.04841 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 30bc5a0f-e688-3e6f-92f6-282fd107c6e1 | -5.00827 | -50.91658 | 2025-11-14 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 833af727-8e5e-3be3-bedc-7bdc2eb29362 | -4.33608 | -49.04663 | 2025-11-14 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 287b0a91-d55b-3704-bff2-b18dd815197b | -7.05129 | -45.05935 | 2025-11-14 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7eee3f8f-c998-3b55-b1e3-7282914f0a27 | -3.35774 | -48.3941 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 948249c0-efc6-36a2-8ca6-90a8a4f27c71 | -4.11317 | -50.06276 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eb406d5-fc60-3280-9d4a-97535d4f674a | -6.1095 | -41.59064 | 2025-11-14 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 08e559ad-d2fe-3d29-9f95-5fac904569b6 | -5.73998 | -42.72823 | 2025-11-14 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 76776fa7-6f5b-3173-862c-a13b66bcabd2 | -3.34842 | -54.10831 | 2025-11-14 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 276a8ba9-e7e5-3a76-a180-60f3ca1c83a8 | -2.17021 | -48.36931 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7088213-2a35-3757-a84e-d780c8bcc200 | -4.71289 | -42.93979 | 2025-11-14 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 851c019d-875a-3c8f-b397-df808e80ec7b | -4.71067 | -46.45097 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01cccd29-4923-3b03-bd51-344dc3f42051 | -2.11461 | -45.36758 | 2025-11-14 04:44:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70d57c51-fdcd-31d0-878d-5cb7899c3b19 | -3.43015 | -50.17105 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0043d076-d582-3c7e-9051-0d67bb262510 | -4.60319 | -43.35305 | 2025-11-14 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32bb111e-e1dd-3976-abad-ee285dcf4c18 | -3.8194 | -52.33587 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ac32910-0a80-36d8-963d-cfc0fbeda567 | -5.78362 | -51.42555 | 2025-11-14 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0de04059-87a0-3f33-8338-9a9a8f89fbca | -6.99347 | -42.78468 | 2025-11-14 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c887d344-9596-3250-b66b-9e4cb7d3bba6 | -6.4729 | -48.36794 | 2025-11-14 04:44:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 293257a1-53b2-3ecf-9bd5-2ec2b792bc30 | -1.33843 | -54.61096 | 2025-11-14 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eb73535-6ea0-3d58-bde9-fb629f7eced9 | -4.10659 | -48.01742 | 2025-11-14 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd752156-e2a8-3481-8a13-aaf8ca02a376 | -6.72302 | -42.02839 | 2025-11-14 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ced369d1-ea17-3b41-a6fb-e580082ee27d | -1.42417 | -55.30573 | 2025-11-14 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72cb379c-dfab-3030-b53b-f5c5ec19b950 | -5.52007 | -41.75651 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 50c4db57-8020-3002-abc9-508c30d122f9 | -5.5254 | -41.7572 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae705328-1fdd-3f7f-acc9-19e2405cf013 | -5.97331 | -42.59687 | 2025-11-14 04:44:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ad4a30c0-6c11-3380-a102-3d9ad1d5cb0c | -4.11095 | -50.05534 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de8c2e2-c271-316c-a817-af7fbe6ed6bc | -1.34315 | -54.6067 | 2025-11-14 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eeef9e89-4277-369e-bacb-b15156e6d46a | -4.21614 | -49.12026 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README40.md)
