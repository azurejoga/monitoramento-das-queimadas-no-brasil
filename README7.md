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
| 68e9db31-506d-3061-a12d-d0bb4f900d7c | -28.58504 | -49.44266 | 2025-05-30 04:00:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fa59d435-e3b3-37be-ab4d-c7783d61ede9 | -13.5456 | -43.6762 | 2025-05-30 04:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| a8247060-0389-3c4b-b3c4-93f07d9fd882 | -13.5456 | -43.6762 | 2025-05-30 04:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 72e1c65c-e0f3-35b0-b0a1-b95e502cf011 | -4.42579 | -47.66479 | 2025-05-30 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 672db478-fb2f-350e-98eb-42032c4ee549 | -6.27133 | -44.20512 | 2025-05-30 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11c021a2-0757-3599-b9b5-1f27374df0b4 | -6.27229 | -44.20651 | 2025-05-30 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4ae314f-2e28-3d1c-98a7-ef66acd2a00f | -4.25393 | -47.58217 | 2025-05-30 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9118cbb-e55b-316a-a751-c4273fc5fed6 | -4.89572 | -37.53016 | 2025-05-30 04:44:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1a797b30-616c-3949-83fb-94b9a778323f | -5.21633 | -43.30779 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ea75793-3d9d-34d1-ad52-b26af3614e15 | -4.81536 | -47.31987 | 2025-05-30 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8489871-cfce-3bee-af4e-f082dcaa4e6a | -5.18166 | -48.07897 | 2025-05-30 04:44:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7a717a4-2c7e-3eb7-8882-fdaf032fc8a6 | -5.21181 | -43.30938 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 45ef3197-4873-32de-b7de-fe3eab88d2cd | -5.18579 | -48.07553 | 2025-05-30 04:44:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d82c344-db53-3dd1-8153-1c6425be1edb | -3.95829 | -41.47858 | 2025-05-30 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f69c0058-2147-3390-bf9f-d5839337aeb0 | -4.48957 | -47.79305 | 2025-05-30 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9bf6fa4b-b1ce-3124-bf2f-38a15d65a221 | -6.2449 | -43.37426 | 2025-05-30 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 39fcf71a-6cc6-3c92-bd93-9387e4c85720 | -4.42223 | -47.66423 | 2025-05-30 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9af08d47-cb49-374a-aaac-349b2fd005cd | -5.78001 | -43.61322 | 2025-05-30 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4971f6e-256d-3c20-bb31-015a2ee5bb89 | -6.34132 | -43.38317 | 2025-05-30 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c35eec5-cf66-3a4a-a7f3-251b9bf48c85 | -5.78401 | -43.61889 | 2025-05-30 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d7c8efe-aca3-3f0f-b85c-d8e5565011ba | -5.20684 | -43.30614 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8f0a9dd-992c-34ab-90b8-2f31ffbfd3de | -5.21558 | -43.31291 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16f837d7-424a-3623-926e-a8da302023a3 | -6.34689 | -43.37859 | 2025-05-30 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 883ce330-ab83-3732-a476-9713e8f6e4d3 | -5.21656 | -43.31021 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f55c1b1-25e4-3dc1-98da-23a7d4cf6f1b | -3.95781 | -41.48183 | 2025-05-30 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af13ee7f-dcbf-39d1-93ea-1e6b895be049 | -6.33651 | -43.38239 | 2025-05-30 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b9f9ead-aefd-3295-b39b-a1859a697183 | -5.21083 | -43.31209 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| daa984c1-2445-366b-909e-4b6fe9efcddb | -4.42518 | -47.66879 | 2025-05-30 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b1358dd-3e46-3003-898c-d5a24e907336 | -6.34281 | -43.37259 | 2025-05-30 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dee52cb-bf51-3fd7-a524-d0716743096d | -3.76473 | -47.50816 | 2025-05-30 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2238325c-4e83-3700-a0e7-6d0bd23deeb7 | -5.21109 | -43.31452 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4b668529-2696-3f89-9b4e-a5be1d5243ee | -4.82249 | -44.3551 | 2025-05-30 04:44:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45cba1b8-d49e-3493-82fb-2475af46e969 | -5.05417 | -43.24574 | 2025-05-30 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69d7451a-7194-3e62-be2b-6442c87c0772 | -5.21482 | -43.31806 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6a85fb6-72b7-33bf-be7f-ee4a7540c450 | -4.25036 | -47.58163 | 2025-05-30 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a4f2af9-edcd-39bf-97bf-fc8c20b2193c | -5.21158 | -43.30697 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41a71b35-d185-31db-8d8b-311802b17fc0 | -5.21252 | -43.30426 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c64fe6e8-9d05-3a83-ba31-88108ebd05e1 | -4.6764 | -48.15936 | 2025-05-30 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3530e92-3a6a-3ee9-8de0-342bc7e7dfa8 | -6.34613 | -43.38396 | 2025-05-30 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c38ae874-e34e-3b0b-8482-8c06933e3813 | -5.21584 | -43.31536 | 2025-05-30 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a5ac9d3-1bf7-33ff-b3e5-419eaacdf550 | -6.24415 | -43.37959 | 2025-05-30 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3bbe977-8058-3cf4-9f5d-128f88c09748 | -12.40377 | -50.00449 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2475b77a-0fc6-3de2-8cf6-451c707a0ea2 | -7.63865 | -46.11568 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54a22fae-75da-302c-9577-3ca385186d9c | -6.82634 | -44.65493 | 2025-05-30 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d96678c-ba88-33c1-b5d6-4ffa9c1277f5 | -11.79183 | -44.28661 | 2025-05-30 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d0c0d69-9754-34bf-8b41-e4f6d60da2bc | -13.63144 | -47.43369 | 2025-05-30 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53f0195c-61ec-394d-89be-dc70af9cb532 | -7.18297 | -43.11012 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 45fc9fe9-5152-354a-9c84-fc57accfb01a | -9.00152 | -49.88343 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9e22b1c-afe3-3b38-9016-89013864686a | -12.06512 | -48.47405 | 2025-05-30 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2790e956-fff7-3923-9db5-c175183ac568 | -7.07274 | -44.91516 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3459eff1-0e34-379b-bd25-63756fee2087 | -9.11027 | -49.62875 | 2025-05-30 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9443779e-8a5e-34e2-839f-2d16b8e6cef5 | -11.40083 | -52.94358 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57546376-08b9-3117-9274-5b8e3a8d5f92 | -11.57278 | -47.45364 | 2025-05-30 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4be670e-55e8-315f-97d3-bd0c130c9ec4 | -7.97169 | -45.94479 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d776ea5c-0362-3a5b-97bb-04bc0c6fdefb | -11.14413 | -53.9447 | 2025-05-30 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6fbf763-cc46-3f62-b302-ab73f9a91a9c | -7.27706 | -44.22142 | 2025-05-30 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 379be8b0-0e23-38a3-9fa9-e24c456ef3af | -12.01501 | -49.51814 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0854dabe-0ea7-3be6-8be8-6737dde070bb | -10.45598 | -47.95378 | 2025-05-30 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdbe8e03-6f8e-33bd-bee0-0c74dde21f54 | -12.82647 | -47.39577 | 2025-05-30 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dba35dd-0af7-32a3-a052-6f6d723243e2 | -7.89565 | -55.41346 | 2025-05-30 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d70428d-be71-30e7-8122-50242145e7e2 | -11.40358 | -52.94765 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ff0ea2-596d-3617-9ff8-b545d291bc49 | -8.5147 | -50.0191 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97d4fa86-a7b3-31d3-8c65-41ac5b246b19 | -11.40633 | -52.95173 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b4f73f6-d7f0-3baa-91a3-fa3b4d8e1e0c | -7.63457 | -46.11505 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ac73829-4658-3565-a69a-d7401e62920d | -7.95954 | -46.17024 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22c03702-aee6-3acd-bc44-44adc6cbb5d2 | -11.68868 | -46.21427 | 2025-05-30 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2842d34d-54a8-3928-afd3-c98e2262e426 | -11.97433 | -52.45713 | 2025-05-30 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4598096d-4eda-39bc-b402-7a44666adcab | -7.18836 | -43.10789 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ca9c8f6d-d224-380e-8d32-45863348ba19 | -8.19922 | -49.81114 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f0d9d9f-eaa6-3ba6-a5d2-d92c52ff4901 | -11.57615 | -51.36261 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fc44ea4-5cb9-3a74-b6b5-b2d298c05f1c | -7.62418 | -45.75227 | 2025-05-30 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbb5b6ba-580c-302e-a48f-0be0914d3a1e | -11.45387 | -49.09795 | 2025-05-30 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d72aca33-60a5-390d-ba18-e842a84fe3dc | -6.21445 | -48.50875 | 2025-05-30 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d544902-f79a-3193-a5b4-4a578b9b40df | -7.94729 | -46.19833 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4a34941-03ae-3a10-8315-a0384ded557f | -8.84758 | -49.83721 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f4d7725-65df-3e4a-a49e-82323dc08979 | -10.64008 | -48.80239 | 2025-05-30 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d89e4880-55bd-3179-b309-296202173771 | -9.93841 | -55.73113 | 2025-05-30 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0437b94-e98b-36b0-97a4-f8027fd89f25 | -7.95549 | -46.16946 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7229a77-bff7-3f36-b2d6-3644d309b68b | -7.54877 | -43.31647 | 2025-05-30 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2de25c28-f0f0-374c-85d9-6323f9bb247f | -13.53532 | -43.67813 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a5a14220-96d5-357e-b2a7-365a85140e07 | -7.24137 | -43.09716 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 07ee0a29-56ea-3016-a514-2f7c5340202c | -8.55151 | -46.42141 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65d66128-2858-3249-920d-11a3d6346a6e | -12.01464 | -49.52068 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca66683b-455f-3efc-925e-62c7c7490626 | -10.75095 | -48.63025 | 2025-05-30 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1f44660-964a-3128-a557-3102a4c55784 | -9.26237 | -48.87487 | 2025-05-30 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 26b832d4-4f27-398d-adf4-11f8af953c86 | -7.19252 | -43.11433 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 58a864ed-038d-35ce-be69-0e52045b8a56 | -7.24635 | -43.0979 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1991aead-4158-30fb-b2de-a63b3d0827cf | -13.53492 | -43.68142 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| db16584b-6fd8-3a34-8610-72e7b029583e | -6.69503 | -44.16282 | 2025-05-30 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bae97df5-1088-3e2f-ace9-8d2393dffca9 | -13.53008 | -43.67743 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c2a09dd-9e78-301b-b2c6-4f35a8ec11fd | -7.61785 | -49.92343 | 2025-05-30 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1cacf7a-b6d7-33a5-9f26-18929f6dbbb1 | -12.07516 | -48.45687 | 2025-05-30 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf22e64d-1828-3604-b49e-0207059e57e8 | -6.63446 | -47.34451 | 2025-05-30 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 709658a3-b479-3fda-99ed-35face87c740 | -7.23718 | -43.09063 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 91ac4cf0-ae73-3f3a-8e14-627b935ad113 | -9.25943 | -48.87031 | 2025-05-30 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65106e24-70be-330b-8669-6addefa16aef | -12.18096 | -51.34064 | 2025-05-30 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 235f87ff-58c3-3f38-93a5-b2ac8e9e518a | -13.22413 | -49.83301 | 2025-05-30 04:46:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2af144b4-ed1c-3db0-a343-a97c8e08663b | -11.8946 | -47.44182 | 2025-05-30 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43929cfa-7070-395b-ae96-a9941c96573c | -7.01085 | -44.61876 | 2025-05-30 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b343982b-220e-3f0f-8fad-286d50d57716 | -8.51525 | -50.01548 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README8.md)
