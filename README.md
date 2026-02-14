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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d99b0ea-3f47-3540-9b74-840cf7699a50 | 3.8216 | -60.9414 | 2026-02-14 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 1ef2c487-1801-3e87-bb84-a64f2f7da039 | 3.8216 | -60.9224 | 2026-02-14 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 01bee664-d2d8-3ad9-a204-afc2b5e43f6a | -18.71364 | -43.00752 | 2026-02-14 00:05:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 058eacf1-ef5a-3cf1-9692-14e68bec5efc | -11.67822 | -43.89429 | 2026-02-14 00:07:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b28e8f13-ab40-3837-b2f0-a7aa35f5599a | -12.3921 | -43.66338 | 2026-02-14 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3dcf9d17-1fc0-3ba2-9071-d943d7d11f33 | -11.8993 | -45.28 | 2026-02-14 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7f0b2eb2-8726-39d4-8440-e7708c038b5c | -10.59867 | -44.34114 | 2026-02-14 00:07:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c6a2e21f-5abf-30ca-861e-dcce3c122a5a | -15.00169 | -45.14989 | 2026-02-14 00:07:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1aaa00f4-b598-36b3-83da-dd0eef626925 | -11.71212 | -44.73339 | 2026-02-14 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 929000c5-acfd-3357-a0a5-0d611c7b773b | -11.78764 | -44.74389 | 2026-02-14 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3b9b81d-1a3e-3a70-bdd4-515f74a718ed | -14.46975 | -46.98906 | 2026-02-14 00:07:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a0daecb4-772a-32e2-b7e7-2b62d0425945 | -11.89808 | -45.27097 | 2026-02-14 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8b438a4c-4175-35cd-9fb0-7c8cd088566c | -10.6124 | -44.3517 | 2026-02-14 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 27d2b5e9-c1a7-3beb-a0d5-b1f2ee0b07fd | -10.6128 | -44.3284 | 2026-02-14 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| a8846ba4-0e72-3a51-a5c4-0be6d75da50d | -10.6128 | -44.3284 | 2026-02-14 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f14aa150-efdb-3b05-8621-c7fab69b7b3e | -10.6128 | -44.3284 | 2026-02-14 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b11fa40d-db5c-398f-8189-ad2b5e0cd361 | 3.8216 | -60.9224 | 2026-02-14 01:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 77c81da3-7c0e-3503-9fcc-0fdf296f22aa | -10.6128 | -44.3284 | 2026-02-14 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 1fa95ca6-a5c6-346d-adf1-5dbd99148df6 | 3.8216 | -60.9414 | 2026-02-14 01:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 98.0 |
| d4151dce-35e4-328e-bce4-0ca5d0c0fa79 | 3.8216 | -60.9224 | 2026-02-14 01:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e589d4fb-93c7-3bf1-9637-a272a474accc | 3.8399 | -60.941 | 2026-02-14 01:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a4c6cbd6-b23a-3bad-8f93-3d393ce4d15d | 3.8216 | -60.9414 | 2026-02-14 01:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 377af51e-b584-361a-9537-e10f62e0fa0f | 3.8399 | -60.941 | 2026-02-14 01:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 43443854-3f28-3419-9b53-861308490fb1 | -10.6128 | -44.3284 | 2026-02-14 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 2604285e-6eee-313e-8243-e097bcfa3476 | -10.6128 | -44.3284 | 2026-02-14 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| fec471cc-ce9b-33b3-8746-ec63d771d946 | -10.6128 | -44.3284 | 2026-02-14 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a9831912-cf38-3362-8774-9c3b817f07a3 | -19.6427 | -40.6471 | 2026-02-14 03:20:00 | GOES-19 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| cdb50a38-e309-36dc-9d91-285a887a6b1d | -10.6128 | -44.3284 | 2026-02-14 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 21bdf8a5-9c9d-3152-ab92-01a1adcacf68 | -2.94462 | -39.94822 | 2026-02-14 03:29:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 10a3d78f-8285-3ece-b0bd-123777a8c171 | -4.51644 | -38.28913 | 2026-02-14 03:29:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08bf58d2-e04e-35c5-9d7e-a8742f2fb128 | -4.5209 | -38.28984 | 2026-02-14 03:29:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f46d942b-7194-336a-b78f-e5b940767690 | -3.32137 | -41.47179 | 2026-02-14 03:29:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a23c5ef6-5518-3ca3-a2f7-8b911d4bfedb | -2.94975 | -39.94905 | 2026-02-14 03:29:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c25ff9e9-76d9-3f52-8a39-1cdc1e45ddcc | -2.94925 | -39.9521 | 2026-02-14 03:29:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1912afb7-93e4-324e-8722-f5dbbe52c63f | -10.6128 | -44.3284 | 2026-02-14 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4ffc2b3c-eefd-3744-a1cd-4834fdb48f21 | -10.60539 | -44.33328 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 84cff55f-a742-3682-a8ae-902e38f222c8 | -10.60596 | -44.34121 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 6bf89ba5-792b-32f4-8262-57219ee57504 | -10.61049 | -44.33913 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 17da968b-dc24-399c-b313-93056f5ae658 | -10.6036 | -44.34262 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 15fe2a01-c369-36cb-87f8-9b5e7d704e2a | -10.6078 | -44.33194 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 86ba7064-ee5c-3e11-9a7a-8e65caefe808 | -10.60689 | -44.33654 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 275dbeee-23a0-37cf-9486-4acaead68180 | -10.61138 | -44.33451 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e8cf4835-8728-38fe-b277-a790f205aada | -10.5985 | -44.33675 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f02420b6-adac-38aa-9718-be94bf8a8c81 | -10.60959 | -44.34382 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5ed156a7-a604-3c2e-b95c-dd0b4ce05a84 | -10.68642 | -40.30881 | 2026-02-14 03:32:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| de96da55-9566-3f23-a50a-0c7f25a8186f | -10.60089 | -44.33538 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3a985b80-7376-3cc4-8cd9-db592e6acfa8 | -10.59995 | -44.34005 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 24295625-59f6-318c-85f6-8cc368b377db | -10.6045 | -44.33792 | 2026-02-14 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b385f817-bad2-3070-9e34-ac61084c7182 | -11.2859 | -38.23235 | 2026-02-14 03:32:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 155283bf-21a9-3983-b142-9ee5f9301580 | -18.54497 | -39.79768 | 2026-02-14 03:34:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 73285221-3332-332a-9524-b41666da5ae1 | -16.94956 | -43.14082 | 2026-02-14 03:34:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4226943b-2a89-3090-a966-d0ae75d371cc | -15.00295 | -45.15392 | 2026-02-14 03:34:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c19824c3-73ca-3426-ad7d-66d5a2ca70c9 | -19.64133 | -40.65001 | 2026-02-14 03:34:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 7ba67b11-132b-338a-bb41-f3594a17432e | -15.00255 | -45.15029 | 2026-02-14 03:34:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 270c2e21-449e-3b30-a7a6-cf38c7e3291e | -15.00347 | -45.14594 | 2026-02-14 03:34:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 132f8c87-b39d-37fe-b8a9-d2bb9e80e359 | -18.54487 | -39.79962 | 2026-02-14 03:34:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4b907828-cfa9-355c-b753-0831dbb46cfd | -17.62583 | -46.66716 | 2026-02-14 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 312d1fe1-517d-3523-bfa7-63c0b693969c | -14.99366 | -45.13485 | 2026-02-14 03:34:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 958a29c4-1232-3a59-aab9-33ff6307711a | -19.63728 | -40.6493 | 2026-02-14 03:34:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 271bb944-611a-3dfe-9539-c5b666dc89db | -16.94514 | -43.13713 | 2026-02-14 03:34:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d41ddfd-9bc2-3519-a7a6-ab0dd5153909 | -17.61975 | -46.6658 | 2026-02-14 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9985f42c-3bf3-3fb7-b0c4-12e48326fc55 | -14.99273 | -45.13921 | 2026-02-14 03:34:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f701752-007b-38b8-9f6f-42d05b7d90f2 | -19.64207 | -40.6461 | 2026-02-14 03:34:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 45.5 |
| d3dfb87d-2bcc-342c-9dde-4ace8afb6cf6 | -22.90967 | -43.30985 | 2026-02-14 03:36:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f9b582a4-148f-385e-a89b-d667617bd97a | -22.90774 | -43.3073 | 2026-02-14 03:36:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c85cbf7e-e715-3c9a-aeec-c558584606d7 | -3.3214 | -41.47375 | 2026-02-14 03:59:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c158830e-9975-3b3e-af17-34d488c7f3ca | -4.52032 | -38.29043 | 2026-02-14 03:59:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b38a42c7-de0a-3385-98f9-62737f548bf1 | -4.81462 | -38.69678 | 2026-02-14 03:59:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b43efdc7-8bcd-3dd7-ad7e-1aaeebfc4d8c | -4.25333 | -38.5219 | 2026-02-14 03:59:00 | NPP-375D | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5f94a9a4-1f07-3f3d-8f3d-5014da0a1579 | -4.52087 | -38.28696 | 2026-02-14 03:59:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a58b2579-1a17-326e-a4f0-22a1d3ca01cd | -4.517 | -38.28991 | 2026-02-14 03:59:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fbdf548d-838f-36c9-8a85-d5ae9a0b359a | -2.94554 | -39.94937 | 2026-02-14 03:59:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a5aeca85-423c-3e49-bfb1-974102a7dfb5 | -2.94902 | -39.94992 | 2026-02-14 03:59:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f81792f6-b655-3803-b140-8fb66cae7a14 | -11.28623 | -38.23331 | 2026-02-14 04:01:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f1b8d689-c060-3cac-b07f-ae12b3c2f13b | -11.89315 | -45.27835 | 2026-02-14 04:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baf42df3-a337-3ff2-98ff-6309346ec5d3 | -11.02057 | -45.06996 | 2026-02-14 04:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecf57e78-30c2-3d7b-849e-74c212c9061f | -12.06225 | -45.34882 | 2026-02-14 04:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0768e7a1-9fe5-3cac-895c-96102b9ec6a2 | -12.6343 | -48.92049 | 2026-02-14 04:01:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 352b97ee-5157-3798-896e-b86a8a4adca0 | -11.89384 | -45.2745 | 2026-02-14 04:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 416d9801-aa92-39f6-bc44-1a7663c5dbe3 | -11.76681 | -37.986 | 2026-02-14 04:01:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8aacbdd2-fb2a-3572-b1d3-a1d7426c22d1 | -11.10257 | -45.29169 | 2026-02-14 04:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b83b132c-87bd-3575-b036-6bf8919fbe06 | -10.60658 | -44.33261 | 2026-02-14 04:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b820883-c86a-3273-8621-c3160a8d200d | -12.63958 | -48.9212 | 2026-02-14 04:01:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86682ff4-f9f9-3f7d-95df-8ef346117e82 | -18.713 | -43.00853 | 2026-02-14 04:04:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7900951-c56c-3e1c-83f6-c279ff8527ca | -16.94879 | -43.14185 | 2026-02-14 04:04:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be6e9b81-f9b6-35d3-9499-3cd8307bbdf3 | -17.61956 | -46.66433 | 2026-02-14 04:04:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 545679d3-1273-3ceb-a636-cf7a4720a1ce | -19.63646 | -40.64738 | 2026-02-14 04:04:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 79077abf-8d0d-3202-ac35-e8925f486954 | -19.63981 | -40.64796 | 2026-02-14 04:04:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 461c9952-5d9b-3017-b6b1-6a2b455d36f1 | -17.62368 | -46.66516 | 2026-02-14 04:04:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e36c3a21-26bf-31be-b805-b41a98825546 | -15.00014 | -45.14874 | 2026-02-14 04:04:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2dd7ed5-92f2-31ec-b6cf-95ac09954d32 | -17.61543 | -46.6635 | 2026-02-14 04:04:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00f0c955-3fce-3c6e-8651-19c0896ce42d | -19.64038 | -40.64425 | 2026-02-14 04:04:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| fa5d073a-7799-3c57-9e65-9d180d1780ac | -14.19567 | -45.50221 | 2026-02-14 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8d68122-863a-3ca3-95db-e06ab722ea08 | -18.71237 | -43.01236 | 2026-02-14 04:04:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2dea7755-7d12-37df-b1b4-b68a346a5c30 | -18.69375 | -40.01448 | 2026-02-14 04:04:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 25d1872e-04e9-364c-98ba-d0a4c73eef8d | -14.19502 | -45.50589 | 2026-02-14 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3f40228-f2a3-395b-911a-c06c4993c925 | -18.69465 | -40.014 | 2026-02-14 04:04:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a45c7439-f5b6-3e51-9a6a-48d000804289 | -19.64316 | -40.64856 | 2026-02-14 04:04:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| fc8f51e8-08d2-33b3-8321-36e3bc90774b | -14.99411 | -45.13697 | 2026-02-14 04:04:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e58d5f44-8369-3d11-8b43-e49823d90696 | -20.9946 | -41.80289 | 2026-02-14 04:04:00 | NPP-375D | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README2.md)
