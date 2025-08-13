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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40522357-fec8-33e9-8300-26945b4a1970 | -5.18491 | -37.65905 | 2025-08-13 00:09:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 21babea6-22a5-3405-bc6c-96a140534943 | -4.77153 | -45.31744 | 2025-08-13 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d739cd30-d1c1-3a11-ac29-56dd54c4901c | -12.53841 | -46.98157 | 2025-08-13 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 2aeba1ba-4949-3ee2-882a-d32e7f90a51e | -6.55121 | -44.00968 | 2025-08-13 00:09:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d59509b5-0e81-3c02-9ca9-dc3e93c48ec6 | -12.52602 | -46.98307 | 2025-08-13 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 8cf06fe9-5222-3435-b906-e06be7a60929 | -6.58051 | -44.55757 | 2025-08-13 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 31a521b9-cb1a-3fe1-8925-6731b537bd94 | -10.2419 | -50.23737 | 2025-08-13 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 084df40b-af0f-3a80-b892-b20f07f94a34 | -12.41239 | -44.51192 | 2025-08-13 00:09:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8acf95c1-8b33-3864-9220-83a16c15a280 | -10.0739 | -44.71684 | 2025-08-13 00:09:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 93e62463-4605-36be-83ac-0106332d0f47 | -12.31316 | -46.04673 | 2025-08-13 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 1551fe42-d7ae-3a92-aabc-3e383856322b | -7.06619 | -44.35127 | 2025-08-13 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 223aacab-3640-3f0f-9fe5-21bf35aefe07 | -5.87178 | -42.39984 | 2025-08-13 00:09:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e61d6e43-1303-3874-b034-0f33d04ff584 | -12.32645 | -46.06077 | 2025-08-13 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 40f44cf0-33a7-34c5-ab74-3d229c653b35 | -12.32459 | -46.0452 | 2025-08-13 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 7d19e7fa-2075-3827-b537-bb9eb8a5bcb7 | -11.75597 | -48.17558 | 2025-08-13 00:09:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 5b581b96-018a-37ea-af24-d757ad214999 | -4.17328 | -42.45055 | 2025-08-13 00:09:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| eb6ae689-ec41-36fb-8639-ea8949a2db74 | -10.19087 | -49.51358 | 2025-08-13 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 565e641b-db12-368b-9459-690301bef1e6 | -12.315 | -46.06234 | 2025-08-13 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| c835d53c-d7bc-3a80-8825-15741c417fa0 | -12.52123 | -46.97135 | 2025-08-13 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 02359b3b-1f5d-3487-bb38-5c6fb085d4c1 | -9.71911 | -49.49089 | 2025-08-13 00:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 276d1bab-24f4-3b42-a335-a4f8a04d7377 | -9.71408 | -49.4713 | 2025-08-13 00:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| c910a86c-ed53-3b03-b65d-d7e4bd6dfc06 | -11.75868 | -48.19782 | 2025-08-13 00:09:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 44e044d9-c544-358e-b478-16e99970a1e5 | -4.18212 | -42.4493 | 2025-08-13 00:09:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2d2cd224-9888-37cd-b44d-29d436d26a3d | -7.48979 | -43.93802 | 2025-08-13 00:09:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0064368-650c-3b6f-9fec-c990aeb79ea1 | -6.58999 | -44.55631 | 2025-08-13 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b17eca0d-986e-3b13-a469-c7e35fece770 | -13.02859 | -47.51109 | 2025-08-13 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f322fc59-f8a6-324d-9e8e-90a41f14db66 | -10.49621 | -42.41859 | 2025-08-13 00:09:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 04597110-5329-3751-93b2-ad5ce3348d74 | -10.9684 | -49.56268 | 2025-08-13 00:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 5866d2d7-e434-3f28-9db4-7ed83fb26b27 | -12.31546 | -46.05211 | 2025-08-13 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| f1ac3c83-ec07-395f-8555-51d1cf1a3870 | -4.60649 | -43.31079 | 2025-08-13 00:09:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 26a4c844-4ebd-3fe8-93f5-500f7142d270 | -9.6043 | -40.56852 | 2025-08-13 00:09:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 31ee26d8-b1ff-3a87-9e22-0e679fda7bb0 | -12.52388 | -46.96452 | 2025-08-13 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5558701f-c558-3836-bfe0-588f47e5f61b | -5.45253 | -43.57617 | 2025-08-13 00:09:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 14210577-f4fc-3ee7-86c9-135c7dc779a4 | -9.3745 | -40.70436 | 2025-08-13 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 34.3 |
| b9d85508-8e69-35e2-91c8-4b618dad8ca5 | -11.01213 | -45.21556 | 2025-08-13 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 70d59ca5-d56a-3df5-809a-b1dd3b8c5595 | -11.76936 | -48.2125 | 2025-08-13 00:09:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 44733de7-e6f1-3d86-b8ac-257f4d517f7c | -6.1319 | -44.71318 | 2025-08-13 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8ee0eff6-1025-31a2-bde2-e3225954e303 | -7.06755 | -44.36152 | 2025-08-13 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 21487fd4-c461-33f1-b542-0fbaaab078f0 | -10.49745 | -42.42779 | 2025-08-13 00:09:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fd6cab72-ad8d-3a6f-8332-c0a5d66da18c | -10.2385 | -50.20658 | 2025-08-13 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 99cb8096-1f52-3e44-aa50-3a41d70b2331 | -7.07255 | -44.94444 | 2025-08-13 00:09:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a0a5a211-ad54-32c8-905f-6a4ba759ce16 | -12.68228 | -44.95273 | 2025-08-13 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3eb42687-1572-3208-8f7b-f0c296e8e9cb | -5.873 | -42.40866 | 2025-08-13 00:09:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| d93d39d2-d8bc-39e6-a704-4510e88de5bc | -12.3225 | -46.0638 | 2025-08-13 00:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 7960915e-7171-3b6c-938e-524e41f191ba | -12.3229 | -46.0409 | 2025-08-13 00:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| ac0e36e7-38a3-37c6-ab9a-669c8204eb86 | -7.1114 | -60.1189 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 36cc675d-8df9-345c-b420-ce64946284cc | -7.1482 | -60.1366 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bdb1eb1e-055d-3a8f-874f-f97df8fa8037 | -8.1246 | -55.569 | 2025-08-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 15fe991f-e7b2-34f0-b962-50b110d9d81c | -7.1299 | -60.1182 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.3 |
| c9a87fe8-a4e5-30bb-aad5-89f42c5e9588 | -22.4079 | -45.4657 | 2025-08-13 00:10:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.4 |
| c59bdb16-f5e2-3e34-a910-5013ac9b2185 | -8.106 | -55.5701 | 2025-08-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| a5659ed1-969e-3027-8028-4c58c4b05dd9 | -11.7699 | -48.18 | 2025-08-13 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 53e82500-16e7-3aaf-b1db-caae3b861412 | -15.0981 | -51.3612 | 2025-08-13 00:10:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 997295f5-904f-3ee8-89e9-33d6f8ed5823 | -9.1894 | -59.6558 | 2025-08-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| d6d9b9d5-b4ce-352e-8038-e183962cf440 | -11.9938 | -45.1496 | 2025-08-13 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 29f5353d-a57b-36f0-8a26-27a781e9fadc | -22.3877 | -45.447 | 2025-08-13 00:10:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.8 |
| d837ff4b-3475-37ef-a936-8a44f1559309 | -7.2562 | -60.6302 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a7d9391c-aadc-3bcd-b839-ee254bf61fc9 | -10.9689 | -49.5856 | 2025-08-13 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| ce896fa1-ec3c-3bd1-94be-9164bedf263a | -14.1144 | -44.3072 | 2025-08-13 00:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| e11c3069-7859-34a8-b890-ce5c8c6e42a2 | -10.2415 | -50.2215 | 2025-08-13 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9107bd0e-7a90-397d-a302-3f892cb27722 | -11.7504 | -48.2046 | 2025-08-13 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ee6cd48d-8076-3553-973f-aa963e147ed0 | -10.9693 | -49.5639 | 2025-08-13 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| e5bd51ae-feef-3308-b027-50850c926682 | -9.1892 | -59.6752 | 2025-08-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 82b98d49-564a-3d00-a75d-900d3208b277 | -7.0935 | -60.0237 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| ac624aa4-2121-3a2b-8711-620ad8ca82d6 | -9.052 | -60.6658 | 2025-08-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 36f271fc-4d14-3759-9092-e93174c304c5 | -8.1061 | -55.5501 | 2025-08-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 26d3bc63-0789-35ec-924d-cd785f69c715 | -7.0934 | -60.0429 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 3c3b6021-1509-3449-8eb1-58f35db98aff | -15.0791 | -51.3424 | 2025-08-13 00:10:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 43.3 |
| bc09026b-90b3-394b-94a2-9b6cb837b555 | -7.4636 | -59.8931 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f015c3e2-d586-30d4-9624-021305ac8cdf | -15.0985 | -51.3396 | 2025-08-13 00:10:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a006e971-8b33-3f69-970e-b259b390bfff | -18.5303 | -46.0414 | 2025-08-13 00:10:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4ee36b29-ab9f-3db5-b147-b6c36fc7a464 | -22.3869 | -45.4716 | 2025-08-13 00:10:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 157.5 |
| c5d2632f-a66e-3d04-b527-6b8d282dd66d | -11.7695 | -48.2021 | 2025-08-13 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| dfc08398-9b66-3608-8c26-6ba31f683732 | -15.0787 | -51.364 | 2025-08-13 00:10:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| c8efc8a5-338a-3f4d-8529-3b480448691d | -9.0521 | -60.6466 | 2025-08-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| e3a04801-fb8f-36ca-989f-07630a975c8f | -7.1483 | -60.1174 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| f83c1ae2-adba-3e59-b1fa-78c0bb3c9d8e | -7.2746 | -60.6294 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 471f0b97-e7c2-3143-9654-436322a02ac1 | -9.208 | -59.6548 | 2025-08-13 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4bf7ca96-446c-33e0-9eaa-3d9c9f594cd0 | -8.1247 | -55.549 | 2025-08-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 6ad94c56-1180-323e-b0a5-0766134abda7 | -7.1298 | -60.1374 | 2025-08-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 643eb6c9-6162-348d-922f-8eda27bcaaab | -11.7508 | -48.1825 | 2025-08-13 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 9deb2901-2528-3533-b006-91c6228aa189 | -9.723 | -49.4806 | 2025-08-13 00:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 889250dd-9a4d-3451-8bbc-3d8bf1663e24 | -10.2407 | -50.202099 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 786fa4c0-2433-3e58-8f35-f05b9fa1effb | -10.7461 | -48.1754 | 2025-08-13 00:12:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 930a745a-d745-3940-977d-1745403bd4bf | -18.6134 | -43.910198 | 2025-08-13 00:12:00 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eb24bffc-3c50-30d6-9485-6433ee326a87 | -10.2389 | -50.194099 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5244cd45-3517-3c00-9d48-c9849124d6d5 | -6.2813 | -53.615799 | 2025-08-13 00:12:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49531cdd-def0-333c-a3b6-c7d2ce8010fe | -10.9642 | -49.557999 | 2025-08-13 00:12:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 323cf8c9-7c7f-3dd0-aa57-b1480c40aa82 | -9.9909 | -47.8302 | 2025-08-13 00:12:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 014a3a8d-3f98-38a3-a610-f1429f7d78f8 | -7.4803 | -43.920502 | 2025-08-13 00:12:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2721ffe5-fe89-3e06-bb4d-194862ce0ca9 | -16.9716 | -48.399101 | 2025-08-13 00:12:00 | METOP-B | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3db4a24b-526d-3006-b639-06af0cd871b1 | -12.5476 | -46.966999 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97098c1d-25ff-3af9-a340-74585b593d5d | -12.5801 | -46.9743 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8551bc78-98b5-3c22-a02e-dcd255f4a42c | -11.7191 | -51.587101 | 2025-08-13 00:12:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d21ce9d7-b307-389b-9ae0-90941c0089d7 | -7.0558 | -44.354099 | 2025-08-13 00:12:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e14ab8d5-742d-36ee-8f1e-1007740fb6eb | -16.973301 | -48.4072 | 2025-08-13 00:12:00 | METOP-B | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13cd7207-6220-3414-b439-61b0beaf082c | -5.7356 | -51.6646 | 2025-08-13 00:12:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7111232b-6d6d-3907-abb5-3095253f1cf5 | -19.2966 | -48.4179 | 2025-08-13 00:12:00 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8092ab23-f00f-324f-963e-64f759aad162 | -22.3776 | -45.4548 | 2025-08-13 00:12:00 | METOP-B | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70709010-7501-3305-a513-98130926671b | -15.092 | -51.324902 | 2025-08-13 00:12:00 | METOP-B | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
