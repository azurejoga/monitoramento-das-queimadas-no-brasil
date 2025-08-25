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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dee3d5e-ee53-35bf-b023-26693fc8bfff | -15.63799 | -52.72353 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2174a75c-857c-3274-a546-90c688e5bf1d | -13.00571 | -56.88642 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65cb8463-4583-39d8-af5f-d988cbfb54d7 | -14.84559 | -48.33053 | 2025-08-25 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb3a5c1f-8efa-337d-b093-33e2b2ab9165 | -15.03984 | -48.52613 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8cd2b61-adac-3227-96b2-4151e440e1e1 | -17.84297 | -44.41265 | 2025-08-25 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec2055ca-fee8-3162-bab1-2e16e168edcd | -14.37388 | -51.94041 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 892b5b0b-9148-3749-8f82-c4ef6f0025fd | -13.68647 | -57.75592 | 2025-08-25 04:44:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff264f9b-700f-3b57-b617-7d8b417f03af | -14.38449 | -51.93851 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac110589-148f-31c3-b3cc-b79421326e09 | -14.67492 | -54.89056 | 2025-08-25 04:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3eacaf8c-e39c-36ed-ab42-90e23899742c | -14.26428 | -58.61344 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56c81ada-4fec-31ab-8adf-816240175d62 | -14.30141 | -60.37263 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eab6c36-1e4b-3848-bb4e-4b10ce517179 | -14.28586 | -60.36829 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d51dcff4-e854-38ce-9e96-4fa4e16c78bb | -15.14635 | -48.62796 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47124d4c-272c-3488-a9dd-00bc3eb5153a | -14.11705 | -53.99811 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c9e754d-2b58-3e05-aa8c-017107f46a90 | -14.28524 | -60.37148 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b108ad53-16ff-33ba-afa5-bfe9d9ec09e6 | -14.30614 | -60.37643 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eb00c17-4dbd-3439-b521-684a72af1865 | -19.7359 | -49.01595 | 2025-08-25 04:44:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a285a6e-599a-3137-9443-d6389c096244 | -20.35864 | -46.71766 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e30e5f10-ec77-3d83-afbd-5a00be14f434 | -17.83764 | -44.41698 | 2025-08-25 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcae7b37-82ca-38e2-9f36-317aba288f07 | -20.078 | -44.57539 | 2025-08-25 04:44:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bff8c25f-9dd2-3cd4-affc-42bebd2a30da | -14.22851 | -58.62218 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe3be1a2-8f58-3602-84dd-f0f0873bf108 | -15.10056 | -48.69678 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8816c2fb-bc07-3613-95f8-78248e4acf27 | -13.34377 | -54.38936 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6706067-f137-3652-bcc3-f7d6bfac1fa3 | -20.1111 | -47.25675 | 2025-08-25 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32f231ca-f419-35e4-9dd8-109c2575cf12 | -19.72702 | -46.46598 | 2025-08-25 04:44:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 899a0068-a207-3f81-b8b5-0955fbfcadd9 | -15.19254 | -48.21899 | 2025-08-25 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c24f1d7f-b80e-3348-aca4-5a5a577e8de0 | -20.37912 | -46.7596 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c1d617fc-c94d-3020-8b0a-2dac0ed8bd09 | -16.85378 | -49.24697 | 2025-08-25 04:44:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abf1b295-1c18-3996-9b28-3cea3a8fc573 | -17.83938 | -44.41333 | 2025-08-25 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 672acc38-c682-3c30-8529-8af161fa3e00 | -14.72236 | -55.93449 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 367b8157-80fc-3167-89ac-acc5125ae35c | -15.13571 | -59.60014 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 46f44acc-54a5-3753-8ea2-d7944d2c31cb | -14.09565 | -53.99438 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21410ea8-7f42-3b3a-8b49-f0f4dda4430d | -14.26427 | -48.03868 | 2025-08-25 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2277b2fc-e2b6-3e13-98fa-c715c52a63b3 | -14.43375 | -56.46539 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 715797ba-6e05-3ebe-a9eb-b0b6854d0e77 | -13.34451 | -54.38497 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8e8783a-ac84-379b-a591-30102f371adc | -15.62908 | -52.71443 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0b2b100-bf6d-30bf-9241-7ca99844d80d | -19.56601 | -41.60992 | 2025-08-25 04:44:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 18439cb0-ded8-3868-8bda-013bd35308b6 | -13.01 | -56.88719 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cdefa19-40b2-3996-8a29-c483d65fd3da | -16.30793 | -48.8944 | 2025-08-25 04:44:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bad666eb-c040-37e5-86f5-ea76dcd158ed | -14.27366 | -58.61532 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 959001c0-f392-3a9d-bf34-5b5bb3d57c40 | -15.05022 | -43.83932 | 2025-08-25 04:44:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5b0a82d8-0411-3b2a-8e75-82685be7d121 | -15.64751 | -52.72895 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1076d9cb-c1a1-3664-a37a-eb47fdb7f443 | -20.73326 | -49.42421 | 2025-08-25 04:44:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0ed3daa-36a7-35b2-ad6f-2cad22a46ede | -15.04674 | -43.82838 | 2025-08-25 04:44:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 373fe35e-75ad-3245-9bb9-8f1d0f40476f | -20.10702 | -47.25637 | 2025-08-25 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 007a6870-72b4-38f0-bbce-3e932b82d41d | -20.61776 | -45.02238 | 2025-08-25 04:44:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bbd93b5a-289d-3ffc-a9d7-98348e2c6088 | -20.36921 | -46.77082 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9c4c4d8-b08e-32be-880e-063408088667 | -18.76709 | -48.03078 | 2025-08-25 04:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9c898dfd-9615-336d-b331-ac4dcec8110c | -13.00927 | -56.89125 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a37c0e6-c66c-306e-9fda-658b5ff11081 | -14.71283 | -55.92595 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c4671f4-e3c4-3301-ae7b-6abd6fb82518 | -19.57183 | -41.61047 | 2025-08-25 04:44:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 426c2e38-2447-35ef-943e-a47ed443374e | -17.50382 | -44.78781 | 2025-08-25 04:44:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f309d569-ca2c-3dc4-a53d-c97e0d01ea0c | -14.34306 | -51.96105 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a906513d-721f-3f64-95cf-fe420b40f605 | -18.38959 | -46.83369 | 2025-08-25 04:44:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54360d21-2c4a-3e0e-adf6-ba5ac7b3429f | -15.62692 | -52.70645 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef259ce7-5a89-3df8-a493-25115b24f3f4 | -15.12893 | -48.65146 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebc03675-0b62-3863-9247-f93d86dd8a03 | -21.63751 | -44.01805 | 2025-08-25 04:44:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e18c6b34-8122-319f-b3c5-2897cc1ad100 | -14.31856 | -53.07427 | 2025-08-25 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3673c3c-77fb-308f-8685-0d320d7a3fd9 | -14.64237 | -56.58104 | 2025-08-25 04:44:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b88ef2f-39d8-3c29-9189-c9f8d40f5c77 | -15.14667 | -59.59651 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e0ebb04-b42e-3eb2-bc08-104920c8181d | -12.05997 | -63.15396 | 2025-08-25 04:44:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6126883-fcb1-31dc-a472-dd4312571af4 | -12.99996 | -56.8938 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 029906af-7106-31e6-86a9-58b832dfa8ff | -14.43647 | -56.47361 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6069f966-2faf-349a-ab86-8d9121b89a6e | -12.06112 | -63.14839 | 2025-08-25 04:44:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba6b40ef-ca5e-36b3-a372-7aa3a39bc267 | -21.29893 | -49.94037 | 2025-08-25 04:44:00 | NPP-375D | BARBOSA | SÃO PAULO | Brasil | 3505104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29bb2c69-d05d-3d69-926c-a610a50193bd | -18.34572 | -46.01934 | 2025-08-25 04:44:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3573c30-b406-382e-9926-7e32266b57e5 | -15.64811 | -52.7253 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cdf9e67-5e55-3092-af00-7aa86ba56d25 | -15.63739 | -52.72721 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44563c2a-4ae6-36fd-8c2b-0fd63450ecdf | -14.12062 | -53.99875 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a24205d-8b41-368d-a1f4-b4600d8503bd | -14.29126 | -60.36866 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d752c323-5ac6-359d-b845-417d2b144c5c | -14.25393 | -58.61666 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2701fb7e-6fa4-3424-9dee-e57fd343d990 | -12.99641 | -56.88894 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b700a231-6074-3853-9f99-a03d677371c5 | -20.04686 | -44.47669 | 2025-08-25 04:44:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2f845e13-4766-3d60-bc59-79cbe0b91b56 | -15.11355 | -48.68217 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 495642b0-5c88-3d31-a3b0-765c20c8bb50 | -15.14872 | -48.6367 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acb6b3fd-a5cf-3727-9696-e8fe0ae29d77 | -14.70759 | -55.92651 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7d73d7a-d024-3f3c-9568-3e9ea0852d29 | -16.44638 | -49.97206 | 2025-08-25 04:44:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36b0a542-dec1-3770-8ac6-1cbbfb54746c | -14.3778 | -51.93737 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 086f93a8-2b32-3115-8658-b923b0a4bb4a | -17.58232 | -48.73403 | 2025-08-25 04:44:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f171ec64-a3a1-336c-a795-e38c8d4b7de0 | -15.04528 | -48.67985 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6c95e54-0f8f-3f95-87f7-8f2662b60388 | -21.41898 | -47.5954 | 2025-08-25 04:44:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b017614-a6e4-3f69-b55b-0fba5ffcabd6 | -20.383 | -46.72822 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c95cc970-aa10-3d09-94cc-c4c671068065 | -18.45172 | -47.55463 | 2025-08-25 04:44:00 | NPP-375D | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1a7a9ad-a996-3c4e-a40b-e2e5f956f43c | -15.14105 | -48.63972 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d90665d7-49e3-3f16-baaf-db782c61c35e | -14.71844 | -55.93376 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c59c452-c9b8-3053-9b82-2d0ee9824b12 | -14.78444 | -47.9334 | 2025-08-25 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69837458-cc7e-3b7d-b6be-d521f18a8ed9 | -15.11415 | -48.67805 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44c7c149-0876-3d6b-8f25-b32d592f03d8 | -18.29699 | -49.53117 | 2025-08-25 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1ee60635-ce8c-347c-88be-11b6a45bbb78 | -20.36708 | -46.71856 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dd8724c-fee3-3fa2-9ac9-b1a621945bbf | -15.75363 | -49.96804 | 2025-08-25 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49e8ea3b-d0c1-3ba0-abb1-da120eecf909 | -18.68153 | -48.18746 | 2025-08-25 04:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 18ecd059-8291-3268-92d6-43b492b688c1 | -14.70251 | -54.68442 | 2025-08-25 04:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de1a3d6f-8d16-3bc1-a550-13712ca8b55b | -14.11063 | -53.99272 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba98a552-c534-3da5-8823-7643eed4995a | -15.65148 | -52.7259 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 025ac79c-86b5-3c40-9dc5-5bcba8a136c7 | -14.42969 | -56.46455 | 2025-08-25 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 110876ad-3803-3e6d-8d24-e4860d6a0f0e | -15.03788 | -48.16236 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 96979114-b09c-3710-b8fc-3d5afd35fe84 | -20.38675 | -46.73246 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 466ae4b9-07e4-3945-aff2-fa2e9c3b022f | -14.6452 | -56.56546 | 2025-08-25 04:44:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e626298a-e204-395a-ad6b-1f2479dde38b | -22.01319 | -44.28561 | 2025-08-25 04:44:00 | NPP-375D | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6a291122-f3cc-3153-8a65-66c9f19e04ff | -14.31513 | -53.07365 | 2025-08-25 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)
