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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6723e5e7-28f2-3234-bf60-25cbd4bfd4c6 | -7.99097 | -43.83173 | 2025-07-25 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 66fa179d-eaf5-3c50-8bca-a3cbc2c38598 | -6.99089 | -47.08307 | 2025-07-25 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c262aa7a-6b89-366b-b881-58f6952903ae | -6.95356 | -44.55973 | 2025-07-25 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e65fafc7-78ac-3235-b76a-7d02443ccae2 | -3.05184 | -47.37862 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42231fb4-2243-3117-a46a-de73db3f052b | -3.04826 | -47.37809 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8111110-2088-3db0-9c95-e011c74b2240 | -3.14546 | -53.1348 | 2025-07-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ec77221-603f-3751-a9d4-80c5337b5fe3 | -4.35373 | -47.68892 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 9ad825cf-1ded-3fdd-b2a0-73debb92dba5 | -6.98365 | -43.3195 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3eefdd22-6ae4-3241-95da-e51e140cc422 | -6.49363 | -50.26602 | 2025-07-25 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d50b1db6-baab-367c-98ab-3ef424087306 | -3.30959 | -51.66724 | 2025-07-25 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0aa29c8-d538-3658-bbff-a268c4c1359e | -6.98287 | -43.32511 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d2fc78eb-6a79-3ca6-874d-ee0b59f135aa | -7.86463 | -48.21591 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bc6b44d-ae11-3b58-9d53-c2d4c7948ebd | -5.22757 | -46.08921 | 2025-07-25 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f9cc679-573d-3fbb-badd-648f63457f1d | -7.91213 | -44.08726 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0f6bad64-ac56-30bb-a080-b2a3ebf1019a | -4.10514 | -47.93642 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79a60e0a-6710-3491-8c0a-9c0760975e6d | -6.58089 | -45.60416 | 2025-07-25 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad5d0126-5632-350f-91b2-24cf62b088d9 | -8.0739 | -43.1516 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1062c5b4-a53a-3425-8dec-3b87c005e66e | -3.49669 | -51.17641 | 2025-07-25 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51574a84-77c9-3793-a117-28eaf256e6d2 | -7.92091 | -44.09373 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eaff04ee-186d-3eb9-81ab-c661a9bd1e34 | -7.49824 | -49.22039 | 2025-07-25 04:44:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79df51ce-0aa6-340f-bbcc-1d97ee199003 | -3.74243 | -49.04687 | 2025-07-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 745f2a70-34d7-305c-b256-11e1df432009 | -7.91209 | -44.08018 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d3a4f178-bdcf-317d-9872-4765b21f3e7e | -7.24425 | -43.06156 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 314a4dd3-d9ac-33d6-a9ad-1f57c3d2d61d | -3.17348 | -49.45341 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1edd2f3-1d69-3ac1-b1f8-6ad437bcbbd1 | -4.57351 | -48.0195 | 2025-07-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8a271f58-11be-3a17-9498-2d37b71e81f7 | -3.31016 | -51.6637 | 2025-07-25 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cccdc42-f45f-36ec-b287-948bcf344ebb | -7.92636 | -44.08915 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e82ebd96-0c40-386d-9ee1-fd70dc1f837e | -7.91061 | -44.09048 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 32082e5d-e04d-304a-a922-5a2a89ffa706 | -3.74636 | -49.0438 | 2025-07-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98687120-f1c8-35a8-88ee-775d713eb1cb | -6.40419 | -47.38691 | 2025-07-25 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48d8f315-c7b7-3214-8a15-633e416a8227 | -7.47997 | -49.23017 | 2025-07-25 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0820867-8756-3fca-9f23-5f991679c19e | -7.2539 | -43.06595 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| eddbe4b3-c1b9-3d19-9ebb-eb0abc802bef | -6.63537 | -56.29244 | 2025-07-25 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 318c2235-a01d-3b96-bc63-381a48ec9066 | -2.91492 | -48.23791 | 2025-07-25 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5b36106-90f7-3d4d-aacb-351de421908d | -3.12019 | -47.009 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a38c6651-ec60-3a7c-b107-c115f2518901 | -7.0379 | -55.50086 | 2025-07-25 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96cde088-98b7-35d6-bca9-218772e78e4a | -4.83722 | -45.30487 | 2025-07-25 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b81573ca-ca2b-3c40-875f-00b7bcdf2f8b | -2.3906 | -47.62785 | 2025-07-25 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b9112ed-13c6-3c7f-a1bb-a238d100963b | -7.85569 | -48.22004 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1523f59f-792c-3abe-8f70-18b38bfddacd | -6.33814 | -43.74741 | 2025-07-25 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e3ac51f-e547-3a5e-b480-ce475f1888a0 | -8.3337 | -44.95357 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bacff054-7125-352b-8f8f-edee70eaafe8 | -7.85996 | -48.21637 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa23beaa-42bf-35ab-9c12-edac227c6b84 | -7.91144 | -44.0924 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 88e32d9c-35fd-3035-98b6-26a6f46dc6c5 | -4.29272 | -48.05646 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30b0453e-ace7-3360-a8e3-31c6fea32bae | -8.28671 | -44.99422 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22b715c8-1bd4-36ae-b63b-3db9dec98305 | -6.22647 | -44.52881 | 2025-07-25 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02c77379-72f5-39b7-b554-0d193d11e877 | -7.25432 | -43.06296 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2710fcc3-4a5f-39c7-b752-9b35f00b7b7b | -7.19446 | -45.32608 | 2025-07-25 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c55e7e5-0c47-3410-aaf2-ffa3dd9d85af | -7.92483 | -44.0924 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dc1deca8-da32-3c33-aa96-c934cfbda23b | -8.09454 | -43.15165 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8caca819-4833-3c5a-948a-7c05a3c48131 | -7.26314 | -43.07332 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 677853fb-4057-3590-96a6-44d428f96e26 | -3.05543 | -47.37917 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9de5a188-5e8d-38df-86df-74bcda6be59f | -7.91608 | -44.08599 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ee550823-a088-3a0c-aa63-9a10dad2ffba | -7.36167 | -43.43564 | 2025-07-25 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16977c35-a214-3da9-8187-93c119b7b7a3 | -7.88126 | -45.53834 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4092c6e0-eeab-36b3-bb1b-40b811360cc6 | -4.45419 | -49.15111 | 2025-07-25 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 860f0c62-f3a2-3659-a402-4b55b03089dd | -6.22713 | -44.52431 | 2025-07-25 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71b075a1-8dae-3079-ae7a-50884f960f41 | -7.85441 | -48.22844 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd41e830-bb01-3d81-b483-29b1b359f554 | -4.10577 | -47.93242 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6c5b2a9-5044-3dba-9d8d-62720e55cfee | -7.85505 | -48.22424 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ff4c27a-4972-3b70-9ce3-c174620a8e45 | -7.85676 | -48.21901 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d94f63c7-7656-3233-adbd-943de13193eb | -3.32645 | -48.72081 | 2025-07-25 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c05f923d-c0f6-3e81-8c7a-6938c5953d3e | -8.288 | -44.98518 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 331abaad-d908-34e4-aa7d-42d22c8dfad4 | -8.51066 | -43.31858 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 3c9b0094-e188-3d8e-a41b-2fba3d60ef3e | -6.41279 | -53.33123 | 2025-07-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d0cd1734-a58f-3e84-8496-31f954d984fc | -6.89978 | -44.21859 | 2025-07-25 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3145450-0a76-31e4-81e9-8e83683816f6 | -6.9935 | -43.321 | 2025-07-25 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f06ee16b-d924-3f84-928f-96af92358aa3 | -6.87277 | -45.23576 | 2025-07-25 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bcfe834-ba7e-3f1a-868a-0132caa1eadd | -7.19183 | -45.3265 | 2025-07-25 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a600609-ed86-3089-8bef-ca2a2335c350 | -3.24626 | -51.10499 | 2025-07-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55b45821-2f1f-332c-acf3-21849d79f81e | -3.04405 | -47.3816 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b61a9da8-e356-345b-8968-71478dc844ce | -6.40872 | -53.33446 | 2025-07-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5082f3e-f4f4-3fba-b528-a37f452b8edb | -2.32978 | -48.61711 | 2025-07-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 699ffc43-c9f2-3c4d-90b0-89155daaf676 | -6.40528 | -53.33389 | 2025-07-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 279161c8-1c01-3366-877f-50799604a64f | -7.25852 | -43.06964 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f468c811-c672-3d2a-b657-9f209eebd5ae | -7.861 | -48.21533 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44d9a4fb-edac-3a1a-b3f1-22bd9bfe4899 | -8.28607 | -44.99873 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c588496a-eea9-34b6-bf8c-3175d9c9caf9 | -7.91934 | -44.0969 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 54f543a7-9b51-3345-b8a4-1572a7349973 | -6.87334 | -45.23187 | 2025-07-25 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45d224ef-8d91-3f44-9577-3f5815a44679 | -7.30102 | -44.01964 | 2025-07-25 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 017d8076-404d-3dd4-9160-103c3cd7012c | -3.32363 | -48.71663 | 2025-07-25 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8576390a-155d-3c8f-ac2b-0a27e0aa820b | -7.36387 | -48.1393 | 2025-07-25 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30200ec6-a616-3a55-b752-58f97ad7a9c4 | -7.92161 | -44.08859 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 15e0972e-f0f1-3451-be9c-b36230d1b523 | -6.98857 | -43.32027 | 2025-07-25 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8dc661bd-757c-3b01-ba8d-f296b312ee3b | -7.85633 | -48.21582 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0fd5bb8-263b-3c36-b9c0-fcdde7e0addc | -7.6053 | -49.94492 | 2025-07-25 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a6a171c-5561-3f90-bbe3-03221a4314b6 | -7.35996 | -43.43407 | 2025-07-25 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd165604-8455-31ce-ad28-5d9c1ab820e4 | -7.88186 | -45.53423 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04e49c9f-f465-3388-bc8b-719830626aa7 | -8.20529 | -44.93906 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e171435-65c0-314b-87e3-64077ab41e6a | -7.88922 | -45.54377 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbf2a5a7-9c60-3a3f-8aa7-cd5bbb2cdb21 | -6.94971 | -44.55441 | 2025-07-25 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3ab53240-7ff4-342b-84aa-12576f70a1d5 | -6.9529 | -44.56429 | 2025-07-25 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 42051227-6f6d-3cdd-9172-1a58aead4dcc | -6.22201 | -44.528 | 2025-07-25 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb479968-cfb5-3a1e-bee6-afb457d1fd15 | -6.92177 | -44.22419 | 2025-07-25 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c11fe165-a63e-340c-97cc-95b307d6efa5 | -8.33435 | -44.94901 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7a14b67-0ef9-359d-9589-cfd60dca11f6 | -8.20978 | -44.9397 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41bf3893-1578-3bc4-9a2e-813595406f8c | -6.87862 | -43.11737 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a1e90e9-2934-3d85-addb-1aced6917a32 | -3.04343 | -47.38563 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92730811-890b-3b6c-8d4d-97215f60ae80 | -7.53574 | -42.42261 | 2025-07-25 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c32d7288-a6af-35b2-a1eb-bfc3df60c4f5 | -6.88197 | -45.24828 | 2025-07-25 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README21.md)
