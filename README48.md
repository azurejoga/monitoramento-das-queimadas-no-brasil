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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6836773-bb93-3780-bd52-4e47ed858891 | -4.29953 | -50.79807 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c165a60f-1cd8-3a12-9883-5dd3fd609cb3 | -4.63286 | -50.60611 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bb31612a-50e0-3248-887d-51378627b608 | -4.49157 | -46.40902 | 2026-10-01 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6059797-5604-3a63-949a-3288217d905c | -3.37796 | -50.94712 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4576269-782e-3cf7-80ba-e317300a4b6d | -4.30209 | -50.7826 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f435c3c1-fae8-3966-8acb-c0c749e90cc9 | 1.79008 | -55.65007 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 423afab1-87a5-3b26-9452-bde6a72773a6 | -3.17217 | -54.10815 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b4c7779e-1f42-3424-98ba-70c196cdcbb0 | -6.32227 | -44.4405 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a57304d5-bb59-30ff-a626-b262da1e261f | -3.57037 | -54.32593 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4556acfa-8729-366b-95f7-ab6975753833 | -3.21365 | -53.94685 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 025fab1c-11ca-3bda-89f9-6ff5ab2d152f | -5.76673 | -45.15133 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4dc3d3a-97d3-317a-a7e5-5847d6eab9df | -4.06624 | -51.09911 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5095fca3-4411-38a0-b64e-29dba4f765e9 | -2.97647 | -51.03236 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24ea800c-4147-387a-9469-938efb321909 | -1.90644 | -45.80528 | 2026-10-01 04:32:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d0b837-1db5-35a5-8194-d5d38f0a6000 | -4.25049 | -55.04373 | 2026-10-01 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90741549-dc7e-3828-a74e-640ef1db8826 | -3.16759 | -54.10432 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a9807671-ded9-3aaf-9d2b-bdadab08cf2f | -1.9583 | -50.6274 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d053e741-a8ac-36a7-a73c-2f5e60680e83 | -7.0232 | -45.2763 | 2026-10-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 847a817b-5a06-3d64-b0b1-7fb4c247849c | -4.29499 | -50.77622 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 8a711849-c278-3762-899c-66a80bc070f1 | -6.87889 | -44.8273 | 2026-10-01 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3cc96637-32ae-36eb-9090-aaac966e18da | -3.10358 | -50.27382 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 199336b2-e1cb-3aa6-8b19-212a0fd7bbe9 | -5.76282 | -45.15438 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8e562a90-5401-3c6b-a566-39b5e7369829 | -2.96532 | -51.02298 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d55403ec-4258-380b-a093-9231e2d9b491 | -3.15021 | -54.08339 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d836188-ac0a-39bb-a9b7-3a44b41c496b | -3.62981 | -54.5065 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 459e20d9-71de-3e74-8c6a-3557e3864be9 | -7.07626 | -42.31607 | 2026-10-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ff6bbe4d-c7ff-3b8e-825c-77e0dfa22824 | -4.26723 | -50.77157 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 55e4cb41-ee3d-37fe-8ccc-2679609e49e0 | -4.2763 | -50.7417 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e577a43b-4c43-35a3-8c67-002fbb91fb32 | -4.26324 | -50.77105 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4ddd2a31-2788-3656-a4fb-700b07b41665 | -3.30048 | -53.85625 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b531962-0f9d-34d5-9c4c-9d2dba1059f0 | -0.38938 | -51.84862 | 2026-10-01 04:32:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1817fb8-49bd-3bfa-a43c-9c4c2520338e | -3.14439 | -53.74729 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4bd6a163-d887-381f-ba7c-458f1ddac97a | -2.4812 | -49.25666 | 2026-10-01 04:32:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ffb92106-c0e9-3696-b28f-b0c5a067a8b7 | -5.75612 | -45.15335 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 01dab561-4827-3651-b1d1-9eca0c9206d9 | -3.11685 | -50.2912 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48e16fd1-ea5d-36ef-90f4-6315a824e915 | -4.27121 | -50.77213 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| d32d2e3e-4a05-3ed9-aa40-6182715a6ff0 | -3.17201 | -54.10072 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| d13824d5-99af-32e9-aa9f-c821d79414d4 | -4.27006 | -50.73885 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5bbaa108-2793-3426-91d0-b221d09b654b | -4.28733 | -50.74877 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9384a273-14e5-3e26-bd68-17ee02232e31 | -6.28476 | -44.14157 | 2026-10-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fddf0a38-c08f-3540-9688-c0c7b1338f59 | -3.16901 | -54.09555 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 39322f15-a519-3064-a6e5-f58286ece4b6 | -3.28557 | -53.85379 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 04c3d837-06a7-3e94-8ad5-dd22a7565a6d | -2.11285 | -49.25106 | 2026-10-01 04:32:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc223a49-31ef-378e-a68d-c50717b3e4d8 | -5.94508 | -51.69573 | 2026-10-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79dd125a-267f-3318-b45a-c7bed98d9db7 | -3.96248 | -49.45195 | 2026-10-01 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dedac09a-fe33-3e39-a9eb-c97c9096d039 | -3.1067 | -50.2794 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83dcf24d-e717-351d-92ae-b28942f7d6f5 | -1.42122 | -48.89128 | 2026-10-01 04:32:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85d7e890-6583-3f07-8ba0-a694a49a0fe2 | -4.29253 | -54.79678 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1dec951-b4e0-3ad3-ac8b-59e60575bed5 | -3.08955 | -50.26137 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c9a0a46-67d2-3b6b-bdb7-4f5fba6a97cb | -1.63878 | -55.12541 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8a72078-7348-3e9a-be9f-c4735a45ee56 | -3.16695 | -54.09988 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f5c66afc-6315-3533-8e97-cf74592e3ab5 | -3.20561 | -49.52357 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adb1e320-0f6c-32c1-8f8f-cc6f09c7831d | -3.57651 | -54.32074 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2735bf37-dca4-3ca4-837d-cb4a176d8a8b | -3.2708 | -50.70751 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f3d874-ffe6-37f4-8fa3-561a6c171462 | -4.2494 | -50.74086 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 52ec3fd1-7e52-3fc5-8feb-755678f0b5a5 | -3.10742 | -50.29985 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb014bde-aaaf-3d0e-a225-39e70789b4d9 | -4.25553 | -50.77858 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ded64da9-1528-3fdc-a1ef-ed411b0d8e18 | -4.26548 | -50.78199 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 2f0c1bd0-c064-380d-9804-def848b9a0c7 | -2.94875 | -47.94907 | 2026-10-01 04:32:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 461d7204-a96b-310b-ba5d-b7dfa1ea79d9 | -4.45329 | -47.92374 | 2026-10-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4de2cf90-7da0-3508-ad62-6b454fd9e147 | -3.11844 | -50.28128 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a143a721-d507-3ee0-8b81-2f8df3422652 | -4.25754 | -50.78069 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0be30946-55a4-3c03-9bde-1d2971727bf0 | -3.15116 | -54.07755 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e64440e0-a522-3841-b505-d4be9c164ba4 | -2.89506 | -54.13381 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c0bd93e-93fd-34a3-9004-3a241c8fe050 | -3.16031 | -54.08515 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0860a0bf-089e-34ef-a5fd-c4bee5586555 | -4.15757 | -48.90059 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ba4b21f-250a-3b5f-bd85-28fcae18d9cf | -1.63818 | -55.12905 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38ec6cc1-a65a-3945-af50-151837872e44 | -3.54827 | -51.53861 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee7d94c3-8da4-3999-8390-1f8ebeff6e40 | -4.26527 | -50.73472 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8fbdfcc0-2a2c-3eef-8631-32345157c7a4 | -3.10039 | -50.29357 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9fd962c9-6ec4-3395-98dc-2187e81f1e46 | -3.17151 | -54.10364 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 5d7db3e4-a0d5-3fcc-a049-46316703489f | -2.92701 | -48.74277 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8948603-deeb-332c-ba58-96632e4c01aa | -4.2944 | -50.7552 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3492105-caf1-35c3-868d-9aec9fe67434 | -4.30773 | -50.77309 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| deebc0e9-8843-30e0-8ced-ca57c99ca8ef | -4.28932 | -50.78581 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 74cb92c0-ccc7-3ae5-9a6c-22c452a304bc | -2.50125 | -56.91103 | 2026-10-01 04:32:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 430b2eec-4219-3690-bebe-2735160b3f21 | -3.10661 | -50.30484 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c5f56d9-e18f-3d74-8a95-23328f493360 | -3.15572 | -54.08143 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fe25097-6920-3d84-8ce6-3e841596fbbf | -2.98589 | -51.02635 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8cef1c0-ea40-3064-8a6c-e2b872cf9da9 | -2.06126 | -48.79468 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 919f5b6c-a056-3492-b0f2-a01fc05afbf3 | -5.75111 | -45.16346 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b3c9a4a-9227-3381-b02b-544a8a8365b3 | -5.22198 | -46.02313 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 110772f7-0e93-384a-953c-664bb33a7b0d | -4.12992 | -46.86802 | 2026-10-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a80830e-1037-3aa7-a608-01a17f4cd76f | -4.26924 | -50.7353 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab94714e-363a-3dd9-91f9-5f963a2e2f09 | -4.2641 | -50.76589 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d3ceca3e-726e-31c2-8712-e15a2e6511fd | 1.79143 | -55.65919 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b19aa81a-7a74-3615-9ee4-67b9210634fc | -3.41977 | -54.54382 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7ea4524-b4b4-3036-8b49-dd32fcf9ff54 | -2.97826 | -51.02133 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a4bffb8-44b2-3b0c-8164-1cb3ce2dd23a | -4.26463 | -50.78706 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 78627b74-91f6-31f0-84c1-9714e2039873 | -4.02904 | -54.19898 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83a62394-45f1-31e5-8fde-11ab3667b54c | -3.11692 | -50.2658 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7eac88d-b16d-3841-b1ef-17531a290cf8 | -2.97999 | -51.03671 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7010eac-c977-33de-954e-a4c944d57801 | -4.27654 | -50.78907 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 83761486-287a-3c8c-970a-ae4908d64441 | -3.80071 | -50.6072 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f7c34f4-6193-3df6-a42e-455a4aa379ca | -5.11451 | -56.01033 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d278f03a-3615-3808-a643-c90d61e84288 | -5.11931 | -56.01564 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05c37f04-5bca-3a28-ac79-8ea18d0de505 | -5.75446 | -45.16398 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d02fc62c-389d-307c-9dd1-e694eb2ce08c | -3.11772 | -50.26085 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4873d6ac-4529-3650-9c4b-e477592af21e | -4.26913 | -50.77005 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 9717bdcc-05a8-3a28-a9e5-cb7fbaf866b0 | -2.44378 | -49.21599 | 2026-10-01 04:32:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README49.md)
