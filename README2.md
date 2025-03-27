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
| 4991a91e-9ca6-3cf2-99cd-e1eeb2d240bd | -7.06861 | -44.37751 | 2025-03-27 03:51:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc1a4849-3a41-3f1b-abae-449a38a57da4 | -7.23941 | -44.77537 | 2025-03-27 03:51:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 894e0677-320f-3bcf-8a32-36ed53ca8861 | -7.37846 | -41.40889 | 2025-03-27 03:51:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64d2ecfc-a5fe-37d8-99a5-3698d17cc1e2 | -3.93747 | -41.49255 | 2025-03-27 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 546e33b8-6f5d-337b-b1de-582a8a9eba8b | -3.95524 | -41.48438 | 2025-03-27 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ecc49ba-6cd3-3e2e-bc4e-8a5513f5bd9a | -7.22196 | -35.7917 | 2025-03-27 03:51:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 67b4228a-9085-3f52-9cbd-423df1eaa7a0 | -7.23867 | -44.77964 | 2025-03-27 03:51:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 889ad093-ee61-3e12-b53a-dbe3360c57d9 | -9.62106 | -40.37098 | 2025-03-27 03:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da2c3269-bf52-3dcc-b28d-fcef306497df | -7.61303 | -39.24371 | 2025-03-27 03:51:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95205a53-252e-3786-89fb-085e788fe39b | -3.93878 | -41.49102 | 2025-03-27 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 055381e1-23fc-364a-9d48-f2174cc98594 | -9.15815 | -43.127 | 2025-03-27 03:51:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4de9227c-9f98-32f6-b13d-d761c5b43dd4 | -5.42624 | -39.51221 | 2025-03-27 03:51:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2a6eec86-c7c1-37af-8d40-c2854565889e | -7.235 | -44.77463 | 2025-03-27 03:51:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b08284b3-8575-3056-9d6f-e269f8932311 | -7.06723 | -44.38551 | 2025-03-27 03:51:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c74b87d9-45ff-3c46-a8ad-3977abeefbd6 | -7.24014 | -44.77111 | 2025-03-27 03:51:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 913b5c06-9ff4-3cc8-b189-a7a5b6488020 | -3.93578 | -41.48589 | 2025-03-27 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75b9570a-be73-308e-a156-bda2aeec8224 | -3.93503 | -41.49041 | 2025-03-27 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e523e78-0d45-3e62-ab08-6facb8011636 | -3.9545 | -41.4889 | 2025-03-27 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4bd1ca83-2478-3624-924a-c6c04a0121e2 | -3.93445 | -41.48742 | 2025-03-27 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 867476fe-b70c-3501-89d3-634a9ece63dc | -8.3762 | -44.04117 | 2025-03-27 03:51:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48239978-648e-3235-87df-be919b5d1f2b | -6.0134 | -43.8745 | 2025-03-27 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b3ccf5b-5585-3b12-9335-d9c72f572941 | -10.36693 | -36.3434 | 2025-03-27 03:51:00 | NOAA-20 | PIAÇABUÇU | ALAGOAS | Brasil | 2706802 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d4b16c97-4fdc-3f42-9a82-61e637147f23 | -6.00917 | -43.87384 | 2025-03-27 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56882cd1-8805-3cce-aee3-405c0d5f577b | -10.52013 | -37.7408 | 2025-03-27 03:53:00 | NOAA-20 | PINHÃO | SERGIPE | Brasil | 2805208 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4196f753-8c78-38a9-a9db-eb22e97e3551 | -16.23779 | -39.17979 | 2025-03-27 03:53:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0e45acd6-6ee1-304d-93c4-215c65d0fff0 | -10.69298 | -40.4262 | 2025-03-27 03:53:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b522daa1-3e8f-3528-b094-45063dbd4ed5 | -10.52068 | -37.73717 | 2025-03-27 03:53:00 | NOAA-20 | PINHÃO | SERGIPE | Brasil | 2805208 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1341d36e-d485-380d-a069-f068a4aad8b2 | -12.43776 | -39.24005 | 2025-03-27 03:53:00 | NOAA-20 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 734dc8c2-1c2a-3d25-9699-9b09370e99fc | -14.13348 | -41.69118 | 2025-03-27 03:53:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 061c8c93-6f71-36de-b043-97cdad58d9a2 | -10.43721 | -43.34784 | 2025-03-27 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ffa7706-913c-3071-abc5-38813d49f27d | -11.28238 | -37.28018 | 2025-03-27 03:53:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9c6ec144-a829-35a1-939c-d691ec09cde5 | -13.20717 | -40.49546 | 2025-03-27 03:53:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c2da3407-0a42-320a-a765-1b08ac1f3036 | -11.28295 | -37.27639 | 2025-03-27 03:53:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1b6a713c-35d5-37a7-b03a-ac0382610e8c | -13.20385 | -40.49491 | 2025-03-27 03:53:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 59784e29-1803-3bdd-8a70-d36dd5829305 | -11.27952 | -37.27586 | 2025-03-27 03:53:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d1af2f86-61c3-3f94-8b82-ef2fb02f08df | -10.50184 | -36.79419 | 2025-03-27 03:53:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f17c9a51-43a8-34c0-9f51-b29955741f39 | -12.86104 | -38.36618 | 2025-03-27 03:53:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 426b7ae8-e0d9-31c8-a1e4-0d371779552e | -13.95955 | -41.48994 | 2025-03-27 03:53:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7decc3da-88fc-3ba0-b82c-a84cfb0d2bf9 | -10.43204 | -40.50236 | 2025-03-27 03:53:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 66de8881-154e-3a7b-9912-10d1b186368c | -11.25187 | -41.90517 | 2025-03-27 03:53:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1f4dd1e9-c6f2-324a-b4c3-25993556bbde | -12.22408 | -38.13692 | 2025-03-27 03:53:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a37a86ab-0a3a-3620-b432-07258793d422 | -10.86402 | -36.98837 | 2025-03-27 03:53:00 | NOAA-20 | BARRA DOS COQUEIROS | SERGIPE | Brasil | 2800605 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d45dfd0e-d303-3c97-acdb-f2905e2aa763 | -11.27895 | -37.27965 | 2025-03-27 03:53:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 527c04c2-eca4-3f0a-98f7-38ff29b13dbc | -10.34732 | -38.47026 | 2025-03-27 03:53:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 69ac370f-9fc2-32b4-8d99-ea2088cb5f84 | -19.8853 | -44.76376 | 2025-03-27 03:55:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86f034c2-766f-30eb-b2a0-896e25474b59 | -21.83034 | -47.0362 | 2025-03-27 03:55:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b24503a-65f9-35c2-bbbb-6b286f4ce9ec | -20.99696 | -51.79465 | 2025-03-27 03:55:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| af809060-e767-3bf7-b92c-ab35d0b9fd40 | -21.69419 | -50.36767 | 2025-03-27 03:55:00 | NOAA-20 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 42c025b0-7dfa-3697-94ca-a874a22806bb | -21.6924 | -50.36691 | 2025-03-27 03:55:00 | NOAA-20 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 10d11fa2-e9b2-3bd9-95d9-ecc1f49e4b5a | -20.08169 | -47.22179 | 2025-03-27 03:55:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 672f66d1-dd7c-385a-ae75-7cecc5d53219 | -23.33625 | -46.7742 | 2025-03-27 03:57:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7db3796-1376-31ee-86d8-35adb27a6464 | -25.19712 | -49.32449 | 2025-03-27 03:57:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ee764bd-b393-3cfc-a112-d23964465f5c | -27.64481 | -52.90708 | 2025-03-27 03:57:00 | NOAA-20 | ENGENHO VELHO | RIO GRANDE DO SUL | Brasil | 4306924 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9c27ce99-aff6-3120-83ad-54c0d1da1118 | -23.40455 | -46.5537 | 2025-03-27 03:57:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 804018f9-778e-3ad4-8695-d0fc2d9de016 | -22.53795 | -48.8109 | 2025-03-27 03:57:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5d3ea99-87c3-3fdf-abc4-58ec0a6f82a8 | -23.29735 | -46.6864 | 2025-03-27 03:57:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14544735-c44a-39b7-944d-ed3847269ac9 | -25.19197 | -49.32777 | 2025-03-27 03:57:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 52b95d92-3aac-36b8-8965-faade41a71e1 | 1.52781 | -60.71306 | 2025-03-27 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 673626b7-d604-3d75-a057-13e77b74d66b | -3.95738 | -41.48748 | 2025-03-27 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 219f46b5-8ea2-3faf-b285-acf8107007a5 | 1.52708 | -60.70812 | 2025-03-27 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4d7eee7b-58c8-389e-98f1-3648f4d4a823 | 1.52877 | -60.71043 | 2025-03-27 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4caa21b3-2814-3790-bed2-ba9cb5d837a4 | -5.39768 | -46.95889 | 2025-03-27 04:44:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba7947e9-465e-353d-9f95-ec8b92787c80 | -3.93529 | -41.49069 | 2025-03-27 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c109c241-4db0-3010-8099-f009fc65c663 | -3.93576 | -41.48742 | 2025-03-27 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 081b9422-09d6-3278-b5fd-90ad3176f118 | -3.73777 | -49.68484 | 2025-03-27 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcb6aae9-8520-3fed-9295-ff71f46da259 | -4.36275 | -48.66928 | 2025-03-27 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d35b6b9a-fa86-3174-9203-6bc124c5def8 | -6.01328 | -43.87279 | 2025-03-27 04:44:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 552f1991-db37-369a-ae1b-a7fa46c0e3bd | -13.2624 | -43.0212 | 2025-03-27 04:46:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 011d17a1-359c-36e3-8dfc-85e3b92c726e | -7.06528 | -44.38212 | 2025-03-27 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21750c27-ce14-33ac-bce5-c478e4cfe77f | -7.23984 | -44.77395 | 2025-03-27 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1a81927-8667-3667-995f-fadfb7922a4c | -7.07048 | -44.37807 | 2025-03-27 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40e812dc-d50d-369e-8e39-6a60b2c4fbf3 | -6.21515 | -48.05223 | 2025-03-27 04:46:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04cf6604-657e-3911-8325-e7d37a85fd1e | -7.06982 | -44.38283 | 2025-03-27 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 553719d8-f463-3f8d-a0b2-e948f89f535e | -10.44035 | -43.34517 | 2025-03-27 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8338376b-6cb1-36d4-9771-7e410e3e21d4 | -11.25338 | -41.90673 | 2025-03-27 04:46:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c7c5f110-6ebc-3c61-8016-50c3b1cf7cef | -6.21158 | -48.0517 | 2025-03-27 04:46:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9de0054-29da-31ce-873c-6b49a7e6de9d | -8.37915 | -44.04035 | 2025-03-27 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52eadedb-211a-355a-90c5-119e86cff042 | -7.23479 | -44.77769 | 2025-03-27 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19f7ffb3-ee4e-3cb6-9ca3-fbe4a2b57fcb | -7.23921 | -44.77839 | 2025-03-27 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8a4a629-481b-319b-9895-a1044b29edce | -10.43995 | -43.34835 | 2025-03-27 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2fd4839-d3c7-3f87-8fcc-d34c3539432a | -6.21218 | -48.04763 | 2025-03-27 04:46:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| def959bd-bfb5-34ac-ac1f-4c86d2201aed | -18.63424 | -54.47562 | 2025-03-27 04:49:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c30eae8f-5e6a-3a24-9d6c-351e4e14291b | -21.4104 | -48.53138 | 2025-03-27 04:51:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e98dff7a-5317-3d78-860d-61fc8c390264 | -23.33942 | -46.7707 | 2025-03-27 04:51:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b44a1b9-379d-3485-8f0a-d4e16cc8eb57 | -25.19912 | -49.32505 | 2025-03-27 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c5f0ac26-878e-336e-ae5d-11e37e435bcf | -25.1902 | -49.32814 | 2025-03-27 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8b2283c-b72d-371d-b651-d4fe1f791cdc | -19.54362 | -54.95937 | 2025-03-27 04:51:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0348caed-ef22-365d-be34-aa6a0295a17c | -20.1379 | -50.71797 | 2025-03-27 04:51:00 | NOAA-21 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 51480cda-57c5-330a-9bb3-c80c575ab89f | -21.23683 | -56.46625 | 2025-03-27 04:51:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d562dcf-5977-3129-8431-c9f9de6f6d09 | -20.45704 | -50.08606 | 2025-03-27 04:51:00 | NOAA-21 | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bad5651-8157-3ff2-b49c-4895ce6b6b13 | -20.59839 | -56.10021 | 2025-03-27 04:51:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56f56bbb-c7a2-38e4-8dab-fd2efb1e9660 | -23.98393 | -48.91707 | 2025-03-27 04:51:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a188b559-0d64-359a-89d6-f780fa516077 | -19.42208 | -54.78244 | 2025-03-27 04:51:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed51430a-b75b-3073-ba06-4f50067a1112 | -21.5748 | -55.97408 | 2025-03-27 04:51:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c9e633f-9dd0-3e4b-b91d-b5de03fcfd7b | -19.42481 | -54.78672 | 2025-03-27 04:51:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa3cba79-e6a2-3073-aa04-f3a6b2c49a04 | -19.4254 | -54.78304 | 2025-03-27 04:51:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f92d001-7dbb-3d0a-a4fd-e4994dbd954f | -22.05863 | -54.40711 | 2025-03-27 04:51:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 007fd9c7-73f9-3129-8c79-57d729b7029a | -21.1002 | -56.04062 | 2025-03-27 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e017c9ba-52f6-3853-b3d5-cef3ba11f3ad | -22.15163 | -56.12707 | 2025-03-27 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb9b0407-dd5a-3a9c-8d0a-4e20449ac36e | -21.57817 | -55.97469 | 2025-03-27 04:51:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
