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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1202cd4-6f62-3759-9de6-78605b5b8b3f | -2.64974 | -48.46791 | 2024-11-16 00:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5516ca33-f3b7-3891-89a6-e3b34fcf2f92 | -4.36614 | -45.62356 | 2024-11-16 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9ffb9b0d-a9c4-3c0f-b076-14fafd9376df | -4.70517 | -44.46964 | 2024-11-16 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fdc32edd-52e1-3710-9cd4-e1fb81a9e3e5 | -3.97831 | -45.80526 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 3b59f002-8f82-3538-912c-173e39b918db | -2.51751 | -47.47802 | 2024-11-16 00:24:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2f2c64a0-5617-30b3-bc7e-14f205385cb6 | -4.15622 | -45.43485 | 2024-11-16 00:24:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| a97e5419-758b-36c2-9570-beefa6f1a2f8 | -3.37545 | -45.42302 | 2024-11-16 00:24:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 49da87a6-4557-3e95-8bd0-fd7f40cebe46 | -3.74288 | -45.67294 | 2024-11-16 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f2770a1d-9c3c-3be3-ab04-ff9615433495 | -5.00118 | -44.3125 | 2024-11-16 00:24:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4341b32c-c25e-3009-bd7e-309338dfcd84 | -3.96226 | -44.04319 | 2024-11-16 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f023c50d-2687-3a8e-b554-dacc2378b67f | -3.96381 | -44.05431 | 2024-11-16 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2db10988-39b4-365e-8f56-56888c189ace | -2.11138 | -46.08384 | 2024-11-16 00:24:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f8eb31ab-08b6-3f7a-9a18-4b15a81916f3 | -6.00108 | -42.63325 | 2024-11-16 00:24:00 | TERRA_M-M | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| ec92c03e-9c7d-3b06-b98c-07534c31d486 | -4.18407 | -45.62568 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 31268616-a257-3930-9c50-05834388127a | -1.46864 | -45.74496 | 2024-11-16 00:24:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| dbcb10ee-68d2-3dec-99ba-59b4e02024ba | -3.74099 | -45.65874 | 2024-11-16 00:24:00 | TERRA_M-M | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8a19bb9b-c5bc-35b2-8743-d45a10bd80c5 | -0.69134 | -48.55698 | 2024-11-16 00:24:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 4912aa89-9bb7-3217-9a86-fa3013746a06 | -5.91026 | -46.22122 | 2024-11-16 00:24:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| fdb076e4-699c-33a1-981c-8db22b1b0889 | -3.79634 | -41.00031 | 2024-11-16 00:24:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 578e7a5f-e96c-3eef-a8d3-b882ec320b0f | -2.0997 | -46.59103 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 7e5e1315-1ebb-3276-b7ad-03edbe8868aa | -2.56851 | -45.2105 | 2024-11-16 00:24:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3c165c39-aa8e-30ca-9aa3-d0d503898a17 | -6.30225 | -39.48372 | 2024-11-16 00:24:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 88.0 |
| fbaf7a59-7635-39d1-9d26-888dea6b804e | -3.91553 | -45.84945 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9ccc405a-133f-3363-aa8b-611085867538 | -2.94648 | -48.02968 | 2024-11-16 00:24:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| cd71947d-8664-34da-8b32-209c5eaf9ec0 | -5.23562 | -44.91926 | 2024-11-16 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 89cc364e-1fd0-3173-ad61-47d2a358b61a | -2.34675 | -47.47514 | 2024-11-16 00:24:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| f19635d7-5c6e-3df2-8309-4eb06650f65c | -5.2463 | -44.91774 | 2024-11-16 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bba894e9-eef6-3a00-bbdd-73954590c79e | -3.2952 | -44.16624 | 2024-11-16 00:24:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b69dbc06-75a0-33fe-b5f2-644af4d93225 | -3.51279 | -44.41154 | 2024-11-16 00:24:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 93a9bfdc-aeae-3cef-a878-d8a87ffb249b | -2.66642 | -46.19513 | 2024-11-16 00:24:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 749d93c7-514e-3e63-8984-4732311ecbc1 | -5.42953 | -42.88683 | 2024-11-16 00:24:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 44e563f9-bbc0-32d2-b64b-6743c00c4596 | -5.78794 | -48.14971 | 2024-11-16 00:24:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 89e23239-5e22-3e84-872c-4c878ae0ae08 | -6.44513 | -47.85201 | 2024-11-16 00:24:00 | TERRA_M-M | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4b9ea344-112d-327f-9f09-b21a9ff7f5b9 | -3.9886 | -43.71306 | 2024-11-16 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c4d26a0c-9561-303b-9162-131dadcb9da4 | -1.52005 | -47.10139 | 2024-11-16 00:24:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| d20d40d3-1bf0-3ca0-95a6-16187cde36ec | -2.46186 | -45.46043 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 6e60360e-eca7-3e2a-8904-6f1e54e2c1fc | -4.1599 | -45.4422 | 2024-11-16 00:24:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6c4f4bb9-0ff3-36ff-a9c0-1363b36b90b9 | -3.29672 | -44.17731 | 2024-11-16 00:24:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b5732e23-d76c-33fe-abf7-d4d6dffd288f | -3.79289 | -43.91604 | 2024-11-16 00:24:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 47b45474-836e-3a3b-8f8e-d117602e78c0 | -5.70948 | -39.85301 | 2024-11-16 00:24:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 425ee578-4e26-3eff-b771-48b50c2fb56b | -3.9803 | -45.81999 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 886b50d5-338d-3ec4-9b8f-5ba870a2de65 | -2.85918 | -45.24283 | 2024-11-16 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3875b4a7-d3c4-38b3-ad2b-e72744e0f169 | -2.66435 | -46.18013 | 2024-11-16 00:24:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| cb03b852-73d3-3999-9614-21f622c46e37 | -2.63909 | -48.49249 | 2024-11-16 00:24:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 1b923a57-800b-3a73-b4c3-287839e8cbf4 | -2.92902 | -45.59707 | 2024-11-16 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| b6396057-42cd-3925-af47-a174dcddfafc | -3.59157 | -50.52974 | 2024-11-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 362335a8-f00a-325e-bf61-03573ea8027c | -3.69089 | -50.1073 | 2024-11-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| af04dd5e-25b7-3b2f-8505-1d6fd2cdc8f1 | -4.18567 | -45.6465 | 2024-11-16 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 17be0641-6e1e-3aa8-96fd-e5c69924648a | -3.96707 | -45.80677 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 33.9 |
| b9bb6d42-ae63-305c-84fa-1f7ba623153a | -3.18161 | -42.07502 | 2024-11-16 00:24:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d7a136d7-bea8-373c-a092-73a26ea21603 | -2.49925 | -46.23008 | 2024-11-16 00:24:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 41.7 |
| d34a2d27-a0a6-3f75-bc7c-cfd248b972e4 | -4.91125 | -44.02857 | 2024-11-16 00:24:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f3298535-b376-31a8-9748-d47f89aff0b2 | -2.86091 | -45.25568 | 2024-11-16 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7ddcdf36-4345-36b3-800f-e3d21e3922d4 | -4.86135 | -42.70185 | 2024-11-16 00:24:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9d20b2e6-1341-3e58-aa29-72273405324e | -2.56296 | -45.2169 | 2024-11-16 00:24:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1b451499-7d7f-31c9-abb3-a2faf681ec71 | -3.75562 | -44.39551 | 2024-11-16 00:24:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d318fd1d-7aff-3f64-82e0-f1d685d0b2e6 | -3.29141 | -44.06615 | 2024-11-16 00:24:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 141557cd-64e8-37ad-8bb5-afe10a0e299f | -3.75405 | -44.38389 | 2024-11-16 00:24:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19637001-e3e1-3705-af37-83ac13af278c | -2.65098 | -46.16679 | 2024-11-16 00:24:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d221295f-ea46-35d9-814a-37fe8be493f5 | -4.56304 | -48.01286 | 2024-11-16 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| c9b83fad-b5b9-3292-96a1-5e778f10126e | -2.15553 | -46.5674 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 79783fdb-cc1c-3bf7-a645-c0a34569ae20 | -4.22252 | -47.23372 | 2024-11-16 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 7631f504-ff16-33a9-8c25-979d68b8183c | -1.7665 | -46.24467 | 2024-11-16 00:24:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b9deaa9c-0143-3674-919e-66d52f0650ed | -2.66495 | -46.84819 | 2024-11-16 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c2b5210d-ccb4-39a3-99d1-2ac4a0e259e2 | -3.58464 | -50.53767 | 2024-11-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 81393c8a-0633-3d77-85a6-1376bbd05d47 | -3.99006 | -43.72365 | 2024-11-16 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| c205c684-2aab-388d-8e62-4dd09e770313 | -5.95271 | -44.47145 | 2024-11-16 00:24:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a073eaed-e68b-3982-b5ab-79bd810978ea | -1.2387 | -47.70634 | 2024-11-16 00:24:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 136202eb-6941-3936-a13f-09f41538bded | -1.47046 | -45.75822 | 2024-11-16 00:24:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| e2a3e7ed-b9c3-3386-99fa-d210fee684c3 | -5.12076 | -45.1601 | 2024-11-16 00:24:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5ddd4879-866d-33cc-bd75-4bfb44e18c38 | -4.22043 | -47.20793 | 2024-11-16 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d50fe03b-7a71-3a2d-85a1-c47a3a750128 | -2.3576 | -47.15325 | 2024-11-16 00:24:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c773d52a-a719-3443-92bf-0e72089d3e86 | -5.67048 | -35.65766 | 2024-11-16 00:24:00 | TERRA_M-M | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 0fc5b1b0-553b-3420-982e-8f2b10147f49 | -3.4665 | -43.40535 | 2024-11-16 00:24:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0daf345a-043e-368b-97fd-508b50e0a054 | -4.33938 | -43.80426 | 2024-11-16 00:24:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ebcf18ea-3bb2-3aed-8797-3d3d8ea7058e | -6.30094 | -39.47456 | 2024-11-16 00:24:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 6318949e-96c9-3e96-a142-14d7b4257b60 | -5.71669 | -44.80415 | 2024-11-16 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b0a10606-83dd-330e-8273-24bcbf069073 | -3.01199 | -42.98335 | 2024-11-16 00:24:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 94c6b9e9-8d05-3f14-88b8-dd83577f57dd | -2.02515 | -46.37213 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ce85c22a-ac57-3544-a28d-0d0971699597 | -4.00223 | -44.3313 | 2024-11-16 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 349d04ff-7ffb-348a-9f54-785ebe67e420 | -3.72166 | -45.85805 | 2024-11-16 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a940b097-0ca8-3c9c-bb48-4d4e9bb1c821 | -5.90039 | -46.23966 | 2024-11-16 00:24:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eac5df92-e777-39ba-9e60-3c73a4ec7d41 | -6.04495 | -43.4987 | 2024-11-16 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1b90f66d-1ec9-3db0-b5d7-869e5507ca21 | -5.4875 | -43.76369 | 2024-11-16 00:24:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| aa8e856e-2af8-36c4-b255-68ca4f0d2b6a | -4.18366 | -45.63205 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| c3fb84cb-1d4c-3ed0-b02b-f7bf5c83f68b | -1.17286 | -47.07184 | 2024-11-16 00:24:00 | TERRA_M-M | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5d870d87-3b37-38f3-9e9f-be670f8a5c97 | -2.64403 | -45.16824 | 2024-11-16 00:24:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9e65d884-b0e6-3cb5-bcc7-770eab835e49 | -4.01738 | -44.58802 | 2024-11-16 00:24:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 22c3c84f-e3bf-3c43-9986-7acee350b476 | -2.93087 | -45.61066 | 2024-11-16 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f1c873d0-b9a9-37c8-8d21-73e5f304e706 | -2.64596 | -48.49697 | 2024-11-16 00:24:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 609c0411-5b0e-3fd7-96d9-e9589d7d012b | -3.1272 | -54.5464 | 2024-11-16 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 2360c86e-0ba5-3504-9046-2e8586607a3f | -3.5439 | -51.4844 | 2024-11-16 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6e0e870f-392c-3ded-a334-95cc54fa71d5 | -3.7685 | -50.7908 | 2024-11-16 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 25946df0-b3f9-35da-a1e2-70467d2ae960 | -2.6131 | -54.5381 | 2024-11-16 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 22fef266-b625-3c6d-b931-895a39251635 | -3.1456 | -54.5259 | 2024-11-16 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 4b5f5aa9-73eb-3777-83d7-285dbac4b990 | -3.5083 | -47.212 | 2024-11-16 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9324b7b0-6bee-3dad-8f6f-9879761fd65f | -17.5879 | -57.4917 | 2024-11-16 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| b1d0b645-0572-3b81-9df0-f0166f9aa796 | -4.3723 | -45.6212 | 2024-11-16 00:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5b11622c-3f7f-3332-be0e-93b4af8b10e6 | -2.1378 | -53.7244 | 2024-11-16 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 7cc16fb0-97f3-39ac-8c52-8728f4181009 | -2.5767 | -54.4188 | 2024-11-16 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |


[Clique aqui para ver as próximas entradas](README5.md)
