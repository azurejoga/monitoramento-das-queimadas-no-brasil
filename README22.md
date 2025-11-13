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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4c2dec9-6055-3c81-abfb-d84762a1a837 | -13.37274 | -46.34857 | 2025-11-13 04:16:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 628b0ef7-87e5-3578-809a-41b0c8316317 | -20.89547 | -45.29504 | 2025-11-13 04:16:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4f674690-1b38-3897-9588-74678c0368f6 | -14.54476 | -46.57395 | 2025-11-13 04:16:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2cc0024-9aff-3d05-9ead-d8b045747d2a | -15.29549 | -43.89894 | 2025-11-13 04:16:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c14262ce-3f7f-328b-85af-d4ec6c247052 | -16.8408 | -46.07555 | 2025-11-13 04:16:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd83de15-84ae-3243-92df-1c18fe98ecc4 | -13.003 | -49.79365 | 2025-11-13 04:16:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf6f8a53-a99c-36fd-bb5d-8766a1379a0c | -19.05599 | -40.3271 | 2025-11-13 04:16:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 60bd5d1b-502f-3e12-9a3c-f8ebe515718b | -19.77241 | -41.26676 | 2025-11-13 04:16:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b73a3411-2793-356a-8b8c-3090a6f27430 | -16.54074 | -52.6022 | 2025-11-13 04:16:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa70d635-8977-3b59-bf14-24f5723ea33c | -18.1692 | -41.30862 | 2025-11-13 04:16:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2eedd640-69d9-3b86-be6f-3a18d283f48a | -16.44859 | -45.00311 | 2025-11-13 04:16:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e199acea-932f-361e-9c5b-315572e44715 | -17.50318 | -44.1016 | 2025-11-13 04:16:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 814a7816-2ae3-356c-8924-fc182a236edf | -15.08098 | -46.47672 | 2025-11-13 04:16:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ff2fd1a-e5ed-3d6c-b07d-17cc8770b6f1 | -17.96498 | -44.93187 | 2025-11-13 04:16:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3808bba4-7690-3690-ad9e-9aef99b71082 | -14.10079 | -44.2052 | 2025-11-13 04:16:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db10a6cf-a0ce-3be1-873c-7dc17f723bef | -14.6411 | -42.71127 | 2025-11-13 04:16:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ff46e31d-857c-326c-ae3c-f968f11e1702 | -18.1653 | -41.3086 | 2025-11-13 04:16:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63bd64b0-d4ac-3c09-a1ff-fc9e28928dc3 | -15.07762 | -46.47611 | 2025-11-13 04:16:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33ac04f6-4dab-3093-a4bf-d22dd46bf88f | -18.02084 | -51.03445 | 2025-11-13 04:16:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 180baf1c-7992-3d73-a974-370cdf6f0355 | -20.45466 | -42.50982 | 2025-11-13 04:16:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5fbcf15e-5cf6-3742-8c28-f05e2c9993b0 | -18.02488 | -51.03521 | 2025-11-13 04:16:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95bd3cdd-d4f6-338f-9c42-e39d4b57db9b | -15.49411 | -52.80383 | 2025-11-13 04:16:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60a4851f-2a79-3146-ab8f-5e0472aa9297 | -16.88204 | -51.6529 | 2025-11-13 04:16:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 226d78bc-e2f1-3f05-a806-f6160e403f55 | -17.03262 | -46.75943 | 2025-11-13 04:16:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb3cccf0-c5c2-3791-a06d-b23c912f2794 | -15.39403 | -43.06776 | 2025-11-13 04:16:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 8a4ab84b-25e1-3683-9931-fcfd32f01aba | -14.17183 | -43.58358 | 2025-11-13 04:16:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f46bd727-51ab-3961-8771-2e2cbe744e6d | -15.55008 | -43.17349 | 2025-11-13 04:16:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 997dfe91-7c59-30bc-a048-093b5196d445 | -17.28485 | -54.88189 | 2025-11-13 04:16:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9d827d8-6498-3234-a80c-92c3a0b34b5b | -20.91113 | -44.04402 | 2025-11-13 04:16:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 101c50d8-96bb-3a68-abf5-dd0694374b40 | -17.62355 | -46.70981 | 2025-11-13 04:16:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc0f3696-2d44-3dda-83e0-b243ef25145d | -17.76516 | -44.57261 | 2025-11-13 04:16:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e021774-7a80-3821-abac-acf9fa5b4b3b | -17.56078 | -54.02389 | 2025-11-13 04:16:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c69937f-b186-338e-8186-f4061ae96828 | -13.78156 | -49.39823 | 2025-11-13 04:16:00 | NOAA-21 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 924ff02f-0f07-31c1-8cf5-b427cb2e1533 | -13.49211 | -46.77918 | 2025-11-13 04:16:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05a7f133-3066-3913-a124-12ccbff28652 | -14.94747 | -42.36678 | 2025-11-13 04:16:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7c3d4977-037a-3092-992b-c2bcd8b783a8 | -15.84181 | -45.63966 | 2025-11-13 04:16:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 339eb27a-c397-347b-ab1c-65afc08e7b0f | -15.49465 | -52.80605 | 2025-11-13 04:16:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1fed624-d4f9-37b3-ba33-6b00f9931470 | -17.53964 | -53.715 | 2025-11-13 04:16:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75a34212-596e-37d6-afe4-588e4d1ecc88 | -18.97772 | -49.7808 | 2025-11-13 04:16:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6580747a-bba7-3eee-987f-e79e73a0e909 | -14.98848 | -42.41347 | 2025-11-13 04:16:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a636b006-941e-3883-a3eb-9aa5b3b3130b | -17.55475 | -54.02097 | 2025-11-13 04:16:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f58f9c92-4bf8-30a3-bb8c-94546ac9b023 | -15.64312 | -45.58385 | 2025-11-13 04:16:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dbf9139f-e6a6-37e4-b86c-b21ba9f0b5e1 | -12.41704 | -54.48375 | 2025-11-13 04:16:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36316542-a951-33e0-b15a-eeb377585bc4 | -16.44803 | -45.00669 | 2025-11-13 04:16:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 900e3b3e-88bb-33fa-818e-09336d8812b7 | -19.05187 | -40.32653 | 2025-11-13 04:16:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ce71a1e3-ca78-35c3-90c4-dba7b5af9570 | -15.62728 | -46.50948 | 2025-11-13 04:16:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8089da3-63e1-3bfc-bbc3-f82b47dfadc1 | -14.01442 | -44.08146 | 2025-11-13 04:16:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06207d2b-001f-3703-896b-10f4ccbf7bec | -14.67959 | -46.88904 | 2025-11-13 04:16:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5947bfd-05fe-33d0-81ef-4cb0269465e8 | -17.53482 | -53.71396 | 2025-11-13 04:16:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa9007f4-14a6-3d79-9a09-d7b600b670d4 | -17.2106 | -47.65385 | 2025-11-13 04:16:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30d09932-7259-36e7-8282-3bdb2decdffd | -15.62391 | -46.50891 | 2025-11-13 04:16:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| aac85307-3922-39b3-91e4-49113f6f8e3c | -16.99787 | -39.77337 | 2025-11-13 04:16:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 575fefae-8274-3638-92ca-ab9cab951a8b | -14.09835 | -43.4636 | 2025-11-13 04:16:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e282bd05-f560-38be-a6e8-a89f88752658 | -15.0152 | -46.6878 | 2025-11-13 04:16:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23ef7079-ed6a-317a-9ad9-c72eb99a8d92 | -17.21403 | -47.65449 | 2025-11-13 04:16:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdb62c3f-0f72-37ed-9063-4acda7b29a45 | -17.96015 | -47.25229 | 2025-11-13 04:16:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 72a8d891-3d2f-34d5-afb2-0a593c312bc2 | -15.39745 | -43.0683 | 2025-11-13 04:16:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0b79dfc8-a7b7-3024-9433-06bbe08f798d | -15.64974 | -45.58497 | 2025-11-13 04:16:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92e63ac3-50ad-3794-8587-15dc2864aea2 | -14.59444 | -46.65935 | 2025-11-13 04:16:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5e5c9cb-5795-3af6-954c-5d7e76d1b796 | -19.6604 | -43.6939 | 2025-11-13 04:16:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9d4ff19-0db0-312d-86da-eb2f9b5ae709 | -14.17128 | -43.58721 | 2025-11-13 04:16:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0be913ba-6327-38c2-a790-676de8ac0d2c | -17.62689 | -46.7104 | 2025-11-13 04:16:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0c0c35f-9262-39e1-83dd-188dd6501cd5 | -17.32059 | -46.49855 | 2025-11-13 04:16:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ba545a5e-68ff-3d07-96d5-07b779e2c170 | -20.09264 | -45.05893 | 2025-11-13 04:16:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 84cb9860-06ea-34c0-ba21-c84382b880d0 | -15.93756 | -45.99957 | 2025-11-13 04:16:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c26121a3-ce87-3732-bf08-c3c91bae4aea | -14.0989 | -43.45995 | 2025-11-13 04:16:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9e51b19-eebf-3185-9891-f0f31c5b0b6e | -13.75362 | -43.63221 | 2025-11-13 04:16:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d73504f8-4c3e-38e3-a4b6-e22035de6346 | -15.44315 | -44.1832 | 2025-11-13 04:16:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d17472d-d30c-3aad-aae2-53f97cc9d8d2 | -15.08159 | -46.47299 | 2025-11-13 04:16:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dff3de6-56a6-33da-99da-1937c5029924 | -17.55712 | -54.01674 | 2025-11-13 04:16:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71223f43-40c9-33a4-b7b2-05593e100744 | -17.03322 | -46.75574 | 2025-11-13 04:16:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03db7f9c-edf9-3359-b781-76ad00d60419 | -15.29883 | -43.89947 | 2025-11-13 04:16:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 924df192-5c73-32d8-8316-1bac744e2784 | -17.96414 | -47.24917 | 2025-11-13 04:16:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaf7b9c9-cfa9-3a9d-98de-4f868e67ffdb | -14.68068 | -51.89227 | 2025-11-13 04:16:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5078ec9-f12d-32cf-8eaa-091f3c0fff87 | -18.24969 | -51.27304 | 2025-11-13 04:16:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aae8c92-6f94-36fe-9601-70a7b03f424f | -15.1682 | -51.27216 | 2025-11-13 04:16:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9979ff32-3087-3997-87ee-f9bf32f5d2cb | -17.96352 | -47.25294 | 2025-11-13 04:16:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9981ada5-dcb4-3f4c-8cd7-be0da14af81e | -15.0158 | -46.68414 | 2025-11-13 04:16:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e69fa12-c231-3d49-97ce-708f4e5ce0b6 | -13.99636 | -46.72604 | 2025-11-13 04:16:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e5df7ad-1f5f-3f2c-a637-c4a40cc2cd33 | -15.67397 | -45.88032 | 2025-11-13 04:16:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ea939c0-f8f0-35f1-bd89-9c00c7d64f03 | -22.65975 | -44.72468 | 2025-11-13 04:18:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4c8f8f4a-4a6e-346f-8c10-08a389fac33e | -22.02833 | -44.247 | 2025-11-13 04:18:00 | NOAA-21 | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c1ca18d5-29f2-33df-aea5-e038f0c7d046 | -21.65443 | -46.76556 | 2025-11-13 04:18:00 | NOAA-21 | DIVINOLÂNDIA | SÃO PAULO | Brasil | 3513900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cac57d05-6c4d-39de-8ad1-202c8048119f | -22.89766 | -43.65533 | 2025-11-13 04:18:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d2259ae4-b442-36d5-b7d4-0c5c880f6a65 | -21.65833 | -46.76245 | 2025-11-13 04:18:00 | NOAA-21 | DIVINOLÂNDIA | SÃO PAULO | Brasil | 3513900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69537505-74f9-3068-858e-2c6ae1a99ad2 | -22.64613 | -44.91642 | 2025-11-13 04:18:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ab17d569-e6dd-3118-a078-c43101281b65 | -22.4646 | -44.20085 | 2025-11-13 04:18:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b4a7faa3-e9a7-34c4-88e6-769765b41fe4 | -22.46751 | -44.20551 | 2025-11-13 04:18:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b79de018-a394-3fb2-9180-e86a265c7f69 | -22.46402 | -44.20496 | 2025-11-13 04:18:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 929dc792-0845-324d-9f36-a9fb2414768c | -21.64104 | -44.19609 | 2025-11-13 04:18:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aa61a219-2d3a-3b8c-ad95-bfa8167d5de4 | -21.49105 | -44.94025 | 2025-11-13 04:18:00 | NOAA-21 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9ec0dbe4-a8ae-3e97-aef9-0d0e2261f89c | -21.85701 | -45.01935 | 2025-11-13 04:18:00 | NOAA-21 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b8decdaa-d188-34bf-b16a-c43b81fdc661 | -22.93321 | -45.3486 | 2025-11-13 04:18:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 18ef83d1-20c1-369a-8dab-ae40960b84c7 | -21.65561 | -46.75815 | 2025-11-13 04:18:00 | NOAA-21 | DIVINOLÂNDIA | SÃO PAULO | Brasil | 3513900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ca5194bf-b249-3bb3-a336-f289cd107c44 | -21.65891 | -46.75875 | 2025-11-13 04:18:00 | NOAA-21 | DIVINOLÂNDIA | SÃO PAULO | Brasil | 3513900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 37a3294a-5113-3ea7-bc68-5a237d5f3a62 | -22.0214 | -44.24583 | 2025-11-13 04:18:00 | NOAA-21 | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a9167aa1-f04e-30a0-8378-34ea38a18e8f | -22.02429 | -44.2505 | 2025-11-13 04:18:00 | NOAA-21 | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a5b684c4-2def-3855-a2d1-ff0e8d825785 | -22.73661 | -44.8464 | 2025-11-13 04:18:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 69c95ff9-9afe-33ef-84e3-be6fc9b69507 | -22.47274 | -44.1937 | 2025-11-13 04:18:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 63b2a631-c90c-3704-910c-f5b9cbcf2091 | -21.65502 | -46.76186 | 2025-11-13 04:18:00 | NOAA-21 | DIVINOLÂNDIA | SÃO PAULO | Brasil | 3513900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
