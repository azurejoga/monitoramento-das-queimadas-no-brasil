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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdcc2d1a-5bcd-3f1d-b882-60172b7fe86a | -1.58095 | -53.33311 | 2024-12-25 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e5f5756-1393-34f4-8ae5-d2beedbda5c7 | -3.06782 | -53.7904 | 2024-12-25 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51841bf2-d7f2-3a74-aa25-69ceb2cde331 | -3.0075 | -53.82301 | 2024-12-25 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5fc1ac2-cbfd-3c34-b6e0-9b0093d11130 | -6.23041 | -55.62242 | 2024-12-25 05:35:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d639a0e-e3e3-3c58-a634-173d1ab58b4e | -6.23098 | -55.6217 | 2024-12-25 05:35:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e97c6f3-d471-3118-bdd8-35d1a88c56a3 | -9.93246 | -65.09878 | 2024-12-25 05:37:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0a3ac02-df3b-3512-83d2-7b522e458d62 | -11.43712 | -60.94231 | 2024-12-25 05:37:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c30c76e-0531-3660-9371-9f2b1ed557c7 | -7.89463 | -37.21637 | 2024-12-25 12:29:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 58.7 |
| f042e204-8dbb-3022-bc73-0c8cc75173b0 | -3.39639 | -41.47716 | 2024-12-25 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 4d0acb46-ccda-3e36-951c-a2ae3c43e005 | -6.16461 | -38.24512 | 2024-12-25 12:29:00 | TERRA_M-T | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 621741ce-fdea-36b3-909c-2a3c35c6ef71 | -7.8211 | -35.00167 | 2024-12-25 12:29:00 | TERRA_M-T | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| 1908803d-6a4f-3926-b1a3-4f18d8acd858 | -7.82954 | -34.96944 | 2024-12-25 12:29:00 | TERRA_M-T | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 111.5 |
| cd9a0c53-2cd5-3473-995b-61629b858ca1 | -5.91759 | -38.13515 | 2024-12-25 12:29:00 | TERRA_M-T | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 884fbccd-d71f-34b2-b957-7e97474d1eeb | -7.82582 | -34.96363 | 2024-12-25 12:29:00 | TERRA_M-T | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| df999fdc-38d2-3f0f-ad05-69cb484ee2b9 | -7.89773 | -37.19048 | 2024-12-25 12:29:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 35.4 |
| d1432f5f-f0b4-358d-8d3b-2749a457e9e2 | -5.92027 | -38.11481 | 2024-12-25 12:29:00 | TERRA_M-T | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 47.6 |
| 7671bed6-e242-3969-92f5-4319d19d292e | -2.32112 | -45.77829 | 2024-12-25 12:29:00 | TERRA_M-T | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1d94ba92-9599-395a-b9e1-b73c33928c0c | -7.89132 | -37.21054 | 2024-12-25 12:29:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 75.4 |
| f0b585b5-c134-3491-a32b-2fbce45ff2e8 | -7.06702 | -40.68454 | 2024-12-25 12:29:00 | TERRA_M-T | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| e93b844f-1e1f-3985-a15b-4fb7e7ad1e79 | -5.11337 | -43.96902 | 2024-12-25 12:29:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 8e5cb5f7-2cf3-3b7a-b5df-b2e547aac8cf | -7.06884 | -40.67114 | 2024-12-25 12:29:00 | TERRA_M-T | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 78e452a3-0999-3f72-a5fe-6accd7db98cf | -3.39791 | -41.46661 | 2024-12-25 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 078404f3-104d-3945-8ee5-00de62cec2e8 | -5.2111 | -39.82003 | 2024-12-25 12:29:00 | TERRA_M-T | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| c4971e9f-48d6-3b70-9cb1-7e8e75104c53 | -2.31967 | -45.78803 | 2024-12-25 12:29:00 | TERRA_M-T | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3242f6b9-eba6-3600-9511-3084b390e481 | -5.1121 | -43.97785 | 2024-12-25 12:29:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 383d16a0-58c1-36be-8916-40f332e09dba | -3.40115 | -41.47334 | 2024-12-25 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| db737fd1-00fc-39f7-a118-c6e854a2ce67 | -4.26135 | -38.19611 | 2024-12-25 12:29:00 | TERRA_M-T | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 01989e58-8916-3e3e-9589-9d8f5d8589e4 | -23.31086 | -48.67253 | 2024-12-25 12:33:00 | TERRA_M-T | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 766673fd-82ed-34b5-b81d-8583d318312b | -22.55607 | -46.566 | 2024-12-25 12:33:00 | TERRA_M-T | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4451e6ff-3add-325e-b94f-f5ac7a3faf44 | -21.2372 | -45.76121 | 2024-12-25 12:33:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2d54b9d8-4ded-3874-ae02-8d7fa1b53d0b | -19.79661 | -50.03677 | 2024-12-25 12:33:00 | TERRA_M-T | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |


