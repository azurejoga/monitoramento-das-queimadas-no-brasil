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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 783a3308-9bc6-3012-b40c-853415381531 | -8.66669 | -62.82954 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bf7987e-9923-31c3-831c-d9ef5747aec2 | -8.67964 | -62.40216 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084436d3-35af-36c1-b7f3-ba200444919c | -7.56195 | -63.06957 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9ae2b305-799f-3ee2-9a22-d86ec48a3472 | -9.44781 | -60.57262 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fd1fd6c-3cc4-3ed9-9131-a72e65f2fe0f | -9.28042 | -59.74608 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1965060-0e31-3121-8d8b-90df700ce23a | -9.64259 | -63.1152 | 2025-09-02 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d25bd75-fdda-3b79-a43f-a20119cd5fab | -6.79253 | -52.81395 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ae33ef7-bb94-38b6-bb1b-a0c326b0aaba | -8.66281 | -62.8325 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c8b2e72b-2bb8-3208-8e6b-df973cb930c9 | -11.6569 | -52.17452 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05c99d33-9ee6-3f31-aa15-2ddbc1fa86c1 | -11.67452 | -52.18141 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6c8bf2e6-dc28-3ea2-aa69-6ed3705842c8 | -11.42976 | -55.18561 | 2025-09-02 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1191408b-8f1a-30c8-b19f-1a94e4897849 | -6.83653 | -52.82267 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 041a6986-4f07-3632-b666-d01acc742559 | -6.84928 | -52.81046 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7027215-d0f1-3c3d-8762-7f3254af4503 | -7.08543 | -63.17791 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 856be7eb-53b2-36c6-a64a-efb3fb193cf0 | -9.31115 | -63.4369 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6a9e6ed-73e6-3073-b825-86119b87eb2a | -6.82568 | -52.821 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de63da4b-6713-3698-a9aa-0eaa9705e3c8 | -7.76775 | -61.20193 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82b07248-312c-3569-af27-e85c84920a78 | -7.28169 | -60.66581 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bec31067-38cb-3e35-bddd-66791a239e81 | -8.69627 | -62.40481 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f67d6c5-c325-3a27-813f-a2753628a373 | -6.40312 | -58.21281 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6dbab0b4-a022-3ea3-8ce9-dcd0a7063325 | -7.6812 | -61.08604 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1501281c-27b1-3609-a497-288f409f52c0 | -7.54564 | -61.3283 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0838ba50-ad6c-3434-b9c3-7b17fb61ad16 | -6.83748 | -52.8157 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac0f4939-15db-3d2d-a7ac-7cb4b6e7b0d9 | -11.68016 | -52.22202 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6736cf3a-c7f4-35c2-8e57-3593efbd7bba | -11.65828 | -52.21574 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9e7f2fce-5fbd-3b53-ac3f-1e817098466a | -7.27659 | -60.65377 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f87671e0-c435-3324-9613-5777cc3ed22b | -11.66846 | -52.18075 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 386c68a4-40bc-3b59-af77-5c0850379fb6 | -8.55569 | -63.01257 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b4bb490-83f1-37b8-9943-9c9784dffeaa | -11.67303 | -52.23013 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f9ac66e1-3277-3ce6-9d16-2af8591f4a02 | -10.75755 | -59.84215 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aab7c8d-6d34-31a4-bbb8-5cfe4589c8de | -9.44434 | -60.5721 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7634b701-3f21-3f62-ada9-1948435d71e6 | -7.60641 | -61.61251 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58fec290-c6fc-36a7-a26d-02d024552f16 | -8.55236 | -63.01204 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80dac966-bdfd-3146-bc26-2f80a878807f | -10.75795 | -59.83975 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae5edac3-e13f-3eac-9dd4-9864cd09ce91 | -10.24887 | -64.32065 | 2025-09-02 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd27013d-6e6c-32af-9fee-8ab652901ee9 | -6.81976 | -52.82381 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 897eada1-b449-36dd-a9e9-f379ed45321f | -11.67357 | -52.2257 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2d06068a-fbd1-372b-8d28-dc177ce30b2c | -10.45416 | -49.05925 | 2025-09-02 05:31:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5aff967-790e-3c08-9567-9d722d729f9e | -6.83514 | -52.83284 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e58cad6b-f03d-3602-8bbc-9a47f33eb1dd | -7.59031 | -61.62798 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 212f66f8-d64d-3a76-88d1-932647c8eae5 | -8.69572 | -62.4083 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6086b0f-0cee-3975-a5b1-3834d671dc91 | -8.69247 | -62.47219 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dcdb0cb-554e-30e1-9498-7848bc712b0e | -6.78753 | -52.81012 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b512c11f-5cd9-3e6f-aa20-b26405707c0c | -7.25558 | -57.54721 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9a7f522-7daa-3ae0-b6d8-1358cc81e415 | -7.56593 | -63.84351 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b61108f-6e77-3e00-a692-daf5b925fc89 | -8.50582 | -63.90479 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 20fdfb8c-dd42-3056-8a99-08c41a92b35a | -10.25161 | -64.4979 | 2025-09-02 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87b9ffbd-d20f-3080-801d-1a5e3cea787a | -6.81424 | -52.81717 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d39a26ea-bbc4-36f8-9b38-70d3d3cb06d9 | -8.73731 | -62.42566 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55846228-d81f-3a81-8774-151ef7fe366d | -11.6648 | -52.19741 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f501b049-b87c-3d20-8b12-c08fc31de4d4 | -9.16209 | -58.89706 | 2025-09-02 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb669e80-93d7-3dd8-b358-f55261b279ee | -6.80385 | -52.81224 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd540b34-fcea-320e-8b66-a0e378c7c631 | -9.16142 | -58.90155 | 2025-09-02 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af6c09e9-e519-345b-adce-0d818e3982f1 | -11.21195 | -55.06306 | 2025-09-02 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 483d0138-f4ae-3be7-ac6f-b85d9dfa0e9d | -7.70203 | -61.10769 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d610fd10-af93-3b87-aedf-d9f94f8a17db | -11.67741 | -52.20933 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| aca269b5-2d6f-35ce-8eb6-65aaa9a989f7 | -7.66549 | -61.09832 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3c8cc2b-5bf9-376a-a5e6-3765677e877e | -9.43856 | -60.5634 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ce5e6b6-735e-37ea-a60e-569a64ec2887 | -8.7144 | -50.44824 | 2025-09-02 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8b4e843-b385-325d-bbfe-124edc7c37b0 | -6.15236 | -62.61843 | 2025-09-02 05:31:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 138a9d47-ecf1-336c-9bea-bb57b4f3712c | -7.45656 | -63.15706 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1339ae62-862d-3dbb-ad3e-7f29bd5578a7 | -9.54169 | -65.94883 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 44e1cbbb-c255-3f05-a82e-f53c10a090f8 | -11.66741 | -52.18982 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 37af63fb-e2eb-38ba-aa25-9cafe67fdae4 | -11.65715 | -52.2098 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9922613a-f085-3fc2-89e1-51c74bad9f93 | -7.66212 | -61.09779 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb7160f4-7f8c-39f2-ae75-6ac6d53272c2 | -6.83607 | -52.82603 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05334850-ed08-313d-805c-55e748ca28d0 | -6.40072 | -58.2031 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 817a9751-3f8e-3091-a485-b8f49f37470f | -8.6595 | -62.91801 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47d7a2bb-cdb0-380d-85ba-15f99037e07f | -6.84244 | -52.81998 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd5b4953-bbb6-323e-ae2d-c9da0c4b4652 | -7.70148 | -61.11128 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67de7f5f-8737-3fae-84a7-9d49acabc1af | -6.82429 | -52.8313 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 078a32b6-04a6-3ecb-ba79-a9dc4cd1c833 | -6.80783 | -52.82328 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14d6dba1-2e62-3518-8bc1-600895ebcd25 | -9.44087 | -60.57157 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6887ad0-4c90-3e63-ad71-8e12a70ff703 | -10.255 | -64.49772 | 2025-09-02 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2176e9a6-f49c-36b9-b4c7-57a437f12995 | -11.66591 | -52.18843 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 135fa3fc-5a99-3062-b1ca-285aab44600e | -6.83108 | -52.81567 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46058ca2-e6de-330a-8f1f-6c9de40f35b7 | -6.43147 | -55.6119 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7494cf04-5d00-3465-ac54-45a12a86639c | -6.75569 | -56.39764 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eb61d5c-1679-3e4f-9103-f7ed46313ef2 | -11.65586 | -52.18354 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1ea5c34d-b533-389b-9f1d-d77c51bbbdc1 | -8.68406 | -62.39571 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dba366a-2d97-300c-a2da-83eefd2082e8 | -9.73298 | -48.96896 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ffda6e3-41f6-368b-b3f4-56a8b08a8c88 | -10.44796 | -54.7701 | 2025-09-02 05:31:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 42456093-d1f3-3857-9501-f1afdb9f1c17 | -8.7312 | -62.4211 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc2f188c-d2e0-3419-9906-d69b903e2847 | -7.70077 | -62.32545 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad16b494-83df-3f80-be1c-5cdc2008383d | -7.70259 | -61.1041 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e82c1a2c-0dd9-39ab-a723-5605d69da844 | -10.88018 | -55.75185 | 2025-09-02 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53c7eff9-7c6a-3809-a476-d3a219f85243 | -6.82368 | -52.82866 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0055274-29ba-3526-8d01-933a970acd7e | -6.92198 | -63.13708 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49b3b08a-a542-3745-ab09-f9afb11f45b8 | -8.71235 | -62.41095 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85ca8c29-d18e-31f6-9603-45922130a8e1 | -7.08822 | -63.182 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd8915b7-f6d1-309a-91c5-d64d9bac6d63 | -11.6555 | -52.17313 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6aea9b00-e9f5-351e-9473-bf1420d2e8a9 | -6.82912 | -52.82936 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23be1772-e344-3b48-ba5b-a2b6e12b83f3 | -6.78611 | -52.82022 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1da403ad-a260-3211-acd7-67a463e901a7 | -11.91845 | -50.62536 | 2025-09-02 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54fb4d6d-ea1c-3628-b9d4-43a99a5abfd8 | -9.73127 | -48.98307 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cb0fa1bb-6310-3b91-8482-3304ba0c3064 | -8.64717 | -62.60806 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d134ca-a8e8-332b-99e2-338828ade52d | -6.85373 | -52.81845 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c61c72e-2443-3e30-9be2-26c7b32e7824 | -6.79205 | -52.8174 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be409417-8080-3d4c-9e02-40beae49ce10 | -8.68962 | -62.40375 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ecbd5b-f73c-3061-8ecd-6fba51c0423e | -7.67445 | -61.08499 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README78.md)
