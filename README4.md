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
| ebb33b16-7946-3f69-a319-888d263c0ae8 | -4.3197 | -48.0908 | 2025-09-24 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 1dfecd2b-74a3-33cc-919a-5bbb52f84fe9 | -7.6399 | -45.9907 | 2025-09-24 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 915c2fa0-838a-3199-9346-c63d2e7b3fae | -5.2448 | -43.7225 | 2025-09-24 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 9a315f73-6d72-3af1-9145-228e29d668c7 | -14.3067 | -41.8364 | 2025-09-24 02:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 1ec93d61-a31e-383c-b196-15dfbff3dfcd | -15.7835 | -59.4853 | 2025-09-24 02:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 6936f62c-f8a7-3fe5-8f5a-9d00374173d7 | -4.3012 | -48.0917 | 2025-09-24 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d9edaa0e-b3f5-3171-bef1-088da19cf1b1 | -7.6587 | -45.9889 | 2025-09-24 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 90cde3d1-65a6-3451-b72f-adc357a16202 | -7.6584 | -46.0114 | 2025-09-24 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 5e922d22-0c3b-3c2e-aa7f-9409e4419ef8 | -7.6396 | -46.0131 | 2025-09-24 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 2052d106-731a-3b5d-a520-27462b2274b1 | -5.6361 | -43.9258 | 2025-09-24 02:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 565d506b-dc4b-3bbf-8579-e5cd5b373097 | -4.3197 | -48.0908 | 2025-09-24 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 85cb4572-8a50-3106-b9cc-4b3c959f4d4c | -5.7605 | -42.6088 | 2025-09-24 03:00:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 94ea344d-41a6-3e44-a463-8e46fdc24210 | -4.3197 | -48.0908 | 2025-09-24 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 30f4ad9e-ebed-3e59-b4f3-deea3cf3b819 | -5.7607 | -42.5852 | 2025-09-24 03:00:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| c1f453cc-5eba-3848-81b0-3a8a9087ad0a | -5.2448 | -43.7225 | 2025-09-24 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0cd411c7-cb52-3705-95ae-ca447078d3ad | -5.7795 | -42.5837 | 2025-09-24 03:00:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 8f971793-e5a0-3983-ba66-4bcef33f19ee | -5.7793 | -42.6073 | 2025-09-24 03:00:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| f1011999-099a-3d0b-a4c7-cce886f486ad | -5.6361 | -43.9258 | 2025-09-24 03:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 71b81872-b81e-306b-8be5-347b7318a7b1 | -7.7689 | -46.2031 | 2025-09-24 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 9f1bb9d5-6e65-3130-a545-96953bc3de6f | -7.6399 | -45.9907 | 2025-09-24 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| fba9346b-61ab-3410-9419-294742e93502 | -5.2448 | -43.7225 | 2025-09-24 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f28a39af-e2bb-3544-8c8b-61197704e629 | -15.7835 | -59.4853 | 2025-09-24 03:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 975d53bb-d64f-3d06-9a0f-ffed1e7eded3 | -4.3197 | -48.0908 | 2025-09-24 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| bf24fdf7-84f5-3643-b6b2-250ad3035e14 | -7.6396 | -46.0131 | 2025-09-24 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ab34b839-7e31-303f-a0d5-871a06cf30bb | -6.19971 | -37.6245 | 2025-09-24 03:10:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30807c7d-0ac9-31d5-954b-39f2820c49e8 | -3.32213 | -40.00644 | 2025-09-24 03:10:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c2d74b28-93b1-31cb-8ffd-64ef613dd70b | -6.20041 | -37.62054 | 2025-09-24 03:10:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5a24af1c-affd-3e93-8ead-97d844bf0398 | -5.4968 | -39.17268 | 2025-09-24 03:10:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9ca6a3af-045b-3352-8249-9bf43edb36ba | -7.21067 | -39.45472 | 2025-09-24 03:10:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ecec1a91-22c5-327e-923f-6a7f313dd807 | -6.20614 | -37.62155 | 2025-09-24 03:10:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| acc05119-fd57-351d-a373-3fcefbddfe49 | -5.49298 | -39.16862 | 2025-09-24 03:10:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 9e7fbbb0-2c79-3bde-b121-2ded98956a27 | -5.49771 | -39.16752 | 2025-09-24 03:10:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 488fbd81-2463-30dc-a0e8-b8438f713f4d | -2.91594 | -40.38774 | 2025-09-24 03:10:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2a00a3c0-4e25-34fe-89d8-83290b832eb3 | -6.20544 | -37.62553 | 2025-09-24 03:10:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89a01afd-e785-3326-b52d-484ea73a6e35 | -3.32144 | -40.00727 | 2025-09-24 03:10:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 04656148-5dd3-3d17-a3a5-c031f87eb8d9 | -5.4904 | -39.17167 | 2025-09-24 03:10:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a86ef69b-08a4-30d3-8670-f5b98aea0488 | -11.92669 | -38.33418 | 2025-09-24 03:13:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b595f75-d8da-302f-87ac-f4f1cc8dd29c | -11.93144 | -38.3315 | 2025-09-24 03:13:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 44e393f8-76f3-3a12-aec0-bd2050c0c35d | -8.1534 | -35.9665 | 2025-09-24 03:13:00 | NOAA-21 | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5992cb70-5f68-3387-a6a5-c0570559b192 | -9.48308 | -40.35765 | 2025-09-24 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 010988af-1ab3-3c24-a0ec-9e24e14cd8b9 | -11.93075 | -38.33511 | 2025-09-24 03:13:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d91d6a0b-9979-3589-8844-21aff28f4798 | -11.9274 | -38.33059 | 2025-09-24 03:13:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d843d63b-6910-3afd-8926-a0c137932439 | -9.48353 | -40.35963 | 2025-09-24 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92ff573b-0952-3aac-8211-2e55e2660c06 | -11.93213 | -38.33524 | 2025-09-24 03:13:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 22a8bdf1-e5e9-37b5-b93c-0b99b3ab377e | -9.48461 | -40.35423 | 2025-09-24 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4af4f6bc-2a00-3d26-8109-9a9ff8c47e40 | -11.92532 | -38.33406 | 2025-09-24 03:13:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c43070fe-a3ee-3c1a-836e-06cf7024b2e0 | -14.30116 | -41.84097 | 2025-09-24 03:15:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 88a0be60-83de-30fc-9330-99cb1e741d9f | -14.2948 | -41.83918 | 2025-09-24 03:15:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| ac61a4fb-4841-3614-88a3-f0b04bfc8ec4 | -14.67531 | -42.48034 | 2025-09-24 03:15:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| bde4be84-fea3-3f8a-9e53-3c9d72ce442f | -14.68197 | -42.4817 | 2025-09-24 03:15:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 60d7d617-da18-3469-8ff8-36a499c14c41 | -19.753 | -42.2791 | 2025-09-24 03:15:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 79f84dbf-c439-36f6-9b34-ad8ed5a74557 | -14.29243 | -41.85025 | 2025-09-24 03:15:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 4202b2ff-6ae9-3373-80dd-94307ac8e3ad | -13.81353 | -43.22871 | 2025-09-24 03:15:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c67ef95b-1d61-36a3-b144-d0ba033334b8 | -14.29999 | -41.84644 | 2025-09-24 03:15:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 159891c9-12e0-34be-be2a-6c801630e11c | -14.28844 | -41.83742 | 2025-09-24 03:15:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 88ab1594-e8d4-3b0c-9d2d-43a746e4f4c9 | -16.48153 | -42.63342 | 2025-09-24 03:15:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13c06626-87a8-3a5a-904c-a97e0b7f55c6 | -14.29363 | -41.84465 | 2025-09-24 03:15:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 1345057e-8f4a-3bd2-b9cc-ed30d71bfb84 | -13.81786 | -43.23039 | 2025-09-24 03:15:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e06c489c-3ea4-34e2-94d5-f7c8baf846a9 | -14.68073 | -42.48732 | 2025-09-24 03:15:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9da71cd9-e028-3967-bb1c-8dc44e199bec | -14.28727 | -41.84286 | 2025-09-24 03:15:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a2a9a8da-3277-3f8a-9f1b-72dbaa5a5650 | -4.3197 | -48.0908 | 2025-09-24 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 63509e9f-3c48-3904-acd4-e1b8a6db37dd | -4.3012 | -48.0917 | 2025-09-24 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4eba0d28-e1a9-3ede-889a-e25a792d3f7d | -7.7689 | -46.2031 | 2025-09-24 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| fd5481f9-27f1-3158-a14c-d2dd2d367a6a | -6.4129 | -43.0958 | 2025-09-24 03:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 8f42a8be-564a-3803-9875-e1c3327a4488 | -4.3012 | -48.0917 | 2025-09-24 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 61352c09-9300-3014-bd70-997da73c35f1 | -4.3197 | -48.0908 | 2025-09-24 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a3e91795-4b2f-3417-a82a-426db2962573 | -5.6393 | -45.7239 | 2025-09-24 03:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 854d0fbd-d05d-302f-9d57-03ba2d43b514 | -6.4317 | -43.0942 | 2025-09-24 03:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| dca0abc5-922c-3110-8a1f-de659f7df88b | -15.7835 | -59.4853 | 2025-09-24 03:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8c0e1fc1-cb82-3a5e-9cc5-455db63bf0a0 | -14.3067 | -41.8364 | 2025-09-24 03:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 8a92a55e-75a2-3c39-ac85-1cbcacc0616c | -6.4129 | -43.0958 | 2025-09-24 03:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 19a56c02-0116-3443-b63e-73850e110920 | -6.4809 | -43.7894 | 2025-09-24 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d452c3e4-a2c4-3c28-876a-410349e1a40f | -6.4317 | -43.0942 | 2025-09-24 03:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 476560f1-7258-3cab-9e28-0095b766c479 | -15.7835 | -59.4853 | 2025-09-24 03:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 03c10292-facb-379c-968a-08abca791fe1 | -4.3196 | -48.1125 | 2025-09-24 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 2f4e4225-8068-38c4-95fa-f936d6a19667 | -4.3197 | -48.0908 | 2025-09-24 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 531a443b-70ec-393a-811d-7e14e5b6ebb0 | -7.7689 | -46.2031 | 2025-09-24 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| dc4546a2-be57-3fea-bee2-82732b85e830 | -14.2871 | -41.8405 | 2025-09-24 03:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 140.5 |
| 3dad8bfb-0d2c-3d34-98de-b7b8b5dfc8a7 | -14.3067 | -41.8364 | 2025-09-24 03:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 129.6 |
| 76025f2a-c54f-3705-b584-2770459deffe | -2.42617 | -47.15926 | 2025-09-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaf17684-5ef1-3f3b-8149-2cb9045362d6 | -0.90664 | -47.54686 | 2025-09-24 03:57:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 129f74a8-de1c-319d-bc6d-cabad1ff2c39 | -2.42571 | -47.16214 | 2025-09-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ded7fed1-ca8e-3f19-8e36-35e98e3f8c7c | -2.87454 | -40.44018 | 2025-09-24 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3d3fe9df-4553-377a-9349-74783f76c60f | -2.4271 | -47.15346 | 2025-09-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3e42a29-00a0-34f5-82f7-b6bbfdc3ea9c | -3.96768 | -38.51257 | 2025-09-24 03:57:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7cf2cfa8-5bd5-3d34-b7d9-daf7cb5ee45f | 0.93803 | -51.21027 | 2025-09-24 03:57:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4847d792-cadf-3be7-b7f8-15a8940b4bb2 | -2.90999 | -40.39093 | 2025-09-24 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 343d7acb-61d4-36f1-aa04-4c15eac975dc | -3.31757 | -40.00752 | 2025-09-24 03:57:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5973e0fd-1500-381e-8b2b-7792048193b2 | -2.91335 | -40.39145 | 2025-09-24 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6257a3d5-0d98-3565-b57e-6e61fd26c614 | -3.96713 | -38.51605 | 2025-09-24 03:57:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f28fedcb-824b-3fca-8c3b-e4ff4efcf05e | -3.16476 | -41.64932 | 2025-09-24 03:57:00 | NOAA-20 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8fb2963c-1416-3848-b861-abaa924349a5 | -0.90716 | -47.54363 | 2025-09-24 03:57:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31137fc5-acb8-32a9-912d-541ce4162406 | 0.93707 | -51.2041 | 2025-09-24 03:57:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 206548ef-bb58-302f-8984-5eb2771a5824 | -2.91392 | -40.38789 | 2025-09-24 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc3b6ff1-5861-3046-b930-c04a2f804ed0 | -3.302 | -42.17152 | 2025-09-24 03:57:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5b45e0ef-87ee-3427-b439-3e2123894f91 | -2.2499 | -47.88531 | 2025-09-24 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bbdfdba-a307-3086-8940-bf33bd18a9bf | 0.94388 | -51.203 | 2025-09-24 03:57:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e498dbda-7698-343b-8263-de02df274a33 | -3.30558 | -42.1721 | 2025-09-24 03:57:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 3d978167-12cc-3920-9bf7-62c8258aac70 | -2.42664 | -47.15637 | 2025-09-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b901b204-1ad8-3037-82c1-403ea7ec8ddb | -14.2871 | -41.8405 | 2025-09-24 04:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 172.1 |


[Clique aqui para ver as próximas entradas](README5.md)
