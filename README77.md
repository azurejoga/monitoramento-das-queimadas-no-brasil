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
| dd2f143c-f7ab-3177-9eff-aac80502ba3e | -12.5562 | -46.9357 | 2025-08-16 10:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 743bf02e-8d8c-3d71-a9dc-6a023aad6b04 | -12.6139 | -46.9273 | 2025-08-16 10:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2e22c10f-055f-394b-8fb5-bf313c6d4ffa | -6.5638 | -43.0357 | 2025-08-16 10:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 4071db4f-894c-31dd-aa94-8f200ced91b6 | -12.6139 | -46.9273 | 2025-08-16 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 12396e54-e537-320e-abd0-e682558b53dd | -12.5558 | -46.9583 | 2025-08-16 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 9ceaf976-57be-336d-a57f-ed6798977720 | -12.5562 | -46.9357 | 2025-08-16 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 119d61a1-30dc-30dd-9086-b8b0a492efd7 | -12.5562 | -46.9357 | 2025-08-16 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 45177e05-68e2-3fe7-85ae-326d4cbae466 | -6.545 | -43.0373 | 2025-08-16 11:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 793a728c-3514-344a-b747-a83eec741e9a | -12.5558 | -46.9583 | 2025-08-16 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 4f902a16-094b-3698-a00d-288e2be313b0 | -12.6139 | -46.9273 | 2025-08-16 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 5e000cd4-f50b-30da-83a1-20dea417f215 | -6.5638 | -43.0357 | 2025-08-16 11:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 51c94919-72e9-3450-8391-fdd918710237 | -12.6139 | -46.9273 | 2025-08-16 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| bbb0165d-fba8-3a87-9023-68a9d0332cce | -12.5562 | -46.9357 | 2025-08-16 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 8af2e9d7-d518-3c4b-9ec4-7b35247f4618 | -6.545 | -43.0373 | 2025-08-16 11:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9f83b293-28d2-34fa-9be8-26c1b6991120 | -12.5558 | -46.9583 | 2025-08-16 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 15963c5e-157d-3e4c-8386-470c1962c33b | -6.5638 | -43.0357 | 2025-08-16 11:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 6adbd6f9-e5ed-3494-8fec-4612622e8dfb | -12.5558 | -46.9583 | 2025-08-16 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 96b7ed43-a756-3008-8622-271e692e023f | -13.8748 | -45.5411 | 2025-08-16 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 2ee15ca6-8a5f-3037-9b24-e809589b9419 | -12.6139 | -46.9273 | 2025-08-16 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 58593d79-7a7c-3f49-91d3-e69f1f99d27b | -12.5558 | -46.9583 | 2025-08-16 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 085afa83-1faf-3b4a-a9d0-8a47f5e8fedc | -12.8045 | -45.9681 | 2025-08-16 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| f464aacd-95bd-34b8-8663-ebe40d8d33f1 | -6.5638 | -43.0357 | 2025-08-16 11:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 572e3c7b-8974-3c66-b250-2cf8f090f492 | -6.545 | -43.0373 | 2025-08-16 11:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 74f98d1b-fefe-34ad-8deb-361c89407e3a | -6.5638 | -43.0357 | 2025-08-16 11:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| a481a6a0-0886-3472-a0e5-7075a7c9e019 | -6.545 | -43.0373 | 2025-08-16 11:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 18680344-307e-3caf-842c-ce7dcf2b5ba2 | -12.6139 | -46.9273 | 2025-08-16 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| a503e4c5-3524-31bf-a354-665904fe22f3 | -12.5558 | -46.9583 | 2025-08-16 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| bab44e48-a2de-348f-a908-4f1e876a4263 | -12.6143 | -46.9047 | 2025-08-16 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e12e0618-3cf8-338f-bc1d-effda61071dc | -6.5638 | -43.0357 | 2025-08-16 11:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 517b794d-2bfd-31cc-8cac-8735941623db | -12.5558 | -46.9583 | 2025-08-16 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 1f48e174-0739-38d3-a4c7-b5ed36ca8bd3 | -6.545 | -43.0373 | 2025-08-16 11:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| e72365f5-2476-32d6-b6b5-81f317839085 | -12.8045 | -45.9681 | 2025-08-16 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| fb869997-7fe9-3649-ad12-26eb99ffb5bf | -12.6143 | -46.9047 | 2025-08-16 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 35335fee-d18d-3eb8-a1d2-f39dc079c701 | -12.5947 | -46.9301 | 2025-08-16 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 38ba3983-632e-3dff-8322-9f297b4aa186 | -12.6139 | -46.9273 | 2025-08-16 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 235.2 |
| 102f1e43-f6cc-3d44-939d-95764708d6f6 | -12.5558 | -46.9583 | 2025-08-16 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 0e12d591-5b9d-39e5-89ad-ca238ec43cec | -12.6143 | -46.9047 | 2025-08-16 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| c0fe641d-7cfe-3125-8429-85127ca5a5b9 | -12.6139 | -46.9273 | 2025-08-16 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 182.5 |
| bf1b47f3-8729-362e-bc6e-801bede090e4 | -6.5638 | -43.0357 | 2025-08-16 12:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 45e67704-71e4-3b5b-bc68-79585a2ef6aa | -7.9439 | -63.2225 | 2025-08-16 12:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bd169b39-c76b-3dcd-a8ec-b473bfc214e1 | -7.9624 | -63.2218 | 2025-08-16 12:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 318f18c6-ccd8-34da-96ce-e237998c0055 | -6.545 | -43.0373 | 2025-08-16 12:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 3badf9a1-6121-3f72-8b21-6e15a9ce5a31 | -13.8748 | -45.5411 | 2025-08-16 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 45b6c6ce-8699-31e7-8c2e-33e7118edd03 | -12.6139 | -46.9273 | 2025-08-16 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 2e3e6cf0-c098-3f3f-9350-1db917c99dc1 | -6.5638 | -43.0357 | 2025-08-16 12:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 64808ece-edc0-38f2-b1b8-5dfbd1539504 | -12.5365 | -46.9611 | 2025-08-16 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 408f1128-8c32-3527-b099-88fb8bd9dc1d | -12.5562 | -46.9357 | 2025-08-16 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 164bba27-d2d6-305e-9090-ed58bd4a2055 | -6.545 | -43.0373 | 2025-08-16 12:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 75ca2d7b-f465-3108-84f1-730300b94b12 | -12.5558 | -46.9583 | 2025-08-16 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| dd3d97ca-7d1a-3d7d-9561-d2bf7cc4e176 | -12.6143 | -46.9047 | 2025-08-16 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| bf3a8869-381c-3a9f-bac9-ed05ab8c7202 | -12.5947 | -46.9301 | 2025-08-16 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8eeb8bc4-afd1-3eb9-a0f3-84896649d3ef | -7.9624 | -63.2218 | 2025-08-16 12:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 71d046d0-36aa-3647-9e3a-20c6ea1e8fbe | -13.8748 | -45.5411 | 2025-08-16 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d5b04626-b731-3b24-bd5d-e5d2aabf3196 | -12.6139 | -46.9273 | 2025-08-16 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 7564dbe5-1c12-3cae-9332-551bce856448 | -12.5947 | -46.9301 | 2025-08-16 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| afa1fab7-d1c1-3953-90ad-1dc23bc10fb7 | -7.9624 | -63.2218 | 2025-08-16 12:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 28dbbe73-119a-3dd5-b1f2-3cf717271bcd | -12.6143 | -46.9047 | 2025-08-16 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| bd527dc5-e30e-37a3-8043-8718b7e9ab19 | -6.5638 | -43.0357 | 2025-08-16 12:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| c000669e-e9d2-31bb-a5bd-7e5f76877775 | -6.545 | -43.0373 | 2025-08-16 12:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c31a8800-b829-3973-8f0a-5c1710b6eed9 | -12.5558 | -46.9583 | 2025-08-16 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 61581cc7-3629-39d8-9c15-8573ea03a40a | -13.8748 | -45.5411 | 2025-08-16 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| b166fd61-2e60-37b9-9432-cf7ec17de24e | -12.8045 | -45.9681 | 2025-08-16 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| bf9e3cb2-ea85-3541-8f9a-98395c09791b | -12.6139 | -46.9273 | 2025-08-16 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| cb594b40-1e5a-3475-937c-ccb6b3ab825f | -6.5638 | -43.0357 | 2025-08-16 12:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 0d33d34e-52d7-333e-8a82-adb0be124051 | -12.6143 | -46.9047 | 2025-08-16 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| edecdb07-c330-332a-940b-3673371294b8 | -7.9624 | -63.2218 | 2025-08-16 12:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8ea55e25-a68b-3456-a7bc-ff93ca8367ba | -6.545 | -43.0373 | 2025-08-16 12:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 84914722-729f-35e3-812c-e4a82d226d84 | -12.8229 | -46.0109 | 2025-08-16 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 64adae66-95d9-32db-8833-f44ca5e4ece0 | -8.9893 | -61.7024 | 2025-08-16 12:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 771600c6-fa81-3d90-ba63-9084e0b363a3 | -12.8418 | -46.0309 | 2025-08-16 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 90d5eff5-2a48-3b73-ad1e-8c46030a987a | -12.8225 | -46.0339 | 2025-08-16 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c03b6711-5003-3c45-8b96-47faa30e84c6 | -12.5558 | -46.9583 | 2025-08-16 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 5f54b8b7-f322-3dc7-a47b-238821f50479 | -12.5947 | -46.9301 | 2025-08-16 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 715b2c50-ab1c-38ac-93ee-d2ace9859daf | -8.9708 | -61.7033 | 2025-08-16 12:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 81a29c82-7fff-3ba2-a756-468382708fb7 | -6.545 | -43.0373 | 2025-08-16 12:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 26d83286-55f6-35f6-a697-da8b7bc84fba | -7.9439 | -63.2225 | 2025-08-16 12:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| b7e234ff-c514-36e1-8efd-0c9c2a562977 | -8.9708 | -61.7033 | 2025-08-16 12:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 40ecaa4c-2093-3dc9-8c08-c4c073861187 | -12.6143 | -46.9047 | 2025-08-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| acfe6ca1-bb50-3586-8789-969d6cd143f5 | -6.5638 | -43.0357 | 2025-08-16 12:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| e0b4880b-78b3-3073-a6bc-f82c2e864ee9 | -12.5562 | -46.9357 | 2025-08-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e7db0cf7-aa49-36df-bc32-946ba85ac017 | -12.5947 | -46.9301 | 2025-08-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 5dbeccf8-5f29-376e-9667-0146741bd30f | -12.6139 | -46.9273 | 2025-08-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 9d5b9fb7-1937-32b2-a13a-513b0e62709f | -14.9628 | -54.7351 | 2025-08-16 12:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9b4a0cf9-b00c-324b-a941-1b7d2014d1fd | -15.1899 | -53.853 | 2025-08-16 12:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b27f5ae0-b9ff-3a9a-b808-57c3034406cb | -12.5558 | -46.9583 | 2025-08-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 314d5fd7-4d83-36f9-9f36-88d8c74cf712 | -7.9624 | -63.2218 | 2025-08-16 12:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 78306d38-4882-35ef-ab66-146e7b65d46a | -8.5677 | -64.1598 | 2025-08-16 12:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| ece5920c-d306-3a20-8fb0-13d83175d5dc | -12.8418 | -46.0309 | 2025-08-16 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ee25a79a-4a5d-3ad1-94b6-2e945d9c41e7 | -12.5947 | -46.9301 | 2025-08-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| b7818133-1757-3398-a6e1-c4f810ac7c58 | -6.545 | -43.0373 | 2025-08-16 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 93865d77-1289-3249-a8ae-053c5d879f20 | -12.6139 | -46.9273 | 2025-08-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 67a47cac-7e7f-35ff-acf1-e7ef24c587b3 | -6.5638 | -43.0357 | 2025-08-16 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 92a3ad64-933c-31b2-8508-6afa05898bd8 | -12.5558 | -46.9583 | 2025-08-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 00913b92-5558-3f6c-919f-926b383ebb9e | -7.9439 | -63.2225 | 2025-08-16 12:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1e13303b-83e1-39ec-b905-58bf0f5af51b | -8.9893 | -61.7024 | 2025-08-16 12:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 49156d65-638b-3941-925b-3246bb86a0f4 | -12.5365 | -46.9611 | 2025-08-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 7b60ef57-0dbe-313e-8751-9ca223ed40a5 | -14.9628 | -54.7351 | 2025-08-16 12:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 90445a7e-6344-3545-9a9c-6ce79012cee3 | -12.6143 | -46.9047 | 2025-08-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 157dc81d-5420-3d9a-9d4c-034a0abb0a0a | -7.9624 | -63.2218 | 2025-08-16 12:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 36ea2ef1-7182-3fcf-b66c-0678d6db6b14 | -13.8748 | -45.5411 | 2025-08-16 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |


[Clique aqui para ver as próximas entradas](README78.md)
