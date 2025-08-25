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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13ca7f04-d4fc-36e3-add1-7b6ce8e34620 | -9.1909 | -59.4619 | 2025-08-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7cc4292c-2e40-346d-8016-ee0d2ec05e8a | -10.6128 | -44.3284 | 2025-08-25 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 0ee9288c-6e35-382c-938b-799ce480da4f | -6.782 | -59.6519 | 2025-08-25 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| dc5dbf97-b955-3437-8ed5-b03b1e4747e2 | -8.5758 | -62.6323 | 2025-08-25 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 543b7eba-43d0-319a-a01c-3bed90edc64e | -8.5942 | -62.6505 | 2025-08-25 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| cf74d822-a388-3248-8b7e-95298eec3807 | -9.06 | -65.7344 | 2025-08-25 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 3580dbff-06b1-3a34-a250-e8e5e5345fe8 | -10.5937 | -44.331 | 2025-08-25 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 704d27d9-fecf-3481-ba32-d277d8f9c6f8 | -9.0416 | -65.7163 | 2025-08-25 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 7894077a-ba9d-326b-b6d3-8e691112226a | -9.0971 | -65.7332 | 2025-08-25 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 06b1dcb4-b92a-3fe9-864f-c66ba77bdc05 | -8.8734 | -62.4495 | 2025-08-25 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 008875b8-4648-3483-8969-f1dd2cfabed8 | -7.6326 | -62.7243 | 2025-08-25 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 75b75bca-a287-3446-9eb6-61df2a383e2e | -9.8101 | -64.2642 | 2025-08-25 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 53305acf-0041-399a-8d07-a4657c387df5 | -8.8919 | -62.4487 | 2025-08-25 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c789ac4d-a1aa-38fc-873d-576e75f63308 | -11.6304 | -46.2311 | 2025-08-25 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 123b8ec8-a985-3c08-bce5-5cce404d5489 | -9.1906 | -59.5007 | 2025-08-25 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7a27eee6-5be6-3b22-bd16-bf391482e522 | -8.8733 | -62.4685 | 2025-08-25 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4082d2fe-a5ed-3101-8f9e-300ff641e1ae | -9.0972 | -65.7145 | 2025-08-25 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 9db9ea3e-9fb6-3f1d-bf08-974be16de42a | -8.5943 | -62.6315 | 2025-08-25 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 235.2 |
| a95da6aa-52af-396c-8c93-f5ff864fb6c0 | -8.5944 | -62.6126 | 2025-08-25 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ce6d99db-c92b-3921-9e7d-cdafe1f061fc | -9.0415 | -65.7349 | 2025-08-25 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 80ae1858-236c-329a-941a-d8e0382c9b47 | -11.6495 | -46.2284 | 2025-08-25 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 043b159b-6b57-39fb-8a2c-7c6c1e3e25d4 | -9.1909 | -59.4619 | 2025-08-25 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ec501ec8-2c28-3697-a8c8-3ae32838e3f1 | -3.4439 | -49.051 | 2025-08-25 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e03c99ce-6a56-3af5-b57b-ec72f0c65ddd | -8.8918 | -62.4677 | 2025-08-25 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0470def7-ab48-32ef-86c3-a1245d2b9bb4 | -9.1722 | -59.4629 | 2025-08-25 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 60cc270f-bbfc-3234-9795-9b8e908d83a4 | -6.8229 | -58.956 | 2025-08-25 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 4444e7a5-0c24-3d50-b731-611a40ac7196 | -9.1988 | -60.9274 | 2025-08-25 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ed9eb1ef-c502-36fc-98c7-87435c76cdf3 | -3.4254 | -49.0517 | 2025-08-25 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| feb23ea1-f75d-38e6-82f2-603a4db75cb5 | -8.6314 | -62.631199 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| af0a8734-f38f-340a-824a-69a303f0e39a | -9.2089 | -59.499599 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25e377b7-6487-39a3-8bc8-33b4b291e1a8 | -14.442 | -56.469002 | 2025-08-25 01:03:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d62fe3c-29a5-3156-ac2f-e96a73b641b1 | -9.3173 | -63.4226 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 06a8bf20-d2e9-347c-9c99-4628b98d421f | -6.2901 | -59.990002 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91ab2114-0e8d-3ce2-acba-638fc20087fe | -14.2145 | -58.615299 | 2025-08-25 01:03:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14122172-9a17-3c7b-965a-bb7e3bd2d34b | -8.9018 | -62.458401 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 04702de8-a9ca-3311-a859-7888706d4ec2 | -14.438 | -56.4519 | 2025-08-25 01:03:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 097e1a04-9352-3437-aa00-2ffe7dfa191c | -7.6542 | -63.518799 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 400d5fd4-4e43-344e-bf07-1ec2c96ca247 | -9.1942 | -59.616299 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac4e7103-fcd4-3a9d-ba50-ecf7b6820098 | -9.2001 | -60.7855 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f9eb63a-eb60-320c-a5c7-c0e07c9c98b6 | -8.6105 | -62.582901 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f1daf8b8-04c7-3fbf-9ab5-4003ebf77d16 | -8.9931 | -63.632401 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b3041e6-9e01-3fc8-8c69-777bd72ddc50 | -15.1524 | -59.587299 | 2025-08-25 01:03:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8afc6f0c-eaa5-3bf4-916c-4c4eb7880d55 | -9.0179 | -65.3769 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0b076a6-0dc3-3ade-b649-e14a489148bd | -9.199 | -59.456299 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bb88ea4-5e6f-3bc7-9acc-6c1da3b982b5 | -9.9709 | -60.180698 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac917f85-9365-3703-a3d5-e29b041bbfb8 | -8.9234 | -62.415901 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 583858b7-3eac-36e9-a2ce-cc5e4526c188 | -6.2607 | -59.9967 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2f7d13-c706-3935-a837-64d1e3384080 | -6.8347 | -58.945202 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4f1eafc-f151-337e-b20b-d5745c20f005 | -9.089 | -65.713699 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7acf7c1-d23b-32e4-8592-e46cc5c17387 | -2.9193 | -53.6749 | 2025-08-25 01:03:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2b2f949-8ad1-3ba0-8d3e-46800aace381 | -8.9332 | -62.4137 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c22dab88-5c32-3ecd-a2c4-a8a905df69e0 | -8.6939 | -62.869701 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| afe769da-a0f4-3320-806d-84ef468f8ea9 | -20.3487 | -46.6959 | 2025-08-25 01:03:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b2b7ab7a-4217-3f83-82f7-141638b20952 | -7.6237 | -62.7244 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c6c5a42-0b63-3dac-8024-f537bc28d1c5 | -9.1356 | -60.727402 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f03cf27b-fba9-3501-888d-fcf483e4b5d3 | -8.1272 | -62.863602 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0f01b627-d3c6-3503-9eb5-a62bc99120d4 | -8.8873 | -62.4389 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e92e2d41-2177-3825-979a-65a0a8c77ca1 | -9.006 | -65.369301 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d97425de-fcf9-35f8-a0bb-a03b0da39803 | -10.2898 | -60.5466 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff37830-6bd9-3704-a448-81ddf80e58c2 | -9.2592 | -59.766499 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14c9258c-87e1-32ab-b956-bdc06fb61da4 | -9.5163 | -60.4958 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5d9911b-3be5-3a5e-99ec-79c4bb4116d5 | -6.246 | -60.0228 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb2d010f-f51f-3fe5-8753-6fdd0aaa798a | -8.1288 | -62.870899 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc30fa6-7d4f-354d-a4f6-3294bac73f0b | -9.9694 | -60.173698 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf588d8d-541d-3eca-98b1-0a4d8fc9d94c | -6.6902 | -58.854801 | 2025-08-25 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef0ae43-e99c-380d-94fa-850ce2d34ce1 | -7.1051 | -59.767101 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce111480-debd-3ed7-ac48-1f1efddc3678 | -9.1753 | -60.812901 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f58ba6a-2e6c-3007-b41f-2a3d302f8bfe | -9.1055 | -61.423801 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45877e38-ef10-3c0a-91b7-32c7e6cd10a3 | -8.106 | -62.8606 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1941c03f-94cd-3040-8e51-9952fce1d684 | -9.1615 | -59.4725 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f560ca11-a0d0-3f7c-9f49-f0fe99d34779 | -18.062799 | -51.387001 | 2025-08-25 01:03:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e21e58c5-0d4d-33dc-aee1-861cf40dec94 | -9.2023 | -59.470699 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac60136-5c10-3891-839c-16f3c00f3bd4 | -9.5173 | -60.5466 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8afaf700-56b7-35a9-9ddc-658822102dfe | -7.5512 | -63.846699 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 498fb983-02f1-302b-b10d-317c08deed7e | -7.4301 | -60.6096 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fbb9f6e-31e7-3d9f-bcda-28dcdd9a088f | -7.6525 | -63.5112 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed82ca61-62bc-3c75-8205-aecafd563eed | -9.1648 | -59.487 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb8ea35a-0cdc-3c71-a9ee-a0ec68a64094 | -9.4739 | -57.826599 | 2025-08-25 01:03:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 972fa600-4dcf-311b-8d21-961c01a97447 | -8.2161 | -61.404701 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f0a355f-0eda-3828-b08e-7418ac214939 | -9.2136 | -59.702 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00a82ce2-a428-3050-b02c-c335de6fa353 | -6.2509 | -59.998901 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81e10f0a-77cf-364e-b29c-f596b6f0c849 | -9.1795 | -59.597099 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5e694ba-3355-3c46-b039-642bf838583d | -9.521 | -60.516602 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b50ff316-c4b8-3498-b592-615d938b150c | -6.6884 | -58.846901 | 2025-08-25 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fae28f6a-36c2-3035-9b28-e1efd4d1a134 | -7.0383 | -59.835701 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae348346-c442-364d-8baa-ad2a4d7b99d4 | -9.1469 | -60.732101 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1e977ef-82ec-3185-a844-24b1155991d2 | -9.1768 | -60.819801 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa9f05ed-1b23-3020-a564-6f1db0cb9206 | -9.2067 | -60.907299 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a92af7c4-551f-3aa6-9aeb-c5a8a58ff331 | -22.535999 | -46.791302 | 2025-08-25 01:03:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf618938-c535-3767-b7c2-0a22f5f25117 | -6.2525 | -60.006199 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a3853be-df2c-3e76-8eeb-9efac4af007d | -14.44 | -56.460499 | 2025-08-25 01:03:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3d67ae-459c-3856-81f8-f6d0645df601 | -9.2099 | -60.783199 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11b02422-cfb4-36d3-a83c-3ecf7a0dd4a4 | -8.119 | -62.873001 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fe5dff0d-0618-3326-b2de-9150bfce117a | -9.0967 | -65.7015 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8239bb15-62f8-3eb7-8937-2c012d764204 | -9.1638 | -62.340302 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6301e1a-0213-370a-ae2d-12479a48a19a | -9.155 | -59.4893 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0429e62-e0a4-39ff-9c9a-49d2dab8338d | -6.2623 | -60.003899 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd5b324-159b-37be-a3a8-375fb5ee0874 | -9.2443 | -60.4772 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58063681-4f36-33e8-9e7a-055d20a7a424 | -8.736 | -64.152199 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a677036-589f-35a3-9ece-cc0a25fd6a3b | -8.9983 | -65.380997 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
