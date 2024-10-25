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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| debae1e6-7d26-39c5-b39e-0673465be631 | -5.72268 | -43.78004 | 2024-10-25 00:28:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| aee39c86-1789-37c2-ab91-d564ce3a11e2 | -5.80075 | -43.40014 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 76417d72-c932-392e-a076-a2d04970f404 | -5.8205 | -42.74123 | 2024-10-25 00:28:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f30a1bcb-a321-3568-b961-cf4f43e89550 | -5.9051 | -43.02326 | 2024-10-25 00:28:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 34dc1d06-99c8-3d2f-9d7b-9fa088bca0c8 | -3.95707 | -46.44613 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 8f8dab54-ad82-3407-8d87-408058815561 | -3.95514 | -46.43173 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 122.8 |
| e4e2dd3e-5b25-3a29-bec7-b5a462e96337 | -3.94598 | -46.44711 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c2111e58-8039-3683-ada3-0a033c710204 | -3.94409 | -46.43295 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| d723f6fc-ddcb-364f-a548-87a0a6633288 | -3.94225 | -46.41908 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3180d304-f904-3a63-8424-30e3efcb570d | -3.93404 | -45.83012 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1b3e7d29-7d47-35ca-b4dd-1ba6e61e863f | -3.93309 | -46.43447 | 2024-10-25 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| cdd92f1d-7bc1-396a-9664-0dc7ef3d4a3b | -5.90535 | -42.75742 | 2024-10-25 00:28:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 6e3c0260-3fdd-3f50-93ff-9864543125c4 | -3.92872 | -45.83653 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 2ef56eb8-ec72-3fc0-b5b0-7ca26745bf22 | -3.91239 | -48.37529 | 2024-10-25 00:28:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bbb099a5-ce9d-3c5e-9d3d-180858590199 | -3.91081 | -48.36048 | 2024-10-25 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9109a3c6-0265-3f09-be1e-fde26bc0351e | -3.84704 | -45.39736 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e91db5a6-acac-3603-b4bd-e8c7b91336e6 | -3.83972 | -44.07697 | 2024-10-25 00:28:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5d2a80b5-23d1-3861-9133-5ac908ae8f7a | -3.75727 | -45.80186 | 2024-10-25 00:28:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c2f44754-a0ac-325a-a649-9b788d306662 | -3.6669 | -50.12767 | 2024-10-25 00:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| e0a2b38b-6e74-320d-a65b-0efa6402cf7e | -3.65213 | -50.12987 | 2024-10-25 00:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 99b99de1-8437-3047-a59f-60b8952ff8d8 | -3.60728 | -47.26134 | 2024-10-25 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eaad24ed-0400-32e4-9575-9daa672ab8f4 | -3.52138 | -51.07267 | 2024-10-25 00:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| a3645325-6393-38ac-b42d-57e284c4d159 | -3.5146 | -51.06844 | 2024-10-25 00:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 7792071f-c805-35d5-8dec-3fec9b85ff73 | -3.47447 | -45.66891 | 2024-10-25 00:28:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 3eec00e9-75a9-3026-8583-85f901df8708 | -3.47282 | -45.65667 | 2024-10-25 00:28:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 157.5 |
| f1c4c2c2-a466-3cc6-af40-44dc5480cf00 | -3.46416 | -45.67032 | 2024-10-25 00:28:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4710fa1f-2a26-32d8-8691-00db256c7f4e | -3.46253 | -45.65812 | 2024-10-25 00:28:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 56e92f8e-93ba-366c-a741-eabe0fa8ee4b | -3.46104 | -47.67202 | 2024-10-25 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 309f64f4-ae28-3084-8130-7fb727af6ac8 | -3.44853 | -45.69125 | 2024-10-25 00:28:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a6489d56-7981-370d-9066-ac3ca69b82bf | -3.22874 | -49.12308 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 59b29a38-2965-33dc-ad1a-691680815a01 | -3.44683 | -45.67904 | 2024-10-25 00:28:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9f0d8228-ecd5-33df-a1d3-da648bb36484 | -3.4193 | -49.54336 | 2024-10-25 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| ffd58288-3f25-3d38-a8ed-2ead6e9222c1 | -3.41597 | -49.51911 | 2024-10-25 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 5c517f27-c6dd-3321-9de2-af78b2fcd753 | -3.4137 | -46.10101 | 2024-10-25 00:28:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fa15d177-70d1-3686-8863-7fb490be4658 | -6.01983 | -41.12488 | 2024-10-25 00:28:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 023423b9-4e1e-3edb-8c14-58f9a7456c95 | -6.05267 | -43.8924 | 2024-10-25 00:28:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bf7111f6-ad00-3f43-82a9-0748545be436 | -6.0541 | -43.90275 | 2024-10-25 00:28:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5f200f27-6a35-3b13-9bdc-0907763c4518 | -5.72149 | -43.84216 | 2024-10-25 00:28:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f9d89fd2-e066-3a58-a0a6-7f3b4b51dd5a | -1.04105 | -47.61253 | 2024-10-25 00:28:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5358a997-e85e-3903-b896-1ac638220df1 | -3.40979 | -49.53798 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 1043828a-9ef0-31e1-bfa8-ab3e724375be | -3.40666 | -49.51368 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e886bd49-9dc1-3c1b-ab56-69607ece81cf | -3.40523 | -49.54524 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| fe4374fd-9078-3c1a-bcab-e5edef754c71 | -3.40193 | -49.52097 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 901bf3f2-6d28-3373-bce6-aaa6ad97e88a | -3.38306 | -45.44366 | 2024-10-25 00:28:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65a7d6db-3bb9-3e47-8da9-6f40e5970f13 | -3.31773 | -49.53254 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 50c651fc-812b-35ac-8649-9a2a136b96a7 | -3.31309 | -49.53857 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| b8231221-32f1-3b0a-9a4e-cf1130a08f46 | -3.30976 | -49.51422 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| d8ab7526-8d28-3878-90c2-bb9561983256 | -3.30162 | -47.03341 | 2024-10-25 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5d404ba6-cbe8-3c60-be82-99c40866a626 | -3.29335 | -50.17411 | 2024-10-25 00:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 47c57358-9fbe-3c04-9543-3c7f51e3752e | -3.27141 | -48.46957 | 2024-10-25 00:28:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bdcb11df-31cc-3c65-b1b8-39b47cfd4358 | -3.2706 | -48.46313 | 2024-10-25 00:28:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 06ff3fb7-14bb-3008-9a37-6ecbfb5570e9 | -3.25268 | -50.20767 | 2024-10-25 00:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 78e490c0-803c-30db-863a-50bc071018d0 | -3.25249 | -50.21317 | 2024-10-25 00:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 7ddd0fc7-d05b-3f50-b865-dbdd9aa4183e | -3.25058 | -45.8185 | 2024-10-25 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 215.0 |
| d9149943-b346-39b3-bffb-679e8f5df617 | -3.24887 | -45.80606 | 2024-10-25 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 330.9 |
| 0f80e9bd-c395-337a-93b6-45e6ad0d86b2 | -3.22742 | -46.00703 | 2024-10-25 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0ad6bd39-e306-30a9-9c10-68bebe1ce618 | -3.2221 | -46.00199 | 2024-10-25 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8bb4e7ad-6e82-3896-a90f-f6862fc270d6 | -3.21689 | -46.00841 | 2024-10-25 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 212c8f8d-3f37-31f2-883f-996de6599ba3 | -3.21366 | -46.80813 | 2024-10-25 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b090f4a9-a39b-3629-bb3a-075f766a3ea6 | -3.21165 | -46.79355 | 2024-10-25 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| af32178c-30b0-32bb-a5f2-5570cbfc07e8 | -3.14948 | -50.46055 | 2024-10-25 00:28:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 97cd625b-b6a5-3c2f-8afb-4cd8217fa6c3 | -3.12371 | -45.71656 | 2024-10-25 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a1061e7e-fd33-30e5-88c2-79d48d8f833a | -3.12206 | -45.70441 | 2024-10-25 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ec793430-5155-3bea-92cb-12de0029d938 | -3.11506 | -45.73011 | 2024-10-25 00:28:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f3eec6af-161d-3adb-bcd1-0ef25dc301ef | -3.11342 | -45.71795 | 2024-10-25 00:28:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 7f5a2e1b-64f1-3e09-8f08-38fa349d6b88 | -3.11179 | -45.70584 | 2024-10-25 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 263.4 |
| bc04f1c9-be69-32d3-977b-2518898edde5 | -3.10763 | -45.29882 | 2024-10-25 00:28:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e7596f8d-b0d2-34ce-b9ce-2655e6ce7476 | -2.96429 | -50.43978 | 2024-10-25 00:28:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 37bf31de-cd43-3f84-89ea-cf2418a0ccc5 | -2.96047 | -50.4116 | 2024-10-25 00:28:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c8a8ded1-dc34-3188-ac0e-df00c3d43696 | -2.93623 | -45.46374 | 2024-10-25 00:28:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b36bffc-d3cc-3990-90d4-9a6479cf4f06 | -2.93462 | -45.45212 | 2024-10-25 00:28:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 81a7b81b-4d75-3cb8-91c4-bec4caf00541 | -2.92455 | -45.45346 | 2024-10-25 00:28:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 695d78de-74a2-391f-a53f-865f04bd2eff | -2.89369 | -48.28202 | 2024-10-25 00:28:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 6f2c45db-62e9-3a3f-a1dd-04a47bb42185 | -2.89265 | -48.28882 | 2024-10-25 00:28:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 61c51460-b552-3885-b40f-8b1717fd805e | -2.89003 | -48.27005 | 2024-10-25 00:28:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7a774a63-d11b-32f0-b841-ec2d8d43a9d0 | -2.83686 | -51.81032 | 2024-10-25 00:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 36195a36-eb16-39d2-aaf8-4e08d67d3d12 | -2.82561 | -51.80502 | 2024-10-25 00:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 56d94d06-4c4c-3af2-b02c-dd4d6d295e86 | -2.81697 | -49.25524 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 343.8 |
| 415f9c67-705e-37dc-94a0-56c25b4f75a9 | -2.81388 | -49.23277 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 7a3fdccf-3367-3319-8dc8-960f97c5fdc9 | -2.80338 | -49.25713 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 296.1 |
| f3380e16-2315-35fa-9c3c-50868650ee1d | -2.8003 | -49.23461 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| aae27b92-39bb-3b12-a713-817f5f6b2594 | -2.77934 | -49.49513 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| a6da14bf-fe79-3158-a356-3273f354d3da | -2.77365 | -49.50152 | 2024-10-25 00:28:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 6ae089b7-993c-39e9-8dac-247ce063538e | -2.65699 | -49.52395 | 2024-10-25 00:28:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 852785ad-6662-377e-8ca8-feb0553f8174 | -2.65379 | -49.5005 | 2024-10-25 00:28:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| da9dcaaf-e92d-343a-bd75-f9d671c4d546 | -2.64644 | -49.24503 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f0bb0a76-7805-3d3d-9301-ae830e3cdd94 | -2.6435 | -49.26168 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 406003af-fe60-3b0e-88f6-f2febf18bc5e | -2.64057 | -49.23931 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 842e97a6-b3bf-3501-bbcb-4aee37ecee0d | -2.63289 | -49.24689 | 2024-10-25 00:28:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 155.6 |
| d1cf1a01-e6d3-3ce3-a64d-591abf3aaf9f | -2.62354 | -52.47221 | 2024-10-25 00:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b6668e66-35b4-3105-b575-607ffd5554da | -2.62211 | -52.47767 | 2024-10-25 00:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ccbb4a18-84cf-3f64-8261-1723fdd94530 | -2.61831 | -52.43209 | 2024-10-25 00:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 368c6622-55eb-328a-adaa-49de63b4639c | -2.6166 | -52.43763 | 2024-10-25 00:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 59e3c2d4-82e0-3689-b20a-e807864517c0 | -2.60668 | -46.12868 | 2024-10-25 00:28:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 455b0bb5-aca9-3e3b-a6fb-3d38a21b3e20 | -2.44077 | -45.87179 | 2024-10-25 00:28:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c2212c82-557d-3676-85d0-3ce7f97a754a | -2.31943 | -46.24517 | 2024-10-25 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a639d610-f3ef-3712-a132-c8e785b73bc2 | -2.31763 | -46.23229 | 2024-10-25 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 55065f6c-73a5-3d68-bce5-65ddd39a40c5 | -2.30887 | -46.24664 | 2024-10-25 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3e3fc64c-a24b-3150-8356-db288038c552 | -2.30708 | -46.23377 | 2024-10-25 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 7d3504e6-bc00-3764-9373-da36052d1967 | -6.01859 | -41.11602 | 2024-10-25 00:28:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |


[Clique aqui para ver as próximas entradas](README8.md)
