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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b7f4908-ab57-3c87-8732-16b8a6a5fb1e | -9.1964 | -60.76459 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f650f16a-07e6-3788-ae55-3fbd4e32fb51 | -9.80186 | -46.42489 | 2025-08-24 04:59:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e67149d-1ef3-3ac9-b8d6-4ae6c717e0e7 | -7.54824 | -63.85666 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab2e1031-0ad3-3ef8-b968-a789c096b35d | -7.73025 | -67.06645 | 2025-08-24 04:59:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abca85e4-aa04-354c-a047-79a3dadec09c | -9.20789 | -60.80067 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cda93f28-e651-32ef-9e08-1857e9ef371e | -9.15912 | -59.47393 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6f06e8fd-4eb2-3cbc-a275-44cc00086d70 | -11.05506 | -44.61353 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ada48de-ac94-3a57-abec-686a0a4d246a | -11.31907 | -47.85857 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5e4def49-f805-3a3a-aa5c-fc79377fda11 | -8.90191 | -47.33172 | 2025-08-24 04:59:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b544117-511d-3cb4-8fbf-d2d064c4a799 | -9.15068 | -59.46482 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9d8a19dd-e4c1-3ac0-ab6a-aebaefb8cee9 | -6.57171 | -59.86774 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9f1dc51-d072-33f1-8f4c-672784d22673 | -8.05876 | -45.00286 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30e95bcd-4310-3215-8041-d84fd0ceeb88 | -9.15655 | -59.50296 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ee439b2-a0e7-368f-a34d-a6c65aef8d12 | -11.05587 | -44.61164 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de4fa1fc-1d68-32a7-bc3b-638c0239d6dc | -6.74903 | -62.86549 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8988c4d0-afa9-3952-90fb-9effeca90570 | -9.15326 | -59.44949 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f30a0d6f-79d9-3db0-8edd-b99991eb00a6 | -9.16483 | -59.47787 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a2a42568-7bc2-346b-b1d3-53788dd5102e | -6.38145 | -62.9066 | 2025-08-24 04:59:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9528bf1-d6a8-3aab-bfaa-034314f99f7b | -9.16883 | -59.46509 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cd2e5119-ace0-3f15-93f7-3fd87f2e5bcf | -8.36841 | -49.30105 | 2025-08-24 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d2019b1-8150-3b22-bff5-772b00b0ca07 | -9.23799 | -60.47735 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e42b8e0-d065-35fc-a2d1-1f8cae832359 | -7.44189 | -60.62994 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e137b376-9ae5-3800-ba9e-688f1793faf9 | -7.55914 | -63.85872 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae776541-f94e-369c-8494-2f8de3c4c5db | -10.5394 | -47.14483 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f1e0e4f-b74f-3bd3-b6b6-ac85c80981e1 | -8.13545 | -62.86489 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4729193e-a8df-3526-a5dc-79dd6cf3c5fb | -8.13905 | -62.86133 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9288f210-6f90-3252-bad4-0de9ebfb8c9d | -9.20143 | -60.7867 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b3f0beb4-3144-3e1b-af79-202a594a4cfd | -8.90764 | -62.44455 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb58a7b1-d865-3d10-8c7d-d3d077d96c45 | -11.10644 | -44.77169 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1397c9c4-d690-3185-8ed9-e814f059f613 | -8.6088 | -62.59593 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f53d70f2-859c-3cdb-bd5f-e63b968b53b0 | -11.33324 | -47.86038 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b0f49db-2503-3199-a12a-1e3362a8afc8 | -9.80145 | -46.42798 | 2025-08-24 04:59:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66a228b3-38f2-3d37-9d5e-72843f5ed09f | -9.14045 | -60.77277 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2497c09d-2cf0-3dc5-9f05-1f50a730e539 | -9.15119 | -59.47255 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 293415a1-85b2-3310-93ee-7736d0382ed1 | -9.15862 | -59.4662 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 95b6f9f9-f409-3538-8c5d-9909d6ace01c | -9.19568 | -60.7687 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d65d8783-fa25-3edd-be80-4d839eb64596 | -10.57578 | -47.13389 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c524b8b-274f-3c50-acae-784da3e69686 | -8.05968 | -44.99599 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76561eb6-cf56-35d9-b99a-0fc0bac92d89 | -9.19413 | -59.65176 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fec1f12-62c7-39c0-9b45-2bf8e808e29c | -7.96929 | -63.07671 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 630f0860-d5e9-35bf-a4e7-4d6f9d05818f | -8.13743 | -62.87019 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e15e171-d3e7-3f5f-a0e7-b5b7eb0f8b43 | -6.92908 | -62.90783 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f4c7b5e-cad0-36f4-9e7d-6083bcee15e6 | -9.17684 | -59.65623 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 142c6832-f592-3e0d-946c-52adbb87ce96 | -9.7407 | -54.93129 | 2025-08-24 04:59:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc4719f2-8672-3103-a4fd-00dc8f2d2ac0 | -8.6343 | -62.62369 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 62adc71b-7e0f-3ecd-8a42-666aeabb545d | -11.11078 | -44.78167 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d0ca69e-a7fa-3337-b319-e15d18d3fead | -9.16655 | -59.4676 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0358b488-b3e3-39a4-ac92-bc861108a04c | -9.17137 | -59.46318 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 992e2f00-9ee2-3c73-a173-3e3b5c363870 | -8.92413 | -62.43637 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 823db4e5-f585-3c27-94df-8551ebf7b156 | -8.13999 | -62.8688 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70f6c09c-729a-3908-9e9f-14091445bca9 | -9.16001 | -59.4688 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 36c7600e-1da0-3a2a-804a-cc3a977d8486 | -8.89891 | -62.43739 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 696389b2-4723-327e-b832-3c27e347ad65 | -9.02503 | -59.01821 | 2025-08-24 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85fc5350-21b4-3ba0-a90c-d80227f6422f | -8.60388 | -62.59503 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a27b0745-c945-3f2d-8fb4-38b8951f27c3 | -9.1885 | -59.61237 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca696bd0-f867-347d-b8c4-2ddd1d9a855d | -11.11073 | -44.78436 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52e92aff-249e-3555-b420-61a72b833488 | -6.93179 | -62.89223 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb039034-a4da-3eff-8bf2-bbb56a68de95 | -9.15552 | -59.49454 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9b6d5498-78f8-36a0-a564-442b14ef8835 | -10.29711 | -46.74603 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9898877b-ecfb-30b3-9eec-7dff48324d65 | -10.64738 | -51.62199 | 2025-08-24 04:59:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00d515d6-50cd-3619-9418-9cfc52f2b643 | -9.17051 | -59.46831 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a04e6df2-87c0-37be-86f0-6414dccb0d70 | -9.15603 | -59.48167 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 34b433f4-9bd1-3c59-9978-280fe161f48b | -8.59897 | -63.29254 | 2025-08-24 04:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef288164-2b0e-3b75-a423-1f7b5a561e6a | -8.89503 | -62.43111 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7c62a67-762b-3e4f-9587-1844a197331e | -8.90666 | -62.42214 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 14fc6fcd-688c-3c39-a85b-d48c0873a06b | -9.19561 | -59.61896 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e41e19d5-7506-3b37-aa4b-1a9b45cbff66 | -9.25001 | -60.92272 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26644ead-2ddf-3c31-9fc3-8de60b832eba | -7.30073 | -59.6272 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76d761c9-2f94-3b02-9a36-cdcb7d6f4773 | -6.58313 | -59.87768 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2343acff-a355-30e3-af6d-cf97a1bbeefb | -11.05456 | -44.61763 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f3c4d9c-6ac7-3a78-8d58-de573afe8bde | -9.1568 | -59.51066 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c8b8d13-c807-3222-b3fa-20ec5f1b66fb | -7.06783 | -55.5898 | 2025-08-24 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a12d4c8f-1758-31d1-befe-b409485441d2 | -9.15476 | -59.45214 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 104b47d2-4c0a-388b-856f-3123a035a9bc | -10.80866 | -46.38907 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 146cc481-b243-344f-84a4-0d025697f40f | -9.74347 | -54.93528 | 2025-08-24 04:59:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50767887-4c10-31f6-bd38-cb8bfb309168 | -8.18107 | -45.08789 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d872956-7d68-3cd7-afd9-38b056fccd3e | -8.14755 | -62.87207 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5296f700-8972-3f51-9e3b-01e92a3a27d1 | -8.91249 | -62.44544 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7835652-8ed7-305d-9598-f39e91bac8ce | -7.74985 | -47.35726 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f7d3614-5399-3682-b548-082bf207bb75 | -9.14844 | -59.45392 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d48f66e-aa7a-33b6-afc0-482ddbce77e5 | -11.28108 | -44.97522 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2637cfc-5543-3715-8d42-5e4f8f93ad12 | -9.15119 | -59.48617 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 38f29015-ca0b-3333-ae0e-816569c37809 | -9.16609 | -60.81018 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3aee1cf-6313-34e7-9d71-f473fd77734a | -6.68714 | -58.85952 | 2025-08-24 04:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e6ab273d-2718-3c13-a0e9-deb1b98129ba | -9.17131 | -58.30275 | 2025-08-24 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c389ca8-454d-3e03-a71e-f6612dfc107a | -6.90446 | -62.98759 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c71caca8-068b-3896-8cc0-e128c9741ff7 | -8.22225 | -45.11103 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f080e79-1dc0-3192-abfd-a535e45b7427 | -9.1588 | -59.51398 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f60591f-7805-3882-9077-c75f286d596f | -9.71395 | -48.54133 | 2025-08-24 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da628264-5207-3a3e-99a9-6f88e1104089 | -9.74015 | -54.93474 | 2025-08-24 04:59:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 788a414c-ad76-3195-addd-7abbe79555ad | -8.06105 | -44.98578 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| effc9f76-dafd-3fdd-8777-171bb8d63547 | -7.42943 | -60.62324 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d801dbea-9de8-3492-bceb-2224a54625d5 | -8.05922 | -44.99942 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 911e533f-a015-335c-909a-9d2910f19492 | -8.63822 | -62.6302 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 899e226d-ca67-3003-b19f-ce52f159fd7a | -8.06033 | -49.65358 | 2025-08-24 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11521397-5303-39a2-a367-d75999c69e2b | -9.20362 | -59.47645 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03c51d63-35af-363b-a2dc-a2ffa7561435 | -8.7618 | -46.75148 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc383978-ee5d-3617-b8a6-76254028d51b | -8.71125 | -51.14036 | 2025-08-24 04:59:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f963802-23bc-3a0c-bd34-1f30ea5d339c | -9.16826 | -59.45736 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a782cd9-992a-3aeb-a48f-8b2b84b8f25f | -8.61445 | -62.64693 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README58.md)
