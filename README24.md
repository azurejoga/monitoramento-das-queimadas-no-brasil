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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b9d508e-2f9e-339a-8996-ea03b7ee2001 | -6.2055 | -43.50598 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2aa6e1c7-e8f0-33d7-b272-9b9af907595e | -6.17498 | -43.39874 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bfa5bdef-5a6f-32fd-bfa6-467e36f23783 | -6.21393 | -43.36598 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2edd7909-b5b9-380e-be32-0e69f6d9f01f | -9.06561 | -49.83168 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 46833669-95c1-3828-90cc-9d06d6bd90e5 | -7.10219 | -50.76213 | 2025-09-10 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b8749e26-43f9-3db2-acf6-1223e791c221 | -7.86468 | -46.03935 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9bea8e4-ba07-3088-b0a0-28219cd70781 | -4.86945 | -42.76213 | 2025-09-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f998ac63-d930-3093-ad58-cf924f87b04d | -9.39234 | -49.22242 | 2025-09-10 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0528d89-83b4-3bad-95da-218820ed508d | -9.76052 | -45.40055 | 2025-09-10 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 44d47368-9e9f-3c0c-a901-da00fa55c7c1 | -9.16226 | -45.57256 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f01b548-2412-331a-8514-9a87a5bd8870 | -5.44071 | -45.10086 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e17d5746-11dc-3cbb-92f4-cfa4d5fc1419 | -5.73924 | -45.25533 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26ca5150-f5d8-3648-9def-3c3e554a4be3 | -5.84688 | -43.86087 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc9ca4e0-dd96-36ee-ba33-c31ef6151eba | -5.71916 | -45.41907 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40a161b9-12b9-3790-9749-2d4a35d7ef62 | -7.37301 | -47.43489 | 2025-09-10 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91a73210-5753-36c5-aa4d-65699446a792 | -8.10153 | -44.85669 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f94fbeb-e287-318f-993a-7a4c359b9075 | -6.77537 | -43.45175 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 70bb91f1-69e3-3a56-8c6f-6dcef72aa725 | -7.10373 | -50.76511 | 2025-09-10 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1ffbe59-603b-3a41-818e-44a313d15c1f | -6.65661 | -44.549 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d8fc3a8-859b-3750-adc5-670b233e5332 | -5.96801 | -44.2577 | 2025-09-10 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27aa0797-fac7-342d-bce1-df75954a96a6 | -6.20094 | -42.4685 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9d4dc7a3-861f-3c21-92a2-c803653f723c | -5.74631 | -45.25202 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b37f10c-3f02-397d-9c72-d623420a2281 | -7.36925 | -47.43427 | 2025-09-10 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28ac3184-482b-35cf-b098-06dae64eae47 | -8.3425 | -44.8409 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a76e37-e991-3c98-87ce-19fd6562fcfc | -5.02588 | -43.1323 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a05914b9-2d0c-3d20-81b2-7e3bbe75044d | -5.41194 | -43.44749 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42b60207-e598-3792-80c3-673ac23ef57b | -10.44334 | -43.3342 | 2025-09-10 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 098e34bd-db9b-31a0-be89-bdbedc66ec20 | -5.79387 | -45.67247 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ef46cbb-a9f4-3433-a57f-9f4451bae79f | -6.409 | -44.39648 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e192e55-0f44-32a5-aa8f-7a5e0c80645e | -5.87454 | -45.61701 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d3c7c75-c4b9-3a4a-adae-decdbe315527 | -8.9868 | -45.72658 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2b96c507-2423-32e8-a610-59f0ec2fa5fd | -9.79862 | -47.79385 | 2025-09-10 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51ed5d51-14f5-39a8-a228-8cc09cf6d555 | -6.24127 | -43.49804 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 504f4edd-1dea-32bb-9524-12f9a1923dfd | -5.93141 | -42.78117 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 77b6f202-c061-36ff-9b09-a5805be335d2 | -6.05901 | -43.11583 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 36c2df6d-ce0c-3875-b3f3-64768e67dfe4 | -9.69288 | -46.80675 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21e519c6-adc8-3d7c-90bd-2b1cb6cb13e1 | -5.65927 | -43.90662 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f96b972-1f5d-3e77-96b6-827bdad981b7 | -5.86264 | -45.29318 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52185a9f-e4fd-3a59-8524-ef3db33b60be | -3.6992 | -43.43233 | 2025-09-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db03d491-3ad3-392e-bc18-ce1df8b7fe8d | -5.88625 | -46.08707 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e31179c1-c182-3242-945a-8468d8bba33e | -9.07057 | -50.48085 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4a4aced-d3e5-3e4f-a4c2-57d75f943a3e | -9.82641 | -46.05363 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92eace34-ef68-33c8-a7dd-c41f1a3727cd | -6.44508 | -44.0598 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a0e039b-0e07-3a78-8210-ae6888c40ca2 | -7.18796 | -44.9351 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bdb9d6e5-a8a3-3c25-9ab2-c9dbecb383fc | -6.24867 | -43.40319 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a56d2ef-2b2e-36db-8e61-933d75e7109d | -6.19705 | -41.04555 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7329b7c6-0fba-3522-b410-865cfd129551 | -7.74171 | -50.7412 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9427652e-8c5c-3438-8285-ce79bd4cc87f | -6.6083 | -43.95385 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1309d20-7799-3e16-948c-70748de7ac82 | -5.78888 | -45.44983 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b172f0df-2bc9-3b04-8c69-10e566b0b7e3 | -5.64654 | -43.92252 | 2025-09-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 622f4172-7da1-39cd-9413-683c598092dc | -9.06201 | -45.7615 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b6a2e4b-ef35-3462-b868-1095e3827b86 | -7.55098 | -44.66269 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc5c125d-6ca7-3592-b1fb-1782973efdd6 | -3.24523 | -52.85335 | 2025-09-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c33d17c-c3d4-39bf-a512-42834dd167fb | -8.07672 | -50.18552 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4d9e9425-f313-35f0-9ad2-8ab7e19ac515 | -3.20908 | -54.96028 | 2025-09-10 04:14:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8df38332-9a8e-3560-8877-6c6843a15525 | -5.67248 | -43.34751 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4227bd8a-1a3d-38f7-a2d3-1611a1539fa5 | -5.57592 | -42.92284 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 476caddd-2452-3cd6-90fb-c35e04bb97cb | -5.7457 | -45.25577 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16a17904-956c-32d0-9129-ace57ffbcef6 | -7.99218 | -46.32876 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eba2853c-1e85-38fe-9bf3-b9d22400af41 | -9.44455 | -46.70547 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d756d6a-4c4b-3d70-9585-11e4499c4912 | -4.09424 | -41.57842 | 2025-09-10 04:14:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a7f8db55-ef71-32ee-ac13-3d22b28c12f5 | -6.53798 | -44.78334 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbd34355-aa2b-3c68-9d0b-2263b1cad7ac | -6.34902 | -42.60896 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2e66b9e-6348-3a22-9460-fd50eea77285 | -9.00989 | -46.05888 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4b7c40b-2b57-31ee-88b7-3662042c7e47 | -2.34459 | -47.59056 | 2025-09-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6704c8a-4c4e-32de-b875-8a270740fa08 | -6.18237 | -41.0518 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db100e1d-ed92-32f3-b852-7e96f48ef615 | -6.38948 | -44.43332 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0effe48-d52f-3a8a-b5b5-bf50ef2a5c4c | -4.41039 | -42.14953 | 2025-09-10 04:14:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d391a4f4-1f4e-30c8-a647-4e9342dbacc0 | -5.35594 | -42.63029 | 2025-09-10 04:14:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9dbe6a0e-de65-37ed-87e9-2a8925b51b8b | -9.06134 | -49.83096 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf26954c-5a3f-3014-8855-a6fde5e562f9 | -9.09857 | -46.9739 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f1dee058-2ede-316d-b505-facbb044a18a | -9.4432 | -46.71362 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9fdcf691-61b4-3583-a115-8b7ff4b60083 | -5.79881 | -43.88552 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a052369-d209-3527-929a-b5067e3a1bb0 | -5.68293 | -43.3456 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d500bb7-e914-39b3-8e81-6ce4452b1688 | -5.94078 | -45.81618 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7efc057-5268-3a44-bccd-1dff99b5dfe3 | -6.08961 | -43.35703 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d4ad449-83ed-3d01-87f0-67622999f361 | -6.83046 | -44.88918 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df22e9fc-ce36-37e2-ae36-c3b3fa0309d3 | -7.13711 | -40.95237 | 2025-09-10 04:14:00 | NOAA-21 | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f0ba8d5e-4317-36be-9591-de41b8a329cf | -9.44522 | -46.70145 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3ce38a4-cafa-3c29-9a97-1b7a91019c2c | -9.17006 | -45.589 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9ddaa34-837c-3760-986f-c0295dcbd420 | -10.17975 | -44.76119 | 2025-09-10 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d96a4106-ccd9-3120-b4a2-3fe67c29534d | -6.68933 | -46.4145 | 2025-09-10 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0f742c0-f010-33e0-b227-0be1558c0893 | -6.17299 | -42.64911 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e5e15c6f-afa8-3fb8-85a9-c37427950951 | -8.85959 | -47.23611 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dff8d19f-ed82-3a2c-8f3d-adac13bbe34f | -8.06648 | -48.63017 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2ea65352-e917-3c9e-9319-76bf5195e3b0 | -5.76616 | -45.52504 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42fe9173-9a8b-3109-a1a8-224626f94875 | -5.64088 | -43.11275 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ccee2638-6309-3c7e-90ea-4b2d374ef4ad | -6.47039 | -44.11452 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 855c02e4-f367-3769-8a15-da5f26767af0 | -8.02938 | -44.50006 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c326ae3-408f-3b42-9fda-6d9af51502ca | -8.05159 | -48.69365 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bf02e349-1fd6-3331-a517-0facef5e76cd | -9.01211 | -49.53725 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa8b595d-b60a-366e-9624-9805f13eddf4 | -5.958 | -45.79876 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f159e4c6-a1fa-328c-88fa-04c27bb50947 | -5.4257 | -43.4461 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b262541-90c2-3e0c-b39b-15691cd56f19 | -5.66315 | -43.90363 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e126c78b-1ea6-3bb6-ad6c-fed1d715eaf8 | -8.00352 | -45.4629 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7090ae5c-70bb-366c-9e4f-50924a2c913d | -5.65983 | -43.90313 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a83efa8f-3e19-365c-a4d5-36b0bf58d46d | -5.67809 | -43.89524 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c755e1b-84d5-3393-b5f3-f77359755ba0 | -5.76235 | -42.75121 | 2025-09-10 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4936b940-f08e-37b6-a395-aea73569846e | -7.30915 | -44.14782 | 2025-09-10 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cde0fad3-3b4c-3c71-be59-b76b0fdc2463 | -7.07547 | -44.54698 | 2025-09-10 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README25.md)
