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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 807a3301-5e5b-3411-a6d8-f427d07a8cb7 | -8.66467 | -68.67458 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be3ad10-79c0-3a6a-96a9-406fe2b60808 | -6.63415 | -58.552 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b12ea77d-c6e2-39b0-8a9f-069ad9cf7c90 | -9.07306 | -65.72552 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 126eed35-f31b-3005-8c37-4202913f8e43 | -8.90616 | -62.43916 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2fce914-054b-3a4a-a10c-7a77f310d5d5 | -9.02418 | -65.70035 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a865d495-1c5b-3910-bc4d-5d2305ccdaa2 | -9.19053 | -59.47842 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 998c59cb-dffb-34c5-aae9-a1261fc90e7e | -8.24685 | -61.45993 | 2025-08-25 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95ba5f40-9de9-335c-ae38-10683cada270 | -9.22115 | -59.67415 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e5d4468-f5bc-344d-9a83-516f985933b8 | -8.2274 | -61.38748 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ed7fb2c-a4e4-3068-8671-ef32a3be3f1d | -8.77821 | -63.96317 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3455705-8e66-3882-a630-6af0e8d320d2 | -8.61379 | -62.59467 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 600bd00f-f0ef-30ad-9df7-48c5beeeefef | -9.25924 | -59.6414 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67f905ec-be9d-320d-9d59-2629e8a89a25 | -9.05038 | -65.72654 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe7c8a6d-dcb4-3fca-89a2-aa4b21600a17 | -9.82569 | -64.25582 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dec11a4-a32e-3dd2-9a9d-bc7a103b5753 | -8.91378 | -62.42813 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c8cf395-6eb1-3df1-9f15-998c60c47fac | -9.22987 | -60.9247 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f6dc376-8286-3629-b2a0-5369dbea42c8 | -9.52162 | -60.5289 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a10f20cd-f806-3948-adb2-ff3a62f7bf97 | -8.87969 | -62.46337 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d3034ad-0dd7-3697-a153-d9d60631b504 | -9.1536 | -59.45803 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e5b427d-303e-39c9-97c6-1318cf5ff609 | -9.17897 | -59.60738 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f60057bb-dec8-3f9c-bc98-b090f11fc660 | -9.18914 | -59.61839 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34f6311-e539-3e72-b08b-0bafec1efe22 | -7.54625 | -63.85594 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23c342f5-3f18-3190-8679-8bb29b66c9fd | -8.63429 | -62.64273 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b86c3ca5-51be-3fb8-91db-53d2b0c982e7 | -9.82518 | -64.25941 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b84718ee-a2f0-3fcf-885b-81a4cc748369 | -9.00947 | -65.69815 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5678cbde-4fa2-332f-a1a5-bf307fd065cd | -7.55482 | -63.85359 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f8d7a98-6357-3a66-b8da-5e0cfc4c5004 | -9.04478 | -65.73904 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa3b3e77-8c78-3177-b572-eaee01543a62 | -7.62862 | -62.72917 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3c8383fb-ec04-3cb0-b4f7-5fb51d0a943f | -8.10499 | -62.86298 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f4cb3e9-e327-3dd8-a9b1-d10bce6eda76 | -9.1904 | -59.43674 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ea43368-2929-3567-a623-e0582a678c31 | -8.21832 | -61.41824 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65fec2aa-ec0b-3ce1-a796-1bb5892d46ca | -9.1749 | -59.46276 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 00377ab9-d39a-3fd5-b55a-513d6a3390da | -9.00897 | -65.40073 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6a3be5e1-693a-3ddf-b472-d5380c79426d | -9.21694 | -59.70655 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aae879f-8b01-3fdc-8beb-5aadc9dc27d4 | -9.35747 | -67.56087 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf41dc59-824d-3b7e-bd46-6e22fad7992f | -8.22792 | -61.41967 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7381ba7d-aacb-3d29-8821-b90607fd7929 | -9.0357 | -65.72427 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a508e6e-1142-3cf9-bc69-c8e62008e207 | -8.92612 | -62.43928 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ca408e2-8ea1-31fd-a68f-4c95f9171ade | -9.00776 | -63.63332 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1df95c3e-040b-389b-adcb-cf73c6c3b5a6 | -8.60242 | -62.61113 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e149abe1-6f04-3947-b471-d7def212fbd8 | -7.54425 | -63.84116 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 860544f4-ea29-3503-aa97-4a64149dc8df | -10.41423 | -64.4166 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5b18fb0-0474-3330-bd84-913d75705496 | -8.23079 | -61.39859 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3e0bfbb-0b2f-3b1e-9409-a81c235ae35a | -9.17125 | -59.45298 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| be9d0731-11e1-31d9-8f92-62e2b331e741 | -9.19182 | -60.79082 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3014a3cb-8a48-3855-97c6-25083ed5cc98 | -8.21851 | -61.3806 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| afdf6164-e6de-3143-a57b-592adf5f9805 | -9.19102 | -59.47473 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62600b68-a7ff-3302-b043-14cf18895098 | -8.10875 | -62.86783 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc743c12-82e4-3341-b1aa-f11cf90dc513 | -7.56339 | -63.85125 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2c8d12c-40d4-3ead-acd6-c2bd3814eae3 | -9.18714 | -60.78704 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9c2f4c8f-bd82-326d-bec4-edce2d3f7a66 | -7.52356 | -63.81258 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3710080-0aae-3ad1-9689-6a42acbc7e3c | -7.49682 | -63.81953 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ddb87a6-753c-3fbb-9632-04eb2abe3feb | -8.65155 | -63.43146 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f52b5e1-0206-3476-b95d-8cdccad56486 | -8.87067 | -62.46206 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a0d1e61-47ae-3acc-bed8-f30257829687 | -9.1962 | -59.47339 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d56877b-5a9d-36d8-8421-d6abe6e1ae25 | -9.01846 | -65.38826 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3286b9e3-b5ef-38d8-9995-04602a711037 | -8.90941 | -62.41621 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4729eee9-f3c0-3379-91ac-4b3f4f048438 | -7.9088 | -63.06731 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b7633ff4-ab82-3220-8c04-af0079c4a777 | -6.63671 | -58.54794 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f409b327-db45-3507-ac35-468c02c47467 | -9.81758 | -64.25465 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71abcc4e-99ba-349d-8ea4-95430304d5c5 | -9.20789 | -60.78691 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 866c5153-b904-3cff-8e29-9e6af91c323f | -6.82466 | -58.95624 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b22f99cc-a7b8-372c-9b1b-a8024f1c0d46 | -9.15578 | -59.48471 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88785642-d012-338b-89ba-3d4dcb38de97 | -7.49734 | -63.81599 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05738e45-f025-390a-99df-bac965a38589 | -8.89201 | -62.45295 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 709672d9-711b-3c27-ab1a-8950cc8500aa | -9.81552 | -64.26904 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f3e6da0-534f-38dc-a34b-b9156a29c223 | -8.22002 | -69.86227 | 2025-08-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57ad2292-30ec-310d-9f2b-ad75afb772b2 | -8.97578 | -65.41877 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b0c9bbcc-87f2-3b5e-9551-40c6aa393766 | -9.05837 | -65.7233 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1339eaec-d739-345f-afab-e86dd58539af | -9.20037 | -59.48523 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3bdfd65-a674-33d5-a84e-21e2d4abcdfb | -9.04671 | -65.72598 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb9f5560-8059-3478-a596-e7c6e732b559 | -9.26389 | -59.78224 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e297641b-ecb4-301e-8f94-5f3db9c51bb8 | -5.79577 | -59.22198 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3514aa93-8595-31c5-a431-398b9f190ad2 | -9.52285 | -60.51945 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7771f623-2c5f-3ec3-858e-fdccbd279901 | -8.89904 | -62.45683 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e43d3994-b7a0-344e-8f2b-6dcd257776b4 | -9.16783 | -59.47903 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0ec0365-2fb0-3906-845a-fd9678021694 | -8.21778 | -61.38602 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 32c60449-5824-3f12-82a2-238ec0f064ff | -9.81655 | -64.26184 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aaf517f2-07a3-3216-bf0b-d2ad3a121961 | -9.19708 | -59.47175 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e287a660-3013-343d-a7a7-2b4349d76822 | -9.51367 | -60.50845 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b07fc50-6753-3d42-88a4-9b8c08a5d5a2 | -9.01779 | -65.3928 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff3da9c0-fd75-3e64-b20f-d1d15380f415 | -8.58969 | -62.60472 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6a6ce90-eff4-352b-a23c-1b31ac37c4d9 | -9.19349 | -59.45615 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3ab49ac-2f16-318e-938a-9947b5d843ff | -7.27014 | -57.66619 | 2025-08-25 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ab9898-8737-3a05-a168-86e5336aa365 | -7.61992 | -62.72788 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7f2282e1-4196-3efc-bb32-64d8b7da3952 | -9.22694 | -59.71537 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 854850aa-376f-37c9-a9e6-69fac8cd07fb | -9.20083 | -59.48154 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b694358-8bee-3015-a8d1-aa3116a022ab | -9.07548 | -66.06477 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67155914-8ed0-3304-bb6a-5b6255fa9c38 | -9.20749 | -60.78994 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6da7faae-aa7b-3e36-a70b-61656767f1c4 | -8.92221 | -62.43404 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d3f68d4-a754-3a82-a7b9-f15abb51e4a8 | -9.52326 | -60.51627 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68580679-3713-3419-8e92-bf0a8816540c | -9.22068 | -59.67775 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f6a1c40-9903-3e58-b700-59b2ece80c9d | -9.06874 | -65.72932 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 046d40ec-f7b0-3f7a-afe9-3748be6b54d2 | -8.1403 | -62.86396 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 551570cb-cdca-3f47-9b23-82e4b8b17615 | -8.13655 | -62.85912 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 601963c8-db58-387a-9edd-d03f10ec00a1 | -8.68637 | -62.87885 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8774cdcd-85c8-3029-a4b1-de5531884a62 | -8.54918 | -63.51935 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ede27072-7231-318c-ab08-cc55043f05fd | -7.57418 | -63.43506 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a4317f2-affa-3c48-9bdf-a4bebc249d2e | -7.54978 | -63.86007 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a92a304f-eebf-31d7-b518-e3e5c1db81cb | -9.25879 | -59.64505 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README79.md)
