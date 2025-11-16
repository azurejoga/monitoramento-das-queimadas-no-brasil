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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 407e9b9c-dcf3-3e5e-a48c-8d08c9fc22d0 | -8.05858 | -43.10812 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 84d0bd84-67ee-3086-b47d-0b93e65c78d3 | -11.71424 | -48.87136 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2724c12b-e4b7-3572-abe9-ba91cbcde41e | -7.8982 | -45.46948 | 2025-11-16 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f3ddfdf-e48f-3dfc-8624-109c405bda44 | -5.74872 | -42.50586 | 2025-11-16 04:08:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 783a6e32-6b01-3806-b12f-1580eb62b0ee | -5.61658 | -44.45831 | 2025-11-16 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7494837e-ec7e-31ce-8ba6-b372844bc305 | -6.39839 | -42.29264 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d57c9029-9332-35fa-8bf8-2a50ed044a7c | -8.30356 | -43.80344 | 2025-11-16 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d94e6d8a-2841-31cb-81ee-bb20e7eec4b5 | -12.65339 | -46.74929 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 45714177-917d-341d-bc72-455d5d8a9956 | -11.66127 | -49.6211 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b85d2893-9672-3149-a339-ac6a708199fa | -11.87846 | -48.99463 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f974216-1163-31cc-9bbe-1624357a624c | -11.8477 | -47.60385 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0c6c6bf6-3f73-3473-9c10-1d89fb0f80b8 | -10.17326 | -44.49709 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8247866e-9c5d-329e-a01f-931e1fa042f6 | -10.62152 | -44.58947 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d66cd6f2-f2c7-3a05-aee4-643445c48c58 | -12.65991 | -46.74365 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b58a054-09e0-32c5-8166-74ec88ec4d55 | -9.14352 | -45.15716 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ca4ebdd-bcf6-36f0-a6c6-d8e8acecb48d | -5.99291 | -41.91446 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 954a7af2-08f3-37f6-876d-73d7d1f301c1 | -11.85111 | -47.60093 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f57e2942-fd18-37b1-bd12-2d32fb9582f3 | -7.29553 | -45.10375 | 2025-11-16 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c22d251f-79b8-3b92-9187-52cc0408967f | -6.95275 | -38.4038 | 2025-11-16 04:08:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 091554ea-c55a-3457-ac1d-8b77236c6865 | -9.34812 | -46.58766 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9fe8002-a660-3844-ad50-d7af9b5273e9 | -6.24557 | -41.7139 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4dbbb106-6e73-3b44-87a8-df6f3a1f0df4 | -11.84859 | -47.59867 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd006d93-f080-34d0-b393-308998d7f4c9 | -6.86558 | -47.0769 | 2025-11-16 04:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 738fc0b8-82c1-3988-9d68-b8138451073f | -6.53874 | -43.41219 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac10bc83-b663-3249-a6f5-ddc3e45e1d9c | -9.7445 | -43.95946 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c0fb9b6d-a7e4-3b47-b8b8-d9680cd388c7 | -13.11731 | -43.26945 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f8c7b3fb-481d-3780-a10c-61149c46f1fa | -8.1472 | -35.69455 | 2025-11-16 04:08:00 | NOAA-20 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b655e379-50e2-3caa-81cb-37c7e183fffc | -6.40407 | -43.63984 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1c5cb68-7d4c-37f6-979e-7f879f19963d | -10.39151 | -49.05438 | 2025-11-16 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe2288cb-ff03-3cc4-acc3-57a6e696d4a0 | -5.99953 | -41.91551 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d8ef2b5-f401-35bf-ba5e-511661f004e5 | -12.40323 | -47.55706 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02035baa-fc07-3fb6-a214-0e4a4ea78957 | -6.01056 | -41.91016 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e2228310-4e59-3fd8-ba06-494665bf421e | -9.83958 | -44.17624 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec04ce26-bdaa-3243-81c1-91b1a61b0943 | -12.2038 | -49.54778 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb1af243-96c7-35aa-a34d-9cd2051bba46 | -9.96434 | -44.93212 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79485f5b-d406-3065-a9c3-01567adfa4c8 | -6.81491 | -48.79274 | 2025-11-16 04:08:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 748f5f56-6120-3d53-bc21-ba0af445c6d6 | -12.06607 | -48.22234 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9a837e0-9f1c-3697-b470-85bf3dd661ed | -10.84707 | -44.09024 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 627fa97b-d8aa-30c1-8096-986d18766047 | -10.11634 | -43.90014 | 2025-11-16 04:08:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d4507b9-94f8-34c7-88b0-ce8fdc7a45e3 | -6.07417 | -42.87611 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| c2353fd8-5d28-3fc7-9a4b-0a7a133d59d5 | -11.95852 | -44.95275 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a734de1-0d9a-3f3e-98b4-a4bb83962b0f | -5.88242 | -46.44649 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39c08a84-00c1-300f-99a3-079979bf01e1 | -9.84907 | -44.71254 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5dd81c1-3d38-34a8-8e4f-8eeb24e58e2b | -11.99581 | -49.27267 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e8b9a5a-920d-31b5-86de-e8948f8c4c81 | -9.15045 | -47.12905 | 2025-11-16 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5729c2ea-e5f0-3ce8-962c-57cad0815cb2 | -9.01593 | -46.00557 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce98d41-eef4-32c5-b808-c6934f87aa87 | -10.33075 | -44.6047 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb508757-b34d-33f9-af33-80405ef8b5e3 | -6.31935 | -43.8131 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63433d21-f168-3c1c-8f93-0d0f78500b0b | -6.06797 | -41.54751 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f982ae7-3d62-3333-b6cd-6d833ead2497 | -6.92551 | -39.62483 | 2025-11-16 04:08:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6e3074a5-b30c-349c-b602-7af71c2e94f1 | -6.89377 | -42.06138 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 15e33078-4410-34a1-b887-6f81dc9d28c5 | -7.35466 | -43.33874 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6ab7acf-7d99-3d00-ace2-b27d48e45e9d | -6.20111 | -39.73524 | 2025-11-16 04:08:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a940102-a35a-3dbe-ac56-a907a2f80503 | -6.36465 | -39.6282 | 2025-11-16 04:08:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a995b8a3-be79-33b1-9d75-96b66a6cbffe | -12.40165 | -48.10073 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2605354c-cf1f-3e9e-badc-a29084f61128 | -12.65786 | -46.74546 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c64e2e7a-6013-3603-8eee-6645c3ca172d | -10.86328 | -44.50409 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90bfa499-61cb-3f1f-9aff-9f5dc1415c23 | -10.10307 | -44.77329 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1dfcc22-cff3-36c3-9e78-c17757373eeb | -11.70925 | -48.87454 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b0046ca-4774-313b-8292-61edc7e85964 | -6.96467 | -41.52688 | 2025-11-16 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6a0621f0-df30-3318-b0c4-f53f84fe7caf | -8.09496 | -46.03333 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22d28168-539a-3ee4-b0f8-24b6e9946899 | -9.85783 | -44.1717 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f5a48ef-da9c-3ba3-95a1-f90c6c1fd3fb | -6.07138 | -42.87196 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c61b94a3-e701-3cb1-b81a-e3e8d8d5ee9a | -6.029 | -48.18718 | 2025-11-16 04:08:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d26e054c-3b01-3019-85bf-71dde96433e3 | -7.35922 | -43.33202 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b70eb4dd-d962-3063-8d18-bcb684a0016e | -11.82677 | -45.5318 | 2025-11-16 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f42bde8d-afc0-387c-aa2d-9e028825ee1f | -9.72697 | -43.9603 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ada947dd-ca27-367b-8311-44129ceef96b | -8.31664 | -45.41188 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7530f036-2403-3946-80d0-c013912d9dec | -12.00457 | -49.27431 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7c62696b-92cb-3f2b-9dfa-131f98296180 | -9.50968 | -47.27277 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7729d8d0-b96a-3996-984f-2d05319a75f0 | -6.28467 | -41.72363 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b067eb7-6e98-340a-a381-ed3bbf082419 | -6.06812 | -41.65351 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f28119e3-b36a-3213-aabf-f8e06c7826fe | -5.96506 | -43.75466 | 2025-11-16 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69ea1629-a76e-34b1-bfb3-b5263773f6ba | -6.81573 | -48.78797 | 2025-11-16 04:08:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc52d51e-3ad4-3d9c-a829-c2a787ca9e24 | -9.06205 | -44.75114 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 795fd583-5370-35b2-b3c6-c7e89227f92c | -7.05019 | -42.23256 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f2881879-494b-3d4e-8da0-ec7fa9f76226 | -11.72882 | -49.84598 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59b95677-9b6c-3d94-8201-4304f8c546de | -9.72917 | -43.96823 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 59a5dbe3-6c25-32f2-9346-4e9c3764b08b | -12.06 | -48.21363 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e6d5696-658d-3f1a-882d-df80b579f474 | -12.51188 | -44.93905 | 2025-11-16 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d650442b-4a4e-3ad5-b2c1-81161c4f3b36 | -6.81273 | -39.14318 | 2025-11-16 04:08:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2f5e593d-bd93-3d72-aa82-f553306a9502 | -10.84111 | -48.03258 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e321815-6f7b-395d-b347-909be00121b9 | -6.05973 | -41.55681 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51ca6543-f5d2-3d00-86e5-11f24b66915e | -10.77394 | -43.97697 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f11c3ea-956a-3774-be22-f4369eb4ec9e | -11.84457 | -43.32486 | 2025-11-16 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 470ef3dd-d938-3b96-b853-0ad232898e3f | -12.69289 | -46.79619 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8a37a97-35c5-3339-b7cb-7b3a93db56bd | -7.35966 | -46.58327 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94a271d2-1318-3213-80b5-57d9bae52229 | -5.48612 | -46.91568 | 2025-11-16 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1925eb02-49ca-3470-8e1c-6187956db066 | -5.77972 | -44.0526 | 2025-11-16 04:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ccde3f0-c106-3800-be05-47556fdd3c8c | -5.53788 | -49.59751 | 2025-11-16 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 965a866d-8643-3cc2-a454-9c4a1e08fca3 | -6.67802 | -40.79935 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9d48bb07-d136-3c9f-9890-1b0d7b4c9490 | -5.74929 | -42.50232 | 2025-11-16 04:08:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2702cb5b-c6f2-3d24-a4f8-3c644da5ca89 | -11.82628 | -47.78584 | 2025-11-16 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9c30257-8dd1-31f7-ac6b-4c84e6f05fa9 | -11.70719 | -48.39261 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd904254-3d8d-32e3-96e9-6e5b5a163e2a | -12.21005 | -49.61465 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb8fc21b-d799-3584-b619-ef9b5821617e | -6.0873 | -41.59642 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3979a5e9-c0b5-3060-8442-098caf2215f1 | -10.81032 | -47.99088 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1dff2c8-dfcd-3fd0-981c-df5d56a6a644 | -12.65913 | -46.74815 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f31a31e0-f5a6-3697-9814-fc4ab7cff7ae | -5.57793 | -46.1498 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60506c76-0f09-3fc2-99cd-564bd58ee747 | -6.00008 | -41.91205 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README34.md)
