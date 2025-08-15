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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63b9a632-da7c-35f8-9e59-751ccd1bd82f | -7.5357 | -61.341801 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e87b7974-de9f-3be6-be05-96fccb7c441f | -6.9058 | -59.1437 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 956b0c69-8a58-39b3-a559-e780551ad04d | -6.9372 | -59.811699 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 936770a9-2054-3a7b-aec0-1f8233328ee7 | -8.6799 | -62.439098 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2de94df0-e9f9-300b-9bf3-92f117772637 | -6.8918 | -59.127899 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b53e2a45-217f-3548-8302-9b5cfc05fc63 | -5.9236 | -59.930599 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3559573d-8ea8-3526-8bff-9f92565ba6d4 | -6.4848 | -62.938 | 2025-08-15 01:10:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9269e8-fb82-3960-b967-bd154a6e5abc | -9.6378 | -63.089802 | 2025-08-15 01:10:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 691fa995-afc9-3f3d-bbb0-28d63705f608 | -9.0943 | -60.762901 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0ef6ecd-24bd-30ba-a35a-34dfa194b9e1 | -9.7974 | -61.499001 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 966833d8-14fe-38df-9f02-e225d3194d53 | -7.3193 | -60.619999 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56809070-d939-3ae5-b5bb-37e67e71a99d | -5.4633 | -60.124401 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de06fc70-53d8-392e-a74f-755918ac3310 | -6.7165 | -58.817902 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b05a837-522c-3210-98de-ac7a5adfe300 | -7.887 | -61.800301 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad65368f-cc97-3c9d-9de7-c946768d4e11 | -8.8023 | -63.451698 | 2025-08-15 01:10:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df4a5e99-5fba-38a3-8f33-488b23f02cc0 | -11.358 | -55.422798 | 2025-08-15 01:10:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59025b88-2d5e-3f29-ab99-269bc7b1e5ff | -6.9155 | -59.141499 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7aad2c34-230d-371a-9e69-26fa12d44009 | -8.0562 | -61.591499 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f30877f2-23b5-3990-adbb-dc565d637fa9 | -6.1095 | -59.932201 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0891ad64-5ad0-3873-a197-9cff5e3cff9b | -6.1075 | -59.923801 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69968497-b930-37a5-9ef3-5e9ddcbf3fcd | -6.0821 | -59.9473 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6a03c2d-1ec9-36c2-a725-fcbf0c931ba7 | -9.2105 | -59.653801 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e421442-b72e-3ab3-8803-af685a996595 | -9.9358 | -60.475201 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1da9556d-c47c-3397-89ca-f76809cd4491 | -6.7284 | -58.8251 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c156dfa-4251-35c0-ae56-cfa2923f6d37 | -7.2997 | -60.6245 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f938ce66-d017-3747-a0ce-3d16635f7aa6 | -10.4786 | -61.3209 | 2025-08-15 01:10:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcf51579-bda1-3d15-a8fb-2a93ce79de69 | -6.6653 | -58.819901 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dce66089-1659-3f14-b5d0-51da4082ee5e | -7.4047 | -60.006001 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32038691-e575-301a-b770-4ec689036df7 | -9.5127 | -60.5186 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d04d7a53-e2ae-3d12-9660-b881a7239ec7 | -9.2203 | -59.6516 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e477039f-9e55-361d-872f-92a2aea53c14 | -6.7306 | -58.834499 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50f59621-2dd3-3535-ad57-960831418adc | -9.1928 | -59.6665 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0ae4d8b-0c93-37d6-9834-7d1376836de3 | -9.175 | -59.6791 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0a39a5b-2d6d-3980-8c36-38b2ba87f105 | -10.3628 | -64.432098 | 2025-08-15 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 461b0c59-f585-37bf-9cfd-c82f0faa7412 | -7.4182 | -60.019798 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84bff764-ce29-3cc4-977c-14c5e340ac3a | -7.3371 | -60.607899 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2034cabe-8f72-317e-8be1-733daa844f7b | -9.1578 | -59.649101 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7403d10b-1490-3449-9e09-70b1caf712b7 | -9.2007 | -59.656101 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccefff58-d037-3e0e-83f7-2d32e8a10a55 | -6.8841 | -59.139301 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1cd853a-f4fc-3214-9b4e-df4f146bedc0 | -13.1241 | -57.1604 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55c9ec7f-c868-33c0-899b-0053c9fcf253 | -13.1194 | -57.1408 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2db853f-c03c-3427-a0c3-c20aba013194 | -7.428 | -60.017502 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa7c5a2-cbf6-3c8d-83bb-881dda39bda6 | -7.8297 | -61.320301 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8410c036-8128-3f5e-b4ca-713ea11a2c43 | -9.1652 | -59.6814 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10e45829-72bd-35d9-a98a-e4a3776f86fd | -5.9334 | -59.928398 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e0bf6a8-865f-3640-be99-956bb91cd7fb | -16.3064 | -52.914902 | 2025-08-15 01:10:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb7ef7d-008b-35fa-8ab6-383d38704ae1 | -7.8036 | -61.3414 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57745586-4d03-338e-8c54-b458faaec5ec | -6.7035 | -58.8508 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7aee7329-f918-3ab0-9903-fae26cd0d7d4 | -6.6969 | -58.822498 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14f1fd22-6213-3996-9b2b-bb2afb1fb453 | -6.7142 | -58.808498 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a79a6be-b745-3dff-a797-dcceb1034a65 | -17.055599 | -51.786201 | 2025-08-15 01:10:00 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1287bd78-4c33-3589-b92d-bbd11b22a525 | -9.9277 | -60.484901 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32ba3292-3096-3ca7-b644-6f6b3db9d3cd | -9.1946 | -59.6745 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb722452-cfcc-30fa-8e41-ab01c127f8ea | -7.3077 | -60.614601 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 545430e5-ecab-3c53-a94d-3b7a72ec077a | -7.4201 | -60.027802 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80a1b8e6-33be-3311-8011-2010899ceeca | -7.0677 | -59.219398 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5854364-898e-3efd-9f7c-78841861b6d6 | -8.8038 | -63.458698 | 2025-08-15 01:10:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7d10a9-c0b2-333e-9855-b379c365b89c | -10.477 | -61.313801 | 2025-08-15 01:10:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02de8e14-ecf7-3fae-a003-0386ca9e8303 | -9.3918 | -60.530899 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa67732-57b0-32cb-af59-ad5ff1e9daba | -6.7239 | -58.806198 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37b42178-c11c-3462-a3b2-5d3177aaaf59 | -7.3095 | -60.622299 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68107232-3eb7-3eb2-a38e-fb2746ea2667 | -9.1634 | -59.673302 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6497e3a-fff8-3b21-a0f6-c5ea541d7ff5 | -6.9061 | -59.632702 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e92e1cd-e7ef-3a00-9c8d-0d29b2cf1477 | -8.1122 | -61.202801 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b58e3837-52aa-30a2-b5b1-1b1ec6174d4c | -13.112 | -57.153099 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 261b53ea-766f-3b76-b1f2-886e4be10844 | -9.5093 | -60.5037 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb286d3d-4f17-34dc-ba43-cda8c53ab2b4 | -7.4164 | -60.0117 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06045cc6-f4b1-3e2c-a51e-263badf2d83c | -7.8772 | -61.802601 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9643f649-5931-3816-b4bc-606d0ec120fc | -6.0978 | -59.926102 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddf2694-6c98-30cd-8a8d-20f7154b2c9d | -7.0852 | -59.205898 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0163f18-bcb5-330d-9cc0-4a17a5115da2 | -7.3291 | -60.617802 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05830651-2d42-377d-b405-e2842edbe816 | -9.5161 | -60.533401 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da51e58f-3de0-33aa-851a-1939063f0471 | -9.1713 | -59.662998 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab37953-0ee9-3730-bfac-3f4d3d2b3058 | -6.0919 | -59.945099 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26c90ee0-edd0-3fdf-9783-18c0d3484f8b | -9.351 | -62.585602 | 2025-08-15 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e38d268e-da66-37aa-88a0-47d9e3dfb3ae | -8.9208 | -60.725399 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 626537e9-93da-3401-b9d1-bb5de1369d68 | -9.9439 | -60.4655 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60b06280-8297-37ce-9d0b-05dff1a55270 | -11.7431 | -64.891998 | 2025-08-15 01:10:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d951e52a-d4d2-376a-a810-4bc243c1e499 | -6.0684 | -59.9328 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc26f20-a0a2-3a90-8360-44691e3fa195 | -7.5325 | -61.372799 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 025c6bd1-4d33-321f-85b7-b4335ef7c1a9 | -8.5626 | -63.9044 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf142d3c-f081-3678-a0ec-1329469ec0f9 | -13.1217 | -57.1506 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8662b47b-8ac8-38a2-865d-62c17b57e42b | -5.4653 | -60.132702 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dccc6515-06c7-3c38-ad06-f7fc5c95607e | -7.3273 | -60.6101 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65571936-5984-3691-bc3b-8174e2ff77bf | -9.1499 | -59.6595 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d03e424-5e6a-3bc2-b0b9-41f541c7ddf7 | -9.183 | -59.6688 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e68c6ecd-34a9-35ab-8bb9-e25438cf57ab | -9.1909 | -59.658401 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b70431e0-a6b7-39ee-bf52-527f79d3e835 | -9.8346 | -60.753899 | 2025-08-15 01:10:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da77d8d8-9c3c-3f20-896d-f6a5b782711d | -9.3479 | -62.5718 | 2025-08-15 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 235f71ea-7db3-3b36-b49d-1f9185a6f482 | -7.1527 | -59.6292 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a50c20b6-5235-357a-a434-52ffe89e7368 | -9.1769 | -59.687099 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8f283a-0968-3665-b63a-4aa1ed0b4534 | -10.3334 | -64.438499 | 2025-08-15 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 70b25b49-dc0f-3885-b51f-ff189caf4a33 | -7.4299 | -60.025501 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4856c173-de7c-321a-a255-a29f92886bb9 | -6.9303 | -59.5305 | 2025-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 2982bcd5-903d-31d4-aee3-cf1d14f168f1 | -5.455 | -60.1391 | 2025-08-15 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 26dea76d-2acf-3b17-a98e-141688409934 | -9.4994 | -60.5278 | 2025-08-15 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 829de0d7-7166-3b4e-97c2-275f234d9105 | -11.3657 | -55.4107 | 2025-08-15 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 12609012-a76d-3be1-948d-ef050415b353 | -2.4876 | -47.5737 | 2025-08-15 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| b8486cb9-d04f-378e-8845-4cfcf48d4108 | -7.5292 | -61.3254 | 2025-08-15 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 3f72f192-f4ea-3f3d-8075-a8457941c92b | -9.5179 | -60.5461 | 2025-08-15 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |


[Clique aqui para ver as próximas entradas](README10.md)
