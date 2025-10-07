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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9b5d49b-9c82-3997-8b12-933b651f0168 | -14.76239 | -46.02703 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc05b369-a1b6-373a-ab16-d6d5fd5f69f2 | -18.1164 | -53.3442 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86e9dcfb-db41-3be5-ab25-dac8bb87d584 | -15.49906 | -47.93221 | 2025-10-07 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 51f74794-2c5b-3894-b4bc-fcf6c2183dd3 | -15.2797 | -46.34415 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75fe25d3-7313-38c7-9fe0-eb28db48fc40 | -13.71761 | -48.06467 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3de4a205-fb14-3cd2-9ddd-ce5521feeef4 | -14.50924 | -46.9219 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 431e34e8-af20-3784-8d4d-870ef9ee1557 | -14.92756 | -51.40999 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bedd1a72-77fa-3f3e-bbb5-6564bb9c877d | -13.76396 | -45.7332 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 20ca524d-d0ac-3ec7-8acf-7ba516b788a4 | -13.58577 | -48.1462 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bebf7c39-dc43-3332-b780-16032ad9f266 | -15.56244 | -52.44736 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d847958-38c2-32a9-af3e-8473656b9cfb | -12.578 | -52.2023 | 2025-10-07 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 077636c3-f22d-3339-9e28-926972d4f08a | -14.75488 | -46.05046 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 917a5ac7-8c52-3bf1-b519-376fdf59ac02 | -12.25382 | -47.84856 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0157214e-b413-30b3-a4cc-0d82547baf0c | -14.91926 | -46.81456 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee358288-824f-30ae-9bc0-00797f4c014c | -15.59069 | -52.56043 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d89d7e5d-d718-3c48-9836-0c391c5401ce | -13.53875 | -42.996 | 2025-10-07 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 105.4 |
| fd78d355-0657-3121-a058-237496638ab6 | -18.28026 | -45.46329 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0766b50-fd0a-365b-9476-b5d3bfa55752 | -13.65693 | -47.28341 | 2025-10-07 04:10:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a68818f0-88e1-3c53-8aa2-d0b8b3cadbd0 | -13.28678 | -47.57473 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7316c40b-a004-3084-89f4-7eeec8e1c929 | -19.70772 | -44.11778 | 2025-10-07 04:10:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39055390-4ff1-38da-b71b-abf6cdbf498b | -15.7826 | -46.25445 | 2025-10-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76a4fabd-4bed-3961-9a03-9e4620d3ad6b | -13.36232 | -47.56332 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0029a8b-78a8-3a08-81fd-1dd95366cd4b | -13.74094 | -48.65828 | 2025-10-07 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f1be94a-b8c6-345c-b1bf-3f8261db104c | -12.73051 | -47.9346 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c441560-adfc-370f-90da-39a047f95805 | -13.81019 | -41.82581 | 2025-10-07 04:10:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 67b0e3f5-67ce-3b87-8967-e14ee86249f0 | -13.26606 | -48.05872 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f32ad95-57bd-3628-9ee3-6fe4d753b788 | -14.61263 | -52.48935 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30e690a0-fbed-3902-9614-bafe87fa61cd | -13.26714 | -47.59634 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36df53ae-4f2a-3903-b1f4-973c1aebd44c | -12.54512 | -48.14533 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 716824a7-a16d-359b-b63b-f8c4dfd73dd2 | -14.93605 | -46.80334 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9ee64cc-2957-3664-91bc-260b2c652fa8 | -14.76468 | -46.05623 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1739f8ca-97a1-355a-b438-d61525b52acf | -14.93302 | -51.43136 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08a735a0-8f28-3ecb-9fb1-9c1b14213754 | -20.40735 | -43.35213 | 2025-10-07 04:10:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d3be7e02-8084-3ec5-80cc-7ee9da80d131 | -14.74012 | -46.0315 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e9200031-a336-3aea-95bb-960ad6bd8940 | -15.39274 | -48.0049 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00ea33ca-c7fe-3956-b886-ca27b693f41f | -13.092 | -47.85712 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc97ff85-34e0-383a-bb83-593c1a84fd9c | -15.55735 | -46.82586 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96e98b61-beeb-39b5-b517-0ac45744f21a | -15.48213 | -47.93922 | 2025-10-07 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bcc6cb4-cd65-351d-8d5c-a5def41ac4b0 | -18.51162 | -47.52225 | 2025-10-07 04:10:00 | NOAA-21 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de658440-41a6-3526-8b39-50a9fb40a4e2 | -12.38929 | -51.08678 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b4fabdc-2782-3ba4-adb2-ce46c0c2d036 | -18.28146 | -45.45583 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5de41798-099e-3cce-b86b-c7df5ae4eba3 | -15.57841 | -47.28774 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0b5bea5-5c23-35f3-b6fa-df00dcf2aa25 | -19.95529 | -44.62852 | 2025-10-07 04:10:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 764090ef-ae41-3978-8d8c-540e6f55afe2 | -13.37078 | -47.24772 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a23a3ea1-fff0-368a-aab2-229d26cb9a66 | -14.7296 | -46.00887 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ab50269-1f0d-32f6-8ea5-dd01614b6ee2 | -19.28425 | -44.34932 | 2025-10-07 04:10:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f369ebaa-9b5e-30fa-b5de-d0b5c6710436 | -14.93139 | -51.4143 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7321716d-6303-34e3-8ed5-8a9d0d27d5d3 | -18.56859 | -44.18312 | 2025-10-07 04:10:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d1380460-6270-3174-93a1-75ff7125b016 | -15.05808 | -42.33654 | 2025-10-07 04:10:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 56941fe9-dd0d-3d0d-b96d-fe8c9dcdc7c3 | -13.39198 | -47.5972 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 582faa5b-3ce6-384b-9fdf-735c5ce3dd5c | -16.06586 | -50.92268 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f56354f9-c616-3cc9-9e21-40ef73aabde6 | -13.02599 | -51.03224 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b8028584-2495-3237-80d4-cb4ae6e7ba14 | -13.24251 | -47.24713 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4226c96-267b-324b-860f-981e56013032 | -14.38873 | -45.93163 | 2025-10-07 04:10:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66184083-8f0d-3aed-87f9-1761e951524b | -19.60899 | -43.20063 | 2025-10-07 04:10:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| aa4814cc-7b11-3aad-a818-e2c7b174c1a4 | -16.06896 | -47.77351 | 2025-10-07 04:10:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d41fc1db-47af-3b31-8599-27c29c1aacdf | -15.36456 | -47.32705 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 762b1dea-8788-3d5b-a686-c270d755bafa | -14.247 | -54.25212 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 092b9778-e533-39ef-9b3d-074032c6160c | -15.35727 | -47.30787 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c818fec-4605-30ca-84c5-4ea6a184c940 | -19.59867 | -44.8624 | 2025-10-07 04:10:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae1a1772-305b-3b90-b746-7f3834053f58 | -20.4507 | -44.17148 | 2025-10-07 04:10:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9e5abf8c-f3b2-3344-9a25-3bb31bf67693 | -15.60691 | -47.29741 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d275e97e-dc48-3238-b767-6afe9fe92f7f | -17.56222 | -46.0731 | 2025-10-07 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf502357-f0bf-3f5c-a523-1cf27d26a5ea | -18.0456 | -42.0231 | 2025-10-07 04:10:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad5c2337-0b14-3861-b681-a12ff0074a9d | -15.49863 | -46.83367 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfcc377e-d358-30aa-86ce-d35eddc613b3 | -14.92583 | -46.79802 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32d64cdc-0a16-35db-87fa-9f7f0c3c098c | -12.94841 | -46.81109 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6a264b0-85df-3faf-93a8-08b4b007d6df | -15.79048 | -43.65369 | 2025-10-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 40971259-28ca-3033-8061-848624e5972f | -16.02256 | -51.05004 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae520a1d-d8c7-3417-ac33-87f31173d7b6 | -15.37913 | -47.99281 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d3298d2-88ec-3225-a025-fd4b9f7c615a | -13.3738 | -48.04319 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3d9f8cb-6a9c-39d2-84d9-4fefe43adf7e | -16.29544 | -45.2438 | 2025-10-07 04:10:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87fe5a3e-a92e-3b8d-8e0b-c9c3dc57072a | -16.04572 | -50.95411 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6252cd0f-5d84-38f0-a353-14de1a01b720 | -13.07952 | -47.88321 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03e749d1-d114-3317-b9a0-2b7b1a671b63 | -13.71101 | -48.07892 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d12a13e5-f9a5-35b2-ba77-554fda34402a | -18.11005 | -53.37536 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5ab72f4-2a00-3407-b70f-f44ccd50a615 | -14.96713 | -49.95033 | 2025-10-07 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b90aa82-a98b-3d69-86ed-9e1e9fd2b696 | -19.59265 | -44.85761 | 2025-10-07 04:10:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33e52cce-96e5-30f9-9f53-e16de96bee6f | -13.25177 | -47.79787 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf328a10-a8a4-3d43-8306-9bfdcade7d90 | -16.10588 | -48.94371 | 2025-10-07 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dee6258e-98d5-35ae-b2ef-d6d07a3f876d | -14.9229 | -51.40704 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8a507cd6-a1d0-3cb8-8a3d-c095184d7414 | -18.2798 | -45.40249 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5254697-84cc-3e8c-8f95-636d4c5d4bc4 | -12.57737 | -52.20558 | 2025-10-07 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| db7870a6-f0a6-38e6-90e9-b4b3aa513c24 | -13.05992 | -47.92644 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6ea399e-fbeb-38b5-bb29-c12bf20bc043 | -14.8091 | -44.8945 | 2025-10-07 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 135a6698-77f9-3565-8983-72b4200da6b6 | -14.71399 | -48.34707 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41714709-b292-3e50-a91e-da8a66457f14 | -13.08004 | -47.83361 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae8cf922-eea5-329a-a567-9f21a866465e | -15.88414 | -46.25647 | 2025-10-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eef25b79-6b91-31c2-832d-460bf0087411 | -15.19571 | -56.8198 | 2025-10-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed792800-050a-3e1b-ad5d-bd1ad50ed57d | -14.91189 | -51.4404 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c025956f-226e-33b8-80bc-a0bff69ba0f2 | -15.0813 | -46.6358 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9492f96c-39a1-32a7-b2d6-8717da536afd | -13.26352 | -48.05639 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c3d0271-123d-369b-8e38-1662de6ba44b | -13.06605 | -47.89089 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44b208ea-6fdc-3794-9804-6824c7b93f8c | -15.22101 | -56.78754 | 2025-10-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26a192d7-f83a-314f-b9d2-f53d68dae63f | -15.27693 | -46.33909 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7f0d61b-9439-341d-85e5-81784fe2bc6b | -20.20576 | -43.92688 | 2025-10-07 04:10:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b4122363-6c25-394b-8e62-68eb50f78991 | -14.77447 | -46.06208 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| fed71f22-06e7-3562-afb6-0c1ebe68985a | -15.91264 | -48.82785 | 2025-10-07 04:10:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 002d51f4-7686-3b3c-8a1f-ce9eba7a6bbc | -19.39356 | -44.39017 | 2025-10-07 04:10:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b38b193d-a2d9-335d-b8e0-7c8b73cad40d | -13.73859 | -47.94697 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README45.md)
