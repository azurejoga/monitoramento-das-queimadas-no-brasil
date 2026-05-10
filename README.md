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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aea190bd-d5d0-3dd5-80c1-5804c7a3bb63 | -9.4071 | -50.6847 | 2026-05-10 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 99309716-868c-3f0a-ae1e-3743693bf9f7 | -17.9479 | -52.9308 | 2026-05-10 00:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 61cdd7b6-cb79-3b54-8c14-ad566e7ee502 | -17.9678 | -52.9277 | 2026-05-10 00:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 0331638a-9639-3097-9c74-b10b05b9c944 | -17.9683 | -52.9061 | 2026-05-10 00:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 0bf216dc-73cc-3178-8152-306cee78dd89 | -17.9484 | -52.9093 | 2026-05-10 00:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| dd1736ac-0678-3043-aa87-19350dda4e83 | -17.9678 | -52.9277 | 2026-05-10 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e061f89b-0c0e-3e46-856e-1197d5b5c564 | -9.4071 | -50.6847 | 2026-05-10 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 7e51d3c7-d4db-3cbe-99d7-c159a5c9d654 | -17.9683 | -52.9061 | 2026-05-10 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f661732d-e8d8-382f-a90e-fbf5634f26ca | -17.9484 | -52.9093 | 2026-05-10 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 83ab2d9b-cac7-3ad4-ad5e-3fa49a7ca6f2 | -17.9565 | -50.6872 | 2026-05-10 00:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 22fd1587-f2e0-358b-85c5-2a521f74e847 | -17.9281 | -52.934 | 2026-05-10 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e3c38211-cf77-3493-8f22-1f6954a5436e | -17.9479 | -52.9308 | 2026-05-10 00:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 4491eb8d-c516-311f-97e9-b0df96249fea | -17.9281 | -52.934 | 2026-05-10 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| d8bd2938-670e-301f-aaf6-01198bc2e2a3 | -9.4071 | -50.6847 | 2026-05-10 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 114b2229-570c-325a-9dff-7f178fcba6f5 | -17.9479 | -52.9308 | 2026-05-10 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 6a0ee0ef-e139-33d9-a638-befa4eae6635 | -17.9285 | -52.9124 | 2026-05-10 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 7155c097-5f2f-3bde-b90b-8d7e9e767b55 | -17.9484 | -52.9093 | 2026-05-10 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 78a2ab12-35a8-3d85-82ac-d57c120c0027 | -9.4071 | -50.6847 | 2026-05-10 00:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 01fac61a-6d23-3d40-9c79-16c2db325bc2 | -17.9479 | -52.9308 | 2026-05-10 00:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 0727f76b-4486-3205-b777-b1a5ce4e1313 | -17.9484 | -52.9093 | 2026-05-10 00:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7bfef6f4-4430-352d-9a1a-f93ea2073404 | -17.9683 | -52.9061 | 2026-05-10 00:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c73d72c2-d257-3cf6-94a2-20dfbc587d0c | -17.9678 | -52.9277 | 2026-05-10 00:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f66a6343-fa85-30e3-966c-1f6e20baeaad | -17.9491 | -52.912399 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93c7f5ee-d44c-3b2d-97ba-a66ee890978c | -9.417 | -50.676498 | 2026-05-10 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b9919d9-8db2-3c53-bde3-cc84a0839234 | -17.958799 | -52.91 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e9e14b1f-53a7-33d9-8685-4f012a8578c2 | -17.9881 | -52.902599 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c23d2c23-77df-3db2-a406-624fb114addd | -17.939301 | -52.914902 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d402a305-2484-3f62-a32a-be769b009358 | -9.42 | -50.688999 | 2026-05-10 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4455bede-2844-3e68-b89c-6d668efebdab | -6.3279 | -51.7127 | 2026-05-10 00:43:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00f9f65-1109-3f4d-94c5-0768a5d8ef3d | -17.950899 | -52.920101 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 975c46cc-fe46-348f-8c74-4ef161dfbc56 | -6.2272 | -55.643101 | 2026-05-10 00:43:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e147f688-176a-310a-a2b7-7bed91f13ea8 | -17.931299 | -52.924999 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45e5a10f-1820-3221-a053-21536ec9b527 | -17.9552 | -52.8946 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 847f656e-c42d-36f8-90f2-abe6edb58453 | -17.941099 | -52.9226 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c453f3c6-a86f-3973-a434-7960b1cf3c9a | -17.945499 | -52.896999 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d4293f8f-c6f8-3895-8c09-723b14b7c108 | -17.9296 | -52.917301 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7d2d1a76-d02b-3f37-8d56-4d0289293408 | -10.5593 | -56.333801 | 2026-05-10 00:43:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45f115ac-e6bb-3f30-b0a9-ce6ea639713a | -18.080601 | -46.361198 | 2026-05-10 00:43:00 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 47a565ba-2e18-3dbb-b16a-6386177fa90e | -17.9331 | -52.932701 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c858740-b241-316b-be5a-1436378530e0 | -7.0627 | -55.420399 | 2026-05-10 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bea2262-8e23-3393-8f72-30383aa42beb | -17.9375 | -52.9072 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 131cf4ad-8773-3b49-8f86-eec5d86df5e3 | -6.2238 | -55.6283 | 2026-05-10 00:43:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff163d35-8a4c-34ba-b954-310fa6e206ba | -17.9429 | -52.930302 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8a7ea9df-9b86-3efb-ad92-b81856bc736d | -9.4072 | -50.678902 | 2026-05-10 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 141fd010-3180-3786-b48f-e7d742c47c43 | -9.4103 | -50.691502 | 2026-05-10 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8946f978-8226-32b4-b34a-977a3ade552a | -17.9473 | -52.904701 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2f33bf48-0bb2-374c-8c26-f845a41d2ec2 | -6.3307 | -51.724602 | 2026-05-10 00:43:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a12bac-f466-3172-b86a-b56a249b2ab2 | -6.2255 | -55.6357 | 2026-05-10 00:43:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c525cf6-da7f-3ba8-9eeb-77ed6502e6b8 | -18.075899 | -46.3437 | 2026-05-10 00:43:00 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1002729e-c9bc-300b-9c03-beb4f4696397 | -17.957001 | -52.902302 | 2026-05-10 00:43:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 197434fa-20b4-31f0-8746-8d97c3391cdd | -17.9479 | -52.9308 | 2026-05-10 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 61109d7c-4961-3873-97ea-5b28c40441f0 | -17.9484 | -52.9093 | 2026-05-10 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f967a983-985c-3476-b0a7-21dc7a76229e | -17.9285 | -52.9124 | 2026-05-10 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| bc3d3299-ff10-3519-a62f-1a9e82fb4cd5 | -17.9281 | -52.934 | 2026-05-10 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f778b8e8-f9c3-31eb-be3a-76232f68a6f9 | -17.9683 | -52.9061 | 2026-05-10 01:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| e1b18a01-aef3-3c4e-a4e4-31b3212fc6e6 | -17.9484 | -52.9093 | 2026-05-10 01:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3e76df50-fe82-3a16-8b27-a5b8066c2131 | -9.4197 | -50.7038 | 2026-05-10 01:14:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 754a5d4f-c2ba-3caf-9dc2-0684ce6eec37 | -18.082001 | -46.3559 | 2026-05-10 01:14:00 | METOP-C | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 72bb31f2-1f8c-3910-8562-f6c6685bfaec | -9.4139 | -50.680099 | 2026-05-10 01:14:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fe850e1-5567-3237-a3c5-b634bbc76137 | -9.4265 | -50.689602 | 2026-05-10 01:14:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff3d4b8c-2a0e-3ce3-a945-128d95df7483 | -13.1901 | -52.7043 | 2026-05-10 01:14:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51bedc63-54a4-3629-9d49-cc81c031e220 | -12.0583 | -49.757702 | 2026-05-10 01:14:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cb39308-05b2-3611-80af-330effb411c1 | -7.0634 | -55.426399 | 2026-05-10 01:14:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 260e4275-0553-3401-8198-dfccb5a6c10a | -12.0614 | -49.7701 | 2026-05-10 01:14:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe210df-76cf-30ae-88ee-4b211613bff3 | -9.4236 | -50.6777 | 2026-05-10 01:14:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3489b8-6476-3314-a8f0-ed6264c119fb | -6.224 | -55.6334 | 2026-05-10 01:14:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae19cb80-1bd0-38bb-8be3-38edd3724b34 | -6.2273 | -55.6478 | 2026-05-10 01:14:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6864fbe4-0336-3e52-a31c-ac23e6afd498 | -9.4168 | -50.692001 | 2026-05-10 01:14:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a62ace4-4582-3353-a626-6f1dd066e574 | -9.4259 | -50.683 | 2026-05-10 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e63327e0-dbd3-39f4-81d9-44f08246acb3 | -9.4259 | -50.683 | 2026-05-10 01:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| c30889c2-ceb5-31fd-912f-43467dfb513b | -9.4259 | -50.683 | 2026-05-10 01:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e7f05d15-0b34-3cdf-9814-f7ffbe18e675 | -17.9479 | -52.9308 | 2026-05-10 01:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 5956fd41-c3d1-339a-9f9a-2899a17dbe55 | -17.9484 | -52.9093 | 2026-05-10 01:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 08927258-a5b5-3ef3-ad4b-3485f512b087 | -6.99151 | -42.86467 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 31ecac96-4f27-3344-9c67-d4ac3fb9c37c | -6.98097 | -42.87304 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 68d0f36a-845d-3365-9d26-a51e29330be4 | -6.97902 | -42.87287 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c5cc247b-0ef8-38d5-838d-bb06af78db46 | -6.97563 | -42.87206 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c32e33b4-0c8f-3db0-9de7-ec97f38ac76c | -6.97962 | -42.86954 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 892f131a-6960-3199-9995-a7775cb09891 | -6.97621 | -42.86872 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eb8a0c83-2895-3fda-9701-d5e3b8a79155 | -6.99031 | -42.87132 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fa274be4-f912-37ae-b504-9fceb6d7e576 | -6.98972 | -42.87463 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7330dd56-4f5c-3ced-8c9b-c14dcb8dd8a6 | -6.98155 | -42.86969 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 88a229b9-0505-37ca-85f6-ef2218e7fb2f | -6.98497 | -42.8704 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d366e5cc-d57f-36d1-9032-9619a69b944e | -6.99091 | -42.86799 | 2026-05-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c867ff8f-f4bb-3e14-87f7-43e970da7f7d | -10.59879 | -44.99692 | 2026-05-10 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cbccf485-4652-3d50-948b-3c86ea8d653a | -11.76295 | -43.64802 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0729af72-7327-362b-819c-f102ea39eccf | -12.86799 | -43.79496 | 2026-05-10 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7398b98-b363-3609-bbf1-26dec397125e | -12.84885 | -43.75584 | 2026-05-10 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b3c657e-c1b0-3d8e-b720-0a141aad0c02 | -13.05072 | -43.86372 | 2026-05-10 03:38:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 704059ab-5251-3ac0-894b-57700a7cd872 | -11.77732 | -43.6571 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80d5212b-292b-3945-81ca-cc844699421a | -11.77614 | -43.66336 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77cd9773-a5b4-335c-a99a-93bbfb4cc824 | -12.84769 | -43.76199 | 2026-05-10 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 307843bd-e4f0-3ea6-a843-494428da4f1f | -11.75319 | -43.64299 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c498dfa7-b7d1-33b7-a2be-215cab83dca4 | -11.76872 | -43.64581 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d15ec76-f1c1-301b-9508-8eb54799127b | -14.8361 | -40.84465 | 2026-05-10 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8f442fda-b701-3826-9a45-30ef91c06330 | -8.73173 | -47.9884 | 2026-05-10 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf39801b-50e7-3e54-a008-aa7c79d4b686 | -11.76813 | -43.64896 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d883145e-3a3b-301a-8649-f9e8addb66ec | -8.72611 | -47.97969 | 2026-05-10 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2b2ebd8-91e6-32c1-8ad7-6a043abfdec8 | -14.15245 | -45.42546 | 2026-05-10 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc34dde9-411d-3514-9202-51a3c950a683 | -11.84819 | -43.9682 | 2026-05-10 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
