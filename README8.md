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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f432fe4d-2c7f-34d7-8799-9e0abd3af8e1 | -5.1217 | -47.5928 | 2026-09-16 01:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8fb3c8c6-8185-3723-b699-67b8fd5c69c5 | -5.1215 | -47.6146 | 2026-09-16 01:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 12200627-1ec2-3a8c-aa37-8b16fecdbb09 | -9.3892 | -60.3215 | 2026-09-16 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 47a929a0-8953-3f33-a0f2-b59366dd45f3 | -5.1624 | -55.9338 | 2026-09-16 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 644ebecc-d047-3b98-a876-f37d81069941 | -15.2821 | -42.8075 | 2026-09-16 01:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 112.5 |
| cf9d8040-3b5a-34a7-8cc9-0c66e4d54a48 | -7.651 | -67.1824 | 2026-09-16 01:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f760ad67-b5df-3c30-b641-75698cf0359f | -8.8399 | -44.894 | 2026-09-16 01:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8f0888fe-765d-36be-8d83-4a7d8a0fc235 | -9.112 | -45.7294 | 2026-09-16 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| ce993a16-dc1c-3213-b07c-e1b0631eba5c | -18.6453 | -50.1845 | 2026-09-16 01:10:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| 5018d484-eca6-3c73-828a-4259025b5fe8 | -8.87 | -44.9 | 2026-09-16 01:15:00 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7da79087-e672-3571-a1ce-aac1479fe296 | -8.84 | -44.89 | 2026-09-16 01:15:00 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 008fefef-ed22-355c-9fe2-2e7723b26bcb | -8.84 | -44.94 | 2026-09-16 01:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4208264a-74a6-328a-a35a-1fd26d18bfc3 | -11.1401 | -40.4748 | 2026-09-16 01:20:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 7f25f662-4f02-357f-8bf6-5ae69e7dee1f | -9.4102 | -62.7113 | 2026-09-16 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 102.3 |
| e538b656-2fc0-31b4-ba3d-2c2f7db80bfd | -9.3893 | -60.3022 | 2026-09-16 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| bf1d26e6-8d6b-3aa1-bc9b-d4c81eef0492 | -9.3892 | -60.3215 | 2026-09-16 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6dc89988-d5b8-3eb4-b74a-aa2d0a81128b | -7.6327 | -67.1644 | 2026-09-16 01:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 9c78de8b-0b06-3862-b532-e0ed1051c37b | -11.9033 | -43.8112 | 2026-09-16 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 0fbd9a0e-eb7d-3e2e-8432-33c3f892db65 | -5.1215 | -47.6146 | 2026-09-16 01:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 158.9 |
| fae49426-bb59-3ae2-9eab-10fbc1777d6b | -5.1217 | -47.5928 | 2026-09-16 01:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| fce18eb8-1883-312f-a3bd-53d02bcb90fc | -8.8588 | -44.8919 | 2026-09-16 01:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 980f563b-232f-3c87-9f42-9189d877aff9 | -8.8585 | -44.9149 | 2026-09-16 01:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 219.2 |
| a9bb5cbe-2f0a-3c0e-9a3d-cddff9b56828 | -9.7136 | -64.9074 | 2026-09-16 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 5fed5868-7a21-3ea1-92be-ac18fc39ba41 | -11.4849 | -45.7965 | 2026-09-16 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 161.6 |
| aa54315e-368c-39e9-885b-b093cfe78712 | -5.144 | -55.9345 | 2026-09-16 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| e806b4de-2f31-3fb5-9a72-9b7ae73df066 | -9.112 | -45.7294 | 2026-09-16 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a9b33db9-1505-3ff3-bde9-8407d4085d00 | -11.4846 | -45.8194 | 2026-09-16 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 9bb9d2ac-f727-35d9-8247-1294f6bb4d01 | -9.0931 | -45.7314 | 2026-09-16 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 808fce57-5b4d-3413-9ab1-4d58037bc66b | -5.7756 | -45.0826 | 2026-09-16 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 71628f9c-5882-3a1e-9953-7c0e01d7e6b1 | -9.7322 | -64.9067 | 2026-09-16 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3eda8948-8ffb-3534-9daf-4f39839580c9 | -8.8396 | -44.917 | 2026-09-16 01:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 97c5bdda-b7d8-3054-8163-57b48c5ed7db | -11.884 | -43.8142 | 2026-09-16 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 921c8e10-ddee-3a1c-bef9-5011e85dd803 | -9.7822 | -46.4876 | 2026-09-16 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 8c3eeb14-2660-3c0c-9ab9-9cc4b927efc6 | -15.4626 | -53.7761 | 2026-09-16 01:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| cba9ce8f-e434-3242-8708-8ecfb5687fd0 | -5.1029 | -47.6157 | 2026-09-16 01:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4553dca5-321b-328d-8861-951d9e9cc95d | -9.8012 | -46.4854 | 2026-09-16 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| caaa55d8-4d64-3412-a52b-0d7167af7656 | -15.2821 | -42.8075 | 2026-09-16 01:20:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 611f3305-e444-3af3-addb-81c80908021b | -5.1624 | -55.9338 | 2026-09-16 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| db5bc8a0-5268-3312-bc08-5ab5852bd30f | -8.8399 | -44.894 | 2026-09-16 01:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3c0664b5-b64a-3da9-a1d3-4ee80aed2a74 | -7.6511 | -67.164 | 2026-09-16 01:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| e630490b-e73d-3bcc-ab51-3414ba487c4f | -7.5476 | -62.3088 | 2026-09-16 01:21:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7c2cf34-f884-3b36-99bc-b0becda2b79f | -9.8089 | -67.542801 | 2026-09-16 01:21:00 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0e293ebe-e999-34cd-85b0-2a50a1ec3827 | -9.7224 | -64.889801 | 2026-09-16 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a20f6803-be0e-398c-96e7-7c8201eb38be | -9.1035 | -65.922699 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5dd7f8-c4ee-3080-9d73-e3b29106f6ad | -9.4069 | -62.708302 | 2026-09-16 01:21:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 683f03dd-5c56-3c35-8ed2-058b0c04d9e5 | -7.5693 | -63.2696 | 2026-09-16 01:21:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d61bc99-acf1-3988-b678-5882a5ad078e | -9.7242 | -64.8974 | 2026-09-16 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3ce7fc5-502a-3f3c-ad47-4a1ff8b3caa6 | -10.0591 | -67.049301 | 2026-09-16 01:21:00 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3b98c4fc-9a14-32b9-bda2-c5920ac5331a | -7.6425 | -67.160698 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37c70f51-0850-3f4d-bee2-ee62a8c90cd1 | -5.1235 | -55.8573 | 2026-09-16 01:21:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daa13930-81d1-379a-b679-cc8624917cac | -9.048 | -65.905403 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58d50db8-39c8-3895-a286-4fb6237862d4 | -7.7999 | -66.899803 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39d1578b-8f8d-379a-8823-d719bd4353e8 | -7.6508 | -67.151604 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65b88f94-7299-3826-8dec-bc492813eaae | -7.6394 | -67.146896 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83e1cfe9-7ce2-3e7b-9781-17970e760e39 | -8.712 | -62.824001 | 2026-09-16 01:21:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bcaa6d73-4e42-3eef-8177-16f2b82504d4 | -15.4364 | -53.73 | 2026-09-16 01:21:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| baa3840d-b0b1-3e5d-8306-3a6f24327c11 | -8.5974 | -64.089302 | 2026-09-16 01:21:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6573b6-94b1-3d41-8e64-b33fd18146b6 | -9.0578 | -65.903099 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7168ea0-3a0b-3203-a311-3a2799ad4a1e | -7.641 | -67.153801 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a1f3bd5-cb4c-39b0-adae-3533e46533a9 | -9.4023 | -62.688801 | 2026-09-16 01:21:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 84276a39-8490-3da8-a26c-c8c7fb728ef8 | -9.0594 | -65.910301 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0e99e9-5086-3687-bf8e-5ba09cdbeb20 | -8.2176 | -64.009201 | 2026-09-16 01:21:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85e25af5-eff4-3829-9f99-a66c283ae7c6 | -9.013 | -60.986698 | 2026-09-16 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a268cc6-8db2-33c3-8686-197bafaa45dd | -5.1412 | -55.887501 | 2026-09-16 01:21:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1777e61d-06ab-3096-87b9-d8304a65cb91 | -11.7985 | -60.433102 | 2026-09-16 01:21:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8c857fce-70a5-37f6-8f84-d6a1a80f58d6 | -9.1345 | -65.832703 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19fd71e8-83e5-3d24-92be-342ec86ae798 | -9.1247 | -65.834999 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c4a8de8-8fc5-32ab-ab0a-a434c25a859d | -7.6523 | -67.158501 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5d45ce-ed51-3387-b5fb-0f03e375f528 | -8.7074 | -62.804501 | 2026-09-16 01:21:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6cea0c3-2512-316b-99e1-ff6849015af6 | -7.6173 | -67.231598 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83dee94c-c50f-3830-8138-6ce71ae07671 | -9.1329 | -65.8256 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6780463-b5f1-303f-83d8-2d06c68e3757 | -5.122 | -55.8923 | 2026-09-16 01:21:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af405dc1-d999-3aaf-b57a-b9493a27bb6e | -8.644 | -66.576599 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dd859e2-33ff-3fe1-b185-ea7c78046bf5 | -9.4143 | -62.696201 | 2026-09-16 01:21:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0ee0437-8e3a-3be3-b2ea-3d10e4383f47 | -7.6091 | -67.2407 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba3dbe10-a439-3c4b-b091-b2df815396e9 | -9.0937 | -65.925003 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d07448f3-caa7-3e02-9576-677130a47bf2 | -9.3859 | -60.277302 | 2026-09-16 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14d92e7f-8716-3303-9fac-9ed5bebc3ee0 | -9.0496 | -65.912598 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea3e6942-705f-397c-b1f1-7ef284db4420 | -8.8725 | -62.501099 | 2026-09-16 01:21:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f26de204-4f90-3df0-8944-66e03a638173 | -9.4046 | -62.698502 | 2026-09-16 01:21:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cb418e46-e397-3bc2-bfee-90edf568aa91 | -9.0365 | -65.900497 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 703b128d-a846-3ed3-8a48-2e9bc7dbb708 | -9.0775 | -60.997398 | 2026-09-16 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db46ad72-2aef-354d-a0a0-bfc0e3ade11e | -9.5029 | -64.698898 | 2026-09-16 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8d1aa3e-a560-3642-86ed-aa5e9c663b52 | -7.6075 | -67.233803 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59d4a563-095e-3bd1-a780-171c60cfbf78 | -9.0161 | -60.999199 | 2026-09-16 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56a75153-301b-317c-afa4-4b5f29174593 | -9.412 | -62.686501 | 2026-09-16 01:21:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7df63158-7783-3f38-9ddf-7ab63a77ef55 | -9.3893 | -60.291199 | 2026-09-16 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fde78d58-99c8-3eb0-9d2a-d7492c5f5a17 | -7.606 | -67.226898 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8504722e-11bf-32c0-bb27-07dab63a7475 | -8.8213 | -62.459599 | 2026-09-16 01:21:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 996dd0de-5aa6-3e1b-ae70-1663bf6a614f | -9.1545 | -68.210403 | 2026-09-16 01:21:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb3968ac-2739-3199-836b-d358e7e35942 | -9.3796 | -60.293598 | 2026-09-16 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25c59915-273f-3c42-b769-d083e1f61791 | -7.6492 | -67.144699 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20424653-7a97-3ffb-9e23-05630ca9f039 | -9.1231 | -65.827797 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7391ca06-d9e5-3f55-b378-20d9a65db263 | -10.6521 | -58.739201 | 2026-09-16 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 066e7d60-22b8-3f11-bcac-de4791543008 | -11.8016 | -60.445599 | 2026-09-16 01:21:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b8f7863d-f8f9-3457-aa3e-bd2aba0644c5 | -9.061 | -65.917397 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ec6809f-a319-3fbb-9fdc-2ceb98282787 | -8.6544 | -66.486099 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c23aef1-09f6-3ca8-a065-11a1cc6c173d | -7.6189 | -67.238503 | 2026-09-16 01:21:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac2686a3-697f-3c44-b74b-42746b73487b | -9.1002 | -65.908401 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c269b9e1-0a26-33d9-948e-3c6cc9701bda | -8.6456 | -66.583504 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
