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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4cedca6-6265-384a-b38c-7bda268aadff | -7.02234 | -59.56239 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10277668-ca38-37e1-8113-054d2f3b4cdb | -8.69993 | -62.89864 | 2026-08-23 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fded54df-1e29-3e7b-968f-441bf6a0903e | -6.85831 | -59.02689 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3cc86b5-dbf7-31aa-bdcc-0c36f54bb750 | -9.16283 | -59.46479 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 563561d4-61d6-36cc-aa3e-67fa928fb651 | -9.43247 | -51.60241 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae35f85a-b3e5-383c-871a-58a1bb8555cf | -8.92343 | -60.71893 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c03c9d22-03d6-306d-90db-c8ded6c0d036 | -6.79257 | -59.66375 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02ce8596-69e2-35ff-b79b-c04c8c85f3d8 | -8.68588 | -54.74621 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e29ae33f-3571-3525-ae87-eebda7d00160 | -7.02069 | -59.54751 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 370c42a1-b00b-3a25-bcb5-30e440130426 | -9.04701 | -50.88164 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e13d841-59cf-3a31-9db2-af815673f67b | -6.76156 | -58.67577 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0111ac77-efac-3ac8-87d8-74e1ef180e7c | -6.95553 | -59.07141 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31f62072-3df6-3ce8-b336-3424411b455d | -6.79955 | -59.42422 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32049fe0-98bd-3699-a898-5de446737573 | -9.45554 | -56.90842 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c29512f-8073-3cfa-9fc6-d3f881813e9a | -6.19375 | -53.53163 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9e23a3d-de13-30d2-aaf1-c3996f4c79e2 | -8.89289 | -60.54413 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14827ae6-1177-39a6-8d61-f5b956d4cf99 | -7.8469 | -56.57355 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0528e2d-9ac5-3aa7-8a0e-dcab9d2097fc | -9.06785 | -60.42963 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5271ac08-b788-3db6-90f2-c81f5610b93e | -6.07358 | -44.89859 | 2026-08-23 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ce71b8c-b720-3cf9-be6d-86bbef8d7803 | -5.8599 | -55.71732 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9326a4d8-f1fb-37dd-9e1b-0d46440f21be | -8.99144 | -50.76477 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da6a0b68-aa0e-306f-a71c-b1466b2a5d66 | -6.76162 | -58.6586 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbbba2e5-5d61-31b8-ac88-4aea2287f3e5 | -9.19322 | -59.44999 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2b88bcae-4e72-3457-af2b-d0ac0ed91e23 | -8.99106 | -50.75699 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e96599bf-3217-36f7-98c5-9a8b80c72563 | -11.16205 | -54.01741 | 2026-08-23 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c92f1c5d-cbd1-3b18-b426-6c989ae174f4 | -8.92624 | -60.72756 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c7dcfad-0992-31a0-8ae5-ac035f12551b | -8.54692 | -54.78811 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7b52f15-3656-3e5e-abfd-5d945732c7d6 | -9.45273 | -56.90422 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cc2b4bf-97cb-31d1-8d96-0eb34e52e89b | -9.50536 | -60.50154 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec5aa79-38a3-347b-8b0a-d0bb4b021625 | -6.74785 | -58.67083 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5a9a2fa-e5da-3321-a7f0-38f8b3813c25 | -6.80413 | -59.42147 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eef227a-6301-3c0e-be9e-61253d2ecda5 | -9.42911 | -60.48512 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4180363a-8be7-308d-b6cf-d691f31dc268 | -8.52315 | -55.34397 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b0a09b49-da42-3e13-b30b-e6db4085ed3f | -6.37428 | -54.94912 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7dbd75cc-0e53-3e53-9617-2542f0c19bc1 | -6.82252 | -59.95634 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 149a4b3a-d4d1-304d-8c7c-8f174c9347c6 | -6.80367 | -58.65873 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14c13d6f-9efb-359d-b6c2-3073cc057b5a | -7.1077 | -59.77651 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed511df9-a3bc-39b9-8dbd-10153f03be84 | -6.38091 | -54.97158 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9edd5658-a238-3472-9ec2-712a32078753 | -6.43104 | -54.9546 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90f86be9-c756-3407-b774-c2a138b23393 | -9.51078 | -60.49482 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cb39ec6-26a0-3aa8-9ac7-759fa48880ef | -6.57037 | -58.59039 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f5e0a95-f06e-3930-8f2c-fa1d408316f0 | -6.75627 | -58.66735 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10d7a4bc-e98c-3c05-9316-b4a68b542442 | -9.40435 | -65.94044 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 165627a9-fcbf-34c8-997e-9797d05681f2 | -6.7639 | -58.66863 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bb458be-b8f7-3a9a-9354-83d2a1f3d8a4 | -9.21219 | -59.7628 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17229653-2fa5-3bfd-9df9-5d5af21a8c73 | -7.43357 | -59.79858 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c13d4daa-d26d-3753-afdd-c51dea87f815 | -8.52259 | -55.34745 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a502dbe8-8ad5-3a12-bfc1-8297582d380b | -6.79097 | -59.42635 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6daf8384-5c5d-306b-8f08-e47dda6a277e | -7.41416 | -60.00799 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84bc2206-0960-3f15-a566-e24b4d68379d | -9.17551 | -58.33095 | 2026-08-23 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f50e8bcf-0609-3411-a879-8a6a2bdb53bf | -6.07406 | -44.89516 | 2026-08-23 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f106c973-b97e-32a2-bba4-fbb58a7bb537 | -10.83739 | -50.96698 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0978fb4e-153f-39ac-b975-a8acb135e548 | -8.9622 | -50.75092 | 2026-08-23 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d266d5b-1339-3de7-b712-7f98e1d5b13c | -6.69092 | -58.7295 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f15c147a-beed-35ac-85cb-ca5689ef4958 | -5.76616 | -57.57319 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b43b43ac-ccd2-334d-a067-9436eec3de1b | -8.6324 | -54.74125 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98528ec0-8854-37af-aa30-48210b0bcef8 | -10.37992 | -50.41492 | 2026-08-23 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bd300999-89e8-348f-9e9b-8d1b10844d4f | -6.94383 | -59.06944 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74d0698f-e4c7-3cd4-b7b4-a4efe3bb27ad | -11.27707 | -50.74157 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e95027-67ae-303b-aadd-aae54475e9b4 | -8.53812 | -54.82232 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b7e471a-b448-3fe6-bb89-47d759389cfb | -9.59345 | -60.50576 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8444b5d-1b93-3637-b0d2-776b4afcd181 | -6.81633 | -44.81372 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7696a916-4f7c-3de9-adb1-b3486da72c95 | -12.56348 | -47.93192 | 2026-08-23 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2820167a-6c92-3d07-949b-3c09bd625416 | -10.93775 | -49.6045 | 2026-08-23 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 079209ce-4daa-36f7-90b3-c993c7630c36 | -6.76159 | -58.68281 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f3a9184-8056-3058-b6ab-692b7c56dcb1 | -6.80604 | -58.64462 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d37de928-e649-3220-aeee-3de0ca0d9b5c | -6.78161 | -59.75466 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c2b5acd-87e2-361c-90e7-1224085ae909 | -6.76683 | -59.44734 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b535f35-f063-3333-98df-ba1541e18acf | -6.52345 | -51.44779 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9eeda823-e45a-3a9a-9aa4-afef4335b561 | -6.79525 | -58.66214 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e40f9ba-8b3c-31d3-9031-e3bc8cd5e18d | -6.12578 | -59.92246 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0541ff2b-4ba0-3c43-a5f9-656bc368b5e3 | -8.55413 | -54.8498 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 413c2c5f-aa8f-32e4-8a64-b5ec99afc8b8 | -6.69476 | -58.73012 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8c87244-9285-3d89-858e-9d73af218605 | -9.15152 | -59.55387 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1a8b50d-20a1-3cfa-a072-4384b9ea343f | -9.79816 | -46.62049 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec193df1-b96d-321a-aa4c-922bf4e9a190 | -6.86526 | -59.03318 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19a840d9-503f-3d18-9669-a7989546de6c | -6.75994 | -58.68523 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7a2ee56-782b-3e3a-b5de-bd4ba2138e83 | -6.92284 | -59.43497 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b246b1d2-1c66-3903-9afa-bcdd1ddc089c | -6.77143 | -59.4445 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff2dda64-9a27-3743-ae09-6d51faee8b7a | -8.91783 | -60.72606 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f50480f7-4b3f-3435-a901-28e25376823e | -7.0201 | -59.55105 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b68fa213-99db-39cc-a785-f0172198d84e | -8.5271 | -54.82768 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 307482df-a008-313f-952a-cb0222f5617c | -6.82849 | -59.67395 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ab28100-3f0a-303d-83e6-4599f55f0833 | -6.38146 | -54.96811 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 541bb229-f3f7-3dd2-aac6-fd55485dace9 | -6.25839 | -55.41871 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ac8b26b-cc03-31da-9bd1-edeb05ce6ec2 | -7.48223 | -55.33031 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66c49572-3fef-3326-861a-49c7bdf8fc5f | -9.21248 | -60.90302 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23346933-6596-3eb1-b86c-e74c5bdc950a | -9.11479 | -60.34631 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deee48fa-d6dc-3174-8559-47858f64e98d | -8.92412 | -60.71504 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87abcdca-eff9-35f5-80b6-25832bbaec1b | -6.82038 | -59.6725 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dd57d3c-c6ea-3459-a16b-d6ffd0a19e7b | -9.03804 | -60.45508 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93aa56c4-83c2-36ec-8dbb-3bffe4848055 | -8.92791 | -48.54174 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e925733b-b843-370d-974d-fe64cbe777bd | -8.40185 | -62.6928 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68d02e18-7526-34a1-be8c-5b09324974e0 | -9.18549 | -59.44865 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 388d4b47-848b-33c3-b712-cef089e02c43 | -10.87585 | -50.22398 | 2026-08-23 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd1a79d7-50ec-321e-8f19-8bca6b2c8c3b | -9.96691 | -54.9365 | 2026-08-23 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18159a73-d600-3f99-a9af-af9226a71cd7 | -9.04837 | -65.45288 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d872527-da77-33a2-b9d6-28651720ae25 | -6.23032 | -55.48676 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea03cb19-f332-32e2-9ce5-584fc120a86d | -11.2062 | -55.04555 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73e0ed1b-184c-3156-b70e-41f54f70b1a6 | -8.46115 | -46.99281 | 2026-08-23 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README41.md)
